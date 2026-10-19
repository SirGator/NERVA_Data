# Minimaltest für Handlungsfähigkeit

1 Seeds, 680 Episoden insgesamt, maximal 6 Aktionen pro Episode.

| Variante | Vorher | Nach Training, eingefroren | Tasten vertauscht, vor Anpassung | Nach Anpassung, eingefroren |
|---|---:|---:|---:|---:|
| development | 5.6% | 5.6% | 0.0% | 5.6% |
| fixed_topology | 5.6% | 5.6% | 0.0% | 5.6% |
| weight_only | 5.6% | 11.1% | 5.6% | 0.0% |
| frozen | 5.6% | 0.0% | 5.6% | 0.0% |
| random | 27.8% | 44.4% | 27.8% | 22.2% |

Machbarkeitskriterien erfüllt: **false**.

Zielkoordinaten, Abstände, Erfolg und korrekte Aktionen gelangen nicht ins Modell. Der sichtbare Zielrahmen ist die einzige Zielrepräsentation. Es gibt keine neue Motivation oder Belohnungsregel und keine Ersatzpolitik bei neuronaler Stille. Der Zufallsagent dient als Kontrolle. Eingefrorene Prüfphasen behalten gelernte Parameter; Membranen und Eingangshistorie entwickeln sich weiter.

[Messwerte und Kriterien](agency.json), [Episoden](agency-episodes.csv), [Aktionen](agency-actions.csv), [Lernverlauf](agency-learning.csv).
