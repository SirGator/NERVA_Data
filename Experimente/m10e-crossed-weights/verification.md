# M10-E: Verifikation vom 27.10.2026

Vom vollständigen Projektverzeichnis:

```bash
cargo test --offline --release --manifest-path NERVA_Modell/Experimente/Cargo.toml --tests
cargo clippy --offline --manifest-path NERVA_Modell/Experimente/Cargo.toml --all-targets -- -D warnings
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m10e/tests -v
```

Der neue Rust-Test prüft identische Baselines und Aktions-Anfangszustände,
Rücksetzung unmittelbar vor der Aktion und exakte Antwortgleichheit bei
gleichzeitig gesperrten geänderten Kanten. Die ursprünglichen sechs CSVs
bleiben bytegleich. Vorhandene M9/M10/M10-D-Regressionstests bleiben erhalten.

Alle 39 aktiven Experimenttests und Clippy mit als Fehler behandelten Warnungen
bestanden. Drei ausdrücklich QEMU-abhängige Tests blieben übersprungen; für
diesen Versuch wird keine VM benötigt. Die NERVA-Runtime wurde in M10-E nicht
verändert; deren Sperr-API wurde bereits in M10-D getestet.

Alle sechs Python-Tests bestanden. Der vollständige technische Lauf findet in
privaten Ausgabeverzeichnissen statt und wird nicht zusätzlich gepoolt.
Manipulierte Gewichtslisten, Resetzeiten, Aktions-Anfangszustände,
Negativkontrollantworten, Vorhersagen, trainierte M10-D-Replikate sowie Quell-
und Manifestprüfsummen werden abgewiesen.

Die Hauptdiagnose umfasst 20 bekannte Seeds und 5.120 Aktionsfenster mit
20.480 Phasen. Das ursprüngliche vollständige M9-Ergebnis und alle 120
historischen CSVs werden reproduziert. Sämtliche vier trainierten Zweige
entsprechen den archivierten M10-D-Traces. In allen acht Varianten stimmen
Baseline, Anfangspotenziale und Refraktärzustände überein.

Änderungslisten werden unabhängig gegen Trainings-/Anfangsgewichte geprüft,
Sperrlisten gegen Topologie und Polarität. Keine gesperrten Ankünfte erreichen
das Aktionsfenster; neun Aktionskopie-Ankünfte bleiben erhalten. Ereigniszähler,
feste Ausleserentscheidungen und neutrale LIF-Trajektorien werden unabhängig
nachgerechnet, Potenzialtoleranz 2e-5. Bei vollständiger Sperre aller geänderten
Kanten müssen beide Gewichtszustände identische Aktionsverläufe liefern.

Gewichtsreset ist nach der Baseline und damit methodisch anders als die frühere
M10-Rücksetzung. Nicht gesperrte, unterwegs befindliche Impulse behalten ihre
vorherige Amplitude; der Zellzustand bleibt erhalten. Die Auswertung isoliert
deshalb nicht sämtliche frühere Gedächtniseinflüsse.

Programm-, Binär-, Manifest- und Quellprüfsummen werden vor und nach Ausführung
verglichen. Die Rohdatenprüfsummen stehen separat in `raw-sha256.csv`.

[Audit](diagnostics.json) · [Provenienz](provenance.json) ·
[Bericht](../../M10E_EXPERIMENT.md).
