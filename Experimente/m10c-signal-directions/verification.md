# M10-C: Verifikation vom 27.10.2026

```bash
python3 -m unittest discover -s NERVA_Modell/Experimente/m10c/tests -v
python3 NERVA_Modell/Experimente/m10c/run.py plan --source Messungen/Experimente/m10-path-audit --output Messungen/Experimente/m10c-signal-directions
python3 NERVA_Modell/Experimente/m10c/run.py run --source Messungen/Experimente/m10-path-audit --output Messungen/Experimente/m10c-signal-directions
```

Alle fünf Tests bestanden. Synthetische Trajektorien prüfen verlorene
Refraktäreingänge, Leckgewichtung, Resetabzug und die mögliche Umkehr des
Restpotenzials bei bereits erzeugtem Spike. Gleichzeitige Erregung/Hemmung wird
als gemeinsames Ereignispaket verarbeitet. Manipulierte Potenziale, fehlende
Spikes und veränderte Manifeste werden erkannt. Der technische End-to-End-Test
verwendet Seed 610 in einem temporären Ausgabeverzeichnis, ohne Quelldaten zu
verändern oder seine Ergebnisse zusätzlich zu poolen.

Die vollständige Auswertung prüft 20 Quelltraces gegen ihre ursprünglichen
M9-Ergebnisse und auditiert 7.680 Phasen / 275.520 Ereignisse. Für alle 1.920
Aktionsfenster werden LIF-Endpotenziale, Refraktärzeiten und die additive Bilanz
rekonstruiert. Maximaler Potenzialfehler 3,2843973041263297e-7 bei erlaubten
2e-5. Gruppen- und Synapsensummen stimmen mit den Gesamtprojektionen überein;
Spikeprojektionen reproduzieren die ursprüngliche M10-B-Achse.

Keine neuen neuronalen Läufe, Decoderfits oder unabhängigen Bestätigungsseeds.
Manifest-, Programm- und Quellprüfsummen stimmen nach Abschluss weiterhin.

[Audit](diagnostics.json) · [Provenienz](provenance.json) ·
[Bericht](../../M10C_EXPERIMENT.md).
