# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 53.1% | 45.3% | 43.8% | 56.2% |
| baseline | normal | 1-ms-Bins bei Standardphase | 62.5% | 45.3% | 51.6% | 54.7% |
| baseline | reversed | Zählung | 48.4% | 45.3% | 40.6% | 43.8% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 32.8% | 59.4% | 57.8% | 40.6% |
| reduced_motor_drive | normal | Zählung | 60.9% | 50.0% | 53.1% | 60.9% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 59.4% | 53.1% | 54.7% | 50.0% |
| reduced_motor_drive | reversed | Zählung | 48.4% | 50.0% | 57.8% | 53.1% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 42.2% | 46.9% | 53.1% | 45.3% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
