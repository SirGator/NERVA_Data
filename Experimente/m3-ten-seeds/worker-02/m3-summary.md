# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 40.6% | 51.6% | 56.2% | 53.1% |
| baseline | normal | 1-ms-Bins bei Standardphase | 45.3% | 54.7% | 53.1% | 50.0% |
| baseline | reversed | Zählung | 57.8% | 45.3% | 40.6% | 54.7% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 46.9% | 50.0% | 59.4% | 53.1% |
| reduced_motor_drive | normal | Zählung | 48.4% | 46.9% | 57.8% | 48.4% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 39.1% | 51.6% | 45.3% | 43.8% |
| reduced_motor_drive | reversed | Zählung | 59.4% | 50.0% | 42.2% | 50.0% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 48.4% | 51.6% | 56.2% | 62.5% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
