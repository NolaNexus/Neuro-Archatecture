# Verification

Part of the [repository guidelines](../AGENTS.md). The only meaningful verification is cross-reference consistency in the markdown; don't hunt for a test suite.

## Build, Test, and Development Commands

No build step exists. Verification is four greps against the canonical paper:

```sh
P="paper/green-paper-v2.2.md"
grep -nE '^#{2,3} ' "$P"                     # section map (## and ###); §9.x are table rows
grep -c '^| 9\.' "$P"                        # pathologies: 13
grep -c '^\*\*Q[0-9]' "$P"                   # questions: 9
grep -oE '§[0-9]+(\.[0-9]+)?' "$P" | sort -u # every ref must be in the map or a 9.x row
```

Counts must agree across the Abstract, §4, §5.3, §9, and §14: eight divisions, eight roles, thirteen pathologies, nine questions.

## Testing Guidelines

The greps above are the suite. The Edition 3 form's A5 checklist asserts the same v2.2 state (9.1–9.13 numbering, Q1–Q9, the §5.2 ninth-and-tenth fix, Appendix A constants, §5.4 comprehension lenses, the N→V rename, §8/Q3 agreement, Appendix E plus B11–B16). All eight should be **Confirmed**; a **Confirmed** on a defect-shaped item means the copy predates the cleanup.

The same gates run automatically after any edit to `paper/green-paper-v*.md` through `.factory/hooks.json`, and `/verify` runs them on demand. See [droid-environment.md](droid-environment.md).
