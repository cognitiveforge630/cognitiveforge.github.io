---
layout: post
title: "Hexahedron Moment Tutorial 01: Isoparametric Ground Zero"
description: "Start reconstructing the HexahedronMoment formulation from the eight-node brick diagram, then connect the HermiteStructural source to Jacobians, Gauss integration, and isotropic or orthotropic material matrices."
tags: [Finite Element Analysis, Python, PyVista, Hexahedron, Orthotropic Material, Tutorial]
comments: true
math: true
---

# Hexahedron Moment Tutorial 01: Isoparametric Ground Zero

This page starts the documentation process for the hexahedron moment element.
The first object to understand is not the stiffness matrix. It is the diagram:
an eight-node isoparametric brick with local natural coordinates
$\xi$, $\eta$, and $\zeta$.

The companion source repository for these reconstruction notes begins here:

[HexahedronMomentDocs on GitHub](https://github.com/cognitiveforge630/HexahedronMomentDocs)

The main reference document for the notation in this tutorial is:

[HexahedronMoment.pdf]({{ "/assets/hexahedron-moment/HexahedronMoment.pdf" | relative_url }})

## The Ground-Zero Figure

The element is numbered with nodes `P1` through `P8`. At each node, the
formulation carries translational and rotational degrees of freedom. The
original figure uses `P1` as the visible example:

```text
u1, v1, w1
theta_u1, theta_v1, theta_w1
```

<figure class="visual-figure">
  <img src="{{ "/assets/hexahedron-moment/isoparametricformulation-source.png" | relative_url }}" alt="Source isoparametric Hex8 diagram with P1 through P8 node labels and P1 degrees of freedom">
  <figcaption>The source diagram is the first documentation anchor: node numbering, natural axes, and the P1 translational and rotational degrees of freedom.</figcaption>
</figure>

That local node picture is the bridge between the geometric brick and the
Hermite-style degrees of freedom used by the working cantilever example.

## First Reconstruction Step

The first PyVista script in the new repository draws the conceptual brick,
labels the eight nodes, adds the natural-coordinate axes, and marks the `P1`
degrees of freedom:

```powershell
py tutorial_01_isoparametric_hexahedron.py
```

To save a screenshot for the blog:

```powershell
py tutorial_01_isoparametric_hexahedron.py --screenshot outputs/isoparametric_hexahedron_ground_zero.png
```

The screenshot will become the first blog image once we are happy with the
camera angle, node numbering, and degree-of-freedom labels.

## Working Notes

This page is intentionally small. The next step is to compare the reproduced
PyVista figure against the source image and then start carrying the notation
from `HexahedronMoment.pdf` into a readable derivation.

## Verification References

The node labels in this tutorial follow the same 8-node hexahedron convention
used by the current `HermiteStructural` shape functions:

| Node | $\xi$ | $\eta$ | $\zeta$ |
| --- | ---: | ---: | ---: |
| P1 | -1 | -1 | -1 |
| P2 | +1 | -1 | -1 |
| P3 | +1 | +1 | -1 |
| P4 | -1 | +1 | -1 |
| P5 | -1 | -1 | +1 |
| P6 | +1 | -1 | +1 |
| P7 | +1 | +1 | +1 |
| P8 | -1 | +1 | +1 |

This convention is consistent with the standard trilinear Hex8 shape functions:

$$
N_I(\xi,\eta,\zeta) =
\frac{1}{8}(1+\xi_I \xi)(1+\eta_I \eta)(1+\zeta_I \zeta)
$$

where $(\xi_I,\eta_I,\zeta_I)$ are the natural coordinates of node $I$.

In the current Python implementation, that convention appears directly as the
eight scalar shape functions:

```python
def hex8_shape_functions(self, xi, eta, zeta):
    N = 0.125 * np.array([
        (1 - xi) * (1 - eta) * (1 - zeta),
        (1 + xi) * (1 - eta) * (1 - zeta),
        (1 + xi) * (1 + eta) * (1 - zeta),
        (1 - xi) * (1 + eta) * (1 - zeta),
        (1 - xi) * (1 - eta) * (1 + zeta),
        (1 + xi) * (1 - eta) * (1 + zeta),
        (1 + xi) * (1 + eta) * (1 + zeta),
        (1 - xi) * (1 + eta) * (1 + zeta),
    ])
    return N
```

Those same Lagrange functions also build the geometry map from the natural
cube to the physical element. The current source does that in the Jacobian
helper:

```python
def get_hermite_jacobian(self, xi, eta, zeta, coords):
    return self.hex8_shape_derivatives(xi, eta, zeta) @ coords
```

The name says `hermite_jacobian` because it belongs to the Hermite-style
element class, but the geometry mapping itself uses the standard Hex8 Lagrange
shape-function derivatives. The variable `coords` is the $8 \times 3$ table of
physical node coordinates:

$$
\mathrm{coords} =
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
\vdots & \vdots & \vdots \\
x_8 & y_8 & z_8
\end{bmatrix}.
$$

The shape functions map natural coordinates to physical coordinates by
interpolating the nodal geometry:

$$
x(\xi,\eta,\zeta) = \sum_{I=1}^{8} N_I(\xi,\eta,\zeta)x_I,
\qquad
y(\xi,\eta,\zeta) = \sum_{I=1}^{8} N_I(\xi,\eta,\zeta)y_I,
\qquad
z(\xi,\eta,\zeta) = \sum_{I=1}^{8} N_I(\xi,\eta,\zeta)z_I.
$$

The Jacobian comes from differentiating those three geometry interpolations
with respect to the natural coordinates. In matrix form, the code is doing

$$
J =
\begin{bmatrix}
\dfrac{\partial N_1}{\partial \xi} & \cdots & \dfrac{\partial N_8}{\partial \xi} \\
\dfrac{\partial N_1}{\partial \eta} & \cdots & \dfrac{\partial N_8}{\partial \eta} \\
\dfrac{\partial N_1}{\partial \zeta} & \cdots & \dfrac{\partial N_8}{\partial \zeta}
\end{bmatrix}
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
\vdots & \vdots & \vdots \\
x_8 & y_8 & z_8
\end{bmatrix}.
$$

So the resulting $3 \times 3$ matrix is

$$
J =
\begin{bmatrix}
\dfrac{\partial x}{\partial \xi} &
\dfrac{\partial y}{\partial \xi} &
\dfrac{\partial z}{\partial \xi} \\
\dfrac{\partial x}{\partial \eta} &
\dfrac{\partial y}{\partial \eta} &
\dfrac{\partial z}{\partial \eta} \\
\dfrac{\partial x}{\partial \zeta} &
\dfrac{\partial y}{\partial \zeta} &
\dfrac{\partial z}{\partial \zeta}
\end{bmatrix}.
$$

Equivalently, in the more explicit operator style used by the original PDF,
but with the source-code coordinate ordering, this is

$$
\mathbf{J}
=
\begin{bmatrix}
\dfrac{\partial}{\partial \xi}x(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \xi}y(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \xi}z(\xi,\eta,\zeta)
\\[1.0em]
\dfrac{\partial}{\partial \eta}x(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \eta}y(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \eta}z(\xi,\eta,\zeta)
\\[1.0em]
\dfrac{\partial}{\partial \zeta}x(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \zeta}y(\xi,\eta,\zeta) &
\dfrac{\partial}{\partial \zeta}z(\xi,\eta,\zeta)
\end{bmatrix}.
$$

This is the same Jacobian style shown in the original PDF, but written in the
source-code ordering: first $\xi$, then $\eta$, then $\zeta$. With that ordering
the derivative transformation is

$$
\begin{bmatrix}
\dfrac{\partial}{\partial x} \\
\dfrac{\partial}{\partial y} \\
\dfrac{\partial}{\partial z}
\end{bmatrix}
=
\left(J^{-1}\right)^T
\begin{bmatrix}
\dfrac{\partial}{\partial \xi} \\
\dfrac{\partial}{\partial \eta} \\
\dfrac{\partial}{\partial \zeta}
\end{bmatrix}.
$$

That transpose is not a separate extra operation in the theory. It appears
because the derivative vector is being treated as a column vector. The Python
source uses the same convention in `build_B_matrix`:

```python
J = self.get_hermite_jacobian(xi, eta, zeta, coords)
J_inv = np.linalg.inv(J)
gradients = [
    J_inv.T @ np.vstack((dN_dxi[row], dN_deta[row], dN_dzeta[row]))
    for row in range(3)
]
```

Here `np.vstack((dN_dxi[row], dN_deta[row], dN_dzeta[row]))` is the natural
derivative column block, ordered as $\xi$, $\eta$, $\zeta$. Multiplying by
`J_inv.T` converts those natural derivatives into physical derivatives with
respect to $x$, $y$, and $z$.

This is where the Lagrange functions remain essential even when the
displacement interpolation is Hermite-style. Their derivatives describe how
the local coordinate directions stretch, skew, or rotate into the real element.
That Jacobian is then used to convert derivatives taken with respect to
$(\xi,\eta,\zeta)$ into derivatives with respect to physical $(x,y,z)$.

## Hermite Basis Functions First

Before looking at the Hex8 Lagrange basis, it helps to remember what the
Hermite beam basis is doing in one natural coordinate. A two-node cubic Hermite
line element carries two kinds of nodal information: the displacement value at
the node and the slope, or rotation, attached to that node.

One way to see the machinery is to start with a cubic polynomial in the natural
coordinate,

$$
w(\xi) = a + b\xi + c\xi^2 + d\xi^3.
$$

Here $a$, $b$, $c$, and $d$ are not nodal degrees of freedom. They are only the
temporary polynomial coefficients. The nodal degrees of freedom are the two
values and two slopes:

$$
\begin{bmatrix}
w_1 \\
\theta_{w1} \\
w_2 \\
\theta_{w2}
\end{bmatrix}
=
\begin{bmatrix}
1 & -1 & 1 & -1 \\
0 & 1 & -2 & 3 \\
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 3
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c \\
d
\end{bmatrix}.
$$

This matrix is just the cubic polynomial and its derivative evaluated at the
two natural-coordinate nodes $\xi=-1$ and $\xi=+1$. The first and third rows
come from the value equation $w(\xi)$. The second and fourth rows come from the
slope equation

$$
\frac{dw}{d\xi} = b + 2c\xi + 3d\xi^2.
$$

So the rows mean

$$
\begin{aligned}
w_1 &= w(-1), &
\theta_{w1} &= \left.\frac{dw}{d\xi}\right|_{\xi=-1}, \\
w_2 &= w(+1), &
\theta_{w2} &= \left.\frac{dw}{d\xi}\right|_{\xi=+1}.
\end{aligned}
$$

Solving that small system expresses the polynomial coefficients
$(a,b,c,d)$ in terms of the physical nodal quantities
$(w_1,\theta_{w1},w_2,\theta_{w2})$. After substitution, the same cubic can be
written as a shape-function interpolation:

$$
w(\xi)
=
H_1(\xi)w_1
+ H_2(\xi)\theta_{w1}
+ H_3(\xi)w_2
+ H_4(\xi)\theta_{w2}.
$$

That is the source of the Hermite basis functions: they are the four cubic
weights that reproduce the two nodal values and the two nodal slopes.

Using $\xi \in [-1,1]$, one common ordering of the four basis functions is

$$
\begin{bmatrix}
H_1(\xi) \\
H_2(\xi) \\
H_3(\xi) \\
H_4(\xi)
\end{bmatrix}
=
\begin{bmatrix}
\dfrac{1}{4}\xi^3 - \dfrac{3}{4}\xi + \dfrac{1}{2} \\
\dfrac{1}{4}\xi^3 - \dfrac{1}{4}\xi^2 - \dfrac{\xi}{4} + \dfrac{1}{4} \\
-\dfrac{1}{4}\xi^3 + \dfrac{3}{4}\xi + \dfrac{1}{2} \\
\dfrac{1}{4}\xi^3 + \dfrac{1}{4}\xi^2 - \dfrac{\xi}{4} - \dfrac{1}{4}
\end{bmatrix}.
$$

In that ordering, $H_1$ and $H_3$ are the translational shape functions. They
interpolate the displacement values at the left and right nodes. The other two,
$H_2$ and $H_4$, are the rotational shape functions. They interpolate the nodal
slopes, which become beam rotations in the structural model. In a physical
beam element, the slope terms are usually paired with the appropriate element
length scaling when mapping from $\xi$ to the real coordinate.

The Python source applies that same idea in three natural directions. The
method `get_hermite_shape_functions_and_derivatives` evaluates the one-axis
Hermite value functions and derivative functions, then multiplies the
appropriate choices together across $\xi$, $\eta$, and $\zeta$. The resulting
`NH` values are the Hermite-style translation weights, while `RH` and `dRH`
carry the rotation-weight machinery and its natural-coordinate derivatives.
Those derivatives are still taken in isoparametric coordinates first; the
Jacobian section above explains how they are converted to physical
$(x,y,z)$ derivatives before the strain-displacement matrix is assembled.

The next piece of machinery is the strain-displacement matrix. For one node
$n$, the PDF-style block can be read as a per-node contribution $B_n$:

$$
\begin{bmatrix}
\varepsilon_x \\
\varepsilon_y \\
\varepsilon_z \\
\gamma_{xy} \\
\gamma_{yz} \\
\gamma_{zx}
\end{bmatrix}
=
\begin{bmatrix}
\dfrac{\partial NH_n}{\partial x} & 0 & 0 &
\dfrac{\partial RH_n}{\partial x} & 0 & 0 \\
0 & \dfrac{\partial NH_n}{\partial y} & 0 &
0 & \dfrac{\partial RH_n}{\partial y} & 0 \\
0 & 0 & \dfrac{\partial NH_n}{\partial z} &
0 & 0 & \dfrac{\partial RH_n}{\partial z} \\
\dfrac{\partial NH_n}{\partial y} &
\dfrac{\partial NH_n}{\partial x} & 0 &
\dfrac{\partial RH_n}{\partial y} &
\dfrac{\partial RH_n}{\partial x} & 0 \\
0 & \dfrac{\partial NH_n}{\partial z} &
\dfrac{\partial NH_n}{\partial y} &
0 & \dfrac{\partial RH_n}{\partial z} &
\dfrac{\partial RH_n}{\partial y} \\
\dfrac{\partial NH_n}{\partial z} & 0 &
\dfrac{\partial NH_n}{\partial x} &
\dfrac{\partial RH_n}{\partial z} & 0 &
\dfrac{\partial RH_n}{\partial x}
\end{bmatrix}
\begin{bmatrix}
u_n \\
v_n \\
w_n \\
\theta_{u n} \\
\theta_{v n} \\
\theta_{w n}
\end{bmatrix}.
$$

This is the same small-strain pattern as the source code: normal strains use
matching physical derivatives, and engineering shear strains use the symmetric
cross-derivative pairs. In the Python implementation, this is not stored as one
separate $6 \times 6$ block per node. Instead, `get_hermite_displacement_matrices`
fills the displacement and derivative columns for the full 8-node element, so
the element matrix has 48 columns:

```python
N_disp[0, col + DOF_UX] = NH[n]
N_disp[1, col + DOF_UY] = NH[n]
N_disp[2, col + DOF_UZ] = NH[n]
```

The rotational columns are added through `RH` and `dRH`:

```python
N_disp[row, col + dof] += sign * RH[axis, n]
dN_dxi[row, col + dof] += sign * dRH[0, axis, n]
dN_deta[row, col + dof] += sign * dRH[1, axis, n]
dN_dzeta[row, col + dof] += sign * dRH[2, axis, n]
```

After the Jacobian converts those natural derivatives into physical gradients,
`build_B_matrix` assembles the same six strain rows:

```python
B[0, :] = gradients[0][0, :]
B[1, :] = gradients[1][1, :]
B[2, :] = gradients[2][2, :]
B[3, :] = gradients[0][1, :] + gradients[1][0, :]
B[4, :] = gradients[1][2, :] + gradients[2][1, :]
B[5, :] = gradients[0][2, :] + gradients[2][0, :]
```

So the image is best understood as the compact mathematical view of the same
operation. The source code builds the full element version column by column,
with physical derivatives produced through the Jacobian transform.

Once the strain vector is built, the material stiffness matrix converts strain
to stress. In the source this matrix is named `D`.

The current code has two material routes. If orthotropic constants are supplied,
that route is used first:

```python
def elastic_matrix(self):
    if self.orthotropic_constants is not None:
        return self.orthotropic_elastic_matrix(self.orthotropic_constants)

    l = self.lambda_
    m = 2 * self.mu
    D = np.array([
        [l + m, l, l, 0, 0, 0],
        [l, l + m, l, 0, 0, 0],
        [l, l, l + m, 0, 0, 0],
        [0, 0, 0, self.mu, 0, 0],
        [0, 0, 0, 0, self.mu, 0],
        [0, 0, 0, 0, 0, self.mu]
    ])
    return D
```

The lower branch is the isotropic Lamé matrix. Since `m = 2 * self.mu`, the
normal-strain diagonal entries are $\lambda + 2\mu$. Written in the same
stress-strain order used by `B`, the isotropic constitutive equation is

$$
\begin{bmatrix}
\sigma_x \\
\sigma_y \\
\sigma_z \\
\tau_{xy} \\
\tau_{yz} \\
\tau_{xz}
\end{bmatrix}
=
\begin{bmatrix}
\lambda + 2\mu & \lambda & \lambda & 0 & 0 & 0 \\
\lambda & \lambda + 2\mu & \lambda & 0 & 0 & 0 \\
\lambda & \lambda & \lambda + 2\mu & 0 & 0 & 0 \\
0 & 0 & 0 & \mu & 0 & 0 \\
0 & 0 & 0 & 0 & \mu & 0 \\
0 & 0 & 0 & 0 & 0 & \mu
\end{bmatrix}
\begin{bmatrix}
\varepsilon_x \\
\varepsilon_y \\
\varepsilon_z \\
\gamma_{xy} \\
\gamma_{yz} \\
\gamma_{xz}
\end{bmatrix}.
$$

The Lamé parameters are computed from the input Young's modulus and Poisson
ratio:

$$
\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)},
\qquad
\mu = \frac{E}{2(1+\nu)}.
$$

For the Redwood/AWC path, the source passes an `OrthotropicElasticity` object
instead. That object builds the compliance matrix first:

$$
S =
\begin{bmatrix}
1/E_x & -\nu_{xy}/E_x & -\nu_{xz}/E_x & 0 & 0 & 0 \\
-\nu_{xy}/E_x & 1/E_y & -\nu_{yz}/E_y & 0 & 0 & 0 \\
-\nu_{xz}/E_x & -\nu_{yz}/E_y & 1/E_z & 0 & 0 & 0 \\
0 & 0 & 0 & 1/G_{xy} & 0 & 0 \\
0 & 0 & 0 & 0 & 1/G_{yz} & 0 \\
0 & 0 & 0 & 0 & 0 & 1/G_{xz}
\end{bmatrix}.
$$

Then the elasticity matrix used by the element is

$$
D = S^{-1}.
$$

The code validates that both the compliance matrix and the elasticity matrix are
positive definite. That is an important guardrail: an orthotropic material is
not just six random moduli plus three random Poisson ratios. The constants have
to form a physically usable stiffness matrix.

For the wood example, `solver.py` maps the material axes as

```text
R -> x
T -> y
L -> z
```

so the longitudinal wood direction is the beam axis. Published major Poisson
ratios such as $\nu_{LR}$ and $\nu_{LT}$ are converted into the reciprocal minor
ratios before filling the source fields `nuxz` and `nuyz`. That is why the blog
can now say "orthotropic" without hand waving: the active source path really is
using the orthotropic `D` matrix when `orthotropic_constants` is present.

The matrix appears directly in the element stiffness integration:

```python
Ke += B.T @ self.D @ B * w * detJ
```

and the same stress relation is used later for stress recovery:

```python
stress = D @ strain
```

The integration order is also no longer a two-point assumption in the current
source. `FEMHermiteBeamRegion` defaults to `gauss_order=3` and calls
`leggauss(self.gauss_order)`. For a hexahedral volume integral this means 27
Gauss points per element. A user can still pass `gauss_order=2` deliberately for
a comparison study, but it is not the default path for the current
Redwood/AWC-calibrated solver.

That distinction is the important conceptual bridge. A Lagrange element only
asks, "what is the field value at each node?" A Hermite element asks for both
the field value and derivative-type information at the node. For a beam, that
means displacement plus rotation. In the full three-dimensional model, each
node carries translational degrees of freedom and rotational degrees of
freedom, which is why the source diagram lists both
$(u_1,v_1,w_1)$ and $(\theta_{u1},\theta_{v1},\theta_{w1})$ at `P1`.

The Hex8 scalar functions above are Lagrange shape functions in nature, but in
the simplest possible 3D brick form: trilinear tensor-product Lagrange
functions. Along one natural axis, the two linear Lagrange basis functions are

$$
L_-(s)=\frac{1-s}{2}, \qquad L_+(s)=\frac{1+s}{2}.
$$

Each Hex8 node chooses either the minus or plus basis on each axis and
multiplies the three choices together. For example, node `P1` sits at
$(\xi,\eta,\zeta)=(-1,-1,-1)$, so its shape function is

$$
N_1(\xi,\eta,\zeta)
= L_-(\xi)L_-(\eta)L_-(\zeta)
= \frac{1}{8}(1-\xi)(1-\eta)(1-\zeta).
$$

That is why each row in the code has the same recognizable pattern: pick the
signs for that node, multiply one linear factor from each coordinate direction,
and scale by `0.125`. The functions are therefore linear in each coordinate
separately, but their product gives the full trilinear interpolation over the
natural cube.

Useful references:

- *HexahedronMoment.pdf*, the source notation document for this reconstruction.  
  [{{ "/assets/hexahedron-moment/HexahedronMoment.pdf" | relative_url }}]({{ "/assets/hexahedron-moment/HexahedronMoment.pdf" | relative_url }})
- J. Machacek, *numgeo: Hexahedral elements*, section "8-node hexahedron."  
  [https://j-machacek.github.io/numgeo/theory/elements/hexahedra.html](https://j-machacek.github.io/numgeo/theory/elements/hexahedra.html)
- X. Zhang, Z. Chen, Y. Liu, *The Material Point Method*, 2017, section 5.1.3,
  "Hexahedron Element." The ScienceDirect excerpt gives the same nodal natural
  coordinate table for $\xi_I$, $\eta_I$, and $\zeta_I$.  
  [https://www.sciencedirect.com/topics/engineering/hexahedron-element](https://www.sciencedirect.com/topics/engineering/hexahedron-element)

Different finite element programs may display or input brick-node numbering in
different visual orders, so the safest verification is always the actual shape
function table used by the code.
