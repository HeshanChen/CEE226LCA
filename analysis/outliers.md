# Outlier rules

Rules use only the reference LCA and the features, never an LLM estimate.

| Rule | Definition | Buildings |
|---|---|---|
| R1 incomplete | new construction with no fenestration GWP | 10 |
| R2 out of scope | `lca_phys_scope` has no Enclosure (E) | 13 |
| R3 extreme | log value outside Tukey's fences (11.6 to 472 kgCO2e/m2) | 18 |
| Any rule | | **30** (10.3%) |

Cleaned set: 262 buildings (dev 181, test 81).

Outliers by project type: New Construction 11, Minor Renovation 9, Tenant Improvement 7, Major Renovation 3.

| project | value | type | scope | incomplete | out of scope | extreme |
|---|---|---|---|---|---|---|
| 108 | 0.5 | Minor Renovation | SEC |  |  | x |
| 74 | 0.6 | New Construction | BSE | x |  | x |
| 134 | 2.6 | Tenant Improvement | CF |  | x | x |
| 135 | 2.7 | Minor Renovation | SCF |  | x | x |
| 163 | 3.1 | Minor Renovation | CF |  | x | x |
| 136 | 4.3 | Tenant Improvement | CF |  | x | x |
| 54 | 6.5 | Major Renovation | BSE |  |  | x |
| 99 | 6.5 | Minor Renovation | SEC |  |  | x |
| 43 | 6.8 | Minor Renovation | CF |  | x | x |
| 66 | 7.0 | New Construction | BSECF | x |  | x |
| 104 | 7.6 | Tenant Improvement | CF |  | x | x |
| 80 | 9.4 | New Construction | BSE | x |  | x |
| 122 | 10.0 | Major Renovation | SCF |  | x | x |
| 103 | 10.1 | Minor Renovation | SECF |  |  | x |
| 42 | 10.4 | Minor Renovation | CF |  | x | x |
| 56 | 10.7 | New Construction | BSEC |  |  | x |
| 146 | 11.3 | Tenant Improvement | ECF |  |  | x |
| 101 | 11.6 | Tenant Improvement | CF |  | x |  |
| 85 | 12.9 | Tenant Improvement | CF |  | x |  |
| 205 | 13.2 | Minor Renovation | SCF |  | x |  |
| 10 | 14.0 | Major Renovation | CF |  | x |  |
| 234 | 15.5 | New Construction | BSE | x |  |  |
| 35 | 17.2 | New Construction | BSE | x |  |  |
| 27 | 24.9 | New Construction | BSE | x |  |  |
| 228 | 26.1 | Tenant Improvement | CF |  | x |  |
| 217 | 27.0 | New Construction | BSECF | x |  |  |
| 91 | 29.2 | New Construction | BSE | x |  |  |
| 141 | 41.7 | New Construction | BSE | x |  |  |
| 264 | 141.4 | New Construction | BSECF | x |  |  |
| 137 | 513.9 | Minor Renovation | BSECF |  |  | x |
