# Verzeichnis sämtlicher Messreihen

Alle folgenden Pfade gelten innerhalb dieses eigenständigen Pakets. Die Einordnung
unterscheidet wissenschaftliche Messreihen, Diagnosen und technische Prüfläufe.
„Bestätigungsreihe“ bezeichnet das Versuchsdesign auf weiteren Seeds; es bedeutet
nicht, dass die Lernhypothese bestätigt wurde. Die Ergebnisse stehen im
[Ergebnisüberblick](../ERGEBNISSE.md).

**Abgebrochene Läufe:** `agency-ten-seeds` enthält laut
[RUN_STATUS.txt](agency-ten-seeds/RUN_STATUS.txt) nur Teilprotokolle. Der vollständige
Nachfolgelauf heißt `agency-ten-seeds-complete`. Auch `interrupted` wird als
historischer Abbruchlauf geführt. Diese Ordner sind keine zusätzlichen Bestätigungen.

## Schneller Einstieg

- [M10-E: Core-Gewichte und Rekurrenz gekreuzt](m10e-crossed-weights/summary.md)
- [M10-E: technischer Pilot](m10e-smoke/README.md)

- [M10-D: Rekurrente Erregung und Hemmung kontrolliert blockieren](m10d-recurrence/summary.md)
- [M10-D: technischer Pilot](m10d-smoke/README.md)

- [M10-C: Eingangsbilanz, Filterung und Resets](m10c-signal-directions/summary.md)

- [M10-B: Wirkungsausrichtung und gemeinsamer Decoderbias](m10b-alignment/summary.md)

- [M10: retrospektive Signalwegdiagnose auf vorhandenen M9-Seeds](m10-path-audit/summary.md)

- [M9: Kombination und Gewichtskausalität auf 20 neuen Seeds](m9-v2-confirm/summary.md)
- [M8: getrennter Parameterscan](m8-confirm/summary.md)
- [M7: Gewichte und Weiterleitung](m7-synapse-audit/summary.md)
- [M6: separate Core-Kontrolle](m6-core-control/summary.md)
- [M4: 20 Bedingungen auf zehn neuen Seeds](m4-confirm/summary.md)

## Vollständiger Bestand

[M10-E](m10e-crossed-weights/summary.md) kreuzt Core-Gewichte auf Trainings-
beziehungsweise Anfangswerten mit vier Rekurrenzsperren auf den bekannten
20 Seeds. Beide Eingriffe erfolgen nach derselben Baseline vor der Aktion.
Die trainierten Zweige reproduzieren M10-D; [Pilotdaten](m10e-smoke/README.md)
bleiben getrennt. Keine neue unabhängige Bestätigung.

[M10-D](m10d-recurrence/summary.md) prüft vier Übertragungsvarianten aus gleichen
eingefrorenen Checkpoints auf den 20 bekannten Kombinationsseeds. Referenz,
Erregung blockiert, Hemmung blockiert und beide blockiert werden bei festem
Ausleser und unveränderten Gewichten verglichen. Der [Pilot](m10d-smoke/README.md)
ist ein separater technischer Kurzlauf. Keine unabhängige Bestätigung.

[M10-C](m10c-signal-directions/summary.md) ergänzt eine algebraisch und physikalisch
geprüfte Bilanz von 1.920 Aktionsfenstern der vorhandenen 20 M10-Traces.
Keine neue Simulation; feste neuronale Auslesergewichte statt neuer Eingangs-
oder Potenzialklassifikatoren.

[M10-B](m10b-alignment/summary.md) ergänzt die reine retrospektive Auswertung
der visuellen Wirkungsausrichtung auf allen 80 M9-Quellfällen. Es gibt keine
neuronalen Läufe und keinen neuen Fit an Aktionslabels.

Die anschließende [M10-Diagnose](m10-path-audit/summary.md) analysiert sämtliche
80 M9-Quellfälle und ergänzt passive Kombinations-Replays auf denselben 20 Seeds.
Sie ist vollständig auditiert und keine neue Bestätigungsreihe.

**Ergänzung vom 27.10.2026:** M9-v2 ist vollständig ausgeführt und auditiert:
[Pilot](m9-v2-pilot/summary.md), zwölf Fälle auf drei Seeds;
[Bestätigung](m9-v2-confirm/summary.md), 80 Fälle auf 20 neuen Seeds mit
Gewichtsrücksetzungen. [Ergebnis: kein funktionaler Lernnachweis](../M9_EXPERIMENT.md). Der technische
[M9-v2-Kurzlauf](m9-v2-smoke/summary.md) ist eine Softwareprüfung mit kleinen
Trialzahlen. Die frühere v1-Planung ([Pilot](m9-pilot/README.md),
[Bestätigung](m9-confirm/README.md)) und ihr technischer
[Kurzlauf](m9-smoke/summary.md) bleiben als ältere Revision erhalten.

Dateizahlen und Größen beschreiben die vorhandenen Laufdateien bei der
Zusammenstellung am 19.10.2026. Größen sind Dezimal-MB, gerundet. Die Einordnung
ist kein neuer Vollständigkeits- oder Signifikanztest.

| Ordner | Einordnung | Inhalt | Einstieg | Dateien | MB |
|---|---|---|---|---:|---:|
| [agency-smoke/](agency-smoke/) | Technischer Kurzlauf | Agency-Ablauf prüfen | [Bericht/Daten](agency-smoke/agency-summary.md) | 17 | 0,2 |
| [agency-ten-seeds/](agency-ten-seeds/) | Unvollständig | Abgebrochen; RUN_STATUS.txt verweist auf den vollständigen Nachfolgelauf | [Bericht/Daten](agency-ten-seeds/RUN_STATUS.txt) | 16 | 0,7 |
| [agency-ten-seeds-complete/](agency-ten-seeds-complete/) | Vollständige Messreihe | Agency, zehn Seeds 0–9 | [Bericht/Daten](agency-ten-seeds-complete/agency-summary.md) | 187 | 7,5 |
| [change/](change/) | Historischer Live-Lauf | Visuelle Demo mit Änderungskodierung | [Bericht/Daten](change/report.json) | 5 | 2,3 |
| [drive-zero-audit/](drive-zero-audit/) | Parameterdiagnose | Strukturentwicklung ohne initialen Wachstumsbedarf | [Bericht/Daten](drive-zero-audit/study-summary.md) | 6 | 1,7 |
| [frozen/](frozen/) | Historischer Live-Lauf | Eingefrorene Variante | [Bericht/Daten](frozen/report.json) | 5 | 2,3 |
| [full-keyboard/](full-keyboard/) | Technischer Live-Lauf | Vollständige virtuelle Tastatur | [Bericht/Daten](full-keyboard/report.json) | 7 | 2,4 |
| [full-keyboard-wasd-control/](full-keyboard-wasd-control/) | Technische Kontrolle | WASD-Vergleich zur vollständigen Tastatur | [Bericht/Daten](full-keyboard-wasd-control/report.json) | 7 | 2,3 |
| [independent-adapters/](independent-adapters/) | Technischer Live-Lauf | Modellunabhängige Adapter | [Bericht/Daten](independent-adapters/report.json) | 5 | 2,3 |
| [interrupted/](interrupted/) | Historischer Abbruchlauf | Kein abgeschlossener Bestätigungsnachweis | [Bericht/Daten](interrupted/report.json) | 5 | 2,3 |
| [m3-seed7-replay/](m3-seed7-replay/) | Replay-Kontrolle | M3-Wiederholung mit Seed 7 | [Bericht/Daten](m3-seed7-replay/m3-summary.md) | 5 | 12,1 |
| [m3-ten-seeds/](m3-ten-seeds/) | Vollständige Messreihe | M3, zehn Seeds | [Bericht/Daten](m3-ten-seeds/m3-summary.md) | 55 | 238,8 |
| [m4-confirm/](m4-confirm/) | Bestätigungsreihe | M4, 20 Bedingungen, Seeds 100–109 | [Bericht/Daten](m4-confirm/summary.md) | 1.207 | 1552,5 |
| [m4-initial-gate/](m4-initial-gate/) | Diagnose-Gate | M4, vier anfängliche Bedingungen auf Seeds 0–2 | [Bericht/Daten](m4-initial-gate/summary.md) | 92 | 332,3 |
| [m4-model-infrastructure/](m4-model-infrastructure/) | Softwareverifikation | Bibliotheks-, Adapter- und Integrationsprüfungen | [Bericht/Daten](m4-model-infrastructure/verification.md) | 6 | 0,0 |
| [m4-pilot/](m4-pilot/) | Pilot | M4, 20 Bedingungen, Seeds 0–2 | [Bericht/Daten](m4-pilot/summary.md) | 365 | 466,1 |
| [m5-confirm/](m5-confirm/) | Bestätigungsreihe | M5, Aktionskopie und Homöostase, Seeds 200–209 | [Bericht/Daten](m5-confirm/summary.md) | 903 | 440,5 |
| [m5-pilot/](m5-pilot/) | Pilot | M5, Seeds 0–2 | [Bericht/Daten](m5-pilot/summary.md) | 270 | 132,1 |
| [m6-confirm/](m6-confirm/) | Bestätigungsreihe | M6-Hauptmatrix, Seeds 300–309 | [Bericht/Daten](m6-confirm/summary.md) | 755 | 976,2 |
| [m6-core-control/](m6-core-control/) | Explorative Folgeprüfung | Separate Core-Homöostase-Kontrolle, Seeds 400–409 | [Bericht/Daten](m6-core-control/summary.md) | 185 | 234,6 |
| [m6-core-diagnostic/](m6-core-diagnostic/) | Mechanistische Diagnose | Einzelzell-/Core-Diagnose, Seeds 0–2 | [Bericht/Daten](m6-core-diagnostic/plan.json) | 10 | 0,1 |
| [m6-pilot/](m6-pilot/) | Pilot | M6-Hauptmatrix, Seeds 0–2 | [Bericht/Daten](m6-pilot/summary.md) | 222 | 292,9 |
| [m7-synapse-audit/](m7-synapse-audit/) | Explorative Ursachenanalyse | M7, Replays vorhandener Seeds 400–409 | [Bericht/Daten](m7-synapse-audit/summary.md) | 76 | 899,8 |
| [m8-confirm/](m8-confirm/) | Bestätigungsreihe | M8, 13 Bedingungen, Seeds 510–519 | [Bericht/Daten](m8-confirm/summary.md) | 1.204 | 1646,1 |
| [m8-pilot/](m8-pilot/) | Pilot | M8, 13 Bedingungen, Seeds 500–502 | [Bericht/Daten](m8-pilot/summary.md) | 358 | 494,0 |
| [pruning-grace-audit/](pruning-grace-audit/) | Parameterdiagnose | Längere Mindestdauer bis zum Pruning | [Bericht/Daten](pruning-grace-audit/study-summary.md) | 6 | 1,7 |
| [recurrent-full-keyboard/](recurrent-full-keyboard/) | Technischer Live-Lauf | Rekurrentes Modell mit vollständiger Tastatur | [Bericht/Daten](recurrent-full-keyboard/report.json) | 9 | 2,5 |
| [recurrent-pilot/](recurrent-pilot/) | Frühe Pilotaufzeichnung | Rekurrentes Modell, Aufnahme und erste Messdaten | [Bericht/Daten](recurrent-pilot/recording.json) | 21 | 14,3 |
| [recurrent-replay/](recurrent-replay/) | Replay-Kontrolle | Wiederholung gespeicherter rekurrenter Erfahrung | [Bericht/Daten](recurrent-replay/study-summary.md) | 4 | 4,5 |
| [recurrent-study/](recurrent-study/) | Aufzeichnung und Messlauf | Gemeinsame Bild-/Aktionsaufnahme für gepaarte Strukturvergleiche | [Bericht/Daten](recurrent-study/recording.json) | 45 | 36,0 |
| [recurrent-verified/](recurrent-verified/) | Gepaarte Messreihe | Rekurrenter Core mit/fester Struktur; drei Seeds | [Bericht/Daten](recurrent-verified/study-summary.md) | 6 | 5,1 |
| [recurrent-wasd-checked/](recurrent-wasd-checked/) | Technischer Live-Lauf | Geprüfte WASD-Steuerung des rekurrenten Modells | [Bericht/Daten](recurrent-wasd-checked/report.json) | 9 | 2,4 |
| [recurrent-wasd-live/](recurrent-wasd-live/) | Historischer Live-Lauf | Rekurrentes Modell mit WASD | [Bericht/Daten](recurrent-wasd-live/report.json) | 9 | 2,4 |
| [relocated/](relocated/) | Technischer Live-Lauf | Historische Prüfung nach Verlagerung | [Bericht/Daten](relocated/report.json) | 5 | 2,3 |
| [retention-1000/](retention-1000/) | Einzel-Seed-Messung | 1.000 Trainingsframes, dokumentierter Seed 42 | [Bericht/Daten](retention-1000/retention-summary.md) | 7 | 29,4 |
| [retention-probe/](retention-probe/) | Prüfaufnahme | Separat aufgezeichnete 64 Prüfungsbilder | [Bericht/Daten](retention-probe/recording.json) | 66 | 49,9 |
| [sensorimotor-seed7-replay/](sensorimotor-seed7-replay/) | Replay-Kontrolle | Sensorimotorik-Wiederholung mit Seed 7 | [Bericht/Daten](sensorimotor-seed7-replay/sensorimotor-summary.md) | 583 | 33,1 |
| [sensorimotor-smoke/](sensorimotor-smoke/) | Technischer Kurzlauf | Sensorimotorik-Ablauf prüfen | [Bericht/Daten](sensorimotor-smoke/sensorimotor-summary.md) | 151 | 6,6 |
| [sensorimotor-ten-seeds/](sensorimotor-ten-seeds/) | Vollständige Messreihe | Getrennte Motor-/Wirkungstests, Seeds 0–9 | [Bericht/Daten](sensorimotor-ten-seeds/sensorimotor-summary.md) | 6.413 | 599,3 |
| [verified/](verified/) | Technischer Live-Lauf | Frühe visuelle VM-Prüfung; auch PNG-Aufnahmen vorhanden | [Bericht/Daten](verified/report.json) | 7 | 2,3 |

`learned.weights` ist der gespeicherte Gewichtsstand der
[früheren seriellen Demo](../SERIAL_MODEL.md); er ist kein Ergebnis des M8-Lerntests.

[Datenhandbuch](../DATENHANDBUCH.md) · [Methodik](../METHODIK.md) · [Startseite](../README.md).
