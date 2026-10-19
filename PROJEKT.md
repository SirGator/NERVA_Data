# Was ist NERVA?

NERVA ist ein Forschungsprojekt zu neuronalen Netzen mit einzelnen elektrischen
Impulsen, sogenannten Spikes. Untersucht wird, ob aus lokalen Veränderungen an
Neuronen und Synapsen erlernte Zusammenhänge zwischen Wahrnehmung und Handlung
entstehen können.

## Forschungsfrage

Die [ursprüngliche Haupthypothese](Dokumentation/HAUPTHYPOTHESE.md) beschreibt
die Entstehung anpassungsfähigen Verhaltens ohne globalen Loss, Backpropagation,
zentrale Policy oder globale Reward-Funktion. Die
[sensorimotorische Teilhypothese](Dokumentation/TEILHYPOTHESE.md) verlangt zwei
Schritte: Das Netz lernt Regelmäßigkeiten aus eigenen Handlungen und deren Folgen;
dieses Gelernte verändert später sein Verhalten.

Die bisherigen Messungen prüfen Voraussetzungen und begrenzte Teilaufgaben.
Ein positiver Befund bei einer Synapse beantwortet deshalb noch nicht die ganze
Forschungsfrage. Besonders die Reihen M3 bis M8 fragen: Lässt sich nach bekannter
Aktion bereits vor dem nächsten Wirkungsbild aus dem Netz ablesen, welche
Bildwirkung folgen wird, und beruht dieser Vorteil auf der gelernten Zuordnung?

## So arbeitet das Modell

```text
Bild der Umgebung → sensorische Neuronen → rekurrentes Netz → Motorneuronen
                                              ↑                 ↓
                                       eigene Aktionskopie ← ausgeführte Taste
                                                                ↓
                                                     verändertes Umgebungsbild
```

Im rekurrenten Netz können Neuronen einander über lokale Verbindungen wiederholt
anregen oder hemmen. Die Aktionskopie meldet dem Netz die tatsächlich ausgeführte
Taste. Sie enthält keine Vorgabe der späteren Bildwirkung. Ein äußerer Decoder
übersetzt motorische Spikes in virtuelle Tastendrücke.

Die Live-Anwendung beobachtet eine virtuelle Maschine über Bilder und steuert
deren Tastatur. Die kontrollierten Versuche verwenden außerdem kleine Rust-Welten
mit denselben Bild- und Tastentypen. Ein Versuch ohne gestartete QEMU-VM ist daher
kein neuer Live-VM-Test. Welche Umgebung verwendet wurde, steht im jeweiligen Bericht.

## Welche lokalen Mechanismen vorkommen

| Mechanismus | Aufgabe |
|---|---|
| LIF-Neuron | Sammelt Eingangswirkungen, lässt Potenzial abklingen und erzeugt beim Überschreiten der Schwelle einen Spike |
| Pair-STDP | Verändert synaptische Gewichte anhand des zeitlichen Abstands präsynaptischer Ankunft und postsynaptischen Spikes |
| Homöostase | Regelt lokale Aktivität und intrinsische Anregung |
| Utility | Bewertet lokal die Nutzung exzitatorischer Verbindungen |
| Wachstum und Pruning | Bildet lokale Verbindungen oder entfernt geeignete schwach genutzte Verbindungen |

Nicht jede Messreihe aktiviert alle Mechanismen. M7 und M8 verwenden beispielsweise
STDP, aber ausgeschaltete Homöostase und Strukturentwicklung. Die detaillierten
Einstellungen stehen in den Berichten und den gespeicherten Konfigurationen.

Der Standard des laufenden Modells mit 256 Processing-Neuronen ist außerdem nicht
mit jeder Versuchskonfiguration gleichzusetzen. Zahlreiche kontrollierte Reihen
verwenden 32 Core-Zellen und eine stark reduzierte visuelle Diagnosesensorik.
M8 benutzt zwei aus aktuellen Pixeln abgeleitete Kanäle. Ergebnisse daraus lassen
sich nicht ohne weitere Messungen auf das volle Live-Modell übertragen.

## Was das Modell wissen darf

Die neuronalen Eingänge der kontrollierten Wirkungsversuche bestehen aus aktuellen
Bildern und eigenen ausgeführten Tasten. Weltpositionen, zukünftige Wirkungsbilder,
richtige Wirkungsklassen und Ergebnisse der Auswertung bleiben außerhalb des
neuronalen Actors. Die externe Auswertung darf diese Größen zur Prüfung verwenden.

Bei M3 bis M8 werden Aktionen für die kontrollierte Erfahrung vorgegeben. Das
prüft die Bildung einer Handlungs-/Wirkungszuordnung und belegt für sich noch
keine selbstständig gelernte Auswahl erfolgreicher Handlungen. Der frühere
Agency-Versuch behandelt eigenständige Handlungsfähigkeit gesondert.

Die [frühere serielle Demo](SERIAL_MODEL.md) verwendet dagegen explizite
Lehrsignale. Sie zeigt eine lokale STDP-Zuordnung und die VM-Anbindung; sie ist
getrennt von der Hypothese ziel- und belohnungsfreien Wirkungslernens zu bewerten.

## Aufbau des Gesamtprojekts

| Bestandteil | Aufgabe |
|---|---|
| `NERVA` | Bibliothek mit neuronalen Grundbausteinen und lokalen Regeln |
| `NERVA_Modell` | Modellaufbau, Laufzeitprogramme, Versuchscode und QEMU-Adapter |
| `Messungen` | Dieses Informations- und Datenpaket |

Der Code wird zum Nachvollziehen dieses Pakets nicht benötigt. Technische Details
sind als lokale Dokumentationskopien enthalten:
[Architektur](Dokumentation/ARCHITECTURE.md),
[visuelles Modell](Dokumentation/VISUAL_MODEL.md) und
[Tastaturbelegung](Dokumentation/KEYBOARD_LAYOUT.md).

Weiter: [Ergebnisse](ERGEBNISSE.md) · [Methodik](METHODIK.md) · [Startseite](README.md).
