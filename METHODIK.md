# Wie die Ergebnisse bewertet werden

Die Studien verfolgen unterschiedliche Fragen. Ein technischer Funktionstest,
eine mechanistische Diagnose und eine Bestätigungsreihe haben deshalb verschiedene
Aussagekraft. Verbindlich ist jeweils das im einzelnen Bericht dokumentierte
Protokoll; diese Einführung erklärt die wiederkehrenden Grundideen.

## Handlung vor Wirkung

In den kontrollierten Wirkungsversuchen wird zuerst A oder D ausgeführt. Das
Modell erhält die entsprechende eigene Aktionskopie. Die Vorhersage wird vor
Präsentation des neuen Wirkungsbildes aus der Core-Aktivität gewonnen. So soll
verhindert werden, dass eine vermeintliche Vorhersage lediglich das bereits
sichtbare Ergebnis erkennt.

Ein separat kalibrierter äußerer Auswerter liest neuronale Merkmale. Seine
Kalibrierung verändert keine neuronalen Gewichte und liefert dem Modell keine
richtige Antwort zurück. Ein Auswerter, der selbst eine Aktions-/Wirkungszuordnung
überwacht lernt, kann eine hohe Trefferrate erreichen, ohne dass das neuronale Netz
eine neue Zuordnung gelernt hat. Solche Referenzen werden getrennt bewertet.

## Wiederkehrende Kontrollarme

Für M3, M4, M6 und M8 werden vier Zustände verglichen; die genaue Benennung variiert
in den Dateien. M7 verwendet für seine Diagnose drei dieser Arme.

| Kennung | Bedeutung | Wogegen kontrolliert wird |
|---|---|---|
| `before`, teils `before_training` | Vor Training eingefroren | Bereits vorhandene Information im Anfangsnetz |
| `aged_frozen` | Gleiche Erfahrung und Zeit ohne aktive Lernmechanismen | Bloßes Altern und dynamischer Zustand |
| `paired` | Lernen mit gekoppelter Aktion und Wirkung | Zu prüfende erfahrungsabhängige Zuordnung |
| `scrambled` | Lernen mit zerstörter Aktions-/Bildzuordnung | Unspezifische Aktivität und Gewichtsänderungen |

Für einen Seed starten verglichene Arme mit demselben Anfangsnetz. Beim normalen
und umgekehrten Tastenmapping bleiben ausgeführte Tasten gleich, ihre Bildwirkungen
werden vertauscht. Eine erlernte Wirkung muss diese Umkehr berücksichtigen.
Eine fest vorhandene Reaktion auf die Taste A allein reicht dafür nicht aus.

## Seeds, Pilot und Bestätigung

Ein Seed bestimmt die verwendeten Zufallsfolgen und den Netzaufbau. Viele Trials
eines Seeds sind wiederholte Beobachtungen desselben Netzaufbaus. Trials, die beiden
Mappings oder vier Arme werden deshalb nicht als zusätzliche unabhängige Seeds
gezählt. Vergleiche werden innerhalb desselben Seeds gepaart.

| Reihe | Pilot | Getrennte weitere Seeds |
|---|---|---|
| M4 | 0–2 | 100–109 |
| M5 | 0–2 | 200–209 |
| M6 | 0–2 | 300–309 |
| M6-Core-Kontrolle | Eigenständige explorative Folgeprüfung | 400–409 |
| M7 | Diagnose auf vorhandenen M6-Core-Seeds | Keine neue Bestätigungsstichprobe; 400–409 werden erneut ausgeführt |
| M8 | 500–502 | 510–519 |

Die gespeicherten `manifest.json`-Dateien enthalten die geplanten Bedingungen.
Pilot und Bestätigung werden getrennt beurteilt. Kurze Software-Smokes und
abgebrochene Messläufe sind keine zusätzlichen wissenschaftlichen Bestätigungen.

## Kennzahlen richtig lesen

Bei den balancierten binären Vorhersageaufgaben entspricht 50 % dem Zufallsniveau.
Die balancierte Genauigkeit mittelt die Trefferquoten der beiden Wirkungsklassen.
Das gilt nicht pauschal für Zielerfolg in Agency oder die siebenklassige
Positionserkennung in einem Motor-Scan; dort gelten die eigenen Vergleichsmaße.

Ein Wert oberhalb 50 % genügt nicht als Lernnachweis. Gefordert werden je nach
Protokoll unter anderem Vorteile gegenüber Kontrollen, Verhalten unter
Belegungsumkehr, ausreichende visuelle Auslesbarkeit und Prüfung nach Ruhe.
Die Berichte nennen die konkreten Kriterien und deren Ergebnisse.

Frühere Reihen verwenden beschreibende 95-%-Bootstrapintervalle über gepaarte
Seeds. Diese sind nicht automatisch eine Korrektur für viele parallele Vergleiche.
M8 ergänzt für die primären Endpunkte exakte gepaarte Vorzeichentests mit
Bonferroni-Korrektur über 13 Bedingungen × 2 Prüfzeitpunkte.

## Unterschiedliche Prüfzeitpunkte

In M4 und Teilen von M5 liegt zwischen Training und erster Vorhersage eine längere
visuelle Kalibrierung. M6 führt die Kalibrierung auf einem getrennten exakten
Replayzweig aus; die Elterninstanz wird unmittelbar am Trainingsende geprüft.
M8 trennt zusätzlich einen unabhängigen Ruhe-Checkpoint vom späteren sequenziellen
Test nach Online-Prüfungen. Diese Zeitpunkte sind nicht austauschbar.

Auch der unmittelbare Checkpointtest benötigt ein Startbild und die Integration
der Aktionskopie. Er erfasst nicht jeden beliebig kurzen Zustand direkt nach
Trainingsende. Die genauen Zeitgrenzen stehen im jeweiligen Bericht.

## Was die Nachweise belegen

| Beobachtung | Belegt | Belegt für sich noch nicht |
|---|---|---|
| Gewichtsänderungen | Plastizität hat stattgefunden. | Funktional gelernte Wirkung |
| Neue oder entfernte Synapsen | Strukturentwicklung hat stattgefunden. | Verbesserte Aufgabenleistung |
| Parameter bleiben nach Freeze erhalten | Einfrieren und Parametererhalt funktionieren. | Stabile Erinnerung bei weiterlaufendem Lernen |
| Zusätzliche Spikes im Core | Aktivität wird über direkte Zielzellen hinaus weitergeleitet. | Richtige erfahrungsabhängige Vorhersage |
| Exakter Replay stimmt überein | Ausführung ist unter den dokumentierten Bedingungen reproduzierbar. | Allgemeine Übertragbarkeit auf andere Rechner, Backends oder Aufgaben |

Die Zahl von zehn Seeds und die kleine Anzahl unabhängiger A/D-Checkpointproben
begrenzen die Teststärke. Eingefrorene Tests, reduzierte Welten und eine teilweise
stark vereinfachte Sensorik begrenzen die Verallgemeinerbarkeit.

Originale Einzelheiten: [M3](M3_EXPERIMENT.md), [M4](M4_EXPERIMENT.md),
[M5](M5_EXPERIMENT.md), [M6](M6_EXPERIMENT.md), [M7](M7_EXPERIMENT.md),
[M8](M8_EXPERIMENT.md).
