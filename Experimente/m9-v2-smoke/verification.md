# M9-v2: Softwareverifikation vom 27.10.2026

**Technischer Kurzlauf, kein wissenschaftlicher Lernnachweis.** Die vier Fälle
verwenden Seed 692 und Trialzahlen 8/8/8. Die Pläne für Pilot und 20 neue
Bestätigungsseeds wurden vor dem ersten neuronalen v2-Kurzlauf gespeichert.
Die wissenschaftlichen Reihen sind noch nicht gestartet.

## Erfolgreiche Prüfungen

```bash
cargo test --offline --release --manifest-path NERVA_Modell/Experimente/Cargo.toml
cargo test --offline --release --manifest-path NERVA_Modell/Modell/Cargo.toml --test m6 --test experimental_parameters
cargo clippy --offline --manifest-path NERVA_Modell/Modell/Cargo.toml --all-targets -- -D warnings
cargo clippy --offline --manifest-path NERVA_Modell/Experimente/Cargo.toml --all-targets -- -D warnings
cargo fmt --manifest-path NERVA_Modell/Modell/Cargo.toml -- --check
cargo fmt --manifest-path NERVA_Modell/Experimente/Cargo.toml -- --check
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m8/tests -v
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m9/tests -v
```

35 aktive Rust-Tests des Experimentpakets und fünf gezielte Modelltests bestanden.
Drei ausdrücklich markierte QEMU-Integrationsprüfungen bleiben ignoriert.
Python: drei M8- und dreizehn M9-Tests bestanden. Beide Clippy- und
Formatierungsprüfungen erfolgreich.

Insbesondere geprüft:

- Zusätzliche Gewichtseingriffe verändern weder ursprüngliche Arm-Ergebnisse
  noch die sechs historischen CSV-Messdateien; v1 und M8 bleiben reproduzierbar.
- Wiederholte kombinierte v2-Läufe liefern identische Ergebnisse einschließlich
  der 96 Gewichtseingriffszweige pro Fall/Seed.
- Unveränderte Eingriffe reproduzieren die ursprünglichen Checkpoint-Vorhersagen
  und Spikezeiten. Eingefrorene Kontrollarme haben keine Gewichtsänderungen und
  identische Antworten unter sämtlichen Eingriffen.
- Der unabhängige Audit rekonstruiert die Vorhersagen aus gespeicherten
  Decoderparametern und Spikezahlen. Er verwirft manipulierte Gewichtsänderungen,
  Zähler, Zeitpunkte, Decoderparameter und Replay-/Elterninvarianten.
- Zehn Seeds reichen auch bei perfekten synthetischen Ergebnissen nicht für
  einen v2-Nachweis. Die Gewichtsanforderung verlangt einen Verlust in beiden
  Belegungen; ein einseitiger Verlust reicht nicht.
- Die ursprünglichen v1-Pläne werden nicht als v2-Pläne interpretiert oder
  überschrieben. Wissenschaftliche Trialzahlen bleiben fest.

## Archivierter Kurzlauf

```bash
python3 NERVA_Modell/Experimente/m9/run.py run --stage smoke --jobs 4 --output Messungen/Experimente/m9-v2-smoke
```

Alle vier Fälle bestanden den vollständigen Audit: 224 ursprüngliche
Replayzweige, **384 zusätzliche Gewichtseingriffszweige**, 1.088 Trial- und
Propagationszeilen sowie je 9.728 Phasen-/Sensorzeilen.
[Bericht](summary.md) · [Datenaudit](diagnostics.json).

Die Rücksetzung prüft den Gewichtsbeitrag bei festem Ausleser und erhaltenem
dynamischem Ausgangszustand. Sie beweist keine ausschließliche Speicherung in
Gewichten. Reisende Impulse behalten ihre bei Emission festgelegten Amplituden.
Die Kurzlaufwerte werden nicht zur Auswahl oder Nachjustierung benutzt.
