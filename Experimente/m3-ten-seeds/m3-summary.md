# M3: bekannte Aktion vor dem Wirkungsbild

10 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 48.4% | 51.2% | 51.6% | 52.2% |
| baseline | normal | 1-ms-Bins bei Standardphase | 51.1% | 51.9% | 49.8% | 51.7% |
| baseline | reversed | Zählung | 50.9% | 48.8% | 47.7% | 49.8% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 45.8% | 53.1% | 51.9% | 47.7% |
| reduced_motor_drive | normal | Zählung | 50.2% | 51.2% | 49.7% | 51.4% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 51.2% | 51.7% | 51.9% | 50.5% |
| reduced_motor_drive | reversed | Zählung | 48.8% | 50.3% | 50.3% | 51.2% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 49.1% | 47.0% | 51.9% | 52.0% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
