# Cognitive Forge — HermiteStructural Research Notes

This website documents the **current higher-order HermiteStructural research benchmark**, not deprecated first-degree Hex8 demonstrations or superseded solver sources.

## Start here

- [Tutorial 001 — higher-order Hermite cantilever and orthotropic verification](_posts/2026-05-10-hermite-beam-theoretical-check.md)
- [Active HermiteStructural implementation and README](https://github.com/cognitiveforge630/HermiteStructural)
- [Chronological PowerShell reproduction instructions](https://github.com/cognitiveforge630/HermiteStructural/blob/main/docs/RUN_COMMANDS_IN_ORDER.md)

## Reproduce the reported result

In Windows PowerShell:

```powershell
git clone https://github.com/cognitiveforge630/HermiteStructural.git
cd .\HermiteStructural
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python .\run_higher_order_hermite.py --nx 4 --ny 5 --nz 17
Get-Content .\hermite_result.json
```

The reported current research run yields a **0.483063%** difference in tip displacement versus its stated AWC-style beam reference. This is not an a posteriori error certificate. The mesh has eight-node hexahedral *connectivity* but the displacement formulation uses **nonlocal higher-order rotation recovery**, and must not be called a plain first-degree Hex8 element. The next milestone is mathematically justified a posteriori certification.

**Do not use historical source snippets or first-order tutorial programs from old snapshots as reproduction instructions for this result.** Git history keeps the old material accessible without displaying it as active documentation.
