"""Tutorial 01: draw the isoparametric Hex8 reference diagram.

This script is a PyVista reconstruction of the first conceptual figure:
an eight-node hexahedron with natural coordinates xi/eta/zeta and the
P1 nodal degrees of freedom u1, v1, w1 plus their rotations.

The P1-P8 order follows the Hex8 shape-function order currently used by
HermiteStructural:
    P1 (-1, -1, -1), P2 (+1, -1, -1), P3 (+1, +1, -1), P4 (-1, +1, -1)
    P5 (-1, -1, +1), P6 (+1, -1, +1), P7 (+1, +1, +1), P8 (-1, +1, +1)

Run:
    py tutorial_01_isoparametric_hexahedron.py

Optional:
    py tutorial_01_isoparametric_hexahedron.py --screenshot outputs/isoparametric_hexahedron_ground_zero.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pyvista as pv


CUBE_HALF_SIZE = 0.72
TEXT_FONT_FILE = Path("C:/Windows/Fonts/arial.ttf")
LABEL_WIPEOUT = {
    "shape": "rect",
    "fill_shape": True,
    "shape_color": "white",
    "shape_opacity": 0.86,
    "margin": 5,
}


def text_font_file() -> str | None:
    """Use a Unicode-capable font so VTK can render Greek labels."""
    return str(TEXT_FONT_FILE) if TEXT_FONT_FILE.exists() else None

NATURAL_COORDS = {
    "P1": (-1, -1, -1),
    "P2": (1, -1, -1),
    "P3": (1, 1, -1),
    "P4": (-1, 1, -1),
    "P5": (-1, -1, 1),
    "P6": (1, -1, 1),
    "P7": (1, 1, 1),
    "P8": (-1, 1, 1),
}

NODE_POINTS = {
    label: tuple(CUBE_HALF_SIZE * value for value in coords)
    for label, coords in NATURAL_COORDS.items()
}

XI_DIRECTION = np.array((1.0, 0.0, 0.0))
ETA_DIRECTION = np.array((0.0, 1.0, 0.0))
ZETA_DIRECTION = np.array((0.0, 0.0, 1.0))
P1_XI_DISPLAY_DIRECTION = -XI_DIRECTION
P1_ETA_DISPLAY_DIRECTION = -ETA_DIRECTION
P1_ZETA_DISPLAY_DIRECTION = -ZETA_DIRECTION

FACE_NODE_IDS = [
    ("P1", "P4", "P3", "P2"),
    ("P5", "P6", "P7", "P8"),
    ("P1", "P2", "P6", "P5"),
    ("P2", "P3", "P7", "P6"),
    ("P3", "P4", "P8", "P7"),
    ("P4", "P1", "P5", "P8"),
]


def as_array(name: str) -> np.ndarray:
    return np.array(NODE_POINTS[name], dtype=float)


def build_brick_faces() -> pv.PolyData:
    labels = list(NODE_POINTS)
    points = np.array([NODE_POINTS[label] for label in labels], dtype=float)
    label_to_index = {label: index for index, label in enumerate(labels)}

    faces = []
    for face in FACE_NODE_IDS:
        faces.extend([4, *(label_to_index[label] for label in face)])

    mesh = pv.PolyData(points, np.array(faces))
    mesh["z_height"] = points[:, 2]
    return mesh


def add_arrow(
    plotter: pv.Plotter,
    start: tuple[float, float, float] | np.ndarray,
    direction: tuple[float, float, float] | np.ndarray,
    label: str,
    label_offset: tuple[float, float, float] = (0.0, 0.0, 0.0),
    color: str = "#050505",
    scale: float = 0.65,
) -> None:
    start = np.array(start, dtype=float)
    direction = np.array(direction, dtype=float)
    unit = direction / np.linalg.norm(direction)
    arrow = pv.Arrow(
        start=start,
        direction=unit,
        scale=scale,
        tip_length=0.28,
        tip_radius=0.055,
        shaft_radius=0.018,
    )
    plotter.add_mesh(arrow, color=color)
    label_point = start + unit * scale + np.array(label_offset, dtype=float)
    plotter.add_point_labels(
        [label_point],
        [label],
        font_size=24,
        text_color=color,
        font_file=text_font_file(),
        always_visible=True,
        **LABEL_WIPEOUT,
    )


def add_rotation_arc(
    plotter: pv.Plotter,
    center: tuple[float, float, float] | np.ndarray,
    basis_a: tuple[float, float, float],
    basis_b: tuple[float, float, float],
    label: str,
    radius: float = 0.16,
    color: str = "#050505",
) -> None:
    center = np.array(center, dtype=float)
    a = np.array(basis_a, dtype=float)
    b = np.array(basis_b, dtype=float)
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)

    angles = np.linspace(np.deg2rad(35.0), np.deg2rad(310.0), 42)
    points = center + radius * (
        np.cos(angles)[:, None] * a + np.sin(angles)[:, None] * b
    )
    arc = pv.lines_from_points(points)
    plotter.add_mesh(arc.tube(radius=0.008), color=color)

    tangent = points[-1] - points[-2]
    add_arrow(
        plotter,
        points[-2],
        tangent,
        "",
        color=color,
        scale=0.10,
    )
    plotter.add_point_labels(
        [center + radius * 1.55 * b],
        [label],
        font_size=18,
        text_color=color,
        font_file=text_font_file(),
        always_visible=True,
        **LABEL_WIPEOUT,
    )


def add_node_labels(plotter: pv.Plotter) -> None:
    points = []
    labels = []
    for label, point in NODE_POINTS.items():
        natural = NATURAL_COORDS[label]
        outward = np.array(natural, dtype=float)
        outward = outward / np.linalg.norm(outward)
        points.append(np.array(point) + 0.34 * outward)
        labels.append(
            f"{label}\n"
            f"ξ = {natural[0]:+d}\n"
            f"η = {natural[1]:+d}\n"
            f"ζ = {natural[2]:+d}"
        )
    plotter.add_point_labels(
        points,
        labels,
        font_size=18,
        text_color="#050505",
        font_file=text_font_file(),
        always_visible=True,
        **LABEL_WIPEOUT,
    )


def add_local_axes(plotter: pv.Plotter) -> None:
    origin = (-1.45, -1.28, 1.02)
    add_arrow(
        plotter,
        origin,
        XI_DIRECTION,
        "X / ξ",
        (0.16, 0.00, 0.00),
        scale=0.72,
    )
    add_arrow(
        plotter,
        origin,
        ETA_DIRECTION,
        "Y / η",
        (0.00, 0.16, 0.00),
        scale=0.72,
    )
    add_arrow(
        plotter,
        origin,
        ZETA_DIRECTION,
        "Z / ζ",
        (0.00, 0.00, 0.18),
        scale=0.72,
    )


def add_greek_letter_legend(plotter: pv.Plotter) -> None:
    plotter.add_point_labels(
        [(-2.05, -1.20, 1.65)],
        ["Greek letters\nξ = xi\nη = eta\nζ = zeta\nθ = theta"],
        font_size=18,
        text_color="#050505",
        font_file=text_font_file(),
        always_visible=True,
        **LABEL_WIPEOUT,
    )


def shape_factor(variable: str, sign: int) -> str:
    operator = "+" if sign > 0 else "-"
    return f"(1 {operator} {variable})"


def add_shape_function_panel(plotter: pv.Plotter) -> None:
    lines = ["Hex8 shape functions"]
    for index, (label, natural) in enumerate(NATURAL_COORDS.items(), start=1):
        xi, eta, zeta = natural
        lines.append(
            f"N{index} = 1/8"
            f"{shape_factor('ξ', xi)}"
            f"{shape_factor('η', eta)}"
            f"{shape_factor('ζ', zeta)}  [{label}]"
        )

    plotter.add_point_labels(
        [(2.05, -1.42, -1.10)],
        ["\n".join(lines)],
        font_size=15,
        text_color="#050505",
        font_file=text_font_file(),
        always_visible=True,
        **LABEL_WIPEOUT,
    )


def add_p1_degrees_of_freedom(plotter: pv.Plotter) -> None:
    p1 = as_array("P1")
    add_arrow(plotter, p1, P1_XI_DISPLAY_DIRECTION, "u1", (0.00, 0.10, 0.00), scale=0.82)
    add_arrow(plotter, p1, P1_ETA_DISPLAY_DIRECTION, "v1", (0.12, 0.00, 0.00), scale=0.82)
    add_arrow(plotter, p1, P1_ZETA_DISPLAY_DIRECTION, "w1", (0.00, 0.00, -0.14), scale=0.82)

    add_rotation_arc(
        plotter,
        p1 + 1.12 * P1_XI_DISPLAY_DIRECTION / np.linalg.norm(P1_XI_DISPLAY_DIRECTION),
        P1_ETA_DISPLAY_DIRECTION,
        P1_ZETA_DISPLAY_DIRECTION,
        "θu1",
    )
    add_rotation_arc(
        plotter,
        p1 + 1.12 * P1_ETA_DISPLAY_DIRECTION / np.linalg.norm(P1_ETA_DISPLAY_DIRECTION),
        P1_XI_DISPLAY_DIRECTION,
        P1_ZETA_DISPLAY_DIRECTION,
        "θv1",
    )
    add_rotation_arc(
        plotter,
        p1 + 1.08 * P1_ZETA_DISPLAY_DIRECTION,
        P1_XI_DISPLAY_DIRECTION,
        P1_ETA_DISPLAY_DIRECTION,
        "θw1",
    )


def make_plot(screenshot: Path | None = None) -> None:
    mesh = build_brick_faces()
    plotter = pv.Plotter(off_screen=screenshot is not None, window_size=(1400, 900))
    plotter.set_background("white")

    plotter.add_mesh(
        mesh,
        scalars="z_height",
        cmap=["#f59f16", "#d8d0bf"],
        opacity=0.84,
        show_edges=True,
        edge_color="#111111",
        line_width=1.6,
        show_scalar_bar=False,
    )
    plotter.add_points(
        np.array(list(NODE_POINTS.values())),
        color="#050505",
        point_size=18,
        render_points_as_spheres=True,
    )

    add_node_labels(plotter)
    add_local_axes(plotter)
    add_greek_letter_legend(plotter)
    add_shape_function_panel(plotter)
    add_p1_degrees_of_freedom(plotter)

    plotter.camera_position = [
        (3.2, -5.4, 2.8),
        (0.00, 0.00, 0.02),
        (0.04, 0.06, 1.0),
    ]
    plotter.camera.parallel_projection = True
    plotter.camera.parallel_scale = 2.70

    if screenshot:
        screenshot.parent.mkdir(parents=True, exist_ok=True)
        plotter.show(screenshot=str(screenshot))
        print(f"Saved screenshot: {screenshot}")
    else:
        plotter.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draw the isoparametric hexahedron ground-zero diagram."
    )
    parser.add_argument(
        "--screenshot",
        type=Path,
        default=None,
        help="Optional PNG path for an off-screen screenshot.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    make_plot(parse_args().screenshot)
