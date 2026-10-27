# M10-D – Rekurrente Beiträge kontrolliert blockieren

Technischer Pilot.

Feste Trainingscheckpoint-Ausleser; Blockade erst nach identischer Baseline. Keine neue Lernregel und kein Refit.

## Gekoppelt trainiert

| Variante | Sofort: Einzelantwort | Sofort: Paar-Rangfolge | Spikes/Aktion | Nach Ruhe: Einzelantwort | Nach Ruhe: Paar-Rangfolge | Spikes/Aktion |
|---|---:|---:|---:|---:|---:|---:|
| Referenz | 50.00% | 50.00% | 15.000 | 50.00% | 50.00% | 15.000 |
| Ohne rekurrente Erregung | 50.00% | 50.00% | 3.000 | 50.00% | 50.00% | 3.000 |
| Ohne rekurrente Hemmung | 50.00% | 100.00% | 25.500 | 50.00% | 100.00% | 25.500 |
| Ohne beide | 50.00% | 50.00% | 3.000 | 50.00% | 50.00% | 3.000 |

## Kontrollarme: Paar-Rangfolge sofort / nach Ruhe

| Variante | Vor Training | Gealtert eingefroren | Gekoppelt | Entkoppelt |
|---|---:|---:|---:|---:|
| Referenz | 50.00% / 50.00% | 0.00% / 0.00% | 50.00% / 50.00% | 50.00% / 50.00% |
| Ohne rekurrente Erregung | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% |
| Ohne rekurrente Hemmung | 50.00% / 50.00% | 50.00% / 50.00% | 100.00% / 100.00% | 50.00% / 50.00% |
| Ohne beide | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% |

Paar-Rangfolge nutzt beide A-/D-Antworten und deren bekannte Balance. Sie ist keine neue einzelne Vorhersage oder autonom gelernte Handlung.

Die vollständigen Tabellen enthalten aktive Zellen, höchste Spikezahl je Zelle, ursprüngliche Vorhersagen und die Unterschiede zu Sham. Mehr Aktivität allein zählt nicht als Erfolg.

Alle Originalergebnisse und sechs historischen CSVs sind reproduziert. Gesperrte Kanten liefern im Aktionsfenster keine Ankünfte; Aktionskopien bleiben erhalten.

Motor-Rückkopplung und andere nicht-Core→Core-Signalwege bleiben auch bei Blockade beider rekurrenter Anteile aktiv.

[Einzelpaare](pairs.csv) · [Deskriptive seed-gepaarte Kontraste](contrasts.csv) · [Audit](diagnostics.json).
