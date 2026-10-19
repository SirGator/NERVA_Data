# NERVA M5 – gemessene Ergebnisse

Stufe: confirm; Seeds: [200, 201, 202, 203, 204, 205, 206, 207, 208, 209].

A prüft eine Signalvoraussetzung, kein Wirkungslernen. Jede Bedingung hat drei Aktionskopien bei 1/10.001/20.001 µs und denselben 50-ms-Stichtag.

| Kopie-Gewicht | Core-Tau | Seeds mit beiden Signalkriterien | Core-Spikes pro Aktion | Ankünfte auf plastischen Core-Kanten | Core-Gewichtsupdates |
|---:|---:|---:|---:|---:|---:|
| 0.45 | 5 ms | 0/10 | 0.00 | 0.00 | 0.00 |
| 0.45 | 20 ms | 0/10 | 0.00 | 0.00 | 0.00 |
| 0.45 | 50 ms | 0/10 | 0.00 | 0.00 | 0.00 |
| 0.9 | 5 ms | 0/10 | 0.00 | 0.00 | 0.00 |
| 0.9 | 20 ms | 10/10 | 3.00 | 12.00 | 0.55 |
| 0.9 | 50 ms | 10/10 | 3.00 | 12.00 | 0.55 |
| 1.8 | 5 ms | 10/10 | 9.00 | 36.00 | 2.75 |
| 1.8 | 20 ms | 10/10 | 9.10 | 36.40 | 3.50 |
| 1.8 | 50 ms | 10/10 | 9.90 | 39.60 | 5.80 |
| 3.6 | 5 ms | 10/10 | 9.00 | 36.00 | 2.75 |
| 3.6 | 20 ms | 10/10 | 9.10 | 36.40 | 3.50 |
| 3.6 | 50 ms | 10/10 | 9.90 | 39.60 | 5.80 |

B verwendet denselben Anfangszustand und dieselben Streams in allen Bereichen. Die erste Vorhersageprobe folgt nach 20,48 s visueller Kalibrierung.

| Homöostase | Vorhersage | Visuelle Auslesbarkeit | Sensor-Neuron-Emissionen / Eingangsspikes | Sensorstrom je Core/s | Nach Ruhe | Nach Interferenz |
|---|---:|---:|---:|---:|---:|---:|---:|
| none | 51.1% | 87.7% | 1.0000 | 9.647 | 49.6% | 50.5% |
| core | 48.4% | 82.7% | 1.0000 | 9.649 | 49.5% | 49.4% |
| core_sensor | 47.6% | 53.0% | 0.5731 | 5.419 | 50.0% | 49.2% |
| all | 47.0% | 52.8% | 0.5731 | 5.419 | 49.1% | 48.5% |

Gepaarte Intervalle: [diagnostics.json](diagnostics.json). Alle Vorhersagekontraste je Belegung, Zeitpunkt und Auswerter: [prediction-contrasts.csv](prediction-contrasts.csv).

Bestätigte Vorhersagekriterien: keine.

Bootstrap-Einheit ist der Seed. Intervalle sind deskriptiv, ohne Korrektur für multiple Vergleiche. Motoraktivität, Plastizität und Vorhersagequalität bleiben getrennte Endpunkte.
