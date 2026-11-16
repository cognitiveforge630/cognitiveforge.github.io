---
layout: hermite-tutorial
title: "01 — From Polynomials to Hermite Element Shape Functions"
subtitle: "Interpolate both a value and a slope at every support point"
series: "Hermite Tensor Elements | Tutorial001"
family: Hermite
permalink: /tutorials/hermite/tutorial001/01-one-dimensional-hermite/
previous_lesson: /tutorials/hermite/tutorial001/
next_lesson: /tutorials/hermite/tutorial001/02-tensor-product-dofs/
comments: true
---
## Start with two endpoints

Imagine drawing a curve between two known points. The dots tell us where the curve must pass. A slope tells us which way it must point as it leaves a point. Those are different kinds of information. The graphs below use the same endpoint values, $(0,0)$ and $(1,1)$, so the difference comes from the data each interpolation method uses.

<figure class="tutorial-figure hermite-compare" aria-labelledby="hermite-compare-caption">
<svg viewBox="0 0 920 400" role="img" aria-labelledby="hermite-svg-title hermite-svg-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="hermite-svg-title">Lagrange values and Hermite values plus slopes</title>
  <desc id="hermite-svg-desc">On the left, two endpoint values determine a straight line. On the right, the same endpoint values and zero slopes determine a cubic curve that starts and ends flat.</desc>
  <rect x="10" y="10" width="435" height="380" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <rect x="475" y="10" width="435" height="380" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <text x="35" y="48" font-size="22" font-weight="700" fill="#17314b">Lagrange: values only</text>
  <text x="500" y="48" font-size="22" font-weight="700" fill="#17314b">Hermite: values + slopes</text>
  <!-- Lagrange axes: x ticks 0, 1/2, 1; y tick 1. The shared origin is labeled on x only. -->
  <line x1="75" y1="275" x2="420" y2="275" stroke="#526778" stroke-width="2"/>
  <line x1="100" y1="300" x2="100" y2="82" stroke="#526778" stroke-width="2"/>
  <path d="M 100 275 L 400 125" fill="none" stroke="#1677a8" stroke-width="5" stroke-linecap="round"/>
  <g stroke="#526778" stroke-width="1.5"><line x1="100" y1="270" x2="100" y2="280"/><line x1="250" y1="270" x2="250" y2="280"/><line x1="400" y1="270" x2="400" y2="280"/><line x1="95" y1="275" x2="105" y2="275"/><line x1="95" y1="125" x2="105" y2="125"/></g>
  <g font-size="13" fill="#35566c" text-anchor="middle"><text x="100" y="298">0</text><text x="250" y="298">0.5</text><text x="400" y="298">1</text></g>
  <g font-size="13" fill="#35566c" text-anchor="end"><text x="89" y="130">1</text></g>
  <text x="411" y="293" font-size="14" fill="#35566c">x</text><text x="91" y="92" font-size="14" fill="#35566c">y</text>
  <circle cx="100" cy="275" r="7" fill="#e26d42" stroke="white" stroke-width="3"/><circle cx="400" cy="125" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <text x="105" y="264" font-size="13" fill="#17314b">(0, 0)</text><text x="355" y="116" font-size="13" fill="#17314b">(1, 1)</text>
  <text x="35" y="335" font-size="15" font-weight="700" fill="#17314b">p(x) = (1 − x)·0 + x·1 = x</text>
  <text x="35" y="360" font-size="14" fill="#35566c">Two nodal values determine this degree-one line.</text>
  <!-- Hermite axes use the same numerical scale and endpoint values. -->
  <line x1="540" y1="275" x2="885" y2="275" stroke="#526778" stroke-width="2"/>
  <line x1="565" y1="300" x2="565" y2="82" stroke="#526778" stroke-width="2"/>
  <path d="M 565 275 C 565 275, 865 125, 865 125" fill="none" stroke="#7454a5" stroke-width="5" stroke-linecap="round"/>
  <g stroke="#526778" stroke-width="1.5"><line x1="565" y1="270" x2="565" y2="280"/><line x1="715" y1="270" x2="715" y2="280"/><line x1="865" y1="270" x2="865" y2="280"/><line x1="560" y1="275" x2="570" y2="275"/><line x1="560" y1="125" x2="570" y2="125"/></g>
  <g font-size="13" fill="#35566c" text-anchor="middle"><text x="565" y="298">0</text><text x="715" y="298">0.5</text><text x="865" y="298">1</text></g>
  <g font-size="13" fill="#35566c" text-anchor="end"><text x="554" y="130">1</text></g>
  <text x="876" y="293" font-size="14" fill="#35566c">x</text><text x="556" y="92" font-size="14" fill="#35566c">y</text>
  <circle cx="565" cy="275" r="7" fill="#e26d42" stroke="white" stroke-width="3"/><circle cx="865" cy="125" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <line x1="565" y1="275" x2="603" y2="275" stroke="#17835d" stroke-width="3"/><line x1="827" y1="125" x2="865" y2="125" stroke="#17835d" stroke-width="3"/>
  <text x="574" y="260" font-size="12" fill="#176b4d">slope 0</text><text x="816" y="111" font-size="12" fill="#176b4d">slope 0</text>
  <text x="500" y="335" font-size="15" font-weight="700" fill="#17314b">y(x) = 3x² − 2x³</text>
  <text x="500" y="360" font-size="14" fill="#35566c">Same endpoint values; both endpoint slopes are zero.</text>
  <text x="500" y="291" font-size="13" fill="#17314b">y(0) = 0</text><text x="800" y="147" font-size="13" fill="#17314b">y(1) = 1</text>
</svg>
<figcaption id="hermite-compare-caption">Both plots label x and y, mark 0, 0.5, and 1 on the horizontal axis, and mark 1 on the vertical axis. The shared origin is labeled once to keep it clear. The Lagrange example is the line through the two values; the Hermite example also matches zero slope at both endpoints, making a cubic that starts and finishes flat.</figcaption>
</figure>

In the left plot, $x$ is the position where we want to find the curve's height. The subscripts in $x_0$ and $x_1$ are just labels: $x_0=0$ is the first input position, and $x_1=1$ is the second. They are not multiplication. The corresponding heights are $y_0=0$ and $y_1=1$, so the two plotted data points are $(x_0,y_0)=(0,0)$ and $(x_1,y_1)=(1,1)$.

For these endpoints, the two Lagrange functions are $L_0(x)=1-x$ and $L_1(x)=x$. They tell how much each endpoint height contributes at the chosen position $x$: at the left endpoint $x=0$, their values are 1 and 0; at the right endpoint $x=1$, their values are 0 and 1.

The interpolation rule multiplies each endpoint height by its function value, then adds the two contributions:

$$
p(x)=y_0L_0(x)+y_1L_1(x)=0(1-x)+1x=x.
$$

Here is each substitution: the general rule is $p(x)=y_0L_0(x)+y_1L_1(x)$. In this example, the left height is $y_0=0$ and its function is $L_0(x)=1-x$; the right height is $y_1=1$ and its function is $L_1(x)=x$. Replacing those four pieces gives $p(x)=0(1-x)+1x$. The first product is zero, and $1x=x$, so the result is $p(x)=x$.

For a numerical example, choose $x=0.25$. This means we are one quarter of the way from the left endpoint $x_0=0$ to the right endpoint $x_1=1$:

$$
\begin{aligned}
L_0(0.25) &= 1-0.25 = 0.75,\\
L_1(0.25) &= 0.25,\\
p(0.25) &= y_0L_0(0.25)+y_1L_1(0.25)\\
         &= 0(0.75)+1(0.25)\\
         &= 0+0.25\\
         &= 0.25.
\end{aligned}
$$

So at the input position $x=0.25$, the interpolated height is $0.25$. The $0.75$ and $0.25$ are the function values at that position; each is multiplied by its endpoint height before the two contributions are added.

This particular Lagrange interpolant is linear because it uses two distinct nodes. **Not all Lagrange polynomials are linear:** with three distinct nodes, the Lagrange interpolant can be quadratic; with $n+1$ nodes, its degree is at most $n$ (and can be lower for special data).

In the right plot, $x$ is the horizontal input and $y(x)$ is the vertical height of the curve. The left endpoint is at input $x=0$ and height $y(0)=0$; the right endpoint is at $x=1$ and height $y(1)=1$. The labels are shown beside those points. A prime means slope, so $y'(0)=0$ and $y'(1)=0$ say the curve is flat at both endpoints. One cubic curve with those four conditions is

$$
y(x)=3x^2-2x^3,\qquad y(0)=0,\quad y(1)=1,\quad y'(0)=y'(1)=0.
$$

For two points, a line has two coefficients, so two values determine it. A cubic has four coefficients, so it can satisfy four conditions: the value and slope at each endpoint. The extra data let us control how the curve arrives at the points. For example, changing the left slope tilts the curve as it leaves the left dot.

The two-point picture introduces values and slopes. Now use three reference support points, $s_1=-1$, $s_2=0$, and $s_3=1$. First we derive the middle point's slope basis, then compare a value basis with a slope basis, and finally combine all six functions in a fully worked summation.

<section class="hs-calculation-box" markdown="1" aria-label="How the middle-node slope basis is constructed">

## Where the slope-basis polynomial comes from

Use the declared reference support points $s_1=-1$, $s_2=0$, and $s_3=1$. In $H_{2,1}(s)$, $H$ names a Hermite basis polynomial, the first subscript 2 selects the middle support point, the second subscript 1 selects slope data, and $s$ is the input coordinate.

The slope basis is a polynomial we construct to satisfy the slope conditions; it is **not** the derivative of the value-basis polynomial. For the middle node, call it $q(s)=H_{2,1}(s)$. Its job is to have zero value at all three nodes, zero slope at the two outside nodes, and unit slope at the middle node:

$$
q(-1)=q(0)=q(1)=0,
\qquad
q'(-1)=0,\quad q'(0)=1,\quad q'(1)=0.
$$

Here is how those conditions determine the polynomial. Since both $q$ and its slope are zero at $s=-1$ and $s=1$, those are double roots. The required value $q(0)=0$ adds a root at the middle. A degree-five polynomial with those roots must have this form, for some scale factor $C$:

$$
q(s)=C(s+1)^2s(s-1)^2=C s(1-s^2)^2.
$$

Near $s=0$, this polynomial begins as $q(s)=Cs+\text{higher powers of }s$, so its slope there is $q^{\prime}(0)=C$. The required unit slope makes $C=1$. Expanding gives the actual polynomial plotted on the right:

$$
\boxed{H_{2,1}(s)=s(1-s^2)^2=s-2s^3+s^5}.
$$

Differentiate it to check the three nodal slopes:

$$
H'_{2,1}(s)=1-6s^2+5s^4,
\qquad
\bigl(H'_{2,1}(-1),H'_{2,1}(0),H'_{2,1}(1)\bigr)=(0,1,0).
$$

So the graph has to cross zero at all three nodes, but leave the middle node with positive slope. That is why it dips below zero to the left and rises above zero to the right. In an interpolant, a supplied middle slope $m_2$ multiplies this function: $m_2H_{2,1}(s)$ contributes zero value at every node, but contributes exactly slope $m_2$ at $s_2=0$.

<figure class="tutorial-figure">
  <img src="{{ '/assets/img/tutorials/hermite/tutorial001/hermite-middle-node-basis-pair.svg' | relative_url }}" alt="Middle support point's value basis and slope basis plotted across support points minus one, zero, and one" loading="lazy">
  <figcaption>The blue curve is the middle value basis $H_{2,0}$; the purple curve is the middle slope basis $H_{2,1}$. Both have zero value at the outside support points. The value basis has unit height and zero slope at the middle point; the slope basis has zero height and unit slope there.</figcaption>
</figure>

</section>

<section class="hs-calculation-box" markdown="1" aria-label="Why each support point has a value and slope basis">

## Two one-dimensional basis functions per support coordinate

***At each support point $s_i$, we are given two scalar data: the field value $u(s_i)$ and the slope $u'(s_i)$. Both basis functions are scalar-valued polynomials: $H_{i,0}$ multiplies the value, while $H_{i,1}$ multiplies the slope.*** The slope basis is its own polynomial; it is not the derivative of the value basis.

Here, a *support point* means one node in the **one-dimensional interpolation rule**, at coordinate $s_i$. It does not mean a point belonging to a function. In the 3D hexahedron, a geometric support node is a coordinate triple $(s_i,s_j,s_k)$; the one-dimensional functions from the three coordinate directions are combined to make its 3D basis functions.

There are two one-dimensional functions for each coordinate $s_i$ because that node supplies **two independent kinds of data**: its field value $u(s_i)$ and its first derivative $u'(s_i)$. One basis function carries the value while making every other nodal value and slope zero. Its partner carries the slope while making every nodal value zero and all other nodal slopes zero. The index $i$ chooses the one-dimensional node; the final index 0 or 1 chooses whether its function carries value or slope data.

The graph below turns on one middle-node datum at a time. First set the middle value to 2 and every other nodal datum to zero. Then set the middle slope to 3 and every other nodal datum to zero. The polynomials act like separate controls: the value basis raises the curve at the node without tilting it; the slope basis tilts the curve through the node without changing its height.

<figure class="tutorial-figure" aria-labelledby="two-dofs-caption">
<svg viewBox="0 0 900 380" role="img" aria-labelledby="two-dofs-title two-dofs-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="two-dofs-title">Value and slope basis functions control different data at one support point</title>
  <desc id="two-dofs-desc">Two graph panels show the middle node of a three-node Hermite interpolant. The left panel shows twice the value basis, which is two at the middle node and flat there. The right panel shows three times the slope basis, which is zero in height at every node and has slope three at the middle node.</desc>
  <rect x="10" y="10" width="430" height="350" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <rect x="460" y="10" width="430" height="350" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <text x="35" y="45" font-size="19" font-weight="700" fill="#17314b">Turn on middle value: u(s₂) = 2</text>
  <text x="485" y="45" font-size="19" font-weight="700" fill="#17314b">Turn on middle slope: u′(s₂) = 3</text>
  <text x="35" y="72" font-size="14" fill="#35566c">2 H₂,₀(s) = 2(1 − s²)²</text>
  <text x="485" y="72" font-size="14" fill="#35566c">3 H₂,₁(s) = 3s(1 − s²)²</text>
  <line x1="80" y1="280" x2="380" y2="280" stroke="#526778" stroke-width="2"/>
  <line x1="80" y1="95" x2="80" y2="280" stroke="#526778" stroke-width="2"/>
  <line x1="530" y1="200" x2="830" y2="200" stroke="#526778" stroke-width="2"/>
  <line x1="530" y1="95" x2="530" y2="305" stroke="#526778" stroke-width="2"/>
  <path d="M80 280 C130 280 190 140 230 140 C270 140 330 280 380 280" fill="none" stroke="#1677a8" stroke-width="5" stroke-linecap="round"/>
  <path d="M530 200 C580 200 625 280 680 200 C735 120 780 200 830 200" fill="none" stroke="#7454a5" stroke-width="5" stroke-linecap="round"/>
  <g stroke="#526778" stroke-width="1.5"><line x1="80" y1="275" x2="80" y2="285"/><line x1="230" y1="275" x2="230" y2="285"/><line x1="380" y1="275" x2="380" y2="285"/><line x1="530" y1="195" x2="530" y2="205"/><line x1="680" y1="195" x2="680" y2="205"/><line x1="830" y1="195" x2="830" y2="205"/></g>
  <g font-size="13" fill="#35566c" text-anchor="middle"><text x="80" y="305">−1 (s₁)</text><text x="230" y="305">0 (s₂)</text><text x="380" y="305">1 (s₃)</text><text x="530" y="225">−1</text><text x="680" y="225">0</text><text x="830" y="225">1</text></g>
  <circle cx="230" cy="140" r="7" fill="#e26d42" stroke="white" stroke-width="3"/><circle cx="680" cy="200" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <line x1="212" y1="140" x2="248" y2="140" stroke="#17835d" stroke-width="3"/>
  <line x1="665" y1="226" x2="695" y2="174" stroke="#17835d" stroke-width="3"/>
  <text x="35" y="338" font-size="14" fill="#35566c">Height = 2 at s₂; slope there stays 0.</text>
  <text x="485" y="338" font-size="14" fill="#35566c">Height = 0 at all nodes; slope at s₂ is 3.</text>
</svg>
<figcaption id="two-dofs-caption">Each curve is the contribution from just one DOF, with the other nodal data set to zero. Add the two contributions to use both pieces of information: $u(s)=u(s_2)H_{2,0}(s)+u'(s_2)H_{2,1}(s)$, plus the contributions from the other support points. The green marks show the required tangent direction at the middle node.</figcaption>
</figure>

For these three one-dimensional coordinates there are $3\times2=6$ functions in total. In general, $m$ one-dimensional support coordinates with value and slope data require $2m$ one-dimensional basis functions. At a 3D Hex support node, choose one of the two functions in each direction and multiply the three choices. This gives $2\times2\times2=8$ tensor-product functions at the node, paired with its value, three first derivatives, three mixed second derivatives, and one mixed third derivative. For example, the center node of `HermiteHex27` uses the center-coordinate value/slope pair in each of $\xi$, $\eta$, and $\zeta$; their eight products are the eight scalar DOF shapes at that Hex node.
For three equally spaced points (-1,0,1), there are six functions and the polynomial degree is five. For four equally spaced points (-1,-1/3,1/3,1), there are eight functions and the degree is seven.

</section>

<section class="hs-calculation-box" markdown="1" aria-label="Worked Hermite example with three support points">

## Worked example: three declared support points

For the complete worked example, use the same three points on the reference line:

$$
s_1=-1,\qquad s_2=0,\qquad s_3=1.
$$

Here $s$ is the horizontal input coordinate. A Hermite basis function $H_{i,0}(s)$ is a polynomial curve that carries a value at support point $i$: it is 1 at that point, 0 at the other two, and has zero slope at all three. The companion $H_{i,1}(s)$ carries a slope: its value is 0 at all three points, and its slope is 1 at point $i$ and 0 at the others. The first index chooses a support point; the second chooses value (0) or slope (1).

For example, the table spells out all six jobs. The ordered triples always follow the declared point order $s_1=-1$, $s_2=0$, $s_3=1$:

| Basis polynomial* | Values at $(s_1,s_2,s_3)$ | Slopes at $(s_1,s_2,s_3)$ |
|---|---|---|
| $H_{1,0}$ | $(1,0,0)$ | $(0,0,0)$ |
| $H_{1,1}$ | $(0,0,0)$ | $(1,0,0)$ |
| $H_{2,0}$ | $(0,1,0)$ | $(0,0,0)$ |
| $H_{2,1}$ | $(0,0,0)$ | $(0,1,0)$ |
| $H_{3,0}$ | $(0,0,1)$ | $(0,0,0)$ |
| $H_{3,1}$ | $(0,0,0)$ | $(0,0,1)$ |

**Notation key (*):** $H$ names a Hermite basis polynomial. In $H_{i,a}(s)$, the first subscript $i$ selects the support point; the second subscript $a$ identifies the data type: $a=0$ means value, and $a=1$ means slope. The $(s)$ says which coordinate the polynomial is evaluated at. For example, $H_{2,0}(s)$ means “the middle support point's value basis, evaluated at coordinate $s$.”

The boxed requirements above can also be read as this smaller value-only table. Each **row is a basis function**; each **column is the coordinate where we evaluate it**. This is a table of polynomial outputs, not a picture of support points arranged in a row or grid:

| Value basis (row $i$) | At $s_1=-1$ ($j=1$) | At $s_2=0$ ($j=2$) | At $s_3=1$ ($j=3$) |
|---|---:|---:|---:|
| $H_{1,0}$ | 1 | 0 | 0 |
| $H_{2,0}$ | 0 | 1 | 0 |
| $H_{3,0}$ | 0 | 0 | 1 |

For instance, the middle row says $H_{2,0}(s_1)=0$, $H_{2,0}(s_2)=1$, and $H_{2,0}(s_3)=0$. Thus, when the summation is evaluated at the middle support point $s_2$, only its matching value input $v_2$ contributes. The slope-basis curves have zero values at all three points; their matching slopes are selected by the analogous derivative conditions.

The six polynomials that meet those requirements are:

$$
\begin{aligned}
H_{1,0}(s)&=\tfrac14(3s+4)s^2(s-1)^2,&
H_{1,1}(s)&=\tfrac14(s+1)s^2(s-1)^2,\\
H_{2,0}(s)&=(1-s^2)^2,&
H_{2,1}(s)&=s(1-s^2)^2,\\
H_{3,0}(s)&=\tfrac14(4-3s)s^2(s+1)^2,&
H_{3,1}(s)&=\tfrac14(s-1)s^2(s+1)^2.
\end{aligned}
$$

Each graph below shows one of these six polynomials over the whole interval. The red dots show its value at each support point. The green short lines show its tangent slope there. For instance, if the only nonzero input data are value 1 at the middle point, the interpolated curve is $H_{2,0}(s)$. If instead the only nonzero datum is slope 1 at the middle point, the curve is $H_{2,1}(s)$.

<figure class="tutorial-figure">
  <img src="{{ '/assets/img/tutorials/hermite/tutorial001/hermite-three-point-all-basis-functions.svg' | relative_url }}" alt="All six Hermite basis polynomials for support points minus one, zero, and one; each graph marks the three values and tangent slopes" loading="lazy">
  <figcaption>All six basis polynomials for the explicitly declared support points $s_1=-1$, $s_2=0$, and $s_3=1$. Red dots mark values; green tangent marks show slopes.</figcaption>
</figure>

For arbitrary prescribed values $v_i$ and slopes $d_i$ at these three points, the interpolating polynomial is the sum of each datum times its matching basis polynomial:

$$
u(s)=\sum_{i=1}^{3}\left[v_iH_{i,0}(s)+d_iH_{i,1}(s)\right].
$$

**Symbol dictionary**

| Symbol | Meaning and use |
|---|---|
| $u(s)$ | The interpolated curve's height at the input coordinate $s$. This is the result we calculate. |
| $s$ | The input coordinate where we want the curve's height. In the example below, we evaluate at $s=0.5$. |
| $s_i$ | Support point number $i$: here $s_1=-1$, $s_2=0$, and $s_3=1$. |
| $i$ | The summation counter. It takes the values 1, 2, then 3, adding one point's value and slope contributions each time. |
| $v_i$ | The height supplied at point $s_i$. It is input data, not something calculated by the sum. |
| $d_i$ | The supplied slope at point $s_i$, measured as derivative with respect to $s$. It is also input data. |
| $H_{i,0}(s)$ | The value basis curve for point $i$. It is 1 at $s_i$, 0 at the other support points, and has zero slope at all three. |
| $H_{i,1}(s)$ | The slope basis curve for point $i$. It is 0 at all three support points; its slope is 1 at $s_i$ and 0 at the others. |

The square brackets group the two contributions from one support point: its height times the value basis, plus its slope times the slope basis. The summation adds those brackets for points 1, 2, and 3.

**Worked summation with actual data**

Choose these input heights and slopes:

| Point | Coordinate $s_i$ | Input height $v_i$ | Input slope $d_i$ |
|---|---:|---:|---:|
| 1 | $s_1=-1$ | $v_1=1$ | $d_1=1$ |
| 2 | $s_2=0$ | $v_2=2$ | $d_2=2$ |
| 3 | $s_3=1$ | $v_3=3$ | $d_3=3$ |

First replace every input height and slope in the sum with the numbers from the data table. Leave $s$ unevaluated for now:

$$
\begin{aligned}
u(s)={}&1\cdot H_{1,0}(s)+1\cdot H_{1,1}(s)\\
&+2\cdot H_{2,0}(s)+2\cdot H_{2,1}(s)\\
&+3\cdot H_{3,0}(s)+3\cdot H_{3,1}(s).
\end{aligned}
$$

Now evaluate that curve at $s=0.5$. Substituting $s=0.5$ into each basis polynomial gives:

| Basis value | Substitute $s=0.5$ | Result |
|---|---|---:|
| $H_{1,0}(0.5)$ | $\frac14(3\cdot0.5+4)(0.5)^2(0.5-1)^2$ | $\frac{11}{128}$ |
| $H_{1,1}(0.5)$ | $\frac14(0.5+1)(0.5)^2(0.5-1)^2$ | $\frac{3}{128}$ |
| $H_{2,0}(0.5)$ | $(1-0.5^2)^2$ | $\frac{72}{128}$ |
| $H_{2,1}(0.5)$ | $0.5(1-0.5^2)^2$ | $\frac{36}{128}$ |
| $H_{3,0}(0.5)$ | $\frac14(4-3\cdot0.5)(0.5)^2(0.5+1)^2$ | $\frac{45}{128}$ |
| $H_{3,1}(0.5)$ | $\frac14(0.5-1)(0.5)^2(0.5+1)^2$ | $-\frac{9}{128}$ |

Now expand the summation. Each input height or slope is multiplied by the matching basis value from the table above:

$$
\begin{aligned}
u(0.5)={}&[v_1H_{1,0}(0.5)+d_1H_{1,1}(0.5)]\\
&+[v_2H_{2,0}(0.5)+d_2H_{2,1}(0.5)]\\
&+[v_3H_{3,0}(0.5)+d_3H_{3,1}(0.5)]\\
={}&[1\cdot\tfrac{11}{128}+1\cdot\tfrac{3}{128}]\\
&+[2\cdot\tfrac{72}{128}+2\cdot\tfrac{36}{128}]\\
&+[3\cdot\tfrac{45}{128}+3\cdot(-\tfrac{9}{128})]\\
={}&\tfrac{14}{128}+\tfrac{216}{128}+\tfrac{108}{128}\\
={}&\tfrac{338}{128}=\tfrac{169}{64}=2.640625.
\end{aligned}
$$

Therefore, for this chosen set of six input data, the interpolated curve has height $2.640625$ at $s=0.5$. The example shows every substitution: $v_1,v_2,v_3$ are replaced by $1,2,3$; $d_1,d_2,d_3$ are replaced by $1,2,3$; and each $H$ is replaced by its evaluated value at $0.5$.

</section>

Now that all six functions are visible in a specific example, we can state the same requirements for any number $m$ of support points.

Label the $m$ support points $s_1,s_2,\ldots,s_m$. The subscript tells us which point we mean. Hermite interpolation builds two basis polynomials for each point: one for its value and one for its slope. The first subscript $i$ chooses which point's basis polynomials we are building. The second subscript, 0 or 1, chooses value or slope.

To define a chosen basis polynomial, we must say what it does at every support point. The index $j$ runs through the points where we check it, so $j=1,2,\ldots,m$. For example, with three points and the middle point selected ($i=2$), $j$ checks the first, middle, and last points in turn. The middle value basis $H_{2,0}$ must have values $0,1,0$ there; the middle slope basis $H_{2,1}$ must have slopes $0,1,0$ there.

Each basis polynomial has degree at most $2m-1$, so it has $2m$ coefficients. The conditions at all $m$ points determine those coefficients:

$$
H_{i,0}(s_j)=\delta_{ij},\quad H'_{i,0}(s_j)=0,\qquad
H_{i,1}(s_j)=0,\quad H'_{i,1}(s_j)=\delta_{ij}.
$$

In the equation, $i$ stays fixed while $j$ checks every support point. The subscript 0 means “value basis”; 1 means “slope basis.” The Kronecker delta is the on/off rule that gives 1 when the selected and checked point match, and 0 otherwise. For three points, the value-basis results form the 3×3 identity table in the worked-example box: row $i$ identifies the basis function, and column $j$ identifies where it is evaluated.

$$
\delta_{ij}=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}
$$

## Confluent Vandermonde construction

<section class="hs-calculation-box" markdown="1" aria-label="Purpose of the confluent Vandermonde method">

**Purpose, in plain terms:** Given $m$ distinct support coordinates and a value plus a slope at each one, this method calculates the coefficients of the unique polynomial of degree at most $2m-1$ that matches all $2m$ numbers. The input is the support locations and the prescribed values/slopes; the output is the polynomial coefficients.

**How we use the result later:** First, set one prescribed datum to 1 and all the others to 0. Solving once for each such pattern produces the value and slope basis polynomials $H_{i,0}$ and $H_{i,1}$. Then multiply those basis polynomials by the actual values and slopes and add them, as in the worked summation above. In three dimensions, the one-dimensional bases are combined by tensor products to form the Hex element shape functions.

The method is called *confluent Vandermonde* because, at every support coordinate, it uses two rows at that same location: one row for the polynomial value and one for its slope.

</section>

Write the polynomial using its coefficient vector:

$$
p(s)=\sum_{k=0}^{2m-1}c_k s^k,
\qquad
\mathbf{c}=\begin{bmatrix}c_0&c_1&\cdots&c_{2m-1}\end{bmatrix}^{\mathsf T}.
$$

At support point $s_i$, evaluating the polynomial produces a row of powers. Differentiating it first produces the slope row:

$$
\begin{aligned}
\text{value row at }s_i &: \begin{bmatrix}1&s_i&s_i^2&\cdots&s_i^{2m-1}\end{bmatrix},\\
\text{slope row at }s_i &: \begin{bmatrix}0&1&2s_i&\cdots&(2m-1)s_i^{2m-2}\end{bmatrix}.
\end{aligned}
$$

Stack one value row and one slope row for every support point. The resulting confluent Vandermonde system connects the polynomial coefficients to all the nodal data:

$$
\underbrace{\begin{bmatrix}
1&s_1&s_1^2&\cdots&s_1^{2m-1}\\
0&1&2s_1&\cdots&(2m-1)s_1^{2m-2}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&s_m&s_m^2&\cdots&s_m^{2m-1}\\
0&1&2s_m&\cdots&(2m-1)s_m^{2m-2}
\end{bmatrix}}_{\mathbf{A}\;\text{(confluent Vandermonde)}}
\underbrace{\begin{bmatrix}c_0\\c_1\\\vdots\\c_{2m-1}\end{bmatrix}}_{\mathbf{c}\;\text{(polynomial coefficients)}}
=
\underbrace{\begin{bmatrix}p(s_1)\\p'(s_1)\\\vdots\\p(s_m)\\p'(s_m)\end{bmatrix}}_{\mathbf{d}\;\text{(values and slopes)}}.
$$

In short, $\mathbf{A}\mathbf{c}=\mathbf{d}$, so solving for the coefficients gives $\mathbf{c}=\mathbf{A}^{-1}\mathbf{d}$. The inverse turns the requested values and slopes into the polynomial that matches them.

The companion implementation constructs this matrix in core/hermite_tensor/basis.py and evaluates its basis and derivatives. It is maintained separately from the Lagrange cardinal-product construction.

## Why these are Hermite functions

At each support point, one function returns unit value and zero slope while its paired function returns zero value and unit slope. The interpolant therefore reproduces each supplied value and slope exactly. Three or four points per direction create the support grids for HermiteHex27 and HermiteHex64; each point has both kinds of one-dimensional data.

## From these polynomials to Hermite element types

An element is built by turning interpolation rules into **shape functions**. A shape function is a basis polynomial tied to one local degree of freedom (DOF): it is one for that DOF and zero for the other nodal data. Then the element interpolant is the sum of each DOF multiplied by its shape function. Lagrange elements attach values to nodes. Hermite elements attach values **and derivatives** to nodes, so their basis must satisfy both kinds of conditions.

For a two-node, one-dimensional cubic Hermite element with physical length $L=x_2-x_1$, use the reference coordinate $\xi=(x-x_1)/L$. The four DOFs are the endpoint values $u_1,u_2$ and physical slopes $\theta_1=\left.\frac{du}{dx}\right\vert_{x=x_1}$, $\theta_2=\left.\frac{du}{dx}\right\vert_{x=x_2}$. Its interpolation is

$$
u(\xi)=N_1(\xi)u_1+N_2(\xi)\theta_1+N_3(\xi)u_2+N_4(\xi)\theta_2,
$$

$$
\begin{aligned}
N_1(\xi)&=1-3\xi^2+2\xi^3, & N_2(\xi)&=L(\xi-2\xi^2+\xi^3),\\
N_3(\xi)&=3\xi^2-2\xi^3, & N_4(\xi)&=L(-\xi^2+\xi^3).
\end{aligned}
$$

$N_1,N_3$ carry endpoint values; $N_2,N_4$ carry endpoint slopes. The factors of $L$ convert a physical slope into a reference-coordinate polynomial coefficient. Evaluating $u$ at either endpoint returns that endpoint's value, and differentiating with respect to the physical coordinate $x$ returns the specified endpoint slopes. The plotted $h(x)=3x^2-2x^3$ is exactly the value basis $N_3$ on a unit-length interval; it is the cubic that raises the right endpoint value while keeping both endpoint slopes zero.

The same construction extends to the 3D element types in this tutorial. First choose one-dimensional Hermite basis functions for the support points in each coordinate. Tensor products combine them across $x,y,z$; at each support point the eight combinations represent the value, three first derivatives, three mixed second derivatives, and one mixed third derivative. Those combinations are the local DOFs used by `HermiteHex27` (a $3\times3\times3$ support grid) and `HermiteHex64` (a $4\times4\times4$ support grid). Thus the endpoint picture explains the rule used to build every basis function: prescribe which nodal value or derivative it carries, enforce zeros for the others, and combine the resulting one-dimensional functions into the element basis.
