# M10: Gewichtseffekte erreichen die Aktivität, selten die Entscheidung

Diagnosebericht vom **27.10.2026**. M10 untersucht die vorhandenen M9-Daten und
ergänzt passive Replaytraces auf denselben 20 Seeds. **Das ist eine retrospektive
explorative Ursachenanalyse, kein neuer Lernnachweis auf unabhängigen Seeds.**

Im gekoppelten Kombinationsarm verändert die Rücksetzung der Core-Gewichte
synaptische Eingänge und synchrone Potenziale in **160/160** Aktionsproben,
Spikezählmuster in **61/160** und die Ausleserentscheidung in **5/160**.
Die Gewichte sind also elektrisch wirksam; diese Wirkung führt im vorhandenen
Protokoll nur selten zu einer anderen Entscheidung und nicht zu einem
abgesicherten funktionalen Vorhersagevorteil.

[Automatischer Bericht](Experimente/m10-path-audit/summary.md) ·
[Diagnoseplan](Dokumentation/M10_METHODIK.md) ·
[Prüfnachweis](Experimente/m10-path-audit/verification.md).

Die anschließende [M10-B-Diagnose](M10B_EXPERIMENT.md) prüft die Wirkungsausrichtung
und zeigt, dass ein gemeinsamer Projektionsoffset die Fehler nicht allein erklärt.

## Umfang und Vorgehen

Retrospektiv ausgewertet werden alle **80 M9-Bestätigungsfälle**: vier Bedingungen,
20 Seeds 610–629, vier Arme, beide Belegungen und beide primären Prüfzeitpunkte.
Das ergibt 5.120 gezielte Gewichtsvergleiche, 1.280 A-/D-Vergleiche und 320
Belegungsvergleiche der Core-Gewichte. Die Quell-JSONs sind über SHA-256 fixiert.

Zusätzliche passive Messungen wiederholen die Kombination auf **allen 20 Seeds**.
Jeder Lauf reproduziert den ursprünglichen M9-Ergebnisbaum und seine sechs
CSV-Begleitdateien. Auf unabhängigen eingefrorenen Replayzweigen werden
unveränderte Gewichte, zurückgesetzte Core-Gewichte und sämtliche plastischen
Gewichte auf Anfangswert verglichen. Es werden nur neutrale Bilder und eigene
Aktionskopien eingespielt; kein Wirkungsbild gelangt in die Probe.

Die Traces erfassen tatsächliche synaptische Ankünfte mit signierter Amplitude,
Spikezeiten und Potenziale vor/nach 50 ms Startbild sowie 10/10/30 ms
Aktionsintegration. Potenziale werden auf **Neuronenkopien auf gemeinsame
Zeitpunkte projiziert**; Netzwerk, Warteschlangen und Lernregeln bleiben unverändert.
Die Eingänge sind Impulsamplituden des vorhandenen LIF-Modells, keine neu
eingeführten biophysikalischen Leitfähigkeitsströme.

## 1. Erfahrung hinterlässt Gewichtsunterschiede

Im gekoppelten Kombinationsarm unterscheiden sich die Core-Gewichte zwischen
normaler und umgekehrter Belegung auf **allen 20 Seeds**. Die mittlere Summe
absoluter Unterschiede beträgt **0,966982** über die vorhandenen Core-Kanten.
In `before`, `aged_frozen` und `scrambled` ist dieser Wert jeweils null.

Das beschreibt erfahrungsabhängige Gewichtsspuren und ist kein Nachweis, dass
die Wirkungsklasse funktional oder ausschließlich in diesen Gewichten gespeichert
wird. [Seedweise Gewichtsunterschiede](Experimente/m10-path-audit/mapping-weights.csv).

## 2. A und D aktivieren unterschiedliche Muster

Im gekoppelten Kombinationsarm sind die A-/D-Spikezählvektoren in **allen 80**
Belegungs-/Seed-/Zeitpunkt-Paaren verschieden. Trotzdem ordnet der feste visuelle
Ausleser beide Aktionen in **71/80** Paaren derselben Klasse zu: 35/40 sofort
und 36/40 nach Ruhe. Unterschiedliche Aktivität geht damit häufig nicht in eine
unterschiedliche Wirkungsvorhersage über.

Auch die eingefrorenen Kontrollarme können verschiedene Aktionen neuronal
unterscheiden. Diese Beobachtung allein belegt deshalb keine erlernte Zuordnung.
[Alle A-/D-Vergleiche](Experimente/m10-path-audit/action-discrimination.csv).

## 3. Gewichtsänderungen beeinflussen Spikes, selten die Klasse

Rücksetzung **nur der Core-Gewichte**, gekoppelter Arm, je 160 Aktionsproben:
20 Seeds × zwei Belegungen × zwei Zeitpunkte × zwei Aktionen.

| M9-Bedingung | Geänderte Spikezeiten/-ereignisse | Geändertes Spikezählmuster | Geänderte Vorhersage |
|---|---:|---:|---:|
| Referenz | 0 | 0 | 0 |
| Rekurrenz ×4 | 88 | 67 | 0 |
| STDP-Tau 100 ms | 0 | 0 | 0 |
| Kombination | 84 | 61 | 5 |

Die Ereignisprüfung erfasst auch veränderte Spikezeiten bei gleicher Zählung.
Stärkere Rekurrenz macht Gewichtsänderungen in einem Teil der Proben auf
Spikeebene sichtbar. Die meisten dieser Aktivitätsänderungen ändern die feste
Klassenentscheidung trotzdem nicht.

In der Kombination verändert die Rücksetzung den Decoderabstand zur richtigen
Klasse sofort in 28/80 Proben: Die trainierten Gewichte verschieben den Abstand
in 16 Fällen zur richtigen Klasse und in zwölf Fällen davon weg. Nach Ruhe sind
es 16 zur richtigen Klasse und 13 davon weg. Die übrigen Abstände bleiben gleich.
Diese deskriptiven Zählungen sind kein neuer Signifikanztest. Die fünf
Entscheidungsänderungen erzeugen keinen abgesicherten beidseitigen Lernvorteil;
die vollständige funktionale Prüfung steht im [M9-Bericht](M9_EXPERIMENT.md).

[Einzelne Gewichtsvergleiche und Decoderabstände](Experimente/m10-path-audit/weight-effects.csv).

## 4. Zeitlich abgeglichene Replaytraces bestätigen die elektrische Wirkung

Kombination, nur Core-Gewichte zurückgesetzt; je Arm dieselben 160 Proben:

| Arm | Veränderte Eingangsimpulssummen | Veränderte Potenziale am Prognosezeitpunkt | Veränderte Spikezählmuster | Veränderte Entscheidungen |
|---|---:|---:|---:|---:|
| Vor Training eingefroren | 0 | 0 | 0 | 0 |
| Mit Erfahrung gealtert, eingefroren | 0 | 0 | 0 | 0 |
| Gekoppelt trainiert | 160 | 160 | 61 | 5 |
| Entkoppelt trainiert | 160 | 160 | 70 | 8 |

Im gekoppelten Arm beträgt die mittlere größte absolute Potenzialdifferenz über
Core-Zellen am gemeinsamen Prognosezeitpunkt **0,274154** in den Modell-Einheiten.
Die eingefrorenen Negativkontrollen bleiben exakt gleich. Die entkoppelte
Kontrolle zeigt ebenfalls elektrische und Aktivitätseffekte: Solche Änderungen
allein sind daher kein Nachweis einer spezifisch gelernten Handlungswirkung.

Die alten M9-Werte `core_potentials` sind gespeicherte Zustände mit verschiedenen
letzten Aktualisierungszeitpunkten. Sie werden unverändert erhalten und nicht
als synchrone Spannungskarte interpretiert. Die obige Aussage verwendet die
zusätzlichen gemeinsamen Zeitpunkte und deren unabhängige LIF-Rekonstruktion.

[Zeitlich abgeglichene Vergleiche](Experimente/m10-path-audit/trace-effects.csv) ·
[Vollständige Traces](Experimente/m10-path-audit/traces/).

## Bedeutung und nächster Untersuchungsbedarf

M10 grenzt zwei Übergänge ein: Veränderte Eingangsimpulse/Potenziale schlagen nur
teilweise in veränderte Spikezählmuster um; diese Musteränderungen ändern noch
seltener die feste visuelle Klassifikation. Die Erklärung „die Gewichte haben
überhaupt keine Wirkung“ reicht für die Kombination somit nicht aus.

Das beweist nicht, dass allein der Ausleser falsch ist. Die Aktivitätsänderungen
können ebenso zu wenig Wirkungsspezifität besitzen oder nicht zur visuellen
Kalibrierung passen. Allgemeine Unauslesbarkeit oder das Fehlen jeglicher
Information folgt daraus nicht. Auch die vielen Proben desselben Seeds sind
keine zusätzlichen unabhängigen Replikate.

Vor einer biologischen Erweiterung sollte der nächste gezielte Versuch die
**Wirkungsspezifität der aktivierten Muster und ihre Passung zu visuellen
Zielmustern** prüfen. Stabilisierung allein behebt einen solchen Zuordnungsengpass
nicht nachweislich; M11 bleibt vom Ergebnis dieser weiteren Diagnose abhängig.

## Datenqualität

Alle 20 Replayläufe bestehen den Audit. Gemessen wurden **7.680 Phasentraces und
275.520 Ereignisse**. Ursprüngliche M9-CSV-Dateien sind jeweils bytegleich,
Ganzzahlen und Spikezeiten exakt reproduziert. Nur beim Vergleich serialisierter
JSON-Fließkommazahlen wird Rundung in der letzten f64-Stelle zugelassen.

Zusätzlich werden Phasen-Zähler und signierte/absolute Eingangsimpulssummen aus
den Ereignissen rekonstruiert. Die synchronen Potenziale werden unabhängig mit
Leck, Eingangsbatches, Reset und Refraktärzeiten des neutralen LIF-Modells
nachgerechnet; Toleranz für f32-Akkumulation: 2×10⁻⁵. Manipulierte Potenziale,
Impulse, Zeitpunkte und Quellmerkmale werden in Softwaretests abgewiesen.
Quellprüfsummen und Programmstand blieben während der Messung unverändert.

[Audit](Experimente/m10-path-audit/diagnostics.json) ·
[Provenienz](Experimente/m10-path-audit/provenance.json).
