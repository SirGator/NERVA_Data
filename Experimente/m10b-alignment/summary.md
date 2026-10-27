# M10-B – Wirkungsausrichtung und gemeinsamer Decoderbias

Retrospektive Diagnose vorhandener M9-Antworten. Kein neuer neuronaler Lauf, kein neu trainierter Ausleser, kein unabhängiger Lernnachweis.

Die Paar-Rangfolge nutzt beide A-/D-Antworten und die bekannte Balance. Sie ist keine einzelne Handlungswirkungsvorhersage.

| Bedingung, gekoppelter Arm | Sofort: Einzelantwort | Sofort: Paar-Rangfolge | Nach Ruhe: Einzelantwort | Nach Ruhe: Paar-Rangfolge |
|---|---:|---:|---:|---:|
| reference | 48.75% | 51.25% | 48.75% | 51.25% |
| weight4 | 50.00% | 47.50% | 51.25% | 47.50% |
| tau100 | 48.75% | 51.25% | 48.75% | 51.25% |
| weight4_tau100 | 51.25% | 42.50% | 50.00% | 45.00% |

## Kombination: Ausrichtung und ursprüngliche Gleichklassifikation

| Zeitpunkt | Paare | Richtige Richtung, aber gleiche Klasse | Richtige Richtung insgesamt | Falsche Richtung | Projektionsgleichstand |
|---|---:|---:|---:|---:|---:|
| checkpoint_probe | 40 | 14 | 17 | 23 | 0 |
| rest_checkpoint_probe | 40 | 16 | 18 | 22 | 0 |

## Kontrollen der Paar-Rangfolge, Kombination

| Arm/Eingriff | Sofort | Nach Ruhe |
|---|---:|---:|
| before/sham | 50.00% | 50.00% |
| aged_frozen/sham | 55.00% | 50.00% |
| paired/sham | 42.50% | 45.00% |
| scrambled/sham | 50.00% | 50.00% |
| paired/restore_core | 40.00% | 45.00% |
| paired/restore_all_plastic | 40.00% | 45.00% |

Die Zentrierung entfernt einen gemeinsamen A-/D-Projektionsoffset. Richtige Richtung trotz gleicher Klasse diagnostiziert einen Schwellen-/Biasbeitrag; falsche Richtung oder Gleichstand wird dadurch nicht behoben.

[Alle Paare und Projektionen](pairs.csv) · [Seed-gepaarte deskriptive Kontraste](contrasts.csv) · [Audit](diagnostics.json).

Intervalle sind deskriptiv. Dieselben bereits untersuchten Seeds werden wiederverwendet; daraus wird kein neuer Lernnachweis abgeleitet.
