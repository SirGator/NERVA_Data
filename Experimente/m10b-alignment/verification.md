# M10-B: Auswertungsprüfung vom 27.10.2026

**Retrospektive Diagnose auf vorhandenen Daten.** Keine neuronalen Läufe,
keine Ausleserfits an Aktionslabels, keine neue unabhängige Bestätigung.

```bash
python3 -W error::ResourceWarning -m unittest discover -s NERVA_Modell/Experimente/m10b/tests -v
python3 NERVA_Modell/Experimente/m10b/run.py plan --source Messungen/Experimente/m9-v2-confirm --output Messungen/Experimente/m10b-alignment
python3 NERVA_Modell/Experimente/m10b/run.py run --source Messungen/Experimente/m9-v2-confirm --output Messungen/Experimente/m10b-alignment
```

Alle sechs Tests bestanden. Synthetische Fälle unterscheiden korrekte
Wirkungsrichtung bei gemeinsamem Bias, orthogonale Aktionsunterschiede,
Belegungsumkehr und entartete visuelle Achsen. Manipulierte ursprüngliche
Vorhersagen und veränderte Quelldateien werden abgewiesen. Die End-to-End-Prüfung
verwendet private Kopien der M9-Kurzlaufdaten und wird nicht mit den Hauptdaten
gepoolt.

Die vollständige Auswertung umfasst **80 Quell-JSONs und 3.840 Paare**. Sie
rekonstruiert die ursprünglichen Vorhersagen aus den bestehenden visuellen
Mittelwerten, Skalierungen und Zentroiden sowie die ursprüngliche Genauigkeit
jedes unveränderten Checkpointpaars. Die algebraische Identität zwischen
Projektionsscores und Differenz der Zentroidabstände wird geprüft. Entartete
visuelle Achsen: null.

Quelle, Manifest und Auswertungsprogramme stimmen nach Abschluss mit den
gespeicherten SHA-256-Prüfsummen überein. Die Paar-Rangfolge verwendet keine
neuronalen Änderungen; die bekannte A-/D-Balance ist zusätzliche Information
für die Diagnose und darf nicht als neue unabhängige Einzelvorhersage gelten.

[Audit](diagnostics.json) · [Provenienz](provenance.json) ·
[Ergebnisbericht](../../M10B_EXPERIMENT.md).
