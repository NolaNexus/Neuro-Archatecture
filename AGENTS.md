# Repository Guidelines

Prose-only research workspace: a Green Paper proposing a neuro-architectural substrate for a terminal AI development environment, plus the consultation forms and peer reviews around it. No code, build, test suite, linter, CI, or git remote. The only meaningful verification is cross-reference consistency in the markdown.

**Canonical file:** `paper/green-paper-v2.2.md` (526 lines, 14 sections, Appendices A–E). "The green paper" always means this file. The `**Version:**` header is the truth; the filename is renamed to match on each bump. Read it whole before editing.

## Guide Index

| Document | Covers | Read before |
|---|---|---|
| [docs/project-structure.md](docs/project-structure.md) | file inventory, filenames-lie table, architecture overview | orienting yourself |
| [docs/verification.md](docs/verification.md) | verification greps, count gates, A5 checklist | claiming work is done |
| [docs/style-and-commits.md](docs/style-and-commits.md) | markdown conventions, naming, commit style | writing or committing |
| [docs/invariants.md](docs/invariants.md) | numbering, questions, finding IDs, terminology, pinned values | editing the paper |
| [docs/workflow.md](docs/workflow.md) | consultation responses, version bumps, registry updates | revising or responding |
| [docs/droid-environment.md](docs/droid-environment.md) | DeepInfra models, droid routing, hook, /verify | using subagents |

## Before You Edit

Four rules that break the document if missed; `docs/invariants.md` has the full set.

- Pathologies are 9.1–9.13 inside §9; §10 is "Plasticity: The Myelination Ladder." Never 10.x inside §9.
- Don't rename the organs, the eight roles, the five Laws, or the Ledger/Chronicle split.
- Finding IDs (`D#`/`F#`/`P#`, `N#`/`M#`/`E#`) belong in the appendices only, never in §1–§14.
- Keep revision-memo voice out of the body; provenance goes in Appendix C.
