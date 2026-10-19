# NERVA M5 – gemessene Ergebnisse

Stufe: pilot; Seeds: [0, 1, 2].

A prüft eine Signalvoraussetzung, kein Wirkungslernen. Jede Bedingung hat drei Aktionskopien bei 1/10.001/20.001 µs und denselben 50-ms-Stichtag.

| Kopie-Gewicht | Core-Tau | Seeds mit beiden Signalkriterien | Core-Spikes pro Aktion | Ankünfte auf plastischen Core-Kanten | Core-Gewichtsupdates |
|---:|---:|---:|---:|---:|---:|
| 0.45 | 5 ms | 0/3 | 0.00 | 0.00 | 0.00 |
| 0.45 | 20 ms | 0/3 | 0.00 | 0.00 | 0.00 |
| 0.45 | 50 ms | 0/3 | 0.00 | 0.00 | 0.00 |
| 0.9 | 5 ms | 0/3 | 0.00 | 0.00 | 0.00 |
| 0.9 | 20 ms | 3/3 | 3.00 | 12.00 | 0.50 |
| 0.9 | 50 ms | 3/3 | 3.00 | 12.00 | 0.50 |
| 1.8 | 5 ms | 3/3 | 9.00 | 36.00 | 2.50 |
| 1.8 | 20 ms | 3/3 | 9.00 | 36.00 | 2.50 |
| 1.8 | 50 ms | 3/3 | 9.50 | 38.00 | 3.50 |
| 3.6 | 5 ms | 3/3 | 9.00 | 36.00 | 2.50 |
| 3.6 | 20 ms | 3/3 | 9.00 | 36.00 | 2.50 |
| 3.6 | 50 ms | 3/3 | 9.50 | 38.00 | 3.50 |

B verwendet denselben Anfangszustand und dieselben Streams in allen Bereichen. Die erste Vorhersageprobe folgt nach 20,48 s visueller Kalibrierung.

| Homöostase | Vorhersage | Visuelle Auslesbarkeit | Sensor-Neuron-Emissionen / Eingangsspikes | Sensorstrom je Core/s | Nach Ruhe | Nach Interferenz |
|---|---:|---:|---:|---:|---:|---:|---:|
| none | 52.3% | 91.9% | 1.0000 | 9.656 | 52.9% | 51.8% |
| core | 53.1% | 85.7% | 1.0000 | 9.666 | 50.9% | 49.9% |
| core_sensor | 48.7% | 56.5% | 0.5732 | 5.402 | 49.9% | 47.9% |
| all | 48.7% | 56.5% | 0.5732 | 5.402 | 49.9% | 47.9% |

Gepaarte Intervalle: [diagnostics.json](diagnostics.json). Alle Vorhersagekontraste je Belegung, Zeitpunkt und Auswerter: [prediction-contrasts.csv](prediction-contrasts.csv).

Bestätigte Vorhersagekriterien: keine.

Bootstrap-Einheit ist der Seed. Intervalle sind deskriptiv, ohne Korrektur für multiple Vergleiche. Motoraktivität, Plastizität und Vorhersagequalität bleiben getrennte Endpunkte.
