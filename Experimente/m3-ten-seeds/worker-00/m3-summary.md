# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 46.9% | 57.8% | 51.6% | 57.8% |
| baseline | normal | 1-ms-Bins bei Standardphase | 39.1% | 39.1% | 43.8% | 51.6% |
| baseline | reversed | Zählung | 53.1% | 56.2% | 50.0% | 54.7% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 51.6% | 50.0% | 48.4% | 48.4% |
| reduced_motor_drive | normal | Zählung | 43.8% | 48.4% | 50.0% | 53.1% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 37.5% | 57.8% | 43.8% | 59.4% |
| reduced_motor_drive | reversed | Zählung | 53.1% | 54.7% | 57.8% | 50.0% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 65.6% | 46.9% | 62.5% | 51.6% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
