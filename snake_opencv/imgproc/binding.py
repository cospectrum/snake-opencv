import cv2
import numpy as np

from typing import Tuple, Optional, Literal, Union

from .const import INTER_LINEAR
from ..core import (
    BORDER_DEFAULT,
    CV_PI,
)


__all__ = [
    'resize',
    'cvt_color',
    'rectangle',
    'circle',
    'line',
    'put_text',
    'canny',
    'find_contours',
    'draw_contours',
    'gaussian_blur',
    'hough_lines',
    'hough_lines_p',
    'min_area_rect',
    'box_points',
]


LineType = Literal[-1, 4, 8, 16]


Width = int
Height = int


def resize(
    src: np.ndarray,
    dsize: Optional[Tuple[Width, Height]] = None,
    dst: Optional[np.ndarray] = None,
    fx: float = 0.,
    fy: float = 0.,
    interpolation: int = INTER_LINEAR,
) -> np.ndarray:
    return cv2.resize(
        src,
        dsize,
        dst,
        fx=fx,
        fy=fy,
        interpolation=interpolation,
    )


def cvt_color(
    src: np.ndarray,
    code: int,
    dst: Optional[np.ndarray] = None,
    dst_cn: int = 0,
) -> np.ndarray:
    return cv2.cvtColor(src, code, dst, dst_cn)


X = int
Y = int
Color = Union[Tuple, int]


def rectangle(
    image: np.ndarray,
    pt1: Tuple[X, Y],
    pt2: Tuple[X, Y],
    color: Color,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    return cv2.rectangle(image, pt1, pt2, color, thickness, line_type, shift)


def circle(
    image: np.ndarray,
    center: Tuple[X, Y],
    radius: int,
    color: Color,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    return cv2.circle(
        image,
        center,
        radius,
        color,
        thickness,
        line_type,
        shift=shift,
    )


def line(
    image: np.ndarray,
    pt1: Tuple[X, Y],
    pt2: Tuple[X, Y],
    color: Color,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    return cv2.line(image, pt1, pt2, color, thickness, line_type, shift)


def put_text(
    image: np.ndarray,
    text: str,
    org: Tuple[X, Y],
    font_face: int,
    font_scale: float,
    color: Color,
    thickness: int = 1,
    line_type: LineType = 8,
    bottom_left_origin: bool = False,
) -> np.ndarray:
    return cv2.putText(
        image,
        text,
        org,
        font_face,
        font_scale,
        color,
        thickness,
        line_type,
        bottom_left_origin,
    )


def canny(
    image: np.ndarray,
    threshold1: float,
    threshold2: float,
    edges: Optional[np.ndarray] = None,
    aperture_size: int = 3,
    l2gradient: bool = False,
) -> np.ndarray:
    """Finds edges in an image using the Canny algorithm.

    The function finds edges in the input image and marks them in the output
    map edges using the Canny algorithm. The smallest value between
    threshold1 and threshold2 is used for edge linking. The largest value is
    used to find initial segments of strong edges.
    See http://en.wikipedia.org/wiki/Canny_edge_detector
    """
    return cv2.Canny(
        image,
        threshold1,
        threshold2,
        edges=edges,
        apertureSize=aperture_size,
        L2gradient=l2gradient,
    )


Contours = Tuple[np.ndarray, ...]
Hierarchy = np.ndarray


def find_contours(
    image: np.ndarray,
    mode: int,
    method: int,
    offset: Optional[Tuple[X, Y]] = None,
) -> Tuple[Contours, Hierarchy]:
    """Finds contours in a binary image.

    The function retrieves contours from the binary image using the algorithm
    Suzuki85. The contours are a useful tool for shape analysis and object
    detection and recognition. See squares.cpp in the OpenCV sample directory.
    """
    return cv2.findContours(image, mode=mode, method=method, offset=offset)


def draw_contours(
    image: np.ndarray,
    contours: Contours,
    contour_idx: int,
    color: Color,
    thickness: int = 1,
    line_type: LineType = 8,
    hierarchy: Optional[Hierarchy] = None,
    max_level: Optional[int] = None,
    offset: Optional[Tuple[X, Y]] = None,
) -> np.ndarray:
    """Draws contours outlines or filled contours.

    The function draws contour outlines in the image if thickness >= 0 or
    fills the area bounded by the contours if thickness < 0.

    Args:
        image: destination image.
        contours:
            All the input contours. Each contour is stored as a point vector.
        contour_idx:
            Parameter indicating a contour to draw.
            If it is negative, all the contours are drawn.
        color: Color of the contours.
        thickness:
            Thickness of lines the contours are drawn with.
            If it is negative, the contour interiors are drawn.
        line_type: Line connectivity. See #LineTypes
        hierarchy:
            Optional information about hierarchy.
            It is only needed if you want to draw only some of the contours.
        max_level:
            Maximal level for drawn contours. If it is 0, only the specified
            contour is drawn. If it is 1, the function draws the contour(s)
            and all the nested contours. If it is 2, the function draws the
            contours, all the nested contours, all the nested-to-nested
            contours, and so on. This parameter is only taken into account
            when there is hierarchy available.
        offset:
            Optional contour shift parameter.
            Shift all the drawn contours by the specified offset = (dx, dy).

    Returns:
        ndarray: destination image.
    """
    return cv2.drawContours(
        image,
        contours,
        contour_idx,
        color,
        thickness,
        line_type,
        hierarchy,
        max_level,
        offset,
    )


def gaussian_blur(
    src: np.ndarray,
    ksize: Tuple[int, int],
    sigma_x: float,
    dst: Optional[np.ndarray] = None,
    sigma_y: float = 0.,
    border_type: int = BORDER_DEFAULT,
) -> np.ndarray:
    return cv2.GaussianBlur(src, ksize, sigma_x, dst, sigma_y, border_type)


def hough_lines(
    image: np.ndarray,
    rho: float,
    theta: float,
    threshold: int,
    lines: Optional[np.ndarray] = None,
    srn: float = 0.,
    stn: float = 0.,
    min_theta: float = 0.,
    max_theta: float = CV_PI,
) -> Optional[np.ndarray]:
    return cv2.HoughLines(
        image,
        rho=rho,
        theta=theta,
        threshold=threshold,
        lines=lines,
        srn=srn,
        stn=stn,
        min_theta=min_theta,
        max_theta=max_theta,
    )


def hough_lines_p(
    image: np.ndarray,
    rho: float,
    theta: float,
    threshold: int,
    lines: Optional[np.ndarray] = None,
    min_line_length: float = 0.,
    max_line_gap: float = 0.,
) -> Optional[np.ndarray]:
    return cv2.HoughLinesP(
        image,
        rho,
        theta,
        threshold,
        lines,
        min_line_length,
        max_line_gap,
    )


Center = Tuple[X, Y]
Angle = float
RotatedRect = Tuple[Center, Tuple[Width, Height], Angle]


def min_area_rect(points: np.ndarray) -> RotatedRect:
    return cv2.minAreaRect(points)


def box_points(
    box: RotatedRect,
    points: Optional[np.ndarray] = None,
) -> np.ndarray:
    return cv2.boxPoints(box, points)
