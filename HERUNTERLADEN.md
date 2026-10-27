# Informationspaket und Rohdaten herunterladen

Dieses Repository enthält den Ordner `Messungen` als eigenständiges Projekt.
Die Bibliothek und der Simulationscode des Gesamtprojekts werden zum Lesen
der Dokumentation und Analysieren der vorhandenen Ergebnisse nicht benötigt.

## Überblick ohne großen Download

Die [Startseite](README.md), der [Projektüberblick](PROJEKT.md) und die
[Ergebnisse](ERGEBNISSE.md) sind direkt auf GitHub lesbar. Von dort führen lokale
Links zu Berichten und kleinen Ergebnistabellen. Die vollständigen Rohdaten
umfassen einschließlich M9 und M10-E ungefähr 11,5 GB (Stand 27.10.2026).

## Vollständige Daten mit Git LFS

Zwei große CSV-Dateien werden über Git Large File Storage gespeichert.
Die Regeln stehen in [.gitattributes](.gitattributes). Nach Installation von
Git und Git LFS das Repository herunterladen:

```bash
git lfs install
git clone https://github.com/SirGator/NERVA_Data.git
cd NERVA_Data
git lfs pull
```

Die letzte Zeile lädt gegebenenfalls noch fehlende große Dateien. Danach sind
die normalen CSV-Inhalte lokal vorhanden. Git LFS verändert ihren Inhalt nicht.
Eine kleine Textdatei mit der ersten Zeile `version https://git-lfs.github.com/spec/v1`
ist dagegen nur ein LFS-Verweis, noch keine Messdatei.

Mit allen heruntergeladenen Dateien lässt sich die Paketintegrität prüfen:

```bash
sha256sum --check --quiet PRUEFSUMMEN.sha256
```

Beim GitHub-Download über „Download ZIP“ hängt die Aufnahme der LFS-Inhalte
von der Repository-Einstellung ab. Der Betreiber kann unter **Settings → Archives →
Include Git LFS objects in archives** die echten Dateien einschließen. Enthält ein
ZIP nur Verweisdateien, ist der oben beschriebene Git-LFS-Download erforderlich.
Die offizielle [Erklärung zu LFS in GitHub-Archiven](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository)
beschreibt diese Einstellung.

[Startseite](README.md) · [Datenhandbuch](DATENHANDBUCH.md).
