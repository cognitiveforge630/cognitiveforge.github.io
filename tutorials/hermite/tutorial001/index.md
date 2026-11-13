---
layout: hermite-tutorial
title: "Hermite Tutorial001 — Higher-node tensor-product Hermite solids"
subtitle: "From one-dimensional value-and-slope data to HermiteHex27 and HermiteHex64"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/
next_lesson: /tutorials/hermite/tutorial001/01-one-dimensional-hermite/
comments: true
---

This tutorial develops higher-node Hermite hexahedra with a tensor-product Hermite basis. It follows the interpolation data into the three-dimensional displacement field, physical gradients, strain-displacement matrix, stiffness, and structured assembly.

> **Keep the families distinct.** The site's separate [Lagrange tutorial]({{ '/tutorials/hermitestructural/tutorial001/' | relative_url }}) uses displacement values at 8, 27, or 64 nodes and C0 Lagrange polynomials. This Hermite tutorial uses displacement values and derivative DOFs at each support point. Its Hex27 and Hex64 have 648 and 1,536 local displacement DOFs.

## Lessons

<div class="hs-lesson-grid">
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/01-one-dimensional-hermite/' | relative_url }}">01 — Hermite data on a line</a><p>Three or four points, value-and-slope data, and degree-five or degree-seven polynomials.</p></div>
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/02-tensor-product-dofs/' | relative_url }}">02 — Build the 3D tensor basis</a><p>Eight derivative types at every support point and the Hex27/Hex64 DOF counts.</p></div>
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/03-physical-derivatives/' | relative_url }}">03 — Scale parent derivatives</a><p>Map derivative-valued DOFs between parent and physical coordinates.</p></div>
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/04-strain-operator/' | relative_url }}">04 — Form displacement and strain</a><p>Assemble the vector interpolation operator and engineering-strain B matrix.</p></div>
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/05-element-integration/' | relative_url }}">05 — Integrate the element</a><p>Stiffness, body force, face traction, and full tensor Gauss rules.</p></div>
<div class="hs-lesson-card"><a href="{{ '/tutorials/hermite/tutorial001/06-connectivity-and-code/' | relative_url }}">06 — Share DOFs and use the code</a><p>Structured connectivity, continuity, implementation entry points, and open verification work.</p></div>
</div>

## Scope and status

The associated implementation is in the separate solver project's core/hermite_tensor package. It currently supports axis-aligned affine elements, structured meshes, constant constitutive data, and constant loads. The interpolation definition is explicit; the implementation still needs independent numerical validation and performance work, especially for Hex64. This tutorial makes no stress-accuracy or structural-certification claim.
