#!/usr/bin/env python3
"""PostToolUse guard: re-run the Green Paper count gates after an edit.

Reads the hook payload on stdin, ignores everything except edits to
paper/green-paper-v*.md, and exits 2 with the failure on stderr so Droid
feeds it back as corrective feedback.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER_DIR = (ROOT / "paper").resolve()


def paper_under_edit(data):
    fp = (data.get("tool_input") or {}).get("file_path")
    if not fp:
        return None
    try:
        path = Path(fp).resolve()
    except OSError:
        return None
    if path.parent != PAPER_DIR:
        return None
    if not (path.name.startswith("green-paper-v") and path.suffix == ".md"):
        return None
    return path if path.exists() else None


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    paper = paper_under_edit(data)
    if paper is None:
        return 0

    text = paper.read_text(encoding="utf-8")
    problems = []

    pathologies = len(re.findall(r"^\|\s*9\.\d+\s*\|", text, re.M))
    questions = len(re.findall(r"^\*\*Q[0-9]", text, re.M))
    if pathologies != 13:
        problems.append(f"pathology rows: {pathologies} (expected 13)")
    if questions != 9:
        problems.append(f"questions: {questions} (expected 9)")

    headings = set(re.findall(r"^#{2,3} (\d+(?:\.\d+)?)(?:\.|\s)", text, re.M))
    rows = set(re.findall(r"^\|\s*(9\.\d+)\s*\|", text, re.M))
    refs = set(re.findall(r"§(\d+(?:\.\d+)?)", text))
    unresolved = sorted(refs - headings - rows, key=lambda s: [int(x) for x in s.split(".")])
    if unresolved:
        problems.append("unresolved refs: " + ", ".join("§" + r for r in unresolved))

    if problems:
        print(f"{paper.name}: " + "; ".join(problems), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
