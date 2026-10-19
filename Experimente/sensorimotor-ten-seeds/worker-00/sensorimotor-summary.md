# Motorische Kontrolle und Wirkungslernen

1 Seeds. Isolierte Motorprüfung: **true** (8 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 33.3% | 48/48 | 21/64 | 51.9% |
| count_then_first_spike | 94.4% | 48/48 | 59/64 | 38.9% |
| inhibitory_competition | 59.7% | 29/29 | 30/64 | 42.8% |
| random_tie_control | 100.0% | 48/48 | 53/64 | 52.8% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
