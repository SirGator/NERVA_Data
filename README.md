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

**Stand der Versuche bis M9:** Lokale Gewichtsänderungen, Einflüsse der
Strukturentwicklung und zusätzliche rekurrente Aktivität sind gemessen.
Ein belastbarer funktionaler Nachweis gelernter Handlungswirkungen fehlt in den
untersuchten Bedingungen weiterhin. Die Forschungsfrage bleibt offen.

**Forschungsplanung vom 28.10.2026:** Der
[Fahrplan M9–M13](Dokumentation/FORSCHUNGSPLAN.md) priorisiert den kontrollierten
Nachweis funktionalen Lernens. [M9-v2](M9_EXPERIMENT.md) ist mit
20 Bestätigungsseeds und Gewichtsrücksetzungen abgeschlossen und liefert keinen
funktionalen Lernnachweis. Technische Kurzläufe bleiben gesondert markiert.
M10 ist einschließlich M10-E abgeschlossen. Als nächster begrenzter Lernversuch
ist M11 mit synaptischer Konkurrenz vorgeschlagen; dafür gibt es noch keinen Lauf.

[M10](M10_EXPERIMENT.md) lokalisiert anschließend auf denselben M9-Seeds den
Gewichtsbeitrag zu Eingängen, Potenzialen, Spikezählmustern und festen
Ausleserentscheidungen. Diese retrospektive Diagnose liefert keinen neuen
unabhängigen Lernnachweis.

[M10-B](M10B_EXPERIMENT.md) prüft die Wirkungsausrichtung auf der vorhandenen
visuellen Achse. Ein gemeinsamer Projektionsoffset erklärt die schwache
Vorhersage nicht vollständig; die Paar-Rangfolge bleibt eine reine Diagnose.

[M10-C](M10C_EXPERIMENT.md) rekonstruiert anschließend Eingangsimpulse,
Refraktärfilter, Leck und Resets. Die unpassende Ausrichtung ist auf der festen
neuronalen Gewichtung bereits in der Eingangsbilanz sichtbar; die ursprüngliche
Ursache innerhalb der Rückkopplung bleibt durch gezielte Eingriffe zu prüfen.

[M10-D](M10D_EXPERIMENT.md) blockiert rekurrente Erregung und Hemmung getrennt
aus identischen eingefrorenen Checkpoints. Weniger Hemmung erhöht die Aktivität,
liefert aber keinen beidseitigen Vorhersagevorteil. Auch das Entfernen rekurrenter
Erregung löst den Engpass nicht; die Diagnose nutzt dieselben bekannten Seeds.

[M10-E](M10E_EXPERIMENT.md) kreuzt Core-Gewichtsrücksetzung und vier
Rekurrenzsperren nach gemeinsamer Baseline. Der Gewichtseinfluss benötigt hier
rekurrente Erregung; eine stärkere Wirkung ohne Hemmung erzeugt keinen
zuverlässigen beidseitigen Vorhersagevorteil.

Das Repository heißt `NERVA_Data`. Hinweise zum vollständigen Download mit den
zwei großen Git-LFS-Dateien stehen unter [Herunterladen](HERUNTERLADEN.md).

## Grafisch ansehen

Die Messdaten lassen sich mit dem enthaltenen lokalen Dashboard durchsuchen:

```bash
./gui.sh
```

Benötigt wird nur Python 3.10 oder neuer. Der Browser öffnet
`http://127.0.0.1:8766`. [Anleitung für die Archiv-GUI](GUI/README.md).
Die GUI funktioniert auch dann, wenn nur dieses Messpaket heruntergeladen wurde.

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
| M9: Kombination und Gewichtskausalität auf 20 neuen Seeds | [M9](M9_EXPERIMENT.md) |
| M10: Retrospektive Signalweg- und Ausleserdiagnose | [M10](M10_EXPERIMENT.md) |
| M10-B: Wirkungsausrichtung und gemeinsamer Decoderbias | [M10-B](M10B_EXPERIMENT.md) |
| M10-C: Eingangsbilanz, Leck, Refraktärfilter und Resets | [M10-C](M10C_EXPERIMENT.md) |
| M10-D: Eingriffe in rekurrente Erregung und Hemmung | [M10-D](M10D_EXPERIMENT.md) |
| M10-E: Core-Gewichtsreset mit Rekurrenzsperren gekreuzt | [M10-E](M10E_EXPERIMENT.md) |
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

Ursprüngliches Dokumentationspaket: 19.10.2026; für dessen Zusammenstellung
wurden damals keine neuen wissenschaftlichen Messläufe durchgeführt.
Ergänzung vom 27.10.2026: M9-Pilot und Bestätigung mit vollständigen Rohdaten,
Audits und Ergebnisbericht.
