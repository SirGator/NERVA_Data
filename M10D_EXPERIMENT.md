# M10-D: Rekurrenz steuert Aktivität, ihre Blockade liefert keinen Lernnachweis

Abgeschlossen am **27.10.2026** auf den 20 bekannten M9-Kombinationsseeds
610–629. Ohne rekurrente Hemmung steigt die Core-Aktivität ungefähr auf das
Doppelte, ohne einen beidseitigen Vorhersagevorteil zu erzeugen. Ohne rekurrente
Erregung sinkt die mittlere Aktivität auf drei Spikes pro Aktion; auch das
verbessert die ursprüngliche Vorhersage im Mittel nicht.

Damit ist rekurrente Erregung unter diesen Zuständen für zusätzliche Aktivität
notwendig, und rekurrente Hemmung begrenzt diese Aktivität. **Keine der vier
Varianten liefert hier einen funktionalen Lernnachweis.** Die Diagnose auf
bekannten Seeds ist keine unabhängige Bestätigung und hat keinen neuen
Signifikanz- oder Lernschwellwert eingeführt.

[Vorab fixierte Methodik](Dokumentation/M10D_METHODIK.md) ·
[Automatischer Bericht](Experimente/m10d-recurrence/summary.md) ·
[Verifikation](Experimente/m10d-recurrence/verification.md).

## Was verändert wurde

Unverändertes M9-Training mit Core-Gewichten ×4 und STDP-Tau 100 ms:
256 Trainings-, 128 Kalibrier- und 128 Online-Testtrials. Vier Arme, beide
Belegungen und die unmittelbaren beziehungsweise nach unabhängigen 2 Sekunden
Ruhe erreichten Checkpoints wurden vollständig wiederholt. Der technische
[Pilot](Experimente/m10d-smoke/README.md) auf Seed 692 mit kleinen Trialzahlen
bleibt getrennt und wird nicht mit der Hauptdiagnose gepoolt.

Jede Aktionsprobe beginnt nach derselben neutralen Baseline aus identischen
Zuständen. Erst direkt vor der Aktion werden erregende Core→Core-Verbindungen,
hemmende Core→Core-Verbindungen oder beide gesperrt. Dabei werden auch noch
unterwegs befindliche Eingänge dieser Kanten entfernt. Gewichte,
Neuronenzustände, Uhrzeit, Aktionskopien und der bereits kalibrierte Ausleser
bleiben erhalten. Es gibt keinen Refit und keine neue neuronale Lernregel.

Motorische und andere nicht-Core→Core-Signalwege bleiben aktiv. Die Variante
„ohne beide“ ist deshalb kein Versuch, der sämtliche möglichen Rückkopplungen
entfernt. Die Sperre gilt nur für den danach verworfenen Probeast, nicht für
Training, Baseline oder andere Originalmessungen.

## Ergebnisse im gekoppelten Arm

Mittel über 20 Seeds und beide Belegungen. Je Zeitpunkt/Variante liegen
40 A-/D-Paare beziehungsweise 80 einzelne Antworten vor. Die Paare sind keine
40 unabhängigen Seed-Replikate.

| Variante | Sofort: Einzelvorhersage | Sofort: Paar-Rangfolge | Spikes/Aktion | Nach Ruhe: Einzelvorhersage | Nach Ruhe: Paar-Rangfolge | Spikes/Aktion |
|---|---:|---:|---:|---:|---:|---:|
| Unverändert | 51,25 % | 42,50 % | 17,200 | 50,00 % | 45,00 % | 15,425 |
| Ohne rekurrente Erregung | 48,75 % | 47,50 % | 3,000 | 48,75 % | 47,50 % | 3,000 |
| Ohne rekurrente Hemmung | 47,50 % | 40,00 % | 31,950 | 50,00 % | 45,00 % | 31,850 |
| Ohne beide | 48,75 % | 47,50 % | 3,000 | 48,75 % | 47,50 % | 3,000 |

Die Einzelvorhersage ist der ursprüngliche feste visuelle Spikezähl-Ausleser.
Die Paar-Rangfolge ist die M10-B-Diagnose mit beiden Antworten und deren
bekannter Balance; sie ist keine zusätzliche autonome Vorhersageleistung.

Ohne Hemmung steigt auch die Zahl aktiver Core-Zellen im Mittel von 12,738 auf
17,638 sofort und von 11,925 auf 17,213 nach Ruhe. Ohne Erregung sind es 3,000
bei beiden Zeitpunkten. Die höchste beobachtete Spikezahl einer einzelnen Zelle
beträgt im gekoppelten Arm fünf ohne Hemmung, fünf/vier in der Referenz und eins
ohne Erregung beziehungsweise ohne beide. Diese Aktivitätsmaße allein sind
keine Messung von Lernfortschritt oder allgemeiner Netzwerkstabilität.

## Wirkung auf einzelne Antworten

Je Zeitpunkt/Variante 80 Aktionsfenster, verglichen mit der unveränderten
Antwort aus demselben Checkpoint:

| Eingriff | Sofort: anderes Spikezählmuster | Andere Vorhersage | Nach Ruhe: anderes Spikezählmuster | Andere Vorhersage |
|---|---:|---:|---:|---:|
| Ohne rekurrente Erregung | 72/80 | 4/80 | 72/80 | 5/80 |
| Ohne rekurrente Hemmung | 48/80 | 11/80 | 45/80 | 8/80 |
| Ohne beide | 72/80 | 4/80 | 72/80 | 5/80 |

Die Rekurrenz greift somit messbar in die Antworten ein. Dass viele
Spikezählmuster, aber weniger Entscheidungen wechseln, passt zur früheren
Ausleserdiagnose. Ein Wechsel allein bedeutet keine Korrektur: Die tatsächliche
Wirkungsrichtung muss gesondert bewertet werden.

## Belegungsabhängigkeit und Kontrollen

Ohne Hemmung liegen die Einzelvorhersagen sofort bei **55 % normal und 40 %
umgekehrt**, nach Ruhe bei **55 % und 45 %**. In der unveränderten Referenz
sind es sofort 50/52,5 % und nach Ruhe 47,5/52,5 %.

Die deskriptive Differenz nach Hemmungsblockade gegenüber Sham beträgt sofort
normal +5 Prozentpunkte, Bootstrapintervall [−5; +15], umgekehrt −12,5 Punkte
[−25; −2,5]. Nach Ruhe betragen die Differenzen +7,5 [0; +15] und −7,5
[−15; 0]. Es gibt somit keinen gleichgerichteten Vorteil in beiden Belegungen.

Auch die diagnostische Rangfolge ist asymmetrisch: Nach Ruhe steigt sie normal
von 40 auf 60 %, umgekehrt fällt sie von 50 auf 30 %. Die zugehörigen
deskriptiven Differenzintervalle sind [+5; +40] und [−40; 0] Prozentpunkte.
Diese ausgewiesenen Teilkontraste werden nicht als neue Signifikanzbefunde
oder Beleg gezielt falschen Lernens behandelt.

Paar-Rangfolge sofort / nach Ruhe, sämtliche Kontrollarme:

| Variante | Vor Training | Gealtert eingefroren | Gekoppelt | Entkoppelt |
|---|---:|---:|---:|---:|
| Unverändert | 50 / 50 % | 55 / 50 % | 42,5 / 45 % | 50 / 50 % |
| Ohne Erregung | 50 / 50 % | 50 / 50 % | 47,5 / 47,5 % | 50 / 50 % |
| Ohne Hemmung | 50 / 50 % | 57,5 / 50 % | 40 / 45 % | 50 / 50 % |
| Ohne beide | 50 / 50 % | 50 / 50 % | 47,5 / 47,5 % | 50 / 50 % |

Die scheinbare Rangfolgenannäherung an 50 % ohne Erregung wird nicht als
Lerngewinn gewertet: Die Einzelvorhersage sinkt dabei und ein Vorteil gegenüber
den Kontrollarmen fehlt. Zwei der 40 gekoppelten Paare haben dort einen
Projektionsgleichstand, der jeweils als 0,5 bewertet wird.

Alle Vergleiche sind über dieselben 20 Seeds gepaart, getrennt nach Belegung
und Zeitpunkt. Die 95-%-Intervalle stammen aus den vorab definierten 4.000
Bootstrapresamples mit Seed 1234 und sind deskriptiv. Es wurden keine Seeds,
Verbindungen oder Ausleser nachträglich zur Leistungssteigerung ausgewählt.
[Alle 240 Kontrollkontraste](Experimente/m10d-recurrence/contrasts.csv) ·
[Alle 1.280 Paare](Experimente/m10d-recurrence/pairs.csv).

## Verifikation

Die gesamte Hauptdiagnose umfasst **2.560 Aktionsfenster, 10.240 Phasen und
264.399 Ereignisse**. In den Probeästen wurden insgesamt 84 bereits unterwegs
befindliche ausgewählte Ankünfte storniert. Gesperrte Kanten liefern danach
keine Ankunft während der Aktion. Alle neun Aktionskopie-Ankünfte pro Fenster
bleiben erhalten.

Für jeden Seed reproduziert der unveränderte Anteil das vollständige
ursprüngliche M9-Ergebnis, und alle **120 historischen CSVs sind bytegleich**.
Shamproben stimmen mit den ursprünglichen eingefrorenen Aktionsproben überein.
Baselines und Anfangspotenziale/Refraktärzustände sind zwischen Varianten
identisch. Die festen Ausleserentscheidungen und die neutralen LIF-Trajektorien
werden unabhängig nachgerechnet. Maximaler Potenzialfehler: **1,987 × 10⁻⁷**,
unter der festgelegten Toleranz 2 × 10⁻⁵.

Die vollständigen NERVA- und 38 aktiven Experimenttests sowie beide Clippy-Läufe
bestanden; drei ausdrücklich QEMU-abhängige Tests blieben übersprungen.
Fünf Python-Tests einschließlich Manipulationserkennung bestanden.
[Audit](Experimente/m10d-recurrence/diagnostics.json) ·
[Provenienz](Experimente/m10d-recurrence/provenance.json) ·
[Rohdatenprüfsummen](Experimente/m10d-recurrence/raw-sha256.csv).

## Konsequenz für den Forschungsplan

Eine pauschale Entfernung der Hemmung beseitigt den Engpass hier nicht. Sie
verstärkt Aktivität und verändert Antworten belegungsabhängig. Das Abschalten
rekurrenter Erregung entfernt zusätzliche Aktivität, erschließt aber ebenfalls
keine zuverlässige Wirkungsvorhersage. Daraus folgt weder eine allgemeine
Ungeeignetheit der Rekurrenz noch die Notwendigkeit einer bestimmten neuen
biologischen Lernregel.

Ein sinnvoller nächster Diagnoseschritt wäre, aus diesen eingefrorenen
Checkpoints **direkte Aktionskopieantwort und durch gelernte Core-Gewichte
veränderte Antwort durch gekreuzte Gewichts- und Übertragungseingriffe** zu
trennen. Die Gewichtsrücksetzungen von M10 und die Sperren von M10-D wurden
bisher separat getestet. Ein solcher Folgeversuch wäre neu festzulegen und
würde noch keine Bestätigung auf neuen Seeds ersetzen.

Der gekreuzte Folgeversuch ist inzwischen als [M10-E](M10E_EXPERIMENT.md)
ausgeführt. Seine Rücksetzung erfolgt nach identischer Baseline, um alle
Aktions-Anfangszustände gleich zu halten.
