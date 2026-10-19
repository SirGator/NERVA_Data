# Projektgrenzen, laufendes Modell und Experimente

> Dokumentationskopie für das eigenständige Messpaket, Stand 19.10.2026. Datenlinks gelten innerhalb dieses Pakets. Enthaltene Startbefehle und Quellcodepfade beziehen sich auf das vollständige NERVA-Projekt.

Die Bibliothek liegt in `NERVA/`. Der Modell-, Adapter- und Versuchscode liegt
unter `NERVA_Modell/`; Daten und Ergebnisse liegen unter `Messungen/`.

## Verbindliche Abhängigkeitsregel

```text
Experimente → Modell → NERVA
                  └─→ nerva-qemu
```

`NERVA_Modell/Modell/` verbindet die neuronalen Bausteine mit der visuellen Schnittstelle.
`NERVA_Modell/Experimente/` ist ein eigenes Rust-Paket und verwendet das Modell als Bibliothek.
Es importiert zusätzlich NERVA-Zustandstypen und Adaptertypen für Kontrollen und
Auswertungen. Das Modell hängt nicht von den Experimenten ab. `NERVA/` und
`NERVA_Modell/nerva-qemu/` hängen weder direkt noch transitiv voneinander ab.

- **NERVA:** Neuronen, Synapsen, Dynamik, Plastizität, Utility, Homöostase und
  Strukturentwicklung. Kennt weder QEMU noch eine konkrete visuelle Aufgabe.
- **nerva-qemu:** QMP, Bilder, visuelle Aufbereitung, Kanalraten, Motorpulse,
  Tastaturaktionen und modellunabhängige Rust-Testwelten. Importiert keine NERVA-Typen.
- **Modell:** Netzaufbau, Konfiguration, Umwandlung zwischen beiden APIs,
  laufender Bild–Core–Tastatur-Zyklus und Lebenszyklus der visuellen Demo-VM.
- **Experimente:** Aufzeichnungen, kontrollierte Trainings-/Prüfabläufe,
  externe Readouts, Kontrollagenten, Parameterscans und das frühere serielle Experiment.

`./NERVA_Modell/Modell/run-demo.sh` startet das laufende Modell. `./NERVA_Modell/Experimente/run.sh`
startet die Versuchswerkzeuge. Experimentberichte und historische Messläufe
liegen unter `Messungen/Experimente/`; neue Live-Modellprotokolle unter `Messungen/Modell/`.
Alte Experimentaufrufe über `NERVA_Modell/Modell/run-demo.sh` werden weitergeleitet.

Das Gastprogramm `NERVA_Modell/Modell/guest/visual.S` definiert die konkrete A/D-Umgebung.
`NERVA_Modell/Modell/src/visual_vm.rs` startet diese gewählte Versuchs-VM. Die allgemeine
QMP-Kommunikation bleibt im Adapter. Das Modell bekommt ausschließlich Bilder,
keinen Gast-RAM, keine Positionswerte, Labels oder Belohnungen.

Der Bildadapter liefert `ChannelRate { channel, rate_hz }`. `Modell` verbindet
diese Raten mit NERVAs `PoissonSensoryTransducer`. Auf dem Rückweg konvertiert
es NERVAs Motor-Ausgaben in `MotorPulse { channel, at_us, amplitude }`. Erst
der Adapter interpretiert diese Pulse als virtuelle Tastaturaktionen.

## Aktueller rekurrenter Netzaufbau

Der Standard in `NERVA_Modell/Modell/src/model.rs` ist ein räumliches, rekurrentes Modell.
Der frühere direkte Sensor→Motor-Aufbau bleibt unter `--model direct` erhalten.

```text
Visuelle Sensorik (Ebene z=-1,5; 4.096 oder 8.192 Neuronen)
                         ↓
Processing-Population (256 räumliche Zellen, ca. 20 % inhibitorisch)
       ↔ lokale Rekurrenz, Pair-STDP, Utility, Homöostase
       ↔ lokales Wachstum und Pruning über NERVA
                         ↓
Motorik (Ebene z=1,5; 105 Tasten, im A/D-Versuch fünf)
       ├→ rohe Motor-Spikes → Processing
       └→ erfolgreich ausgeführte/gehaltene Tasten
              → eigene Aktionskopie-Zellen (z=1,2) → Processing
```

`NERVA_Modell/Modell/src/model/topology.rs` erzeugt nur ein dünnes, geseedetes Grundgerüst:

- Processing-Zellen liegen mit kleinem Seed-Jitter auf einem dreidimensionalen
  Raster, Abstand 0,12. Ihre Polaritäten werden geseedet verteilt.
- Jede visuelle Zelle projiziert auf vier zufällig gewählte Zellen aus ihren
  24 räumlich nächsten Processing-Nachbarn. Es gibt keinen direkten visuellen
  Sensor→Motor-Pfad im rekurrenten Modell.
- Jede Processing-Zelle besitzt anfangs höchstens vier zufällige ausgehende
  Verbindungen zu Zellen im Radius 0,25. Es gibt keine vorgegebenen Sequenzketten
  oder internen Verarbeitungsschichten.
- Jedes Motorneuron erhält acht geseedet gewählte exzitatorische Core-Eingänge.
  Rohe Motor-Spikes und zugehörige Aktionskopie-Zellen erreichen jeweils drei
  geseedete Core-Zellen. Diese Anschlussverbindungen bleiben bestehen.

256 Processing-Neuronen, Nachbarschaftsradien, Fan-in/Fan-out und Polaritätsanteil
sind Versuchskonfiguration, keine behauptete optimale Architektur.

## Lernen und Strukturentwicklung

NERVA stellt weiterhin sämtliche neuronalen Regeln bereit. Modell verwendet:

- `PairStdp`: Potenzierung 0,0001, Depression 0,00012, Zeitkonstanten 20 ms,
  Fenster 100 ms, Gewichtsgrenzen 0 bis 2.
- `LocalHomeostasis`: neuronlokale, unabhängig phasierte 100-ms-Uhren;
  Zielrate 8 Hz, Zielinput 50, intrinsische Anpassung 0,5,
  Strukturanpassung 0,002, intrinsische Stromgrenzen -10 bis 20,
  Wachstumsanforderung 0 bis 3.
- `ExcitatoryCausalUtility`: Eligibility 20 ms, Utility-Gedächtnis 500 ms,
  EMA-Faktor 0,1. Inhibitorische Verbindungen werden durch diese Regel nicht
  bewertet und deshalb nicht aufgrund fehlender exzitatorischer Utility entfernt.
- `IncomingGrowthDrive` und `local_candidates`: lokale Wachstumsanforderung,
  Aktivität, zeitliche Nähe und Distanz bestimmen neue eingehende Verbindungen.
- `DevelopmentPlan` und `PruningController`: validierte atomare Änderungen und
  Entfernung exzitatorischer Core-Synapsen unter Utility 0,01 nach 300 ms.

Die vorhandene Homeostase-API gilt pro Simulation und ist hier für alle
Populationen aktiv. Gezählt werden im Versuchsbericht ihre Änderungen an
Processing-Zellen. Neue und entfernte Verbindungen sind dagegen ausdrücklich
auf Processing→Processing begrenzt. Modell wählt dafür die zulässige Population;
Wachstumsnachfrage, Kandidatenscores, Pruning und Commit kommen aus NERVA.

Alle Processing-Zellen erhalten standardmäßig denselben Wachstumsbedarf 2,5
(`--initial-drive`, auch 0 möglich). Die Pruning-Mindestdauer ist mit
`--pruning-min-us` einstellbar; Standard bleibt 300.000 µs.
Eine Bildung verbraucht 0,5, Wachstum setzt Bedarf größer 0,5 voraus.
Neue Synapsen beginnen bei Gewicht 0,25 und Verzögerung 1 ms.
Der Bedarf wird anschließend durch lokale Homöostase verändert. Ein Wachstum
ist keine Garantie: Der Kandidatenscore muss mindestens 0,01 betragen.

Der Host führt alle 100 ms Simulationszeit einen Entwicklungsschritt zwischen
vollständigen Ereignisfenstern aus. Das ist ein Strukturkontrollpunkt; die
neuronal-synaptische Simulation bleibt ereignisgesteuert. Laufende Impulse
werden bei Pruning durch NERVAs Runtime konsistent storniert.

`Model::freeze()` schaltet diese plastischen Mechanismen am laufenden Modell
ab und erhält dessen gelernten Zustand. Der Trainieren–Einfrieren–Prüfen-Versuch
liegt vollständig in `NERVA_Modell/Experimente/src/retention.rs`; externe Readouts und
kontrolliert veränderte Aktionskopien führen keine Lernregeln in die Adapter ein.
Protokoll und gemessene Grenzen stehen in
[RETENTION_EXPERIMENT.md](../RETENTION_EXPERIMENT.md).

Der geschlossene Zielversuch liegt in `NERVA_Modell/Experimente/src/agency.rs`. Seine unabhängige
Welt liegt entsprechend dem Minimaltest-Aufbau in `NERVA_Modell/nerva-qemu/src/test_world.rs`;
nur der externe Auswerter liest ihren Erfolg und Abstand. Der Actor erhält
weiterhin ausschließlich Frames und seine eigenen Tastensignale. Regeln in
`NERVA/` bleiben unverändert. Der Ablauf und der negative Erstbefund stehen in
[AGENCY_EXPERIMENT.md](../AGENCY_EXPERIMENT.md).

`NERVA_Modell/Experimente/src/sensorimotor/` trennt anschließend Handlungskontrolle und Wirkungslernen.
`Step` liefert dafür auch exakte `MotorPulse`-Zeiten und nichtleere motorische
Ankünfte während Refraktärphasen. Eine optionale A/D-Konkurrenz fügt zwei
inhibitorische Vermittler mit vorhandener LIF-Dynamik hinzu; das Standardnetz
bleibt unverändert. Die experimentellen Decoder leben im unabhängigen Adapter.
Eigene Explorationsfolgen, Freeze und Gegenkontrollen werden weiterhin nur
in Experimente zusammengesetzt. Ergebnisse und Grenzen stehen in
[SENSORIMOTOR_EXPERIMENT.md](../SENSORIMOTOR_EXPERIMENT.md).

## Eigene Aktionen und visuelle Daten

Die externe Wahrnehmung bleibt auf Pixel beschränkt. Der Host meldet zusätzlich
seine eigenen erfolgreich gesendeten beziehungsweise gehaltenen Tasten zurück.
Das sind propriozeptive Aktionsinformationen, keine korrekten Soll-Antworten,
keine Positionswerte aus dem Gast und keine Belohnungen.

Rohe Motor-Spikes sind nicht mit ausgeführten Tasten gleichzusetzen: Der
Decoder kann enthalten oder Modifier halten. Deshalb werden rohe motorische
Rückführung und tatsächlich ausgeführte Aktionskopien separat protokolliert.
Aktionskopien besitzen eigene Eingangsneuronen und verändern keine Gewichte
außerhalb der normalen lokalen NERVA-Regeln.

## Gepaarter A/D-Versuch

`NERVA_Modell/Experimente/src/experiment.rs` vergleicht Strukturentwicklung und feste Topologie
bei identischem Anfangsnetz, Seed, Bildern, ausgeführten Aktionen, STDP und
Homöostase. Der Host zeichnet eine Folge A,A,D,D in QEMU auf und spielt diese
anschließend beiden Varianten vor. Die neuronalen Tastenvorschläge werden
während dieses Versuchs gemessen, aber nicht ausgeführt.

Jede Variante wird wiederholt. Verglichen werden sämtliche gespeicherten
Schrittwerte, die exakten Core-Spikezeiten und der abschließende `Network`-
Zustand. Dies ist keine Behauptung über CPU/GPU-Gleichheit oder neue Live-VM-Läufe.
Die gespeicherte Bildfolge kann ohne QEMU erneut verarbeitet werden.

Unterschiedliche Core-Muster zeigen einen Einfluss von Strukturentwicklung.
Sie beweisen weder funktionale Verbesserung noch gelernte Handlungswirkungen.
Insbesondere können A/D-konditionierte Aktivitätsmittel bereits durch
unterschiedliche visuelle Eingaben entstehen.

Befehle und Messergebnisse: [NERVA_Modell/Experimente/RECURRENT_EXPERIMENT.md](../RECURRENT_EXPERIMENT.md).


## Bekannte Aktion vor dem Wirkungsbild (M3)

`NERVA_Modell/Experimente/src/m3/` setzt die vorhandenen Regeln zu einem ziel- und belohnungsfreien
Versuch zusammen. Ein identisches Startbild, balancierte ausgeführte A/D-Aktionen
und verzögert gezeigte Wirkungsbilder trennen Aktionskenntnis von Zukunftsbildern.
`Model::step_for` erhält beim Wechsel kurzer Beobachtungsphasen laufende Zustände,
Zufallsströme und ausstehende Ereignisse; Entwicklung bleibt an 100-ms-Intervalle
gebunden. Training, zeitlich zerstörte Zuordnung und eingefrorene Kontrollen
liegen vollständig in Experimente. NERVA bekommt keine Wirkungslabels oder Auswerterwerte.

Der Standarddecoder im laufenden Modell nutzt bei nichtleeren Zählgleichständen
einen eindeutigen frühesten ersten Spike, auch für die vollständige ISO-Tastatur.
Die unabhängige Adapter-API bietet diese Regel optional; `--motor-decoder count`
erhält die historische Modellregel. Der separate kleine Motor-Scan variiert
Core→Motor-Gewichte, Motor-Refraktärzeit und vorhandene Konkurrenzinhibition.
Aufbau, Kontrollen und Grenzen: [M3_EXPERIMENT.md](../M3_EXPERIMENT.md).


## M4: JSON-Brücke und Diagnosetests

`NERVA_Modell/Modell/src/m4/` führt einen JSON-konfigurierten Fall mit dem bestehenden Modell
aus. Der Python-Orchestrator unter `NERVA_Modell/Experimente/m4/` definiert die Fälle und liest
ausschließlich externe Ergebnisse. Modell importiert keine Experimentbibliothek;
M3 verwendet nun denselben generischen Auswerter und balancierten Zeitplan aus
der Modellbibliothek. Beide Bibliotheken NERVA und nerva-qemu bleiben unabhängig.

Der M4-Modellport akzeptiert nur aktuelle Frames und bereits ausgeführte Tasten.
Die getrennte Testwelt plant echte Bewegungsereignisse. Feste Trialdauer,
visuelle Kalibrierung, Inputbudget und Freeze-Grenzen sind explizit dokumentiert.
Weitere Details: [NERVA_Modell/Experimente/m4/README.md](M4_METHODIK.md).

## M5: Signalparameter und ausgewählte Homöostase-Population

`NERVA_Modell/Modell/src/m5.rs` verwendet das bestehende Modell für zwei isolierte Ursachenversuche.
Der Plan und die externen Auswerter liegen in `NERVA_Modell/Experimente/m5/`. Core-Membranzeitkonstante
und Gewicht der bestehenden Aktionskopie-Anschlüsse sind konfigurierbare Modellparameter.
Die Standardwerte 20 ms und 0,9 sowie die Grundverschaltung bleiben erhalten.

`Simulation::set_homeostasis_population` in NERVA wählt anhand generischer Neuronen-IDs,
welche Zellen die vorhandene lokale Regel erhalten. Ohne Auswahl gilt weiterhin die
gesamte Population. Abgewählte Uhren werden storniert; neu ausgewählte Zellen beginnen
am aktuellen Zeitpunkt. Auch explizite Wartungsereignisse beachten die Auswahl.
Die Homöostaseregel selbst und die Trennung von NERVA und Adapter ändern sich nicht.

Modell übersetzt `HomeostasisScope::Core` beziehungsweise `CoreSensor` in diese IDs.
Die zweite Auswahl umfasst ausschließlich Processing- und visuelle Neuronen,
keine Aktionskopie- oder Motorneuronen. Der separate Ein-/Aus-Schalter und Freeze
gelten weiterhin. M5 protokolliert erzeugte Sensorimpulse, tatsächliche
Sensorneuronen-Emissionen und Populationsupdates zusätzlich; der M4-Vertrag und
seine bisherigen Ergebnisdateien bleiben erhalten. Ergebnisse und Grenzen stehen
in [NERVA_Modell/Experimente/M5_EXPERIMENT.md](../M5_EXPERIMENT.md).

## M6: kombinierte Eingriffe und unveränderter Elternzustand

`NERVA_Modell/Modell/src/m6.rs` führt die JSON-konfigurierten Vierervarianten aus; Plan,
Orchestrierung, Statistik und Messdaten liegen unter `NERVA_Modell/Experimente/m6/` und
`Messungen/Experimente/`. Der Actor erhält nur aktuelle Frames, ausgeführte Tasten
und Beobachtungsdauer. Testwelt, zukünftige Wirkungen und Auswerterlabels bleiben
außerhalb dieser Grenze. Bestehende Lernregeln und Live-Standardwerte bleiben erhalten.

Die Kalibrierung des externen Auswerters läuft auf einem durch dieselben
Eingaben reproduzierten Checkpointzweig. `Model::same_replay_state` vergleicht
dafür Netz und laufenden Ausführungszustand: insbesondere ausstehende Ereignisse,
STDP-Spuren, lokale Uhren, Sensorphase, Decoder und Modellzeit. Die generische
NERVA-Prüfung ist nur lesend; undurchsichtige Compute-/Utility-Implementierungen
müssen vom Aufrufer identisch und zustandslos gewählt werden. M6 erfüllt diese
Voraussetzung mit seinem festen CPU-Modell. Passive Audit-/Profilingdaten sind
ausgenommen. Die Elterninstanz bleibt während Kalibrierung und Checkpointzweigen
unverändert und beginnt ihren Online-Test ohne Kalibrierzeit oder Rücksetzen.

`NERVA_Modell/Modell/src/m6/mechanisms.rs` prüft ergänzend reale Eingänge auf unabhängigen
Zellkopien; `NERVA_Modell/Experimente/m6/core_control.py` führt die ausdrücklich separate
Core-Homöostase-Kontrolle aus. Beide ändern keine NERVA-Regel. Technische Grenzen,
Protokoll und gemessene Ergebnisse: [NERVA_Modell/Experimente/M6_EXPERIMENT.md](../M6_EXPERIMENT.md).

## M7: Synapsendiagnose im Experimentpaket

`NERVA_Modell/Experimente/src/m7.rs` zeichnet vorhandene M6-Erfahrungen erneut auf und prüft
einzelne Gewichtsupdates anhand ihrer realen nächsten Prä-/Post-Partner.
Die bestehende anfängliche Sensorstromnormierung ist als wiederverwendbare
Modellfunktion öffentlich. Python unter `NERVA_Modell/Experimente/m7/` übernimmt Plan,
Prozesssteuerung und unabhängige Auswertung. NERVA und Adapter werden nicht verändert.

`Model::diagnostic_synapse_weight` erlaubt kontrollierte Eingriffe ausschließlich
bei eingefrorener Plastizität, Entwicklung und Homöostase. Die Methode verwendet
NERVAs vorhandene Runtime-Transaktion für Synapsenänderungen; sie ist keine
neuronale Lernregel. Vor dem Eingriff werden vollständige ausführbare Zustände
auf getrennten Replay-Instanzen verglichen. Das Elternmodell, Zellen, Topologie
und Uhren bleiben erhalten. Bereits reisende Impulse behalten ihre bei Emission
festgelegten Amplituden. Live-Standardwerte und Anfangsverschaltung bleiben unverändert.

[M7-Ergebnisse und Grenzen](../M7_EXPERIMENT.md) trennen lokale
Zuordnungsspuren, elektrische Wirkung auf Potenziale und tatsächliche Spike-Weiterleitung.

## M8: vorhandene Dynamik konfigurieren, Versuche getrennt halten

`NERVA_Modell/Experimente/src/m8.rs` legt den Scan von sechs bestehenden Mechanismen fest;
CLI, Manifest, Statistik und Datenaudits bleiben in `NERVA_Modell/Experimente/`. Die sechs
neuen `ModelConfig`-Felder haben die bisherigen Werte als Standard. NERVA und
Adapter werden dafür nicht verändert. Die STDP-Regel bleibt nächste-Paar-STDP;
Modell übergibt lediglich die konfigurierte gemeinsame Plus-/Minus-Zeitkonstante.

Höhere Core-Dichte ergänzt zufällige lokale Kanten nach dem bisherigen Gerüst
aus einem eigenen Zufallsstrom. Originalkanten, Sensor-/Motoranschlüsse, Zellen
und Geometrie bleiben erhalten. Es werden keine Aktions-/Wirkungspfade vorgegeben.

Das bestehende M6-Replayprotokoll bietet optionale `RunOptions`: einen festen
Referenz-Ratenverstärker, unabhängige Ruhe-Checkpointzweige sowie tatsächliche
Core-Spikezeiten und No-copy-Kontrollen. Ohne Optionen bleibt die ursprüngliche
M6-Ausgabe bytegleich. Die Elterninstanz wird weiterhin nicht kalibriert oder
zurückgesetzt. Vorhersagen liegen vor Bewegung und Wirkungsbild. No-copy-Zweige
unterscheiden Aktionswirkung von bereits laufender Netzaktivität.

[M8-Ergebnisse](../M8_EXPERIMENT.md) und
[Ausführung/Dateivertrag](M8_METHODIK.md) trennen Weiterleitung,
synaptische Zuordnung und funktionalen Lernnachweis.
