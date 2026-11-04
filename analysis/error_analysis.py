#!/usr/bin/env python3
"""
error_analysis.py - why the LLM under- or overestimates: diagnostics for one or more runs.

Each diagnostic targets one failure mode found in the baseline (report/report.md, section 5):
compression toward a typical value, HFC-blown XPS, missing envelope area, climate, renovations,
incomplete ground truth, and what the model's reasoning mentions.

Reads:   results/<run>/project-#_runs.csv and raw/*.md, results/ground_truth.csv,
         results/ground_truth_breakdown.csv (GWP-calculation/enclosure_breakdown.py),
         references/buildings_metadata_LLM.xlsx
Writes:  analysis/error_analysis_<run1>[_vs_<run2>].md  (also printed)

Usage:   python analysis/error_analysis.py 20261104_baseline-innate
         python analysis/error_analysis.py 20261104_baseline-innate 20261104_prompt-v2
         python analysis/error_analysis.py --split dev 20261104_baseline-innate   (results/split.csv)
"""

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import summarize_run as sr  # noqa: E402

BREAKDOWN = ROOT / "results" / "ground_truth_breakdown.csv"
METADATA = ROOT / "references" / "buildings_metadata_LLM.xlsx"
COLD = {"Zone 5A", "Zone 5B", "Zone 6A", "Zone 6B", "Zone 7", "Zone 8"}
WARM = {"Zone 1A", "Zone 2A", "Zone 2B", "Zone 3A", "Zone 3B", "Zone 3C"}
TRUTH_BINS = [(0, 25), (25, 50), (50, 100), (100, 200), (200, 10_000)]
MENTIONS = {"XPS": r"\bxps\b|extruded polystyrene", "HFC / blowing agent": r"\bhfc|blowing agent",
            "curtain wall": r"curtain", "envelope area": r"therm_env|envelope area|thermal envelope",
            "mass_total": r"mass_total|total mass"}


SPLIT = ROOT / "results" / "split.csv"   # from analysis/make_split.py


def load(run: str, split: str | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    d = sr.load(sr.RESULTS_ROOT / run)
    if split:
        keep = pd.read_csv(SPLIT).query("split == @split")["project_index"]
        d = d[d["project_index"].isin(keep)]
    b = pd.read_csv(BREAKDOWN).set_index("project_index")
    m = pd.read_excel(METADATA).set_index("project_index")
    d = d.set_index("project_index")
    d["xps"] = b["XPS [kgCO2e/m2]"].reindex(d.index)
    d["has_env"] = m["bldg_therm_env_area"].reindex(d.index).notna()
    texts = []
    for f in (sr.RESULTS_ROOT / run / "raw").glob("project-*_run*.md"):
        texts.append({"project_index": int(re.search(r"project-(\d+)_", f.name).group(1)),
                      "text": f.read_text(encoding="utf-8").lower()})
    t = pd.DataFrame(texts)
    if split and len(t):
        t = t[t["project_index"].isin(d.index)]
    return d, t


def med(s: pd.Series) -> float:
    return float(s.median()) if len(s) else float("nan")


def diagnostics(d: pd.DataFrame, t: pd.DataFrame) -> dict:
    out = {}
    m = sr.metrics(d.reset_index())
    out["Accuracy"] = {"±20% coverage %": m["±20% coverage %"], "RMSE": m["RMSE"],
                       "median APE %": m["median APE %"], "geo-mean est/true": m["geo-mean est/true"],
                       "mean CV across runs %": m["mean CV across runs %"]}
    lt, le = np.log(d["truth"]), np.log(d["estimate"])
    se = ((d["estimate"] - d["truth"]) ** 2).sort_values(ascending=False)
    out["1 Compression"] = {
        "log-log slope est~truth (1 = none)": float(np.polyfit(lt, le, 1)[0]),
        "SD across buildings: estimate / truth": float(d["estimate"].std() / d["truth"].std()),
        "share of squared error from top 20 buildings %": 100 * se.head(20).sum() / se.sum(),
        **{f"median est/true, truth {a}-{b if b < 10_000 else 'max'}":
           med(d.loc[(d["truth"] >= a) & (d["truth"] < b), "ratio"]) for a, b in TRUTH_BINS},
    }
    rest = d["truth"] - d["xps"]
    out["2 HFC-blown XPS"] = {
        "median est/true, projects with XPS": med(d.loc[d["xps"] > 0, "ratio"]),
        "median est/true, projects without XPS": med(d.loc[d["xps"] == 0, "ratio"]),
        "median est/true, XPS > 30% of truth": med(d.loc[d["xps"] > 0.3 * d["truth"], "ratio"]),
        "median est/(truth - XPS)": med(d["estimate"] / rest.where(rest > 0)),
    }
    out["3 Climate"] = {
        "median est/true, cold zones 5-8": med(d.loc[d["climate"].isin(COLD), "ratio"]),
        "median est/true, warm zones 1-3": med(d.loc[d["climate"].isin(WARM), "ratio"]),
        "median est/true, zone 4": med(d.loc[d["climate"].str.startswith("Zone 4"), "ratio"]),
    }
    out["4 Envelope area"] = {
        "median est/true, bldg_therm_env_area given": med(d.loc[d["has_env"], "ratio"]),
        "median est/true, not given": med(d.loc[~d["has_env"], "ratio"]),
    }
    out["5 Project type"] = {f"median est/true, {k}": med(g["ratio"])
                             for k, g in d.groupby("bldg_proj_type")}
    out["6 Incomplete ground truth"] = {
        "median est/true, flagged incomplete (n=%d)" % d["flag_incomplete"].sum(): med(d.loc[d["flag_incomplete"], "ratio"]),
        "±20% coverage %, excluding flagged": 100 * d.loc[~d["flag_incomplete"], "inside"].mean(),
    }
    if len(t):
        out["7 Reasoning text (% of answers mentioning)"] = {
            k: 100 * t["text"].str.contains(p, regex=True).mean() for k, p in MENTIONS.items()}
        xp = t[t["project_index"].isin(d.index[d["xps"] > 0])]
        out["7 Reasoning text (% of answers mentioning)"]["XPS, among projects that have XPS"] = \
            100 * xp["text"].str.contains(MENTIONS["XPS"], regex=True).mean()
    return out


def main(runs: list[str], split: str | None = None):
    res = {r: diagnostics(*load(r, split)) for r in runs}
    tag = f" ({split} split)" if split else ""
    lines = [f"# Error analysis: {' vs '.join(runs)}{tag}", "",
             "Enclosure A1–A3, kgCO2e/m² floor area; estimate = mean of run midpoints. "
             "est/true below 1 = underestimate.", ""]
    for section in res[runs[0]]:
        lines += [f"## {section}", "", "| diagnostic | " + " | ".join(runs) + " |",
                  "|---|" + "---|" * len(runs)]
        for k in res[runs[0]][section]:
            vals = [res[r].get(section, {}).get(k, float("nan")) for r in runs]
            lines.append(f"| {k} | " + " | ".join(f"{v:.2f}" if abs(v) < 10 else f"{v:.1f}"
                                                   for v in vals) + " |")
        lines.append("")
    text = "\n".join(lines)
    out = ROOT / "analysis" / f"error_analysis_{'_vs_'.join(runs)}{'_' + split if split else ''}.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"Saved {out}")


if __name__ == "__main__":
    args = sys.argv[1:]
    split = None
    if args[:1] == ["--split"]:
        split, args = args[1], args[2:]
    if not args:
        raise SystemExit("Usage: python analysis/error_analysis.py [--split dev|test] <run> [<run2> ...]")
    main(args, split)
