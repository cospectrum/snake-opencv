import random
import cv2
import snake_opencv as cv
import numpy as np

from typing import Tuple

from .utils import eq


Width = int
Height = int
Size = Tuple[Width, Height]


def get_size(image: np.ndarray) -> Size:
    return tuple(reversed(image.shape[:2]))  # type: ignore


def random_size(max_width: int = 3000, max_height: int = 3000) -> Size:
    return (random.randint(1, max_width), random.randint(1, max_height))


def test_resize(test_image: np.ndarray) -> None:
    img = test_image.copy()
    original_size = get_size(img)

    size = random_size()
    left = cv.resize(img, size)
    right = cv2.resize(img, size)

    assert get_size(img) == original_size
    assert get_size(left) == size
    assert get_size(left) == get_size(right)
    assert eq(left, right)


def test_cvt_color(test_image: np.ndarray) -> None:
    left = cv.cvt_color(test_image, cv.COLOR_BGR2RGB)
    right = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
    assert eq(left, right)


def test_rectangle(test_image: np.ndarray) -> None:
    pt1 = (1, 1)
    pt2 = (40, 40)
    color = (0, 5, 25)

    left = cv.rectangle(
        test_image,
        pt1,
        pt2,
        color=color,
    )
    right = cv2.rectangle(
        test_image,
        pt1,
        pt2,
        color,
    )
    assert eq(left, right)

    image = cv.cvt_color(test_image, cv.COLOR_BGR2GRAY)
    left = cv.rectangle(
        image,
        pt1,
        pt2,
        color
    )
    right = cv2.rectangle(
        image,
        pt1,
        pt2,
        color
    )
    assert eq(left, right)


def test_circle(test_image: np.ndarray) -> None:
    center = (5, 5)
    radius = 3
    color = 100
    left = cv.circle(test_image, center=center, radius=radius, color=color)
    right = cv2.circle(test_image, center=center, radius=radius, color=color)
    assert eq(left, right)


def test_put_text(test_image: np.ndarray) -> None:
    text = 'text'
    org = (10, 10)
    font = cv.FONT_HERSHEY_COMPLEX
    thickness = 2
    color = (255, 0, 0)
    image = cv.put_text(
        test_image.copy(),
        text,
        org,
        font,
        font_scale=1,
        color=color,
        thickness=thickness,
    )
    cv.imshow('put text', image)
    cv.wait_key(1000)


def test_canny(test_image: np.ndarray) -> None:
    threshold1 = 30
    threshold2 = 200
    left = cv.canny(test_image, threshold1, threshold2)
    assert isinstance(left, np.ndarray)
    right = cv2.Canny(test_image, threshold1, threshold2)
    assert eq(left, right)


def test_contours(test_image: np.ndarray) -> None:
    edges = cv.canny(test_image, 30, 200)
    contours, hierarchy = cv.find_contours(
        edges,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_NONE,
    )
    right_contours, right_hierarchy = cv2.findContours(  # type: ignore
        edges,
        cv2.RETR_EXTERNAL,  # type: ignore
        cv2.CHAIN_APPROX_NONE,  # type: ignore
    )
    for left, right in zip(contours, right_contours):  # type: ignore
        assert eq(left, right)

    assert eq(hierarchy, right_hierarchy)
    cv.draw_contours(edges, contours, contour_idx=-1, color=(0, 255, 0))
    cv.imshow('contours', edges)
    cv.wait_key(1000)


def test_gaussian_blur(test_image: np.ndarray) -> None:
    ksize = (3, 3)
    sigma_x = 0.
    left = cv.gaussian_blur(test_image, ksize, sigma_x)
    right = cv2.GaussianBlur(test_image, ksize, sigma_x)
    assert eq(left, right)


def test_hough_lines(chess_board: np.ndarray) -> None:
    rho = 1.
    theta = 3.1415 / 180
    threshold = 150
    image = cv.canny(chess_board, 100, 200)

    left = cv.hough_lines(image, rho, theta, threshold)
    right = cv2.HoughLines(image, rho, theta, threshold)
    assert left is not None
    assert eq(left, right)


def test_hough_lines_p(chess_board: np.ndarray) -> None:
    image = cv.canny(chess_board, 100, 200)
    rho = 1.
    theta = 3.1415 / 180
    threshold = 150

    left = cv.hough_lines_p(image, rho, theta, threshold)
    right = cv2.HoughLinesP(image, rho, theta, threshold)
    assert left is not None
    assert eq(left, right)

    color = (0, 255, 0)
    for points in left:
        x1, y1, x2, y2 = points[0]
        pt1 = (x1, y1)
        pt2 = (x2, y2)
        cv.line(image, pt1, pt2, color)

    cv.imshow('hough_lines_p', image)
    cv.wait_key(1000)


def test_rect() -> None:
    points = np.array([[0, 0], [3, 0], [3, 3], [0, 3]])
    left_rect = cv.min_area_rect(points)
    right_rect = cv2.minAreaRect(points)
    assert left_rect == right_rect

    left_box = cv.box_points(left_rect)
    right_box = cv2.boxPoints(left_rect)
    assert eq(left_box, right_box)


def test_perspective(chess_board: np.ndarray) -> None:
    # top-left, top-right, bottom-right, bottom-left
    src = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ]).astype(np.float32)
    dst = 2 * src

    transform = cv.get_perspective_transform(src, dst)
    right_transform = cv2.getPerspectiveTransform(src, dst)
    assert eq(transform, right_transform)

    result = cv.warp_perspective(
        chess_board,
        transform,
        dsize=get_size(chess_board),
    )
    right_result = cv2.warpPerspective(
        chess_board,
        transform,
        dsize=get_size(chess_board),
    )
    assert eq(result, right_result)

    cv.imshow('chess_board', chess_board)
    cv.imshow('transformed chess_board', result)
    cv.wait_key(4000)


def test_fill_poly(test_image: np.ndarray) -> None:
    poly = [(2 * x, 2 * x + 1) for x in range(50)]
    array = np.array(poly)
    pts = [array]
    color = 0

    left = cv.fill_poly(test_image.copy(), pts, color)
    right = cv2.fillPoly(test_image.copy(), pts, color)
    assert eq(left, right)


def test_laplacian(test_image: np.ndarray) -> None:
    left = cv.laplacian(test_image, cv.CV_64F)
    right = cv2.Laplacian(test_image, cv2.CV_64F)
    assert eq(left, right)


def test_threshold(test_image: np.ndarray) -> None:
    left = cv.threshold(test_image, 120, 255, cv.THRESH_BINARY)
    right = cv2.threshold(test_image, 120, 255, cv.THRESH_BINARY)

    assert left[0] == right[0]
    assert eq(left[1], right[1])


def test_connected_components_with_stats(gray_image: np.ndarray) -> None:
    left_val, *left = cv.connected_components_with_stats(gray_image.copy())
    right_val, *right = cv2.connectedComponentsWithStats(gray_image.copy())

    assert left_val == right_val

    for lval, rval in zip(left, right):
        assert eq(lval, rval)


def test_connected_components(gray_image: np.ndarray) -> None:
    left = cv.connected_components(gray_image.copy())
    right = cv2.connectedComponents(gray_image.copy())  # type: ignore

    assert left[0] == right[0]
    assert eq(left[1], right[1])
    assert isinstance(left[0], int)


def test_match_template(gray_image: np.ndarray) -> None:
    w, h = get_size(gray_image)
    rand_w = random.randint(1, w - 1)
    rand_h = random.randint(1, w - 1)
    templ = gray_image[rand_h:h, rand_w:w]

    method = cv.TM_CCOEFF
    assert method == cv2.TM_CCOEFF  # type: ignore

    left = cv.match_template(gray_image, templ, method=method)
    right = cv2.matchTemplate(gray_image, templ, method=method)
    assert eq(left, right)


def test_warp_affine(gray_image: np.ndarray) -> None:
    src = gray_image
    src_ = np.array([
        [0, 0],
        [src.shape[1] - 1, 0], [0, src.shape[0] - 1]
    ]).astype(np.float32)
    dst = np.array([
        [0, src.shape[1] * 0.33],
        [src.shape[1] * 0.85, src.shape[0] * 0.25],
        [src.shape[1] * 0.15, src.shape[0] * 0.7],
    ]).astype(np.float32)

    warp_mat = cv.get_affine_transform(src_, dst)
    expect = cv2.getAffineTransform(src_, dst)  # type: ignore
    assert eq(warp_mat, expect)

    h, w, *_ = src.shape
    shape = (w, h)

    left = cv.warp_affine(src_, warp_mat, shape)
    right = cv2.warpAffine(src_, warp_mat, shape)  # type: ignore
    assert eq(left, right)


def test_get_rotation_matrix_2d() -> None:
    w, h = random_size()
    center = (w / 2, h / 2)
    angle = random.uniform(-180, 180)
    scale = random.uniform(0, 10)

    left = cv.get_rotation_matrix_2d(center, angle, scale=scale)
    right = cv2.getRotationMatrix2D(center, angle, scale=scale)  # type: ignore
    assert eq(left, right)


def test_median_blur(gray_image: np.ndarray) -> None:
    ksize = 3
    left = cv.median_blur(gray_image, ksize)
    right = cv2.medianBlur(gray_image, ksize)  # type: ignore
    assert eq(left, right)


def test_blur(gray_image: np.ndarray) -> None:
    ksize = (3, 3)
    left = cv.blur(gray_image, ksize)
    right = cv2.blur(gray_image, ksize)  # type: ignore
    assert eq(left, right)


def test_bilateral_filter(gray_image: np.ndarray) -> None:
    d = 11
    sigma_color = 21
    sigma_space = 7

    left = cv.bilateral_filter(gray_image, d, sigma_color, sigma_space)
    right = cv2.bilateralFilter(gray_image, d, sigma_color, sigma_space)
    assert eq(left, right)


def test_point_polygon_test(gray_image: np.ndarray) -> None:
    contours, _ = cv.find_contours(
        gray_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    contour = contours[0]

    h, w = gray_image.shape
    point = (random.randint(0, w), random.randint(0, h))

    left = cv.point_polygon_test(contour, point, measure_dist=True)
    assert isinstance(left, float)
    right = cv2.pointPolygonTest(contour, point, True)  # type: ignore

    assert left == right


def test_contour_area(gray_image: np.ndarray) -> None:
    contours, _ = cv.find_contours(
        gray_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    contour = contours[0]
    left = cv.contour_area(contour)
    right = cv2.contourArea(contour)  # type: ignore
    assert left == right
    assert isinstance(left, float)


def test_convex_hull(gray_image: np.ndarray) -> None:
    contours, _ = cv.find_contours(
        gray_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    contour = contours[0]
    left = cv.convex_hull(contour)
    right = cv2.convexHull(contour)  # type: ignore
    assert eq(left, right)


def test_arc_length(gray_image: np.ndarray) -> None:
    contours, _ = cv.find_contours(
        gray_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    curve = contours[0]
    closed = True
    left = cv.arc_length(curve, closed)
    right = cv2.arcLength(curve, closed)  # type: ignore
    assert isinstance(left, float)
    assert left == right


def test_approx_poly_dp(gray_image: np.ndarray) -> None:
    contours, _ = cv.find_contours(
        gray_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    curve = contours[0]
    closed = True
    eps = 0.01 * cv.arc_length(curve, closed)
    left = cv.approx_poly_dp(curve, eps, closed)
    right = cv2.approxPolyDP(curve, eps, closed)  # type: ignore
    assert eq(left, right)
