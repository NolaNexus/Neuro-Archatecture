#!/usr/bin/env python3
"""PreToolUse guard: refuse whole-file reads of the canonical paper.

Reads the hook payload on stdin. Blocks (exit 2) a Read of
paper/green-paper-v*.md that supplies neither offset nor limit, and tells
the agent to map sections first. An explicit limit at or above
FULL_READ_MIN is treated as a deliberate full read, so a structural
rewrite can still opt in.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER_DIR = (ROOT / "paper").resolve()
FULL_READ_MIN = 400


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    if data.get("tool_name") != "Read":
        return 0

    tool_input = data.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    if not file_path:
        return 0

    try:
        path = Path(file_path).resolve()
    except OSError:
        return 0

    if path.parent != PAPER_DIR:
        return 0
    if not (path.name.startswith("green-paper-v") and path.suffix == ".md"):
        return 0

    limit = tool_input.get("limit")
    if tool_input.get("offset") is not None:
        return 0
    if isinstance(limit, int) and limit >= FULL_READ_MIN:
        return 0

    lines = len(path.read_text(encoding="utf-8").splitlines())
    rel = path.relative_to(ROOT)
    print(
        f"Blocked: whole-file read of {path.name} ({lines} lines). "
        f"Map it first with `grep -nE '^#{{1,3}} ' {rel}`, then Read with offset and limit "
        "(for example §9 at offset=232, limit=24). "
        f"For a deliberate structural rewrite, pass limit={lines}.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
