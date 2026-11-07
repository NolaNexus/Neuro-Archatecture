# Droid Environment

Part of the [repository guidelines](../AGENTS.md). The repository is prose; the only executable code is the hook in `.factory/hooks/`.

## Models (DeepInfra BYOK)

Configured in `~/.factory/settings.json` under `customModels`. Droid registers each entry as `custom:<displayName>-0`, so the IDs below are the ones to use in droid frontmatter and routing.

| Role | Model | ID | Context |
|---|---|---|---|
| Session default | DeepSeek V4.1 Flash | `custom:DeepSeek-V4.1-Flash-(DeepInfra)-0` | 1,048,576 |
| Light subagents | Qwen3 Coder 30B | `custom:Qwen3-Coder-30B-(DeepInfra)-0` | 262,144 |
| Medium subagents | MiniMax M2.1 | `custom:MiniMax-M2.1-(DeepInfra)-0` | 196,608 |
| Heavy subagents | Qwen3.8 Max | `custom:Qwen3.8-Max-(DeepInfra)-0` | 256,000 |

Base URL is `https://api.deepinfra.com/v1/openai`. The key is stored only in the `0600` settings file; `deepinfra_key.json` is gitignored and must not be committed.

Renaming a model's `displayName` changes its registered ID and breaks every reference below. Change both together.

## Droids

Project droids, `.factory/droids/`:

| Droid | Model | Purpose |
|---|---|---|
| `paper-consistency` | light | counts, numbering, section references |
| `paper-reviewer` | medium | prose against the invariants |
| `consultation-grader` | medium | Position / Mechanism / Falsifier |
| `revision-planner` | heavy | Appendix C rows and affected sections |

Personal droids, `~/.factory/droids/`: `deep-analyst` (heavy) and `fast-scout` (light).

## Hook

`.factory/hooks.json` runs `.factory/hooks/check_paper.py` after `Create`, `Edit`, or `ApplyPatch`. The script ignores every file except `paper/green-paper-v*.md`; on the paper it re-runs the count gates and exits `2` with the mismatch, which Droid feeds back as corrective feedback.

## Command

`/verify` runs the gates from `docs/verification.md` and reports the four counts.
