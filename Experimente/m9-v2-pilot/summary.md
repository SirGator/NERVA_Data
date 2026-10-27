# M9 – gemessene Ergebnisse

Stufe pilot; Seeds [600, 601, 602]. Alle Bedingungen verwenden bestehende Lernregeln und dieselben vier Kontrollarme.

| Fall | Sofort-Checkpoint | Checkpoint nach 2s Ruhe | Online | Visuell | Extra-Spikes sofort / ohne Kopie | Extra-Spikes nach Ruhe / ohne Kopie |
|---|---:|---:|---:|---:|---:|---:|
| reference | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4 | 50.0% | 50.0% | 48.6% | 100.0% | 16.25 / 0.00 | 9.08 / 0.00 |
| tau100 | 50.0% | 50.0% | 50.0% | 100.0% | 0.00 / 0.00 | 0.00 / 0.00 |
| weight4_tau100 | 50.0% | 50.0% | 50.0% | 100.0% | 8.33 / 0.00 | 8.33 / 0.00 |

checkpoint_probe – Verhaltenskriterien einschließlich Familienkorrektur: keine.

rest_checkpoint_probe – Verhaltenskriterien einschließlich Familienkorrektur: keine.

[Kontroll-/Belegungskontraste](prediction-contrasts.csv) · [Weiterleitung und Kontrollarme](propagation-summary.csv) · [Gewichtsdiagnose](weight-summary.csv) · [Unabhängiger Datenaudit](diagnostics.json).

Spikezahlen außerhalb der direkten Kopie-Zielzellen sind getrennt von der Vorhersageleistung zu bewerten. Prüfzeitpunkte sind getrennte Endpunkte; 95%-Bootstrapintervalle sind deskriptiv. Primär wird zusätzlich jeder gerichtete Kontrollkontrast durch einen exakten gepaarten Vorzeichentest mit Bonferroni über 4×2 Endpunkte geprüft.

M9-v2 verlangt mindestens 20 Seeds und zusätzlich einen kontrollierten Gewichtseffekt.

checkpoint_probe – Gesamtnachweis einschließlich Gewichtskausalität: keine.

rest_checkpoint_probe – Gesamtnachweis einschließlich Gewichtskausalität: keine.

[Gewichtsrücksetzungen und gepaarte Kontraste](causal-contrasts.csv). Der Ausleser bleibt fest; Membran-/Spurzustand und reisende Impulse bleiben erhalten.

Pilot: keine Bestätigung; alle Bedingungen unverändert auf neuen Seeds prüfen.

[Faktorielle Kontraste](factorial-contrasts.csv) sind deskriptiv; eine positive Interaktion allein belegt keinen Lernerfolg.

| Fall | Erhaltener visueller Gewichtsanteil, gekoppelt |
|---|---:|
| reference | 55.8% |
| weight4 | 55.2% |
| tau100 | 42.5% |
| weight4_tau100 | 42.3% |
