import random
import cv2
import snake_opencv as cv

import numpy as np


from .utils import eq, random_image


def test_bitwise_or() -> None:
    w = random.randint(1, 1000)
    h = random.randint(1, 1000)

    img1 = random_image(h, w)
    img2 = random_image(h, w)

    left = cv.bitwise_or(img1, img2)
    right = cv2.bitwise_or(img1, img2)

    assert eq(left, right)
