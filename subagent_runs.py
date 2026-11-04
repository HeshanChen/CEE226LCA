#!/usr/bin/env python3
"""
subagent_runs.py - run the LLM estimates with Claude Code subagents instead of the Gemini API.

The prompt (experiment_config.py) is the same for every model. Here a subagent reads a task file
holding the shared context plus a chunk of buildings, answers each building, and writes its
answers to text files. "collect" parses those answers with the same RANGE parser as
gemini_lca_batch.py and writes results/<run-name>/project-#_runs.csv in the same format, so
LLM-data-cleaning.py and make_fig1_bands.py work unchanged.

Steps
  python subagent_runs.py prepare --run-name 20261104_baseline-innate --runs 3
        -> results/<run-name>/subagent/tasks/run-R_chunk-K.md  (one file per subagent)
           results/<run-name>/subagent/manifest.json
  (Claude Code: one subagent per task file, prompted with tasks/run-R_chunk-K.instructions.txt,
   writes subagent/answers/run-R_chunk-K_part-P.md)
  python subagent_runs.py collect --run-name 20261104_baseline-innate
  python LLM-data-cleaning.py 20261104_baseline-innate
  python make_fig1_bands.py 20261104_baseline-innate

Each run (run_idx) shuffles the buildings with its own seed before chunking, so a building
meets different neighbours in every run. Answers in one subagent share a context, unlike
separate API calls; the subagent prompt tells it to answer each building on its own.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
from datetime import datetime
from pathlib import Path

import experiment_config as cfg

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_ROOT = SCRIPT_DIR / "results"

CSV_COLUMNS = [
    "project", "run_idx", "low", "high", "mid", "parse_ok", "failure_type",
    "ontology_mode", "geometry_mode", "finish_reason", "output_tokens", "thought_tokens",
    "cached_tokens", "prompt_tokens", "latency_s", "model", "temperature",
    "thinking_setting", "timestamp", "best",
]
KEY_LINE = re.compile(r"^=====\s*KEY:\s*(project-\d+__run\d+)\s*=====\s*$", re.MULTILINE)

# Same regex as gemini_lca_batch.py. One change in parse_range: a lower bound of 0 is accepted.
# For enclosure-only A1-A3, renovations and tenant fit-outs that leave the envelope untouched
# have a true value near 0 (e.g. 0.49 kgCO2e/m2), so "0 - 5" is a valid answer, not a failure.
_RANGE_RE = re.compile(
    r"RANGE_kgCO2e_per_m2\s*:\s*([0-9][0-9,]*\.?[0-9]*)\s*(?:-|–|—|to)\s*([0-9][0-9,]*\.?[0-9]*)",
    re.IGNORECASE,
)


_BEST_RE = re.compile(r"BEST_kgCO2e_per_m2\s*:\s*([0-9][0-9,]*\.?[0-9]*)", re.IGNORECASE)


def parse_best(text: str):
    """Prompt v2 also asks for a single best estimate (last BEST line). None if absent."""
    matches = _BEST_RE.findall(text.replace("*", "").replace("`", ""))
    try:
        return float(matches[-1].replace(",", "").rstrip(".")) if matches else None
    except ValueError:
        return None


def parse_range(text: str):
    clean = text.replace("*", "").replace("`", "")
    matches = _RANGE_RE.findall(clean)
    if not matches:
        return None, None, "no_range"
    try:
        low, high = (float(x.replace(",", "").rstrip(".")) for x in matches[-1])
    except ValueError:
        return None, None, "no_range"
    if low < 0 or high <= 0 or high < low:
        return low, high, "invalid_range"
    return low, high, ""


def parse_project_selection(spec: str, available: list[int]) -> list[int]:
    if spec == "all":
        return available
    chosen = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            a, b = chunk.split("-")
            chosen.update(range(int(a), int(b) + 1))
        elif chunk:
            chosen.add(int(chunk))
    return sorted(chosen & set(available))


def sub_dir(run_name: str) -> Path:
    return RESULTS_ROOT / run_name / "subagent"


# --------------------------------------------------------------------------------------
# prepare
# --------------------------------------------------------------------------------------
def cmd_prepare(args):
    sd = sub_dir(args.run_name)
    if (sd / "manifest.json").exists() and not args.force:
        raise SystemExit(f"{sd / 'manifest.json'} exists. Use a new --run-name or --force.")
    (sd / "tasks").mkdir(parents=True, exist_ok=True)
    (sd / "answers").mkdir(parents=True, exist_ok=True)

    meta = cfg.load_metadata()
    projects = parse_project_selection(args.projects, [int(x) for x in meta["project_index"]])
    meta = meta.set_index("project_index")
    prefix = "\n\n".join(cfg.build_prefix())

    tasks = []
    for r in range(args.runs):
        order = projects[:]
        random.Random(1000 + r).shuffle(order)
        n_chunks = -(-len(order) // args.chunk_size)
        for k in range(n_chunks):
            chunk = order[k::n_chunks]       # even chunk sizes
            name = f"run-{r}_chunk-{k + 1:02d}"
            blocks = [f"===== KEY: project-{p}__run{r} =====\n"
                      f"{cfg.build_building_prompt(cfg.format_building(meta.loc[p]))}"
                      for p in chunk]
            text = (f"# Task {name}  ({len(chunk)} buildings, condition: {cfg.CONDITION})\n\n"
                    f"## System\n\n{cfg.SYSTEM_PROMPT}\n\n"
                    f"## Shared context (applies to every building below)\n\n{prefix}\n\n"
                    f"## Buildings\n\n" + "\n\n".join(blocks) + "\n")
            path = sd / "tasks" / f"{name}.md"
            path.write_text(text, encoding="utf-8")
            keys = [f"project-{p}__run{r}" for p in chunk]
            instructions = cfg.SUBAGENT_INSTRUCTIONS.format(
                task_file=path, n_lines=text.count("\n"), n_buildings=len(chunk), example_key=keys[0],
                answers_prefix=sd / "answers" / name, answer_length=cfg.ANSWER_LENGTH,
                final_lines=cfg.FINAL_LINES, example_final=cfg.EXAMPLE_FINAL)
            (sd / "tasks" / f"{name}.instructions.txt").write_text(instructions, encoding="utf-8")
            tasks.append({"task": name, "run_idx": r, "file": str(path.relative_to(SCRIPT_DIR)),
                          "keys": keys,
                          "answers_prefix": str((sd / "answers" / name).relative_to(SCRIPT_DIR))})

    manifest = {"run_name": args.run_name, "created": datetime.now().isoformat(timespec="seconds"),
                "model": args.model_label, "effort": args.effort, "runs": args.runs,
                "projects": projects, "settings": cfg.settings(), "tasks": tasks}
    (sd / "manifest.json").write_text(json.dumps(manifest, indent=2, default=str))
    print(f"{len(tasks)} task files ({len(projects)} projects x {args.runs} runs) in {sd / 'tasks'}")


# --------------------------------------------------------------------------------------
# resume: new task files with only the buildings that have no answer yet (e.g. after an
# interrupted subagent). Same prompt; answers go to answers/<task>_resume_part-P.md.
# --------------------------------------------------------------------------------------
def cmd_resume(args):
    sd = sub_dir(args.run_name)
    manifest = json.loads((sd / "manifest.json").read_text())
    if manifest["settings"]["task_text"] != cfg.TASK_TEXT:
        raise SystemExit("experiment_config.py no longer matches this run's prompt; set PROMPT_VERSION back.")
    meta = cfg.load_metadata().set_index("project_index")
    prefix = "\n\n".join(cfg.build_prefix())
    answers = read_answers(sd)
    made = []
    for t in manifest["tasks"]:
        keys = [k for k in t["keys"] if k not in answers]
        if not keys:
            continue
        name = f"{t['task']}_resume"
        blocks = [f"===== KEY: {k} =====\n"
                  f"{cfg.build_building_prompt(cfg.format_building(meta.loc[int(k.split('__')[0].split('-')[1])]))}"
                  for k in keys]
        text = (f"# Task {name}  ({len(keys)} buildings, condition: {cfg.CONDITION})\n\n"
                f"## System\n\n{cfg.SYSTEM_PROMPT}\n\n"
                f"## Shared context (applies to every building below)\n\n{prefix}\n\n"
                f"## Buildings\n\n" + "\n\n".join(blocks) + "\n")
        path = sd / "tasks" / f"{name}.md"
        path.write_text(text, encoding="utf-8")
        instructions = cfg.SUBAGENT_INSTRUCTIONS.format(
            task_file=path, n_lines=text.count("\n"), n_buildings=len(keys), example_key=keys[0],
            answers_prefix=sd / "answers" / name, answer_length=cfg.ANSWER_LENGTH,
            final_lines=cfg.FINAL_LINES, example_final=cfg.EXAMPLE_FINAL)
        (sd / "tasks" / f"{name}.instructions.txt").write_text(instructions, encoding="utf-8")
        made.append({"task": name, "keys": keys, "created": datetime.now().isoformat(timespec="seconds")})
        print(f"{name}: {len(keys)} buildings, {text.count(chr(10)):,} lines")
    manifest.setdefault("resumes", []).extend(made)
    (sd / "manifest.json").write_text(json.dumps(manifest, indent=2, default=str))
    if not made:
        print("Nothing to resume: every key has an answer.")


# --------------------------------------------------------------------------------------
# collect
# --------------------------------------------------------------------------------------
def read_answers(sd: Path) -> dict[str, str]:
    answers = {}
    for f in sorted((sd / "answers").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        hits = list(KEY_LINE.finditer(text))
        for i, m in enumerate(hits):
            end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
            answers[m.group(1)] = text[m.end():end].strip()
    return answers


def cmd_collect(args):
    sd = sub_dir(args.run_name)
    manifest = json.loads((sd / "manifest.json").read_text())
    answers = read_answers(sd)
    expected = [k for t in manifest["tasks"] for k in t["keys"]]
    missing = [k for k in expected if k not in answers]

    out = RESULTS_ROOT / args.run_name
    raw = out / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    by_project: dict[str, list[dict]] = {}
    n_fail = 0
    stamp = datetime.now().isoformat(timespec="seconds")
    for key in expected:
        if key not in answers:
            continue
        name, run = key.split("__run")
        text = answers[key]
        (raw / f"{name}_run{run}.md").write_text(text, encoding="utf-8")
        low, high, ftype = parse_range(text)
        best = parse_best(text)
        ok = ftype == ""
        n_fail += not ok
        by_project.setdefault(name, []).append({
            "project": name, "run_idx": int(run),
            "low": low if low is not None else "", "high": high if high is not None else "",
            "mid": (low + high) / 2 if ok else "", "parse_ok": ok, "failure_type": ftype,
            "ontology_mode": manifest["settings"]["condition"], "geometry_mode": "none",
            "finish_reason": "", "output_tokens": "", "thought_tokens": "", "cached_tokens": "",
            "prompt_tokens": "", "latency_s": "", "model": manifest["model"], "temperature": "",
            "thinking_setting": f"effort={manifest['effort']}", "timestamp": stamp,
            "best": best if (ok and best is not None) else "",
        })
    for name, rows in by_project.items():
        with open(out / f"{name}_runs.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            w.writeheader()
            w.writerows(sorted(rows, key=lambda r: r["run_idx"]))

    print(f"{len(expected) - len(missing)}/{len(expected)} answers found, {n_fail} failed to parse; "
          f"{len(by_project)} project CSVs written to {out}")
    if missing:
        tasks = sorted({t["task"] for t in manifest["tasks"] for k in t["keys"] if k in missing})
        print(f"Missing {len(missing)} answers, from tasks: {', '.join(tasks)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("prepare")
    p.add_argument("--run-name", required=True)
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--projects", default="all")
    p.add_argument("--chunk-size", type=int, default=49, help="max buildings per subagent")
    p.add_argument("--model-label", default="claude-sonnet-5-5 (Claude Code subagent)")
    p.add_argument("--effort", default="medium")
    p.add_argument("--force", action="store_true")
    c = sp.add_parser("collect")
    c.add_argument("--run-name", required=True)
    r = sp.add_parser("resume")
    r.add_argument("--run-name", required=True)
    args = ap.parse_args()
    {"prepare": cmd_prepare, "collect": cmd_collect, "resume": cmd_resume}[args.cmd](args)


if __name__ == "__main__":
    main()
