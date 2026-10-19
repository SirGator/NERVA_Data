# M5: technische Verifikation und Datenaudit

Abgeschlossen am 16.10.2026. Die bestehenden neuronalen Lernregeln bleiben
unverändert. Neu sind Modellparameter für Aktionskopiegewicht und Core-Tau,
die generische Auswahl der Homöostase-Population in NERVAs Runtime sowie
passive Sensor-/Populationsdiagnosen. Die Standardkonfiguration bleibt erhalten.

## Softwareprüfungen

| Prüfung | Ergebnis |
|---|---:|
| Modell einschließlich M4, M5, Sensorik, Freeze und Rekurrenz | 21 bestanden |
| NERVA mit development, diagnostics, visualization, einschließlich Doc-Tests | 323 bestanden |
| Experimente einschließlich M3, Retention und Sensorimotorik | 29 bestanden |
| nerva-qemu einschließlich lokaler Sockettests | 20 bestanden |
| Echte QEMU-Regression: Live-Modell, Replay, Retention und serieller Gast | 4 bestanden |
| Bestehende M4-Python-Selbsttests | 7 bestanden |
| M5-Python-Selbsttests | 2 bestanden |
| Insgesamt | **406 bestanden** |

Clippy mit `-D warnings` und Formatprüfungen bestehen für alle vier Rust-Pakete.
Shell-Syntax und die ausgeführten Python-Werkzeuge bestehen ebenfalls.
CUDA war nicht aktiviert. Socket-/QEMU-Prüfungen liefen mit freigegebenem
Zugriff außerhalb der Sandbox und der vorhandenen lokalen QEMU-Installation.

Der neue Runtime-Test prüft abgewählte Uhren, ignorierte Wartungsereignisse
außerhalb der Auswahl, frisch gesetzte Zeitanker beim Hinzunehmen von Zellen,
unveränderten Zustand bei ungültigen IDs und das Verhalten neu angelegter Zellen.
M5-Tests prüfen strenge Eingaben, echte plastische Signalpfade, unveränderte
eingefrorene Parameter, bitgleiche Wiederholungen und identische Anfangsnetze
über Homöostasebereiche. Die ältere Experiment-CLI verwendet für die neuen
Konfigurationsfelder die bisherigen Standardwerte.

Die [Prüfprotokolle](verification/) enthalten die abschließenden Rust-/QEMU-/
Clippy-Ergebnisse, den M5-Python-Test und unabhängige Reportläufe. Die sieben
M4-Python-Tests wurden während der Integration ebenfalls erfolgreich ausgeführt.

## Tatsächliche Messungen

| Reihe | A: Motor-Fall-/Seed-Ergebnisse | B: Sensor-Fall-/Seed-Ergebnisse | Geprüfte B-Trialzeilen | Geprüfte B-Phasenzeilen |
|---|---:|---:|---:|---:|
| Pilot, Seeds 0–2 | 36 | 12 | 55.296 | 344.448 |
| Neue Prüfung, Seeds 200–209 | 120 | 40 | 184.320 | 1.148.160 |
| Gesamt | 156 | 52 | 239.616 | 1.492.608 |

A enthält je Ergebnis sechs Interventionen: A, D und keine Kopie, jeweils
mit und ohne STDP. Alle 936 Interventionen werden validiert. Das Fehlen eines
Signalerfolgs ist ein zulässiger Messbefund, kein durch Ersatzwerte gefülltes Ergebnis.

B enthält je Ergebnis vier Arme und zwei Belegungen. Die 1.492.608 zusätzlichen
Sensor-CSV-Zeilen werden ebenfalls gelesen: Zähler müssen mit den JSONs
übereinstimmen, ausgeschlossene Populationen erhalten keine Homöostaseupdates,
eingefrorene Phasen bleiben unverändert und ausgeschlossene Sensorneuronen
behalten ihren intrinsischen Strom null. Alle erwarteten Daten sind vorhanden;
es bleiben keine `.partial`-Ergebnisdateien.

Alle vier B-Bereiche haben pro Seed denselben Anfangsnetz-Fingerabdruck und
dieselbe Normierung. Die erzeugten Sensorimpulse stimmen über alle Bereiche
überein; eingefrorene Kontrollen sind vollständig identisch. Die bisherigen
M4-Audits prüfen zusätzlich echte Bewegungsverzögerung, Vorhersage vor Wirkung,
Aktions-/Klassenbalance, Replays, entkoppelte Zuordnung, Freeze und Ablationen.

## Reproduzierbarkeit

- Ein vollständiger M4-2-Kanal-Lauf mit Seed 0 ist gegenüber dem archivierten
  Gate bytegleich in Ergebnis-JSON, Details und Audit.
- Der vollständige M5-`b_core`-Lauf mit Seed 200 wurde seriell wiederholt.
  Ergebnis-JSON, Details, Audit und Sensor-CSV sind bytegleich zur ursprünglich
  parallel erzeugten Messung.
- Die isolierten A-Tests wiederholen JSON und Rohereignisse exakt.
- Der M5-`all`-Test reproduziert den M4-Lauf bis auf ausdrücklich zusätzliche
  M5-Metadaten; die bisherigen Details/Audit-Dateien sind bytegleich.

[Quelltext- und Programmhashes beim Abschluss](source-sha256.json),
[Pilotmanifest](../m5-pilot/manifest.json), [Bestätigungsmanifest](manifest.json),
[vollständiger unabhängiger Audit](diagnostics.json).

Die Manuskriptwerte stammen aus tatsächlichen Rust-Läufen. Der Signalerfolg in A
ist kein Wirkungslernen. B zeigt keinen bestätigten Vorhersagevorteil und
kombiniert noch nicht beide gezielten Änderungen. Die Kalibrier-/Zeitfenster-
Grenzen stehen im [wissenschaftlichen Bericht](../../M5_EXPERIMENT.md).
