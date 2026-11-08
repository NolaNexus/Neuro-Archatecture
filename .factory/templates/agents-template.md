<!--
Generic contributor-guide template. Copy to AGENTS.md and replace every {{PLACEHOLDER}}.
Delete optional blocks you do not use; keep the file to 200-400 words of prose.
Guidance for the writer lives in these comments and is not part of the guide.
-->

# Repository Guidelines

{{ONE_SENTENCE: what this repository is, and what it is not. Name the artifact, not the tooling.}}

**Canonical file:** `{{PATH}}` ({{LINE_COUNT}} lines). Its `{{VERSION_HEADER}}` header is the truth; filenames are renamed to match on each bump.

## Project Structure & Module Organization

```
{{DIR_TREE}}
```

- `{{PATH}}` — {{PURPOSE}}
- `{{PATH}}` — {{PURPOSE}}

<!-- OPTIONAL: keep only when a file index actually saves context. Read a section, not the file.
## File Index

| File | Lines | Sections |
|---|---|---|
| `{{PATH}}` | {{N}} | {{SECTION}} {{LINE}} · {{SECTION}} {{LINE}} |
-->

## Build, Test, and Development Commands

```sh
{{BUILD_CMD}}    # {{WHAT_IT_DOES}}
{{TEST_CMD}}     # {{WHAT_IT_DOES}}
{{LINT_CMD}}     # {{WHAT_IT_DOES}}
```

{{WHAT_PASSING_MEANS — the one check that matters most, and what a failure indicates.}}

## Coding Style & Naming Conventions

- {{INDENTATION_AND_FORMATTING}}
- Filenames: {{NAMING_PATTERN}}
- {{LINTER_OR_FORMATTER}}, configured at `{{CONFIG_PATH}}`.

<!-- OPTIONAL: invariants are rules whose violation changes the artifact's identity without an error.
## Invariants

Break one and the document silently stops being the same document.

- **{{INVARIANT}}** — {{WHAT_BREAKS_IF_VIOLATED}}
-->

<!-- OPTIONAL
## Architecture Overview

{{TWO_OR_THREE_SENTENCES: the parts, how they connect, and which one is load-bearing.}}
-->

## Testing Guidelines

- Framework: {{FRAMEWORK}}
- Test naming: `{{TEST_NAMING_PATTERN}}`
- Run with `{{TEST_CMD}}`; {{COVERAGE_RULE}}
- {{WHAT_MUST_BE_COVERED_BEFORE_MERGE}}

<!-- OPTIONAL: repeatable procedures that must be followed exactly, not rediscovered each time.
## Common Workflows

### {{WORKFLOW_NAME}}

{{STEPS in order, naming the files each step touches and the check that ends it.}}
-->

## Commit & Pull Request Guidelines

- Commit style: {{CONVENTION}}, e.g. `{{EXAMPLE_MESSAGE}}`.
- Trailers: {{TRAILER_RULE}}
- Pull requests: {{PR_REQUIREMENTS — description, linked issue, screenshots, review gate.}}

<!-- OPTIONAL
## Security & Configuration Tips

- Secrets live in `{{SECRET_LOCATION}}` and are never committed.
- {{CONFIG_CAVEAT}}
-->

<!-- OPTIONAL: agent-specific behavior belongs here, not in the sections above.
## Agent-Specific Instructions

### Context Budget

- Never read `{{CANONICAL_FILE}}` whole by default. Map it first with `{{MAP_CMD}}`, then read only the sections you touch.
- Never re-read a file already read in the session.
- Subagents receive line ranges, not whole documents, and return verdicts, not passages.
- {{COMPACTION_POLICY}}
-->
