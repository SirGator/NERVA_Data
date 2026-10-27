# M10-D: Rekurrente Erregung und Hemmung blockieren

Diagnose vom 27.10.2026 auf den bekannten M9-Kombinationsseeds 610–629.
Vier Varianten: unverändert, ohne rekurrente Erregung, ohne rekurrente Hemmung,
ohne beide. Alle vier Arme, beide Belegungen und zwei unabhängige Zeitpunkte.
128 Aktionsfenster je Seed; 2.560 insgesamt. Keine unabhängige Bestätigung,
keine neue neuronale Lernregel und keine Ausleserneukalibrierung.

[Zusammenfassung](summary.md) · [Bericht](../../M10D_EXPERIMENT.md) ·
[Methodik](../../Dokumentation/M10D_METHODIK.md) · [Verifikation](verification.md).

- `manifest.json`: vor Ausführung fixierte Quellen, SHA-256 und Definition.
- `provenance.json`: Programm-, Binär- und Manifestprüfsummen vor Ausführung.
- `execution.json`: tatsächliche Parallelität und vollständige Seedliste.
- `traces/`: Originalergebnis mit neuen Probeästen, Baseline/Aktionsereignissen,
  Zuständen, Sperrlisten und Queue-Stornierungen; sechs historische CSVs je Seed.
- `pairs.csv`: 1.280 A-/D-Paare, getrennt nach Seed/Arm/Belegung/Zeitpunkt/Variante.
- `summary.csv`: sämtliche Varianten und Kontrollen, Aktivität und Vorhersagen.
- `contrasts.csv`: deskriptive seed-gepaarte Kontroll- und Shamvergleiche.
- `diagnostics.json`: Quellreproduktion, Ereignis- und LIF-Audits.
- `raw-sha256.csv`: Prüfsummen aller Roh-JSONs und sechs historischen CSVs.

Blockiert werden ausschließlich ausgewählte Core→Core-Kanten. Motorische und
andere nicht-Core→Core-Signalwege bleiben erhalten. Die bekannte A-/D-Balance
ist Zusatzinformation für die Paar-Rangfolge; sie ist keine einzelne autonome
Wirkungsprognose. Pilotdaten werden [getrennt geführt](../m10d-smoke/README.md).
