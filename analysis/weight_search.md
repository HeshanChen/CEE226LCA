# Evidence-weight search (bottom-up run: `20261104_prompt-v3`)

Cleaned development set: 181 buildings; cleaned test set: 81. Score used to rank = dev CV coverage - 0.15 x dev CV median abs log error. The test column is shown for information; it was not used to choose weights.

## Round 1: one source at a time

| wA bottom-up | wB use benchmark | wG geometry | k | dev CV coverage % | dev CV median abs log err | test coverage % |
|---|---|---|---|---|---|---|
| 1.0 | 0.0 | 0.0 | 1.10 | 27.1 | 0.394 | 32.1 |
| 0.0 | 1.0 | 0.0 | 1.00 | 33.1 | 0.381 | 27.2 |
| 0.0 | 0.0 | 1.0 | 1.00 | 25.4 | 0.555 | 18.5 |

## Round 2: bottom-up + use benchmark (best 8 of 33)

| wA bottom-up | wB use benchmark | wG geometry | k | dev CV coverage % | dev CV median abs log err | test coverage % |
|---|---|---|---|---|---|---|
| 0.6 | 0.4 | 0.0 | 1.00 | 36.5 | 0.347 | 33.3 |
| 0.6 | 0.4 | 0.0 | 1.10 | 35.9 | 0.316 | 35.8 |
| 0.7 | 0.3 | 0.0 | 1.10 | 35.9 | 0.333 | 35.8 |
| 0.6 | 0.4 | 0.0 | 1.05 | 35.9 | 0.338 | 35.8 |
| 0.5 | 0.5 | 0.0 | 1.00 | 35.4 | 0.328 | 35.8 |
| 0.3 | 0.7 | 0.0 | 1.00 | 35.4 | 0.353 | 35.8 |
| 0.7 | 0.3 | 0.0 | 1.05 | 34.8 | 0.355 | 35.8 |
| 0.5 | 0.5 | 0.0 | 1.05 | 33.7 | 0.326 | 37.0 |

## Round 3: adding the geometry benchmark (best 5)

| wA bottom-up | wB use benchmark | wG geometry | k | dev CV coverage % | dev CV median abs log err | test coverage % |
|---|---|---|---|---|---|---|
| 0.6 | 0.3 | 0.1 | 1.10 | 35.9 | 0.327 | 37.0 |
| 0.5 | 0.4 | 0.1 | 1.05 | 35.9 | 0.345 | 35.8 |
| 0.6 | 0.3 | 0.1 | 1.05 | 35.9 | 0.359 | 35.8 |
| 0.5 | 0.4 | 0.1 | 1.00 | 35.4 | 0.343 | 32.1 |
| 0.5 | 0.3 | 0.2 | 1.05 | 35.4 | 0.375 | 33.3 |

## Chosen for prompt v4

| wA bottom-up | wB use benchmark | wG geometry | k | dev CV coverage % | dev CV median abs log err | test coverage % |
|---|---|---|---|---|---|---|
| 0.5 | 0.5 | 0.0 | 1.00 | 35.4 | 0.328 | 35.8 |

Equal weights on the bottom-up estimate and the use benchmark, no extra factor. Coverage is flat for bottom-up weights between 0.3 and 0.6, so the choice within that range is not critical; the geometry benchmark adds nothing.

## Round 4: richer fits (dev CV)

| Model | dev CV coverage % | dev CV median abs log err |
|---|---|---|
| 0.5 A + 0.5 x ridge benchmark on 11 feature groups | 30.4 | 0.371 |
| A x per-feature correction factors (ridge on the residual) | 26.5 | 0.438 |

Neither beats the plain blend with the use benchmark.
