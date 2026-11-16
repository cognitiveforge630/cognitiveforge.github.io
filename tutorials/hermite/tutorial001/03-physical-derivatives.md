---
layout: hermite-tutorial
title: "03 — Scale parent derivatives"
subtitle: "Convert between reference slopes and physical slopes step by step"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/03-physical-derivatives/
previous_lesson: /tutorials/hermite/tutorial001/02-tensor-product-dofs/
next_lesson: /tutorials/hermite/tutorial001/04-strain-operator/
comments: true
---
## One physical element, two coordinate systems

The Hermite polynomials are easiest to define on a standard reference cube, where each coordinate runs from $-1$ to $1$. The finite-element model, however, lives on a physical box measured in length units. The map between them changes the numerical size of derivatives. This lesson works through that conversion for one specific element.

Use a box whose lower corner is $(0,0,0)$ and whose side lengths are $h_x=4$, $h_y=6$, and $h_z=8$. Its reference cube and physical box are shown below. The green point has reference coordinates $(\xi,\eta,\zeta)=(0.5,0,-0.5)$.

<figure class="tutorial-figure" aria-labelledby="coordinate-map-caption">
<svg viewBox="0 0 900 390" role="img" aria-labelledby="coordinate-map-title coordinate-map-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="coordinate-map-title">Reference cube mapped to a physical box</title>
  <desc id="coordinate-map-desc">A reference cube with coordinates from minus one to one maps to a physical box with side lengths four, six, and eight. A highlighted reference point at 0.5, zero, minus 0.5 maps to physical point 3, 3, 2.</desc>
  <rect x="10" y="10" width="880" height="365" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <text x="45" y="48" font-size="21" font-weight="700" fill="#17314b">Reference element</text>
  <text x="485" y="48" font-size="21" font-weight="700" fill="#17314b">Physical element</text>
  <g stroke="#1677a8" stroke-width="2.5" fill="none">
    <path d="M70 120H245V285H70Z M115 85H290V250H115Z M70 120L115 85 M245 120L290 85 M245 285L290 250 M70 285L115 250"/>
  </g>
  <g font-size="14" fill="#35566c">
    <text x="68" y="315">each parent axis: −1 to 1</text>
    <text x="80" y="111">(−1,−1,−1)</text>
    <text x="250" y="304">(1,1,1)</text>
    <text x="250" y="278">ξ</text><text x="96" y="80">ζ</text><text x="53" y="205">η</text>
  </g>
  <path d="M335 185H435" stroke="#7454a5" stroke-width="4"/>
  <path d="M435 185l-13-8v16z" fill="#7454a5"/>
  <text x="347" y="164" font-size="14" fill="#7454a5">map coordinates</text>
  <g stroke="#1677a8" stroke-width="2.5" fill="none">
    <path d="M510 120H685V285H510Z M555 85H730V250H555Z M510 120L555 85 M685 120L730 85 M685 285L730 250 M510 285L555 250"/>
  </g>
  <g font-size="14" fill="#35566c">
    <text x="510" y="315">x: 0 to 4</text><text x="607" y="315">y: 0 to 6</text><text x="706" y="270">z: 0 to 8</text>
    <text x="517" y="111">(0,0,0)</text><text x="683" y="302">(4,6,8)</text>
  </g>
  <circle cx="213" cy="194" r="8" fill="#17835d" stroke="white" stroke-width="3"/>
  <text x="128" y="231" font-size="13" fill="#176b4d">(0.5, 0, −0.5)</text>
  <circle cx="652" cy="194" r="8" fill="#17835d" stroke="white" stroke-width="3"/>
  <text x="595" y="231" font-size="13" fill="#176b4d">(3, 3, 2)</text>
  <text x="45" y="356" font-size="14" fill="#526778">A full parent-coordinate step spans half the physical side length: hₓ/2=2, hᵧ/2=3, h_z/2=4.</text>
</svg>
<figcaption id="coordinate-map-caption">The reference cube gives every element the same convenient coordinates. The physical box supplies its actual location and size. Since the physical box is twice as long as the parent interval in each direction, one unit of parent-coordinate change corresponds to half a physical side length.</figcaption>
</figure>

## 1. Map a point before differentiating

For this box, $x_0=y_0=z_0=0$, so the coordinate map is

$$
x=2(1+\xi),\qquad y=3(1+\eta),\qquad z=4(1+\zeta).
$$

Substitute the green point one coordinate at a time:

$$
\begin{aligned}
x&=2(1+0.5)=3,\\
y&=3(1+0)=3,\\
z&=4(1-0.5)=2.
\end{aligned}
$$

So evaluating a field at parent point $(0.5,0,-0.5)$ means evaluating the same field at physical point $(3,3,2)$. Coordinates tell us *where* we are; the derivative scales below tell us how a change in one coordinate compares to a change in the other.

## 2. Convert one derivative at a time

Differentiate the map. For example, $dx/d\xi=2$, so the chain rule says

$$
\frac{\partial u}{\partial\xi}
=\frac{\partial u}{\partial x}\frac{dx}{d\xi}
=2\frac{\partial u}{\partial x}.
$$

Rearrange to get the physical derivative from the parent derivative:

$$
u_x=\frac{\partial u}{\partial x}
=\frac{1}{2}\frac{\partial u}{\partial\xi}
=\frac{2}{h_x}u_\xi.
$$

In the same way, for this box,

$$
u_y=\frac{1}{3}u_\eta,\qquad
u_z=\frac{1}{4}u_\zeta.
$$

The fractions are reciprocals of the half-lengths. A given physical change in $x$ is only half as large in parent coordinates when the element is wide; converting a parent slope back to a physical slope therefore multiplies by $2/h_x$.

### Numerical check with a real function

Let $u(x,y,z)=6xz$. At the mapped point $(x,y,z)=(3,3,2)$, its value and physical derivatives are

$$
u=6(3)(2)=36,\qquad
u_x=6z=12,\qquad
u_y=0,\qquad
u_z=6x=18.
$$

Now express the same function in parent coordinates. Since $x=2(1+\xi)$ and $z=4(1+\zeta)$,

$$
u(\xi,\eta,\zeta)=6\,[2(1+\xi)]\,[4(1+\zeta)]
=48(1+\xi)(1+\zeta).
$$

Differentiate with respect to the parent coordinates and substitute $(0.5,0,-0.5)$:

$$
u_\xi=48(1+\zeta)=48(0.5)=24,\qquad
u_\eta=0,\qquad
u_\zeta=48(1+\xi)=48(1.5)=72.
$$

Convert those results back to physical slopes:

$$
u_x=\frac12(24)=12,\qquad
u_y=\frac13(0)=0,\qquad
u_z=\frac14(72)=18.
$$

We recover the same physical derivatives. This is what the first-derivative scale factors do in practice.

## 3. Convert mixed derivatives by applying both scales

The mask $(a,b,c)$ says whether to differentiate once in each direction: 0 means no derivative there, 1 means take one. For $(a,b,c)=(1,0,1)$, the physical quantity is $u_{xz}$. Apply the chain rule in $x$ and then in $z$:

$$
u_{\xi\zeta}
=\frac{h_x}{2}\frac{h_z}{2}u_{xz}
=2\cdot4\cdot u_{xz}
=8u_{xz}.
$$

For our function, $u_{xz}=6$. Therefore

$$
u_{\xi\zeta}=8(6)=48,
\qquad\text{and conversely}\qquad
u_{xz}=\frac{1}{8}(48)=6.
$$

The same rule applies to any mask $(a,b,c)$ with entries 0 or 1:

$$
\frac{\partial^{a+b+c}u}{\partial\xi^a\partial\eta^b\partial\zeta^c}
=\left(\frac{h_x}{2}\right)^a
 \left(\frac{h_y}{2}\right)^b
 \left(\frac{h_z}{2}\right)^c
\frac{\partial^{a+b+c}u}{\partial x^a\partial y^b\partial z^c}.
$$

For this $4\times6\times8$ box, the eight cases are:

| Mask $(a,b,c)$ | What it measures | Parent derivative in terms of physical data |
|---|---|---|
| $(0,0,0)$ | $u$ | $u$ |
| $(1,0,0)$ | $u_x$ | $u_\xi=2u_x$ |
| $(0,1,0)$ | $u_y$ | $u_\eta=3u_y$ |
| $(0,0,1)$ | $u_z$ | $u_\zeta=4u_z$ |
| $(1,1,0)$ | $u_{xy}$ | $u_{\xi\eta}=6u_{xy}$ |
| $(1,0,1)$ | $u_{xz}$ | $u_{\xi\zeta}=8u_{xz}$ |
| $(0,1,1)$ | $u_{yz}$ | $u_{\eta\zeta}=12u_{yz}$ |
| $(1,1,1)$ | $u_{xyz}$ | $u_{\xi\eta\zeta}=24u_{xyz}$ |

The value case has no scale factor because it does not differentiate. A mixed derivative gets one half-length factor for every direction in which its mask is 1.

## 4. Why the Hermite shape functions get half-length factors

The global nodal data in this implementation are physical derivatives such as $u_x$ and $u_{xz}$. But the one-dimensional Hermite polynomials are defined using parent-coordinate derivatives such as $u_\xi$. To make a basis function match the *physical* DOF, its value-basis factor is multiplied by $h_d/2$ for each derivative in direction $d$.

For example, let $G(\xi)$ be the one-dimensional slope basis at a node, normalized so that its parent derivative there is $G'(\xi_i)=1$. If a node stores physical slope $u_x=5$, its contribution along $x$ is

$$
S(\xi)u_x=\left(\frac{h_x}{2}G(\xi)\right)5
=\left(2G(\xi)\right)5.
$$

Differentiate this contribution with respect to physical $x$. Because $\partial/\partial x=(2/h_x)\partial/\partial\xi=\frac12\partial/\partial\xi$,

$$
\left.\frac{\partial}{\partial x}\left[2G(\xi)5\right]\right|_{\xi_i}
=\frac12\,2\,G'(\xi_i)\,5
=\frac12\,2\,1\,5=5.
$$

The scale factor $h_x/2=2$ in the shape and the derivative conversion factor $2/h_x=1/2$ cancel. The basis therefore reproduces the physical slope that the global DOF represents.

The same cancellation works for the mixed $xz$ DOF. Its shape contains $(h_x/2)(h_z/2)=2\cdot4=8$. Taking one physical derivative in both directions contributes $(2/h_x)(2/h_z)=(1/2)(1/4)=1/8$. Their product is $8\cdot1/8=1$, so the shape returns exactly its stored $u_{xz}$ at its node.

## 5. Why neighboring elements must use physical derivatives

Imagine two elements sharing a face. One has $h_x=4$, and the other has $h_x=2$. The same shared physical slope, say $u_x=5$, must describe the same field on both sides. The parent-coordinate slopes differ because the elements have different sizes:

$$
u_\xi^{(left)}=\frac{4}{2}(5)=10,\qquad
u_\xi^{(right)}=\frac{2}{2}(5)=5.
$$

Those are different parent-coordinate numbers, but converting each back gives the same physical slope:

$$
u_x^{(left)}=\frac{2}{4}(10)=5,\qquad
u_x^{(right)}=\frac{2}{2}(5)=5.
$$

So the mesh stores and shares the physical derivative $u_x=5$ at the common node. Each element's shape function supplies its own half-length scale when it interpolates that shared value. If one side stored a parent slope while the other stored a physical slope, they would be assigning different meanings to the same shared DOF, and the two interpolated pieces would not match consistently.

## Where the code applies this

In `core/elements/hermite/tensor_product/basis.py`, `tensor_hermite_shapes` multiplies each 1D derivative basis by $(h_d/2)$ when that DOF differentiates along direction $d$. When the code asks for a physical gradient, it differentiates the 1D basis and multiplies by $2/h_d$. The two factors cancel in the matching nodal derivative, as in the arithmetic above. `tensor_hermite_functional_shapes` uses the same conversion when it evaluates physical nodal data to form hanging-node constraints.

This lesson uses an axis-aligned affine box, which is the geometry supported by this implementation. For a skewed or curved element, physical derivatives mix directions and require the full Jacobian chain rule (including additional terms for mixed derivatives); the simple independent factors $2/h_x$, $2/h_y$, and $2/h_z$ would no longer be sufficient.
