# M8 – gemessene Ergebnisse

Stufe pilot; Seeds [500, 501, 502]. Alle Bedingungen verwenden bestehende Lernregeln und dieselben vier Kontrollarme.

| Fall | Sofort-Checkpoint | Checkpoint nach 2s Ruhe | Online | Visuell | Extra-Spikes sofort / ohne Kopie | Extra-Spikes nach Ruhe / ohne Kopie |
|---|---:|---:|---:|---:|---:|---:|
| reference | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| a_weight2 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| a_weight4 | 50.0% | 50.0% | 50.0% | 100.0% | 21.33 / 0.00 | 21.33 / 0.00 |
| b_threshold08 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| b_threshold06 | 50.0% | 50.0% | 50.0% | 100.0% | 0.17 / 0.00 | 0.00 / 0.00 |
| c_tau50 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| c_tau100 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| d_delay500 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| d_delay5000 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| e_fanout8 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| e_fanout12 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| f_visual05 | 58.3% | 58.3% | 58.3% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| f_visual15 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |

checkpoint_probe – Kriterien einschließlich Familienkorrektur: keine.

rest_checkpoint_probe – Kriterien einschließlich Familienkorrektur: keine.

[Kontroll-/Belegungskontraste](prediction-contrasts.csv) · [Weiterleitung und Kontrollarme](propagation-summary.csv) · [Gewichtsdiagnose](weight-summary.csv) · [Unabhängiger Datenaudit](diagnostics.json).

Spikezahlen außerhalb der direkten Kopie-Zielzellen sind getrennt von der Vorhersageleistung zu bewerten. Prüfzeitpunkte sind getrennte Endpunkte; 95%-Bootstrapintervalle sind deskriptiv. Primär wird zusätzlich jeder gerichtete Kontrollkontrast durch einen exakten gepaarten Vorzeichentest mit Bonferroni über 13×2 Endpunkte geprüft.
