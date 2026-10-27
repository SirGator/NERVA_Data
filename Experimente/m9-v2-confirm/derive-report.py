import csv,json,statistics
from collections import Counter,defaultdict
from pathlib import Path

root=Path(__file__).resolve().parent
def rows(name):
    with (root/name).open(newline='') as f:return list(csv.DictReader(f))
summary=rows('summary.csv');prop=rows('propagation-summary.csv');weights=rows('weight-summary.csv')
predictions=rows('prediction-contrasts.csv');causal=rows('causal-contrasts.csv')
result={}
for row in summary:
    case=row['case'];w=[r for r in weights if r['case']==case and r['arm']=='paired']
    item=dict(summary=row,alignment_mean=statistics.mean(float(r['alignment']) for r in w),
              visual_retained_fraction=statistics.mean(float(r['visual_retained_fraction']) for r in w),
              propagation=[r for r in prop if r['case']==case],
              causal_required=[r for r in causal if r['case']==case and r['required_for_weight_causality']=='True'],
              primary_patterns={},arm_accuracy=defaultdict(list))
    patterns=defaultdict(Counter)
    for p in sorted((root/'results'/case).glob('*.json')):
        r=json.loads(p.read_text())
        for stage in ['checkpoint_probe','rest_checkpoint_probe']:
            for mapping in ['normal_mapping','reversed_mapping']:
                guesses=r['arms']['paired'][mapping][stage]['predictions_count']
                patterns[stage][str(guesses)]+=1
                for arm in ['before','aged_frozen','paired','scrambled']:
                    item['arm_accuracy'][stage+':'+arm].append(r['arms'][arm][mapping][stage]['count']['balanced_accuracy'])
    item['primary_patterns']={stage:dict(values) for stage,values in patterns.items()}
    item['arm_accuracy']={key:statistics.mean(values) for key,values in item['arm_accuracy'].items()}
    item['failed_required_behavioral_contrasts']={stage:sum(not(float(r['ci_low'])>0 and float(r['one_sided_sign_p'])<=.00625) for r in predictions if r['case']==case and r['stage']==stage and r['feature']!='time_bins') for stage in ['checkpoint_probe','rest_checkpoint_probe']}
    result[case]=item
(root/'report-data.json').write_text(json.dumps(result,indent=2)+'\n')
for case,item in result.items():
    row=item['summary'];print(case,{k:row[k] for k in ['checkpoint_probe','rest_checkpoint_probe','probe','visual']})
    print('  alignment',item['alignment_mean'],'visual retained',item['visual_retained_fraction'])
    print('  patterns',item['primary_patterns'])
    print('  controls',item['arm_accuracy'])
    for r in item['propagation']:
        if r['arm']=='paired':print('  propagation',r['stage'],r['mean_extra_core_spikes'],'no copy',r['mean_no_copy_extra_spikes'])
    print('  required causal',[(r['stage'],r['mapping'],r['delta'],r['one_sided_sign_p']) for r in item['causal_required']])
