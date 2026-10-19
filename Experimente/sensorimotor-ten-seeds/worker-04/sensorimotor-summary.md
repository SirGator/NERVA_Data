# Motorische Kontrolle und Wirkungslernen

1 Seeds. Isolierte Motorprüfung: **true** (8 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 33.3% | 48/48 | 20/64 | 34.4% |
| count_then_first_spike | 94.4% | 48/48 | 51/64 | 35.4% |
| inhibitory_competition | 58.3% | 30/30 | 31/64 | 40.7% |
| random_tie_control | 100.0% | 48/48 | 61/64 | 39.0% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
