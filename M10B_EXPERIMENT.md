# M10-B: Gemeinsamer Decoderbias erklärt die Fehler nicht allein

Zusatzdiagnose vom **27.10.2026** auf den vorhandenen M9-Daten. Nach Entfernung
des gemeinsamen A-/D-Projektionsoffsets erreicht die Kombination in einer
**diagnostischen Paar-Rangfolge 42,5 % sofort und 45,0 % nach Ruhe**. Die
Aktionsunterschiede zeigen auf der bestehenden visuellen Wirkungsachse somit
nicht zuverlässig in die richtige Richtung.

Dies ist eine **retrospektive explorative Auswertung** derselben 20 Seeds,
kein neuer unabhängiger Lernnachweis. Es gab keinen neuronalen Lauf und keinen
Ausleserfit an Aktionslabels. Die ursprünglichen Einzelvorhersagen bleiben exakt
die von M9. [Definition](Dokumentation/M10B_METHODIK.md) ·
[Automatischer Bericht](Experimente/m10b-alignment/summary.md) ·
[Prüfnachweis](Experimente/m10b-alignment/verification.md).

## Frage und Methode

M10 zeigte unterschiedliche A-/D-Aktivität bei häufiger Gleichklassifikation.
Ein möglicher Grund wäre ein gemeinsamer Aktivitätsoffset: Die Differenz könnte
bereits richtig ausgerichtet sein, während beide Antworten auf derselben Seite
der festen Entscheidungsgrenze bleiben. Die andere Möglichkeit ist eine
unpassende Ausrichtung der Differenz selbst.

M10-B verwendet die vorhandenen visuellen Mittelwerte, Skalierungen und
Klassenmittelpunkte. Der Einheitsvektor zwischen den beiden visuellen Zentren
definiert die feste Wirkungsachse. Die beiden Aktionsantworten werden auf diese
Achse projiziert. Der Mittelwert ihrer Projektionen ist der gemeinsame Offset;
ihre Differenz bestimmt die Rangfolge. Die tatsächliche Belegung dient nur der
externen Bewertung, nicht zum Anpassen einer Richtung oder eines Auslesers.

Die Diagnose wertet alle vier Bedingungen, vier Arme, beide Belegungen, beide
Zeitpunkte und drei bestehende Eingriffe aus. Das sind **3.840 Paare** aus den
80 vorhandenen Quell-JSONs. Quelldaten und Auswertungsdefinition wurden vor
Ausführung über SHA-256 fixiert; die Fragestellung entstand nach Kenntnis von M10.

**Die Paar-Rangfolge nutzt Zusatzinformation:** Beide Antworten stammen aus
identischen Checkpoints, und das Paar enthält bekanntlich eine positive und
eine negative Wirkung. Die höhere Projektion wird der positiven Wirkung
zugeordnet. Dies ist keine neue einzelne Handlungswirkungsvorhersage und kein
autonomes Verhalten des Netzwerks. Projektionsgleichstand zählt 0,5.

## Ergebnisse der vier Bedingungen

Gekoppelter Arm, Mittel über 20 Seeds und beide Belegungen. Je Zeitpunkt liegen
40 A-/D-Paare vor; diese sind keine 40 unabhängigen Seed-Replikate.

| Bedingung | Sofort: ursprüngliche Einzelantwort | Sofort: Paar-Rangfolge | Nach Ruhe: ursprüngliche Einzelantwort | Nach Ruhe: Paar-Rangfolge |
|---|---:|---:|---:|---:|
| Referenz | 48,75 % | 51,25 % | 48,75 % | 51,25 % |
| Rekurrenz ×4 | 50,00 % | 47,50 % | 51,25 % | 47,50 % |
| STDP-Tau 100 ms | 48,75 % | 51,25 % | 48,75 % | 51,25 % |
| Kombination | **51,25 %** | **42,50 %** | **50,00 %** | **45,00 %** |

Die ursprüngliche und die diagnostische Aufgabe unterscheiden sich. Ihre Werte
werden deshalb nicht als Verbesserungsnachweis einer neu eingesetzten Steuerung
verglichen. Die Rangfolge beantwortet nur, ob die Differenz entlang der festen
visuellen Achse zur tatsächlichen Wirkungsrichtung passt.

## Kombination: Teilweise Bias, häufiger falsche Richtung

| Zeitpunkt | Richtige Richtung | Davon ursprünglich gleiche Klasse | Falsche Richtung | Gleichstand |
|---|---:|---:|---:|---:|
| Sofort, 40 Paare | 17 | 14 | 23 | 0 |
| Nach Ruhe, 40 Paare | 18 | 16 | 22 | 0 |

Ein Biasbeitrag existiert: In 14 beziehungsweise 16 Paaren ist die Richtung
richtig, obwohl beide Antworten zunächst dieselbe Klasse erhalten. Zugleich
zeigen 23 beziehungsweise 22 Paare in die falsche Richtung. Das Entfernen eines
gemeinsamen Offsets kann diese falsche Rangfolge nicht korrigieren.

Die mittleren wirkungskorrigierten Kosinuswerte zur visuellen Achse betragen
−0,0396 sofort und −0,0297 nach Ruhe. Diese Mittelwerte nahe null beschreiben
die Gesamtheit; sie bedeuten nicht, dass jedes einzelne Paar orthogonal wäre.
[Projektionen, Bias und Ausrichtung je Paar](Experimente/m10b-alignment/pairs.csv).

## Kontrollarme und Gewichtsrücksetzungen

Diagnostische Paar-Rangfolge der Kombination:

| Arm/Eingriff | Sofort | Nach Ruhe |
|---|---:|---:|
| Vor Training eingefroren | 50,0 % | 50,0 % |
| Gealtert eingefroren | 55,0 % | 50,0 % |
| Gekoppelt trainiert | 42,5 % | 45,0 % |
| Entkoppelt trainiert | 50,0 % | 50,0 % |
| Gekoppelt, Core-Gewichte zurückgesetzt | 40,0 % | 45,0 % |
| Gekoppelt, alle plastischen Gewichte zurückgesetzt | 40,0 % | 45,0 % |

Die Gewichtseffekte sind belegungsabhängig. Sofort beträgt die Rangfolge im
gekoppelten Arm 40 % bei normaler und 45 % bei umgekehrter Belegung; nach
Core-Rücksetzung sind es 45 % beziehungsweise 35 %. Das liefert keinen
beidseitigen Vorteil trainierter Gewichte. Nach Ruhe liegen gekoppelt 40/50 %
und nach Rücksetzung 50/40 % vor.

Deskriptive 95-%-Bootstrapintervalle der Rangfolgedifferenz gegenüber 50 %
Zufall überlappen null: sofort normal −10 Prozentpunkte [−30; +10], umgekehrt
−5 [−25; +15]; nach Ruhe normal −10 [−30; +10], umgekehrt 0 [−20; +20].
Die Werte werden nicht als Nachweis systematisch falschen Lernens interpretiert.
Alle Kontraste sind wie vorab festgelegt seedgepaart und deskriptiv; es gibt
keinen neuen Signifikanz- oder Bestätigungsschwellwert.
[Sämtliche Kontrollkontraste](Experimente/m10b-alignment/contrasts.csv).

## Bedeutung für die weitere Diagnose

Die Erklärung „die richtigen Wirkungen sind schon geordnet, nur ein gemeinsamer
Offset verhindert die Klassifikation“ reicht für dieses Protokoll nicht aus.
Eine Schwellenkorrektur allein würde die falsche Ausrichtung vieler Paare auf
dieser Achse nicht beheben.

Das zeigt keine allgemeine Informationslosigkeit: Andere Repräsentationen,
zeitliche Merkmale oder Ausleser sind damit nicht ausgeschlossen. Die Diagnose
betrifft ausdrücklich die vorhandene visuelle Spikezähl-Achse. Sie rechtfertigt
noch keine bestimmte zusätzliche biologische Lernregel.

Der nächste gezielte Schritt sollte verfolgen, **an welcher Stelle synaptische
Beiträge, Potenziale und Spikes die richtige Wirkungsrichtung erhalten oder
verlieren**. Die vorhandenen M10-Traces erlauben dafür eine weiter aufgelöste
Ursachenanalyse, bevor Stabilisierung oder neue Mechanismen ergänzt werden.

## Datenqualität

Der Audit rekonstruiert alle ursprünglichen Vorhersagen und Genauigkeiten aus
den gespeicherten Decoderparametern. Projektionsscores und Zentroidabstände
stimmen algebraisch überein; es gibt keine entartete visuelle Achse in den
3.840 Paaren. Sechs Softwaretests prüfen korrekte Richtung trotz Bias,
orthogonale Aktionsunterschiede, Belegungsumkehr, Gleichstand/Entartung,
Vorhersageintegrität und unveränderte Quellen.

[Audit](Experimente/m10b-alignment/diagnostics.json) ·
[Quelle und Methode](Experimente/m10b-alignment/manifest.json) ·
[Programmprüfsummen](Experimente/m10b-alignment/provenance.json).
