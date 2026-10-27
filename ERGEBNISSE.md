# Was bisher gemessen wurde

**Die vorhandenen kontrollierten Reihen liefern bislang keinen belastbaren
funktionalen Nachweis gelernter Handlungswirkungen.** Zugleich sind lokale
Gewichtsänderungen, Änderungen der Netzstruktur und unter bestimmten Parametern
zusätzliche rekurrente Spikes nachgewiesen. Diese Befunde betreffen verschiedene
Stufen der Forschungsfrage und werden getrennt bewertet.

## Der Weg durch die Versuche

| Untersuchung | Wesentlicher Befund | Reichweite und Beleg |
|---|---|---|
| Rekurrenter Core | Strukturentwicklung verändert die Aktivität bei gleicher aufgezeichneter Erfahrung. | Drei Seeds; technische und mechanistische Messung. [Bericht](RECURRENT_EXPERIMENT.md) |
| Retention | Einfrieren erhält die Parameter nach Training. Im dokumentierten Seed-42-Lauf ergeben sich 15/32 korrekte Vorhersagen bei Strukturentwicklung, ebenso 15/32 vor Training. | Kein funktionaler Vorteil in dieser Einzel-Seed-Prüfung. [Bericht](RETENTION_EXPERIMENT.md) |
| Agency | Nach Training 11/180 Zielerfolge mit Entwicklung, 9/180 eingefroren und 41/180 beim Zufallsagenten. | Zehn Seeds; Kriterium eigenständigen Lernfortschritts nicht erreicht. [Bericht](AGENCY_EXPERIMENT.md) |
| Sensorimotorik | Ein Decoder mit Erstspike-Zeit löst mehr Motor-Gleichstände: sichtbare Bewegungen nach Freeze steigen von 32,8 % auf 85,2 %. | Verbesserung der Aktionsauswahl; kein ausreichender Nachweis gelernter Handlungswirkungen. [Bericht](SENSORIMOTOR_EXPERIMENT.md) |
| M3 | Vorhersage vor dem Wirkungsbild bleibt nahe Zufall; kein Vorteil gegenüber allen Kontrollen. | Zehn Seeds; schwache visuelle Auslesbarkeit nach Training begrenzt zusätzlich die Aussage. [Bericht](M3_EXPERIMENT.md) |
| M4 | Keine der 20 Bedingungen bestätigt funktionales Wirkungslernen auf zehn neuen Seeds. | Veränderte Sensorik, Kapazität, Kodierung, Zeitabstände und Lernmechanismen. [Bericht](M4_EXPERIMENT.md) |
| M5 | Aktionskopien können Core-Spikes auslösen; sensorische Homöostase kann die Weiterleitung abschwächen. | Zwei Engpässe eingegrenzt; ihre Behebung beweist noch kein Wirkungslernen. [Bericht](M5_EXPERIMENT.md) |
| M6 | Kombination der Eingriffe ohne bestätigten Vorhersagevorteil. Ohne Core-Homöostase entstehen in der separaten Kontrolle Aktionsspikes. | Hauptreihe und explorative Folgekontrolle getrennt. [Bericht](M6_EXPERIMENT.md) |
| M7 | STDP erzeugt belegungsabhängige Gewichtsänderungen. Gewichtseingriffe ändern Potenziale, aber keine zusätzlichen Core-Spikes in den untersuchten Aktionsproben. | Erneute Ausführung vorhandener Seeds 400–409; Ursachenanalyse. [Bericht](M7_EXPERIMENT.md) |
| M8 | Vierfache Core-Gewichte ermöglichen zusätzliche rekurrente Spikes; längere STDP-Zeitskalen verstärken separat Gewichtsspuren. Kein bestätigter funktionaler Vorhersagevorteil. | 13 Bedingungen, Bestätigung auf zehn weiteren Seeds 510–519. [Bericht](M8_EXPERIMENT.md) |
| M9-v2 | Kombination erreicht sofort 51,25 % und nach Ruhe 50,00 %; weder funktionaler Lernnachweis noch abgesicherter beidseitiger Verlust nach Gewichtsrücksetzung. | Vier Bedingungen, 20 neue Bestätigungsseeds 610–629. [Bericht](M9_EXPERIMENT.md) |
| M10 | Core-Gewichte beeinflussen in 160/160 gekoppelten Kombinationsproben Eingänge/Potenziale, in 61/160 Spikezählmuster und in 5/160 die feste Entscheidung. | Retrospektive Diagnose und passive Replays auf denselben M9-Seeds; kein neuer Lernnachweis. [Bericht](M10_EXPERIMENT.md) |
| M10-B | Nach diagnostischer Entfernung des gemeinsamen Projektionsoffsets erreicht die Kombination nur 42,5/45,0 % richtige Paar-Rangfolgen. | Retrospektiv auf derselben visuellen Achse; keine neue Einzelvorhersage oder Bestätigung. [Bericht](M10B_EXPERIMENT.md) |

| M10-C | Bereits die Eingangsprojektion zeigt in 23/40 Paaren je Zeitpunkt in die unpassende Richtung auf der festen Auslesergewichtung; spätere Vorzeichenwechsel sind selten. | Retrospektive Bilanz von 1.920 Aktionsfenstern, konditional auf beobachtete Rückkopplung. [Bericht](M10C_EXPERIMENT.md) |

| M10-D | Ohne Hemmung ungefähr doppelte Aktivität, ohne beidseitigen Vorhersagevorteil; ohne Erregung drei Spikes/Aktion, ebenfalls kein Vorhersagegewinn. | Vier kontrollierte Übertragungsvarianten, identische eingefrorene Zustände, 20 bekannte Seeds; keine neue Bestätigung. [Bericht](M10D_EXPERIMENT.md) |

| M10-E | Core-Reset ändert bei aktiver Rekurrenz 61/160 gekoppelte Spikezählmuster und 5/160 Vorhersagen; ohne Erregung kein Gewichtseinfluss, weiterhin kein zuverlässiger Vorhersagevorteil. | Zwei Gewichtszustände × vier Sperren nach identischer Baseline; 20 bekannte Seeds, keine neue Bestätigung. [Bericht](M10E_EXPERIMENT.md) |

Die serielle Demo mit Lehrneuronen ist als [früher technischer Demonstrator](SERIAL_MODEL.md)
dokumentiert. Ihr Erfolg wird nicht als Erfolg der späteren Wirkungslerntests gezählt.

## M9: Kombination auf 20 neuen Seeds

Der feste 2×2-Vergleich bestätigt keinen funktionalen Lernnachweis. Mittelwerte
des gekoppelten Arms über 20 Seeds und beide Belegungen:

| Bedingung | Sofort | Nach unabhängigen 2 s Ruhe | Extra-Spikes sofort |
|---|---:|---:|---:|
| Referenz | 48,75 % | 48,75 % | 0,00 |
| Core-Gewichte ×4 | 50,00 % | 51,25 % | 21,65 |
| STDP-Tau 100 ms | 48,75 % | 48,75 % | 0,00 |
| Kombination | 51,25 % | 50,00 % | 13,43 |

Keine Bedingung besteht die vollständigen Verhaltenskriterien, auch schon ohne
die zusätzliche exakte Familienkorrektur. Die kontrollierte Rücksetzung aller
plastischen Gewichte erzeugt ebenfalls keinen abgesicherten Genauigkeitsverlust
in beiden Belegungen. Die visuelle Auslesbarkeit bleibt im Mittel 99,73–100 %.

[Kompakte Tabelle](Darstellung/M9_UEBERBLICK.md) ·
[Vollständiger Bericht](M9_EXPERIMENT.md) ·
[Daten und Audits](Experimente/m9-v2-confirm/summary.md).

## M8: getrennte Parameterscans als Ausgangspunkt

Die folgenden Zahlen stammen aus der Bestätigungsreihe. Angegeben sind die
Mittelwerte des gekoppelt trainierten Arms über zehn Seeds und beide Belegungen.
Die balancierten Vorhersageaufgaben haben hier ein Zufallsniveau von 50 %.

| Bedingung | Vorhersage sofort | Vorhersage nach unabhängigen 2 s Ruhe | Zusätzliche Core-Spikes sofort |
|---|---:|---:|---:|
| Referenz | 50,0 % | 50,0 % | 0 |
| Core-Gewichte ×4 | 50,0 % | 50,0 % | 19,48 |
| STDP-Zeitkonstanten 100 ms | 50,0 % | 50,0 % | 0 |
| Core-Verzögerung 0,5 ms | 52,5 % | 52,5 % | 0 |

„Zusätzlich“ bezeichnet Spikes außerhalb der drei direkt von der betreffenden
Aktionskopie angeregten Core-Zellen. Höhere Aktivität ist damit messbar, führt hier
aber noch nicht zu einer abgesicherten Vorhersage der gelernten Wirkung.
Keine der 13 Bedingungen erfüllt die primären Kriterien einschließlich der
Korrektur für die vielen Vergleiche. Die visuelle Auslesbarkeit beträgt bei allen
Bedingungen 100 %. In den 2.080 No-copy-Kontrollfenstern der Bestätigung entstehen
keine Core-Spikes.

Die [kompakte M8-Tabelle](Darstellung/M8_UEBERBLICK.md) enthält alle 13 Bedingungen.
Die Zahlen lassen sich direkt mit den originalen
[Vorhersagewerten](Experimente/m8-confirm/summary.csv), der
[Weiterleitungsstatistik](Experimente/m8-confirm/propagation-summary.csv) und den
[Kontrollkontrasten](Experimente/m8-confirm/prediction-contrasts.csv) vergleichen.

## Was daraus folgt

Die Messungen grenzen konkrete Hindernisse ein: Verlust von Zeitinformation bei
Motorzählungen, geringe Wirksamkeit mancher Aktionssignale, Abschwächung sensorischer
Signale und begrenzte Weiterleitung von Aktionsaktivität. M7 zeigt, dass Erfahrung
in Gewichten Spuren hinterlassen kann. M8 zeigt, dass zusätzliche Weiterleitung
durch Parameteränderungen erreichbar ist. Die Verbindung dieser Spuren mit einem
robusten funktionalen Lernvorteil bleibt auch nach dem gezielten M9-Kombinationstest
auf 20 neuen Seeds offen. M10 zeigt inzwischen, dass Gewichtseffekte die Aktivität
erreichen, aber selten die feste Entscheidung verändern. Wirkungsspezifität und
Passung zu visuellen Zielmustern bleiben gezielt zu untersuchen, bevor neue
biologische Regeln ergänzt werden.

Das negative Ergebnis betrifft die dokumentierten Aufgaben, Konfigurationen,
Prüfzeitpunkte und Auswerter. Es ist kein Nachweis, dass lokale Plastizität
grundsätzlich kein Wirkungslernen ermöglichen kann. Noch nicht untersuchte
Parameterkombinationen, andere Auswerter oder Gedächtnisbildung bei weiterlaufender
Plastizität werden hier nicht als gemessene Ergebnisse dargestellt.

Zur Bewertung einzelner Zahlen: [Kontrollen und Grenzen](METHODIK.md).
Alle Messordner einschließlich unvollständiger Versuche:
[Messreihenverzeichnis](Experimente/README.md).
