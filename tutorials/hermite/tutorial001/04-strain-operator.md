---
layout: hermite-tutorial
title: "04 — Form displacement and strain"
subtitle: "The Hermite basis enters the familiar six-component elasticity equations"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/04-strain-operator/
previous_lesson: /tutorials/hermite/tutorial001/03-physical-derivatives/
next_lesson: /tutorials/hermite/tutorial001/05-element-integration/
comments: true
---
Collect all scalar basis functions into N_H. For displacement components u,v,w, the displacement interpolant is assembled by placing the scalar basis in the columns belonging to its component and derivative type:
\[
\begin{bmatrix}u\\v\\w\end{bmatrix}=\mathbf N_H\mathbf d_e.
\]
Here d_e is the full local vector of value and derivative DOFs described in [Lesson 02]({{ '/tutorials/hermite/tutorial001/02-tensor-product-dofs/' | relative_url }}).

Differentiate each basis function in physical coordinates to obtain the strain-displacement matrix. With engineering shear strain and Voigt order (xx,yy,zz,xy,yz,xz), the six rows are
\[
\epsilon_{xx}=u_{,x},\quad \epsilon_{yy}=v_{,y},\quad \epsilon_{zz}=w_{,z},
\]
\[
\gamma_{xy}=u_{,y}+v_{,x},\quad
\gamma_{yz}=v_{,z}+w_{,y},\quad
\gamma_{xz}=u_{,z}+w_{,x}.
\]
Thus epsilon=B_H d_e. The basis is Hermite; the small-strain constitutive relation retains its familiar form sigma=D epsilon.

The local B matrix has six rows and 648 columns for HermiteHex27, or six rows and 1,536 columns for HermiteHex64. Its width follows from the derivative-valued DOFs, not from a change in the number of strain components.
