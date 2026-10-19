# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 50.0% | 46.9% | 51.6% | 60.9% |
| baseline | normal | 1-ms-Bins bei Standardphase | 50.0% | 59.4% | 54.7% | 54.7% |
| baseline | reversed | Zählung | 48.4% | 56.2% | 48.4% | 53.1% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 56.2% | 46.9% | 42.2% | 45.3% |
| reduced_motor_drive | normal | Zählung | 53.1% | 50.0% | 53.1% | 57.8% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 53.1% | 59.4% | 48.4% | 53.1% |
| reduced_motor_drive | reversed | Zählung | 46.9% | 50.0% | 50.0% | 46.9% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 51.6% | 46.9% | 45.3% | 50.0% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
