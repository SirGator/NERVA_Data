# Trainieren – Einfrieren – Prüfen

1000 Trainingsframes durch zyklische Wiederholung von 40 aufgenommenen Bildern; 64 separate Prüfungsbilder.

Alle Prüfzweige behalten Gewichte, Topologie, STDP-/Utility-Zustände und homöostatische Parameter.

| Seed | Bedingung | Core-Synapsen beim Einfrieren | A/D bei gleichem Bild: L1 | Nächstes Pixel-Delta: Core | Nur aktuelles Bild | Mehrheitskontrolle |
|---|---|---:|---:|---:|---:|---:|
| 42 | before_training | 1024 | 0 | 0.469 | 0.438 | 0.062 |
| 42 | aged_frozen | 1024 | 0 | 0.438 | 0.438 | 0.062 |
| 42 | trained_fixed | 1024 | 0 | 0.438 | 0.438 | 0.062 |
| 42 | trained_development | 476 | 0 | 0.469 | 0.438 | 0.062 |

Die Werte messen eine externe Vorhersage auf den eingefrorenen Aktivitätsmustern. Sie sind keine autonome Aufgabenleistung. Neue Klassen im Test zählen als Fehler. Aktionskopien werden vertauscht, um einen Frame verzögert oder entfernt; die Bilder bleiben dabei gleich. Die A/D-Festbildkontrolle hält das erste Prüfungsbild konstant.
