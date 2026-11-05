#!/usr/bin/env python3
"""
hotspot_agreement.py - proposal 6.4 / LEED v5 MRp2: does the LLM name the reference LCA's
top-3 enclosure hotspots?

The answers are prose (no structured hotspot list), so this is a mention-based proxy:
  * reference hotspots: the 3 largest material categories of each building's enclosure A1-A3
    (results/ground_truth_breakdown.csv, groups merged into design-level categories);
  * LLM hotspots: the categories an answer names (keyword match on the answer text).
Because naming many categories inflates recall, every prompt is compared with a constant
"typical-building" guess: the 3 categories that are most often in the reference top 3.

Usage:  python analysis/hotspot_agreement.py <run> [<run> ...]
Writes analysis/hotspot_agreement.md and analysis/hotspot_agreement.csv.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results"

# design-level categories -> breakdown columns
CATS = {
    "Aluminum framing": ["Aluminum"],
    "Glass & windows": ["Glazing", "Windows and frames"],
    "Insulation": ["Insulation"],
    "Concrete": ["Concrete"],
    "Masonry": ["Masonry"],
    "Cladding & panels": ["Cladding", "Wall coverings", "Synthetic composites"],
    "Steel & metals": ["Steel", "Other metals"],
    "Roofing & membranes": ["Roofing and waterproofing", "Air and vapor barriers"],
    "Gypsum": ["Gypsum"],
    "Wood": ["Wood and composites"],
    "Doors": ["Doors and frames"],
}
# keywords an answer uses for each category (lower case, word-boundary regex)
KEYS = {
    "Aluminum framing": r"alumin|curtain[- ]?wall|storefront|window[- ]wall|mullion|extrusion",
    "Glass & windows": r"glaz|glass|\bigu|window|fenestration|curtain[- ]?wall|storefront",
    "Insulation": r"insulat|\bxps\b|polyiso|mineral wool|\beps\b|spray foam|\bspf\b|\bbatt|foam board",
    "Concrete": r"concrete|precast|tilt[- ]up|cast[- ]in[- ]place|\bcip\b",
    "Masonry": r"brick|\bcmu\b|masonry|concrete block|stone veneer",
    "Cladding & panels": r"cladding|metal panel|\bacm\b|\bmcm\b|fib(er|re) cement|siding|terracotta|stucco|\beifs\b|rainscreen|\bimp\b|insulated metal",
    "Steel & metals": r"steel stud|cold[- ]formed|\bcfs\b|steel|stud",
    "Roofing & membranes": r"membrane|\btpo\b|\bepdm\b|roofing|waterproof|bitumen|\bsbs\b|vapou?r barrier|air barrier",
    "Gypsum": r"gypsum|drywall|sheathing",
    "Wood": r"\bwood|timber|\bclt\b|plywood|\bosb\b",
    "Doors": r"\bdoors?\b",
}


def reference_top3() -> pd.DataFrame:
    b = pd.read_csv(RES / "ground_truth_breakdown.csv").set_index("project_index")
    cat = pd.DataFrame({c: b[[f"{g} [kgCO2e/m2]" for g in gs]].sum(axis=1) for c, gs in CATS.items()})
    top = cat.apply(lambda r: [c for c in r.sort_values(ascending=False).index if r[c] > 0][:3], axis=1)
    return pd.DataFrame({"top3": top, "flag_incomplete": b["flag_incomplete"]})


def mentioned(text: str) -> set:
    t = text.lower()
    return {c for c, rx in KEYS.items() if re.search(rx, t)}


def answers(run: str):
    for f in sorted((RES / run / "raw").glob("project-*_run*.md")):
        m = re.match(r"project-(\d+)_run(\d+)\.md", f.name)
        yield int(m.group(1)), int(m.group(2)), f.read_text(encoding="utf-8")


def main(runs):
    ref = reference_top3()
    freq = pd.Series([c for t in ref.top3 for c in t]).value_counts()
    typical = list(freq.index[:3])
    rows = []
    for p, t in ref.top3.items():
        if len(t) == 0:
            continue
        rows.append({"run": "typical-building guess", "project_index": p, "rep": 0,
                     "top1_hit": t[0] in typical, "top3_recall": len(set(t) & set(typical)) / len(t),
                     "n_named": 3, "precision": len(set(t) & set(typical)) / 3})
    for run in runs:
        for p, r, txt in answers(run):
            t = ref.top3.get(p, [])
            if len(t) == 0:
                continue
            m = mentioned(txt)
            rows.append({"run": run, "project_index": p, "rep": r, "top1_hit": t[0] in m,
                         "top3_recall": len(set(t) & m) / len(t), "n_named": len(m),
                         "precision": len(set(t) & m) / len(m) if m else 0.0})
    df = pd.DataFrame(rows)
    df.to_csv(ROOT / "analysis" / "hotspot_agreement.csv", index=False)
    clean = ref.index[~ref.flag_incomplete.astype(bool)]
    out = ["# Hotspot agreement (proposal 6.4, LEED v5 MRp2)", "",
           "Mention-based proxy: an answer 'names' a category when its text matches the category's keywords "
           "(see `KEYS` in `analysis/hotspot_agreement.py`). Reference hotspots are the 3 largest design-level "
           "material categories of each building's enclosure A1-A3. Means over all answers (buildings x runs); "
           "the 10 flagged incomplete references are excluded.", "",
           f"Typical-building guess (most frequent reference top-3): {', '.join(typical)}.", "",
           "Reference top-1 category, share of buildings: " +
           ", ".join(f"{c} {100 * v:.0f}%" for c, v in
                     ref.loc[clean, "top3"].map(lambda t: t[0] if t else None).value_counts(normalize=True).head(5).items()),
           "",
           f"Chance = expected value when the same number of categories is named at random out of {len(CATS)} "
           "(top-1 hit and top-3 recall both equal n_named / n_categories).", "",
           "| Condition | Top-1 named | Top-3 recall | Chance at same count | Categories named per answer | Precision |",
           "|---|---|---|---|---|---|"]
    for run, g in df[df.project_index.isin(clean)].groupby("run", sort=False):
        chance = (g.n_named.clip(upper=len(CATS)) / len(CATS)).mean()
        out.append(f"| {run} | {100 * g.top1_hit.mean():.1f}% | {100 * g.top3_recall.mean():.1f}% | "
                   f"{100 * chance:.1f}% | {g.n_named.mean():.1f} | {100 * g.precision.mean():.1f}% |")
    # buildings whose top-1 is NOT one of the typical categories: the building-specific test
    atyp = [p for p in clean if ref.top3[p] and ref.top3[p][0] not in typical]
    out += ["", f"Building-specific test: the {len(atyp)} buildings whose top-1 category is not in the typical guess "
            "(e.g. concrete, masonry or cladding dominated).", "",
            "| Condition | Top-1 named | Top-3 recall | Chance at same count |", "|---|---|---|---|"]
    for run, g in df[df.project_index.isin(atyp)].groupby("run", sort=False):
        chance = (g.n_named.clip(upper=len(CATS)) / len(CATS)).mean()
        out.append(f"| {run} | {100 * g.top1_hit.mean():.1f}% | {100 * g.top3_recall.mean():.1f}% | {100 * chance:.1f}% |")
    (ROOT / "analysis" / "hotspot_agreement.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1:] or ["20261104_baseline-innate", "20261104_prompt-v2", "20261104_prompt-v3"])
