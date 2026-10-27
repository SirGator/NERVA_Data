# M10-E – Core-Gewichte und Rekurrenz gekreuzt

Diagnose auf denselben 20 bekannten Seeds, keine unabhängige Bestätigung.

Gewichtsreset und Sperre erst nach identischer Baseline; feste Ausleser. Nicht gesperrte unterwegs befindliche Eingänge behalten ihre Emissionsamplitude.

## Gekoppelter Arm, trainiert / zurückgesetzt

| Sperre | Sofort: Einzelvorhersage | Nach Ruhe: Einzelvorhersage | Sofort: Paar-Rangfolge | Nach Ruhe: Paar-Rangfolge |
|---|---:|---:|---:|---:|
| sham | 51.25% / 51.25% | 50.00% / 51.25% | 42.50% / 40.00% | 45.00% / 45.00% |
| block_exc | 48.75% / 48.75% | 48.75% / 48.75% | 47.50% / 47.50% | 47.50% / 47.50% |
| block_inh | 47.50% / 45.00% | 50.00% / 51.25% | 40.00% / 45.00% | 45.00% / 50.00% |
| block_both | 48.75% / 48.75% | 48.75% / 48.75% | 47.50% / 47.50% | 47.50% / 47.50% |

## Änderungen durch Core-Rücksetzung im gekoppelten Arm

| Zeitpunkt / Sperre | Fenster | Anderes Spikezählmuster | Andere Ereignisse | Andere Vorhersage | Anderes Restpotenzial |
|---|---:|---:|---:|---:|---:|
| checkpoint_probe / sham | 80 | 30 | 42 | 4 | 80 |
| checkpoint_probe / block_exc | 80 | 0 | 0 | 0 | 0 |
| checkpoint_probe / block_inh | 80 | 31 | 43 | 6 | 80 |
| checkpoint_probe / block_both | 80 | 0 | 0 | 0 | 0 |
| rest_checkpoint_probe / sham | 80 | 31 | 42 | 1 | 80 |
| rest_checkpoint_probe / block_exc | 80 | 0 | 0 | 0 | 0 |
| rest_checkpoint_probe / block_inh | 80 | 34 | 43 | 7 | 80 |
| rest_checkpoint_probe / block_both | 80 | 0 | 0 | 0 | 0 |

Die Paar-Rangfolge nutzt beide Antworten und ihre bekannte Balance, keine neue einzelne Wirkungsvorhersage. Mehr Aktivität und Gewichtseinfluss allein sind kein Lernerfolg.

Alle vier trainierten Zweige reproduzieren M10-D. Rücksetzungszweige unterscheiden sich methodisch von den früheren Rücksetzungen vor der Baseline.

[Alle Paare und Kontrollarme](pairs.csv) · [Gewichtseffekte](weight-effects.csv) · [Seed-gepaarte Kontraste und Wechselwirkungen](contrasts.csv) · [Audit](diagnostics.json).
