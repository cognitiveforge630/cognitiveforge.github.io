# Hermite 01 — From Polynomials to Hermite Element Shape Functions

## Start with two endpoints

Imagine drawing a curve between two known points. The dots tell us where the curve must
pass. A slope tells us which way it must point as it leaves a point. Those are different
kinds of information. The graphs below use the same endpoint values, (0,0) and (1,1), so
the difference comes from the data each interpolation method uses.

<figure style="max-width:100%;margin:1.25rem auto;text-align:center;overflow-x:auto" class="tutorial-figure hermite-compare" aria-labelledby="hermite-compare-caption">
<svg width="100%" height="auto" style="max-width:100%;display:block;margin:auto" viewBox="0 0 920 400" role="img" aria-labelledby="hermite-svg-title hermite-svg-desc" xmlns="http://www.w3.org/2000/svg">
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
  <g stroke="#526778" stroke-width="1.5">
<line x1="100" y1="270" x2="100" y2="280"/>
<line x1="250" y1="270" x2="250" y2="280"/>
<line x1="400" y1="270" x2="400" y2="280"/>
<line x1="95" y1="275" x2="105" y2="275"/>
<line x1="95" y1="125" x2="105" y2="125"/>
</g>
  <g font-size="13" fill="#35566c" text-anchor="middle">
<text x="100" y="298">0</text>
<text x="250" y="298">0.5</text>
<text x="400" y="298">1</text>
</g>
  <g font-size="13" fill="#35566c" text-anchor="end">
<text x="89" y="130">1</text>
</g>
  <text x="411" y="293" font-size="14" fill="#35566c">x</text>
<text x="91" y="92" font-size="14" fill="#35566c">y</text>
  <circle cx="100" cy="275" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
<circle cx="400" cy="125" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <text x="105" y="264" font-size="13" fill="#17314b">(0, 0)</text>
<text x="355" y="116" font-size="13" fill="#17314b">(1, 1)</text>
  <text x="35" y="335" font-size="15" font-weight="700" fill="#17314b">p(x) = (1 − x)·0 + x·1 = x</text>
  <text x="35" y="360" font-size="14" fill="#35566c">Two nodal values determine this degree-one line.</text>
  <!-- Hermite axes use the same numerical scale and endpoint values. -->
  <line x1="540" y1="275" x2="885" y2="275" stroke="#526778" stroke-width="2"/>
  <line x1="565" y1="300" x2="565" y2="82" stroke="#526778" stroke-width="2"/>
  <path d="M 565 275 C 565 275, 865 125, 865 125" fill="none" stroke="#7454a5" stroke-width="5" stroke-linecap="round"/>
  <g stroke="#526778" stroke-width="1.5">
<line x1="565" y1="270" x2="565" y2="280"/>
<line x1="715" y1="270" x2="715" y2="280"/>
<line x1="865" y1="270" x2="865" y2="280"/>
<line x1="560" y1="275" x2="570" y2="275"/>
<line x1="560" y1="125" x2="570" y2="125"/>
</g>
  <g font-size="13" fill="#35566c" text-anchor="middle">
<text x="565" y="298">0</text>
<text x="715" y="298">0.5</text>
<text x="865" y="298">1</text>
</g>
  <g font-size="13" fill="#35566c" text-anchor="end">
<text x="554" y="130">1</text>
</g>
  <text x="876" y="293" font-size="14" fill="#35566c">x</text>
<text x="556" y="92" font-size="14" fill="#35566c">y</text>
  <circle cx="565" cy="275" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
<circle cx="865" cy="125" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <line x1="565" y1="275" x2="603" y2="275" stroke="#17835d" stroke-width="3"/>
<line x1="827" y1="125" x2="865" y2="125" stroke="#17835d" stroke-width="3"/>
  <text x="574" y="260" font-size="12" fill="#176b4d">slope 0</text>
<text x="816" y="111" font-size="12" fill="#176b4d">slope 0</text>
  <text x="500" y="335" font-size="15" font-weight="700" fill="#17314b">y(x) = 3x² − 2x³</text>
  <text x="500" y="360" font-size="14" fill="#35566c">Same endpoint values; both endpoint slopes are zero.</text>
  <text x="500" y="291" font-size="13" fill="#17314b">y(0) = 0</text>
<text x="800" y="147" font-size="13" fill="#17314b">y(1) = 1</text>
</svg>
<figcaption id="hermite-compare-caption">Both plots label x and y, mark 0, 0.5, and 1 on the horizontal axis, and mark 1 on the vertical axis. The shared origin is labeled once to keep it clear. The Lagrange example is the line through the two values; the Hermite example also matches zero slope at both endpoints, making a cubic that starts and finishes flat.</figcaption>
</figure>

In the left plot, x is the position where we want to find the curve's height. The
subscripts in x₀ and x₁ are just labels: x₀=0 is the first input position, and x₁=1 is
the second. They are not multiplication. The corresponding heights are y₀=0 and y₁=1, so
the two plotted data points are (x₀,y₀)=(0,0) and (x₁,y₁)=(1,1).

For these endpoints, the two Lagrange functions are L₀(x)=1-x and L₁(x)=x. They tell how
much each endpoint height contributes at the chosen position x: at the left endpoint
x=0, their values are 1 and 0; at the right endpoint x=1, their values are 0 and 1.

The interpolation rule multiplies each endpoint height by its function value, then adds
the two contributions:


```text
p(x) = y₀L₀(x) + y₁L₁(x)
     = 0(1 − x) + 1x
     = x
```


Here is each substitution: the general rule is p(x)=y₀L₀(x)+y₁L₁(x). In this example,
the left height is y₀=0 and its function is L₀(x)=1-x; the right height is y₁=1 and its
function is L₁(x)=x. Replacing those four pieces gives p(x)=0(1-x)+1x. The first product
is zero, and 1x=x, so the result is p(x)=x.

For a numerical example, choose x=0.25. This means we are one quarter of the way from
the left endpoint x₀=0 to the right endpoint x₁=1:


```text
L₀(0.25) = 1 − 0.25 = 0.75
L₁(0.25) = 0.25

p(0.25) = y₀L₀(0.25) + y₁L₁(0.25)
        = 0(0.75) + 1(0.25)
        = 0 + 0.25
        = 0.25
```


So at the input position x=0.25, the interpolated height is 0.25. The 0.75 and 0.25 are
the function values at that position; each is multiplied by its endpoint height before
the two contributions are added.

This particular Lagrange interpolant is linear because it uses two distinct nodes. **Not
all Lagrange polynomials are linear:** with three distinct nodes, the Lagrange
interpolant can be quadratic; with n+1 nodes, its degree is at most n (and can be lower
for special data).

In the right plot, x is the horizontal input and y(x) is the vertical height of the
curve. The left endpoint is at input x=0 and height y(0)=0; the right endpoint is at x=1
and height y(1)=1. The labels are shown beside those points. A prime means slope, so
y'(0)=0 and y'(1)=0 say the curve is flat at both endpoints. One cubic curve with those
four conditions is


```text
y(x) = 3x² − 2x³
y(0) = 0,  y(1) = 1,  y′(0) = y′(1) = 0
```


For two points, a line has two coefficients, so two values determine it. A cubic has
four coefficients, so it can satisfy four conditions: the value and slope at each
endpoint. The extra data let us control how the curve arrives at the points. For
example, changing the left slope tilts the curve as it leaves the left dot.

The two-point picture introduced values and slopes. Now use three reference support points: s₁ = −1, s₂ = 0, and s₃ = 1. First we derive the middle point's slope basis, then compare its value and slope bases, and then combine all six functions in the worked summation.

<div style="border:2px solid #4385b1;border-radius:10px;padding:1rem 1.2rem;margin:1.5rem 0;overflow-wrap:anywhere">
<h2>Where the slope-basis polynomial comes from</h2>
<p>Use three reference support points: <code>s₁ = −1</code>, <code>s₂ = 0</code>, and <code>s₃ = 1</code>. In <code>H₂,₁(s)</code>, H names a Hermite basis polynomial, the first subscript 2 selects the middle support point, the second subscript 1 selects slope data, and s is the input coordinate.</p>
<p>Call the middle point's slope basis <code>q(s) = H₂,₁(s)</code>. It must have zero value at all three points, zero slope at the two outside points, and unit slope at the middle point:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>q(−1) = q(0) = q(1) = 0
q′(−1) = 0,  q′(0) = 1,  q′(1) = 0</code></pre>
<p>At s = −1, both q and its slope are zero, so (s + 1) is a double factor. At s = 1, both are zero again, so (s − 1) is a double factor. The zero value at s = 0 adds a factor s. Therefore the degree-five polynomial has this form, with an unknown scale C:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>q(s) = C(s + 1)²s(s − 1)²
     = Cs(1 − s²)²</code></pre>
<p>Near s = 0, q(s) begins with Cs, so q′(0) = C. The required slope q′(0) = 1 therefore sets C = 1. The resulting polynomial is:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>H₂,₁(s) = q(s) = s(1 − s²)² = s − 2s³ + s⁵</code></pre>
<p>Differentiate to check the slopes at the three support points:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>H′₂,₁(s) = 1 − 6s² + 5s⁴
(H′₂,₁(−1), H′₂,₁(0), H′₂,₁(1)) = (0, 1, 0)</code></pre>
<p>The graph shows why this function dips below zero to the left and rises above zero to the right: it crosses all three support points at height zero but leaves the middle point with positive slope.</p>
<figure style="max-width:980px;margin:1rem auto;text-align:center;overflow-x:auto"><svg width="100%" height="auto" style="max-width:980px;display:block;margin:auto" viewBox="0 0 980 440" role="img" aria-labelledby="three-node-basis-title three-node-basis-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="three-node-basis-title">The two Hermite basis functions associated with the middle of three support points</title>
  <desc id="three-node-basis-desc">Across support points minus one, zero, and one, the value basis H two zero has heights zero, one, zero and zero slopes at all points. The slope basis H two one has zero heights at all three points and slopes zero, one, zero.</desc>
  <rect x="10" y="10" width="470" height="420" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <rect x="500" y="10" width="470" height="420" rx="16" fill="#f1f7fb" stroke="#cbd9e4"/>
  <text x="35" y="43" font-size="20" font-weight="700" fill="#17314b">i = 2: value basis H₂,₀(s)</text>
  <text x="525" y="43" font-size="20" font-weight="700" fill="#17314b">i = 2: slope basis H₂,₁(s)</text>
  <text x="35" y="67" font-size="14" fill="#526778">The middle node's value is 1; the other node values are 0.</text>
  <text x="525" y="67" font-size="14" fill="#526778">Only the middle node has slope 1; all three values are 0.</text>
  <line x1="105" y1="300" x2="415" y2="300" stroke="#526778" stroke-width="2"/>
  <line x1="105" y1="120" x2="105" y2="300" stroke="#526778" stroke-width="2"/>
  <line x1="555" y1="220" x2="865" y2="220" stroke="#526778" stroke-width="2"/>
  <line x1="555" y1="120" x2="555" y2="320" stroke="#526778" stroke-width="2"/>
  <g stroke="#a9bbc8" stroke-width="1.5" stroke-dasharray="4 5">
    <line x1="105" y1="120" x2="105" y2="300"/><line x1="260" y1="120" x2="260" y2="300"/><line x1="415" y1="120" x2="415" y2="300"/>
    <line x1="555" y1="120" x2="555" y2="320"/><line x1="710" y1="120" x2="710" y2="320"/><line x1="865" y1="120" x2="865" y2="320"/>
  </g>
  <path d="M105 300 C155 300 210 150 260 150 C310 150 365 300 415 300" fill="none" stroke="#1677a8" stroke-width="5" stroke-linecap="round"/>
  <path d="M555 220 C561.46 220, 567.92 225.73, 574.38 233.46 C580.83 241.19, 587.29 250.94, 593.75 260.20 C600.21 269.45, 606.67 278.21, 613.13 284.98 C619.58 291.76, 626.04 296.56, 632.50 298.75 C638.96 300.94, 645.42 300.52, 651.88 297.55 C658.33 294.57, 664.79 289.04, 671.25 281.52 C677.71 274.00, 684.17 264.50, 690.63 253.91 C697.08 243.33, 703.54 231.67, 710 220 C716.46 208.33, 722.92 196.67, 729.38 186.09 C735.83 175.50, 742.29 166.00, 748.75 158.48 C755.21 150.96, 761.67 145.43, 768.13 142.45 C774.58 139.48, 781.04 139.06, 787.50 141.25 C793.96 143.44, 800.42 148.24, 806.88 155.02 C813.33 161.79, 819.79 170.55, 826.25 179.80 C832.71 189.06, 839.17 198.81, 845.63 206.54 C852.08 214.27, 858.54 220, 865 220" fill="none" stroke="#7454a5" stroke-width="5" stroke-linecap="round"/>
  <g fill="#e26d42" stroke="white" stroke-width="3">
    <circle cx="105" cy="300" r="7"/><circle cx="260" cy="150" r="7"/><circle cx="415" cy="300" r="7"/>
    <circle cx="555" cy="220" r="7"/><circle cx="710" cy="220" r="7"/><circle cx="865" cy="220" r="7"/>
  </g>
  <g stroke="#17835d" stroke-width="3">
    <line x1="87" y1="300" x2="123" y2="300"/><line x1="242" y1="150" x2="278" y2="150"/><line x1="397" y1="300" x2="433" y2="300"/>
    <line x1="537" y1="220" x2="573" y2="220"/><line x1="694" y1="249" x2="726" y2="191"/><line x1="847" y1="220" x2="883" y2="220"/>
  </g>
  <g stroke="#526778" stroke-width="1.5">
    <line x1="100" y1="300" x2="110" y2="300"/><line x1="100" y1="210" x2="110" y2="210"/><line x1="100" y1="120" x2="110" y2="120"/>
    <line x1="550" y1="136" x2="560" y2="136"/><line x1="550" y1="220" x2="560" y2="220"/><line x1="550" y1="304" x2="560" y2="304"/>
    <line x1="105" y1="295" x2="105" y2="305"/><line x1="260" y1="295" x2="260" y2="305"/><line x1="415" y1="295" x2="415" y2="305"/>
    <line x1="555" y1="215" x2="555" y2="225"/><line x1="710" y1="215" x2="710" y2="225"/><line x1="865" y1="215" x2="865" y2="225"/>
  </g>
  <g font-size="12" fill="#35566c" text-anchor="end">
    <text x="94" y="124">1</text><text x="94" y="214">0.5</text><text x="94" y="304">0</text>
    <text x="544" y="140">0.3</text><text x="544" y="224">0</text><text x="544" y="308">−0.3</text>
  </g>
  <g font-size="12" fill="#35566c" text-anchor="middle">
    <text x="105" y="324">−1 (s₁)</text><text x="260" y="324">0 (s₂)</text><text x="415" y="324">1 (s₃)</text>
    <text x="555" y="244">−1 (s₁)</text><text x="710" y="244">0 (s₂)</text><text x="865" y="244">1 (s₃)</text>
  </g>
  <text x="408" y="344" font-size="13" fill="#35566c">s</text><text x="858" y="264" font-size="13" fill="#35566c">s</text>
  <text transform="translate(67 220) rotate(-90)" font-size="12" fill="#35566c">H₂,₀(s)</text>
  <text transform="translate(517 220) rotate(-90)" font-size="12" fill="#35566c">H₂,₁(s)</text>
  <text x="35" y="370" font-size="14" fill="#35566c">At s₁, s₂, s₃: values = 0, 1, 0</text>
  <text x="35" y="393" font-size="14" fill="#35566c">slopes = 0, 0, 0</text>
  <text x="525" y="370" font-size="14" fill="#35566c">At s₁, s₂, s₃: values = 0, 0, 0</text>
  <text x="525" y="393" font-size="14" fill="#35566c">slopes = 0, 1, 0</text>
  <text x="35" y="418" font-size="13" fill="#526778">Each j is one of the three marked support points; the red dots show the required values.</text>
</svg><figcaption>The purple middle-node slope basis is zero in height at each support point and has slope 1 at s₂ = 0. The blue value basis is shown for comparison.</figcaption></figure>
</div>

<div style="border:2px solid #4385b1;border-radius:10px;padding:1rem 1.2rem;margin:1.5rem 0;overflow-wrap:anywhere">
<h2>Two one-dimensional basis functions per support coordinate</h2>
<p><strong><em>At each support point sᵢ, we are given two scalar data: the field value u(sᵢ) and the slope u′(sᵢ). Both basis functions are scalar-valued polynomials: Hᵢ,₀ multiplies the value, while Hᵢ,₁ multiplies the slope.</em></strong> The slope basis is its own polynomial; it is not the derivative of the value basis.</p>
<p>A one-dimensional support point is one coordinate sᵢ on the reference line. It is not a three-dimensional node layout. In a hexahedron, a geometric support node is a triple such as (sᵢ, sⱼ, sₖ); the one-dimensional functions from the three coordinate directions are combined to form the 3D basis functions.</p>
<p>Each one-dimensional support point supplies two independent data: its field value u(sᵢ) and its first derivative u′(sᵢ). The value basis carries the value while making all other nodal values and slopes zero. The slope basis carries the slope while making every nodal value and all other nodal slopes zero. The first subscript i selects the support point; the second subscript 0 or 1 selects value or slope.</p>
<p>This graph turns on one middle-point input at a time. On the left, the middle value is 2 and every other datum is zero, so the curve is 2H₂,₀(s). On the right, the middle slope is 3 and every other datum is zero, so the curve is 3H₂,₁(s).</p>
<figure style="max-width:900px;margin:1rem auto;text-align:center;overflow-x:auto"><svg width="100%" height="auto" style="max-width:100%;display:block;margin:auto" viewBox="0 0 900 380" role="img" aria-labelledby="two-dofs-title two-dofs-desc" xmlns="http://www.w3.org/2000/svg">
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
  <g stroke="#526778" stroke-width="1.5">
<line x1="80" y1="275" x2="80" y2="285"/>
<line x1="230" y1="275" x2="230" y2="285"/>
<line x1="380" y1="275" x2="380" y2="285"/>
<line x1="530" y1="195" x2="530" y2="205"/>
<line x1="680" y1="195" x2="680" y2="205"/>
<line x1="830" y1="195" x2="830" y2="205"/>
</g>
  <g font-size="13" fill="#35566c" text-anchor="middle">
<text x="80" y="305">−1 (s₁)</text>
<text x="230" y="305">0 (s₂)</text>
<text x="380" y="305">1 (s₃)</text>
<text x="530" y="225">−1</text>
<text x="680" y="225">0</text>
<text x="830" y="225">1</text>
</g>
  <circle cx="230" cy="140" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
<circle cx="680" cy="200" r="7" fill="#e26d42" stroke="white" stroke-width="3"/>
  <line x1="212" y1="140" x2="248" y2="140" stroke="#17835d" stroke-width="3"/>
  <line x1="665" y1="226" x2="695" y2="174" stroke="#17835d" stroke-width="3"/>
  <text x="35" y="338" font-size="14" fill="#35566c">Height = 2 at s₂; slope there stays 0.</text>
  <text x="485" y="338" font-size="14" fill="#35566c">Height = 0 at all nodes; slope at s₂ is 3.</text>
</svg><figcaption>Changing the middle value raises the curve without tilting it at that point. Changing the middle slope tilts the curve while its height stays zero at all three support points.</figcaption></figure>
<p>Three support points therefore need 3 × 2 = 6 one-dimensional functions. In general, m support points need 2m such functions. In 3D, choose one value-or-slope function in each of the ξ, η, and ζ directions. Their 2 × 2 × 2 = 8 products correspond to the value, three first derivatives, three mixed second derivatives, and one mixed third derivative at a Hex support node.</p>
</div>

<div style="border:2px solid #4385b1;border-radius:10px;padding:1rem 1.2rem;margin:1.5rem 0;overflow-wrap:anywhere">
<h2>Worked example: three declared support points</h2>
<p>For the complete example, use the same three support points:</p>
<pre>
<code>s₁ = −1,    s₂ = 0,    s₃ = 1</code>
</pre>
<p>Here <code>s</code> is the horizontal input coordinate. Each <code>H</code> is a polynomial curve. <code>Hᵢ,₀(s)</code> carries a value at support point <code>i</code>: it equals 1 there, 0 at the other two points, and has zero slope at all three. <code>Hᵢ,₁(s)</code> carries a slope: its value is 0 at all three points, while its slope is 1 at point <code>i</code> and 0 at the others. The first subscript chooses a point; the second chooses value (0) or slope (1).</p>
<p>The triples below always follow the declared point order <code>(s₁, s₂, s₃) = (−1, 0, 1)</code>:</p>
<table style="width:100%;border-collapse:collapse">
<thead>
<tr>
<th style="border:1px solid #9db4c5;padding:.45rem">Basis polynomial*</th>
<th style="border:1px solid #9db4c5;padding:.45rem">Values at (s₁, s₂, s₃)</th>
<th style="border:1px solid #9db4c5;padding:.45rem">Slopes at (s₁, s₂, s₃)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₁,₀</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(1, 0, 0)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
</tr>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₁,₁</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(1, 0, 0)</td>
</tr>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₂,₀</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 1, 0)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
</tr>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₂,₁</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 1, 0)</td>
</tr>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₃,₀</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 1)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
</tr>
<tr>
<td style="border:1px solid #9db4c5;padding:.4rem">
<code>H₃,₁</code>
</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 0)</td>
<td style="border:1px solid #9db4c5;padding:.4rem">(0, 0, 1)</td>
</tr>
</tbody>
</table>
<p><strong>*Notation key:</strong> H names a Hermite basis polynomial. In <code>Hᵢ,ₐ(s)</code>, the first subscript i selects the support point; the second subscript a identifies the data type: a = 0 means value, and a = 1 means slope. The argument (s) tells which coordinate is being used. For example, <code>H₂,₀(s)</code> means “the middle support point's value basis, evaluated at coordinate s.”</p>
<p>The requirements above can also be read as this smaller value-only table. Each <strong>row is a basis function</strong>; each <strong>column is the coordinate where it is evaluated</strong>. It is a table of polynomial outputs, not a diagram of support points arranged in a row or grid:</p>
<table style="width:100%;table-layout:fixed;border-collapse:collapse">
<thead><tr><th style="border:1px solid #9db4c5;padding:.4rem">Value basis (row i)</th><th style="border:1px solid #9db4c5;padding:.4rem">At s₁ = −1 (j = 1)</th><th style="border:1px solid #9db4c5;padding:.4rem">At s₂ = 0 (j = 2)</th><th style="border:1px solid #9db4c5;padding:.4rem">At s₃ = 1 (j = 3)</th></tr></thead>
<tbody>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>H₁,₀</code></td><td style="border:1px solid #9db4c5;padding:.4rem">1</td><td style="border:1px solid #9db4c5;padding:.4rem">0</td><td style="border:1px solid #9db4c5;padding:.4rem">0</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>H₂,₀</code></td><td style="border:1px solid #9db4c5;padding:.4rem">0</td><td style="border:1px solid #9db4c5;padding:.4rem">1</td><td style="border:1px solid #9db4c5;padding:.4rem">0</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>H₃,₀</code></td><td style="border:1px solid #9db4c5;padding:.4rem">0</td><td style="border:1px solid #9db4c5;padding:.4rem">0</td><td style="border:1px solid #9db4c5;padding:.4rem">1</td></tr>
</tbody></table>
<p>For example, the middle row says <code>H₂,₀(s₁) = 0</code>, <code>H₂,₀(s₂) = 1</code>, and <code>H₂,₀(s₃) = 0</code>. At support point s₂, only the matching value input v₂ contributes to the sum. The slope basis functions have zero values at all three nodes; their matching slopes are selected by the derivative conditions.</p>
<p>These are the six polynomials that meet those requirements:</p>
<pre>
<code>H₁,₀(s) = ¼(3s + 4)s²(s − 1)²
H₁,₁(s) = ¼(s + 1)s²(s − 1)² H₂,₀(s) = (1 − s²)² H₂,₁(s) = s(1 − s²)² H₃,₀(s) = ¼(4 −
3s)s²(s + 1)²
H₃,₁(s) = ¼(s − 1)s²(s + 1)²</code>
</pre>
<p>Each panel graphs one polynomial over the interval. Red dots mark its values at the support points; green strokes show the tangent slopes. If the only nonzero input datum is value 1 at the middle point, the curve is <code>H₂,₀(s)</code>. If the only nonzero datum is slope 1 at the middle point, it is <code>H₂,₁(s)</code>.</p>
<figure style="max-width:1080px;margin:1rem auto;text-align:center;overflow-x:auto">
<svg width="100%" height="auto" style="max-width:1080px;display:block;margin:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 610" role="img" aria-labelledby="title desc">
<title id="title">All six cubic Hermite basis polynomials for support points minus one, zero, and one</title>
<desc id="desc">Six graphs show the value and slope basis polynomial for each of three support points. Red dots mark function values at the three nodes; green tangent marks show slopes.</desc>
<rect width="100%" height="100%" rx="14" fill="#f9fcfe"/>
<rect x="20" y="16" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="34" y="42" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₁,₀(s) — value basis</text>
<text x="34" y="64" font-family="Arial,sans-serif" font-size="14" fill="#35566c">¼(3s + 4)s²(s − 1)²</text>
<line x1="62" y1="223.97" x2="332" y2="223.97" stroke="#526778" stroke-width="1.5"/>
<line x1="197.00" y1="93" x2="197.00" y2="238" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="62.00,107.03 62.67,107.05 63.35,107.10 64.03,107.18 64.70,107.29 65.38,107.44 66.05,107.61 66.73,107.82
67.40,108.05 68.08,108.31 68.75,108.60 69.43,108.91 70.10,109.25 70.77,109.62 71.45,110.01 72.12,110.42
72.80,110.86 73.47,111.32 74.15,111.81 74.82,112.31 75.50,112.84 76.17,113.39 76.85,113.96 77.53,114.54
78.20,115.15 78.88,115.77 79.55,116.41 80.22,117.07 80.90,117.75 81.58,118.44 82.25,119.15 82.93,119.87
83.60,120.61 84.28,121.36 84.95,122.13 85.62,122.91 86.30,123.70 86.98,124.50 87.65,125.31 88.33,126.14
89.00,126.98 89.67,127.82 90.35,128.68 91.02,129.55 91.70,130.42 92.38,131.31 93.05,132.20 93.72,133.10
94.40,134.00 95.08,134.92 95.75,135.84 96.42,136.76 97.10,137.70 97.78,138.63 98.45,139.58 99.12,140.52
99.80,141.47 100.47,142.43 101.15,143.39 101.82,144.35 102.50,145.31 103.17,146.28 103.85,147.25 104.52,148.22
105.20,149.19 105.88,150.16 106.55,151.14 107.22,152.11 107.90,153.08 108.57,154.06 109.25,155.03 109.92,156.01
110.60,156.98 111.28,157.95 111.95,158.92 112.62,159.89 113.30,160.86 113.97,161.82 114.65,162.78 115.33,163.74
116.00,164.70 116.68,165.65 117.35,166.60 118.03,167.54 118.70,168.48 119.38,169.42 120.05,170.35 120.73,171.28
121.40,172.21 122.08,173.13 122.75,174.04 123.43,174.95 124.10,175.85 124.78,176.75 125.45,177.64 126.12,178.53
126.80,179.41 127.47,180.28 128.15,181.14 128.82,182.00 129.50,182.86 130.18,183.70 130.85,184.54 131.53,185.37
132.20,186.20 132.88,187.02 133.55,187.83 134.23,188.63 134.90,189.42 135.57,190.21 136.25,190.98 136.93,191.75
137.60,192.52 138.27,193.27 138.95,194.01 139.62,194.75 140.30,195.48 140.97,196.20 141.65,196.90 142.32,197.61
143.00,198.30 143.68,198.98 144.35,199.66 145.03,200.32 145.70,200.98 146.38,201.62 147.05,202.26 147.72,202.89
148.40,203.51 149.07,204.11 149.75,204.71 150.43,205.30 151.10,205.88 151.78,206.46 152.45,207.02 153.12,207.57
153.80,208.11 154.48,208.64 155.15,209.17 155.82,209.68 156.50,210.18 157.18,210.68 157.85,211.16 158.52,211.64
159.20,212.10 159.88,212.56 160.55,213.00 161.22,213.44 161.90,213.87 162.57,214.28 163.25,214.69 163.93,215.09
164.60,215.48 165.28,215.85 165.95,216.22 166.62,216.58 167.30,216.93 167.98,217.27 168.65,217.61 169.32,217.93
170.00,218.24 170.68,218.55 171.35,218.84 172.02,219.13 172.70,219.40 173.38,219.67 174.05,219.93 174.72,220.18
175.40,220.42 176.07,220.66 176.75,220.88 177.43,221.10 178.10,221.30 178.78,221.50 179.45,221.69 180.12,221.87
180.80,222.05 181.47,222.21 182.15,222.37 182.82,222.52 183.50,222.66 184.18,222.79 184.85,222.92 185.53,223.04
186.20,223.15 186.88,223.25 187.55,223.35 188.23,223.43 188.90,223.52 189.57,223.59 190.25,223.66 190.92,223.72
191.60,223.77 192.28,223.82 192.95,223.86 193.62,223.89 194.30,223.92 194.97,223.94 195.65,223.96 196.32,223.96
197.00,223.97 197.67,223.96 198.35,223.96 199.02,223.94 199.70,223.92 200.38,223.90 201.05,223.87 201.72,223.83
202.40,223.79 203.07,223.74 203.75,223.69 204.42,223.64 205.10,223.58 205.78,223.51 206.45,223.45 207.12,223.37
207.80,223.30 208.47,223.22 209.15,223.13 209.82,223.04 210.50,222.95 211.18,222.85 211.85,222.75 212.53,222.65
213.20,222.55 213.88,222.44 214.55,222.33 215.22,222.21 215.90,222.09 216.57,221.98 217.25,221.85 217.93,221.73
218.60,221.60 219.28,221.47 219.95,221.34 220.62,221.21 221.30,221.08 221.97,220.94 222.65,220.80 223.33,220.66
224.00,220.53 224.68,220.38 225.35,220.24 226.03,220.10 226.70,219.96 227.38,219.81 228.05,219.67 228.73,219.52
229.40,219.38 230.08,219.23 230.75,219.09 231.42,218.94 232.10,218.79 232.77,218.65 233.45,218.51 234.12,218.36
234.80,218.22 235.47,218.07 236.15,217.93 236.82,217.79 237.50,217.65 238.17,217.51 238.85,217.37 239.53,217.24
240.20,217.10 240.88,216.97 241.55,216.84 242.22,216.71 242.90,216.58 243.57,216.45 244.25,216.33 244.93,216.20
245.60,216.08 246.28,215.97 246.95,215.85 247.62,215.74 248.30,215.63 248.97,215.52 249.65,215.41 250.32,215.31
251.00,215.21 251.68,215.11 252.35,215.02 253.03,214.93 253.70,214.84 254.38,214.76 255.05,214.68 255.72,214.60
256.40,214.53 257.08,214.45 257.75,214.39 258.43,214.32 259.10,214.26 259.77,214.21 260.45,214.15 261.12,214.11
261.80,214.06 262.48,214.02 263.15,213.98 263.83,213.95 264.50,213.92 265.17,213.89 265.85,213.87 266.52,213.85
267.20,213.84 267.88,213.83 268.55,213.83 269.23,213.83 269.90,213.83 270.57,213.84 271.25,213.85 271.92,213.87
272.60,213.89 273.27,213.91 273.95,213.94 274.62,213.97 275.30,214.01 275.98,214.05 276.65,214.10 277.32,214.15
278.00,214.20 278.68,214.26 279.35,214.32 280.02,214.39 280.70,214.46 281.38,214.53 282.05,214.61 282.73,214.69
283.40,214.78 284.07,214.87 284.75,214.97 285.43,215.06 286.10,215.16 286.77,215.27 287.45,215.38 288.12,215.49
288.80,215.61 289.48,215.73 290.15,215.85 290.83,215.97 291.50,216.10 292.18,216.24 292.85,216.37 293.52,216.51
294.20,216.65 294.88,216.79 295.55,216.94 296.23,217.09 296.90,217.24 297.58,217.39 298.25,217.54 298.92,217.70
299.60,217.86 300.27,218.02 300.95,218.18 301.62,218.35 302.30,218.51 302.98,218.68 303.65,218.84 304.32,219.01
305.00,219.18 305.67,219.35 306.35,219.52 307.02,219.68 307.70,219.85 308.38,220.02 309.05,220.19 309.73,220.36
310.40,220.52 311.07,220.69 311.75,220.85 312.43,221.02 313.10,221.18 313.77,221.34 314.45,221.50 315.12,221.65
315.80,221.80 316.48,221.95 317.15,222.10 317.82,222.24 318.50,222.38 319.18,222.52 319.85,222.65 320.52,222.77
321.20,222.90 321.88,223.01 322.55,223.13 323.23,223.23 323.90,223.33 324.57,223.43 325.25,223.52 325.93,223.60
326.60,223.67 327.28,223.74 327.95,223.80 328.62,223.85 329.30,223.89 329.98,223.92 330.65,223.95 331.32,223.96
332.00,223.97" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="51.00" y1="107.03" x2="73.00" y2="107.03" stroke="#17835d" stroke-width="2.5"/>
<circle cx="62.00" cy="107.03" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="62.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="186.00" y1="223.97" x2="208.00" y2="223.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="197.00" cy="223.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="197.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="321.00" y1="223.97" x2="343.00" y2="223.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="332.00" cy="223.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="332.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="34" y="268" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<rect x="360" y="16" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="374" y="42" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₁,₁(s) — slope basis</text>
<text x="374" y="64" font-family="Arial,sans-serif" font-size="14" fill="#35566c">¼(s + 1)s²(s − 1)²</text>
<line x1="402" y1="165.50" x2="672" y2="165.50" stroke="#526778" stroke-width="1.5"/>
<line x1="537.00" y1="93" x2="537.00" y2="238" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="402.00,165.50 402.68,164.45 403.35,163.43 404.02,162.44 404.70,161.49 405.38,160.56 406.05,159.66 406.73,158.79
407.40,157.95 408.07,157.14 408.75,156.35 409.43,155.59 410.10,154.86 410.77,154.16 411.45,153.48 412.12,152.82
412.80,152.19 413.48,151.59 414.15,151.01 414.82,150.45 415.50,149.91 416.18,149.40 416.85,148.91 417.52,148.44
418.20,147.99 418.88,147.56 419.55,147.16 420.23,146.77 420.90,146.40 421.57,146.06 422.25,145.73 422.93,145.42
423.60,145.12 424.27,144.85 424.95,144.59 425.62,144.35 426.30,144.13 426.98,143.92 427.65,143.73 428.32,143.55
429.00,143.39 429.68,143.25 430.35,143.11 431.02,143.00 431.70,142.89 432.38,142.80 433.05,142.73 433.73,142.66
434.40,142.61 435.07,142.57 435.75,142.54 436.43,142.53 437.10,142.52 437.77,142.53 438.45,142.54 439.12,142.57
439.80,142.61 440.47,142.66 441.15,142.71 441.82,142.78 442.50,142.85 443.18,142.94 443.85,143.03 444.52,143.13
445.20,143.24 445.88,143.35 446.55,143.48 447.23,143.61 447.90,143.74 448.57,143.89 449.25,144.04 449.93,144.20
450.60,144.36 451.27,144.53 451.95,144.70 452.62,144.88 453.30,145.06 453.98,145.25 454.65,145.45 455.32,145.65
456.00,145.85 456.68,146.05 457.35,146.27 458.02,146.48 458.70,146.70 459.38,146.92 460.05,147.14 460.73,147.37
461.40,147.60 462.07,147.83 462.75,148.07 463.43,148.30 464.10,148.54 464.78,148.78 465.45,149.02 466.12,149.27
466.80,149.51 467.48,149.76 468.15,150.01 468.82,150.26 469.50,150.51 470.18,150.76 470.85,151.01 471.52,151.26
472.20,151.51 472.88,151.76 473.55,152.01 474.23,152.26 474.90,152.52 475.57,152.77 476.25,153.02 476.93,153.27
477.60,153.52 478.27,153.76 478.95,154.01 479.62,154.26 480.30,154.50 480.98,154.75 481.65,154.99 482.32,155.23
483.00,155.47 483.68,155.71 484.35,155.94 485.02,156.18 485.70,156.41 486.38,156.64 487.05,156.87 487.73,157.10
488.40,157.32 489.07,157.54 489.75,157.76 490.43,157.98 491.10,158.20 491.77,158.41 492.45,158.62 493.12,158.83
493.80,159.03 494.48,159.23 495.15,159.43 495.82,159.63 496.50,159.82 497.18,160.02 497.85,160.20 498.52,160.39
499.20,160.57 499.88,160.75 500.55,160.92 501.23,161.10 501.90,161.27 502.57,161.43 503.25,161.60 503.93,161.76
504.60,161.91 505.27,162.06 505.95,162.21 506.62,162.36 507.30,162.50 507.98,162.64 508.65,162.78 509.32,162.91
510.00,163.04 510.68,163.17 511.35,163.29 512.02,163.41 512.70,163.53 513.38,163.64 514.05,163.75 514.73,163.86
515.40,163.96 516.08,164.06 516.75,164.15 517.42,164.24 518.10,164.33 518.77,164.42 519.45,164.50 520.12,164.58
520.80,164.65 521.48,164.72 522.15,164.79 522.83,164.86 523.50,164.92 524.17,164.98 524.85,165.03 525.52,165.09
526.20,165.13 526.88,165.18 527.55,165.22 528.23,165.26 528.90,165.30 529.58,165.33 530.25,165.36 530.92,165.39
531.60,165.41 532.27,165.43 532.95,165.45 533.62,165.47 534.30,165.48 534.98,165.49 535.65,165.49 536.33,165.50
537.00,165.50 537.67,165.50 538.35,165.49 539.02,165.49 539.70,165.48 540.38,165.47 541.05,165.45 541.73,165.44
542.40,165.42 543.08,165.40 543.75,165.37 544.42,165.35 545.10,165.32 545.77,165.29 546.45,165.26 547.12,165.22
547.80,165.19 548.48,165.15 549.15,165.11 549.83,165.07 550.50,165.03 551.17,164.98 551.85,164.93 552.52,164.88
553.20,164.83 553.88,164.78 554.55,164.73 555.23,164.67 555.90,164.62 556.58,164.56 557.25,164.50 557.92,164.44
558.60,164.38 559.27,164.32 559.95,164.26 560.62,164.19 561.30,164.13 561.98,164.06 562.65,164.00 563.33,163.93
564.00,163.86 564.67,163.79 565.35,163.72 566.02,163.66 566.70,163.58 567.38,163.51 568.05,163.44 568.73,163.37
569.40,163.30 570.08,163.23 570.75,163.16 571.42,163.09 572.10,163.01 572.77,162.94 573.45,162.87 574.12,162.80
574.80,162.73 575.48,162.66 576.15,162.58 576.83,162.51 577.50,162.44 578.17,162.37 578.85,162.30 579.52,162.24
580.20,162.17 580.88,162.10 581.55,162.03 582.23,161.97 582.90,161.90 583.58,161.84 584.25,161.78 584.92,161.71
585.60,161.65 586.27,161.59 586.95,161.53 587.62,161.47 588.30,161.42 588.98,161.36 589.65,161.31 590.33,161.25
591.00,161.20 591.67,161.15 592.35,161.10 593.02,161.05 593.70,161.01 594.38,160.96 595.05,160.92 595.73,160.88
596.40,160.84 597.08,160.80 597.75,160.77 598.42,160.73 599.10,160.70 599.77,160.67 600.45,160.64 601.12,160.61
601.80,160.58 602.48,160.56 603.15,160.54 603.83,160.52 604.50,160.50 605.17,160.49 605.85,160.47 606.52,160.46
607.20,160.45 607.88,160.44 608.55,160.44 609.23,160.44 609.90,160.43 610.58,160.44 611.25,160.44 611.92,160.44
612.60,160.45 613.27,160.46 613.95,160.47 614.62,160.49 615.30,160.50 615.98,160.52 616.65,160.54 617.33,160.56
618.00,160.59 618.67,160.61 619.35,160.64 620.02,160.67 620.70,160.71 621.38,160.74 622.05,160.78 622.73,160.82
623.40,160.86 624.08,160.90 624.75,160.95 625.42,160.99 626.10,161.04 626.77,161.09 627.45,161.15 628.12,161.20
628.80,161.26 629.48,161.32 630.15,161.38 630.83,161.44 631.50,161.50 632.17,161.57 632.85,161.64 633.52,161.70
634.20,161.77 634.88,161.84 635.55,161.92 636.23,161.99 636.90,162.07 637.58,162.14 638.25,162.22 638.92,162.30
639.60,162.38 640.27,162.46 640.95,162.54 641.62,162.62 642.30,162.71 642.98,162.79 643.65,162.87 644.33,162.96
645.00,163.04 645.67,163.13 646.35,163.21 647.02,163.30 647.70,163.39 648.38,163.47 649.05,163.56 649.73,163.64
650.40,163.73 651.08,163.81 651.75,163.90 652.42,163.98 653.10,164.06 653.77,164.14 654.45,164.22 655.12,164.30
655.80,164.38 656.48,164.46 657.15,164.53 657.83,164.61 658.50,164.68 659.17,164.75 659.85,164.82 660.52,164.88
661.20,164.95 661.88,165.01 662.55,165.06 663.23,165.12 663.90,165.17 664.58,165.22 665.25,165.27 665.92,165.31
666.60,165.35 667.28,165.38 667.95,165.41 668.62,165.44 669.30,165.46 669.98,165.48 670.65,165.49 671.33,165.50
672.00,165.50" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="391.00" y1="148.13" x2="413.00" y2="182.87" stroke="#17835d" stroke-width="2.5"/>
<circle cx="402.00" cy="165.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="402.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="526.00" y1="165.50" x2="548.00" y2="165.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="537.00" cy="165.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="537.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="661.00" y1="165.50" x2="683.00" y2="165.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="672.00" cy="165.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="672.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="374" y="268" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<rect x="700" y="16" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="714" y="42" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₂,₀(s) — value basis</text>
<text x="714" y="64" font-family="Arial,sans-serif" font-size="14" fill="#35566c">(1 − s²)²</text>
<line x1="742" y1="223.97" x2="1012" y2="223.97" stroke="#526778" stroke-width="1.5"/>
<line x1="877.00" y1="93" x2="877.00" y2="238" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="742.00,223.97 742.67,223.96 743.35,223.92 744.02,223.86 744.70,223.78 745.38,223.68 746.05,223.56 746.73,223.41
747.40,223.25 748.08,223.06 748.75,222.86 749.42,222.63 750.10,222.38 750.77,222.12 751.45,221.83 752.12,221.53
752.80,221.21 753.48,220.87 754.15,220.51 754.83,220.14 755.50,219.75 756.17,219.34 756.85,218.91 757.52,218.47
758.20,218.02 758.88,217.54 759.55,217.06 760.23,216.56 760.90,216.04 761.58,215.51 762.25,214.96 762.92,214.40
763.60,213.83 764.27,213.25 764.95,212.65 765.62,212.04 766.30,211.42 766.98,210.78 767.65,210.14 768.33,209.48
769.00,208.81 769.67,208.13 770.35,207.44 771.02,206.75 771.70,206.04 772.38,205.32 773.05,204.59 773.73,203.85
774.40,203.10 775.08,202.35 775.75,201.59 776.42,200.81 777.10,200.04 777.77,199.25 778.45,198.45 779.12,197.65
779.80,196.85 780.48,196.03 781.15,195.21 781.83,194.38 782.50,193.55 783.17,192.72 783.85,191.87 784.52,191.02
785.20,190.17 785.88,189.31 786.55,188.45 787.23,187.59 787.90,186.72 788.58,185.85 789.25,184.97 789.92,184.09
790.60,183.21 791.27,182.32 791.95,181.43 792.62,180.55 793.30,179.65 793.98,178.76 794.65,177.86 795.33,176.97
796.00,176.07 796.67,175.17 797.35,174.27 798.02,173.37 798.70,172.47 799.38,171.57 800.05,170.67 800.73,169.77
801.40,168.87 802.08,167.98 802.75,167.08 803.42,166.18 804.10,165.29 804.77,164.39 805.45,163.50 806.12,162.61
806.80,161.72 807.48,160.83 808.15,159.95 808.83,159.07 809.50,158.19 810.17,157.32 810.85,156.44 811.52,155.57
812.20,154.71 812.88,153.85 813.55,152.99 814.23,152.13 814.90,151.28 815.58,150.44 816.25,149.60 816.92,148.76
817.60,147.93 818.27,147.10 818.95,146.28 819.62,145.46 820.30,144.65 820.98,143.84 821.65,143.04 822.33,142.25
823.00,141.46 823.67,140.68 824.35,139.90 825.02,139.13 825.70,138.36 826.38,137.61 827.05,136.86 827.73,136.11
828.40,135.38 829.08,134.65 829.75,133.93 830.42,133.21 831.10,132.51 831.77,131.81 832.45,131.11 833.12,130.43
833.80,129.75 834.48,129.09 835.15,128.43 835.83,127.78 836.50,127.13 837.17,126.50 837.85,125.87 838.52,125.26
839.20,124.65 839.88,124.05 840.55,123.46 841.23,122.88 841.90,122.31 842.58,121.75 843.25,121.19 843.92,120.65
844.60,120.12 845.27,119.59 845.95,119.08 846.62,118.57 847.30,118.08 847.98,117.59 848.65,117.12 849.33,116.65
850.00,116.20 850.67,115.76 851.35,115.32 852.02,114.90 852.70,114.49 853.38,114.08 854.05,113.69 854.73,113.31
855.40,112.94 856.08,112.58 856.75,112.24 857.42,111.90 858.10,111.57 858.77,111.26 859.45,110.95 860.12,110.66
860.80,110.38 861.48,110.10 862.15,109.84 862.83,109.60 863.50,109.36 864.17,109.13 864.85,108.92 865.52,108.72
866.20,108.52 866.88,108.34 867.55,108.18 868.23,108.02 868.90,107.87 869.58,107.74 870.25,107.62 870.92,107.51
871.60,107.41 872.27,107.32 872.95,107.24 873.62,107.18 874.30,107.13 874.98,107.08 875.65,107.06 876.33,107.04
877.00,107.03 877.67,107.04 878.35,107.06 879.02,107.08 879.70,107.13 880.38,107.18 881.05,107.24 881.73,107.32
882.40,107.41 883.08,107.51 883.75,107.62 884.42,107.74 885.10,107.87 885.77,108.02 886.45,108.18 887.12,108.34
887.80,108.52 888.48,108.72 889.15,108.92 889.83,109.13 890.50,109.36 891.17,109.60 891.85,109.84 892.52,110.10
893.20,110.38 893.88,110.66 894.55,110.95 895.23,111.26 895.90,111.57 896.58,111.90 897.25,112.24 897.92,112.58
898.60,112.94 899.27,113.31 899.95,113.69 900.62,114.08 901.30,114.49 901.98,114.90 902.65,115.32 903.33,115.76
904.00,116.20 904.67,116.65 905.35,117.12 906.02,117.59 906.70,118.08 907.38,118.57 908.05,119.08 908.73,119.59
909.40,120.12 910.08,120.65 910.75,121.19 911.42,121.75 912.10,122.31 912.77,122.88 913.45,123.46 914.12,124.05
914.80,124.65 915.48,125.26 916.15,125.87 916.83,126.50 917.50,127.13 918.17,127.78 918.85,128.43 919.52,129.09
920.20,129.75 920.88,130.43 921.55,131.11 922.23,131.81 922.90,132.51 923.58,133.21 924.25,133.93 924.92,134.65
925.60,135.38 926.27,136.11 926.95,136.86 927.62,137.61 928.30,138.36 928.98,139.13 929.65,139.90 930.33,140.68
931.00,141.46 931.67,142.25 932.35,143.04 933.02,143.84 933.70,144.65 934.38,145.46 935.05,146.28 935.73,147.10
936.40,147.93 937.08,148.76 937.75,149.60 938.42,150.44 939.10,151.28 939.77,152.13 940.45,152.99 941.12,153.85
941.80,154.71 942.48,155.57 943.15,156.44 943.83,157.32 944.50,158.19 945.17,159.07 945.85,159.95 946.52,160.83
947.20,161.72 947.88,162.61 948.55,163.50 949.23,164.39 949.90,165.29 950.58,166.18 951.25,167.08 951.92,167.98
952.60,168.87 953.27,169.77 953.95,170.67 954.62,171.57 955.30,172.47 955.98,173.37 956.65,174.27 957.33,175.17
958.00,176.07 958.67,176.97 959.35,177.86 960.02,178.76 960.70,179.65 961.38,180.55 962.05,181.43 962.73,182.32
963.40,183.21 964.08,184.09 964.75,184.97 965.42,185.85 966.10,186.72 966.77,187.59 967.45,188.45 968.12,189.31
968.80,190.17 969.48,191.02 970.15,191.87 970.83,192.72 971.50,193.55 972.17,194.38 972.85,195.21 973.52,196.03
974.20,196.85 974.88,197.65 975.55,198.45 976.23,199.25 976.90,200.04 977.58,200.81 978.25,201.59 978.92,202.35
979.60,203.10 980.27,203.85 980.95,204.59 981.62,205.32 982.30,206.04 982.98,206.75 983.65,207.44 984.33,208.13
985.00,208.81 985.67,209.48 986.35,210.14 987.02,210.78 987.70,211.42 988.38,212.04 989.05,212.65 989.73,213.25
990.40,213.83 991.08,214.40 991.75,214.96 992.42,215.51 993.10,216.04 993.77,216.56 994.45,217.06 995.12,217.54
995.80,218.02 996.48,218.47 997.15,218.91 997.83,219.34 998.50,219.75 999.17,220.14 999.85,220.51 1000.52,220.87
1001.20,221.21 1001.88,221.53 1002.55,221.83 1003.23,222.12 1003.90,222.38 1004.58,222.63 1005.25,222.86
1005.92,223.06 1006.60,223.25 1007.28,223.41 1007.95,223.56 1008.62,223.68 1009.30,223.78 1009.98,223.86
1010.65,223.92 1011.33,223.96 1012.00,223.97" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="731.00" y1="223.97" x2="753.00" y2="223.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="742.00" cy="223.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="742.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="866.00" y1="107.03" x2="888.00" y2="107.03" stroke="#17835d" stroke-width="2.5"/>
<circle cx="877.00" cy="107.03" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="877.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="1001.00" y1="223.97" x2="1023.00" y2="223.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="1012.00" cy="223.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="1012.00" y="256" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="714" y="268" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<rect x="20" y="296" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="34" y="322" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₂,₁(s) — slope basis</text>
<text x="34" y="344" font-family="Arial,sans-serif" font-size="14" fill="#35566c">s(1 − s²)²</text>
<line x1="62" y1="445.50" x2="332" y2="445.50" stroke="#526778" stroke-width="1.5"/>
<line x1="197.00" y1="373" x2="197.00" y2="518" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="62.00,445.50 62.67,445.52 63.35,445.58 64.03,445.69 64.70,445.83 65.38,446.01 66.05,446.22 66.73,446.47
67.40,446.76 68.08,447.08 68.75,447.43 69.43,447.81 70.10,448.22 70.77,448.65 71.45,449.12 72.12,449.61
72.80,450.13 73.47,450.67 74.15,451.23 74.82,451.82 75.50,452.43 76.17,453.06 76.85,453.70 77.53,454.37
78.20,455.05 78.88,455.75 79.55,456.46 80.22,457.19 80.90,457.93 81.58,458.69 82.25,459.46 82.93,460.24
83.60,461.02 84.28,461.82 84.95,462.63 85.62,463.44 86.30,464.27 86.98,465.09 87.65,465.93 88.33,466.77
89.00,467.61 89.67,468.45 90.35,469.30 91.02,470.15 91.70,471.01 92.38,471.86 93.05,472.71 93.72,473.56
94.40,474.41 95.08,475.26 95.75,476.11 96.42,476.95 97.10,477.80 97.78,478.63 98.45,479.46 99.12,480.29
99.80,481.11 100.47,481.92 101.15,482.73 101.82,483.53 102.50,484.32 103.17,485.11 103.85,485.88 104.52,486.65
105.20,487.41 105.88,488.15 106.55,488.89 107.22,489.62 107.90,490.33 108.57,491.03 109.25,491.72 109.92,492.40
110.60,493.07 111.28,493.72 111.95,494.36 112.62,494.99 113.30,495.60 113.97,496.20 114.65,496.78 115.33,497.35
116.00,497.90 116.68,498.44 117.35,498.97 118.03,499.47 118.70,499.96 119.38,500.44 120.05,500.89 120.73,501.34
121.40,501.76 122.08,502.17 122.75,502.56 123.43,502.93 124.10,503.28 124.78,503.62 125.45,503.94 126.12,504.24
126.80,504.52 127.47,504.79 128.15,505.04 128.82,505.26 129.50,505.47 130.18,505.66 130.85,505.83 131.53,505.99
132.20,506.12 132.88,506.24 133.55,506.33 134.23,506.41 134.90,506.47 135.57,506.51 136.25,506.53 136.93,506.53
137.60,506.51 138.27,506.47 138.95,506.42 139.62,506.34 140.30,506.25 140.97,506.14 141.65,506.00 142.32,505.85
143.00,505.68 143.68,505.50 144.35,505.29 145.03,505.06 145.70,504.82 146.38,504.55 147.05,504.27 147.72,503.97
148.40,503.66 149.07,503.32 149.75,502.97 150.43,502.60 151.10,502.21 151.78,501.80 152.45,501.38 153.12,500.93
153.80,500.48 154.48,500.00 155.15,499.51 155.82,499.00 156.50,498.47 157.18,497.93 157.85,497.37 158.52,496.80
159.20,496.21 159.88,495.61 160.55,494.99 161.22,494.35 161.90,493.70 162.57,493.03 163.25,492.35 163.93,491.66
164.60,490.95 165.28,490.23 165.95,489.49 166.62,488.74 167.30,487.98 167.98,487.21 168.65,486.42 169.32,485.62
170.00,484.80 170.68,483.98 171.35,483.14 172.02,482.29 172.70,481.44 173.38,480.57 174.05,479.69 174.72,478.79
175.40,477.89 176.07,476.98 176.75,476.06 177.43,475.13 178.10,474.19 178.78,473.25 179.45,472.29 180.12,471.33
180.80,470.36 181.47,469.38 182.15,468.39 182.82,467.40 183.50,466.40 184.18,465.39 184.85,464.38 185.53,463.36
186.20,462.34 186.88,461.31 187.55,460.28 188.23,459.24 188.90,458.20 189.57,457.16 190.25,456.11 190.92,455.06
191.60,454.00 192.28,452.94 192.95,451.89 193.62,450.82 194.30,449.76 194.97,448.70 195.65,447.63 196.32,446.57
197.00,445.50 197.67,444.43 198.35,443.37 199.02,442.30 199.70,441.24 200.38,440.18 201.05,439.11 201.72,438.06
202.40,437.00 203.07,435.94 203.75,434.89 204.42,433.84 205.10,432.80 205.78,431.76 206.45,430.72 207.12,429.69
207.80,428.66 208.47,427.64 209.15,426.62 209.82,425.61 210.50,424.60 211.18,423.60 211.85,422.61 212.53,421.62
213.20,420.64 213.88,419.67 214.55,418.71 215.22,417.75 215.90,416.81 216.57,415.87 217.25,414.94 217.93,414.02
218.60,413.11 219.28,412.21 219.95,411.31 220.62,410.43 221.30,409.56 221.97,408.71 222.65,407.86 223.33,407.02
224.00,406.20 224.68,405.38 225.35,404.58 226.03,403.79 226.70,403.02 227.38,402.26 228.05,401.51 228.73,400.77
229.40,400.05 230.08,399.34 230.75,398.65 231.42,397.97 232.10,397.30 232.77,396.65 233.45,396.01 234.12,395.39
234.80,394.79 235.47,394.20 236.15,393.63 236.82,393.07 237.50,392.53 238.17,392.00 238.85,391.49 239.53,391.00
240.20,390.52 240.88,390.07 241.55,389.62 242.22,389.20 242.90,388.79 243.57,388.40 244.25,388.03 244.93,387.68
245.60,387.34 246.28,387.03 246.95,386.73 247.62,386.45 248.30,386.18 248.97,385.94 249.65,385.71 250.32,385.50
251.00,385.32 251.68,385.15 252.35,385.00 253.03,384.86 253.70,384.75 254.38,384.66 255.05,384.58 255.72,384.53
256.40,384.49 257.08,384.47 257.75,384.47 258.43,384.49 259.10,384.53 259.77,384.59 260.45,384.67 261.12,384.76
261.80,384.88 262.48,385.01 263.15,385.17 263.83,385.34 264.50,385.53 265.17,385.74 265.85,385.96 266.52,386.21
267.20,386.48 267.88,386.76 268.55,387.06 269.23,387.38 269.90,387.72 270.57,388.07 271.25,388.44 271.92,388.83
272.60,389.24 273.27,389.66 273.95,390.11 274.62,390.56 275.30,391.04 275.98,391.53 276.65,392.03 277.32,392.56
278.00,393.10 278.68,393.65 279.35,394.22 280.02,394.80 280.70,395.40 281.38,396.01 282.05,396.64 282.73,397.28
283.40,397.93 284.07,398.60 284.75,399.28 285.43,399.97 286.10,400.67 286.77,401.38 287.45,402.11 288.12,402.85
288.80,403.59 289.48,404.35 290.15,405.12 290.83,405.89 291.50,406.68 292.18,407.47 292.85,408.27 293.52,409.08
294.20,409.89 294.88,410.71 295.55,411.54 296.23,412.37 296.90,413.20 297.58,414.05 298.25,414.89 298.92,415.74
299.60,416.59 300.27,417.44 300.95,418.29 301.62,419.14 302.30,419.99 302.98,420.85 303.65,421.70 304.32,422.55
305.00,423.39 305.67,424.23 306.35,425.07 307.02,425.91 307.70,426.73 308.38,427.56 309.05,428.37 309.73,429.18
310.40,429.98 311.07,430.76 311.75,431.54 312.43,432.31 313.10,433.07 313.77,433.81 314.45,434.54 315.12,435.25
315.80,435.95 316.48,436.63 317.15,437.30 317.82,437.94 318.50,438.57 319.18,439.18 319.85,439.77 320.52,440.33
321.20,440.87 321.88,441.39 322.55,441.88 323.23,442.35 323.90,442.78 324.57,443.19 325.25,443.57 325.93,443.92
326.60,444.24 327.28,444.53 327.95,444.78 328.62,444.99 329.30,445.17 329.98,445.31 330.65,445.42 331.32,445.48
332.00,445.50" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="51.00" y1="445.50" x2="73.00" y2="445.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="62.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="62.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="186.00" y1="428.13" x2="208.00" y2="462.87" stroke="#17835d" stroke-width="2.5"/>
<circle cx="197.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="197.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="321.00" y1="445.50" x2="343.00" y2="445.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="332.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="332.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="34" y="548" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<rect x="360" y="296" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="374" y="322" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₃,₀(s) — value basis</text>
<text x="374" y="344" font-family="Arial,sans-serif" font-size="14" fill="#35566c">¼(4 − 3s)s²(s + 1)²</text>
<line x1="402" y1="503.97" x2="672" y2="503.97" stroke="#526778" stroke-width="1.5"/>
<line x1="537.00" y1="373" x2="537.00" y2="518" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="402.00,503.97 402.68,503.96 403.35,503.95 404.02,503.92 404.70,503.89 405.38,503.85 406.05,503.80 406.73,503.74
407.40,503.67 408.07,503.60 408.75,503.52 409.43,503.43 410.10,503.33 410.77,503.23 411.45,503.13 412.12,503.01
412.80,502.90 413.48,502.77 414.15,502.65 414.82,502.52 415.50,502.38 416.18,502.24 416.85,502.10 417.52,501.95
418.20,501.80 418.88,501.65 419.55,501.50 420.23,501.34 420.90,501.18 421.57,501.02 422.25,500.85 422.93,500.69
423.60,500.52 424.27,500.36 424.95,500.19 425.62,500.02 426.30,499.85 426.98,499.68 427.65,499.52 428.32,499.35
429.00,499.18 429.68,499.01 430.35,498.84 431.02,498.68 431.70,498.51 432.38,498.35 433.05,498.18 433.73,498.02
434.40,497.86 435.07,497.70 435.75,497.54 436.43,497.39 437.10,497.24 437.77,497.09 438.45,496.94 439.12,496.79
439.80,496.65 440.47,496.51 441.15,496.37 441.82,496.24 442.50,496.10 443.18,495.97 443.85,495.85 444.52,495.73
445.20,495.61 445.88,495.49 446.55,495.38 447.23,495.27 447.90,495.16 448.57,495.06 449.25,494.97 449.93,494.87
450.60,494.78 451.27,494.69 451.95,494.61 452.62,494.53 453.30,494.46 453.98,494.39 454.65,494.32 455.32,494.26
456.00,494.20 456.68,494.15 457.35,494.10 458.02,494.05 458.70,494.01 459.38,493.97 460.05,493.94 460.73,493.91
461.40,493.89 462.07,493.87 462.75,493.85 463.43,493.84 464.10,493.83 464.78,493.83 465.45,493.83 466.12,493.83
466.80,493.84 467.48,493.85 468.15,493.87 468.82,493.89 469.50,493.92 470.18,493.95 470.85,493.98 471.52,494.02
472.20,494.06 472.88,494.11 473.55,494.15 474.23,494.21 474.90,494.26 475.57,494.32 476.25,494.39 476.93,494.45
477.60,494.53 478.27,494.60 478.95,494.68 479.62,494.76 480.30,494.84 480.98,494.93 481.65,495.02 482.32,495.11
483.00,495.21 483.68,495.31 484.35,495.41 485.02,495.52 485.70,495.63 486.38,495.74 487.05,495.85 487.73,495.97
488.40,496.08 489.07,496.20 489.75,496.33 490.43,496.45 491.10,496.58 491.77,496.71 492.45,496.84 493.12,496.97
493.80,497.10 494.48,497.24 495.15,497.37 495.82,497.51 496.50,497.65 497.18,497.79 497.85,497.93 498.52,498.07
499.20,498.22 499.88,498.36 500.55,498.51 501.23,498.65 501.90,498.79 502.57,498.94 503.25,499.09 503.93,499.23
504.60,499.38 505.27,499.52 505.95,499.67 506.62,499.81 507.30,499.96 507.98,500.10 508.65,500.24 509.32,500.38
510.00,500.53 510.68,500.66 511.35,500.80 512.02,500.94 512.70,501.08 513.38,501.21 514.05,501.34 514.73,501.47
515.40,501.60 516.08,501.73 516.75,501.85 517.42,501.98 518.10,502.09 518.77,502.21 519.45,502.33 520.12,502.44
520.80,502.55 521.48,502.65 522.15,502.75 522.83,502.85 523.50,502.95 524.17,503.04 524.85,503.13 525.52,503.22
526.20,503.30 526.88,503.37 527.55,503.45 528.23,503.51 528.90,503.58 529.58,503.64 530.25,503.69 530.92,503.74
531.60,503.79 532.27,503.83 532.95,503.87 533.62,503.90 534.30,503.92 534.98,503.94 535.65,503.96 536.33,503.96
537.00,503.97 537.67,503.96 538.35,503.96 539.02,503.94 539.70,503.92 540.38,503.89 541.05,503.86 541.73,503.82
542.40,503.77 543.08,503.72 543.75,503.66 544.42,503.59 545.10,503.52 545.77,503.43 546.45,503.35 547.12,503.25
547.80,503.15 548.48,503.04 549.15,502.92 549.83,502.79 550.50,502.66 551.17,502.52 551.85,502.37 552.52,502.21
553.20,502.05 553.88,501.87 554.55,501.69 555.23,501.50 555.90,501.30 556.58,501.10 557.25,500.88 557.92,500.66
558.60,500.42 559.27,500.18 559.95,499.93 560.62,499.67 561.30,499.40 561.98,499.13 562.65,498.84 563.33,498.55
564.00,498.24 564.67,497.93 565.35,497.61 566.02,497.27 566.70,496.93 567.38,496.58 568.05,496.22 568.73,495.85
569.40,495.48 570.08,495.09 570.75,494.69 571.42,494.28 572.10,493.87 572.77,493.44 573.45,493.00 574.12,492.56
574.80,492.10 575.48,491.64 576.15,491.16 576.83,490.68 577.50,490.18 578.17,489.68 578.85,489.17 579.52,488.64
580.20,488.11 580.88,487.57 581.55,487.02 582.23,486.46 582.90,485.88 583.58,485.30 584.25,484.71 584.92,484.11
585.60,483.51 586.27,482.89 586.95,482.26 587.62,481.62 588.30,480.98 588.98,480.32 589.65,479.66 590.33,478.98
591.00,478.30 591.67,477.61 592.35,476.90 593.02,476.20 593.70,475.48 594.38,474.75 595.05,474.01 595.73,473.27
596.40,472.52 597.08,471.75 597.75,470.98 598.42,470.21 599.10,469.42 599.77,468.63 600.45,467.83 601.12,467.02
601.80,466.20 602.48,465.37 603.15,464.54 603.83,463.70 604.50,462.86 605.17,462.00 605.85,461.14 606.52,460.28
607.20,459.41 607.88,458.53 608.55,457.64 609.23,456.75 609.90,455.85 610.58,454.95 611.25,454.04 611.92,453.13
612.60,452.21 613.27,451.28 613.95,450.35 614.62,449.42 615.30,448.48 615.98,447.54 616.65,446.60 617.33,445.65
618.00,444.70 618.67,443.74 619.35,442.78 620.02,441.82 620.70,440.86 621.38,439.89 622.05,438.92 622.73,437.95
623.40,436.98 624.08,436.01 624.75,435.03 625.42,434.06 626.10,433.08 626.77,432.11 627.45,431.14 628.12,430.16
628.80,429.19 629.48,428.22 630.15,427.25 630.83,426.28 631.50,425.31 632.17,424.35 632.85,423.39 633.52,422.43
634.20,421.47 634.88,420.52 635.55,419.58 636.23,418.63 636.90,417.70 637.58,416.76 638.25,415.84 638.92,414.92
639.60,414.00 640.27,413.10 640.95,412.20 641.62,411.31 642.30,410.42 642.98,409.55 643.65,408.68 644.33,407.82
645.00,406.98 645.67,406.14 646.35,405.31 647.02,404.50 647.70,403.70 648.38,402.91 649.05,402.13 649.73,401.36
650.40,400.61 651.08,399.87 651.75,399.15 652.42,398.44 653.10,397.75 653.77,397.07 654.45,396.41 655.12,395.77
655.80,395.15 656.48,394.54 657.15,393.96 657.83,393.39 658.50,392.84 659.17,392.31 659.85,391.81 660.52,391.32
661.20,390.86 661.88,390.42 662.55,390.01 663.23,389.62 663.90,389.25 664.58,388.91 665.25,388.60 665.92,388.31
666.60,388.05 667.28,387.82 667.95,387.61 668.62,387.44 669.30,387.29 669.98,387.18 670.65,387.10 671.33,387.05
672.00,387.03" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="391.00" y1="503.97" x2="413.00" y2="503.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="402.00" cy="503.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="402.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="526.00" y1="503.97" x2="548.00" y2="503.97" stroke="#17835d" stroke-width="2.5"/>
<circle cx="537.00" cy="503.97" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="537.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="661.00" y1="387.03" x2="683.00" y2="387.03" stroke="#17835d" stroke-width="2.5"/>
<circle cx="672.00" cy="387.03" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="672.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="374" y="548" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<rect x="700" y="296" width="320" height="260" rx="12" fill="#f1f7fb" stroke="#cbd9e4"/>
<text x="714" y="322" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17314b">H₃,₁(s) — slope basis</text>
<text x="714" y="344" font-family="Arial,sans-serif" font-size="14" fill="#35566c">¼(s − 1)s²(s + 1)²</text>
<line x1="742" y1="445.50" x2="1012" y2="445.50" stroke="#526778" stroke-width="1.5"/>
<line x1="877.00" y1="373" x2="877.00" y2="518" stroke="#9babb7" stroke-width="1" stroke-dasharray="3 4"/>
<polyline points="742.00,445.50 742.67,445.50 743.35,445.51 744.02,445.52 744.70,445.54 745.38,445.56 746.05,445.59 746.73,445.62
747.40,445.65 748.08,445.69 748.75,445.73 749.42,445.78 750.10,445.83 750.77,445.88 751.45,445.94 752.12,445.99
752.80,446.05 753.48,446.12 754.15,446.18 754.83,446.25 755.50,446.32 756.17,446.39 756.85,446.47 757.52,446.54
758.20,446.62 758.88,446.70 759.55,446.78 760.23,446.86 760.90,446.94 761.58,447.02 762.25,447.10 762.92,447.19
763.60,447.27 764.27,447.36 764.95,447.44 765.62,447.53 766.30,447.61 766.98,447.70 767.65,447.79 768.33,447.87
769.00,447.96 769.67,448.04 770.35,448.13 771.02,448.21 771.70,448.29 772.38,448.38 773.05,448.46 773.73,448.54
774.40,448.62 775.08,448.70 775.75,448.78 776.42,448.86 777.10,448.93 777.77,449.01 778.45,449.08 779.12,449.16
779.80,449.23 780.48,449.30 781.15,449.36 781.83,449.43 782.50,449.50 783.17,449.56 783.85,449.62 784.52,449.68
785.20,449.74 785.88,449.80 786.55,449.85 787.23,449.91 787.90,449.96 788.58,450.01 789.25,450.05 789.92,450.10
790.60,450.14 791.27,450.18 791.95,450.22 792.62,450.26 793.30,450.29 793.98,450.33 794.65,450.36 795.33,450.39
796.00,450.41 796.67,450.44 797.35,450.46 798.02,450.48 798.70,450.50 799.38,450.51 800.05,450.53 800.73,450.54
801.40,450.55 802.08,450.56 802.75,450.56 803.42,450.56 804.10,450.57 804.77,450.56 805.45,450.56 806.12,450.56
806.80,450.55 807.48,450.54 808.15,450.53 808.83,450.51 809.50,450.50 810.17,450.48 810.85,450.46 811.52,450.44
812.20,450.42 812.88,450.39 813.55,450.36 814.23,450.33 814.90,450.30 815.58,450.27 816.25,450.23 816.92,450.20
817.60,450.16 818.27,450.12 818.95,450.08 819.62,450.04 820.30,449.99 820.98,449.95 821.65,449.90 822.33,449.85
823.00,449.80 823.67,449.75 824.35,449.69 825.02,449.64 825.70,449.58 826.38,449.53 827.05,449.47 827.73,449.41
828.40,449.35 829.08,449.29 829.75,449.22 830.42,449.16 831.10,449.10 831.77,449.03 832.45,448.97 833.12,448.90
833.80,448.83 834.48,448.76 835.15,448.70 835.83,448.63 836.50,448.56 837.17,448.49 837.85,448.42 838.52,448.34
839.20,448.27 839.88,448.20 840.55,448.13 841.23,448.06 841.90,447.99 842.58,447.91 843.25,447.84 843.92,447.77
844.60,447.70 845.27,447.63 845.95,447.56 846.62,447.49 847.30,447.42 847.98,447.34 848.65,447.28 849.33,447.21
850.00,447.14 850.67,447.07 851.35,447.00 852.02,446.94 852.70,446.87 853.38,446.81 854.05,446.74 854.73,446.68
855.40,446.62 856.08,446.56 856.75,446.50 857.42,446.44 858.10,446.38 858.77,446.33 859.45,446.27 860.12,446.22
860.80,446.17 861.48,446.12 862.15,446.07 862.83,446.02 863.50,445.97 864.17,445.93 864.85,445.89 865.52,445.85
866.20,445.81 866.88,445.78 867.55,445.74 868.23,445.71 868.90,445.68 869.58,445.65 870.25,445.63 870.92,445.60
871.60,445.58 872.27,445.56 872.95,445.55 873.62,445.53 874.30,445.52 874.98,445.51 875.65,445.51 876.33,445.50
877.00,445.50 877.67,445.50 878.35,445.51 879.02,445.51 879.70,445.52 880.38,445.53 881.05,445.55 881.73,445.57
882.40,445.59 883.08,445.61 883.75,445.64 884.42,445.67 885.10,445.70 885.77,445.74 886.45,445.78 887.12,445.82
887.80,445.87 888.48,445.91 889.15,445.97 889.83,446.02 890.50,446.08 891.17,446.14 891.85,446.21 892.52,446.28
893.20,446.35 893.88,446.42 894.55,446.50 895.23,446.58 895.90,446.67 896.58,446.76 897.25,446.85 897.92,446.94
898.60,447.04 899.27,447.14 899.95,447.25 900.62,447.36 901.30,447.47 901.98,447.59 902.65,447.71 903.33,447.83
904.00,447.96 904.67,448.09 905.35,448.22 906.02,448.36 906.70,448.50 907.38,448.64 908.05,448.79 908.73,448.94
909.40,449.09 910.08,449.24 910.75,449.40 911.42,449.57 912.10,449.73 912.77,449.90 913.45,450.08 914.12,450.25
914.80,450.43 915.48,450.61 916.15,450.80 916.83,450.98 917.50,451.18 918.17,451.37 918.85,451.57 919.52,451.77
920.20,451.97 920.88,452.17 921.55,452.38 922.23,452.59 922.90,452.80 923.58,453.02 924.25,453.24 924.92,453.46
925.60,453.68 926.27,453.90 926.95,454.13 927.62,454.36 928.30,454.59 928.98,454.82 929.65,455.06 930.33,455.29
931.00,455.53 931.67,455.77 932.35,456.01 933.02,456.25 933.70,456.50 934.38,456.74 935.05,456.99 935.73,457.24
936.40,457.48 937.08,457.73 937.75,457.98 938.42,458.23 939.10,458.48 939.77,458.74 940.45,458.99 941.12,459.24
941.80,459.49 942.48,459.74 943.15,459.99 943.83,460.24 944.50,460.49 945.17,460.74 945.85,460.99 946.52,461.24
947.20,461.49 947.88,461.73 948.55,461.98 949.23,462.22 949.90,462.46 950.58,462.70 951.25,462.93 951.92,463.17
952.60,463.40 953.27,463.63 953.95,463.86 954.62,464.08 955.30,464.30 955.98,464.52 956.65,464.73 957.33,464.95
958.00,465.15 958.67,465.35 959.35,465.55 960.02,465.75 960.70,465.94 961.38,466.12 962.05,466.30 962.73,466.47
963.40,466.64 964.08,466.80 964.75,466.96 965.42,467.11 966.10,467.26 966.77,467.39 967.45,467.52 968.12,467.65
968.80,467.76 969.48,467.87 970.15,467.97 970.83,468.06 971.50,468.15 972.17,468.22 972.85,468.29 973.52,468.34
974.20,468.39 974.88,468.43 975.55,468.46 976.23,468.47 976.90,468.48 977.58,468.47 978.25,468.46 978.92,468.43
979.60,468.39 980.27,468.34 980.95,468.27 981.62,468.20 982.30,468.11 982.98,468.00 983.65,467.89 984.33,467.75
985.00,467.61 985.67,467.45 986.35,467.27 987.02,467.08 987.70,466.87 988.38,466.65 989.05,466.41 989.73,466.15
990.40,465.88 991.08,465.58 991.75,465.27 992.42,464.94 993.10,464.60 993.77,464.23 994.45,463.84 995.12,463.44
995.80,463.01 996.48,462.56 997.15,462.09 997.83,461.60 998.50,461.09 999.17,460.55 999.85,459.99 1000.52,459.41
1001.20,458.81 1001.88,458.18 1002.55,457.52 1003.23,456.84 1003.90,456.14 1004.58,455.41 1005.25,454.65
1005.92,453.86 1006.60,453.05 1007.28,452.21 1007.95,451.34 1008.62,450.44 1009.30,449.51 1009.98,448.56
1010.65,447.57 1011.33,446.55 1012.00,445.50" fill="none" stroke="#1677a8" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="731.00" y1="445.50" x2="753.00" y2="445.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="742.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="742.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₁</text>
<line x1="866.00" y1="445.50" x2="888.00" y2="445.50" stroke="#17835d" stroke-width="2.5"/>
<circle cx="877.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="877.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₂</text>
<line x1="1001.00" y1="428.13" x2="1023.00" y2="462.87" stroke="#17835d" stroke-width="2.5"/>
<circle cx="1012.00" cy="445.50" r="4.8" fill="#e26d42" stroke="white" stroke-width="2"/>
<text x="1012.00" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#35566c">s₃</text>
<text x="714" y="548" font-family="Arial,sans-serif" font-size="12" fill="#526778">Red = value; green = tangent slope</text>
<text x="540" y="599" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#526778">Reference coordinate s; support points s₁ = −1, s₂ = 0, s₃ = 1</text>
</svg>
<figcaption>All six basis polynomials for <code>s₁ = −1</code>, <code>s₂ = 0</code>, and <code>s₃ = 1</code>. Red dots mark values; green strokes show slopes.</figcaption>
</figure>
<p>The compact summation formula is:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>u(s) = Σ [vᵢ · Hᵢ,₀(s) + dᵢ · Hᵢ,₁(s)]    for i = 1, 2, 3</code></pre>
<h3>Symbol dictionary</h3>
<table style="width:100%;table-layout:fixed;border-collapse:collapse">
<thead><tr><th style="border:1px solid #9db4c5;padding:.4rem;width:24%">Symbol</th><th style="border:1px solid #9db4c5;padding:.4rem">Meaning and use</th></tr></thead>
<tbody>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>u(s)</code></td><td style="border:1px solid #9db4c5;padding:.4rem">The curve height we calculate at input coordinate s.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>s</code></td><td style="border:1px solid #9db4c5;padding:.4rem">The input coordinate where we ask for the height. We use s = 0.5 below.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>s₁, s₂, s₃</code></td><td style="border:1px solid #9db4c5;padding:.4rem">The support locations: −1, 0, and 1.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>i</code></td><td style="border:1px solid #9db4c5;padding:.4rem">The sum counter. It takes 1, then 2, then 3, adding one point's pair of contributions each time.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>vᵢ</code></td><td style="border:1px solid #9db4c5;padding:.4rem">Input height supplied at support point sᵢ.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>dᵢ</code></td><td style="border:1px solid #9db4c5;padding:.4rem">Input slope supplied at sᵢ, measured with respect to s.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>Hᵢ,₀(s)</code></td><td style="border:1px solid #9db4c5;padding:.4rem">Value basis curve for point i. It carries vᵢ and has zero slope at all support points.</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem"><code>Hᵢ,₁(s)</code></td><td style="border:1px solid #9db4c5;padding:.4rem">Slope basis curve for point i. It carries dᵢ while all support-point values remain zero.</td></tr>
</tbody></table>
<p>Each bracket groups one support point's contributions: input height × value basis, plus input slope × slope basis.</p>
<h3>Worked example: substitute every input</h3>
<p>Choose the following six input data:</p>
<table style="width:100%;table-layout:fixed;border-collapse:collapse">
<thead><tr><th style="border:1px solid #9db4c5;padding:.4rem">Point</th><th style="border:1px solid #9db4c5;padding:.4rem">Location</th><th style="border:1px solid #9db4c5;padding:.4rem">Input height</th><th style="border:1px solid #9db4c5;padding:.4rem">Input slope</th></tr></thead>
<tbody>
<tr><td style="border:1px solid #9db4c5;padding:.4rem">1</td><td style="border:1px solid #9db4c5;padding:.4rem">s₁ = −1</td><td style="border:1px solid #9db4c5;padding:.4rem">v₁ = 1</td><td style="border:1px solid #9db4c5;padding:.4rem">d₁ = 1</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem">2</td><td style="border:1px solid #9db4c5;padding:.4rem">s₂ = 0</td><td style="border:1px solid #9db4c5;padding:.4rem">v₂ = 2</td><td style="border:1px solid #9db4c5;padding:.4rem">d₂ = 2</td></tr>
<tr><td style="border:1px solid #9db4c5;padding:.4rem">3</td><td style="border:1px solid #9db4c5;padding:.4rem">s₃ = 1</td><td style="border:1px solid #9db4c5;padding:.4rem">v₃ = 3</td><td style="border:1px solid #9db4c5;padding:.4rem">d₃ = 3</td></tr>
</tbody></table>
<p>First substitute the heights and slopes from the table into the sum. Leave s unevaluated:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>u(s) = 1·H₁,₀(s) + 1·H₁,₁(s)
     + 2·H₂,₀(s) + 2·H₂,₁(s)
     + 3·H₃,₀(s) + 3·H₃,₁(s)</code></pre>
<p>Now evaluate this curve at s = 0.5. Substitute 0.5 into each basis polynomial:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>H₁,₀(0.5) = ¼(3·0.5 + 4)(0.5)²(0.5 − 1)² = 11/128
H₁,₁(0.5) = ¼(0.5 + 1)(0.5)²(0.5 − 1)² = 3/128
H₂,₀(0.5) = (1 − 0.5²)² = 72/128
H₂,₁(0.5) = 0.5(1 − 0.5²)² = 36/128
H₃,₀(0.5) = ¼(4 − 3·0.5)(0.5)²(0.5 + 1)² = 45/128
H₃,₁(0.5) = ¼(0.5 − 1)(0.5)²(0.5 + 1)² = −9/128</code></pre>
<p>Now replace each symbol in the sum with its declared input or evaluated basis value:</p>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>u(0.5) = [1·11/128 + 1·3/128]
       + [2·72/128 + 2·36/128]
       + [3·45/128 + 3·(−9/128)]
       = 14/128 + 216/128 + 108/128
       = 338/128 = 169/64 = 2.640625</code></pre>
<p>The first factor in each product comes from the input table (vᵢ or dᵢ). The fraction comes from evaluating the matching H curve at s = 0.5. Therefore the interpolated height at s = 0.5 is 2.640625.</p>
</div>

Now that all six functions are visible in a specific example, we can state the same
requirements for any number m of support points.

Label the m support points s₁,s₂,…,sₘ. The subscript tells us which point we mean.
Hermite interpolation builds two basis polynomials for each point: one for its value and
one for its slope. The first subscript i chooses which point's basis polynomials we are
building. The second subscript, 0 or 1, chooses value or slope.

To define a chosen basis polynomial, we must say what it does at every support point.
The index j runs through the points where we check it, so j=1,2,…,m. For example, with
three points and the middle point selected (i=2), j checks the first, middle, and last
points in turn. The middle value basis H₂,₀ must have values 0,1,0 there; the middle
slope basis H₂,₁ must have slopes 0,1,0 there.

Each basis polynomial has degree at most 2m-1, so it has 2m coefficients. The conditions
at all m points determine those coefficients:


```text
Hᵢ,₀(sⱼ) = δᵢⱼ       H′ᵢ,₀(sⱼ) = 0
Hᵢ,₁(sⱼ) = 0          H′ᵢ,₁(sⱼ) = δᵢⱼ
```


In the equation, i stays fixed while j checks every support point. The subscript 0 means
“value basis”; 1 means “slope basis.” The Kronecker delta is the on/off rule that gives
1 when the selected and checked point match, and 0 otherwise:


```text
δᵢⱼ = 1 when i = j; otherwise δᵢⱼ = 0.
```


For three points, the value-basis results form the 3×3 identity table in the worked-example box. Row i identifies the basis function; column j identifies where it is evaluated. This is the same zero/one pattern expressed by δᵢⱼ, not a spatial arrangement of nodes.

## Confluent Vandermonde construction

<div style="border:2px solid #4385b1;border-radius:10px;padding:1rem 1.2rem;margin:1.5rem 0;overflow-wrap:anywhere">
<p><strong>Purpose, in plain terms:</strong> Given m distinct support coordinates and a value plus a slope at each one, this method calculates the coefficients of the unique polynomial of degree at most 2m − 1 that matches all 2m numbers. The inputs are the support locations and prescribed values/slopes; the output is the polynomial's coefficients.</p>
<p><strong>How we use the result later:</strong> To build each basis polynomial, set its matching prescribed datum to 1 and all other values and slopes to 0, then solve for the coefficients. This produces Hᵢ,₀ and Hᵢ,₁. For actual input data, multiply each basis by its supplied value or slope and add the contributions, as in the worked summation above. In three dimensions, combine the one-dimensional bases by tensor products to form the Hex element shape functions.</p>
<p>The name <em>confluent Vandermonde</em> refers to the two rows created at every support coordinate: one row for the polynomial value and one for its slope, both at the same location.</p>
</div>

Write the polynomial using its coefficient vector:


```text
p(s) = c₀ + c₁s + … + c₂ₘ₋₁s^(2m−1)
c = [c₀, c₁, …, c₂ₘ₋₁]ᵀ
```


At support point s_i, evaluating the polynomial produces a row of powers.
Differentiating it first produces the slope row:


```text
Value row at sᵢ: [1, sᵢ, sᵢ², …, sᵢ^(2m−1)]
Slope row at sᵢ: [0, 1, 2sᵢ, …, (2m − 1)sᵢ^(2m−2)]
```


Stack one value row and one slope row for every support point. The resulting confluent
Vandermonde system connects the polynomial coefficients to all the nodal data:


```text
A c = d

A is made by stacking one value row and one slope row for each support point.
c = [c₀, c₁, …, c₂ₘ₋₁]ᵀ                         polynomial coefficients
d = [p(s₁), p′(s₁), …, p(sₘ), p′(sₘ)]ᵀ          values and slopes
```


In short, Ac=d, so solving for the coefficients gives c=A⁻¹d. The inverse turns the
requested values and slopes into the polynomial that matches them.

The companion implementation constructs this matrix in core/hermite_tensor/basis.py and
evaluates its basis and derivatives. It is maintained separately from the Lagrange
cardinal-product construction.

## Why these are Hermite functions

At each support point, one function returns unit value and zero slope while its paired
function returns zero value and unit slope. The interpolant therefore reproduces each
supplied value and slope exactly. Three or four points per direction create the support
grids for HermiteHex27 and HermiteHex64; each point has both kinds of one-dimensional
data.

## From these polynomials to Hermite element types

An element is built by turning interpolation rules into **shape functions**. A shape
function is a basis polynomial tied to one local degree of freedom (DOF): it is one for
that DOF and zero for the other nodal data. Then the element interpolant is the sum of
each DOF multiplied by its shape function. Lagrange elements attach values to nodes.
Hermite elements attach values **and derivatives** to nodes, so their basis must satisfy
both kinds of conditions.

For a two-node, one-dimensional cubic Hermite element with physical length L=x₂-x₁, use
the reference coordinate ξ=(x-x₁)/L. The four DOFs are the endpoint values u₁,u₂ and
physical slopes θ₁=du/dx|ₓ=ₓ_₁, θ₂=du/dx|ₓ=ₓ_₂. Its interpolation is


```text
u(ξ) = N₁(ξ)u₁ + N₂(ξ)θ₁ + N₃(ξ)u₂ + N₄(ξ)θ₂
```



```text
N₁(ξ) = 1 − 3ξ² + 2ξ³       N₂(ξ) = L(ξ − 2ξ² + ξ³)
N₃(ξ) = 3ξ² − 2ξ³           N₄(ξ) = L(−ξ² + ξ³)
```


N₁,N₃ carry endpoint values; N₂,N₄ carry endpoint slopes. The factors of L convert a
physical slope into a reference-coordinate polynomial coefficient. Evaluating u at
either endpoint returns that endpoint's value, and differentiating with respect to the
physical coordinate x returns the specified endpoint slopes. The plotted h(x)=3x²-2x³ is
exactly the value basis N₃ on a unit-length interval; it is the cubic that raises the
right endpoint value while keeping both endpoint slopes zero.

The same construction extends to the 3D element types in this tutorial. First choose
one-dimensional Hermite basis functions for the support points in each coordinate.
Tensor products combine them across x,y,z; at each support point the eight combinations
represent the value, three first derivatives, three mixed second derivatives, and one
mixed third derivative. Those combinations are the local DOFs used by `HermiteHex27` (a
3×3×3 support grid) and `HermiteHex64` (a 4×4×4 support grid). Thus the endpoint picture
explains the rule used to build every basis function: prescribe which nodal value or
derivative it carries, enforce zeros for the others, and combine the resulting
one-dimensional functions into the element basis.
