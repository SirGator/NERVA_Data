# M10-E – Core-Gewichte und Rekurrenz gekreuzt

Technischer Pilot.

Gewichtsreset und Sperre erst nach identischer Baseline; feste Ausleser. Nicht gesperrte unterwegs befindliche Eingänge behalten ihre Emissionsamplitude.

## Gekoppelter Arm, trainiert / zurückgesetzt

| Sperre | Sofort: Einzelvorhersage | Nach Ruhe: Einzelvorhersage | Sofort: Paar-Rangfolge | Nach Ruhe: Paar-Rangfolge |
|---|---:|---:|---:|---:|
| sham | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% |
| block_exc | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% |
| block_inh | 50.00% / 50.00% | 50.00% / 50.00% | 100.00% / 100.00% | 100.00% / 100.00% |
| block_both | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% | 50.00% / 50.00% |

## Änderungen durch Core-Rücksetzung im gekoppelten Arm

| Zeitpunkt / Sperre | Fenster | Anderes Spikezählmuster | Andere Ereignisse | Andere Vorhersage | Anderes Restpotenzial |
|---|---:|---:|---:|---:|---:|
| checkpoint_probe / sham | 4 | 0 | 0 | 0 | 4 |
| checkpoint_probe / block_exc | 4 | 0 | 0 | 0 | 0 |
| checkpoint_probe / block_inh | 4 | 0 | 0 | 0 | 4 |
| checkpoint_probe / block_both | 4 | 0 | 0 | 0 | 0 |
| rest_checkpoint_probe / sham | 4 | 0 | 0 | 0 | 4 |
| rest_checkpoint_probe / block_exc | 4 | 0 | 0 | 0 | 0 |
| rest_checkpoint_probe / block_inh | 4 | 0 | 0 | 0 | 4 |
| rest_checkpoint_probe / block_both | 4 | 0 | 0 | 0 | 0 |

Die Paar-Rangfolge nutzt beide Antworten und ihre bekannte Balance, keine neue einzelne Wirkungsvorhersage. Mehr Aktivität und Gewichtseinfluss allein sind kein Lernerfolg.

Alle vier trainierten Zweige reproduzieren M10-D. Rücksetzungszweige unterscheiden sich methodisch von den früheren Rücksetzungen vor der Baseline.

[Alle Paare und Kontrollarme](pairs.csv) · [Gewichtseffekte](weight-effects.csv) · [Seed-gepaarte Kontraste und Wechselwirkungen](contrasts.csv) · [Audit](diagnostics.json).
