# HexahedronMomentDocs

Documentation and reconstruction notes for understanding the Hexahedron Moment
formulation used in the Hermite structural system.

The first target is the ground-zero diagram from `HexahedronMoment.pdf`: an
eight-node isoparametric brick element with local natural axes `xi`, `eta`, and
`zeta`, plus the translational and rotational degrees of freedom shown at node
`P1`.

The goal is not just to reproduce figures. The goal is to turn the original
notation into a readable derivation trail that can be compared against the
working Python implementation.

## Run

```powershell
py -m pip install -r requirements.txt
py tutorial_01_isoparametric_hexahedron.py
```

To save a blog-ready image:

```powershell
py tutorial_01_isoparametric_hexahedron.py --screenshot outputs/isoparametric_hexahedron_ground_zero.png
```

## Current Scope

This is intentionally only the first documentation anchor. It reproduces the
conceptual geometry and labels before carrying over the mathematical
formulation step by step.

## Reference

The `reference/` folder contains the source image used for the first
isoparametric hexahedron reconstruction.
