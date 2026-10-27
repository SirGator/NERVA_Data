# M9 kompakt: Kombination ohne funktionalen Lernnachweis

Bestätigungsreihe mit 20 neuen Seeds 610–629. Angegeben sind Mittelwerte des
gekoppelt trainierten Arms über Seeds und beide Belegungen. Zufallsniveau: 50 %.
Pilot und technische Kurzläufe werden nicht mitgerechnet.

| Bedingung | Sofort | Nach unabhängigen 2 s Ruhe | Online | Extra-Spikes sofort | Visueller Gewichtserhalt |
|---|---:|---:|---:|---:|---:|
| Referenz: ×1, 20 ms | 48,75 % | 48,75 % | 48,75 % | 0,00 | 59,2 % |
| Rekurrenz: ×4, 20 ms | 50,00 % | 51,25 % | 50,78 % | 21,65 | 58,2 % |
| STDP: ×1, 100 ms | 48,75 % | 48,75 % | 48,75 % | 0,00 | 46,7 % |
| Kombination: ×4, 100 ms | **51,25 %** | **50,00 %** | 51,74 % | 13,43 | 46,3 % |

**Keine der vier Bedingungen erfüllt die primären Lernkriterien.** Die
Kombination besteht weder die vollständigen Kontroll-/Belegungsvergleiche noch
die zusätzliche Prüfung, ob Rücksetzen der plastischen Gewichte die Leistung
abgesichert in beiden Belegungen verschlechtert.

Zusatzspikes werden außerhalb der direkt angeregten Aktionskopie-Zielzellen
gezählt. In der Rekurrenzbedingung entstehen sofort ohne neue Aktionskopie
bereits durchschnittlich 0,59 solcher Hintergrundspikes. Mehr Aktivität ist kein
Lernnachweis. Die mittlere visuelle Auslesbarkeit beträgt 99,73–100 %.

Tabelliert aus [summary.csv](../Experimente/m9-v2-confirm/summary.csv),
[propagation-summary.csv](../Experimente/m9-v2-confirm/propagation-summary.csv) und
[weight-summary.csv](../Experimente/m9-v2-confirm/weight-summary.csv).
Genauigkeiten und Spikes auf zwei Dezimalstellen gerundet, Gewichtserhalt auf eine.
Der Gewichtserhalt ist der Mittelwert der seedweisen Quotienten im gekoppelten Arm.

[Vollständiger Bericht](../M9_EXPERIMENT.md) ·
[Gewichtsinterventionen](../Experimente/m9-v2-confirm/causal-contrasts.csv) ·
[Prüfnachweis](../Experimente/m9-v2-confirm/verification.md).
