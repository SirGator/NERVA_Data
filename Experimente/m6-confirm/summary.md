# NERVA M6 – gemessene Ergebnisse

Stufe: confirm; Seeds: [300, 301, 302, 303, 304, 305, 306, 307, 308, 309].

A: Einzelkopie/Sensor-Homöostase an; B: drei Kopien/an; C: Einzelkopie/aus; D: drei Kopien/aus. Core-Homöostase bleibt an. Alle Varianten: Kopiegewicht 0,9, Core-Tau 20 ms, Wirkungsabstand 50 ms.

Kalibrierung läuft ausschließlich auf exakten Replayzweigen. Die laufende Elterninstanz startet ohne Kalibrierzeit am Trainingsendzustand. Checkpoint prüft A und D aus demselben Zustand separat (zwei Beispiele pro Belegung/Seed).

| Fall | Seeds | Checkpoint | Online sofort | Erste 16 | Nach Ruhe | Nach Interferenz | Visuelle Auslesbarkeit | Sensorweiterleitung | Belegungswechsel / beide richtig |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| diag_A | 10 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 96.9% | 0.0% / 0.0% |
| diag_B | 10 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 96.9% | 0.0% / 0.0% |
| diag_C | 10 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 100.0% | 0.0% / 0.0% |
| diag_D | 10 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 100.0% | 0.0% / 0.0% |
| pixels_A | 10 | 50.0% | 50.8% | 51.2% | 50.7% | 52.2% | 100.0% | 57.3% | 9.1% / 5.3% |
| pixels_B | 10 | 50.0% | 50.6% | 51.2% | 50.3% | 51.9% | 100.0% | 57.3% | 7.9% / 4.5% |
| pixels_C | 10 | 50.0% | 50.2% | 49.1% | 50.0% | 50.0% | 100.0% | 100.0% | 7.8% / 4.1% |
| pixels_D | 10 | 50.0% | 50.1% | 49.4% | 49.7% | 50.0% | 100.0% | 100.0% | 7.7% / 3.9% |

checkpoint_probe – bestätigte Kriterien: keine.

probe – bestätigte Kriterien: keine.

retained_probe – bestätigte Kriterien: keine.

interference_probe – bestätigte Kriterien: keine.

[Alle gepaarten Vorhersagekontraste](prediction-contrasts.csv) · [Faktorielle Kontraste und unabhängiger Datenaudit](diagnostics.json).

Intervalle sind deskriptive Bootstrap-Intervalle über Seeds, ohne Korrektur für multiple Vergleiche. Spikezahlen, Aktionsunterscheidung und visuelle Auslesbarkeit allein sind kein Lernnachweis. Die erste Prognose liegt 100 ms nach dem Checkpoint; noch kürzere Zustände sind nicht ausgeschlossen.
