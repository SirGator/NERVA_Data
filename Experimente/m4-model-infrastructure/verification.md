# M4-Modellinfrastruktur: Verifikationslauf

Ausgeführt am 15.10.2026. Dies ist ein technischer Verifikationsbericht,
kein Ergebnis der geforderten M4-Pilot-/20-Bedingungen-/Bestätigungsreihen.

Der verbindliche Runner, sein README-Schema und die 20 Fallkonfigurationen
fehlen. Die M4-JSON-CLI und diese Versuchsreihen wurden nicht ausgeführt.
Der Stand steht in ../../../Modell/M4_STATUS.md.

| Ausgeführte Prüfung | Ergebnis |
|---|---|
| Modelltests einschließlich sechs neuer Sensor-/Audit-Tests | 13 bestanden |
| Experimenttests mit bisherigen M3-/Agency-/Retention-Kontrollen | 30 bestanden |
| NERVA mit development, diagnostics, visualization; einschließlich Doc-Test | 322 bestanden |
| nerva-qemu mit lokalen QMP-Test-Sockets | 20 bestanden |
| Explizite QEMU-Regression: Live-VM, Aufzeichnung/Wiedergabe, Retention, serieller Gast | 4 bestanden |
| Clippy mit -D warnings: Modell, Experimente, NERVA, nerva-qemu | Bestanden |
| Formatprüfungen aller vier Pakete | Bestanden |
| Vollständiger vorhandener M3-Seed 7 gegen gespeicherte Referenz | Alle fünf Ergebnisdateien bytegleich |

Insgesamt 389 erfolgreiche Tests; zusätzlich gezielte Wiederholungen der sechs
Sensor-/Audit-Tests nach ergänzten Validierungen. CUDA wurde nicht aktiviert.
Es wurden keine neuronalen Lernregeln in NERVA geändert.

## Befehle

```bash
cargo test --offline --release --manifest-path Modell/Cargo.toml
cargo test --offline --release --manifest-path Experimente/Cargo.toml
cargo test --offline --release --manifest-path NERVA/Cargo.toml --features development,diagnostics,visualization
cargo test --offline --release --manifest-path nerva-qemu/Cargo.toml
cargo test --offline --release --manifest-path Modell/Cargo.toml --test visual_qemu -- --ignored --nocapture
cargo test --offline --release --manifest-path Experimente/Cargo.toml --test visual_qemu --test qemu -- --ignored --nocapture
./Experimente/run.sh m3 --seed 7 --jobs 1 --output /tmp/nerva-m4-infrastructure-m3-seed7
```

Für QEMU wurden die vorhandenen lokalen Programme unter Modell/.tools/qemu
mit QEMU_SYSTEM_X86_64, QEMU_FIRMWARE_DIR, QEMU_VGA_ROM, QEMU_MODULE_DIR und
LD_LIBRARY_PATH verwendet. Socket-/VM-Tests liefen außerhalb der Sandbox.

Verglichen wurden m3.json, m3-summary.md, m3-trials.csv, m3-spikes.csv und
motor-scan.csv mit Experimente/runs/m3-seed7-replay. Die vorliegende M3-Wiederholung
ist keine M4-Bestätigung und enthält weiterhin keinen M3-Lernnachweis.
