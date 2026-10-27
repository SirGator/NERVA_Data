# M10-E: Core-Gewichte wirken über Rekurrenz, ohne zuverlässigen Vorhersagegewinn

Abgeschlossen am **27.10.2026** auf den bekannten Kombinationsseeds 610–629.
Der gekreuzte Versuch zeigt: Bei aktiver Rekurrenz beeinflussen gelernte
Core-Gewichte Potenziale und teilweise Spikes; ihre Rücksetzung verändert im
gekoppelten Arm **61/160 Spikezählmuster und 5/160 feste Vorhersagen**. Wird die
rekurrente Erregung gesperrt, verschwindet dieser Gewichtseinfluss vollständig.
Ohne Hemmung wird der Einfluss auf die Spikezählmuster im Mittel größer, aber
es entsteht kein positiver Vorhersagebeitrag in beiden Belegungen.

**Kein neuer funktionaler Lernnachweis.** Dies ist eine explorative
Ursachenanalyse auf denselben bekannten Seeds, keine unabhängige Bestätigung.
Es wurden keine neuronale Regel und kein Ausleser neu gelernt oder angepasst.

[Vorab fixierte Definition](Dokumentation/M10E_METHODIK.md) ·
[Automatische Tabellen](Experimente/m10e-crossed-weights/summary.md) ·
[Verifikation](Experimente/m10e-crossed-weights/verification.md).

## Warum dieser Vergleich aussagekräftiger ist als getrennte Eingriffe

M10 prüfte Gewichtsrücksetzungen, M10-D die Blockade rekurrenter Erregung und
Hemmung. M10-E kreuzt beide Eingriffe: trainierte Core-Gewichte oder
bedingungsspezifische Anfangsgewichte, jeweils bei allen aktiven Signalwegen,
blockierter Erregung, blockierter Hemmung oder beidem. Alle vier Arme, beide
Belegungen und beide unabhängigen Prüfzeitpunkte bleiben erhalten.

Das ursprüngliche M9-Training bleibt unverändert: Core-Gewichte ×4, STDP-Tau
100 ms, 256 Trainings-/128 Kalibrier-/128 Online-Testtrials. Der technische
[Pilot](Experimente/m10e-smoke/README.md) auf Seed 692 mit 8/8/8 Trials wird
getrennt geführt und nicht zusätzlich mit der Hauptdiagnose gepoolt.

**Wichtiger methodischer Unterschied:** Der Gewichtsreset findet hier erst
nach derselben neutralen Baseline unmittelbar vor der Aktion statt. Bei den
früheren Gewichtsrücksetzungen geschah das vor der Baseline. So sind jetzt
Anfangspotenziale und Refraktärzustände in allen acht Varianten identisch.
Die neuen Resetäste sind deshalb methodisch keine direkten Replikate der
früheren Resetäste. Die vier trainierten Äste reproduzieren dagegen M10-D.

Nur Core→Core-Gewichte, ausgewählte Enabled-Flags und gesperrte Queueeinträge
werden verändert. Aktionskopien, andere Signalwege, Zellzustände und lokale
Spuren bleiben erhalten, ebenso der am Trainingscheckpoint kalibrierte
visuelle Ausleser. Bereits unterwegs befindliche, nicht gesperrte Eingänge
behalten ihre zuvor erzeugte Amplitude. Der Reset entfernt somit nicht das
gesamte neuronale Gedächtnis und isoliert keine reine Aktionskopieantwort.

## Vorhersage und Wirkungsausrichtung

Gekoppelter Arm, Mittel über 20 Seeds und beide Belegungen; je Zeitpunkt und
Variante 40 A-/D-Paare beziehungsweise 80 Einzelantworten. Die 40 Paare sind
keine 40 unabhängigen Seed-Replikate. Zahlen jeweils **trainiert / zurückgesetzt**.

| Rekurrenzsperre | Sofort: Einzelvorhersage | Nach Ruhe: Einzelvorhersage | Sofort: Paar-Rangfolge | Nach Ruhe: Paar-Rangfolge |
|---|---:|---:|---:|---:|
| Keine | 51,25 / 51,25 % | 50,00 / 51,25 % | 42,50 / 40,00 % | 45,00 / 45,00 % |
| Erregung | 48,75 / 48,75 % | 48,75 / 48,75 % | 47,50 / 47,50 % | 47,50 / 47,50 % |
| Hemmung | 47,50 / 45,00 % | 50,00 / 51,25 % | 40,00 / 45,00 % | 45,00 / 50,00 % |
| Beide | 48,75 / 48,75 % | 48,75 / 48,75 % | 47,50 / 47,50 % | 47,50 / 47,50 % |

Die Einzelvorhersage ist die ursprüngliche feste Klassifikation. Die
Paar-Rangfolge ist die diagnostische M10-B-Auswertung mit beiden Antworten
und deren bekannter Balance; sie ist keine weitere autonome Vorhersageleistung.

Ohne Sperre erzeugt der Reset sofort gleich viele richtige Vorhersagen und
nach Ruhe einen geringfügig höheren Mittelwert. Ohne Hemmung liegen trainierte
Gewichte sofort 2,5 Prozentpunkte über zurückgesetzten, nach Ruhe dagegen
1,25 Punkte darunter. Das ergibt keinen stabilen funktionalen Gewichtsvorteil.

## Wo der Gewichtsbeitrag wirksam wird

Änderungen durch die Rücksetzung, je Zeitpunkt/Sperre 80 einzelne Aktionsfenster:

| Zeitpunkt / Sperre | Anderes Spikezählmuster | Andere Spikeereignisse | Andere Vorhersage | Anderes synchrones Restpotenzial |
|---|---:|---:|---:|---:|
| Sofort / keine | 30/80 | 42/80 | 4/80 | 80/80 |
| Nach Ruhe / keine | 31/80 | 42/80 | 1/80 | 80/80 |
| Sofort / Hemmung | 31/80 | 43/80 | 6/80 | 80/80 |
| Nach Ruhe / Hemmung | 34/80 | 43/80 | 7/80 | 80/80 |
| Sofort / Erregung oder beide | 0/80 | 0/80 | 0/80 | 0/80 |
| Nach Ruhe / Erregung oder beide | 0/80 | 0/80 | 0/80 | 0/80 |

Ein Vorhersagewechsel ist dabei keine automatische Verbesserung. Die
Gewichtseingriffe zeigen einen kausalen Beitrag zur konkreten Antwort unter
dem festen Zustand und Ausleser, keinen allgemeinen Informationsverlust.
Das Restpotenzial ist ein Zustand nach Spikes und Resets; seine Änderung wird
nicht als Vorhersageleistung vor der Spikebildung gewertet.

Die mittlere L1-Differenz der Spikezählvektoren beträgt ohne Sperre 5,313
sofort und 6,450 nach Ruhe; ohne Hemmung 9,538 beziehungsweise 9,700. Hemmung
begrenzt damit hier im Mittel die Stärke des beobachteten Gewichtseinflusses.
Die Zahl veränderter Fenster steigt dabei nur geringfügig. Eine stärkere
Gewichtswirkung ist nicht gleichbedeutend mit besserer Wirkungsausrichtung.

Ohne rekurrente Erregung erzeugen beide Gewichtszustände dieselben Verläufe
mit im Mittel drei Core-Spikes pro Aktion. Die vollständigen Vergleiche
bestätigen diese Gleichheit auch außerhalb des gekoppelten Arms. In dieser
Konfiguration sind die tatsächlich veränderten Core-Kanten erregend; ihre
gleichzeitige Sperre verhindert folgerichtig jede Wirkung ihres Gewichtsresets.
[Alle Einzelvergleiche](Experimente/m10e-crossed-weights/weight-effects.csv).

## Belegungen und Kontrollarme

Der Gewichtseffekt ist vorab als `trainiert − zurückgesetzt` festgelegt.
Für die Einzelvorhersage im gekoppelten Arm ergeben sich folgende deskriptive
Differenzen mit 95-%-Bootstrapintervallen, in Prozentpunkten:

| Zeitpunkt / Sperre | Normale Belegung | Umgekehrte Belegung |
|---|---:|---:|
| Sofort / keine | +2,5 [−5; +10] | −2,5 [−7,5; 0] |
| Nach Ruhe / keine | 0 [0; 0] | −2,5 [−7,5; 0] |
| Sofort / Hemmung | +5 [0; +12,5] | 0 [−10; +10] |
| Nach Ruhe / Hemmung | +5 [0; +12,5] | −7,5 [−15; 0] |

Der positive Mittelwert ohne Hemmung sofort stammt also nicht aus einem
positiven Effekt in beiden Belegungen. Nach Ruhe liegt erneut eine
gegengerichtete Wirkung vor. Die Wechselwirkung zwischen Hemmungsblockade und
Gewichtseffekt beträgt nach Ruhe normal +5 [0; +12,5], umgekehrt −5
[−12,5; 0] Prozentpunkte gegenüber der Variante ohne Sperre. Das ist kein
gleichgerichteter funktionaler Zugewinn.

Vor Training und im gealtert eingefrorenen Arm ist die Änderungsliste leer:
Rücksetzung hat in allen Sperrvarianten exakt keinen Effekt. Im entkoppelt
trainierten Arm verändert die Rücksetzung ohne Sperre sofort 36/80 und nach
Ruhe 32/80 Spikezählmuster; ohne Hemmung sind es 40/80 und 34/80. Die zugehörigen
Vorhersagewechsel betragen 6/2 beziehungsweise 8/4. Gewichtseinfluss auf die
Aktivität tritt somit auch ohne gelernte Handlungs-Wirkungs-Kopplung auf.

Alle acht Kombinationen und vier Arme werden vollständig berichtet. Die
**800 vorab definierten Kontraste** prüfen Gewichtseffekt, Wechselwirkung mit
Sperren und Unterschiede zu Kontrollarmen seedgepaart, getrennt nach Belegung
und Zeitpunkt. Bootstrap: 4.000 Resamples, Seed 1234. Die Intervalle sind
explorativ/deskriptiv, ohne neuen Signifikanz- oder Lernschwellwert. Einzelne
Grenzen bei null werden nicht in einen Bestätigungsnachweis umgedeutet.
[Alle Kontraste](Experimente/m10e-crossed-weights/contrasts.csv).

## Verifikation und Grenzen

Die Hauptdiagnose umfasst **5.120 Aktionsfenster, 20.480 Phasen und 529.173
Ereignisse**. 1.920 zurückgesetzte Vergleichsfenster erfüllen die interne
Negativkontrolle: Alle geänderten Kanten sind zugleich gesperrt oder es gibt
keine Änderungen. Ihre vollständigen Aktionsverläufe entsprechen exakt den
trainierten Gegenstücken. Insgesamt wurden in den Probeästen 168 ausgewählte,
noch unterwegs befindliche Ankünfte storniert; ungesperrte behalten ihre Amplitude.

Das vollständige ursprüngliche M9-Ergebnis und alle 120 historischen CSVs
bleiben unverändert. Sämtliche vier trainierten Äste stimmen mit den M10-D-
Archiven überein. Baselines, Aktions-Anfangspotenziale und Refraktärzustände
sind in allen acht Kombinationen identisch. Sperrlisten, Gewichtswerte,
Aktionskopien, feste Ausleser und neutrale LIF-Trajektorien wurden unabhängig
nachgerechnet. Maximaler Potenzialfehler: **2,762 × 10⁻⁷**, unter der
festgelegten Toleranz 2 × 10⁻⁵.

Alle 39 aktiven Experimenttests, sechs Python-Tests und Clippy bestanden.
Drei ausdrücklich QEMU-abhängige Tests blieben übersprungen. Kein neuer
Ausleserfit, keine neue Trainingsregel und keine unabhängigen Bestätigungsseeds.
[Audit](Experimente/m10e-crossed-weights/diagnostics.json) ·
[Provenienz](Experimente/m10e-crossed-weights/provenance.json) ·
[Rohdatenprüfsummen](Experimente/m10e-crossed-weights/raw-sha256.csv).

## Bedeutung für den nächsten Versuch

Der Antwortpfad des aktiven Core-Gewichtsbeitrags ist eingegrenzt: Er benötigt
hier die rekurrente Erregung; das Entfernen von Hemmung verstärkt die Wirkung,
stellt aber keine zuverlässige Zuordnung zu den tatsächlichen Wirkungen her.
Dies beweist weder, dass alle gelernten Informationen in diesen Gewichten
liegen, noch dass das Netzwerk keine andere nutzbare Repräsentation enthält.

Als nächster gezielter Test bietet sich ein **Tausch der Core-Gewichte zwischen
normaler und umgekehrter Trainingsbelegung desselben Seeds** an, während Zustand
und Ausleser fest bleiben. Anders als ein Reset würde das prüfen, ob der
belegungsabhängige Gewichtsanteil Antworten in eine passende Wirkungsrichtung
verschiebt. Dies ist ein Vorschlag für einen neu festzulegenden Versuch,
keine schon ausgeführte Messung und keine Begründung für zusätzliche biologische
Mechanismen ohne weiteren Befund.

## Planungsentscheidung vom 28.10.2026

M10 ist mit dieser Auswertung abgeschlossen. Der oben am 27.10. vorgeschlagene
Gewichtstausch wird vorerst zurückgestellt; weitere M10-Zusatzdiagnosen sind
nicht geplant. Als nächste Forschungsrichtung ist ein begrenzter Vergleich
mit synaptischer Konkurrenz vorgeschlagen, noch ohne Implementierung oder Lauf.
Der aktuelle Stand steht im [Forschungsplan](Dokumentation/FORSCHUNGSPLAN.md).
Die Messdaten und Schlussfolgerungen dieses Berichts bleiben unverändert.
