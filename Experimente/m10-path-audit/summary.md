# M10 – Signalwegdiagnose

Retrospektive Ursachenanalyse vorhandener M9-Daten; kein neuer unabhängiger Lernnachweis.
Seeds: [610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629]. Alle vier Quellbedingungen; passive Replaytraces für die Kombination.

| Bedingung, gekoppelter Arm | Aktionsproben | Spikezählmuster nach Core-Rücksetzung geändert | Vorhersagen geändert | A/D unterschiedlich aktiv, aber gleiche vorhergesagte Klasse |
|---|---:|---:|---:|---:|
| reference | 160 | 0 | 0 | 54/80 |
| weight4 | 160 | 67 | 0 | 73/80 |
| tau100 | 160 | 0 | 0 | 58/80 |
| weight4_tau100 | 160 | 61 | 5 | 71/80 |

## Passive Traces mit gemeinsamen Messzeitpunkten

| Arm, Core-Rücksetzung, Kombination | Proben | Geänderte Eingangsimpulssummen | Geänderte Potenziale am Prognosezeitpunkt | Geänderte Spikezählmuster | Geänderte Entscheidungen |
|---|---:|---:|---:|---:|---:|
| before | 160 | 0 | 0 | 0 | 0 |
| aged_frozen | 160 | 0 | 0 | 0 | 0 |
| paired | 160 | 160 | 160 | 61 | 5 |
| scrambled | 160 | 160 | 160 | 70 | 8 |

Die Beobachtung verändert weder ursprüngliche M9-Ergebnisse noch deren CSV-Dateien. Alle Replay- und Ereignisaudits bestanden.

Potenziale werden auf Neuronenkopien auf gemeinsame Phasengrenzen fortgeschrieben. Die alten gespeicherten Zustandswerte sind keine synchronen Spannungsmessungen.

Synaptische Eingänge sind signierte Ankunftsimpulse. Ihre Summe allein bestimmt wegen Leck, Hemmung und Refraktärzeiten keine Spikezahl.

Die Vergleiche diagnostizieren den festen Spikezähl-Ausleser. Gleichklassifikation beweist keine identischen neuronalen Antworten und keinen allgemeinen Informationsverlust.

[Gewichtseffekte](weight-effects.csv) · [Aktionsunterschiede](action-discrimination.csv) · [Gewichtsspeicherung](mapping-weights.csv) · [Zeitlich abgeglichene Traces](trace-effects.csv) · [Audit](diagnostics.json).
