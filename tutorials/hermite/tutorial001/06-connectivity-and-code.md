---
layout: hermite-tutorial
title: "06 — Share DOFs and use the code"
subtitle: "Structured connectivity carries Hermite data across element faces"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/06-connectivity-and-code/
previous_lesson: /tutorials/hermite/tutorial001/05-element-integration/
next_lesson: /tutorials/hermite/tutorial001/
comments: true
---
The structured mesh shares support points across adjacent macro-elements. At every shared point, it shares all 24 displacement and derivative DOFs. In this tensor-product construction, the face displacement trace and first derivative normal to that face are determined by the shared face data. This gives matching displacement and first-derivative traces for axis-aligned affine neighbors.

A fully fixed face must prescribe displacement values and the derivative data needed by the chosen support model. The implementation convenience boundary_dofs(face) selects every DOF at every support point on that face; the physical meaning of any less restrictive condition needs to be stated explicitly.

## Implementation map

| Responsibility | Module |
| --- | --- |
| Confluent Vandermonde and tensor Hermite functions | core/hermite_tensor/basis.py |
| HermiteHex27/64 mechanics and element loads | core/hermite_tensor/elements.py |
| Structured support-point connectivity | core/hermite_tensor/mesh.py |
| Global sparse assembly and prescribed-DOF solve | core/hermite_tensor/assembly.py |

The public classes are HermiteHex27 and HermiteHex64, available from core.hermite_tensor. Their support-point counts are 27 and 64. Their derivative DOFs are independent unknowns; no Lagrange displacement-only basis is used in these classes.

## Verification still required

Before trusting a solve, check the one-dimensional Hermite cardinal identities, tensor-product nodal functionals, physical derivative scaling, rigid-body modes, affine displacement/strain reproduction, stiffness symmetry, load resultants, and mesh refinement. Hex64 also needs memory and runtime profiling. These checks are not claimed by this tutorial.

Continue to the [Lagrange tutorial]({{ '/tutorials/hermitestructural/tutorial001/' | relative_url }}) for the separate C0 displacement-only basis.
