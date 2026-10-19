# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 43.8% | 50.0% | 48.4% | 48.4% |
| baseline | normal | 1-ms-Bins bei Standardphase | 54.7% | 65.6% | 50.0% | 50.0% |
| baseline | reversed | Zählung | 57.8% | 50.0% | 56.2% | 42.2% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 51.6% | 57.8% | 53.1% | 39.1% |
| reduced_motor_drive | normal | Zählung | 46.9% | 51.6% | 46.9% | 53.1% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 51.6% | 57.8% | 56.2% | 59.4% |
| reduced_motor_drive | reversed | Zählung | 51.6% | 50.0% | 46.9% | 48.4% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 50.0% | 48.4% | 46.9% | 53.1% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
