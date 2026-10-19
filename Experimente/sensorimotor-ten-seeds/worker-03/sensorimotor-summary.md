# Motorische Kontrolle und Wirkungslernen

1 Seeds. Isolierte Motorprüfung: **true** (8 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 36.1% | 46/46 | 17/64 | 18.1% |
| count_then_first_spike | 97.2% | 46/46 | 58/64 | 32.2% |
| inhibitory_competition | 52.8% | 34/34 | 22/64 | 30.6% |
| random_tie_control | 100.0% | 46/46 | 51/64 | 68.4% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
