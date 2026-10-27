# M10-E: Core-Gewichte und Rekurrenz gekreuzt

Diagnose vom 27.10.2026 auf den bekannten Kombinationsseeds 610–629.
Zwei Gewichtszustände (trainiert/Core auf Anfangswerte) × vier Sperren (keine,
rekurrente Erregung, rekurrente Hemmung, beide), vier Arme, beide Belegungen
und zwei unabhängige Zeitpunkte. 5.120 einzelne Aktionsfenster insgesamt.

[Bericht](../../M10E_EXPERIMENT.md) · [Zusammenfassung](summary.md) ·
[Methodik](../../Dokumentation/M10E_METHODIK.md) · [Verifikation](verification.md).

- `manifest.json`: vorab fixierte Quellen, SHA-256 und Auswertungsdefinition.
- `provenance.json`: Programm-, Binär- und Manifestprüfsummen vor Ausführung.
- `execution.json`: tatsächliche Parallelität und Seedliste.
- `traces/`: vollständiges ursprüngliches Ergebnis plus neue Probeäste,
  Gewichtsänderungslisten, Sperrlisten, Zustände und Ereignisse.
- `pairs.csv`: alle 2.560 Paare je Seed/Arm/Belegung/Zeitpunkt/Sperre/Gewicht.
- `summary.csv`: beide Gewichtszustände, sämtliche Arme und Sperren.
- `weight-effects.csv`: 2.560 Vergleiche einzelner trainierter/zurückgesetzter
  Antworten; Änderungen von Spikezählmuster, Ereignissen, Vorhersage, Restpotenzial.
- `weight-effect-summary.csv`: Änderungszahlen je Arm/Zeitpunkt/Sperre.
- `contrasts.csv`: Gewichtseffekte, Wechselwirkungen und Kontrollvergleiche,
  seedgepaart und ausschließlich deskriptiv.
- `diagnostics.json`: Quell-, Zustands-, Ausleser-, Ereignis- und LIF-Prüfungen.
- `raw-sha256.csv`: Prüfsummen der 20 Roh-JSONs und 120 historischen CSVs.

Rücksetzungen finden hier **nach** derselben Baseline statt, bei M10 hingegen
davor. Vier trainierte Zweige reproduzieren M10-D exakt. Unterwegs befindliche,
nicht gesperrte Eingänge behalten ihre Emissionsamplitude; Zellzustände und
Spuren bleiben erhalten. Es wird nicht das gesamte neuronale Gedächtnis gelöscht.
Die Analyse ist keine neue unabhängige Bestätigung gelernter Wirkungen.

Zeitfelder: `intervention_us` bleibt der historische Startanker vor der
Baseline. Der tatsächliche Gewichtsreset steht in
`weight_intervention.activation_us`, die Sperre in
`recurrence_gate.activation_us`; beide entsprechen `action_us`.
