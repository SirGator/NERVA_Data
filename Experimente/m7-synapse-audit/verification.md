# M7: Verifikation und Reproduzierbarkeit

Abschluss am 16.10.2026. M7 benutzt vorhandene neuronale Regeln und Anfangsnetze.
Neu sind das Experimentprogramm, seine passiven Aufzeichnungen, der unabhängige
Auswerter und ein eingefrorener kontrollierter Gewichtseingriff im Modell.
NERVA und nerva-qemu werden für M7 nicht verändert.

## Tatsächlich ausgeführte Softwareprüfungen

| Paket / Prüfung | Bestanden |
|---|---:|
| Modell: vollständige Release-Tests einschließlich M4/M5/M6 und Gewichtsintervention | 26 |
| Experimente: vollständige Release-Tests einschließlich M7 | 30 |
| M7-Python-Audit, einschließlich absichtlich verfälschter Daten | 2 |
| Gesamt, ohne doppelt gezählte Wiederholungen | **58** |

Der neue Modelltest prüft Ablehnung aktiver Plastizität, ungültiger IDs, negativer,
nicht endlicher und zu großer Gewichte. Bei abgewiesenen Änderungen bleibt der
vollständige Replayzustand gleich. Ein gültiger Eingriff ändert ausschließlich
die gewählte Synapse; Neuronen und übrige Synapsen bleiben gleich.

Der M7-Integrationstest erzeugt eine kleine echte M6-Referenz, startet zwei
M7-CLI-Läufe parallel und vergleicht Ergebnis-JSON und alle drei CSVs byteweise.
Alle sechs Trainingsarme und 60 Gegenprüfungen müssen vorliegen. Ungültige
Referenzkonfigurationen, fehlende M6-Pflichtprüfungen und falsche Seeds werden
abgewiesen. Der abschließende gezielte M7-Test lief nach der Verschärfung dieser
Eingangsprüfung erneut erfolgreich.

Die Python-Tests erzeugen separate kleine M6-/M7-Rust-Läufe im temporären Ordner.
Gültige Daten bestehen den unabhängigen Audit. Ein um eine Mikrosekunde geänderter
nächster Prä-Partner und ein verfälschtes Retentionsgewicht werden erkannt.
Dateien schließen auch im Fehlerfall; die Tests liefen mit
`-W error::ResourceWarning`. Testdaten werden nicht in die Matrix eingemischt.

Clippy mit `--all-targets -- -D warnings` und Formatprüfung bestehen für Modell
und Experimente. Shell-Syntax und Python-Kompilierung bestehen ebenfalls.
Die bestehenden ignorierten QEMU-Livetests wurden in diesem Schritt nicht erneut
ausgeführt; M7 benötigt keine VM und verändert deren Adapter nicht.

[Prüfprotokolle und gemessene Reproduzierbarkeit](verification/),
[Quelltext-/Programmhashes](source-sha256.json),
[Hashes der Messdateien und abgeleiteten Auswertungen](data-sha256.json).

## Datenumfang und unabhängiger Audit

Zehn vorhandene Seeds 400–409; drei Arme, zwei Belegungen, je 256 Trainingstrials.
Die ursprünglichen Referenzen sind durch SHA-256 im Manifest festgehalten.
Alle vorgesehenen Messungen sind vollständig:

| Datentyp | Geprüfte Anzahl |
|---|---:|
| Trainingsläufe | 60 |
| Reale neuronale Ereignisse | 7.188.605 |
| Tatsächliche Gewichtsänderungen und nächste Spikepaare | 1.834.289 |
| Einzelgewichte an acht Checkpoints je Trainingslauf | 78.720 |
| Gegenprüfungen ab demselben vollständigen Replayzustand | 600 |

Die Rust-Prüfung vergleicht jede einzelne Gewichtsänderung exakt mit der bestehenden
f32-Nächste-Paar-STDP-Gleichung. Der passive Ledger rekonstruiert alle Gewichte
aus initialen Gewichten und den tatsächlichen Updateereignissen. Er muss an jedem
aufgezeichneten Schritt mit dem Netz übereinstimmen.

Der Python-Audit rekonstruiert letzte Prä-Ankünfte und Post-Spikes unabhängig,
prüft Partner, Trial-/Phasen-/Tastenmetadaten, Paarfenster, Richtung und auslösenden
Zeitpunkt. Alle Updates müssen auf angenommenen exzitatorischen plastischen
Kanten liegen. Gewichte, Updatezahlen, Ereigniszahlen, Core-Spikes und Kopienankünfte
werden zwischen CSVs und JSON verglichen. Die unabhängige Formelprüfung verwendet
eine Toleranz von 10⁻⁷ für Unterschiede zwischen Rust-/Python-Exponentialrechnung;
der Rust-interne Formelvergleich bleibt exakt.

Anfangs-, Zwischen- und Freeze-Gewichte müssen mit dem Ereignisledger
übereinstimmen. Frozen-/Ruhe-/Interferenzgewichte müssen exakt erhalten bleiben.
Jede Gegenprüfung enthält dieselben 32 Core-Kanäle, vollständige Spikeereignisse,
korrekte Kopienzahl und ausschließlich Ereignisse im Aktionsfenster. Alle 600
Zweige beginnen vor dem Eingriff am exakt gleichen ausführbaren Zustand wie ihre
unveränderte Elterninstanz. Kein zukünftiges Wirkungsbild wird in ihnen gezeigt.

## Reproduzierbarkeit und Geltungsbereich

Der vollständige Seed-400-Lauf wurde nach Abschluss seriell wiederholt.
`result.json`, `events.csv`, `pairs.csv` und `weights.csv` sind bytegleich zu der
ursprünglich parallel ausgeführten Messung. Die Wiederholung benutzt die zuletzt
verschärfte Referenzvalidierung; diese verändert keine neuronalen Rechenwege.

M6-Referenzzustände werden anhand der veröffentlichten Anfangsnetz-Fingerabdrücke,
des neu berechneten Verstärkungsfaktors, aller genannten Trainingszähler und der
Core-Membranwerte auf ihrer ursprünglichen f32-Präzision geprüft. Daraus wird keine
Vollständigkeit eines in M6 nicht gespeicherten serialisierten Runtimezustands
abgeleitet. Die **M7-Gegenprüfungen** vergleichen hingegen zusätzlich ausstehende
Ereignisse, STDP-Spuren, Uhren, Sensor-/Decoderzustände und Modellzeit über die
bestehende Replay-API. Deren feste CPU-/zustandslose Utility-Voraussetzungen bleiben
wie in M6 bestehen.

Die Analyse verwendet vorhandene Seeds und ist explorativ. Sie erhebt keine neue
funktionale Lernerfolgsrate. Gewichtsretention bei abgeschalteter Plastizität
belegt keine Konsolidierung. Grenzen der direkten topologischen Zuordnungsdiagnose
und der A/D-Proben nach zwei Sekunden Ruhe stehen im
[wissenschaftlichen Bericht](../../M7_EXPERIMENT.md).
