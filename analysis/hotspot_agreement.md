# Hotspot agreement (proposal 6.4, LEED v5 MRp2)

Mention-based proxy: an answer 'names' a category when its text matches the category's keywords (see `KEYS` in `analysis/hotspot_agreement.py`). Reference hotspots are the 3 largest design-level material categories of each building's enclosure A1-A3. Means over all answers (buildings x runs); the 10 flagged incomplete references are excluded.

Typical-building guess (most frequent reference top-3): Insulation, Glass & windows, Aluminum framing.

Reference top-1 category, share of buildings: Insulation 36%, Aluminum framing 19%, Glass & windows 16%, Concrete 10%, Cladding & panels 6%

Chance = expected value when the same number of categories is named at random out of 11 (top-1 hit and top-3 recall both equal n_named / n_categories).

| Condition | Top-1 named | Top-3 recall | Chance at same count | Categories named per answer | Precision |
|---|---|---|---|---|---|
| typical-building guess | 71.6% | 61.1% | 27.3% | 3.0 | 60.4% |
| 20261104_baseline-innate | 81.4% | 77.1% | 51.4% | 5.7 | 42.0% |
| 20261104_prompt-v2 | 93.3% | 89.7% | 67.5% | 7.4 | 36.9% |
| 20261104_prompt-v3 | 94.6% | 89.7% | 60.5% | 6.7 | 41.1% |

Building-specific test: the 80 buildings whose top-1 category is not in the typical guess (e.g. concrete, masonry or cladding dominated).

| Condition | Top-1 named | Top-3 recall | Chance at same count |
|---|---|---|---|
| typical-building guess | 0.0% | 42.1% | 27.3% |
| 20261104_baseline-innate | 74.6% | 79.3% | 53.6% |
| 20261104_prompt-v2 | 81.2% | 87.9% | 68.6% |
| 20261104_prompt-v3 | 82.1% | 88.2% | 62.4% |
