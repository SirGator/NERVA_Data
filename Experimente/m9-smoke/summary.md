# M9 – gemessene Ergebnisse

Stufe smoke; Seeds [690]. Alle Bedingungen verwenden bestehende Lernregeln und dieselben vier Kontrollarme.

| Fall | Sofort-Checkpoint | Checkpoint nach 2s Ruhe | Online | Visuell | Extra-Spikes sofort / ohne Kopie | Extra-Spikes nach Ruhe / ohne Kopie |
|---|---:|---:|---:|---:|---:|---:|
| reference | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4 | 50.0% | 50.0% | 50.0% | 100.0% | 7.50 / 0.00 | 8.00 / 0.00 |
| tau100 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4_tau100 | 50.0% | 50.0% | 56.2% | 100.0% | 7.50 / 0.00 | 8.00 / 0.00 |

checkpoint_probe – Kriterien einschließlich Familienkorrektur: keine.

rest_checkpoint_probe – Kriterien einschließlich Familienkorrektur: keine.

[Kontroll-/Belegungskontraste](prediction-contrasts.csv) · [Weiterleitung und Kontrollarme](propagation-summary.csv) · [Gewichtsdiagnose](weight-summary.csv) · [Unabhängiger Datenaudit](diagnostics.json).

Spikezahlen außerhalb der direkten Kopie-Zielzellen sind getrennt von der Vorhersageleistung zu bewerten. Prüfzeitpunkte sind getrennte Endpunkte; 95%-Bootstrapintervalle sind deskriptiv. Primär wird zusätzlich jeder gerichtete Kontrollkontrast durch einen exakten gepaarten Vorzeichentest mit Bonferroni über 4×2 Endpunkte geprüft.

Technischer Kurzlauf; kein wissenschaftlicher Lernnachweis.

[Faktorielle Kontraste](factorial-contrasts.csv) sind deskriptiv; eine positive Interaktion allein belegt keinen Lernerfolg.

| Fall | Erhaltener visueller Gewichtsanteil, gekoppelt |
|---|---:|
| reference | 98.9% |
| weight4 | 98.9% |
| tau100 | 98.6% |
| weight4_tau100 | 98.5% |
