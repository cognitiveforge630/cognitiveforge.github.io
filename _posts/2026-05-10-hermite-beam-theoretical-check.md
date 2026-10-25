---
layout: post
title: "HermiteStructural: Higher-Order Hermite Cantilever and Orthotropic Matrix Verification"
description: "October 2026 progress report on the higher-order Hermite cantilever, prescribed material properties, and orthotropic compliance and stiffness matrix verification."
tags: [Finite Element Analysis, Python, Hermite, Orthotropic Material, Verification]
comments: true
math: true
---

# HermiteStructural: Higher-Order Hermite Cantilever and Orthotropic Matrix Verification

*Technical progress update — October 24, 2026*

[HermiteStructural source repository](https://github.com/cognitiveforge630/HermiteStructural)

HermiteStructural develops and verifies finite-element methods based on Hermite interpolation and rotational enrichment. The current demonstration emphasizes **higher-order Hermite bending behavior**, physically prescribed orthotropic material parameters, and independent numerical comparisons.

This article replaces the previous cantilever walkthrough. It describes the current research benchmark, not an earlier implementation or its solver outputs.

## Current Higher-Order Hermite Cantilever

The active research demonstration uses a Hex8-based Hermite formulation with a **nonlocal quadratic rotation-recovery stencil**. The geometry has eight-node hexahedral connectivity, but the enriched formulation **must not be described as an ordinary first-degree/trilinear Hex8 displacement element**: its recovery uses higher-order information from neighboring nodes.

The example combines an integrated end-face transverse traction with volume-integrated self-weight, then compares the calculated tip displacement against an AWC-style Euler–Bernoulli reference that accounts for both loads.

The reported Windows run on October 24, 2026 used:

| Item | Reported value |
| --- | ---: |
| Formulation | Quadratic-rotation Hermite / higher-order recovery |
| Node mesh | 4 × 5 × 17 |
| Total applied global-y force, including self-weight | −79.616000 lbf |
| Calculated tip displacement, $u_y$ | −0.064190591 in |
| Beam-theory reference | −0.063882000 in |
| Absolute relative displacement difference | **0.483063%** |
| Comparison against a 1% displacement target | **Pass** |

This is a useful **independent benchmark agreement**, not a manufactured exact solution, a proof of mesh convergence, or a rigorous a posteriori error certificate. A small difference against beam theory does not by itself bound the three-dimensional FEM discretization error, local stresses, or general performance on other meshes and loading cases.

To reproduce the reported higher-order benchmark from the repository root on Windows:

```powershell
python .\run_higher_order_hermite.py --nx 4 --ny 5 --nz 17
```

The benchmark writes `hermite_result.json` with its formulation, mesh, resultant force, comparison values, and certification status. For any release assessment, consult the current repository and freshly generated output rather than treating the table above as a universal result.

## Prescribed Material Properties, Not Modulus Fitting

The elastic constants are **material inputs**, not adjustable factors chosen to force a target displacement. In a predictive finite-element workflow, the specified longitudinal modulus and other orthotropic constants define the constitutive model before the beam is solved.

The procedure is therefore:

1. Specify material orientation, elastic constants, geometry, loading, and boundary conditions.
2. Assemble and solve the chosen Hermite finite-element formulation.
3. Compare the independently predicted response with a reference and report the actual discrepancy.

Agreement should come from the element formulation, integration, physical assumptions, boundary treatment, and numerical resolution—not from retuning stiffness until a desired answer appears.

## Orthotropic Matrix Comparison

A separate, reproducible [orthotropic matrix companion](https://github.com/cognitiveforge630/HermiteStructural/tree/main/orthotropic_companion) compares two algebraic representations of the **same orthotropic linear-elastic constitutive law**:

- a full reciprocal-Poisson-pair compliance matrix, labeled *eFunda-style* in the comparison;
- the compact symmetric compliance-matrix construction used by HermiteStructural.

The comparison uses material axes **radial $R\to x$**, **tangential $T\to y$**, and **longitudinal $L\to z$**. The component order is `xx, yy, zz, xy, yz, xz`, with **engineering shear strains** (so the shear compliance terms are $1/G$).

The constitutive relationship is

$$
\boldsymbol{\varepsilon}=\mathbf S\boldsymbol{\sigma},
\qquad
\boldsymbol{\sigma}=\mathbf D\boldsymbol{\varepsilon},
\qquad
\mathbf D=\mathbf S^{-1}.
$$

Reciprocal Poisson ratios satisfy, for example,

$$
\frac{\nu_{xy}}{E_x}=\frac{\nu_{yx}}{E_y}.
$$

For the saved comparison inputs, both representations produce the same numerical compliance matrix $\mathbf S$ and the same inverted stiffness matrix $\mathbf D$:

| Companion check | Reported result |
| --- | ---: |
| Maximum absolute entrywise difference in $\mathbf S$ | 0 |
| Maximum absolute entrywise difference in $\mathbf D$ | 0 |
| Numerical equivalence checks | Pass |

These zeros are the **reported numerical matrix differences for the supplied test inputs**, not a claim of zero physical-model error. They confirm agreement of the two algebraic constructions under the chosen reciprocity and shear conventions. They do **not** independently validate experimental Redwood properties, finite-element interpolation, assembly, stress accuracy, or a posteriori certification.

To inspect the comparison independently:

```powershell
cd .\orthotropic_companion
python -m unittest discover -s tests -v
python .\compare_efunda_vs_hermite_orthotropic.py
```

The [comparison script](https://github.com/cognitiveforge630/HermiteStructural/blob/main/orthotropic_companion/compare_efunda_vs_hermite_orthotropic.py) and [saved matrix output](https://github.com/cognitiveforge630/HermiteStructural/blob/main/orthotropic_companion/compare_efunda_vs_hermite_orthotropic_output.txt) preserve the test inputs and full matrices. The companion is a **constitutive-matrix verification exercise**, separate from the current higher-order cantilever benchmark; its saved input values should not be mistaken for a newly measured material dataset.

## What Is Verified—and What Is Not Yet Certified

The results support two deliberately narrow statements:

**First**, a higher-order Hermite cantilever run has shown a **0.483063% displacement difference** from its stated beam-theory comparison with the specified applied loads and reference assumptions.

**Second**, the two tested orthotropic matrix constructions produce numerically identical compliance and stiffness matrices for their published comparison fixture.

Neither observation establishes a general certified Hermite finite-element solver. Rigorous a posteriori error certification would require documented admissibility and boundary treatment, verified equilibrium or equilibrated reconstruction as appropriate, and mathematically justified error bounds for a clearly defined problem and norm. Displacement agreement, passing unit tests, and mesh refinement evidence are valuable verification steps, but they are not substitutes for such a certificate.

The project will continue to distinguish **benchmark comparison**, **mesh convergence**, **constitutive implementation checks**, and **rigorous certification** rather than applying one label to all four.

## Source and Reproduction

- [HermiteStructural repository](https://github.com/cognitiveforge630/HermiteStructural)
- [Higher-order Hermite runner](https://github.com/cognitiveforge630/HermiteStructural/blob/main/run_higher_order_hermite.py)
- [Orthotropic companion and its instructions](https://github.com/cognitiveforge630/HermiteStructural/tree/main/orthotropic_companion)
- [Current repository README](https://github.com/cognitiveforge630/HermiteStructural/blob/main/README.md)

All dimensional values above use **in, lbf, and psi**. The example and its published comparison are research and verification results, not a claim that the broader codebase or future applications are mathematically certified.

## Next Step: Rigorous A Posteriori Error Certification

The next major objective for **Tutorial 001** is to develop and demonstrate a **rigorous a posteriori error certificate** for the current higher-order Hermite finite-element formulation. This means going beyond agreement with a beam-theory reference to construct and verify a mathematically justified bound on the numerical error for a clearly specified problem and norm.

The certification work will address the admissibility of the approximation, boundary conditions and applied loads, equilibrium or equilibrated stress reconstruction where appropriate, and a computable error bound backed by reproducible tests. **This is the next research milestone, not a certification already achieved.**
