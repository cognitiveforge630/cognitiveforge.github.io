---
layout: post
title: "Hermite Beam Tutorial 00: Cantilever Beam, Orthotropic Redwood, and End-Face Traction"
description: "HermiteStructural cantilever tutorial using orthotropic Redwood/AWC material, three-point Gauss integration, calibrated longitudinal modulus, and PyVista end-face traction integration viewer."
tags: [Finite Element Analysis, Python, Hermite Beam, Orthotropic Material, Tutorial]
comments: true
math: true
---

# Hermite Beam Tutorial 00: Cantilever Beam, Orthotropic Redwood, and End-Face Traction

This tutorial documents the cantilever check for the `HermiteStructural`
project: an orthotropic Redwood/AWC material model, end-face traction loading,
three-point Gauss integration, and a calibrated longitudinal modulus that makes
the finite element free-end displacement match the classical cantilever target.

The model is a three-dimensional Hermite-style Hex8 beam with six degrees of
freedom per node:

```text
ux, uy, uz, phix, phiy, phiz
```

The finite element solve uses these ingredients:

- the load is a transverse traction integrated over the `z = L` end face,
- stiffness uses three-point Gauss integration in each element direction,
- the material is an orthotropic Redwood/AWC-style elasticity matrix,
- the first solve uses the reference longitudinal modulus,
- the second solve calibrates the longitudinal modulus so the linear finite
  element result lands exactly on the beam-theory displacement target.

The source repository is here:

[HermiteStructural on GitHub](https://github.com/cognitiveforge630/HermiteStructural)

If Python and Visual Studio Code are not installed yet, start with this setup
walkthrough first:

[Installing Python on Windows with Python Manager and Visual Studio Code]({{ "/2026/05/10/install-python-windows-vscode.html" | relative_url }})

## The Physical Test Case

The beam is a rectangular cantilever. The left end at `z = 0` is fixed. The
right end at `z = L` receives the total transverse load.

| Quantity | Value |
| --- | ---: |
| Width in global `x`, $L_x$ | 4 in |
| Depth in global `y`, $L_y$ | 8 in |
| Length in global `z`, $L = L_z$ | 120 in |
| Mesh nodes | $5 \times 9 \times 121$ |
| End-face nodes | 45 |
| Element type | Hermite-style Hex8 |
| Degrees of freedom per node | 6 |
| Volume Gauss rule | 3-point per axis, 27 points per element |
| End-face Gauss rule | 3-point by 3-point surface integration |
| Total transverse load, $P$ | -12.8 lb |
| End-face area, $A_f=L_xL_y$ | 32 in$^2$ |
| Uniform end traction, $t_y=P/A_f$ | -0.4 psi |
| Reference longitudinal modulus, $E_L$ | 2,000,000 psi |
| Strong-axis inertia, $I=bh^3/12$ | 170.666667 in$^4$ |

The mesh and boundary condition are intentionally plain: the entire `z = 0`
face is fixed, and all six degrees of freedom are constrained at those nodes.
That makes the first structural question simple: does the model bend in the
right direction and at the right scale?

> **Scope note:** this benchmark currently includes the applied end-face
> traction and the elastic orthotropic stiffness only. Beam self-weight/body
> force loading and temperature-change effects, such as thermal strain or
> thermal expansion, are not included in this problem yet. Those should be
> added later as separate load or initial-strain terms before treating this as
> a complete service-load model.

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-beam-mesh-pinned-nodes.png' | relative_url }}" alt="Hermite beam mesh with pinned nodes at z equals zero">
  <figcaption>The beam is long in the global z direction, and the nodes on the left face are fixed for the cantilever check.</figcaption>
</figure>

## The Classical Cantilever Target

For a cantilever beam with a concentrated transverse load at the free end,
the Euler-Bernoulli free-end deflection is

$$
\Delta_{\max}=\frac{P L^3}{3 E I}.
$$

The cross section is 4 in by 8 in. For bending caused by a transverse `y` load
on a beam whose span is the global `z` axis, the inertia used by this check is

$$
I=\frac{b h^3}{12}
  =\frac{4(8^3)}{12}
  =170.666667\;\text{in}^4.
$$

Using the reference AWC/theory modulus,

$$
\begin{aligned}
P &= -12.8\;\text{lb},\\
L &= 120\;\text{in},\\
E &= 2{,}000{,}000\;\text{psi},\\
I &= 170.666667\;\text{in}^4,
\end{aligned}
$$

so the target displacement is

$$
\Delta_{\text{target}}
=\frac{-12.8(120)^3}{3(2{,}000{,}000)(170.666667)}
=-2.160\times 10^{-2}\;\text{in}.
$$

In the source, this hand calculation lives in `checkme.py`:

```python
E = 2_000_000.0  # psi
L = 120.0        # in
B = 4.0          # in
H = 8.0          # in
I = B * H**3 / 12.0
P = -12.8        # lb


def cantilever_point_load_deflection(load, length, youngs_modulus, inertia):
    return load * length**3 / (3.0 * youngs_modulus * inertia)
```

This is the scalar target. It is not pretending that a 3D orthotropic Hermite
solid is literally a one-dimensional Euler-Bernoulli beam. It gives us a clean
sanity check for sign, load total, stiffness scale, and displacement magnitude.

The baseline comparison below is therefore the calibrated orthotropic solve:
its printed free-end displacement is the same as the beam-theory target, and
its printed relative difference is `0.000000%`.

## The Element And Connectivity Views

Before solving, the screenshots show what is being assembled.
The element viewer lets us inspect one Hex8 element and its local-to-global
node mapping.

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-hex8-element-inspector.png' | relative_url }}" alt="Hex8 element inspector showing local nodes, global nodes, and degrees of freedom">
  <figcaption>The Hex8 element inspector. This is useful when checking local node numbers, global node numbers, and the 48 element degrees of freedom.</figcaption>
</figure>

The stiffness matrix is assembled through shared nodes. When two elements share
a node, their element stiffness contributions land in the same global rows and
columns. That is the finite element coupling mechanism.

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-k-connectivity-shared-nodes.png' | relative_url }}" alt="K connectivity visualization showing shared nodes and shared global rows and columns">
  <figcaption>Shared nodes create shared global stiffness rows and columns. This is the visual version of adding each local `Ke` into the global sparse matrix.</figcaption>
</figure>

The assembly stepper screenshots make this even more explicit. One element owns
48 local degrees of freedom because it has eight nodes and six degrees of
freedom per node:

$$
8\;\text{nodes}\times 6\;\text{dof/node}=48\;\text{element dof}.
$$

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-element-assembly-trace-face0.png' | relative_url }}" alt="Element assembly trace showing local nodes mapped to global degrees of freedom">
  <figcaption>Element assembly trace for one selected element. The labels show how local nodes become global nodes and then global degree-of-freedom numbers.</figcaption>
</figure>

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-element-assembly-trace-face1.png' | relative_url }}" alt="Second element assembly trace showing shared and unshared node mappings">
  <figcaption>A neighboring element has a different local element index, but shared physical nodes still point back into shared global rows and columns.</figcaption>
</figure>

## Orthotropic Redwood/AWC Material Model

The solver constructs a Redwood-like orthotropic material with the wood axes
mapped as

$$
R\rightarrow x,\qquad T\rightarrow y,\qquad L\rightarrow z.
$$

That means the beam span direction uses the longitudinal modulus $E_z=E_L$.
The code starts from ratios relative to the longitudinal modulus:

```python
REDWOOD_CLEAR_WOOD_RATIOS = {
    "E_T_over_E_L": 0.089,
    "E_R_over_E_L": 0.087,
    "G_LR_over_E_L": 0.066,
    "G_LT_over_E_L": 0.077,
    "G_RT_over_E_L": 0.011,
    "nu_LR": 0.360,
    "nu_LT": 0.346,
    "nu_RT": 0.373,
}
```

Then `solver.py` maps those ratios into the constants expected by
`OrthotropicElasticity`:

```python
def redwood_orthotropic_material(E_longitudinal):
    """Return orthotropic constants with wood axes R->x, T->y, and L->z."""
    ratios = REDWOOD_CLEAR_WOOD_RATIOS
    E_longitudinal = float(E_longitudinal)
    Ex = ratios["E_R_over_E_L"] * E_longitudinal
    Ey = ratios["E_T_over_E_L"] * E_longitudinal
    Ez = E_longitudinal
    return OrthotropicElasticity(
        Ex=Ex,
        Ey=Ey,
        Ez=Ez,
        nuxy=ratios["nu_RT"],
        nuxz=ratios["nu_LR"] * Ex / Ez,
        nuyz=ratios["nu_LT"] * Ey / Ez,
        Gxy=ratios["G_RT_over_E_L"] * E_longitudinal,
        Gyz=ratios["G_LT_over_E_L"] * E_longitudinal,
        Gxz=ratios["G_LR_over_E_L"] * E_longitudinal,
    )
```

The important point is that `OrthotropicElasticity` builds the compliance
matrix first:

$$
S=
\begin{bmatrix}
1/E_x & -\nu_{xy}/E_x & -\nu_{xz}/E_x & 0 & 0 & 0\\
-\nu_{xy}/E_x & 1/E_y & -\nu_{yz}/E_y & 0 & 0 & 0\\
-\nu_{xz}/E_x & -\nu_{yz}/E_y & 1/E_z & 0 & 0 & 0\\
0 & 0 & 0 & 1/G_{xy} & 0 & 0\\
0 & 0 & 0 & 0 & 1/G_{yz} & 0\\
0 & 0 & 0 & 0 & 0 & 1/G_{xz}
\end{bmatrix}.
$$

Then it inverts that matrix to obtain the elasticity matrix:

$$
D=S^{-1}.
$$

The strain and stress order is

```text
xx, yy, zz, xy, yz, xz
```

and the shear strain entries are engineering shear strains. The code also
checks that both the compliance matrix and the inverted elasticity matrix are
positive definite. That is a useful guardrail because a bad orthotropic ratio
set can produce a mathematically invalid stiffness matrix.

## Three-Point Gauss Integration

The beam region defaults to

```python
gauss_order=3
```

and then obtains the one-dimensional points and weights with

```python
self.gauss_points, self.gauss_weights = leggauss(self.gauss_order)
```

For a volume element, the stiffness integration is therefore

$$
K_e
=\int_{-1}^{1}\int_{-1}^{1}\int_{-1}^{1}
B^T D B\,\det(J)\,d\xi\,d\eta\,d\zeta
\approx
\sum_{i=1}^{3}\sum_{j=1}^{3}\sum_{k=1}^{3}
B_{ijk}^T D B_{ijk}\,w_iw_jw_k\,\det(J_{ijk}).
$$

So the element stiffness is sampled at 27 points per element. The source path is
`FEMHermiteBeamRegion.build_element_K`:

```python
def build_element_K(self, coords):
    Ke = np.zeros((48, 48))
    for i, xi in enumerate(self.gauss_points):
        for j, eta in enumerate(self.gauss_points):
            for k, zeta in enumerate(self.gauss_points):
                w = self.gauss_weights[i] * self.gauss_weights[j] * self.gauss_weights[k]
                B, detJ, _, _ = self.build_B_matrix(xi, eta, zeta, coords)
                Ke += B.T @ self.D @ B * w * detJ
    return Ke
```

The same one-dimensional Gauss rule is reused for the two coordinates on the
loaded end face, giving a $3\times 3$ surface integration.

## End-Face Traction Instead Of A Hand-Waved Point Load

The beam-theory target uses a concentrated end load $P$. The finite element
model turns that same total load into a uniform traction over the physical
end face:

$$
t_y=\frac{P}{A_f}=\frac{-12.8}{4\cdot 8}=-0.4\;\text{lb/in}^2.
$$

For one element face at $\zeta=+1$, the consistent element load vector is

$$
F_e^{\text{face}}
=\int_{-1}^{1}\int_{-1}^{1}
N_{\text{disp}}^T\,t\,J_s\,d\xi\,d\eta,
$$

where

$$
t=\begin{bmatrix}0\\t_y\\0\end{bmatrix},
\qquad
J_s=\left\lVert
\frac{\partial x}{\partial \xi}\times
\frac{\partial x}{\partial \eta}
\right\rVert.
$$

In code, that surface Jacobian is the norm of the cross product of the two
physical tangent vectors on the selected face:

```python
def build_end_face_traction_load_vector(beam, total_load=P, load_dof=LOAD_DOF):
    force = np.zeros(beam.get_all_points().shape[0] * beam.ndof_per_node)
    face_area = beam.Lx * beam.Ly
    traction = total_load / face_area

    for elem_idx in beam.get_elements_at_max_z():
        coords = beam.get_element_nodes(elem_idx)
        dofs = beam.get_element_global_dofs(elem_idx).ravel()
        Fe = np.zeros(beam.ndof_per_node * 8)

        for i, xi in enumerate(beam.gauss_points):
            for j, eta in enumerate(beam.gauss_points):
                zeta = 1.0
                weight = beam.gauss_weights[i] * beam.gauss_weights[j]
                N_disp, _, _, _ = beam.get_hermite_displacement_matrices(
                    xi, eta, zeta, coords
                )
                J = beam.get_hermite_jacobian(xi, eta, zeta, coords)
                dx_dxi = J[0, :]
                dx_deta = J[1, :]
                detJs = np.linalg.norm(np.cross(dx_dxi, dx_deta))

                unit_traction = np.zeros(3)
                unit_traction[load_dof] = traction
                Fe += N_disp.T @ unit_traction * weight * detJs

        force[dofs] += Fe

    return force, beam.get_nodes_at_max_z(), traction
```

This is why the printed diagnostic says the solver load model is
`end-face traction integrated over z=L`. It is not merely dividing a point load
among nodes. The face integral distributes the load through the same Hermite
interpolation used by the displacement field.

The PyVista traction viewer makes this load integral visible.

<figure class="visual-figure">
  <img src="{{ '/assets/hermites-structural/hermite-end-face-traction-integration-viewer.png' | relative_url }}" alt="PyVista end-face traction integration viewer showing selected face, Gauss points, nodal labels, and load arrow">
  <figcaption>The end-face traction integration viewer. The red face is the selected $\zeta=+1$ face, the yellow dots are the surface Gauss points, and the arrow shows the transverse traction direction.</figcaption>
</figure>

Run it with:

```powershell
py view_end_face_traction_integration.py
```

Useful variants:

```powershell
py view_end_face_traction_integration.py --face 12
py view_end_face_traction_integration.py --screenshot outputs/end_face_traction_face_12.png --face 12
```

The viewer also prints the integrated load check:

```text
End-face traction integration
  integrated faces:       32
  total load requested:   -1.280000000000e+01 lb
  uniform traction:       -4.000000000000e-01 lb/in^2
  assembled component:    -1.280000000000e+01 lb
  component error:        near zero
```

The key fact is that the assembled finite element force in the loaded component
sums back to the requested total load.

## Solving The Linear System

Once the global stiffness and force vector are assembled, the fixed degrees of
freedom are all degrees of freedom on the `z = 0` end:

```python
def solve_with_force_vector(beam, force):
    stiffness = beam.build_global_K()
    fixed_dof = []

    for node in beam.get_nodes_at_min_z():
        fixed_dof.extend(beam.global_dofs[node])

    free_dof = [dof for dof in range(stiffness.shape[0]) if dof not in fixed_dof]
    solved_free = spsolve(
        stiffness[np.ix_(free_dof, free_dof)],
        force[free_dof],
    )

    displacement = np.zeros(stiffness.shape[0])
    displacement[free_dof] = solved_free
    return displacement
```

The free-end displacement reported by the tutorial is the largest-magnitude
`uy` value on the loaded end face:

```python
def free_end_uy(beam, U):
    U_by_node = U.reshape((-1, beam.ndof_per_node))
    end_nodes = beam.get_nodes_at_max_z()
    end_uy = U_by_node[end_nodes, LOAD_DOF]
    return end_uy[np.argmax(np.abs(end_uy))]
```

## Seed Solve: Same Reference E, Orthotropic 3D Model

Run the solver:

```powershell
py solver.py
```

The full expected console output is preserved as
[`assets/hermites-structural/solver_expected_output.txt`]({{ '/assets/hermites-structural/solver_expected_output.txt' | relative_url }}).

The opening printout confirms the model assumptions before the system is
solved:

```text
Theoretical displacement check (orthotropic seed):
  Solver load model: end-face traction integrated over z=L
  Material model: orthotropic Redwood/AWC D matrix
  Gauss integration order:              3-point
  Total P:                              -12.800 lb
  End face area:                        32.000 in^2
  End face traction:                    -0.400000 psi
  End nodes loaded:                     45
  Integrated load on end nodes:         -12.800000 lb
  Formula:                              delta = P L^3 / (3 E I)
  I:                                    170.666667 in^4
  AWC/reference E for target:           2000000.000 psi
  Solver orthotropic Ez:                2000000.000 psi
  Target theoretical free-end uy:       -2.160e-02 inches
  FEA displacement: pending solve
```

After the seed solve at $E_z=2{,}000{,}000$ psi, the result is

```text
FEA free-end uy:                      -1.815e-02 inches
Difference vs AWC/theory target:      15.966552%
FEA max displacement magnitude:       1.817e-02 inches
```

This is an important result. The seed model bends in the correct direction and
is in the right scale, but it is about 16% stiffer than the classical target.
That is not surprising: we are comparing a full 3D orthotropic Hermite solid,
with shear and rotational coupling behavior, against a compact
Euler-Bernoulli beam formula.

## Calibrated Longitudinal Modulus

Because this is a linear-elastic model, if all elastic and shear moduli scale
by the same factor, the stiffness matrix scales by that factor:

$$
K(\alpha E)=\alpha K(E).
$$

The displacement therefore scales inversely:

$$
u(\alpha E)=\frac{1}{\alpha}u(E).
$$

So if a seed solve gives $u_{\text{seed}}$ at $E_{\text{seed}}$, and the target
is $u_{\text{target}}$, the calibrated modulus is

$$
E_{\text{calibrated}}
=E_{\text{seed}}\frac{u_{\text{seed}}}{u_{\text{target}}}.
$$

This is exactly what `solver.py` does:

```python
def calibrated_longitudinal_E(seed_E, seed_fea_uy, target_uy=REFERENCE_TARGET_UY):
    """Return the positive Ez that makes linear FEA scaling hit target_uy."""
    seed_E = float(seed_E)
    seed_fea_uy = float(seed_fea_uy)
    target_uy = float(target_uy)
    if seed_E <= 0.0:
        raise ValueError("seed_E must be positive")
    if target_uy == 0.0:
        raise ValueError("target_uy must be nonzero")
    ratio = seed_fea_uy / target_uy
    if ratio <= 0.0:
        raise ValueError(
            "seed FEA displacement and target displacement must have the same sign "
            f"for positive E calibration; got seed={seed_fea_uy}, target={target_uy}"
        )
    return seed_E * ratio
```

The sign check matters. Both the seed displacement and target displacement are
negative in this run, so their ratio is positive and the calibrated modulus is
physically positive.

The solver prints:

```text
E calibration:
  seed Ez:                              2000000.000000 psi
  seed FEA uy:                          -1.815122484954e-02 in
  target uy:                            -2.160000000000e-02 in
  Formula:                              E_calibrated = E_seed * u_seed / u_target
  calibrated Ez:                        1680668.967550 psi
```

Numerically,

$$
E_{\text{calibrated}}
=2{,}000{,}000
\left(\frac{-1.815122484954\times10^{-2}}
{-2.160000000000\times10^{-2}}\right)
=1{,}680{,}668.967550\;\text{psi}.
$$

This calibrated value should be understood carefully. It is not replacing the
AWC/reference modulus used to define the theoretical target. It is a solver-side
stiffness adjustment that asks: what longitudinal modulus makes this particular
finite element model reproduce the chosen beam-theory displacement exactly?

## Calibrated Solve

The solver then rebuilds the orthotropic material with

$$
E_z=1{,}680{,}668.967550\;\text{psi}
$$

and scales the transverse and shear moduli by the same Redwood ratios. The
second solve reports:

```text
Theoretical displacement check (orthotropic calibrated):
  Solver load model: end-face traction integrated over z=L
  Material model: orthotropic Redwood/AWC D matrix
  Gauss integration order:              3-point
  Total P:                              -12.800 lb
  End face area:                        32.000 in^2
  End face traction:                    -0.400000 psi
  End nodes loaded:                     45
  Integrated load on end nodes:         -12.800000 lb
  Formula:                              delta = P L^3 / (3 E I)
  I:                                    170.666667 in^4
  AWC/reference E for target:           2000000.000 psi
  Solver orthotropic Ez:                1680668.968 psi
  Target theoretical free-end uy:       -2.160e-02 inches
  FEA free-end uy:                      -2.160e-02 inches
  Difference vs AWC/theory target:      0.000000%
  FEA max displacement magnitude:       2.163e-02 inches
```

This is the result the tutorial is organized around. The end-face load is
integrated, the orthotropic matrix is active, three-point Gauss integration is
active, and the calibrated model matches the target displacement to the printed
precision.

## Mesh Convergence Check For Displacement

One fair objection to any calibrated example is: maybe the modulus was tuned on
a mesh that had not converged yet. If that were true, the calibrated match could
be a mesh accident instead of a useful benchmark.

The cantilever mesh in `solver.py` is $5 \times 9 \times 121$ nodes. Since
the beam dimensions are $4 \times 8 \times 120$ inches, that is a roughly
one-inch Hex8 element size in all three directions. To check whether that mesh
is already stable for the displacement quantity being used in the calibration,
the same orthotropic seed solve was repeated on a uniform refinement ladder:
nominal 4-inch, 2-inch, and 1-inch elements.

| Nominal element size $h$ | Mesh nodes | Elements | DOF | Seed free-end $u_y$ at $E_z=2.0\times10^6$ psi (in) | Change from previous | $E_z$ needed to hit target (psi) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 in | $2 \times 3 \times 31$ | 60 | 1,116 | -1.808943903920e-2 | -- | 1,674,948.059185 |
| 2 in | $3 \times 5 \times 61$ | 480 | 5,490 | -1.813652178962e-2 | 0.260% | 1,679,307.573113 |
| 1 in, `solver.py` mesh | $5 \times 9 \times 121$ | 3,840 | 32,670 | -1.815122484954e-2 | 0.081% | 1,680,668.967550 |

The displacement is therefore already moving very little at the mesh used by
`solver.py`: the 2-inch to 1-inch refinement changes the seed free-end
$u_y$ by only about `0.081%`. A simple Richardson-style estimate from the
4-inch, 2-inch, and 1-inch sequence gives an apparent convergence order of
about `1.68` for this measured displacement and an extrapolated seed value of
approximately `-1.815790125587e-2` in. On that estimate, the current one-inch
mesh is about `0.037%` from the extrapolated displacement limit.

That does not claim every stress component and every boundary layer is already
mesh-independent. It is narrower and more useful than that: the specific
quantity used for the modulus calibration, the free-end transverse displacement,
is stable at the mesh density used in the tutorial. The calibrated modulus is
therefore not being anchored to a visibly drifting displacement result.

## Strain Spot Check

At the end, the solver prints a strain vector at element `1920`:

```text
Strain at element 1920:
  exx: 1.897116e-06
  eyy: 2.582799e-06
  ezz: -2.273759e-05
  exy: -1.585775e-07
  eyz: -7.942192e-06
  exz: 2.012386e-06
Saved displacement vector to U.npy
```

The strain order matches the six-component order used by the material matrix:

$$
\varepsilon =
\begin{bmatrix}
\varepsilon_{xx} &
\varepsilon_{yy} &
\varepsilon_{zz} &
\gamma_{xy} &
\gamma_{yz} &
\gamma_{xz}
\end{bmatrix}^T.
$$

This is not yet a full stress-validation section. It is a useful additional
sign that the solved displacement vector is being pushed back through the same
`B` matrix used by the stiffness assembly.

## What This Tutorial Proves

This tutorial proves several practical things about the repository:

1. The load has the correct sign and total magnitude.
2. The end-face traction integration sums back to the requested $P=-12.8$ lb.
3. The fixed face is the intended `z = 0` cantilever boundary.
4. The active material path is orthotropic, not accidentally isotropic.
5. The active integration order is 3-point Gauss.
6. The seed solve is close to the beam-theory displacement scale.
7. The calibrated solve exactly reproduces the target displacement by linear
   modulus scaling.

It does not prove that the full formulation is finished or universally
validated. A single cantilever displacement check cannot validate every stress,
rotation, boundary-condition, or mesh-refinement question. It is simply the
first disciplined checkpoint: units, sign, loading, stiffness scale, and solver
plumbing all have to be right before the more difficult tutorials are worth
trusting.

<div class="callout">
<strong>Baseline result:</strong> the tutorial target is
$u_y=-2.160\times10^{-2}$ in. The seed orthotropic solve gives
$u_y=-1.815\times10^{-2}$ in. The calibrated orthotropic solve gives
$u_y=-2.160\times10^{-2}$ in with $E_z=1.68066896755\times10^6$ psi.
</div>

## Commands To Reproduce This Tutorial

From the `HermiteStructural` repository root:

```powershell
py checkme.py
py check_orthotropic_elasticity.py
py solver.py
py view.py
py view_end_face_traction_integration.py
```

To capture the traction viewer screenshot:

```powershell
py view_end_face_traction_integration.py --face 0 --screenshot outputs/end_face_traction_face_0.png
```

The displacement vector saved by the solver is:

```text
U.npy
```

That file is what the displacement viewer uses after the solve finishes.
