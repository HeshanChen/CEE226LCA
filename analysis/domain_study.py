#!/usr/bin/env python3
"""
domain_study.py - TA check-in item: envelope-focused documents in context (domain knowledge)
versus the innate baseline, and versus the final prompt.

domain-envelope = prompt v1 + four envelope documents (RDH 2025 wall assemblies, CLF 2023 material
baselines, Arup/Saint-Gobain facades and glass, UBC 2022 fenestration), 30k characters each.
One run; compared paired, building by building, with run 0 of v1 (same chunks and order) and run 0 of v3.
Also checks whether the answers used the documents (mentions) and the XPS blind spot.

Writes analysis/domain_study.md.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from feature_study import RES, estimates, metrics, paired, table  # noqa: E402

RUNS = {"v1 (innate)": "20261104_baseline-innate", "domain-envelope (v1 + documents)": "20261105_domain-envelope",
        "v3 (final prompt)": "20261104_prompt-v3"}
DOC_RX = {"cites a document": r"\bRDH\b|\bCLF\b|baseline report|Arup|Saint[- ]Gobain|UBC|Zargar|the (?:provided|reference) (?:documents?|report|study)",
          "mentions XPS": r"\bXPS\b", "mentions HFC / blowing agent": r"\bHFC|blowing agent"}


def texts(run):
    out = {}
    for f in (RES / run / "raw").glob("project-*_run0.md"):
        out[int(re.match(r"project-(\d+)_", f.name).group(1))] = f.read_text(encoding="utf-8")
    return pd.Series(out)


def main():
    gt = pd.read_csv(RES / "ground_truth.csv")
    truth = pd.Series(gt["ECI_true_kgCO2e_m2"].values, index=gt["Project Name"].str.extract(r"(\d+)")[0].astype(int))
    b = pd.read_csv(RES / "ground_truth_breakdown.csv").set_index("project_index")
    xps = b.index[b["XPS [kgCO2e/m2]"] > 0]
    m = {k: metrics(estimates(v, runs=[0]), truth) for k, v in RUNS.items()}
    rows = [{"condition": k, **{c: v for c, v in mm.items() if not c.startswith("_")}} for k, mm in m.items()]
    out = ["# Domain knowledge: envelope documents in context (run 0, 292 buildings)", "",
           "domain-envelope = prompt v1 + four envelope-focused documents (30k characters each): RDH 2025 spray-foam "
           "wall assemblies, CLF 2023 North American Material Baselines, Arup/Saint-Gobain facades and glass, "
           "UBC 2022 fenestration. Run 0 of every condition uses the same chunks and building order.", "",
           table(rows), ""]
    pr = [{"comparison": "domain-envelope vs v1", **paired(m["v1 (innate)"], m["domain-envelope (v1 + documents)"])},
          {"comparison": "v3 vs domain-envelope", **paired(m["domain-envelope (v1 + documents)"], m["v3 (final prompt)"])}]
    out += ["Paired (Δ = second minus first):", "", table(pr), ""]
    # by subgroup: XPS / no XPS
    sub = []
    for k, v in RUNS.items():
        e = estimates(v, runs=[0])
        r = (e / truth).dropna()
        sub.append({"condition": k, "median ratio, XPS projects": float(r[r.index.isin(xps)].median()),
                    "median ratio, no XPS": float(r[~r.index.isin(xps)].median())})
    out += ["Median estimate/reference by XPS presence:", "", table(sub), ""]
    use = []
    for k, v in RUNS.items():
        t = texts(v)
        use.append({"condition": k, **{lab: 100 * t.str.contains(rx, regex=True).mean() for lab, rx in DOC_RX.items()},
                    "median answer words": float(t.str.split().str.len().median())})
    out += ["Share of answers (%) that cite the documents or name XPS / HFC:", "", table(use), ""]
    (Path(__file__).resolve().parent / "domain_study.md").write_text("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
