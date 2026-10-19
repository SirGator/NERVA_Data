# M6: technische Verifikation und Datenaudit

Abgeschlossen am 16.10.2026. Neue Software ergänzt den kontrollierten M6-Ablauf,
passive Kopienzeitpunkte und lesende Vergleiche des ausführbaren Replayzustands.
Die neuronalen Rechen-/Lernregeln und Standardwerte des Live-Modells bleiben
erhalten. M4-/M5-Pläne und historische Ergebnisse werden nicht ersetzt.

## Softwareprüfungen

| Prüfung | Ergebnis |
|---|---:|
| Modell einschließlich M4/M5/M6, Replayzustand und Einzelzelldiagnose | 25 bestanden |
| NERVA mit development, diagnostics, visualization, einschließlich Doc-Tests | 323 bestanden |
| Experimente einschließlich M3, Retention und Sensorimotorik | 29 bestanden |
| nerva-qemu einschließlich lokaler Sockettests | 20 bestanden |
| Echte QEMU-Regression: Live-Modell, Replay, Retention und serieller Gast | 4 bestanden |
| Bestehende M4-Python-Selbsttests | 7 bestanden |
| Bestehende M5-Python-Selbsttests | 2 bestanden |
| M6-Python-Selbsttests | 3 bestanden |
| Insgesamt | **413 bestanden** |

Clippy mit `-D warnings` und Formatprüfungen bestehen für alle vier Rust-Pakete.
Shell-Syntax und Python-Kompilierung sind geprüft. CUDA war nicht aktiviert.
Socket-/QEMU-Regressionen liefen mit freigegebenem Zugriff außerhalb der Sandbox
und der vorhandenen lokalen QEMU-Installation. M6 selbst verwendet Rust-Testweltbilder
und braucht keine QEMU-Instanz.

Die M6-Modelltests vergleichen ein gleiches sichtbares Netz mit unterschiedlichen
ausstehenden Eingaben, prüfen anschließende identische Fortsetzungen und führen
denselben CLI-Fall seriell und zweimal parallel aus. JSON und alle fünf
Standard-CSV-Dateien müssen bytegleich sein. Strenge Konfigurationsprüfung lehnt
unerwartete Felder/Parameter ab; Core-Homöostase aus ist nur bei ausgeschalteter
Sensor-Homöostase zulässig. Der Zelltest überprüft die Wirkung negativen
intrinsischen Stroms auf dieselben drei Eingänge ohne Veränderung des Originals.

Die Python-Selbsttests verwenden ausschließlich temporäre synthetische
Auswerterwerte. Sie prüfen, dass ein unmittelbarer Lernerfolg nicht durch spätere
Vergessenswerte versteckt wird, ein Erfolg nur einer Belegung oder reine
Aktionsunterscheidung nicht genügt und der Plan mit neuen Seeds wiederaufnehmbar
ist. Diese Testdaten gehen in keinen wissenschaftlichen Bericht ein.

[Abschließende Prüfprotokolle](verification/),
[Quelltext- und Programmhashes](source-sha256.json),
[Hashes der archivierten Messdaten und Auswertungen](data-sha256.json).

## Vollständigkeit der tatsächlichen Messdaten

| Reihe | Fall-/Seed-Ergebnisse | Trialzeilen | Phasenzeilen | Sensorzeilen | Replayzweige |
|---|---:|---:|---:|---:|---:|
| Hauptmatrix Pilot, Seeds 0–2 | 24 | 110.976 | 777.216 | 777.216 | 576 |
| Hauptmatrix Bestätigung, Seeds 300–309 | 80 | 369.920 | 2.590.720 | 2.590.720 | 1.920 |
| Separate Core-Kontrolle, Seeds 400–409 | 20 | 92.480 | 647.680 | 647.680 | 480 |
| Gesamt | **124** | **573.376** | **4.015.616** | **4.015.616** | **2.976** |

Jede Trialzeile besitzt eine zusätzliche Kopienzeile mit den tatsächlichen
synaptischen Ankunftszeiten. Der unabhängige Python-Audit liest alle diese
Standard-CSVs. Er berechnet Vorhersagegenauigkeiten, Belegungswechsel und
beidseitige Korrektheit aus Einzelvorhersagen neu und vergleicht sie mit den
Trialprotokollen. Die Kopien liegen bei +1,5 ms beziehungsweise +1,5/+11,5/+21,5 ms
an je drei Zellen, vor Prognose und Wirkung. Die reale Weltbewegung beginnt bei
+50 ms und nicht vor der Prognose.

Weitere Prüfungen umfassen Klassen-/Aktionsbalance und eindeutige Trialnummern,
gleiche Tasten bei umgekehrter Wirkung, identische gekoppelte/eingefrorene
Erfahrungen, unabhängige entkoppelte Zuordnungen und unveränderte Lernparameter
außerhalb des Trainings. Sensorzähler müssen zwischen JSON und CSV übereinstimmen;
ausgeschlossene Populationen bekommen keine Homöostaseupdates. Entwicklung ist
aus. Kalibrier-/Checkpointzweige müssen dieselbe Ausgangslage reproduzieren und
dürfen die Elternzeit nicht verändern. Der erste Online-Trial beginnt unmittelbar
am Trainingscheckpoint.

Pro Seed stimmen über die vier Hauptvarianten Anfangsnetze, Normierung und
erzeugte Sensorimpulse überein. Die eingefrorenen Kontrollen sind beim Umschalten
der Sensorhomöostase vollständig identisch. Die getrennte Core-Kontrolle prüft
ebenfalls identische Anfangsnetze, Normierung und eingefrorene An-/Aus-Kontrollen.
Keine `.partial`-Datei oder erwartete Messdatei fehlt.

Die separate Einzelzelldiagnose liefert drei weitere JSONs mit 36 echten
Zellinterventionen. Ihre Trainingsendzustände stimmen mit dem ursprünglichen
Pilot überein. Die unveränderten Zellkopien reproduzieren jeweils die echten
Netz-Spikezeiten, und die Elternparameter bleiben erhalten. Diese Fälle sind
keine zusätzlichen unabhängigen Trainingsseeds der Bestätigung.

Datenaudits: [Pilot](../m6-pilot/diagnostics.json),
[Bestätigung](diagnostics.json), [Core-Kontrolle](../m6-core-control/diagnostics.json).

## Reproduzierbarkeit und Grenzen

- Der vollständige M6-Fall `diag_D`, Seed 300, wurde nach Abschluss seriell
  wiederholt. Ergebnis-JSON, Audit-, Details-, Sensor-, Kopien- und Zweig-CSV
  sind bytegleich zur ursprünglichen parallel erzeugten Messung.
- Der vollständige M4-Fall `a01_minimal_2ch`, Seed 0, bleibt gegenüber dem
  historischen Gate bytegleich in Ergebnis-JSON, Audit und Details.
- Die archivierten M4-/M5-Orchestratoren, ihre Tests und M5-Modellprogramme
  stimmen weiterhin mit den bei M5 gespeicherten Quelltexthashes überein.
- Replaygleichheit umfasst Netz, Scheduler einschließlich ausstehender Ereignisse,
  STDP-eigene Spuren, lokale Wartungsuhren und die relevanten Modellzustände.
  Der generische NERVA-Vergleich setzt gleiche zustandslose Compute-/Utility-
  Implementierungen voraus; M6 verwendet den festen CPU-Pfad. Passive Logs sind
  ausgeschlossen. Es wird keine portable Serialisierungs- oder GPU-Gleichheit
  behauptet.

Die neuronalen JSON-/CSV-Messungen wurden für den abschließenden verschärften
Datenaudit nicht erneut gerechnet. Nur die daraus abgeleiteten Auswertungen
wurden neu erzeugt. Die SHA-256-Datei hält die abschließende Softwareversion fest.

Die wissenschaftlichen Ergebnisse bleiben negativ: Signalübertragung und
visuelle Auslesbarkeit sind kein Zuordnungslernen. Grenzen der unmittelbaren
Probe und der explorativen Zusatzreihen stehen im
[M6-Bericht](../../M6_EXPERIMENT.md).
