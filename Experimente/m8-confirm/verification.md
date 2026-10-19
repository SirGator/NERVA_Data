# M8: technische Verifikation und vollständiger Datenaudit

Abschluss am 17.10.2026. M8 variiert Parameter bestehender Mechanismen. Neue
Lernregeln, Aufgabenpfade oder Änderungen an NERVA und am QEMU-Adapter wurden
nicht eingeführt. Sämtliche Live-Standardwerte bleiben erhalten.

## Softwareprüfungen

| Prüfung | Bestanden |
|---|---:|
| Modell: vollständige Release-Tests einschließlich M4–M6 und experimenteller Parameter | 28 |
| Experimente: vollständige Release-Tests einschließlich M7/M8 | 32 |
| M4-Python-Tests | 7 |
| M5-Python-Tests | 2 |
| M6-Python-Tests | 3 |
| M7-Python-Tests | 2 |
| M8-Python-Tests | 3 |
| Gesamt, ohne doppelt gezählte gezielte Wiederholungen | **77** |

Clippy mit `--all-targets -- -D warnings` und Formatprüfung bestehen für Modell
und Experimente. Shell-Syntax und Python-Kompilierung bestehen ebenfalls. Die
neuen M8-Python-Tests und die M7-Regression liefen mit
`-W error::ResourceWarning`. Die vorhandenen ignorierten QEMU-Livetests wurden
hier nicht erneut ausgeführt; M8 benötigt keine VM.

Die neuen Modelltests prüfen, dass höhere Dichte alle Originalzellen und -kanten
erhält und nur zusätzliche lokale Core-Kanten ohne Selbst- oder Doppelverbindung
anlegt. Gewichtsskalen, Schwellen und Verzögerungen müssen ausschließlich auf den
ausgewählten Populationen wirken. Eine geänderte STDP-Zeitskala darf das initiale
Netz nicht verändern.

Die M8-Integrationstests prüfen strenge Konfiguration, Ablehnung zusätzlicher
Felder und kombinierter Parameter, parallele Bytegleichheit aller sieben
Standarddateien, unveränderte Elternzeit und unabhängige Ruhe-/No-copy-Zweige.
Die Python-Tests erkennen erfundene Extra-Spikezahlen und ungültige Neuronen im
No-copy-Kontrollzweig. Sie prüfen außerdem frische Seedbereiche, 13 Bedingungen
und die exakte familienkorrigierte Vorzeichentest-Schwelle einschließlich Ties.

Eine separate Softwarematrix mit kleinen 8/8/8-Zählern prüfte alle 13 Bedingungen
auf drei Seeds. Deren Daten liegen ausschließlich unter `/tmp` und fließen nicht
in die wissenschaftlichen Berichte ein. Ein dort erkannter Fehler in der
Trialnummer der neuen Propagationsaufzeichnung wurde vor Beginn der wissenschaftlichen
Reihen korrigiert. Die anschließende vollständige technische Vorprüfung bestand.

[Prüfprotokolle und Reproduzierbarkeit](verification/),
[Quelltext-/Programmhashes](source-sha256.json),
[Hashes der archivierten Messungen und Auswertungen](data-sha256.json).

## Tatsächliche wissenschaftliche Daten

| Reihe | Fall-/Seed-Ergebnisse | Trialzeilen | Phasenzeilen | Sensorzeilen | Propagationszeilen | Replayzweige |
|---|---:|---:|---:|---:|---:|---:|
| Pilot: 13 Fälle × Seeds 500–502 | 39 | 180.960 | 1.266.720 | 1.266.720 | 180.960 | 2.184 |
| Bestätigung: 13 Fälle × Seeds 510–519 | 130 | 603.200 | 4.222.400 | 4.222.400 | 603.200 | 7.280 |
| Gesamt | **169** | **784.160** | **5.489.120** | **5.489.120** | **784.160** | **9.464** |

Jede Trialzeile besitzt zusätzlich eine Kopienzeile mit den echten synaptischen
Ankunftszeiten. 56 Zweige je Ergebnis umfassen Kalibrierung, zwei unmittelbare
A/D-Checkpointproben, zwei unabhängige Ruhe-Checkpointproben und zwei No-copy-
Kontrollen je Arm/Belegung. Die 2.080 No-copy-Kontrollfenster der Bestätigung
enthalten insgesamt null Core-Spikes. Keine erwartete Datei fehlt; keine
`.partial`-Ergebnisdatei bleibt übrig.

Die unabhängige Python-Prüfung liest sämtliche Standard-CSVs. Vorhersagegenauigkeit,
Belegungswechsel und beidseitige Korrektheit werden aus Einzelvorhersagen
nachgerechnet. CSV- und JSON-Vorhersagen müssen übereinstimmen. Sie prüft
Klassen-/Aktionsbalance, eindeutige Trials, gleiche Tasten bei umgekehrter Wirkung,
identische gekoppelte/eingefrorene Erfahrungen, unabhängige entkoppelte Zuordnungen,
Freeze und ausgeschlossene Homöostase-/Entwicklungsupdates.

Die Propagationsdatei muss jede Trialzeile genau einmal abdecken. Direkt
angeschlossene Zielzellen werden aus der tatsächlichen Anfangsverschaltung
abgeleitet; sämtliche Core-Spikezeiten müssen vor der Wirkung liegen. Extra-Spikes
werden aus den tatsächlichen Neuronen-IDs neu gezählt. Sensorzähler stimmen
zwischen Phasen-, Sensor- und JSON-Berichten überein.

Alle Kopien treffen bei +1,5/+11,5/+21,5 ms jeweils an drei Zellen ein. Prognosen
liegen vor realer Bewegung und Wirkungsbild bei +50 ms. Exakte Replayzweige
dürfen die Elternzeit nicht verändern. Unabhängige Ruheproben enthalten vor der
Aktionsintegration exakt 2 Sekunden zusätzliche neutrale Beobachtung. No-copy-
Zeitfenster werden separat geprüft.

Über alle 13 Bedingungen eines Seeds stimmen die erzeugten visuellen Impulse
überein. Alle Originalkanten müssen dieselben Endpunkte und Plastizitätsflags
behalten. Gewichts- und Verzögerungsunterschiede müssen genau dem gewählten
Parameter entsprechen. Zusätzliche Kanten sind nur bei Dichtebedingungen erlaubt.
Zellpositionen und Polaritäten bleiben gleich. Der initiale erwartete Sensorstrom
muss entsprechend dem festen Referenz-Ratenverstärker 10 beziehungsweise bei
F=0,5/1,5 ungefähr 5/15 pro Core/s betragen.

[Pilot-Audit](../m8-pilot/diagnostics.json), [Bestätigungs-Audit](diagnostics.json),
[vor Ausführung gespeicherter Bestätigungsplan](manifest.json).

## Reproduzierbarkeit und Grenzen

- Der vollständige aktive Fall `a_weight4`, Seed 510, wurde nach Abschluss seriell
  wiederholt. JSON und alle sechs CSV-Begleitdateien sind bytegleich zur
  ursprünglich parallelen Ausführung.
- Der vollständige historische M6-Fall `diag_D`, Seed 300, bleibt bytegleich in
  JSON und allen fünf bisherigen CSV-Dateien. Optionale Ruhe-/No-copy-/Weiterleitungs-
  Messungen verändern den ursprünglichen M6-Vertrag ohne Optionen nicht.
- Der vollständige historische M4-Fall `a01_minimal_2ch`, Seed 0, bleibt bytegleich
  in JSON, Audit und Details.
- 108 NERVA-/Adapter-Quelldateien stimmen weiterhin mit den bei M6 gespeicherten
  Hashes überein. Neue Modellparameter konfigurieren ausschließlich bereits
  vorhandene neuronale Mechanismen.

Die Wiederholungen wurden nach Abschluss der neuronalen Implementierung
ausgeführt. Spätere Änderungen betreffen ausschließlich Dokumentation und
abgeleitete Auswertungsspalten beziehungsweise deskriptive Parameterkontraste.
Die neuronalen Messdateien wurden dafür nicht verändert. Abschließende
unabhängige Reportläufe prüfen die gesamten Reihen erneut.

Die Replay-API setzt wie in M6 den festen CPU-Pfad und gleiche zustandslose
Utility-Implementierungen voraus; passive Protokolle sind ausgenommen.
Primäre Vorhersagekriterien verwenden getrennte Endpunkte und Bonferroni über
13×2 Bedingungen/Zeitpunkte. Mechanistische Gewichtskontraste und Bootstrapintervalle
bleiben deskriptiv. Die geringe Zahl unabhängiger A/D-Proben begrenzt die Teststärke.
Parameterkombinationen und Gedächtnisstabilisierung bei weiterlaufender Plastizität
wurden nicht untersucht. Weitere Grenzen stehen im
[wissenschaftlichen Bericht](../../M8_EXPERIMENT.md).
