# M4: Ausführung und technische Verifikation

Abgeschlossen am 15.10.2026. Die Messungen verwenden das vorhandene NERVA;
es wurden keine neuronalen Lernregeln ergänzt. Modell und Experimente bleiben
getrennte Pakete. Die JSON-CLI liegt gemäß Auftrag in Modell.

## Tatsächlich ausgeführt

| Reihe | Fall-/Seed-Läufe | Trialzeilen unabhängig geprüft | Phasenzeilen unabhängig geprüft |
|---|---:|---:|---:|
| Erstes Gate: 4 Fälle, Seeds 0–2 | 12 | 55.296 | 310.656 |
| Vollständiger Pilot: 20 Fälle, Seeds 0–2 | 60 | 276.480 | 1.688.448 |
| Vollständige neue Prüfung: 20 Fälle, Seeds 100–109 | 200 | 921.600 | 5.628.160 |
| Gesamt | 272 | 1.253.376 | 7.627.264 |

Jeder Lauf enthält vier Arme und zwei Belegungen. Die wiederholten Gate-Fälle
im Pilot zählen nicht als zusätzliche unabhängige Seeds. Alle Läufe verwenden
256 Trainingstrials, 128 Kalibriertrials und 128 Testtrials je Belegung und
Prüfzeitpunkt. Kurze technische Acht-Trial-Läufe sind separat gespeichert und
fließen nicht in die statistischen Ergebnisse ein.

Alle fünf verpflichtenden Auditflags sind in allen 272 Ergebnisdateien wahr.
Zusätzlich prüft `diagnose.py` die tatsächlichen CSV-Zeilen unabhängig:
Vorhersage vor Bewegung/Wirkungsbild, echte konfigurierte Bewegungsverzögerung,
Aktionskopie-Ankünfte, gültige Spikezeitgrenzen, eindeutige Trialnummern,
Klassen-/Aktionsbalance, gepaarte Replays, zerstörte Zuordnung, Freeze und
STDP-/Homöostase-/Entwicklungs-/Feedback-Ablationen. Die gespeicherten
Membranwerte sind endlich. Keine Prüfung ist durch erfundene Messwerte ersetzt.

## Softwareprüfungen

| Prüfung | Ergebnis |
|---|---|
| Modell: einschließlich JSON-Vertrag, Kausalität, Freeze, Sensorik und Determinismus | 18 Tests bestanden |
| Experimente: einschließlich M3-, Retention- und Sensorimotorik-Regression | 29 Tests bestanden |
| NERVA mit development, diagnostics, visualization, einschließlich Doc-Tests | 322 Tests bestanden |
| nerva-qemu einschließlich lokaler QMP-Sockettests | 20 Tests bestanden |
| Explizite echte QEMU-Regression: Live-VM, Replay, Retention und serieller Gast | 4 Tests bestanden |
| Python-Runner: einschließlich Schutz gegen unvollständige oder nur aggregierte Bestätigungen | 7 Tests bestanden |
| Insgesamt | **400 Tests bestanden** |
| Clippy mit `-D warnings` für alle vier Rust-Pakete | Bestanden |
| Formatprüfung aller vier Rust-Pakete | Bestanden |
| Shell-Syntax und Kompilierung der Python-Dateien | Bestanden |
| Alle 20 Konfigurationen als kurze CLI-Smoketests | Bestanden; keine Leistungsdaten |

Die QEMU-/Sockettests wurden mit freigegebenem Zugriff außerhalb der Sandbox
ausgeführt. Verwendet wurde die vorhandene lokale QEMU-Installation unter
`Modell/.tools/qemu`, keine neu installierte Systemabhängigkeit. CUDA war nicht aktiv.

Die M4-Integrationstests vergleichen serielle und parallele Einzelfälle byteweise
für JSON, Details, Audit und Rohereignisse. Zusätzlich ist ein vollständiger
256/128/128-Trial-Lauf von `a01_minimal_2ch`, Seed 0, mit dem gespeicherten Gate
bytegleich in JSON, Details und Audit. Die optionale Rohprotokollierung ändert
somit die geprüften Ergebnisdaten nicht. Die frühere M3-Seed-7-Referenz wurde
bei der Sensor-/Audit-Integration in allen fünf Ergebnisdateien bytegleich reproduziert;
nach Wiederverwendung der generischen Auswerter bestehen außerdem die M3-Tests.

Die direkte Diagnose umfasst neun STDP-Paarungen, zwölf Aktuatorfälle, 24
Feedbackinterventionen und neun visuelle Signalpfade. Alle STDP-Gewichte stimmen
innerhalb 1e−7 mit der bestehenden Regel überein; alle Aktuatorfälle bestehen.
Die Feedback- und Signalpfade enthalten ausdrücklich auch gemessene Nullantworten.

## Berichte erneut erzeugen

Vom Projektverzeichnis:

```bash
python3 Experimente/m4/runner.py report --output Experimente/runs/m4-confirm
python3 Experimente/m4/diagnose.py --output Experimente/runs/m4-confirm
python3 -m unittest discover -s Experimente/m4/tests -v
```

[Runner-Bericht](summary.md), [Kennzahlen](summary.csv),
[Belegungs-/Ruhe-/Zeitbin-Kontraste](contrasts.csv),
[unabhängiger Datenaudit](diagnostics.json),
[Quelltext-/Programmhashes beim Abschluss](source-sha256.json),
[direkte Mechanismendiagnose](../m4-initial-gate/mechanisms.json),
[technische 20-Fall-Smoketests](../m4-initial-gate/interface-smokes.json).

Kein Fall erfüllt die M4-Erfolgskriterien. Die erste Vorhersageprobe erfolgt
nach 20,48 Sekunden visueller Kalibrierung; eine sofort am Trainingsende
vorhandene, kurzlebige Repräsentation wird damit nicht ausgeschlossen.
Die getrennten Fehlergrenzen und weiteren methodischen Grenzen stehen im
[wissenschaftlichen Bericht](../../M4_EXPERIMENT.md).
