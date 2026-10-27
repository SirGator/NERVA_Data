# M9 – gemessene Ergebnisse

Stufe confirm; Seeds [610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629]. Alle Bedingungen verwenden bestehende Lernregeln und dieselben vier Kontrollarme.

| Fall | Sofort-Checkpoint | Checkpoint nach 2s Ruhe | Online | Visuell | Extra-Spikes sofort / ohne Kopie | Extra-Spikes nach Ruhe / ohne Kopie |
|---|---:|---:|---:|---:|---:|---:|
| reference | 48.8% | 48.8% | 48.8% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4 | 50.0% | 51.2% | 50.8% | 99.7% | 21.65 / 0.59 | 17.26 / 0.00 |
| tau100 | 48.8% | 48.8% | 48.8% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4_tau100 | 51.2% | 50.0% | 51.7% | 100.0% | 13.43 / 0.00 | 11.84 / 0.00 |

checkpoint_probe – Verhaltenskriterien einschließlich Familienkorrektur: keine.

rest_checkpoint_probe – Verhaltenskriterien einschließlich Familienkorrektur: keine.

[Kontroll-/Belegungskontraste](prediction-contrasts.csv) · [Weiterleitung und Kontrollarme](propagation-summary.csv) · [Gewichtsdiagnose](weight-summary.csv) · [Unabhängiger Datenaudit](diagnostics.json).

Spikezahlen außerhalb der direkten Kopie-Zielzellen sind getrennt von der Vorhersageleistung zu bewerten. Prüfzeitpunkte sind getrennte Endpunkte; 95%-Bootstrapintervalle sind deskriptiv. Primär wird zusätzlich jeder gerichtete Kontrollkontrast durch einen exakten gepaarten Vorzeichentest mit Bonferroni über 4×2 Endpunkte geprüft.

M9-v2 verlangt mindestens 20 Seeds und zusätzlich einen kontrollierten Gewichtseffekt.

checkpoint_probe – Gesamtnachweis einschließlich Gewichtskausalität: keine.

rest_checkpoint_probe – Gesamtnachweis einschließlich Gewichtskausalität: keine.

[Gewichtsrücksetzungen und gepaarte Kontraste](causal-contrasts.csv). Der Ausleser bleibt fest; Membran-/Spurzustand und reisende Impulse bleiben erhalten.

Bestätigungsreihe mit vorab festgelegten Bedingungen und neuen Seeds.

[Faktorielle Kontraste](factorial-contrasts.csv) sind deskriptiv; eine positive Interaktion allein belegt keinen Lernerfolg.

| Fall | Erhaltener visueller Gewichtsanteil, gekoppelt |
|---|---:|
| reference | 59.2% |
| weight4 | 58.2% |
| tau100 | 46.7% |
| weight4_tau100 | 46.3% |
