# Umfang, Herkunft und Nachvollziehbarkeit

## Stand dieses Pakets

Das Informationspaket wurde am **19.10.2026** aus dem lokal vorhandenen
NERVA-Projekt zusammengestellt. Es beschreibt die enthaltenen Messreihen bis M8.
Die ursprünglichen Berichte und Messdateien tragen ihre eigenen Abschlussdaten.
Die Zusammenstellung ist keine neue Messreihe.

Die neuen Einführungen fassen ausschließlich die hier enthaltenen Berichte und
gespeicherten Ergebnisse zusammen. Sie ergänzen keine ungemessenen
Leistungsbehauptungen. Insbesondere bleiben Pilot, Bestätigung, Ursachenanalyse
und reine Softwareprüfungen unterscheidbar.

## Planung vom 28.10.2026

Die Diagnosephase M10 ist mit M10-E abgeschlossen. Weitere M10-Zusatzversuche
sind vorerst zurückgestellt. M11 ist als begrenzter Vergleich mit synaptischer
Konkurrenz vorgeschlagen, noch ohne Implementierung oder Messlauf. Diese
Planungsaktualisierung ändert keine historischen Ergebnisse.

## Ergänzung vom 27.10.2026: M10

[M10-E](M10E_EXPERIMENT.md) kombiniert Core-Gewichtsrücksetzung und vier
Rekurrenzsperren auf den bekannten 20 Seeds. Die Rücksetzung erfolgt diesmal
nach der Baseline, damit alle Aktionsproben mit gleichem Zellzustand beginnen.
Neue Probeäste, alte Originalergebnisse und ein getrennter technischer Pilot
sind enthalten; die Diagnose ist keine unabhängige Bestätigung.

[M10-D](M10D_EXPERIMENT.md) ergänzt neue kontrollierte Übertragungsproben auf
den bekannten 20 M9-Kombinationsseeds. Erregung und Hemmung werden einzeln oder
gemeinsam erst nach der Baseline blockiert; Aktionskopien und feste Ausleser
bleiben erhalten. Der technische Pilot ist getrennt archiviert. Die neuen
Proben sind keine unabhängige Bestätigung und verändern die Originaldaten nicht.

[M10-C](M10C_EXPERIMENT.md) zerlegt vorhandene Eingangsbeiträge nach Quelle,
Refraktärfilter, Leck und Resetverlust. 1.920 Aktionsfenster sind rekonstruiert;
Gruppen- und Einzelkantensummen sowie die M10-B-Spikeprojektion werden geprüft.
Es gab keine neue neuronale Simulation und keinen Ausleserfit.

Die weitere [M10-B-Zusatzdiagnose](M10B_EXPERIMENT.md) trennt gemeinsamen
Projektionsbias und Wirkungsausrichtung anhand der vorhandenen visuellen
Kalibrierparameter. Sie umfasst alle 80 M9-Quellfälle, keine neue Simulation
und keinen neuen Ausleserfit. Quelldaten bleiben unverändert.

Die [M10-Signalwegdiagnose](M10_EXPERIMENT.md) ergänzt die retrospektive
Auswertung der 80 M9-Fälle und passive Replays der Kombination auf denselben
20 Seeds. Neue Phasentraces und unabhängige Ereignis-/Spannungsprüfungen sind
enthalten; die ursprünglichen Messdaten bleiben unverändert.

## Ergänzung vom 22.10.2026

Das Paket enthält jetzt eine eigenständige lokale Archiv-GUI unter
[GUI/](GUI/README.md), startbar mit `./gui.sh`. Sie liest die vorhandenen Daten,
Berichte und Bilder ohne Modellcode und verändert die historischen Messdateien
nicht. Die wissenschaftlichen Abschlussdaten und Ergebnisse bleiben erhalten.
Die Paketprüfsummen wurden um die GUI und die aktualisierten Einstiegstexte ergänzt.
Python-Cachedateien und interne Git-Metadaten sind ausgenommen.

## Enthaltene Unterlagen

Ergänzung vom **27.10.2026**: M9-v2 ist mit zwölf Pilotfällen und 80 Fällen auf
20 neuen Bestätigungsseeds vollständig ausgeführt und auditiert. Der
[Abschlussbericht](M9_EXPERIMENT.md), Rohdaten, Gewichtsinterventionen,
Prüfnachweise und der [Forschungsfahrplan](Dokumentation/FORSCHUNGSPLAN.md) sind
enthalten. Frühere v1-Pläne und technische Kurzläufe bleiben getrennt erhalten.
Die Paketprüfsummen umfassen auch diese Ergänzungen; Python-Caches bleiben
ausgeschlossen. Keine M9-Bedingung erfüllt die primären Lernkriterien.

- Projektüberblick, Ergebnisübersicht, Methodikerklärung und Datenhandbuch.
- Elf ausführliche Berichte: rekurrenter Core, Retention, Agency, Sensorimotorik,
  M3 bis M8 sowie die frühere serielle Demo.
- Technische Beschreibungen von Architektur, Modell, Tastatur und Versuchsverträgen.
- Die ursprünglichen Hypothesentexte.
- Sämtliche vorhandenen archivierten Messordner, auch historische und
  unvollständige Läufe, mit einer ausdrücklichen Einordnung im Verzeichnis.
- Eine kompakte M8-Tabelle, direkt aus den originalen CSVs abgeleitet.

Die originalen Laufdateien unter `Experimente/` wurden für diese Zusammenstellung
nicht verändert. Das schließt die historischen Markdown-Zusammenfassungen,
Verifikationsberichte und Hashlisten ein. Fehlende Berichte wurden hier ergänzt,
sodass auch die bisherigen Rückverweise aus den Verifikationsberichten aufgehen.
Die Datei `Experimente/README.md` ist ein neuer Wegweiser.

Die ausführlichen Berichtskopien und technischen Dokumente wurden aus dem Codeprojekt
übernommen. Sie erhielten einen Pakethinweis und lokale Linkziele. Ihr fachlicher
Inhalt wurde übernommen. [Dokumentation/QUELLEN.json](Dokumentation/QUELLEN.json)
verzeichnet die Herkunft mit Quell-Hashes. Diese Hashes betreffen den bei der
Übernahme gelesenen Stand; historische `source-sha256.json`-Dateien können einen
früheren Stand beschreiben.

## Was sich mit diesem Ordner nachvollziehen lässt

Die Forschungsfrage, Modellkonzepte, Versuchsbedingungen, Parameter, Kontrollen,
Auswertungskriterien, Ergebnisse und Einschränkungen sind ohne Quellcode lesbar.
CSV- und JSON-Dateien stehen für eigene Analysen bereit. Gespeicherte Prüfberichte
beschreiben, welche Software- und Datenprüfungen damals ausgeführt wurden.

Eine vollständige erneute Simulation oder Ausführung der ursprünglichen
Python-Audits benötigt zusätzlich den passenden Projektcode und dessen
Laufzeitvoraussetzungen. Historische Quell-Hashes ersetzen diese Dateien nicht.
Reproduzierbarkeit gilt im Umfang der jeweils dokumentierten Wiederholungen;
sie wird nicht pauschal für andere Backends oder Umgebungen behauptet.

## Dateien nach dem Herunterladen prüfen

[PRUEFSUMMEN.sha256](PRUEFSUMMEN.sha256) enthält relative Pfade und SHA-256-Werte
der Paketdateien zum Zeitpunkt der Zusammenstellung. Die Hashliste selbst und
die interne Git-Verwaltung unter `.git/` sind ausgenommen. Für die zwei über
Git LFS gespeicherten CSVs gelten die Prüfsummen ihrer vollständigen Messinhalte,
nicht der Verweisdateien. [Downloadhinweise](HERUNTERLADEN.md) erklären den Bezug.
Die Liste lässt sich unabhängig vom ursprünglichen Projekt prüfen.
Im heruntergeladenen Ordner `Messungen` unter Linux zum Beispiel:

```bash
sha256sum --check --quiet PRUEFSUMMEN.sha256
```

Ohne Fehlermeldungen und mit Rückgabewert 0 stimmen alle aufgeführten Dateien
überein. Für die vollständige Prüfung werden auch sämtliche Rohdaten benötigt.
Die Prüfung erkennt fehlende oder geänderte Dateien; sie bewertet weder die
wissenschaftliche Richtigkeit noch bestätigt sie ohne separat vertrauenswürdige
Hashliste die Urheberschaft. Später hinzugefügte Dateien werden nicht erfasst.

Die Hashliste gilt für diese Zusammenstellung. Wenn das Messverzeichnis später
um neue Ergebnisse erweitert oder Dokumentation verändert wird, muss ein neuer
Paketstand mit aktualisierter Hashliste erstellt werden.

Zurück: [Startseite](README.md).
