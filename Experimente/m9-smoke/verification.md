# M9: Softwareverifikation vom 27.10.2026

**Technische Prüfung, kein wissenschaftlicher Lernnachweis.** Der archivierte
Kurzlauf verwendet Seed 690 mit 8 Trainingstrials, 8 Kalibriertrials und
8 Trials pro Online-Prüfphase in allen vier Bedingungen. Die wissenschaftlichen
Pläne für Pilot und Bestätigung wurden vor den technischen neuronalen Läufen
gespeichert und sind weiterhin unverändert; diese Reihen wurden nicht gestartet.

## Erfolgreiche Prüfungen

```bash
cargo test --offline --release --manifest-path NERVA_Modell/Experimente/Cargo.toml
cargo clippy --offline --manifest-path NERVA_Modell/Experimente/Cargo.toml --all-targets -- -D warnings
cargo fmt --manifest-path NERVA_Modell/Experimente/Cargo.toml -- --check
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m8/tests -v
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m9/tests -v
bash -n NERVA_Modell/Experimente/run.sh
```

Das Experimentpaket besteht seine 34 aktiven Rust-Tests. Drei ausdrücklich als
QEMU-Integration markierte Tests bleiben ignoriert. Python: drei M8- und acht
M9-Tests erfolgreich. Clippy, Formatierung und Shell-Syntaxprüfung erfolgreich.

Geprüft wurden insbesondere:

- Strenge Konfiguration: nur die vier Kombinationen, keine Zusatzparameter;
  M8 weist kombinierte Eingriffe weiterhin zurück.
- Kombinierte neuronale Läufe liefern bei paralleler Wiederholung bytegleiche
  JSON- und CSV-Dateien; vorhandene Ergebnisse werden nicht überschrieben.
- Referenz und beide Einzelbedingungen reproduzieren die M8-Neuronen,
  Anfangskanten, Normierung, Resultate sämtlicher Arme und sämtliche sechs
  CSV-Begleitdateien exakt bei gleichen technischen Trialzahlen und gleichem Seed.
- Der unabhängige Audit verwirft verfälschte effektive Zeitkonstanten und
  Zusatzspikezahlen. Ein verändertes Manifest kann den festen Plan nicht ersetzen.
- Die M9-Familienkorrektur 4×2 wird tatsächlich angewandt. Ein synthetischer
  Grenzfall besteht M9, scheitert aber wie vorgesehen an M8s unveränderter
  Familienkorrektur 13×2.
- Faktorielle Kontraste unterscheiden rohe Genauigkeit von Lernvorteilen
  gegenüber Kontrollen; visuelle Gewichtserhaltung wird aus den Summen berechnet.
- Kleine wissenschaftliche Trialzahlen werden vom Runner abgewiesen;
  technische Läufe sind als `smoke` gekennzeichnet und können nichts bestätigen.

## Archivierter technischer Lauf

```bash
python3 NERVA_Modell/Experimente/m9/run.py run --stage smoke --jobs 4 --output Messungen/Experimente/m9-smoke
```

Alle vier Ergebnisse wurden vollständig auditiert: 224 Replayzweige,
1.088 Trial-/Propagationszeilen und jeweils 9.728 Phasen-/Sensorzeilen.
Referenznormierung und ursprüngliche Verschaltung stimmen über die Bedingungen
überein. [Datenaudit](diagnostics.json) · [Technischer Bericht](summary.md).

Die Prozentwerte dieses kurzen Ein-Seed-Laufs dienen ausschließlich der
Softwareprüfung und werden nicht zur Auswahl von Bedingungen verwendet.
