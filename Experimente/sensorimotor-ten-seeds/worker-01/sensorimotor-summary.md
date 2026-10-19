# Motorische Kontrolle und Wirkungslernen

1 Seeds. Isolierte Motorprüfung: **true** (8 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 36.1% | 46/46 | 18/64 | 17.9% |
| count_then_first_spike | 100.0% | 46/46 | 48/64 | 49.7% |
| inhibitory_competition | 44.4% | 40/40 | 24/64 | 31.7% |
| random_tie_control | 100.0% | 46/46 | 57/64 | 62.0% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
