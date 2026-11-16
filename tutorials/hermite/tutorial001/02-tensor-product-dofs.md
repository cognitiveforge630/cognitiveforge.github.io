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
`HermiteHex27` is a cube-shaped reference element with three support points on each axis: $-1,0,1$. The picture shows the 27 support points; the center point is highlighted. At every point, the element stores a field value and derivative data, not just a value.

<figure class="tutorial-figure" aria-labelledby="hex27-caption">
<svg viewBox="0 0 760 410" role="img" aria-labelledby="hex27-title hex27-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="hex27-title">HermiteHex27 support grid and an evaluation point</title>
  <desc id="hex27-desc">A three by three by three lattice of 27 points forms a reference cube. The center support point at zero, zero, zero is highlighted, and a sample evaluation point at one half, minus one half, one quarter is marked inside it.</desc>
  <rect x="10" y="10" width="740" height="390" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <text x="35" y="45" font-size="21" font-weight="700" fill="#17314b">HermiteHex27: 3 × 3 × 3 support points</text>
  <g stroke="#91a7b8" stroke-width="1.5" fill="none">
    <!-- Lines parallel to ξ, η, ζ through the 3×3×3 lattice. -->
    <path d="M160 180H360 M160 280H360 M160 380H360 M210 142.5H410 M210 242.5H410 M210 342.5H410 M260 105H460 M260 205H460 M260 305H460"/>
    <path d="M160 180V380 M260 105V305 M360 180V380 M210 142.5V342.5 M310 105V305 M410 142.5V342.5 M260 105V305 M360 180V380 M460 105V305"/>
    <path d="M160 180L260 105 M160 280L260 205 M160 380L260 305 M260 180L360 105 M260 280L360 205 M260 380L360 305 M360 180L460 105 M360 280L460 205 M360 380L460 305"/>
  </g>
  <g fill="#1677a8" stroke="white" stroke-width="2">
    <circle cx="160" cy="180" r="5"/><circle cx="260" cy="180" r="5"/><circle cx="360" cy="180" r="5"/><circle cx="160" cy="280" r="5"/><circle cx="260" cy="280" r="5"/><circle cx="360" cy="280" r="5"/><circle cx="160" cy="380" r="5"/><circle cx="260" cy="380" r="5"/><circle cx="360" cy="380" r="5"/>
    <circle cx="210" cy="142.5" r="5"/><circle cx="310" cy="142.5" r="5"/><circle cx="410" cy="142.5" r="5"/><circle cx="210" cy="242.5" r="5"/><circle cx="310" cy="242.5" r="5"/><circle cx="410" cy="242.5" r="5"/><circle cx="210" cy="342.5" r="5"/><circle cx="310" cy="342.5" r="5"/><circle cx="410" cy="342.5" r="5"/>
    <circle cx="260" cy="105" r="5"/><circle cx="360" cy="105" r="5"/><circle cx="460" cy="105" r="5"/><circle cx="260" cy="205" r="5"/><circle cx="360" cy="205" r="5"/><circle cx="460" cy="205" r="5"/><circle cx="260" cy="305" r="5"/><circle cx="360" cy="305" r="5"/><circle cx="460" cy="305" r="5"/>
  </g>
  <circle cx="310" cy="242.5" r="9" fill="#e26d42" stroke="white" stroke-width="3"/>
  <text x="319" y="239" font-size="14" font-weight="700" fill="#9b4528">center node (0,0,0)</text>
  <path d="M372.5 182.8l8 8-8 8-8-8z" fill="#17835d" stroke="white" stroke-width="2"/>
  <text x="385" y="195" font-size="13" fill="#176b4d">sample point</text>
  <text x="350" y="392" font-size="15" fill="#35566c">ξ: −1, 0, 1</text>
  <text x="70" y="283" font-size="15" fill="#35566c">η: −1, 0, 1</text>
  <text x="468" y="95" font-size="15" fill="#35566c">ζ: −1, 0, 1</text>
  <g font-size="15" fill="#17314b">
    <text x="515" y="118" font-weight="700">Each support point carries</text>
    <text x="515" y="150">8 scalar data types:</text>
    <text x="515" y="181">u, u<tspan baseline-shift="sub" font-size="70%">x</tspan>, u<tspan baseline-shift="sub" font-size="70%">y</tspan>, u<tspan baseline-shift="sub" font-size="70%">z</tspan></text>
    <text x="515" y="207">u<tspan baseline-shift="sub" font-size="70%">xy</tspan>, u<tspan baseline-shift="sub" font-size="70%">xz</tspan>, u<tspan baseline-shift="sub" font-size="70%">yz</tspan>, u<tspan baseline-shift="sub" font-size="70%">xyz</tspan></text>
    <text x="515" y="257" font-weight="700">27 points × 8 = 216</text>
    <text x="515" y="280">scalar DOFs per field</text>
    <text x="515" y="324" font-weight="700">3 displacement fields</text>
    <text x="515" y="347">× 216 = 648 local DOFs</text>
  </g>
</svg>
<figcaption id="hex27-caption">The blue dots are the 27 interpolation support points. The highlighted center node is $(\xi,\eta,\zeta)=(0,0,0)$; the green diamond is an interior point where we can evaluate the interpolated field. Each point carries the eight derivative combinations shown.</figcaption>
</figure>

## A real tensor-product calculation

At the three one-dimensional support points $-1,0,1$, the middle node's value basis and slope basis are

$$
H_{1,0}(s)=(1-s^2)^2=1-2s^2+s^4,\qquad
H_{1,1}(s)=s(1-s^2)^2=s-2s^3+s^5.
$$

They are chosen so that at the middle node, $H_{1,0}(0)=1$, $H_{1,0}'(0)=0$, $H_{1,1}(0)=0$, and $H_{1,1}'(0)=1$; at the other two nodes, both value and slope data for these middle-node functions are zero. The other two support points have their own paired polynomials, giving six 1D functions per axis and $6^3=216$ scalar tensor-product functions in a Hex27.

For completeness, the six one-dimensional polynomials used on the three-point axis are:

$$
\begin{array}{c|cc}
\text{support point} & \text{value basis }H_{i,0}(s) & \text{slope basis }H_{i,1}(s)\\ \hline
-1\ (i=0) & \frac14s^2(s-1)^2(3s+4) & -\frac1{12}s^2(s-1)^2\\[2pt]
0\ (i=1) & (1-s^2)^2 & s(1-s^2)^2\\[2pt]
1\ (i=2) & \frac14s^2(s+1)^2(4-3s) & \frac1{12}s^2(s+1)^2
\end{array}
$$

The subscript $0$ means “unit value at this support point”; subscript $1$ means “unit derivative there.” Every other value and derivative at all three support points is zero. Each 3D scalar shape is made by choosing one of these six polynomials independently for $\xi$, $\eta$, and $\zeta$, then multiplying the three choices (with length factors for derivative DOFs).

Choose the center support node $(i,j,k)=(1,1,1)$ and its mixed $xz$ derivative DOF, whose derivative mask is $(a,b,c)=(1,0,1)$. On a physical cube with side lengths $h_x=h_y=h_z=2$, the half-length scales are all one. Its actual 3D shape function is therefore

$$
N_{111}^{101}(\xi,\eta,\zeta)
=\left[\frac{h_x}{2}H_{1,1}(\xi)\right]
 H_{1,0}(\eta)
 \left[\frac{h_z}{2}H_{1,1}(\zeta)\right]
=H_{1,1}(\xi)H_{1,0}(\eta)H_{1,1}(\zeta).
$$

Now evaluate at the green point $(\xi,\eta,\zeta)=(0.5,-0.5,0.25)$. Substitute one coordinate at a time:

$$
\begin{aligned}
H_{1,1}(0.5)&=0.5(1-0.5^2)^2=0.5(0.75)^2=0.28125=\frac{9}{32},\\
H_{1,0}(-0.5)&=(1-(-0.5)^2)^2=(0.75)^2=0.5625=\frac{9}{16},\\
H_{1,1}(0.25)&=0.25(1-0.25^2)^2=0.25(0.9375)^2=0.2197265625=\frac{225}{1024}.
\end{aligned}
$$

Multiply those three numbers to get the scalar basis value:

$$
N_{111}^{101}(0.5,-0.5,0.25)
=\frac{9}{32}\times\frac{9}{16}\times\frac{225}{1024}
=\frac{18225}{524288}
\approx 0.0347614.
$$

That number is the weight of the center node's $u_{xz}$ DOF in the interpolated scalar field at this point. For example, if that one DOF were 4 and every other DOF were zero, its contribution to the field here would be $4\times0.0347614\approx0.139046$. In a real element, we add the corresponding contribution from every one of the 216 scalar DOFs (or 648 displacement DOFs).

The implementation in `core/elements/hermite/tensor_product/basis.py` computes these same weights: `one_dimensional_hermite` evaluates the 1D polynomials and `tensor_hermite_shapes` multiplies the three directional factors. `HermiteHex27.displacement_at` uses the resulting weights to interpolate displacement; the strain and stiffness calculations use their physical gradients.

## What the nodal functional does

The nodal functional is the operation that **reads one particular piece of nodal data from a function**. For support point $(i,j,k)$ and derivative type $(a,b,c)$, write it as

$$
\ell_{ijk}^{abc}[u]
=\left.
\frac{\partial^{a+b+c}u}
{\partial x^a\,\partial y^b\,\partial z^c}
\right|_{\text{support node }(i,j,k)},
\qquad a,b,c\in\{0,1\}.
$$

If an exponent is zero, there is no derivative in that direction: $(0,0,0)$ reads the value $u$, $(1,0,0)$ reads $u_x$, and $(1,0,1)$ reads the mixed derivative $u_{xz}$. So a nodal functional is like a precisely defined measurement at a node. It is not another basis polynomial, and it is not an extra input to choose during evaluation. In this implementation it acts on the interpolated field; the matching DOF stores the value that this measurement must return.

Each basis function is built to be *dual* to one such measurement:

$$
\ell_{i'j'k'}^{a'b'c'}\!\left[N_{ijk}^{abc}\right]
=\delta_{ii'}\delta_{jj'}\delta_{kk'}\delta_{aa'}\delta_{bb'}\delta_{cc'}.
$$

The deltas mean “one for the matching node and derivative type, zero for every other one.” We can calculate the matching functional directly for our selected shape. At the center node, $\xi=\eta=\zeta=0$, and the affine map gives $\partial\xi/\partial x=2/h_x$ and $\partial\zeta/\partial z=2/h_z$:

$$
\begin{aligned}
\ell_{111}^{101}[N_{111}^{101}]
&=\left.\frac{\partial^2 N_{111}^{101}}{\partial x\,\partial z}\right|_{(0,0,0)}\\
&=\frac{h_x}{2}\frac{h_z}{2}\frac{2}{h_x}\frac{2}{h_z}\,
 H'_{1,1}(0)H_{1,0}(0)H'_{1,1}(0)\\
&=1\times1\times1\times1\times1=1.
\end{aligned}
$$

The half-length factors in the shape cancel the coordinate-conversion factors from differentiating, leaving exactly one. Evaluating any other nodal functional on this shape returns zero. This is how the interpolant preserves the data that were put into its DOF vector.

For one scalar field, the full interpolation is the sum of all data times their matching shape functions:

$$
u_h(\xi,\eta,\zeta)
=\sum_{i,j,k=0}^{2}\ \sum_{a,b,c\in\{0,1\}}
\ell_{ijk}^{abc}[u]\,N_{ijk}^{abc}(\xi,\eta,\zeta).
$$

In a finite-element solve, the solver's unknowns provide those nodal data. At integration points, the element evaluates the shape functions and their gradients to compute displacement and strain from those unknowns. The nodal functionals define what each unknown means and guarantee that the basis interpolates it correctly. For nonconforming mesh interfaces, the code also evaluates these same value/derivative measurements from a neighboring element to construct hanging-node constraints in `tensor_hermite_functional_shapes`.

One coordinate detail is important: the polynomials are evaluated in parent coordinates $(\xi,\eta,\zeta)$, while this element stores physical-coordinate derivatives ($u_x,u_y,u_z,\ldots$). For an affine box, the shape factors for a derivative in direction $x$, $y$, or $z$ include $h_x/2$, $h_y/2$, or $h_z/2$, respectively. These factors make the parent-coordinate polynomial reproduce the physical derivative DOF; [Lesson 03 explains this scaling]({{ '/tutorials/hermite/tutorial001/03-physical-derivatives/' | relative_url }}).

## Hex27 and Hex64 data counts

For a three-component displacement field, every support point carries three copies of the eight scalar data types. The element counts are:

| Element | Support grid | Data per point | Local displacement DOFs |
| --- | ---: | ---: | ---: |
| HermiteHex27 | 3 × 3 × 3 | 3 × 8 = 24 | 648 |
| HermiteHex64 | 4 × 4 × 4 | 3 × 8 = 24 | 1,536 |

These counts include derivative data. They are not the $3\times27$ or $3\times64$ counts of displacement-only Lagrange elements.

## Tensor ordering

The implementation enumerates support points as $(i,j,k)$ with $k$ fastest, then enumerates the eight derivative masks $(a,b,c)$, also with $c$ fastest. The vector DOF block at a point is grouped by displacement component, with its eight derivative types contiguous. A solver must use this convention consistently in interpolation, $B$, connectivity, and boundary conditions.

This is a full tensor-product Hermite space. It does not infer mixed derivatives from neighboring values: the seven derivative types are independent DOFs.
