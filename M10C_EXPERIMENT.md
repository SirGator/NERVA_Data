# M10-C: Unpassende Ausrichtung ist bereits in der Eingangsbilanz sichtbar

Zusatzdiagnose vom **27.10.2026** auf den vorhandenen M10-Traces der Kombination.
Die gesamten synaptischen Eingangsimpulse zeigen entlang der festen neuronalen
Gewichtung des bisherigen visuellen Auslesers in **23 von 40 A-/D-Paaren** in die
unpassende Richtung, sowohl sofort als auch nach Ruhe. Die spätere Verarbeitung
verändert dieses Vorzeichen nur in wenigen Paaren.

Damit reicht eine Erklärung allein durch die abschließende Spikebildung oder
Entscheidungsschwelle nicht aus. **Die Eingänge enthalten allerdings schon
rekurrente Rückkopplung.** Die Bilanz lokalisiert daher noch keine ursprüngliche
Ursache und ist kein Beweis gegen andere neuronale Repräsentationen.

[Methodik](Dokumentation/M10C_METHODIK.md) ·
[Automatische Zusammenfassung](Experimente/m10c-signal-directions/summary.md) ·
[Prüfnachweis](Experimente/m10c-signal-directions/verification.md).

## Was genau untersucht wurde

Alle 20 vorhandenen Kombinations-Traces, Seeds 610–629: vier Arme, zwei
Belegungen, zwei Zeitpunkte und drei Gewichtseingriffe. Das ergibt **960 Paare
und 1.920 einzelne Aktionsfenster**. Es wurden keine neuen neuronalen Läufe,
Lernregeln oder Ausleserfits hinzugefügt. Diese retrospektive explorative Analyse
verwendet dieselben bekannten Seeds und ist keine unabhängige Bestätigung.

Die Ausleserkoeffizienten stammen unverändert aus den visuellen Spikezählmustern.
Ihre Anwendung auf Eingangsimpulse und Potenziale beschreibt den Antrieb in
ausleserrelevante Neuronen. **Das sind keine eigenständig kalibrierten
Eingangs- oder Potenzialklassifikatoren.** Ein positives Vorzeichen bedeutet
Passung zur bewerteten Wirkungsrichtung auf genau dieser festen Gewichtung.
Die verschiedenen physikalischen Größen werden nicht als vergleichbare Stärken
oder Vorhersagegenauigkeiten behandelt.

## Vorzeichen der Beiträge im gekoppelten Arm

Unveränderte trainierte Gewichte; je Zeitpunkt 40 Paare aus 20 Seeds und beiden
Belegungen. Die 40 Paare sind keine 40 unabhängigen Seed-Replikate.

| Signal | Sofort: positiv / negativ | Nach Ruhe: positiv / negativ |
|---|---:|---:|
| Alle Eingangsimpulse | 17 / 23 | 17 / 23 |
| Nach Refraktärfilter | 16 / 24 | 16 / 24 |
| Angenommene Eingänge mit Leck bis zum Endzeitpunkt | 17 / 23 | 17 / 23 |
| Antrieb einschließlich abgeklungenem Anfangszustand, vor Resetabzug | 17 / 23 | 17 / 23 |
| Restpotenzial nach den beobachteten Spikes und Resets | 19 / 21 | 20 / 20 |
| Spikezählmuster, identisch mit M10-B | 17 / 23 | 18 / 22 |

Es gibt in diesen Zeilen keine Gleichstände. Die vollständigen acht Signaltypen
stehen in [summary.csv](Experimente/m10c-signal-directions/summary.csv), die
Einzelwerte einschließlich Belegung in [signals.csv](Experimente/m10c-signal-directions/signals.csv).

Die ähnlichen Gesamthäufigkeiten verbergen einzelne Wechsel. Der Refraktärfilter
ändert je Zeitpunkt ein Paar von positiv zu negativ; die Leckgewichtung ändert
ein anderes von negativ zu positiv. Von leckgewichteten angenommenen Eingängen
zu Spikezahlen wechseln sofort ein positives Paar nach negativ und ein negatives
nach positiv. Nach Ruhe wechseln ein positives nach negativ und zwei negative
nach positiv. Die Vorzeichen stimmen an diesem letzten Vergleich also in
**38/40 beziehungsweise 37/40 Paaren** überein.
[Alle Übergänge](Experimente/m10c-signal-directions/transitions.csv).

## Warum das Restpotenzial kein einfacher Zwischenschritt ist

Die Analyse rekonstruiert für jedes Neuron die Bilanz:

`Endpotenzial = abgeklungener Anfangszustand + leckgewichtete Eingänge
− verworfene Refraktäreingänge − leckgewichtete Resetabzüge`.

Ein Spike setzt das Potenzial zurück. Der spätere Restwert kann dadurch eine
andere Richtung haben, obwohl ein relevanter Spike bereits erzeugt wurde.
Die 19 beziehungsweise 20 positiven Restpotenzialprojektionen sind deshalb
kein Nachweis einer besseren Vorhersage vor der Spikebildung.

Die Bilanz verwendet aufgezeichnete Spikes und ihre tatsächlich erzeugten
rekurrenten Eingänge. Der rechnerische Antrieb vor Resetabzug ist **keine
Resimulation eines Netzwerks ohne Resets**; dort könnten andere Spikes und
andere Rückkopplungen entstehen.

## Quellgruppen und Kontrollen

Alle Beiträge sind nach Aktionskopie, rekurrenter Erregung, rekurrenter Hemmung,
visuellen Neuronen und sonstigen Quellen aufgeteilt. Die sonstigen Quellen
umfassen in dieser Topologie die motorischen Neuronen. Direkte visuelle
Beiträge sind in sämtlichen untersuchten Aktionsfenstern null, wie für die
Vorhersage vor dem Wirkungsbild erwartet. Aktionskopien zeigen im gekoppelten
Arm je Zeitpunkt 20 positive und 20 negative leckgewichtete angenommene
Beiträge; rekurrente Erregung 18/22 und rekurrente Hemmung 15/25.

Diese Gruppen sind Teile derselben gekoppelten Trajektorie. Ihre Vorzeichen
beweisen nicht, dass Entfernen von Hemmung oder einer bestimmten Synapse das
Lernen verbessern würde. Dazu wäre ein gezielter Eingriff erforderlich.
[Quellgruppen](Experimente/m10c-signal-directions/sources.csv) ·
[84.327 synaptische Beitragszeilen](Experimente/m10c-signal-directions/edges.csv).

Positive Spikezählrichtungen je 40 Paare, sofort / nach Ruhe:

| Arm oder Eingriff | Positive Paare |
|---|---:|
| Vor Training eingefroren | 20 / 20 |
| Gealtert eingefroren | 22 / 20 |
| Gekoppelt trainiert | 17 / 18 |
| Entkoppelt trainiert | 20 / 20 |
| Gekoppelt, Core-Gewichte zurückgesetzt | 16 / 18 |
| Gekoppelt, alle plastischen Gewichte zurückgesetzt | 16 / 18 |

Das reproduziert M10-B und liefert keinen neuen funktionalen Lernnachweis.
Die unveränderten M9-Kriterien und ihre negativen Ergebnisse bleiben maßgeblich.

## Verifikation und nächster gezielter Schritt

Die vollständigen ursprünglichen Ergebnisse und Traces wurden erneut auditiert:
20 Quelldateien, 7.680 Phasen und 275.520 Ereignisse. Für sämtliche 1.920
Aktionsfenster stimmen rekonstruierte Potenziale und Refraktärzustände mit den
Quellen überein. Größter Potenzialfehler: **3,285 × 10⁻⁷**, unter der festgelegten
f32-Toleranz 2 × 10⁻⁵. Gruppen- und Synapsensummen reproduzieren die
Gesamtprojektionen; Spikeprojektionen reproduzieren die M10-B-Kontraste.
Fünf Tests prüfen Bilanz, gleichzeitige Erregung/Hemmung, Manipulationserkennung,
Skalierung/Belegungsumkehr und einen vollständigen technischen Seed-Durchlauf.

Der nächste gezielte Versuch sollte die **Rolle der rekurrenten Beiträge durch
kontrollierte Eingriffe in identische eingefrorene Checkpoints** untersuchen.
Dabei müssen Aktionskopie und rekurrente Erregung/Hemmung getrennt geprüft und
Aktivität, Richtung und ursprüngliche Vorhersage gemeinsam bewertet werden.
Die vorhandene Bilanz allein rechtfertigt weder eine neue Lernregel noch das
gezielte Verstärken eines nach Ergebnis ausgewählten Signalwegs.

[Audit](Experimente/m10c-signal-directions/diagnostics.json) ·
[Fixierte Quellen und Methode](Experimente/m10c-signal-directions/manifest.json) ·
[Programmprüfsummen](Experimente/m10c-signal-directions/provenance.json).
