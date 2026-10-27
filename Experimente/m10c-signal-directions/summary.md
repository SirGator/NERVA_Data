# M10-C – Signalbeiträge entlang fester Auslesergewichte

Retrospektive algebraische Diagnose aufgezeichneter M10-Trajektorien, keine neue Simulation und kein Lernnachweis.

Eingänge und Potenziale werden auf die neuronale Relevanz des vorhandenen Spikezähl-Auslesers projiziert. Dies sind keine eigenständig kalibrierten Eingangs-/Potenzialklassifikatoren.

## Gekoppelter Arm, unveränderte Gewichte

| Signal | Sofort: positiv / negativ / null | Nach Ruhe: positiv / negativ / null |
|---|---:|---:|
| Alle Eingangsimpulse | 17 / 23 / 0 | 17 / 23 / 0 |
| Nach Refraktärfilter | 16 / 24 / 0 | 16 / 24 / 0 |
| Leckgewichtete Eingänge | 18 / 22 / 0 | 18 / 22 / 0 |
| Leckgewichtete angenommene Eingänge | 17 / 23 / 0 | 17 / 23 / 0 |
| Antrieb vor Resetabzug | 17 / 23 / 0 | 17 / 23 / 0 |
| Resetabzug | 18 / 22 / 0 | 18 / 22 / 0 |
| Restpotenzial nach Reset | 19 / 21 / 0 | 20 / 20 / 0 |
| Spikezählmuster / M10-B-Achse | 17 / 23 / 0 | 18 / 22 / 0 |

## Übergänge, gekoppelter Arm, unveränderte Gewichte

| Zeitpunkt / Übergang | Positiv → negativ | Negativ → positiv |
|---|---:|---:|
| checkpoint_probe: all_input → accepted_input | 1 | 0 |
| checkpoint_probe: accepted_input → accepted_leak_input | 0 | 1 |
| checkpoint_probe: accepted_leak_input → spike_counts | 1 | 1 |
| rest_checkpoint_probe: all_input → accepted_input | 1 | 0 |
| rest_checkpoint_probe: accepted_input → accepted_leak_input | 0 | 1 |
| rest_checkpoint_probe: accepted_leak_input → spike_counts | 1 | 2 |

Positive/negative Vorzeichen betreffen nur die feste Neuronengewichtung. Unterschiedliche physikalische Einheiten werden nicht als vergleichbare Stärken oder Genauigkeiten behandelt.

Das Endpotenzial ist ein Restzustand nach den beobachteten Spikes und Resets. Der Resetabzug kann seine Richtung umkehren, obwohl Spikes erzeugt wurden.

Die linearen Terme sind eine Bilanz der beobachteten wiederkehrenden Eingänge, keine Resimulation eines Netzwerks ohne Reset oder Hemmung.

[Signale](signals.csv) · [Quellgruppen](sources.csv) · [Synaptische Einzelbeiträge](edges.csv) · [Übergänge](transitions.csv) · [Audit](diagnostics.json).
