---
layout: hermite-tutorial
title: "01 — Hermite data on a line"
subtitle: "Interpolate both a value and a slope at every support point"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/01-one-dimensional-hermite/
previous_lesson: /tutorials/hermite/tutorial001/
next_lesson: /tutorials/hermite/tutorial001/02-tensor-product-dofs/
comments: true
---
A Lagrange polynomial is fixed by its values at distinct points. A Hermite polynomial is fixed by values and derivatives. This change in interpolation data gives the Hermite basis its additional degrees of freedom.

Let there be m support points s_i on the reference interval. We seek a polynomial of degree at most 2m-1, with 2m coefficients, satisfying

<div class="hs-equation">
\[
H_{i,0}(s_j)=\delta_{ij},\quad H'_{i,0}(s_j)=0,\qquad
H_{i,1}(s_j)=0,\quad H'_{i,1}(s_j)=\delta_{ij}.

\]
</div>

The index 0 selects the value functional; 1 selects the slope functional. These conditions uniquely determine the 2m one-dimensional Hermite shape functions.

For three equally spaced points (-1,0,1), there are six functions and the polynomial degree is five. For four equally spaced points (-1,-1/3,1/3,1), there are eight functions and the degree is seven.

## Confluent Vandermonde construction

Write p(s)=sum c_k s^k. Each nodal value contributes a row [1,s_i,s_i^2,...] to the interpolation matrix. Each slope contributes the differentiated row [0,1,2s_i,...]. This value-and-derivative matrix is a confluent Vandermonde matrix. Inverting it maps nodal functionals to polynomial coefficients.

The companion implementation constructs this matrix in core/hermite_tensor/basis.py and evaluates its basis and derivatives. It is maintained separately from the Lagrange cardinal-product construction.

## Why these are Hermite functions

At each support point, one function returns unit value and zero slope while its paired function returns zero value and unit slope. The interpolant therefore reproduces each supplied value and slope exactly. Three or four points per direction create the support grids for HermiteHex27 and HermiteHex64; each point has both kinds of one-dimensional data.
