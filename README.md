# NERVA_Data – Messungen zum NERVA-Projekt

**Dieser Ordner ist das eigenständig lesbare Informations- und Datenpaket des
NERVA-Projekts.** Er kann allein heruntergeladen, weitergegeben und offline gelesen
werden. Für die hier enthaltenen Erklärungen, Versuchsberichte und Messdaten werden
die Bibliothek und die Modellprogramme nicht benötigt.

NERVA untersucht, ob ein rekurrentes Netzwerk aus spikenden Neuronen durch lokale
Lernregeln Zusammenhänge zwischen eigenen Handlungen und deren sichtbaren Folgen
lernen kann. Das neuronale Modell erhält Bilder und die Kopie seiner ausgeführten
Tasten; die kontrollierten Wirkungsversuche verwenden keine globale Belohnung und
keine richtigen Antworten als neuronale Trainingsvorgabe.

**Stand der Versuche bis M8:** Lokale Gewichtsänderungen, Einflüsse der
Strukturentwicklung und zusätzliche rekurrente Aktivität sind gemessen.
Ein belastbarer funktionaler Nachweis gelernter Handlungswirkungen fehlt in den
untersuchten Bedingungen weiterhin. Die Forschungsfrage bleibt offen.

Das Repository heißt `NERVA_Data`. Hinweise zum vollständigen Download mit den
zwei großen Git-LFS-Dateien stehen unter [Herunterladen](HERUNTERLADEN.md).

## Hier anfangen

| Interesse | Einstieg |
|---|---|
| Projekt in wenigen Minuten verstehen | [Projektidee und Modellaufbau](PROJEKT.md) |
| Ergebnisse und ihre Bedeutung kennenlernen | [Ergebnisüberblick](ERGEBNISSE.md) |
| Verstehen, wie Lernen geprüft wurde | [Methodik, Kontrollen und Aussagegrenzen](METHODIK.md) |
| Einzelmessungen selbst ansehen | [Datenhandbuch und Begriffe](DATENHANDBUCH.md) |
| Einen bestimmten Lauf finden | [Vollständiges Verzeichnis der Messreihen](Experimente/README.md) |
| Herkunft und Umfang des Pakets prüfen | [Dokumentationsstand](DOKUMENTATIONSSTAND.md) |

Für einen kurzen Überblick reichen diese Texte und die verlinkten kleinen
Zusammenfassungen. Die umfangreichen Rohdateien werden erst für Detailanalysen
benötigt. Markdown-Dateien lassen sich mit einem Texteditor oder Markdown-Betrachter
lesen, CSV-Dateien mit einer Tabellenkalkulation, JSON-Dateien mit einem Texteditor.

## Ausführliche Berichte

Die Berichte enthalten Aufbau, Parameter, Kontrollen, Messwerte und Grenzen.
Ihre Datenlinks führen innerhalb dieses Ordners zu den jeweiligen Messläufen.

| Untersuchung | Bericht |
|---|---|
| Rekurrentes Netz und Strukturentwicklung | [Rekurrenter Core](RECURRENT_EXPERIMENT.md) |
| Trainieren, Einfrieren, Erhalten | [Retention](RETENTION_EXPERIMENT.md) |
| Eigenständiges zielgerichtetes Handeln | [Agency](AGENCY_EXPERIMENT.md) |
| Motorsteuerung und Wirkungslernen getrennt | [Sensorimotorik](SENSORIMOTOR_EXPERIMENT.md) |
| M3: Vorhersage vor dem Wirkungsbild | [M3](M3_EXPERIMENT.md) |
| M4: Sensorik, Zeitabstände und Lernmechanismen | [M4](M4_EXPERIMENT.md) |
| M5: Aktionskopie und sensorische Homöostase | [M5](M5_EXPERIMENT.md) |
| M6: Kombinierter Wirkungslerntest | [M6](M6_EXPERIMENT.md) |
| M7: Gewichts- und Synapsendiagnose | [M7](M7_EXPERIMENT.md) |
| M8: Weiterleitung und Zeitskalen | [M8](M8_EXPERIMENT.md) |
| Frühere serielle Zuordnungsdemo mit Lehrsignalen | [Serielle Demo](SERIAL_MODEL.md) |

## Was wo liegt

| Pfad | Inhalt |
|---|---|
| `Experimente/` | Originale Messläufe mit Plänen, Rohdaten, Zusammenfassungen und Prüfnachweisen |
| `Dokumentation/` | Technischer Modellaufbau, ursprüngliche Hypothesen und detaillierte Versuchsverträge |
| [Darstellung/](Darstellung/README.md) | Kompakte Aufbereitung wichtiger Ergebnisse |
| [Modell/](Modell/README.md) | Ablage für neue Live-Protokolle; beim Erstellen dieses Pakets noch ohne Laufdaten |

Neue Simulationen auszuführen erfordert den vollständigen Projektcode. Die
Startbefehle in den technischen Dokumentationskopien beschreiben diesen Weg;
sie sind keine Voraussetzung zum Lesen und Prüfen der hier enthaltenen Ergebnisse.

Dokumentationspaket: 19.10.2026. Die enthaltenen Abschlussberichte stammen aus
den darin angegebenen Messreihen; für dieses Paket wurden keine neuen
wissenschaftlichen Messläufe durchgeführt.
