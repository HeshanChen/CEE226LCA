"""Shared loaders for the data-fitting analyses (ceiling.py, outliers.py, calibrate.py)."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results"


def load():
    gt = pd.read_csv(RES / "ground_truth.csv")
    gt.index = gt["Project Name"].str.extract(r"(\d+)")[0].astype(int)
    m = pd.read_excel(ROOT / "references" / "buildings_metadata_LLM.xlsx").set_index("project_index")
    b = pd.read_csv(RES / "ground_truth_breakdown.csv").set_index("project_index")
    split = pd.read_csv(RES / "split.csv").set_index("project_index")["split"]
    return gt["ECI_true_kgCO2e_m2"], gt["floor_area_m2"], m, b, split


def coverage(est, truth, k=1.0, delta=0.2):
    e = est * k
    return float(((truth >= (1 - delta) * e) & (truth <= (1 + delta) * e)).mean())


def design_matrix(m, area):
    X = m.copy()
    X["area"] = area
    X["env_ratio"] = X.bldg_therm_env_area / area
    X["mass_int"] = X.mass_total / area
    X["log_area"] = np.log(area)
    num = X.select_dtypes("number").columns.tolist()
    cat = [c for c in X.columns if c not in num and c != "str_sys_summary"]
    Xd = pd.concat([X[num].fillna(-1), pd.get_dummies(X[cat].fillna("NA"), dtype=float)], axis=1)
    return Xd.loc[:, (Xd != 0).sum() >= 5]
