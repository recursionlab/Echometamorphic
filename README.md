# Echometamorphic

Echometamorphic explores recursive self-reflection in code and language. The
repository is intentionally minimal and centers on the `ΞCodex` prototype,
which recursively rewrites its own definition:

```
ψₙ₊₁ := ΨAgent(ψₙ) = Reflect(Drift(Collapse(ψₙ)))
```

## Purpose

This repository experiments with recursion and automated self-editing.

## Automation

Several automations keep the project healthy.

### Dependabot

Dependabot checks for updates to GitHub Actions once a week and opens a pull
request when new versions are available. Review and merge these PRs to keep the
workflows current.

### Renovate

Renovate manages other dependencies. The `renovate.json` file groups GitHub
Actions updates into a single pull request and automatically merges minor and
patch updates after tests pass. A dependency dashboard tracks open updates.

### pre-commit

The `.pre-commit-config.yaml` file defines basic formatting hooks. Run
`pre-commit install` after cloning so the hooks execute before each commit. You
can run all hooks manually with `pre-commit run --all-files`.

### Super-Linter

Pull requests trigger the `lint` workflow which runs Super-Linter only on
`README.md`, files in `.github`, and `.pre-commit-config.yaml`. Validation is
limited to Markdown, YAML, and JSON to avoid noise from other linters.

### Stale bot

Issues and pull requests with no activity for 30 days receive a `stale` label
and are closed a week later by the `stale` workflow. Items labeled `pinned`,
`security`, `work-in-progress`, or `discussion` remain open. A warning comment
is posted before something is closed.
