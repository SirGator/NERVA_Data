# Die Messdaten lesen

Dieses Handbuch beschreibt die vorhandene Ablage und häufige Felder. Die
Versuchsverträge unter [Dokumentation](Dokumentation/README.md) ergänzen die
genauen Schemata der einzelnen Reihen. Nicht jede Datei verwendet alle hier
genannten Felder.

## Vom Ergebnis zur Einzelbeobachtung

Am Beispiel M8:

1. Die [wissenschaftliche Einordnung](M8_EXPERIMENT.md) erklärt Fragestellung,
   Parameter, Endpunkte und Grenzen.
2. Die [Zusammenfassung des Messlaufs](Experimente/m8-confirm/summary.md) zeigt die
   wichtigsten Kennzahlen; [summary.csv](Experimente/m8-confirm/summary.csv) enthält
   die zugehörigen Tabellenwerte.
3. Der [gespeicherte Plan](Experimente/m8-confirm/manifest.json) nennt Bedingungen,
   Seeds und feste Vorgaben. Die einzelnen Konfigurationen liegen unter `configs/`.
4. Unter `results/` liegen Ergebnisse pro Bedingung und Seed sowie die
   zugehörigen CSV-Begleitdateien. Ein konkretes Beispiel ist
   [Referenz, Seed 510](Experimente/m8-confirm/results/reference/seed-510.json).
5. [diagnostics.json](Experimente/m8-confirm/diagnostics.json) und
   [verification.md](Experimente/m8-confirm/verification.md) dokumentieren
   Datenprüfungen und damalige Softwareverifikation.

Eine Kennung wie `seed-510.json.details.csv` gehört zu `seed-510.json`.
Das doppelte Suffix kennzeichnet eine Begleitdatei und ist beabsichtigt.

## Wiederkehrende Dateien

| Datei oder Muster | Inhalt |
|---|---|
| `manifest.json`, vereinzelt `plan.json` | Geplante Bedingungen, Seeds und Protokollangaben |
| `configs/<Bedingung>/seed-….json` | Eingabekonfiguration für einen einzelnen Lauf |
| `results/…/*.json` | Zusammengefasste Messwerte und tatsächlich verwendete Konfiguration |
| `summary.md`, `*-summary.md` | Lesbare Zusammenfassung des jeweiligen Laufs |
| `summary.csv` | Aggregierte Tabellenwerte; nicht in jeder Reihe vorhanden |
| `*.details.csv` | Einzelvorhersagen, Phasen, Zeitpunkte, Klassen und Aktionsdiagnosen |
| `*.audit.csv` | Zustands-, Eingangs- und Freeze-Prüfungen; genaue Spalten sind versuchsspezifisch |
| `prediction-contrasts.csv`, M4: `contrasts.csv` | Gepaarte Vergleiche zwischen Bedingungen oder Kontrollarmen |
| `*.events.csv` | Optionale ausführliche Ereignisprotokolle |
| `diagnostics.json` | Ergebnisse unabhängiger Prüfungen und abgeleitete Diagnosen |
| `verification.md` | Dokumentation damaliger Softwaretests und Wiederholungsläufe |
| `*.log`, `*.stdout.log`, `*.stderr.log` | Gespeicherte Programmausgaben |
| `source-sha256.json` | Historische Hashes von Quellcode und weiteren damaligen Artefakten |
| `data-sha256.json` | Historische Hashes ausgewählter Messdateien und Berichte |

M7 speichert seine Diagnose beispielsweise unter
`Experimente/m7-synapse-audit/results/seed-400/`. Dort heißen die Dateien
`result.json`, `weights.csv`, `pairs.csv` und weitere Diagnoseexporte. Das ist
kein Fehler gegenüber dem anders aufgebauten M8-Verzeichnis.

## Einheiten und wichtige Spalten

CSV-Dateien verwenden Kommas als Trennzeichen und Punkte als Dezimalzeichen.
Für eine Tabellenkalkulation daher den Import mit Komma und passender
Zahleninterpretation wählen. In den Zusammenfassungen werden Bruchteile oft als
Prozente angezeigt: `0.5` in einer Genauigkeitsspalte entspricht 50 %.

| Feld | Bedeutung |
|---|---|
| `case`, `case_id` | Kennung der untersuchten Parameterbedingung |
| `seed` | Kennung der Zufallsinitialisierung; siehe [Methodik](METHODIK.md) |
| `arm` | Kontroll- oder Lernzustand, etwa `paired` oder `aged_frozen` |
| `mapping` | Normale oder umgekehrte Zuordnung von Tasten zu Wirkungen |
| `stage` | Trainings- oder Prüfphase |
| `trial` | Index einer Beobachtung innerhalb des betreffenden Arms, Mappings und der Phase |
| `action_us` | Zeitpunkt der ausgeführten Aktion in Mikrosekunden Simulationszeit |
| `forecast_us` | Zeitpunkt der Vorhersage |
| `motion_us`, `effect_image_us` | Zeitpunkt der Bewegung beziehungsweise Präsentation des Wirkungsbildes |
| `shown_effect`, `actual_effect` | Gezeigte beziehungsweise tatsächliche Wirkungsklasse; beim entkoppelten Training können sie abweichen |
| `count_prediction`, `time_prediction` | Externe Vorhersage aus Spikezählungen beziehungsweise zeitlichen Merkmalen |
| `copy_arrivals_before_image` | Zahl der erfassten Aktionskopie-Ankünfte vor dem Wirkungsbild |
| `cue_core_spikes` | Gemessene Core-Spikes im Aktionsfenster |
| `visual` | Leistung der visuellen Ausleseprüfung; keine Handlungs-Vorhersageleistung |
| `checkpoint_probe` | Vorhersageprobe am Trainingscheckpoint im jeweiligen Protokoll |
| `rest_checkpoint_probe` | M8-Probe nach unabhängiger Ruhephase aus demselben Trainingscheckpoint |
| `probe` | Online-Vorhersageprobe |
| `retained_probe`, `interference_probe` | Nachfolgende Prüfung nach Ruhe beziehungsweise Interferenz im sequenziellen Ablauf |
| `*_evidence`, `*_confirmed` | Ergebnis der im betreffenden Protokoll definierten Kriterien, kein universeller Wahrheitswert |

Klassenwerte wie `-1` und `1` stehen in den binären Wirkungsversuchen für die
beiden Wirkungsrichtungen. Sie sind keine Belohnungen. Für einzelne Analysen
Zeilen immer mit Bedingung, Seed, Arm, Mapping, Phase und Trial zuordnen; eine
Trialnummer allein ist kein eindeutiger Schlüssel über das gesamte Paket.

Bei M7 benennt `pre` die Quellzelle und `post` die Zielzelle einer Synapse.
`synapse` ist deren Kennung, `weight` ihr Gewicht und `time_us` die Simulationszeit.
Eine Neuronen-ID bezeichnet keine über alle Seeds identische Funktion. Die
Anfangstopologie im jeweiligen Ergebnis erklärt die tatsächlichen Anschlüsse.

M8 verwendet in `propagation-summary.csv` unter anderem:

| Feld | Bedeutung |
|---|---|
| `windows` | Zahl der zusammengefassten Beobachtungsfenster |
| `mean_core_spikes` | Mittlere gesamte Core-Spikezahl pro Fenster |
| `mean_extra_core_spikes` | Mittlere Spikes außerhalb der direkt angeregten Kopie-Zielzellen |
| `mean_no_copy_extra_spikes` | Derselbe Zusatzspike-Messwert in der Probe ohne Aktionskopie |
| `mean_action_extra_difference` | Differenz zwischen Aktion und Kontrolle ohne Kopie |

## Bilder und frühere Messungen

Frühere Live-Läufe enthalten `report.json`, `trace.csv` und Bilder wie `first.ppm`,
`last.ppm` und `current.ppm`. PPM ist ein unkomprimiertes Bildformat. Manche Läufe
enthalten zusätzlich PNG-Dateien, zum Beispiel
[diese frühe Bildaufnahme](Experimente/verified/first.png). Eine Bildaufnahme
belegt die Aufnahme der Umgebung, für sich jedoch keinen Lernerfolg.

`recording.json` und zugehörige Bilddateien sind gespeicherte Bild-/Aktionsfolgen.
Sie dienen kontrollierten Wiederholungen. Topologie- oder Parameterexporte sind
nicht automatisch wieder ladbare vollständige Laufzeit-Checkpoints.

## Historische Pfade und Prüfsummen

In originalen JSONs, Hashlisten und Logs können noch Pfade mit
`Experimente/runs/`, `Modell/runs/` oder absolute Pfade des damaligen Rechners
stehen. Diese Texte sind historische Metadaten. Die Dateien liegen nun innerhalb
dieses Pakets unter `Experimente/` beziehungsweise `Modell/`; das
[Messreihenverzeichnis](Experimente/README.md) ordnet sie zu.

Beispiel: `Experimente/runs/m8-confirm/results/reference/seed-510.json`
bezeichnet hier `Experimente/m8-confirm/results/reference/seed-510.json`.
Alte Angaben zu `Modell/runs/` können auch archivierte Versuchsläufe meinen,
die heute unter `Experimente/` liegen; den benannten Lauf im Verzeichnis nachschlagen.

Die historischen `source-sha256.json`-Dateien dokumentieren den damaligen
Quellstand. Die Quelldateien selbst sind in diesem Datenpaket nicht enthalten.
Eine Dokumentationskopie mit angepassten Links muss daher auch nicht den alten
Quell-Hash eines Berichts erfüllen. Die originalen Messdateien und historischen
Prüfberichte bleiben unverändert. Eine aktuelle, paketbezogene Hashliste wird in
[Dokumentationsstand](DOKUMENTATIONSSTAND.md) erklärt.

Zurück: [Startseite](README.md) · [Ergebnisse](ERGEBNISSE.md).
