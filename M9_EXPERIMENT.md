# M9: Kombination geprüft, funktionales Lernen nicht bestätigt

Abschlussbericht vom **27.10.2026**. Der feste 2×2-Vergleich auf **20 neuen
Bestätigungsseeds 610–629** liefert keinen belastbaren funktionalen Lernnachweis.
Die Kombination erreicht am unmittelbaren Checkpoint **51,25 %**, nach
unabhängigen 2 Sekunden Ruhe **50,00 %**. Sie besteht weder die vollständigen
Verhaltensvergleiche noch die zusätzliche Gewichtskausalitätsprüfung.

[Bestätigungsbericht](Experimente/m9-v2-confirm/summary.md) ·
[Pilot](Experimente/m9-v2-pilot/summary.md) ·
[Vorab festgelegte Methodik](Dokumentation/M9_METHODIK.md) ·
[Prüfnachweis](Experimente/m9-v2-confirm/verification.md).

## Aufbau und unveränderte Bedingungen

M8 zeigte zusätzliche Weiterleitung bei vierfachen Core-Gewichten und stärkere
Gewichtszuordnung bei längeren STDP-Zeitkonstanten getrennt. M9 untersucht die
Referenz, beide Einzelbedingungen und ihre Kombination. Das Netzwerk verwendet
weiterhin bestehende lokale Regeln; es wird kein neuer biologischer Mechanismus
eingeführt. Homöostase und Strukturentwicklung bleiben ausgeschaltet.

Der Pilot mit Seeds 600–602 umfasst zwölf Fälle. Alle vier Bedingungen wurden
anschließend unverändert auf den 20 neuen Seeds geprüft: **80 vollständige
Bestätigungsfälle**. Pro Fall gelten 256 Trainings-, 128 Kalibrier- und 128 Trials
je Online-Prüfphase. Die Manifeste wurden vor den wissenschaftlichen Reihen
gespeichert; es gab keine Parameterauswahl anhand des Piloten.

Jeder Fall enthält `before`, `aged_frozen`, `paired`, `scrambled` und beide
Tastenbelegungen. Kalibriert wird ausschließlich auf einem eigenen Replayzweig.
Beide primären Endpunkte verwenden pro Belegung/Seed zwei unabhängige
A-/D-Proben aus demselben Trainingscheckpoint: sofort und nach 2 Sekunden Ruhe.
Die Inferenz behandelt **Seeds als Replikate**, nicht einzelne Trials oder
Belegungen als zusätzliche unabhängige Stichproben.

## Vorhersageleistung

Mittelwerte des gekoppelten Arms über 20 Seeds und beide Belegungen;
Zufallsniveau 50 %. Die Ruheprobe beginnt unabhängig von der Online-Probe.

| Bedingung | Sofort | Nach 2 s Ruhe | Online | Visuelle Auslesbarkeit |
|---|---:|---:|---:|---:|
| Referenz: ×1, 20 ms | 48,75 % | 48,75 % | 48,75 % | 100,00 % |
| Rekurrenz: ×4, 20 ms | 50,00 % | 51,25 % | 50,78 % | 99,73 % |
| Zeitkonstante: ×1, 100 ms | 48,75 % | 48,75 % | 48,75 % | 100,00 % |
| Kombination: ×4, 100 ms | **51,25 %** | **50,00 %** | 51,74 % | 100,00 % |

**Keine Bedingung erfüllt die primären Kriterien.** Auch der vollständige
Verhaltensvergleich ohne die zusätzliche exakte Familienkorrektur scheitert.
Das Ergebnis entsteht somit nicht allein durch die strengere p-Grenze.
Online-, sequenzielle Ruhe- und Interferenzproben erfüllen bei der Spikezähl-
Auslesung ebenfalls nicht die vollständigen unkorrigierten Kontroll-/Belegungskriterien.

Die vorab festgelegten Anforderungen gelten in beiden Belegungen separat:
Vorhersagevorteil gegenüber Zufall und allen drei Kontrollen, Vorteile beim
Belegungswechsel und bei gleichzeitig richtigen Antworten sowie ausreichende
visuelle Auslesbarkeit. Erforderlich sind positive untere Bootstrapgrenzen und
einseitige exakte Vorzeichen-p ≤0,00625; Familienkorrektur über vier Bedingungen
und zwei Endpunkte. Die gemittelte visuelle Auslesbarkeit in der Tabelle ersetzt
nicht die getrennte Belegungsprüfung.

Am unmittelbaren Checkpoint erreicht der gealtert eingefrorene Kontrollarm der
Kombination durchschnittlich **52,50 %**, der gekoppelte Arm nur 51,25 %.
Die kleine Abweichung vom Zufallsniveau ist damit kein Lernnachweis.
[Alle Kontrollkontraste](Experimente/m9-v2-confirm/prediction-contrasts.csv).

## Zusätzliche Spikes und Gewichtsspuren

Spikes außerhalb der drei direkt durch die jeweilige Aktionskopie angeregten
Core-Zellen; Mittelwerte des gekoppelten Arms:

| Bedingung | Extra-Spikes sofort | Hintergrund ohne Kopie sofort | Extra-Spikes nach Ruhe |
|---|---:|---:|---:|
| Referenz | 0,00 | 0,00 | 0,00 |
| Rekurrenz ×4 | 21,65 | 0,59 | 17,26 |
| STDP-Tau 100 ms | 0,00 | 0,00 | 0,00 |
| Kombination | 13,43 | 0,00 | 11,84 |

Nach Ruhe ist die No-copy-Hintergrundaktivität in diesen gekoppelten Bedingungen
null. Die unmittelbare Hintergrundaktivität bei ×4 zeigt, warum zusätzliche
Spikes nicht vollständig als neu durch die Testaktion ausgelöst interpretiert
werden dürfen. Mehr Aktivität allein ist keine Vorhersageleistung.
[Weiterleitung einschließlich aller Kontrollarme](Experimente/m9-v2-confirm/propagation-summary.csv).

| Bedingung | Mittlere topologische Gewichtszuordnung | Erhaltener visueller Gewichtsanteil |
|---|---:|---:|
| Referenz | +0,010040 | 59,2 % |
| Rekurrenz ×4 | +0,001511 | 58,2 % |
| STDP-Tau 100 ms | +0,066749 | 46,7 % |
| Kombination | +0,019146 | 46,3 % |

Längere Zeitkonstanten erhöhen die deskriptiv gemessene Gewichtszuordnung,
zugleich bleiben weniger visuelle Eingangsgewichte erhalten. Die Kombination
zeigt im Mittel weniger Zusatzspikes und einen niedrigeren Zuordnungswert als
die jeweils darauf spezialisierte Einzelbedingung. Diese Größen belegen keine
funktionale Nutzung. Die Zuordnungskontraste und ihre Bootstrapintervalle sind
deskriptiv; für diese mechanistischen Mehrfachvergleiche gibt es keinen eigenen
bestätigenden Signifikanznachweis.
[Gewichtsdiagnose](Experimente/m9-v2-confirm/weight-summary.csv).

## Kontrollierte Gewichtsrücksetzungen

An beiden primären Zeitpunkten werden auf identischen eingefrorenen
Replayzuständen unveränderte Gewichte (`sham`), zurückgesetzte Core-Gewichte
und sämtliche plastischen Gewichte auf ihren bedingungsspezifischen Anfangswerten
verglichen. Der Ausleser bleibt fest; es wird kein Wirkungsbild gezeigt.

In der Kombination ergeben sich folgende Genauigkeitsdifferenzen **unverändert
minus alle plastischen Gewichte zurückgesetzt**:

| Zeitpunkt | Belegung | Differenz | Deskriptives 95-%-Intervall | Exaktes einseitiges p |
|---|---|---:|---:|---:|
| Sofort | Normal | +2,5 Prozentpunkte | [−5,0; +10,0] | 0,5 |
| Sofort | Umgekehrt | −2,5 Prozentpunkte | [−7,5; 0,0] | 1,0 |
| Nach Ruhe | Normal | 0,0 Prozentpunkte | [0,0; 0,0] | 1,0 |
| Nach Ruhe | Umgekehrt | −2,5 Prozentpunkte | [−7,5; 0,0] | 1,0 |

**Kein abgesicherter beidseitiger Verlust nach Rücksetzung.** Die drei anderen
Bedingungen zeigen bei diesem Vergleich an beiden primären Zeitpunkten in
beiden Belegungen jeweils null mittlere Genauigkeitsdifferenz. Keine Bedingung
erfüllt die zusätzliche Gewichtskausalitätsanforderung.
[Sämtliche Eingriffskontraste](Experimente/m9-v2-confirm/causal-contrasts.csv).

Das bedeutet nicht, dass Gewichte keinerlei elektrische Wirkung hätten. Der
Test betrifft ihre Nutzung für diese Vorhersage bei festem Ausleser und
erhaltenem dynamischem Zustand. Membran-/Spurzustände und reisende Impulse
werden nicht zurückgesetzt; Impulse behalten ihre Emissionsamplituden.

## Bedeutung für den nächsten Versuch

Die bloße Kombination der zwei in M8 getrennt verbesserten Voraussetzungen reicht
in diesem Protokoll nicht für den angestrebten Nachweis. Sie liefert auch keinen
abgesicherten Synergienachweis. Die
[faktoriellen Kontraste](Experimente/m9-v2-confirm/factorial-contrasts.csv) bleiben
wie geplant deskriptiv.

Im gekoppelten Kombinationsarm ordnet der Ausleser A und D in **35 von 40**
Belegungs-/Seed-Instanzen sofort und in **36 von 40** nach Ruhe derselben Klasse
zu. Das beschreibt die Auslesung und behauptet keine identischen neuronalen
Spikeantworten. Im Pilot war diese Gleichklassifikation in allen sechs Instanzen
zu beobachten; die Bestätigung zeigt zusätzliche Unterschiede und begrenzt
damit diese anfängliche Beobachtung.

M10 sollte deshalb anhand vorhandener Spike-, Gewichts- und Potenzialdaten
lokalisieren, ob erfahrungsabhängige Unterschiede elektrisch zu schwach bleiben,
nicht in passende Aktivitätsmuster übertragen oder vom Ausleser nicht genutzt
werden. Ein konkretes M10-Protokoll bleibt vor seiner Ausführung festzulegen.
M9 begründet noch keine bestimmte neue biologische Regel und schließt lokale
Selbstorganisation unter anderen Bedingungen nicht aus.

Alle 80 Fälle bestanden den Audit: 4.480 ursprüngliche Replayzweige,
7.680 zusätzliche Eingriffszweige, 371.200 Trial-/Propagationszeilen und je
2.598.400 Phasen-/Sensorzeilen. Manifeste, relevante Quellen und ausführbares
Programm stimmen mit den gespeicherten Prüfsummen überein.
[Datenaudit](Experimente/m9-v2-confirm/diagnostics.json) ·
[Provenienz](Experimente/m9-v2-confirm/provenance.json).
