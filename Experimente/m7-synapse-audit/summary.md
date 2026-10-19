# M7 – gemessene Synapsendiagnose

Explorative Replays aller vorhandenen Core-off-Seeds 400–409; keine neue Lernregel und kein neuer funktionaler Lernnachweis.

| Arm | Core-Kanten verstärkt | abgeschwächt | unverändert | Mittlere absolute Änderung | Größte absolute Änderung |
|---|---:|---:|---:|---:|---:|
| aged_frozen | 0.00 | 0.00 | 128.00 | 0.000000 | 0.000000 |
| paired | 7.40 | 8.80 | 111.80 | 0.000963 | 0.047186 |
| scrambled | 7.50 | 8.80 | 111.70 | 0.000953 | 0.046426 |

| Eingriff, gekoppelter Arm | Core-Spikes | Spikes außerhalb der Kopie-Zielzellen | Veränderte Spikefolgen gegenüber Sham | Maximale Potenzialänderung |
|---|---:|---:|---:|---:|
| sham | 3.000 | 0.000 | 0/40 | 0.000000 |
| restore_core | 3.000 | 0.000 | 0/40 | 0.032855 |
| restore_all_plastic | 3.000 | 0.000 | 0/40 | 0.032855 |
| block_core | 3.000 | 0.000 | 0/40 | 0.591560 |
| no_copy | 0.000 | 0.000 | 40/40 | 1.190755 |

[Gewichte](weights-summary.csv) · [Zeitpaare](pair-summary.csv) · [Belegungsvergleich](mapping-summary.csv) · [Gegenprüfungen](counterfactuals.csv) · [Datenaudit](diagnostics.json).

Die direkte Gewichtszuordnung ist eine aus Anschlusszellen abgeleitete topologische Diagnose, kein funktionaler Lernnachweis. Gefrorene Gewichtsretention folgt aus dem Abschalten der Plastizität und belegt keine Konsolidierung. Bootstrapintervalle sind deskriptiv.
