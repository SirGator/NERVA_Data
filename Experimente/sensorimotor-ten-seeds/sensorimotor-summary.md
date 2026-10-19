# Motorische Kontrolle und Wirkungslernen

10 Seeds. Isolierte Motorprüfung: **true** (80 Fälle).

| Variante | Auswahl bei gleichem Replay | Zeitlich verschiedene Zählgleichstände | Eigene sichtbare Bewegung nach Training | Core-Vorhersage, balanciert |
|---|---:|---:|---:|---:|
| count | 36.4% | 458/458 | 210/640 | 31.7% |
| count_then_first_spike | 95.0% | 458/458 | 545/640 | 36.1% |
| inhibitory_competition | 54.6% | 327/327 | 308/640 | 36.3% |
| random_tie_control | 100.0% | 458/458 | 560/640 | 47.1% |

Kontrollierte Lernkriterien erfüllt: **false**. Die externe Vorhersage ist kein Nachweis von Motivation oder kausalem Verständnis. Zufälliger Tie-Break ist ausschließlich eine Kontrollvariante.

[Messwerte](sensorimotor.json), [Motorfenster](motor-windows.csv), [Spikezeiten](motor-spikes.csv), [Aktuatorprüfung](motor-actuator.csv), [Core-Spikes](effect-core.csv), [Bild-/Aktionsfolgen](effect-streams.csv).
