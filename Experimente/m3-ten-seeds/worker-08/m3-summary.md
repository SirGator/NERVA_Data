# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 40.6% | 53.1% | 50.0% | 50.0% |
| baseline | normal | 1-ms-Bins bei Standardphase | 45.3% | 56.2% | 59.4% | 59.4% |
| baseline | reversed | Zählung | 53.1% | 45.3% | 45.3% | 54.7% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 46.9% | 59.4% | 54.7% | 53.1% |
| reduced_motor_drive | normal | Zählung | 48.4% | 53.1% | 51.6% | 43.8% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 46.9% | 35.9% | 46.9% | 59.4% |
| reduced_motor_drive | reversed | Zählung | 46.9% | 60.9% | 60.9% | 59.4% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 45.3% | 46.9% | 56.2% | 45.3% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
