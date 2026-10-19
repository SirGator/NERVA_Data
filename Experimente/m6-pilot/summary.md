# NERVA M6 – gemessene Ergebnisse

Stufe: pilot; Seeds: [0, 1, 2].

A: Einzelkopie/Sensor-Homöostase an; B: drei Kopien/an; C: Einzelkopie/aus; D: drei Kopien/aus. Core-Homöostase bleibt an. Alle Varianten: Kopiegewicht 0,9, Core-Tau 20 ms, Wirkungsabstand 50 ms.

Kalibrierung läuft ausschließlich auf exakten Replayzweigen. Die laufende Elterninstanz startet ohne Kalibrierzeit am Trainingsendzustand. Checkpoint prüft A und D aus demselben Zustand separat (zwei Beispiele pro Belegung/Seed).

| Fall | Seeds | Checkpoint | Online sofort | Erste 16 | Nach Ruhe | Nach Interferenz | Visuelle Auslesbarkeit | Sensorweiterleitung | Belegungswechsel / beide richtig |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| diag_A | 3 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 97.0% | 0.0% / 0.0% |
| diag_B | 3 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 97.0% | 0.0% / 0.0% |
| diag_C | 3 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 100.0% | 0.0% / 0.0% |
| diag_D | 3 | 50.0% | 50.0% | 50.0% | 50.0% | 50.0% | 100.0% | 100.0% | 0.0% / 0.0% |
| pixels_A | 3 | 50.0% | 49.1% | 49.0% | 49.3% | 50.3% | 100.0% | 57.3% | 10.2% / 4.2% |
| pixels_B | 3 | 50.0% | 52.7% | 53.1% | 52.5% | 52.6% | 100.0% | 57.3% | 8.6% / 7.0% |
| pixels_C | 3 | 50.0% | 50.1% | 50.0% | 49.7% | 49.9% | 100.0% | 100.0% | 0.3% / 0.3% |
| pixels_D | 3 | 50.0% | 50.0% | 50.0% | 49.9% | 50.1% | 100.0% | 100.0% | 0.0% / 0.0% |

checkpoint_probe – bestätigte Kriterien: keine.

probe – bestätigte Kriterien: keine.

retained_probe – bestätigte Kriterien: keine.

interference_probe – bestätigte Kriterien: keine.

[Alle gepaarten Vorhersagekontraste](prediction-contrasts.csv) · [Faktorielle Kontraste und unabhängiger Datenaudit](diagnostics.json).

Intervalle sind deskriptive Bootstrap-Intervalle über Seeds, ohne Korrektur für multiple Vergleiche. Spikezahlen, Aktionsunterscheidung und visuelle Auslesbarkeit allein sind kein Lernnachweis. Die erste Prognose liegt 100 ms nach dem Checkpoint; noch kürzere Zustände sind nicht ausgeschlossen.
