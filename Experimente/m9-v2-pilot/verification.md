# M9-v2: Pilotprüfung vom 27.10.2026

Der wissenschaftliche Pilot mit Seeds 600–602 ist vollständig ausgeführt.
Alle vier Bedingungen verwenden die vorab festgelegten Trialzahlen 256/128/128.
Die Softwareverifikation des verwendeten Protokolls ist im
[technischen Kurzlauf](../m9-v2-smoke/verification.md) dokumentiert.

```bash
python3 NERVA_Modell/Experimente/m9/run.py run --stage pilot --jobs 4 --output Messungen/Experimente/m9-v2-pilot
```

Alle zwölf Fälle bestanden den vollständigen unabhängigen Audit. Erfasst und
geprüft wurden 672 ursprüngliche Replayzweige, 1.152 zusätzliche
Gewichtseingriffszweige, 55.680 Trial-/Propagationszeilen und je 389.760
Phasen-/Sensorzeilen. Der Matrixaudit prüft ursprüngliche Verschaltung,
sensorische Impulszahlen und identische Referenznormierung.

Das Manifest hat weiterhin die vor Beginn gespeicherte SHA-256-Prüfsumme
`a4136814b375cd74eff969871d613f0aa8676ee0f08595dd38a9995452f912fe`.
Die in [provenance.json](provenance.json) gespeicherten Quellcode- und
Programmprüfsummen wurden nach Abschluss erneut geprüft und stimmen überein.
[raw-sha256.csv](raw-sha256.csv) enthält Größe und Prüfsumme aller 84 Rohdateien.

Alle vier Bedingungen liegen an beiden primären Zeitpunkten im gekoppelten Arm
bei 50 % Vorhersagegenauigkeit. Der Pilot mit drei Seeds kann die
Mindestanforderung von 20 Seeds nicht erfüllen. Seine Ergebnisse wurden nicht
zur Auswahl oder Nachjustierung verwendet; alle vier Bedingungen gehen
unverändert in die separate Bestätigungsreihe ein.

[Ergebnisse](summary.md) · [Unabhängiger Datenaudit](diagnostics.json) ·
[Vorab gespeicherter Bestätigungsplan](../m9-v2-confirm/manifest.json).
