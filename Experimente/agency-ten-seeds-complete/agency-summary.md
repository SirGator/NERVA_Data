# Minimaltest für Handlungsfähigkeit

10 Seeds, 6800 Episoden insgesamt, maximal 6 Aktionen pro Episode.

| Variante | Vorher | Nach Training, eingefroren | Tasten vertauscht, vor Anpassung | Nach Anpassung, eingefroren |
|---|---:|---:|---:|---:|
| development | 3.3% | 6.1% | 3.9% | 2.8% |
| fixed_topology | 3.3% | 4.4% | 2.8% | 3.9% |
| weight_only | 3.3% | 5.0% | 3.3% | 3.3% |
| frozen | 3.3% | 5.0% | 3.3% | 3.9% |
| random | 31.1% | 22.8% | 30.6% | 22.2% |

Machbarkeitskriterien erfüllt: **false**.

Zielkoordinaten, Abstände, Erfolg und korrekte Aktionen gelangen nicht ins Modell. Der sichtbare Zielrahmen ist die einzige Zielrepräsentation. Es gibt keine neue Motivation oder Belohnungsregel und keine Ersatzpolitik bei neuronaler Stille. Der Zufallsagent dient als Kontrolle. Eingefrorene Prüfphasen behalten gelernte Parameter; Membranen und Eingangshistorie entwickeln sich weiter.

[Messwerte und Kriterien](agency.json), [Episoden](agency-episodes.csv), [Aktionen](agency-actions.csv), [Lernverlauf](agency-learning.csv).
