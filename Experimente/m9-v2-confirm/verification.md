# M9-v2: Bestätigung vollständig geprüft

Abschluss am **27.10.2026**. Alle vier vorab festgelegten Bedingungen wurden auf
sämtlichen 20 neuen Seeds 610–629 ausgeführt: **80 vollständige Fälle**.
Trialzahlen 256/128/128, vier Arme und beide Belegungen unverändert.
Der [Pilot](../m9-v2-pilot/verification.md) wurde vorher abgeschlossen; anhand
seiner Ergebnisse wurden keine Fälle ausgewählt oder Parameter geändert.

## Ausführung und Softwarestand

```bash
python3 NERVA_Modell/Experimente/m9/run.py run --stage confirm --jobs 8 --output Messungen/Experimente/m9-v2-confirm
```

Die Ausführung nutzte acht parallele Prozesse statt der anfangs aufgezeichneten
vier; dies ist in [execution.json](execution.json) dokumentiert. Seeds, neuronale
Parameter, Trialzahlen, Prüfkriterien und Code blieben unverändert. Die
vorausgehenden Wiederholungs- und Parallelitätstests stehen im
[Softwareprüfnachweis](../m9-v2-smoke/verification.md).

Nach Abschluss stimmen sämtliche in [provenance.json](provenance.json)
gespeicherten Quellcode- und Programmprüfsummen überein. Das Manifest blieb
gegenüber der vorab gespeicherten Planung unverändert, SHA-256:
`4d45b29c4dac556c0d3baacd45e9ac9d950dfa8800719ff59517c08dff4a4b36`.
Die wissenschaftlichen Rohdateien unter `results/` wurden nach Veröffentlichung
nicht verändert. [raw-sha256.csv](raw-sha256.csv) enthält Größe und Prüfsumme
aller 560 Rohdateien. Auswertungsdateien werden aus diesen Daten abgeleitet.

## Unabhängiger Audit

Jeder Fall wurde vor Wiederverwendung oder Aufnahme in den Bericht gegen seine
exakte Konfiguration und die CSV-Begleitdateien geprüft. Der Gesamtaudit enthält:

| Geprüfte Einträge | Anzahl |
|---|---:|
| Vollständige Fälle | 80 |
| Ursprüngliche exakte Replayzweige | 4.480 |
| Zusätzliche Gewichtsinterventionszweige | 7.680 |
| Trialzeilen | 371.200 |
| Propagationszeilen | 371.200 |
| Phasenzeilen | 2.598.400 |
| Sensorzeilen | 2.598.400 |

Der Matrixaudit bestätigt ursprüngliche Verschaltung, Geometrie und Polarität,
unveränderte erzeugte sensorische Spikezahlen und identische Referenznormierung
pro Seed. Replayzustände, eingefrorene Gewichte, Aktionskopien und Zeitgrenzen
vor dem Wirkungsbild wurden geprüft. Der Gewichtsinterventionsaudit rekonstruiert
Vorhersagen aus Decoderparametern und Spikezahlen, vergleicht unveränderte Proben
mit den ursprünglichen Checkpointantworten und prüft sämtliche Eingriffe gegen
die trainierten und bedingungsspezifischen Anfangsgewichte.

Der [Datenaudit](diagnostics.json) besteht. Keine Bedingung erfüllt die
Verhaltens- oder Gewichtskausalitätsanforderungen; auch die unkorrigierten
vollständigen Kontroll-/Belegungskriterien scheitern.

## Nachrechnen

Im vollständigen Projekt:

```bash
python3 NERVA_Modell/Experimente/m9/run.py report --output Messungen/Experimente/m9-v2-confirm
```

Zusätzliche passive Zusammenfassungen für den wissenschaftlichen Bericht lassen
sich im eigenständigen Datenpaket mit
`python3 Experimente/m9-v2-confirm/derive-report.py` erzeugen. Das Skript verwendet
die vorhandenen CSV-/JSON-Dateien und speichert [report-data.json](report-data.json);
es führt keine neuronalen Läufe und keine neue Parameterauswahl aus.

[Wissenschaftlicher Bericht](../../M9_EXPERIMENT.md) ·
[Automatisch erzeugter Bericht](summary.md) · [Vorab gespeicherter Plan](manifest.json).
