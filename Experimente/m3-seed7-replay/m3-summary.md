# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 51.6% | 54.7% | 43.8% | 53.1% |
| baseline | normal | 1-ms-Bins bei Standardphase | 56.2% | 39.1% | 53.1% | 51.6% |
| baseline | reversed | Zählung | 48.4% | 46.9% | 56.2% | 40.6% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 35.9% | 65.6% | 45.3% | 46.9% |
| reduced_motor_drive | normal | Zählung | 48.4% | 53.1% | 46.9% | 48.4% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 56.2% | 43.8% | 59.4% | 43.8% |
| reduced_motor_drive | reversed | Zählung | 46.9% | 40.6% | 46.9% | 54.7% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 34.4% | 42.2% | 48.4% | 48.4% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
