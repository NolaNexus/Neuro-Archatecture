# Repository Guidelines

Prose-only research workspace: a Green Paper proposing a neuro-architectural substrate for a terminal AI development environment, plus the consultation forms and peer reviews around it. No code, build, test suite, linter, CI, or git remote. The only meaningful verification is cross-reference consistency in the markdown.

**Canonical file:** `paper/green-paper-v2.3.md` (644 lines, 14 sections, Appendices A–H). "The green paper" always means this file. The `**Version:**` header is the truth; the filename is renamed to match on each bump.

## Context Budget

This file is the whole guide. There is no `docs/` guide set to chase; do not create one.

- **Never read the paper whole by default.** Map it first with `grep -nE '^#{1,3} ' paper/green-paper-v2.3.md`, then read only the sections you touch plus Appendix C. A full read is for a structural rewrite, and you say why before doing it.
- **Never re-read a file already read this session.** Use `offset`/`limit` or `grep -n` for a second look.
- **Locate with grep, then read narrow.** Do not open a 220-line review to answer one question; read the row or paragraph you need.
- **Subagents get ranges, not the paper.** Pass section numbers or the exact grep. A subagent told to "read the paper" burns the context you were saving.
- **Never paste long file contents** into replies, subagent prompts, or commit messages. Pass paths and line ranges.
- **Historical files are input only.** `paper/archive/`, `forms/consultation-response-form-edition-2.md`, `forms/consultation-response-form-edition-3.md`, and the v1.2 reviews load only when a task names them. The current form is Edition 4.
- **Subagents return verdicts, not passages.** Ask for the finding, the line number, and the minimal correction. A subagent that quotes the paper back to you has doubled your context, not halved it.
- **One revision per session.** After a version bump, start a fresh session; the old one only carries stale text.
- **Compact when the transcript costs more than it carries.** `/context` shows the split; `/compress` summarizes into a fresh session. The 120k limit is the automatic floor, not a target.

## Layout

```
paper/     the Green Paper, current and archived
forms/     consultation response forms
reviews/   completed peer reviews and audits
```

## Files

- `paper/green-paper-v2.3.md` — the canonical paper. The version is in the header; the filename is renamed to match on each bump.
- `paper/archive/green-paper-v1.2.md` — superseded edition; input only.
- `forms/consultation-response-form-edition-4.md` — current template, grades v2.3. Copy it into `reviews/`; never edit it in place.
- `forms/consultation-response-form-edition-3.md` — historical; grades v2.2 and asserts the v2.2 state in A5.
- `forms/consultation-response-form-edition-2.md` — historical.
- `reviews/` — completed reviews and audits from the prior three rounds.

## Naming

Filenames carry the paper version, the reviewer, and the document kind, in that order, lowercase and hyphenated: `v1.2-lumo-peer-audit.md`. The paper follows `green-paper-v<version>.md` in both `paper/` and `paper/archive/`. Trust the header when the two disagree, and fix the filename rather than recording the mismatch.

## Review and Form Index

Read a section, not the file: open with `offset` and `limit` at the line shown.

| File | Lines | Sections |
|---|---|---|
| `reviews/v1.2-lumo-consultation-response-edition-2.md` | 176 | A 9 · B 29 · C 57 (Q1–Q14) · D 147 · E 167 |
| `reviews/v1.2-lumo-consultation-response-freeform.md` | 220 | A 10 · B 23 · C 45 (Q1–Q12) · D 196 · E 212 |
| `reviews/v1.2-lumo-peer-audit.md` | 139 | verdict 9 · D1–D7 15 · F1–F7 42 · neuroscience 67 · P1–P2 88 · laws 99 · questions 111 · form audit 119 |
| `reviews/v1.4-lumo-peer-review.md` | 101 | A 9 (N1–N6 23) · B 45 (M1–M8 51) · C 79 · D 99 |
| `reviews/v2.2-lumo-peer-review-round-3.md` | 148 | verdict 12 · R1–R5 35 · R6–R13 79 · R14–R19 115 · phase plan 126 |
| `reviews/v2.3-deepinfra-route-registry.md` | 94 | route change 8 · criteria 12 · cost model 31 · registry 39 · unfunded tier 62 · falsifiers 74 · constitution 85 |
| `forms/consultation-response-form-edition-4.md` | 173 | A 11 (A5 split 25) · B 51 · C 86 (Q1–Q9 96–142) · D 149 · E 165 |
| `forms/consultation-response-form-edition-3.md` | 150 | A 10 · B 36 · C 69 (Q1–Q9 77–123) · D 130 · E 142 |
| `forms/consultation-response-form-edition-2.md` | 165 | A 9 · B 31 · C 63 · D 148 · E 158 |

## Architecture Overview

Five laws (Metabolism, Sparse Activation, Decorrelated Errors, Earned Existence, Substrate Silence) elaborate into eight divisions, a cerebrum of four stages with two witnesses each (eight roles), the Ledger/Chronicle signal split, an endocrine tier, a bandit-trained macro router, and a dispute interrupt that binds on mechanical fields. §9 inventories thirteen pathologies; §13 pins nine inherited lesions as the golden set.

## Invariants

Break one and the document silently stops being the same document.

### Numbering

Pathologies are 9.1–9.13 inside §9; §10 is "Plasticity: The Myelination Ladder." v1.2's error was 10.x inside §9 — don't reintroduce it.

### Questions

v2.3 has Q1–Q9 in §14; the Edition 4 form asks the same, with Q1, Q3, and Q8 reworded where v2.3 changed their inputs. §14's preamble says which old questions are now settled in text — use it instead of inventing answers.

### Finding IDs

`D#`/`F#`/`P#` come from the v1.2 audit, `N#`/`M#`/`E#` from the v1.4 review, and `R#` from the v2.2 round-3 review. All are dispositioned in Appendix C and appear only in the appendices, never in body sections §1–§14.

### Terminology

Terminology is specification: don't rename the organs, the eight roles (Driver, Sentinel, Spotlight, Cartographer, Chronicle, Canon, Reader, Surveyor), the five Laws, or the Ledger/Chronicle split, and don't swap their mandated behaviors. The Cerebrum thinks; the Thalamus gates without judging; the locus-coeruleus reflex binds only on mechanical fields, with learned salience advisory.

### Pinned Values

Appendix A constants and §13's nine-lesion golden set are pinned per epoch. Appendix D is a living registry — keep its verified vs. "to be measured at Epoch 0" distinction. Appendix E is living too — keep its Faithful / Approximate / Missing (provisional) verdict distinction. Appendix F is the census protocol, Appendix G the fixture specification, and Appendix H the falsifier register: a falsifier is powered only with a statistic, data source, decision rule, and power target.

### Biological Deviations

Deviations belong in Appendix B. Substrate gaps found in OpenCode go there as well (B11–B20); don't paper over them in body text.

## Verification

The only meaningful verification is cross-reference consistency; don't hunt for a test suite. Four greps against the canonical paper:

```sh
P="paper/green-paper-v2.3.md"
grep -nE '^#{2,3} ' "$P"                     # section map (## and ###); §9.x are table rows
grep -c '^| 9\.' "$P"                        # pathologies: 13
grep -c '^\*\*Q[0-9]' "$P"                   # questions: 9
grep -oE '§[0-9]+(\.[0-9]+)?' "$P" | sort -u # every ref must be in the map or a 9.x row
```

Counts must agree across the Abstract, §4, §5.3, §9, and §14: eight divisions, eight roles, thirteen pathologies, nine questions.

The Edition 4 form's A5 checklist is split in two. The carry-over half asserts the v2.2 state v2.3 preserves (9.1–9.13 numbering, Q1–Q9, the §5.2 ninth-and-tenth fix, Appendix A constants, §5.4 comprehension lenses, the N→V rename, §8/Q3 agreement, Appendix E plus B11–B20); the v2.3 half asserts the new state (Law 5 by provenance, the three §5.2 tests, error-conditional disagreement and kappa, the pipeline default, the bandwidth axis, version-pinned fixtures with Appendices G–H, B17–B20, and D's installed-versus-watchlist split). Every line should be **Confirmed**; a **Confirmed** on a defect-shaped item means the copy predates the cleanup, and an **Absent** on a v2.3 item means the copy is Edition 3 or older.

The same gates run automatically after any edit to `paper/green-paper-v*.md` through `.factory/hooks.json`, and `/verify` runs them on demand.

## Workflow

### Consultation Responses

Copy `forms/consultation-response-form-edition-4.md` into `reviews/` and state the paper version in the header. Every response needs a definite **Position**, a **Mechanism** (*how*), and a **Falsifier** that could kill the proposal. No hedges; "no position" is stated explicitly.

### Revising the Paper

- Bump the `**Version:**` header (v2.3 → v2.4 …), rename the file to match (`git mv paper/green-paper-v2.3.md paper/green-paper-v2.4.md`), and update the paths here in `AGENTS.md`. Add an Appendix C row; no finding is silently dropped.
- Registry or lane-economy changes: update Appendix D and the affected §5.7 / Q8–Q9 text together.
- Substrate-mapping changes: update Appendix E and the affected Appendix B rows (B11–B20) together.

## Style and Commits

Markdown only: ATX headings, `§` for section references, tables for enumerations. Keep revision-memo voice out of the body ("added in this version", "per finding N#"); provenance belongs in Appendix C. Filenames lie; headers don't.

History is terse — `init commit for Neuro-Archatecture`, then `v2`: short subject, no body, no trailers. Work on `master`; there is no remote, so never push. Check `git status` first, since paper edits are usually uncommitted. There is no pull-request workflow; changes land as local commits.

## Droid Environment

The repository is prose; the only executable code is the hook in `.factory/hooks/`.

### Models (DeepInfra BYOK)

Configured in `~/.factory/settings.json` under `customModels`. Droid registers each entry as `custom:<displayName>-0`, so the IDs below are the ones to use in droid frontmatter and routing.

| Role | Model | ID | Context |
|---|---|---|---|
| Session default | DeepSeek V4.1 Flash | `custom:DeepSeek-V4.1-Flash-(DeepInfra)-0` | 1,048,576 |
| Light subagents | Qwen3 Coder 30B | `custom:Qwen3-Coder-30B-(DeepInfra)-0` | 262,144 |
| Medium subagents | MiniMax M2.1 | `custom:MiniMax-M2.1-(DeepInfra)-0` | 196,608 |
| Heavy subagents | Qwen3.8 Max | `custom:Qwen3.8-Max-(DeepInfra)-0` | 256,000 |

Base URL is `https://api.deepinfra.com/v1/openai`. The key lives only in the `0600` settings file and a `0600` local copy at `~/.factory/deepinfra_key.json`; neither is in the repository, and neither is ever committed.

Renaming a model's `displayName` changes its registered ID and breaks every reference below. Change both together.

### Droids

Project droids, `.factory/droids/`:

| Droid | Model | Purpose |
|---|---|---|
| `paper-consistency` | light | counts, numbering, section references |
| `paper-reviewer` | medium | prose against the invariants |
| `consultation-grader` | medium | Position / Mechanism / Falsifier |
| `revision-planner` | heavy | Appendix C rows and affected sections |

Personal droids, `~/.factory/droids/`: `deep-analyst` (heavy) and `fast-scout` (light).

`~/.factory/droids/` also holds five ML droids used by the `~/LMp2LMa` journey workspace: `ml-experimenter`, `ml-evaluator`, `data-auditor`, `notebook-engineer`, and `ml-code-reviewer`. Their shared skills live in `~/.factory/skills/`: `pytorch-training`, `mlflow-tracking`, `sklearn-pipelines`, `data-validation`, `jupyter-notebook`, and `anaconda-intelligence`. The ML workspace's `AGENTS.md` documents when to use them; they are not part of paper work.

### Hooks

`.factory/hooks.json` runs two guards:

- `guard_paper_read.py` before `Read`: an un-ranged read of `paper/green-paper-v*.md` exits `2` and returns the map-first instruction. A read with `offset`, or with `limit` ≥ 400, passes; that is the opt-in for a structural rewrite.
- `check_paper.py` after `Create`, `Edit`, or `ApplyPatch`: on the paper it re-runs the count gates and exits `2` with the mismatch.

Droid snapshots hooks at startup, so a new hook takes effect in the next session.

### Compaction

`.factory/settings.json` sets `compactionTokenLimit` to 120,000. BYOK models default to 250,000 even with a million-token window, which lets a session run well past the point where re-sending the transcript costs more than the detail is worth. `/context` shows the breakdown, `/compress [prompt]` summarizes now and continues in a new session, and `/clear` discards. Raise the limit if a revision legitimately needs more working text.

### Command

`/verify` runs the gates above and reports the four counts.
