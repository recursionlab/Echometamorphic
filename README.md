# Echometamorphic
ψₙ₊₁ := ΨAgent(ψₙ) = Reflect(Drift(Collapse(ψₙ)))

## Development
Install `pre-commit` and the local hooks:

```bash
pip install pre-commit
pip install -e .  # install recursive_complexity_check entry point
pre-commit install
```

Run all checks manually with:

```bash
pre-commit run --all-files
```
