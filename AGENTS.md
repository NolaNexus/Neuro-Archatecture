# Repository Guidelines

Prose-only research workspace: a Green Paper on a neuro-architectural substrate for a terminal AI development environment, with its consultation forms and peer reviews. No code, build, or CI; verification is cross-reference consistency in the markdown.

**Canonical file:** `paper/green-paper-v2.3.md` (646 lines, 14 sections, Appendices A–H). The `**Version:**` header is the truth; filenames are renamed to match.

**Full rules:** `.factory/agents-detail.md`, read before any paper edit or review.

## Project Structure & Module Organization

```
paper/     the Green Paper, current and archived
forms/     consultation response forms
reviews/   completed peer reviews and audits
```

Edition 4 is current; copy it into `reviews/`, never edit in place. Historical files load only when named.

## Build, Test, and Development Commands

No build. Four greps are the suite:

```sh
P="paper/green-paper-v2.3.md"
grep -nE '^#{2,3} ' "$P"                     # section map
grep -c '^| 9\.' "$P"                        # pathologies: 13
grep -c '^\*\*Q[0-9]' "$P"                   # questions: 9
grep -oE '§[0-9]+(\.[0-9]+)?' "$P" | sort -u # every ref must resolve
```

Counts agree across Abstract, §4, §5.3, §9, §14. `/verify` runs the gates on demand.

## Coding Style & Naming Conventions

Markdown only: ATX headings, `§` for section references, tables for enumerations. Filenames carry version, reviewer, and kind, lowercase and hyphenated (`v1.2-lumo-peer-audit.md`). Trust the header over the filename.

## Testing Guidelines

No framework. A red gate means the document stopped being the same document.

## Commit & Pull Request Guidelines

Terse history: `init commit for Neuro-Archatecture`, then short subjects, no body, no trailers. Work on `master`, which tracks `origin` at `git@github.com:NolaNexus/Neuro-Archatecture.git` (public); push only when asked, and never rewrite published history. No pull-request workflow.

## Invariants

Break one and the document silently stops being the same document.

- Pathologies are 9.1–9.13 inside §9; §10 is "Plasticity: The Myelination Ladder."
- Q1–Q9 live in §14; the Edition 4 form asks the same.
- Finding IDs (`D#`/`F#`/`P#`, `N#`/`M#`/`E#`, `R#`) appear only in appendices.
- Don't rename the organs, eight roles, five Laws, or the Ledger/Chronicle split.
- Deviations belong in Appendix B, substrate gaps included (B11–B20).

## Architecture Overview

Five laws elaborate into eight divisions, a cerebrum of four stages with two witnesses each, the Ledger/Chronicle split, an endocrine tier, and a bandit-trained router.

## Agent-Specific Instructions

- Never read the paper whole; map it first, then read only the sections you touch.
- Subagents get line ranges and return verdicts, not passages.
- One revision per session; compaction limit 120,000.
- Model routes, droids, and hooks are in `.factory/agents-detail.md`.
