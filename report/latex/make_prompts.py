"""Export the exact prompts from experiment_config.py to report/latex/prompts/*.txt for the paper.
Six non-ASCII characters are written as ASCII (pdflatex listings): subscript 2 -> 2, curly quotes
-> straight quotes, en dash -> -, 2/3 fraction -> 2/3."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import experiment_config as cfg  # noqa: E402

OUT = Path(__file__).resolve().parent / "prompts"
ASCII = {"₂": "2", "’": "'", "‘": "'", "“": '"', "”": '"', "⅔": "2/3", "–": "-", "—": "-"}


def clean(t):
    for a, b in ASCII.items():
        t = t.replace(a, b)
    assert all(ord(c) < 128 for c in t), [c for c in t if ord(c) >= 128]
    return t


def main():
    OUT.mkdir(exist_ok=True)
    # shared context without the task text (v4 writes the task once per file, after the glossary)
    parts = [p for p in cfg.build_prefix() if not p.startswith("## Task")]
    files = {"system.txt": cfg.SYSTEM_PROMPT, "shared_context.txt": "\n\n".join(parts),
             "task_v1.txt": cfg.TASK_TEXT_V1, "task_v2.txt": cfg.TASK_TEXT_V2, "task_v3.txt": cfg.TASK_TEXTS["v3"],
             "task_v4.txt": cfg.TASK_TEXTS["v4"],
             "task_v5.txt": cfg.TASK_TEXTS["v5"], "task_wb5.txt": cfg.TASK_TEXTS["wb5"], "task_wb6.txt": cfg.TASK_TEXTS["wb6"],
             "subagent_instructions.txt": cfg.SUBAGENT_INSTRUCTIONS}
    meta = cfg.load_metadata().set_index("project_index")
    files["building_225.txt"] = cfg.format_building(meta.loc[225])
    for name, text in files.items():
        (OUT / name).write_text(clean(text) + "\n", encoding="ascii")
    print("wrote", sorted(files))


if __name__ == "__main__":
    main()
