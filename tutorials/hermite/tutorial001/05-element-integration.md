---
layout: hermite-tutorial
title: "05 — Integrate the element"
subtitle: "Stiffness and loads use the same Hermite displacement interpolation"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/05-element-integration/
previous_lesson: /tutorials/hermite/tutorial001/04-strain-operator/
next_lesson: /tutorials/hermite/tutorial001/06-connectivity-and-code/
comments: true
---
Once B_H is available, linear elastic stiffness has the standard expression

$$
\mathbf K_e=\int_{\Omega_e}\mathbf B_H^T\mathbf D\mathbf B_H\,dV.
$$

A body force b uses the displacement interpolation,

$$
\mathbf f_e^{(b)}=\int_{\Omega_e}\mathbf N_H^T\mathbf b\,dV,
$$

and a face traction t uses its trace,

$$
\mathbf f_e^{(t)}=\int_{\Gamma_e}\mathbf N_H^T\mathbf t\,dA.
$$

Because N_H includes derivative DOFs, consistent loads can contribute to those generalized entries too. Loads should be integrated; a midpoint stress or force replacement is not an integration rule.

For the current degree-five and degree-seven tensor bases, the implementation selects six and eight Gauss points per axis for full integration. Curved geometry, spatially varying materials, and nonconstant tractions need additional treatment.
