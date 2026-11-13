---
layout: hermite-tutorial
title: "03 — Scale parent derivatives"
subtitle: "Derivative DOFs must use a consistent physical-coordinate convention"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/03-physical-derivatives/
previous_lesson: /tutorials/hermite/tutorial001/02-tensor-product-dofs/
next_lesson: /tutorials/hermite/tutorial001/04-strain-operator/
comments: true
---
Hermite data include derivatives, so changing coordinates changes the nodal functionals. For an axis-aligned affine element,

<div class="hs-equation">
\[
x=x_0+\frac{h_x}{2}(1+\xi),\quad
y=y_0+\frac{h_y}{2}(1+\eta),\quad
z=z_0+\frac{h_z}{2}(1+\zeta).

\]
</div>

For derivative mask (a,b,c), with each entry 0 or 1,

<div class="hs-equation">
\[
\frac{\partial^{a+b+c}u}{\partial \xi^a\partial\eta^b\partial\zeta^c}
=
\left(\frac{h_x}{2}\right)^a
\left(\frac{h_y}{2}\right)^b
\left(\frac{h_z}{2}\right)^c
\frac{\partial^{a+b+c}u}{\partial x^a\partial y^b\partial z^c}.

\]
</div>

Therefore, if global DOFs store physical-coordinate derivatives, the parent-space Hermite shape paired with that DOF carries the product of half-length scale factors. Differentiating the shape back to physical space contributes the corresponding Jacobian factor 2/h_d.

This convention matters when adjacent elements have different sizes: shared physical derivative DOFs must represent the same quantity on both sides. Mixing parent-coordinate slopes with physical-coordinate slopes would make assembly inconsistent.

The current higher-node Hermite implementation uses an axis-aligned affine map. Curved or skewed geometry needs the full chain rule for mixed derivatives and is outside this first implementation.
