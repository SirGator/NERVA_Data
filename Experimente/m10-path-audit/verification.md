# M10: Replay- und Ereignisprüfung

Abschluss am **27.10.2026**. Retrospektive Diagnose aller 80 M9-Quellfälle und
20 zusätzliche passive Kombinations-Replays auf den vorhandenen Seeds 610–629.
Quellprüfsummen und Diagnosemanifest wurden vor den zusätzlichen Replays
gespeichert. Die Wahl der Diagnose beruht auf bekannten M9-Ergebnissen; sie
ist keine neue unabhängige Bestätigung.

## Erfolgreiche Softwareprüfungen

```bash
cargo test --offline --release --manifest-path NERVA_Modell/Experimente/Cargo.toml
cargo test --offline --release --manifest-path NERVA_Modell/Modell/Cargo.toml --test m6 --test experimental_parameters
cargo clippy --offline --manifest-path NERVA_Modell/Experimente/Cargo.toml --all-targets -- -D warnings
cargo fmt --manifest-path NERVA_Modell/Modell/Cargo.toml -- --check
cargo fmt --manifest-path NERVA_Modell/Experimente/Cargo.toml -- --check
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m8/tests -v
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m9/tests -v
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m10/tests -v
```

37 aktive Rust-Tests des Experimentpakets und fünf gezielte Modelltests bestanden.
Drei ausdrücklich markierte QEMU-Integrationstests bleiben ignoriert. Python:
drei M8-, dreizehn M9- und vier M10-Tests erfolgreich. Clippy und Formatierung
erfolgreich. Technische Tests verwenden private Kopien der M9-Kurzlaufdaten und
werden nicht mit den wissenschaftlichen Daten gepoolt.

Die neuen Tests prüfen insbesondere:

- Passive Traces reproduzieren M9 und alle sechs CSV-Dateien; wiederholte
  Trace-Läufe stimmen vollständig überein.
- Ganzzahlen bleiben exakt; der Ergebnisvergleich toleriert lediglich JSON-f64-
  Rundung bis acht Maschinen-Epsilon relativ beziehungsweise absolut. Größere
  Änderungen und zusätzliche ursprüngliche Felder werden verworfen.
- Der Audit verwirft manipulierte Potenziale, Eingangsimpulssummen, Zeitgrenzen
  und ursprüngliche Vorhersagemerkmale sowie veränderte Quelldateien.
- Alte gespeicherte Zustandswerte und zeitlich abgeglichene Potenziale bleiben
  getrennte Größen; eingefrorene Negativkontrollen bleiben unverändert.

## Vollständige Diagnose

```bash
python3 NERVA_Modell/Experimente/m10/run.py run --jobs 8 --source Messungen/Experimente/m9-v2-confirm --output Messungen/Experimente/m10-path-audit
```

Alle 20 Traces bestanden die vollständige Prüfung: 7.680 Phasen und 275.520
Ereignisse; die retrospektiven Tabellen enthalten 5.120 Gewichtsinterventions-,
1.280 A-/D- und 320 Gewichtsvergleiche zwischen Belegungen.

Der Audit prüft Ereigniszeiten, Endpunkte, Polaritäten, Spikezähler, signierte
und absolute Eingangsimpulssummen sowie Aktionskopien. Er rekonstruiert synchrone
Potenziale unabhängig aus Anfangspotenzialen, Ereignisbatches, Leck, Reset und
Refraktärzuständen des neutralen LIF-Modells. Toleranz für f32-Akkumulation:
2×10⁻⁵; dies ist kein neuronaler Modellparameter.

Die ursprünglichen M9-Ergebnisbäume stimmen bis auf zulässige JSON-Rundung
überein. Alle 120 ursprünglichen CSV-Dateien der Replayfälle sind bytegleich mit
ihren Quellen. Die 80 Eingabe-JSONs stimmen weiterhin mit den SHA-256-Prüfsummen
im [Manifest](manifest.json) überein. Quellen, Programm und Diagnoseplan stimmen
nach Abschluss mit [provenance.json](provenance.json) überein.
[raw-sha256.csv](raw-sha256.csv) enthält Größe und SHA-256 aller 140 neuen
Rohdateien (20 JSON-Ergebnisse und 120 CSV-Dateien).

[Ergebnisbericht](../../M10_EXPERIMENT.md) · [Datenaudit](diagnostics.json).
