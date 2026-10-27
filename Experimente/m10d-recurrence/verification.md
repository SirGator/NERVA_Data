# M10-D: Verifikation vom 27.10.2026

Ausführung vom vollständigen Projektverzeichnis:

```bash
cargo test --offline --manifest-path NERVA/Cargo.toml --features development
cargo test --offline --release --manifest-path NERVA_Modell/Experimente/Cargo.toml --tests
cargo clippy --offline --manifest-path NERVA/Cargo.toml --all-targets --features development -- -D warnings
cargo clippy --offline --manifest-path NERVA_Modell/Experimente/Cargo.toml --all-targets -- -D warnings
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m10d/tests -v
```

Der neue Runtime-Test prüft unterwegs befindliche Ankünfte, zukünftige
Übertragungen, erhaltene andere Eingänge sowie atomare Ablehnung einer falschen
Synapsenliste. Der Rust-Integrationstest prüft alle Varianten mit identischer
Baseline, erhaltenen Ausgangspotenzialen und ursprünglichem Ausleser, ausbleibenden
gesperrten Ankünften sowie bytegleichen historischen CSVs.

Die vollständigen NERVA-Tests mit Entwicklungsfeature und alle 38 aktiven
Experimenttests bestanden. Drei ausdrücklich QEMU-abhängige Tests blieben
übersprungen; der M10-D-Versuch benötigt keine VM. Beide Clippy-Läufe bestanden
mit als Fehler behandelten Warnungen.

Alle fünf Python-Tests bestanden. Der vollständige technische Lauf in privaten
Verzeichnissen prüft 128 Aktionsfenster; manipulierte Sperrlisten, unerlaubte
Ankünfte, geänderte Ausgangszustände, Vorhersagen, Potenziale und Quell-Hashes
werden erkannt. Dieser Lauf wird nicht zusätzlich mit der Hauptdiagnose gepoolt.

Die Hauptdiagnose umfasst 20 bekannte Seeds, 2.560 Aktionsfenster und 10.240
Phasen. Für jeden Seed wird das vollständige ursprüngliche M9-Ergebnis nach
Entfernung ausschließlich der neuen Probeäste reproduziert. Alle 120 historischen
CSVs sind bytegleich. Shamproben entsprechen den ursprünglichen eingefrorenen
Proben. Alle Varianten beginnen nach exakt identischer Baseline; Kantenlisten,
neun Aktionskopie-Ankünfte, feste Ausleserentscheidungen und LIF-Endzustände werden
unabhängig nachgerechnet. Die erlaubte Potenzialtoleranz beträgt 2e-5.

Programm-, Binär-, Manifest- und Quellprüfsummen werden vor und nach Ausführung
verglichen. Die Rohdaten sind zusätzlich in `raw-sha256.csv` erfasst.

Dies ist eine Ursachenanalyse auf bekannten Seeds. Es gab keinen neuen
Ausleserfit und keine unabhängige Bestätigung des Lernens.

[Audit](diagnostics.json) · [Provenienz](provenance.json) ·
[Ergebnisbericht](../../M10D_EXPERIMENT.md).
