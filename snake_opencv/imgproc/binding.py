import cv2
import numpy as np

from typing import Tuple, Optional, List, Literal, Union
from typing_extensions import TypeAlias


from .const import INTER_LINEAR
from ..core import (
    BORDER_CONSTANT,
    BORDER_DEFAULT,
    CV_PI,
    CV_32S,
    DECOMP_LU,
)


__all__ = [
    'resize',
    'cvt_color',
    'rectangle',
    'circle',
    'line',
    'fill_poly',
    'put_text',
    'canny',
    'find_contours',
    'draw_contours',
    'gaussian_blur',
    'hough_lines',
    'hough_lines_p',
    'min_area_rect',
    'box_points',
    'get_perspective_transform',
    'warp_perspective',
    'laplacian',
    'threshold',
    'connected_components_with_stats',
    'connected_components',
    'match_template',
    'warp_affine',
    'get_affine_transform',
    'get_rotation_matrix_2d',
    'median_blur',
    'blur',
    'bilateral_filter',
    'point_polygon_test',
    'contour_area',
]


LineType = Literal[-1, 4, 8, 16]

Width = int
Height = int


def resize(
    src: np.ndarray,
    dsize: Optional[Tuple[Width, Height]] = None,
    dst: Optional[np.ndarray] = None,
    fx: float = 0.0,
    fy: float = 0.0,
    interpolation: int = INTER_LINEAR,
) -> np.ndarray:
    """Resizes an image.

    The function resize resizes the image src down to or up to the specified
    size. Note that the initial dst type or size are not taken into account.
    Instead, the size and type are derived from the src, dsize, fx, and fy.
    If you want to resize src so that it fits the pre-created dst, you may
    call the function as follows:
       resize(src, dsize, dst, 0, 0, interpolation)

    If you want to decimate the image by factor of 2 in each direction, you
    can call the function this way:
       # specify fx and fy and let the function compute the destination image
       # size.
       resize(src, dsize, dst, 0.5, 0.5, interpolation);

    To shrink an image, it will generally look best with #INTER_AREA
    interpolation, whereas to enlarge an image, it will generally look best
    with #INTER_CUBIC (slow) or #INTER_LINEAR (faster but still looks OK).

    Args:
        src: input image.
        dsize:
            output image size; if it equals zero (None in Python), it is
            computed as:
                dsize = Size(round(fx*src.cols), round(fy*src.rows))
            Either dsize or both fx and fy must be non-zero.
        dst:
            output image; it has the size dsize (when it is non-zero) or the
            size computed from src.shape, fx, and fy; the type of dst is the
            same as of src.
        fx:
            scale factor along the horizontal axis; when it equals 0, it is
            computed as dsize.width / src.cols
        fy:
            scale factor along the vertical axis; when it equals 0, it is
            computed as dsize.height / src.rows
        interpolation: interpolation method, see #InterpolationFlags
    """
    return cv2.resize(  # type: ignore
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
    """Converts an image from one color space to another.

    The function converts an input image from one color space to another. In
    case of a transformation to-from RGB color space, the order of the
    channels should be specified explicitly (RGB or BGR). Note that the
    default color format in OpenCV is often referred to as RGB but it is
    actually BGR (the bytes are reversed). So the first byte in a standard
    (24-bit) color image will be an 8-bit Blue component, the second byte will
    be Green, and the third byte will be Red. The fourth, fifth, and sixth
    bytes would then be the second pixel (Blue, then Green, then Red), and so
    on.

    The conventional ranges for R, G, and B channel values are:
        0 to 255 for CV_8U images
        0 to 65535 for CV_16U images
        0 to 1 for CV_32F images

    In case of linear transformations, the range does not matter. But in case
    of a non-linear transformation, an input RGB image should be normalized to
    the proper value range to get the correct results, for example, for
    RGB -> L*u*v* transformation. For example, if you have a 32-bit
    floating-point image directly converted from an 8-bit image without any
    scaling, then it will have the 0..255 value range instead of 0..1 assumed
    by the function. So, before calling #cvtColor, you need first to scale
    the image down:
       img *= 1./255;
       cvt_color(img, img, COLOR_BGR2Luv);

    If you use #cvtColor with 8-bit images, the conversion will have some
    information lost. For many applications, this will not be noticeable but
    it is recommended to use 32-bit images in applications that need the full
    range of colors or that convert an image before an operation and then
    convert back.

    If conversion adds the alpha channel, its value will set to the maximum of
    corresponding channel range: 255 for CV_8U, 65535 for CV_16U, 1 for CV_32F

    Args:
        src:
            input image: 8-bit unsigned, 16-bit unsigned (CV_16UC…), or
            single-precision floating-point.
        code: color space conversion code (see #ColorConversionCodes).
        dst: output image of the same size and depth as src.
        dst_cn:
            number of channels in the destination image; if the parameter is
            0, the number of the channels is derived automatically from src
            and code.
    """
    return cv2.cvtColor(src, code, dst, dst_cn)  # type: ignore


X = int
Y = int
Scalar = Union[Tuple[float, ...], float]


def rectangle(
    image: np.ndarray,
    pt1: Tuple[X, Y],
    pt2: Tuple[X, Y],
    color: Scalar,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    """Draws a simple, thick, or filled up-right rectangle.

    The function cv.rectangle draws a rectangle outline or a filled rectangle
    whose two opposite corners are pt1 and pt2.

    Args:
        image: Image.
        pt1: Vertex of the rectangle.
        pt2: Vertex of the rectangle opposite to pt1 .
        color: Rectangle color or brightness (grayscale image).
        thickness:
            Thickness of lines that make up the rectangle. Negative values,
            like #FILLED, mean that the function has to draw a filled
            rectangle.
        line_type: Type of the line. See #LineTypes
        shift: Number of fractional bits in the point coordinates.
    """
    return cv2.rectangle(image, pt1, pt2, color, thickness, line_type, shift)  # type: ignore


def circle(
    image: np.ndarray,
    center: Tuple[X, Y],
    radius: int,
    color: Scalar,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    """Draws a circle.

    The function cv.circle draws a simple or filled circle with a given center
    and radius.

    Args:
        image: Image where the circle is drawn.
        center: Center of the circle.
        radius: Radius of the circle.
        color: Circle color.
        thickness:
            Thickness of the circle outline, if positive. Negative values,
            like #FILLED, mean that a filled circle is to be drawn.
        line_type: Type of the circle boundary. See #LineTypes
        shift:
            Number of fractional bits in the coordinates of the center and in
            the radius value.
    """
    return cv2.circle(  # type: ignore
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
    color: Scalar,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    """Draws a line segment connecting two points.

    The function line draws the line segment between pt1 and pt2 points in the
    image. The line is clipped by the image boundaries. For non-antialiased
    lines with integer coordinates, the 8-connected or 4-connected Bresenham
    algorithm is used. Thick lines are drawn with rounding endings.
    Antialiased lines are drawn using Gaussian filtering.

    Args:
        image: Image.
        pt1: First point of the line segment.
        pt2: Second point of the line segment.
        color: Line color.
        thickness: Line thickness.
        line_type: Type of the line. See #LineTypes.
        shift: Number of fractional bits in the point coordinates.
    """
    return cv2.line(image, pt1, pt2, color, thickness, line_type, shift)  # type: ignore


def fill_poly(
    image: np.ndarray,
    pts: List[np.ndarray],
    color: Scalar,
    line_type: LineType = 8,
    shift: int = 0,
    offset: Optional[Tuple[X, Y]] = None,
) -> np.ndarray:
    """Fills the area bounded by one or more polygons.

    The function cv.fill_poly fills an area bounded by several polygonal
    contours. The function can fill complex areas, for example, areas with
    holes, contours with self-intersections (some of their parts), and so
    forth.

    Args:
        image: Image.
        pts:
            Array of polygons where each polygon is represented as an array of
            points.
        color: Polygon color.
        line_lype: Type of the polygon boundaries. See #LineTypes
        shift: Number of fractional bits in the vertex coordinates.
        offset: Optional offset of all points of the contours.
    """
    return cv2.fillPoly(image, pts, color, line_type, shift, offset)  # type: ignore


def put_text(
    image: np.ndarray,
    text: str,
    org: Tuple[X, Y],
    font_face: int,
    font_scale: float,
    color: Scalar,
    thickness: int = 1,
    line_type: LineType = 8,
    bottom_left_origin: bool = False,
) -> np.ndarray:
    """Draws a text string.

    The function cv.put_text renders the specified text string in the image.
    Symbols that cannot be rendered using the specified font are replaced by
    question marks. See #getTextSize for a text rendering code example.

    Args:
        image: Image.
        text: Text string to be drawn.
        org: Bottom-left corner of the text string in the image.
        font_face: Font type, see #HersheyFonts.
        font_scale:
            Font scale factor that is multiplied by the font-specific base
            size.
        color: Text color.
        thickness: Thickness of the lines used to draw a text.
        line_type: Line type. See #LineTypes
        bottom_left_origin:
            When true, the image data origin is at the bottom-left corner.
            Otherwise, it is at the top-left corner.
    """
    return cv2.putText(  # type: ignore
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

    Args:
        image: 8-bit input image.
        threshold1: first threshold for the hysteresis procedure.
        threshold2: second threshold for the hysteresis procedure.
        edges:
            output edge map; single channels 8-bit image, which has the same
            size as image.
        aperture_size: aperture size for the Sobel operator.
        l2gradient:
            a flag, indicating whether a more accurate
            l2-norm = sqrt((dI/dx)^2 + (dI/dy)^2) should be used to calculate
            the image gradient magnitude (l2gradient=true), or whether the
            default l1-norm = |dI/dx| + |dI/dy| is enough (l2gradient=false).
    """
    return cv2.Canny(  # type: ignore
        image,
        threshold1,
        threshold2,
        edges=edges,
        apertureSize=aperture_size,
        L2gradient=l2gradient,
    )


Contours = Tuple[np.ndarray, ...]
Hierarchy: TypeAlias = np.ndarray


def find_contours(
    image: np.ndarray,
    mode: int,
    method: int,
    offset: Optional[Tuple[X, Y]] = None,
) -> Tuple[Contours, Hierarchy]:
    """Finds contours in a binary image.

    The function retrieves contours from the binary image using the algorithm
    Suzuki85
    (https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Suzuki85).
    The contours are a useful tool for shape analysis and object detection and
    recognition. See squares.cpp in the OpenCV sample directory.

    Args:
        image:
            Source, an 8-bit single-channel image. Non-zero pixels are treated
            as 1’s. Zero pixels remain 0’s, so the image is treated as binary.
            You can use #compare, #inRange, #threshold , #adaptiveThreshold,
            #Canny, and others to create a binary image out of a grayscale or
            color one. If mode equals to #RETR_CCOMP or #RETR_FLOODFILL, the
            input can also be a 32-bit integer image of labels (CV_32SC1).
        mode: Contour retrieval mode, see #RetrievalModes
        method: Contour approximation method, see #ContourApproximationModes
        offset:
            Optional offset by which every contour point is shifted. This is
            useful if the contours are extracted from the image ROI and then
            they should be analyzed in the whole image context.
    """
    return cv2.findContours(image, mode=mode, method=method, offset=offset)  # type: ignore


def draw_contours(
    image: np.ndarray,
    contours: Contours,
    contour_idx: int,
    color: Scalar,
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

    Returns: destination image.
    """
    return cv2.drawContours(  # type: ignore
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
    """Blurs an image using a Gaussian filter.

    The function convolves the source image with the specified Gaussian
    kernel. In-place filtering is supported.

    Args:
        src:
            input image; the image can have any number of channels, which are
            processed independently, but the depth should be CV_8U, CV_16U,
            CV_16S, CV_32F or CV_64F.
        ksize:
            Gaussian kernel size. ksize.width and ksize.height can differ but
            they both must be positive and odd. Or, they can be zero’s and
            then they are computed from sigma.
        sigma_x: Gaussian kernel standard deviation in X direction.
        dst: output image of the same size and type as src.
        sigma_y:
            Gaussian kernel standard deviation in Y direction; if sigmaY is
            zero, it is set to be equal to sigmaX, if both sigmas are zeros,
            they are computed from ksize.width and ksize.height, respectively
            (see #getGaussianKernel for details); to fully control the result
            regardless of possible future modifications of all this semantics,
            it is recommended to specify all of ksize, sigmaX, and sigmaY.
        border_type:
            pixel extrapolation method, see #BorderTypes.
            #BORDER_WRAP is not supported.
    """
    return cv2.GaussianBlur(src, ksize, sigma_x, dst, sigma_y, border_type)  # type: ignore


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
    """Finds lines in a binary image using the standard Hough transform.

    The function implements the standard or standard multi-scale Hough
    transform algorithm for line detection. See
    http://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm for a good explanation
    of Hough transform.

    Args:
        image:
            8-bit, single-channel binary source image. The image may be
            modified by the function.
        rho: Distance resolution of the accumulator in pixels.
        theta: Angle resolution of the accumulator in radians.
        threshold:
            %Accumulator threshold parameter. Only those lines are returned
            that get enough votes (> votes).
        lines:
            Output vector of lines. Each line is represented by a 2 or 3
            element vector (rho, theta) or (rho, theta, votes), where rho is
            the distance from the coordinate origin (0, 0) (top-left corner of
            the image), theta is the line rotation angle in radians (
            0 ~ vertical line, pi/2 ~ horizontal line), and votes is the value
            of accumulator.
        srn:
            For the multi-scale Hough transform, it is a divisor for the
            distance resolution rho. The coarse accumulator distance
            resolution is rho and the accurate accumulator resolution is
            rho/srn. If both srn=0 and stn=0, the classical Hough transform is
            used. Otherwise, both these parameters should be positive.
        stn:
            For the multi-scale Hough transform, it is a divisor for the
            distance resolution theta.
        min_theta:
            For standard and multi-scale Hough transform, minimum angle to
            check for lines. Must fall between 0 and max_theta.
        max_theta:
            For standard and multi-scale Hough transform, an upper bound for
            the angle. Must fall between min_theta and CV_PI. The actual
            maximum angle in the accumulator may be slightly less than
            max_theta, depending on the parameters min_theta and theta.
    """
    return cv2.HoughLines(  # type: ignore
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
    """Finds line segments in a binary image using the probabilistic Hough
    transform.

    The function implements the probabilistic Hough transform algorithm for
    line detection, described in Matas00
    (https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Matas00)

    Args:
        image:
            8-bit, single-channel binary source image. The image may be
            modified by the function.
        rho: Distance resolution of the accumulator in pixels.
        theta: Angle resolution of the accumulator in radians.
        threshold:
            %Accumulator threshold parameter. Only those lines are returned
            that get enough votes (> threshold).
        lines:
            Output vector of lines. Each line is represented by a 4-element
            vector (x1, y1, x2, y2), where (x1, y1) and (x2, y2) are the
            ending points of each detected line segment.
        min_line_length:
            Minimum line length. Line segments shorter than that are rejected.
        max_line_gap:
            Maximum allowed gap between points on the same line to link them.
    """
    return cv2.HoughLinesP(  # type: ignore
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
    """Finds a rotated rectangle of the minimum area enclosing the input 2D
    point set.

    The function calculates and returns the minimum-area bounding rectangle
    (possibly rotated) for a specified point set. Developer should keep in
    mind that the returned RotatedRect can contain negative indices when data
    is close to the containing Mat element boundary.

    Args:
        points: Input vector of 2D points.
    """
    return cv2.minAreaRect(points)  # type: ignore


def box_points(
    box: RotatedRect,
    points: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Finds the four vertices of a rotated rect. Useful to draw the rotated
    rectangle.

    The function finds the four vertices of a rotated rectangle. This function
    is useful to draw the rectangle. In C++, instead of using this function,
    you can directly use RotatedRect::points method. Please visit the
    tutorial_bounding_rotated_ellipses “tutorial on Creating Bounding rotated
    boxes and ellipses for contours” for more information.

    Args:
        box: The input rotated rectangle. It may be the output of
        points: The output array of four vertices of rectangles.
    """
    return cv2.boxPoints(box, points)  # type: ignore


def get_perspective_transform(
    src: np.ndarray,
    dst: np.ndarray,
    solve_method: int = DECOMP_LU,
) -> np.ndarray:
    """Calculates a perspective transform from four pairs of the corresponding
    points.

    Args:
        src: Coordinates of quadrangle vertices in the source image.
        dst:
            Coordinates of the corresponding quadrangle vertices in the
            destination image.
        solve_method: method passed to cv::solve (#DecompTypes)
    """
    return cv2.getPerspectiveTransform(src, dst, solve_method)  # type: ignore


def warp_perspective(
    src: np.ndarray,
    m: np.ndarray,
    dsize: Tuple[Width, Height],
    dst: Optional[np.ndarray] = None,
    flag: int = INTER_LINEAR,
    border_mode: int = BORDER_CONSTANT,
    border_value: Optional[Scalar] = None,
) -> np.ndarray:
    """Applies a perspective transformation to an image.

    The function warpPerspective transforms the source image using the
    specified matrix m.

    Args:
        src: input image.
        m: 3x3 transformation matrix.
        dsize: size of the output image.
        dst: output image that has the size dsize and the same type as src.
        flag:
            combination of interpolation methods (#INTER_LINEAR or
            #INTER_NEAREST) and the optional flag #WARP_INVERSE_MAP, that sets
            m as the inverse transformation.
        border_mode:
            pixel extrapolation method (#BORDER_CONSTANT or
            #BORDER_REPLICATE).
        border_value:
            value used in case of a constant border; by default, it equals 0.

    Returns: output image that has the size dsize and the same type as src
    """
    return cv2.warpPerspective(  # type: ignore
        src,
        m,
        dsize,
        dst,
        flag,
        border_mode,
        border_value,
    )


def laplacian(
    src: np.ndarray,
    ddepth: int,
    dst: Optional[np.ndarray] = None,
    ksize: int = 1,
    scale: float = 1.0,
    delta: float = 0.0,
    border_type: int = BORDER_DEFAULT,
) -> np.ndarray:
    """Calculates the Laplacian of an image.

    The function calculates the Laplacian of the source image by adding up the
    second x and y derivatives calculated using the Sobel operator.

    This is done when ksize > 1. When ksize == 1, the Laplacian is computed by
    filtering the image with the following 3x3 aperture:
        [0,  1,  0]
        [1, -4,  1]
        [0,  1,  0]

    Args:
        src: Source image.
        ddepth:
            Desired depth of the destination image, see filter_depths
            “combinations”.
        dst:
            Destination image of the same size and the same number of channels
            as src.
        ksize:
            Aperture size used to compute the second-derivative filters. See
            #getDerivKernels for details. The size must be positive and odd.
        scale:
            Optional scale factor for the computed Laplacian values. By
            default, no scaling is applied. See #getDerivKernels for details.
        delta:
            Optional delta value that is added to the results prior to storing
            them in dst.
        border_type:
            Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not
            supported.
    """
    return cv2.Laplacian(  # type: ignore
        src,
        ddepth,
        dst,
        ksize=ksize,
        scale=scale,
        delta=delta,
        borderType=border_type,
    )


def threshold(
    src: np.ndarray,
    thresh: float,
    maxval: float,
    type: int,
    dst: Optional[np.ndarray] = None,
) -> Tuple[float, np.ndarray]:
    """Applies a fixed-level threshold to each array element.

    The function applies fixed-level thresholding to a multiple-channel array.
    The function is typically used to get a bi-level (binary) image out of a
    grayscale image ( #compare could be also used for this purpose) or for
    removing a noise, that is, filtering out pixels with too small or too
    large values. There are several types of thresholding supported by the
    function. They are determined by type parameter.

    Also, the special values #THRESH_OTSU or #THRESH_TRIANGLE may be combined
    with one of the above values. In these cases, the function determines the
    optimal threshold value using the Otsu’s or Triangle algorithm and uses it
    instead of the specified thresh.

    Note: Currently, the Otsu’s and Triangle methods are implemented only for
    8-bit single-channel images.

    Args:
        src: input array (multiple-channel, 8-bit or 32-bit floating point).
        thresh: threshold value.
        maxval:
            maximum value to use with the #THRESH_BINARY and
            #THRESH_BINARY_INV thresholding types.
        type: thresholding type (see #ThresholdTypes).
        dst:
            output array of the same size and type and the same number of
            channels as src.

    Returns: the computed threshold value if Otsu’s or Triangle methods used.
    """
    return cv2.threshold(  # type: ignore
        src,
        thresh,
        maxval,
        type=type,
        dst=dst,
    )


Labels: TypeAlias = np.ndarray
Stats: TypeAlias = np.ndarray
Centroids: TypeAlias = np.ndarray


def connected_components_with_stats(
    image: np.ndarray,
    labels: Optional[np.ndarray] = None,
    stats: Optional[np.ndarray] = None,
    centroids: Optional[np.ndarray] = None,
    connectivity: Literal[4, 8] = 8,
    ltype: int = CV_32S,
) -> Tuple[int, Labels, Stats, Centroids]:
    """computes the connected components labeled image of boolean image and
    also produces a statistics output for each label

    image with 4 or 8 way connectivity - returns N, the total number of labels
    [0, N-1] where 0 represents the background label. ltype specifies the
    output label image type, an important consideration based on the total
    number of labels or alternatively the total number of pixels in the source
    image. ccltype specifies the connected components labeling algorithm to
    use, currently Bolelli (Spaghetti) Bolelli2019, Grana (BBDT) Grana2010 and
    Wu’s (SAUF) Wu2009 algorithms are supported, see the
    #ConnectedComponentsAlgorithmsTypes for details. Note that SAUF algorithm
    forces a row major ordering of labels while Spaghetti and BBDT do not. This
    function uses parallel version of the algorithms (statistics included) if
    at least one allowed parallel framework is enabled and if the rows of the
    image are at least twice the number returned by #getNumberOfCPUs.

    Args:
        image: the 8-bit single-channel image to be labeled
        labels: destination labeled image
        stats:
            statistics output for each label, including the background label.
            Statistics are accessed via stats(label, COLUMN) where COLUMN is
            one of #ConnectedComponentsTypes, selecting the statistic. The data
            type is CV_32S.
        centroids:
            centroid output for each label, including the background label.
            Centroids are accessed via centroids(label, 0) for x and
            centroids(label, 1) for y. The data type CV_64F.
        connectivity: 8 or 4 for 8-way or 4-way connectivity respectively
        ltype:
            output image label type. Currently CV_32S and CV_16U are supported.
    """
    return cv2.connectedComponentsWithStats(  # type: ignore
        image,
        labels=labels,
        stats=stats,
        centroids=centroids,
        connectivity=connectivity,
        ltype=ltype,
    )


def connected_components(
    image: np.ndarray,
    labels: Optional[np.ndarray] = None,
    connectivity: Literal[4, 8] = 8,
    ltype: int = CV_32S,
) -> Tuple[int, Labels]:
    """computes the connected components labeled image of boolean image

    image with 4 or 8 way connectivity - returns N, the total number of labels
    [0, N-1] where 0 represents the background label. ltype specifies the
    output label image type, an important consideration based on the total
    number of labels or alternatively the total number of pixels in the source
    image. ccltype specifies the connected components labeling algorithm to
    use, currently Bolelli (Spaghetti) Bolelli2019, Grana (BBDT) Grana2010 and
    Wu’s (SAUF) Wu2009 algorithms are supported, see the
    #ConnectedComponentsAlgorithmsTypes for details. Note that SAUF algorithm
    forces a row major ordering of labels while Spaghetti and BBDT do not.
    This function uses parallel version of the algorithms if at least one
    allowed parallel framework is enabled and if the rows of the image are at
    least twice the number returned by #getNumberOfCPUs.

    Args:
        image: the 8-bit single-channel image to be labeled
        labels: destination labeled image
        connectivity: 8 or 4 for 8-way or 4-way connectivity respectively
        ltype:
            output image label type. Currently CV_32S and CV_16U are supported.
    """
    return cv2.connectedComponents(  # type: ignore
        image,
        labels=labels,
        connectivity=connectivity,
        ltype=ltype,
    )


def match_template(
    image: np.ndarray,
    templ: np.ndarray,
    method: int,
    result: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Compares a template against overlapped image regions.

    The function slides through image , compares the overlapped patches of size
    w×h against templ using the specified method and stores the comparison
    results in result . TemplateMatchModes describes the formulae for the
    available comparison methods ( I denotes image, T template, R result, M the
    optional mask ). The summation is done over template and/or the image
    patch: x′=0...w−1,y′=0...h−1

    After the function finishes the comparison, the best matches can be found
    as global minimums (when TM_SQDIFF was used) or maximums (when TM_CCORR or
    TM_CCOEFF was used) using the minMaxLoc function. In case of a color image,
    template summation in the numerator and each sum in the denominator is done
    over all of the channels and separate mean values are used for each
    channel. That is, the function can take a color template and a color image.
    The result will still be a single-channel image, which is easier to
    analyze.

    Args:
        image:
            Image where the search is running. It must be 8-bit or 32-bit
            floating-point.
        templ:
            Searched template. It must be not greater than the source image and
            have the same data type.
        result:
            Map of comparison results. It must be single-channel 32-bit
            floating-point. If image is W×H and templ is w×h, then result is
            (W−w+1)×(H−h+1).
        method:
            Parameter specifying the comparison method, see TemplateMatchModes
        mask:
            Optional mask. It must have the same size as templ. It must either
            have the same number of channels as template or only one channel,
            which is then used for all template and image channels. If the data
            type is CV_8U, the mask is interpreted as a binary mask, meaning
            only elements where mask is nonzero are used and are kept unchanged
            independent of the actual mask value (weight equals 1). For data
            tpye CV_32F, the mask values are used as weights. The exact
            formulas are documented in TemplateMatchModes.
    """
    return cv2.matchTemplate(  # type: ignore
        image,
        templ=templ,
        method=method,
        result=result,
        mask=mask,
    )


def warp_affine(
    src: np.ndarray,
    m: np.ndarray,
    dsize: Tuple[Width, Height],
    dst: Optional[np.ndarray] = None,
    flags: int = INTER_LINEAR,
    border_mode: int = BORDER_CONSTANT,
    border_value: Optional[Scalar] = None,
) -> np.ndarray:
    """Applies an affine transformation to an image.

    The function warpAffine transforms the source image using the specified
    matrix:
        𝚍𝚜𝚝(x,y) = 𝚜𝚛𝚌(𝙼11x + 𝙼12y + 𝙼13, 𝙼21x + 𝙼22y + 𝙼23)

    when the flag WARP_INVERSE_MAP is set. Otherwise, the transformation is
    first inverted with invertAffineTransform and then put in the formula
    above instead of M. The function cannot operate in-place.

    Args:
        src: input image.
        dst: output image that has the size dsize and the same type as src.
        M: 2×3 transformation matrix.
        dsize: size of the output image.
        flags:
            combination of interpolation methods (see InterpolationFlags) and
            the optional flag WARP_INVERSE_MAP that means that M is the
            inverse transformation ( 𝚍𝚜𝚝→𝚜𝚛𝚌 ).
        border_mode:
            pixel extrapolation method (see BorderTypes); when
            borderMode=BORDER_TRANSPARENT, it means that the pixels in the
            destination image corresponding to the "outliers" in the source
            image are not modified by the function.
        border_value:
            value used in case of a constant border; by default, it is 0.
    """
    return cv2.warpAffine(  # type: ignore
        src,
        m,
        dsize=dsize,
        dst=dst,
        flags=flags,
        borderMode=border_mode,
        borderValue=border_value,
    )


def get_affine_transform(src: np.ndarray, dst: np.ndarray) -> np.ndarray:
    """Calculates an affine transform from three pairs of the corresponding
    points.

    The function calculates the 2×3 matrix of an affine transform so that:
        [x', y'].T == map_matrix * [x, y, 1].T

    where
        dst(i) = (x'i, y'i), src(i) = (xi, yi),  i = 0, 1, 2

    Args:
        src: Coordinates of triangle vertices in the source image.
        dst:
            Coordinates of the corresponding triangle vertices in the
            destination image.
    """
    return cv2.getAffineTransform(src, dst=dst)  # type: ignore


Point2f = Tuple[float, float]


def get_rotation_matrix_2d(
    center: Point2f,
    angle: float,
    scale: float,
) -> np.ndarray:
    """Calculates an affine matrix of 2D rotation.

    The function calculates the following matrix:

        [ α   β   (1 − α)⋅𝚌𝚎𝚗𝚝𝚎𝚛.𝚡 − β⋅𝚌𝚎𝚗𝚝𝚎𝚛.𝚢]
        [-β   α   β⋅𝚌𝚎𝚗𝚝𝚎𝚛.𝚡 + (1 − α)⋅𝚌𝚎𝚗𝚝𝚎𝚛.𝚢]

    where
        α = 𝚜𝚌𝚊𝚕𝚎⋅cos(𝚊𝚗𝚐𝚕𝚎),
        β = 𝚜𝚌𝚊𝚕𝚎⋅sin(𝚊𝚗𝚐𝚕𝚎)

    The transformation maps the rotation center to itself. If this is not the
    target, adjust the shift.

    Args:
        center: Center of the rotation in the source image.
        angle:
            Rotation angle in degrees. Positive values mean counter-clockwise
            rotation (the coordinate origin is assumed to be the top-left
            corner).
        scale: Isotropic scale factor.
    """
    return cv2.getRotationMatrix2D(center, angle, scale=scale)  # type: ignore


def median_blur(
    src: np.ndarray,
    ksize: int,
    dst: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Blurs an image using the median filter.

    The function smoothes an image using the median filter with the
    𝚔𝚜𝚒𝚣𝚎×𝚔𝚜𝚒𝚣𝚎 aperture. Each channel of a multi-channel image is processed
    independently. In-place operation is supported.

    Args:
        src:
            input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image
            depth should be CV_8U, CV_16U, or CV_32F, for larger aperture
            sizes, it can only be CV_8U.
        dst: destination array of the same size and type as src.
        ksize:
            aperture linear size; it must be odd and greater than 1, for
            example: 3, 5, 7 ...
    """
    return cv2.medianBlur(src, ksize=ksize, dst=dst)  # type: ignore


def blur(
    src: np.ndarray,
    ksize: Tuple[int, int],
    dst: Optional[np.ndarray] = None,
    anchor: Tuple[int, int] = (-1, -1),
    border_type: int = BORDER_DEFAULT,
) -> np.ndarray:
    """Blurs an image using the normalized box filter.

    The function smooths an image using the kernel:

        K = (1 / (ksize.width * ksize.height)) * J,

    where

        J = [1 1 1 ... 1 1]
            [1 1 1 ... 1 1]
            [...          ]
            [1 1 1 ... 1 1]

    The call blur(src, dst, ksize, anchor, borderType) is equivalent to
    boxFilter(src, dst, src.type(), ksize, anchor, true, borderType).

    Args:
        src:
            input image; it can have any number of channels, which are
            processed independently, but the depth should be CV_8U, CV_16U,
            CV_16S, CV_32F or CV_64F.
        dst: output image of the same size and type as src.
        ksize: blurring kernel size.
        anchor:
            anchor point; default value Point(-1,-1) means that the anchor is
            at the kernel center.
        border_type:
            border mode used to extrapolate pixels outside of the image, see
            BorderTypes. BORDER_WRAP is not supported.
    """
    return cv2.blur(  # type: ignore
        src,
        ksize,
        dst=dst,
        anchor=anchor,
        borderType=border_type,
    )


def bilateral_filter(
    src: np.ndarray,
    d: int,
    sigma_color: float,
    sigma_space: float,
    dst: Optional[np.ndarray] = None,
    border_type: int = BORDER_DEFAULT,
) -> np.ndarray:
    """Applies the bilateral filter to an image.

    The function applies bilateral filtering to the input image, as described
    in http://www.dai.ed.ac.uk/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html
    bilateralFilter can reduce unwanted noise very well while keeping edges
    fairly sharp. However, it is very slow compared to most filters.

    Sigma values: For simplicity, you can set the 2 sigma values to be the
    same. If they are small (< 10), the filter will not have much effect,
    whereas if they are large (> 150), they will have a very strong effect,
    making the image look "cartoonish".

    Filter size: Large filters (d > 5) are very slow, so it is recommended to
    use d=5 for real-time applications, and perhaps d=9 for offline
    applications that need heavy noise filtering.

    This filter does not work inplace.

    Args:
        src: Source 8-bit or floating-point, 1-channel or 3-channel image.
        dst: Destination image of the same size and type as src.
        d:
            Diameter of each pixel neighborhood that is used during filtering.
            If it is non-positive, it is computed from sigmaSpace.
        sigma_color:
            Filter sigma in the color space. A larger value of the parameter
            means that farther colors within the pixel neighborhood
            (see sigmaSpace) will be mixed together, resulting in larger areas
            of semi-equal color.
        sigma_space:
            Filter sigma in the coordinate space. A larger value of the
            parameter means that farther pixels will influence each other as
            long as their colors are close enough (see sigmaColor). When d > 0,
            it specifies the neighborhood size regardless of sigmaSpace.
            Otherwise, d is proportional to sigmaSpace.
        border_type:
            border mode used to extrapolate pixels outside of the image, see
            BorderTypes
    """
    return cv2.bilateralFilter(  # type: ignore
        src,
        d=d,
        sigmaColor=sigma_color,
        sigmaSpace=sigma_space,
        dst=dst,
        borderType=border_type,
    )


def point_polygon_test(
    contour: np.ndarray,
    pt: Point2f,
    measure_dist: bool,
) -> float:
    """Performs a point-in-contour test.

    The function determines whether the point is inside a contour, outside, or
    lies on an edge (or coincides with a vertex). It returns positive (inside),
    negative (outside), or zero (on an edge) value, correspondingly. When
    measureDist=false , the return value is +1, -1, and 0, respectively.
    Otherwise, the return value is a signed distance between the point and the
    nearest contour edge.

    See below a sample output of the function where each image pixel is tested
    against the contour:

    Args:
        contour: Input contour.
        pt: Point tested against the contour.
        measure_dist:
            If true, the function estimates the signed distance from the point
            to the nearest contour edge. Otherwise, the function only checks if
            the point is inside a contour or not.
    """
    return cv2.pointPolygonTest(contour, pt, measure_dist)  # type: ignore


def contour_area(contour: np.ndarray, oriented: bool = False) -> float:
    """Calculates a contour area.

    The function computes a contour area. Similarly to moments , the area is
    computed using the Green formula. Thus, the returned area and the number of
    non-zero pixels, if you draw the contour using #drawContours or #fillPoly,
    can be different. Also, the function will most certainly give a wrong
    results for contours with self-intersections.

    Args:
        contour:
            Input vector of 2D points (contour vertices), stored in std::vector
            or Mat.
        oriented:
            Oriented area flag. If it is true, the function returns a signed
            area value, depending on the contour orientation (clockwise or
            counter-clockwise). Using this feature you can determine
            orientation of a contour by taking the sign of an area. By default,
            the parameter is false, which means that the absolute value is
            returned.
    """
    return cv2.contourArea(contour, oriented)  # type: ignore
