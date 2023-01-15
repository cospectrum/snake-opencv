import random
import cv2
import snake_opencv as cv
import numpy as np

from typing import Tuple

from .utils import eq


Width = int
Height = int
Size = Tuple[Width, Height]


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
    start_point = (1, 1)
    end_point = (40, 40)
    color = (24, 24, 0)

    left = cv.rectangle(
        test_image,
        start_point,
        end_point,
        color=color,
    )
    right = cv2.rectangle(
        test_image,
        start_point,
        end_point,
        color,
    )
    assert eq(left, right)
    assert not eq(-left, right)


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


def get_size(image: np.ndarray) -> Size:
    return tuple(reversed(image.shape[:2]))  # type: ignore


def random_size(max_width: int = 3000, max_height: int = 3000) -> Size:
    return (random.randint(1, max_width), random.randint(1, max_height))
