---
layout: hermite-tutorial
title: "02 — Build the 3D tensor basis"
subtitle: "Eight derivative types at every support point"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/02-tensor-product-dofs/
previous_lesson: /tutorials/hermite/tutorial001/01-one-dimensional-hermite/
next_lesson: /tutorials/hermite/tutorial001/03-physical-derivatives/
comments: true
---
Let H_i,a(s) be the one-dimensional basis at support point i, where a=0 means value and a=1 means first derivative. The three-dimensional scalar basis is

<div class="hs-equation">
\[
N_{ijk}^{abc}(\xi,\eta,\zeta)=H_{i,a}(\xi)H_{j,b}(\eta)H_{k,c}(\zeta),
\qquad a,b,c\in\{0,1\}.

\]
</div>

It pairs with the nodal functional

<div class="hs-equation">
\[
\frac{\partial^{a+b+c}u}{\partial x^a\,\partial y^b\,\partial z^c}

\]
</div>

at support point (i,j,k). One scalar field therefore has eight data at each point:
u, u_x, u_y, u_z, u_xy, u_xz, u_yz, u_xyz.

For a three-component displacement field, each point carries 24 scalar unknowns. The element counts are:

| Element | Support grid | Data per point | Local displacement DOFs |
| --- | ---: | ---: | ---: |
| HermiteHex27 | 3 × 3 × 3 | 3 × 8 = 24 | 648 |
| HermiteHex64 | 4 × 4 × 4 | 3 × 8 = 24 | 1,536 |

These counts include derivative data. They are not the 3×27 or 3×64 counts of displacement-only Lagrange elements.

## Tensor ordering

The implementation enumerates support points as (i,j,k) with k fastest, then enumerates the eight derivative masks (a,b,c), also with c fastest. The vector DOF block at a point is grouped by displacement component, with its eight derivative types contiguous. A solver must use this convention consistently in interpolation, B, connectivity, and boundary conditions.

This is a full tensor-product Hermite space. It does not infer mixed derivatives from neighboring values: the seven derivative types are independent DOFs.
