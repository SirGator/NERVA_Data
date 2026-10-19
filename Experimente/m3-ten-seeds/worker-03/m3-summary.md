# M3: bekannte Aktion vor dem Wirkungsbild

1 Seeds, 128 ausgeglichene Trainingstrials pro Modell. M3-Kriterien erfüllt: **false**.

| Dynamik | Belegung | Merkmale | Vor Training | Gleich alt, eingefroren | Gekoppelt gelernt | Zuordnung im Training zerstört |
|---|---|---|---:|---:|---:|---:|
| baseline | normal | Zählung | 60.9% | 48.4% | 53.1% | 46.9% |
| baseline | normal | 1-ms-Bins bei Standardphase | 54.7% | 50.0% | 42.2% | 46.9% |
| baseline | reversed | Zählung | 43.8% | 48.4% | 50.0% | 46.9% |
| baseline | reversed | 1-ms-Bins bei Standardphase | 40.6% | 57.8% | 60.9% | 50.0% |
| reduced_motor_drive | normal | Zählung | 56.2% | 53.1% | 45.3% | 50.0% |
| reduced_motor_drive | normal | 1-ms-Bins bei Standardphase | 57.8% | 40.6% | 56.2% | 32.8% |
| reduced_motor_drive | reversed | Zählung | 37.5% | 53.1% | 45.3% | 51.6% |
| reduced_motor_drive | reversed | 1-ms-Bins bei Standardphase | 53.1% | 57.8% | 53.1% | 65.6% |

Primäre Auswerter wurden ausschließlich auf visuellen Wirkungszuständen kalibriert. Die Vorhersage entsteht nach bekannter Aktion und vor dem neuen Bild. Zufallsniveau: 50 %. Eingefrorene Parameter werden erhalten.

[Messwerte](m3.json), [Zeitfolge und Vorhersagen](m3-trials.csv), [Core-Spikes](m3-spikes.csv), [Motor-Parameterscan](motor-scan.csv).
