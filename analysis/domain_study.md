# Domain knowledge: envelope documents in context (run 0, 292 buildings)

domain-envelope = prompt v1 + four envelope-focused documents (30k characters each): RDH 2025 spray-foam wall assemblies, CLF 2023 North American Material Baselines, Arup/Saint-Gobain facades and glass, UBC 2022 fenestration. Run 0 of every condition uses the same chunks and building order.

| condition | n | coverage % | median |log err| | geo-mean est/true | RMSE |
|---|---|---|---|---|---|
| v1 (innate) | 292 | 17.8 | 0.519 | 0.718 | 81.2 |
| domain-envelope (v1 + documents) | 292 | 15.8 | 0.609 | 0.606 | 85.3 |
| v3 (final prompt) | 292 | 24.3 | 0.461 | 0.860 | 77.8 |

Paired (Δ = second minus first):

| comparison | Δ coverage pp | Δ median |log err| | McNemar p | Wilcoxon p | closer than all % |
|---|---|---|---|---|---|
| domain-envelope vs v1 | -2.1 | 0.090 | 0.480 | 0.000 | 34.6 |
| v3 vs domain-envelope | 8.6 | -0.148 | 0.011 | 0.000 | 66.1 |

Median estimate/reference by XPS presence:

| condition | median ratio, XPS projects | median ratio, no XPS |
|---|---|---|
| v1 (innate) | 0.641 | 0.779 |
| domain-envelope (v1 + documents) | 0.501 | 0.683 |
| v3 (final prompt) | 0.734 | 0.979 |

Share of answers (%) that cite the documents or name XPS / HFC:

| condition | cites a document | mentions XPS | mentions HFC / blowing agent | median answer words |
|---|---|---|---|---|
| v1 (innate) | 0.000 | 0.685 | 0.000 | 99.0 |
| domain-envelope (v1 + documents) | 21.9 | 0.000 | 0.000 | 105.0 |
| v3 (final prompt) | 0.000 | 92.1 | 90.4 | 212.5 |
