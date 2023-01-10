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


def get_size(image: np.ndarray) -> Size:
    return tuple(reversed(image.shape[:2]))  # type: ignore


def random_size(max_width: int = 3000, max_height: int = 3000) -> Size:
    return (random.randint(1, max_width), random.randint(1, max_height))
