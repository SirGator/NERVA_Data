# M10-D – Rekurrente Beiträge kontrolliert blockieren

Diagnose auf denselben 20 bekannten M9-Seeds, keine unabhängige Bestätigung.

Feste Trainingscheckpoint-Ausleser; Blockade erst nach identischer Baseline. Keine neue Lernregel und kein Refit.

## Gekoppelt trainiert

| Variante | Sofort: Einzelantwort | Sofort: Paar-Rangfolge | Spikes/Aktion | Nach Ruhe: Einzelantwort | Nach Ruhe: Paar-Rangfolge | Spikes/Aktion |
|---|---:|---:|---:|---:|---:|---:|
| Referenz | 51.25% | 42.50% | 17.200 | 50.00% | 45.00% | 15.425 |
| Ohne rekurrente Erregung | 48.75% | 47.50% | 3.000 | 48.75% | 47.50% | 3.000 |
| Ohne rekurrente Hemmung | 47.50% | 40.00% | 31.950 | 50.00% | 45.00% | 31.850 |
| Ohne beide | 48.75% | 47.50% | 3.000 | 48.75% | 47.50% | 3.000 |

## Kontrollarme: Paar-Rangfolge sofort / nach Ruhe

| Variante | Vor Training | Gealtert eingefroren | Gekoppelt | Entkoppelt |
|---|---:|---:|---:|---:|
| Referenz | 50.00% / 50.00% | 55.00% / 50.00% | 42.50% / 45.00% | 50.00% / 50.00% |
| Ohne rekurrente Erregung | 50.00% / 50.00% | 50.00% / 50.00% | 47.50% / 47.50% | 50.00% / 50.00% |
| Ohne rekurrente Hemmung | 50.00% / 50.00% | 57.50% / 50.00% | 40.00% / 45.00% | 50.00% / 50.00% |
| Ohne beide | 50.00% / 50.00% | 50.00% / 50.00% | 47.50% / 47.50% | 50.00% / 50.00% |

Paar-Rangfolge nutzt beide A-/D-Antworten und deren bekannte Balance. Sie ist keine neue einzelne Vorhersage oder autonom gelernte Handlung.

Die vollständigen Tabellen enthalten aktive Zellen, höchste Spikezahl je Zelle, ursprüngliche Vorhersagen und die Unterschiede zu Sham. Mehr Aktivität allein zählt nicht als Erfolg.

Alle Originalergebnisse und sechs historischen CSVs sind reproduziert. Gesperrte Kanten liefern im Aktionsfenster keine Ankünfte; Aktionskopien bleiben erhalten.

Motor-Rückkopplung und andere nicht-Core→Core-Signalwege bleiben auch bei Blockade beider rekurrenter Anteile aktiv.

[Einzelpaare](pairs.csv) · [Deskriptive seed-gepaarte Kontraste](contrasts.csv) · [Audit](diagnostics.json).
