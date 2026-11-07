# Style and Commits

Part of the [repository guidelines](../AGENTS.md).

## Coding Style & Naming Conventions

Markdown only: ATX headings, `§` for section references, tables for enumerations. Keep revision-memo voice out of the body ("added in this version", "per finding N#"); provenance belongs in Appendix C.

Filenames lie; headers don't — trust `**Version:**`. The full table is in [project-structure.md](project-structure.md#filenames-lie-headers-dont).

## Commit & Pull Request Guidelines

History is terse — `init commit for Neuro-Archatecture`, then `v2`: short subject, no body, no trailers. Work on `master`; there is no remote, so never push. Check `git status` first, since paper edits are usually uncommitted.

There is no pull-request workflow in this repository; changes land as local commits.
