# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 53.1% | 51.6% | 54.7% | 46.9% |
| baseline | normal | 1-ms-Bins bei Standardphase | 53.1% | 62.5% | 40.6% | 50.0% |
| baseline | reversed | Zählung | 46.9% | 51.6% | 39.1% | 57.8% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 51.6% | 39.1% | 50.0% | 46.9% |
| reduced_motor_drive | normal | Zählung | 54.7% | 45.3% | 43.8% | 42.2% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 59.4% | 60.9% | 65.6% | 45.3% |
| reduced_motor_drive | reversed | Zählung | 48.4% | 46.9% | 48.4% | 51.6% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 39.1% | 37.5% | 59.4% | 42.2% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
