# Messungen grafisch ansehen

Dieses Verzeichnis enthält den eigenständig nutzbaren NERVA-Messbetrachter.
Die fertige Browseroberfläche und der lokale Server sind vollständig enthalten.
Internet, Node.js, Rust, QEMU und die Modellbibliothek werden nicht benötigt.
Voraussetzung ist **Python 3.10 oder neuer**.

## Starten

Unter Linux oder macOS aus dem heruntergeladenen Messpaket:

```bash
./gui.sh
```

Oder unter Windows, Linux und macOS:

```bash
python3 GUI/server.py
# Unter Windows gegebenenfalls: py GUI/server.py
```

Der Browser öffnet automatisch `http://127.0.0.1:8766`.
Das Terminal bleibt geöffnet; Strg+C beendet den Server. Für einen anderen
Port `--port 9000` ergänzen. Mit `--no-browser` den Browser selbst öffnen.
Der Start funktioniert auch von einem anderen Arbeitsverzeichnis mit dem
absoluten Pfad zu `GUI/server.py`.

## Bedienung

1. **Messarchiv:** Eine Messreihe links auswählen. Suche und Typfilter grenzen
   die Liste ein. Die Übersicht zeigt gespeicherte Tabellen und, soweit vorhanden,
   Vorhersagekennzahlen. Messgröße und Vergleichsmessgröße bestimmen das Diagramm.
2. **Dateien:** Ordner öffnen und CSVs, JSONs, Bilder oder Texte auswählen.
   CSV-Vorschauen enthalten bis zu 100 Zeilen pro Seite. „Nächste Zeilen“ liest
   weiter; die Suche filtert zeilenweise. Jede Suchanfrage scannt höchstens 50.000
   Zeilen; bei sehr großen Dateien lässt sich mit der nächsten Seite fortsetzen.
3. **Diagramm:** In einer CSV-Vorschau die Y-Spalte und optional die X-Spalte
   auswählen. Gezeigt wird die aktuelle Vorschauseite mit den tatsächlichen
   Tabellenwerten. Ein solches Diagramm ist keine neue statistische Auswertung.
4. **Bericht öffnen:** Die vorhandene Zusammenfassung lesen. Links innerhalb
   der Dokumente öffnen andere lokale Berichte und Datendateien.
5. **Dokumentation:** Projektidee, Methodik und ausführliche Berichte ansehen.
   „Original herunterladen“ speichert die unveränderte ausgewählte Datei.

Große Dateien werden schrittweise gelesen und gestreamt. JSON-/Textvorschauen
sind auf 256 kB begrenzt; der Originaldownload ist vollständig. Diagramme ergänzen
keine fehlenden Messwerte und berechnen keine erfundenen Fehlerbalken. Die
Kennzahl „Bestätigte Endpunkte“ zählt nur die expliziten Kriterienfelder der
angezeigten Tabelle; ein Strich bedeutet, dass solche Felder nicht vorliegen.

Es wird keine Datei in einem historischen Messlauf geändert. Der reine
Archivserver startet keine Simulationen und benötigt keine Verbindung zu den
anderen Projektordnern. Er ist nur auf dem eigenen Rechner erreichbar.

## Neue Live-Läufe ansehen

Läufe mit `dashboard.json` und `network.json` lassen sich über **Dateien** ebenfalls
öffnen; die zugehörigen Bilder, CSV-Protokolle und Berichte bleiben verfügbar.
Für das laufende Modell gibt es zusätzlich ein steuerbares Live-Dashboard im
Gesamtprojekt. Es gehört zum Modellpaket und ist hier bewusst nicht erforderlich.

Wenn eine Datei nur einen Git-LFS-Verweis enthält, fehlen noch ihre eigentlichen
Messdaten. Dann die [Downloadhinweise](../HERUNTERLADEN.md) beachten.

## Paketstand

GUI ergänzt am 22.10.2026. `server.py` verwendet ausschließlich die
Python-Standardbibliothek. `dist/` enthält die gebaute React-Oberfläche ohne
extern geladene Schriftarten, Skripte oder Dienste. Die Paketprüfsummen erfassen
auch diese Dateien; die internen Cacheverzeichnisse sind ausgenommen.

[Startseite des Messpakets](../README.md) · [Datenhandbuch](../DATENHANDBUCH.md).
