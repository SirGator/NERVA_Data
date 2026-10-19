# M8 kompakt: Vorhersage und Weiterleitung

Bestätigungsreihe mit Seeds 510–519, gekoppelt trainierter Arm, Mittelwerte über
zehn Seeds und beide Belegungen. Zufallsniveau der binären Vorhersage: 50 %.

**Keine der 13 Bedingungen erfüllt die primären Lernkriterien.** Vierfache
Core-Gewichte führen zu mehr Spikes außerhalb der direkt angeregten Zielzellen,
aber ohne abgesicherten funktionalen Vorhersagevorteil.

| Bedingung | Vorhersage sofort | Nach unabhängigen 2 s Ruhe | Online | Extra-Spikes sofort | Extra-Spikes nach Ruhe |
|---|---:|---:|---:|---:|---:|
| Referenz | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |
| Core-Gewichte ×2 | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |
| Core-Gewichte ×4 | 50,0 % | 50,0 % | 50,6 % | 19,48 | 19,05 |
| Schwelle 0,8 | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |
| Schwelle 0,6 | 50,0 % | 52,5 % | 51,7 % | 0,12 | 0,00 |
| STDP-Tau 50 ms | 47,5 % | 47,5 % | 47,5 % | 0,00 | 0,00 |
| STDP-Tau 100 ms | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |
| Core-Verzögerung 0,5 ms | 52,5 % | 52,5 % | 52,5 % | 0,00 | 0,00 |
| Core-Verzögerung 5 ms | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |
| Fan-out höchstens 8 | 47,5 % | 47,5 % | 47,5 % | 0,00 | 0,00 |
| Fan-out höchstens 12 | 47,5 % | 47,5 % | 47,5 % | 0,00 | 0,00 |
| Visuelle Gewichte ×0,5 | 47,5 % | 47,5 % | 47,5 % | 0,00 | 0,00 |
| Visuelle Gewichte ×1,5 | 50,0 % | 50,0 % | 50,0 % | 0,00 | 0,00 |

Extra-Spikes liegen außerhalb der drei direkt von der betreffenden Aktionskopie
angeregten Core-Zellen. Die entsprechende Kontrolle ohne Aktionskopie hat in allen
hier gezeigten Bedingungen an beiden Zeitpunkten null Extra-Spikes. Die visuelle
Auslesbarkeit beträgt jeweils 100 %. Die Zahl zusätzlicher Spikes ist keine
Genauigkeit und kein eigenständiger Lernnachweis.

Automatisch tabelliert aus den unveränderten Originaldateien
[summary.csv](../Experimente/m8-confirm/summary.csv) und
[propagation-summary.csv](../Experimente/m8-confirm/propagation-summary.csv).
Rundung: eine Nachkommastelle bei Prozenten, zwei bei Spike-Mittelwerten.

[Vollständiger wissenschaftlicher Bericht](../M8_EXPERIMENT.md) ·
[Kontrollkontraste](../Experimente/m8-confirm/prediction-contrasts.csv) ·
[Methodik](../METHODIK.md) · [Startseite](../README.md).
