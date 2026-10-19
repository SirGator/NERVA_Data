# Motorische Kontrolle und Wirkungslernen

1 Seeds. Isolierte Motorprüfung: **true** (8 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 36.1% | 46/46 | 24/64 | 41.4% |
| count_then_first_spike | 90.3% | 46/46 | 60/64 | 45.7% |
| inhibitory_competition | 61.1% | 28/28 | 35/64 | 35.3% |
| random_tie_control | 100.0% | 46/46 | 62/64 | 50.0% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
