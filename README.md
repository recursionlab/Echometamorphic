# Echometamorphic

Echometamorphic explores recursive self-reflection in code and language. The
repository is intentionally minimal and centers on the `ΞCodex` prototype:

```
ψₙ₊₁ := ΨAgent(ψₙ) = Reflect(Drift(Collapse(ψₙ)))
```

## Automation

Several automations keep the project healthy.

### Dependabot

Dependabot checks for updates to GitHub Actions once a week and opens pull
requests when new versions are available.

### Renovate

Renovate opens pull requests for dependency updates and provides a dependency
dashboard. GitHub Actions updates are grouped together under one pull request.

### pre-commit

The `.pre-commit-config.yaml` file defines basic formatting hooks. Run
`pre-commit install` after cloning so the hooks execute before each commit.

### Super-Linter

Pull requests trigger the `lint` workflow which runs Super-Linter on Markdown,
YAML, and JSON files to enforce a consistent style.

### Stale bot

Issues and pull requests with no activity for 30 days receive a `stale` label
and are closed a week later by the `stale` workflow. Items labeled `pinned`,
`security`, or `work-in-progress` are exempt.
