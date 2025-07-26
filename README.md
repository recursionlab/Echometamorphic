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

Renovate uses its default configuration to manage dependencies. Enable the app
on your fork to start receiving automated dependency updates.

### pre-commit

The `.pre-commit-config.yaml` file defines basic formatting hooks. Run
`pre-commit install` after cloning so the hooks execute before each commit.

### Super-Linter

Pull requests trigger the `lint` workflow which runs Super-Linter to enforce a
consistent code style across the repository.

### Stale bot

Issues and pull requests with no activity for 30 days are marked stale and
closed a week later by the `stale` workflow.
