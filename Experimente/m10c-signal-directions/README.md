# M10-C: Vorzeichen der Signalbeiträge

Retrospektive Analyse vom 27.10.2026, vollständig auf den 20 vorhandenen
M10-Kombinations-Traces der Seeds 610–629. Keine neue Simulation und kein
neuer Ausleserfit; 960 A-/D-Paare, 1.920 Aktionsfenster.

[Ergebnisbericht](../../M10C_EXPERIMENT.md) · [Zusammenfassung](summary.md) ·
[Methodik](../../Dokumentation/M10C_METHODIK.md) · [Verifikation](verification.md).

- `manifest.json`: vor Auswertung fixierte Methode, Quellen und SHA-256.
- `provenance.json`: Programm- und Manifestprüfsummen vor voller Auswertung.
- `signals.csv`: acht Signalprojektionen je Paar, einschließlich Vorzeichen.
- `sources.csv`: Beiträge der fünf Quellgruppen.
- `edges.csv`: aktive synaptische Beiträge einschließlich Anfangs-, Trainings-
  und Probegewicht; Zeilen sind keine unabhängigen Replikate.
- `windows.csv`: Potenzial-Rekonstruktionsfehler je Aktionsfenster.
- `transitions.csv`: Vorzeichenvergleich bei Filterung, Leck und Spikezählung.
- `summary.csv`: deskriptive Häufigkeiten je Arm, Zeitpunkt, Eingriff und Signal.
- `diagnostics.json`: Quellreproduktion, physikalische und algebraische Audits.

Eingangs- und Potenzialprojektionen benutzen die festen neuronalen Gewichte
des bestehenden Spikezähl-Auslesers, keine eigenen visuellen Klassenachsen
dieser Signaltypen. Das Endpotenzial ist ein Zustand nach Spikes und Resets.
