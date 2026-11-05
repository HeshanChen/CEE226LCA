#!/usr/bin/env python3
"""Figure variants for the weekly updates: each week shows only the prompt versions presented so far."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import make_figures as mf  # noqa: E402

mf.OUT = HERE / "figures"
mf.OUT.mkdir(exist_ok=True)
d, b, m, split = mf.load()
orig_save = mf.save
for keys in (["v1"], ["v1", "v2"]):
    tag = "_".join(keys)
    mf.save = lambda fig, name, tag=tag: orig_save(fig, f"{name}_{tag}")
    sub = {k: d[k] for k in keys}
    mf.fig_bins(sub)
    mf.fig_diagnostics(sub, b, m)
mf.save = orig_save
print("saved to", mf.OUT)
