import random
import cv2
import snake_opencv as cv

import numpy as np


from .utils import eq, random_image


w = random.randint(1, 1000)
h = random.randint(1, 1000)

img1 = random_image(h, w)
img2 = random_image(h, w)


def test_absdiff() -> None:
    left = cv.absdiff(img1, img2)
    right = cv2.absdiff(img1, img2)
    assert eq(left, right)


def test_add() -> None:
    left = cv.add(img1, img2)
    right = cv2.add(img1, img2)
    assert eq(left, right)


def test_add_weighted() -> None:
    alpha = random.random()
    beta = random.random()
    gamma = random.random()
    left = cv.add_weighted(img1, alpha, img2, beta, gamma)
    right = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    assert eq(left, right)


def test_bitwise_and() -> None:
    left = cv.bitwise_and(img1, img2)
    right = cv2.bitwise_and(img1, img2)
    assert eq(left, right)


def test_bitwise_not() -> None:
    left = cv.bitwise_not(img1)
    right = cv2.bitwise_not(img1)
    assert eq(left, right)


def test_bitwise_or() -> None:
    left = cv.bitwise_or(img1, img2)
    right = cv2.bitwise_or(img1, img2)
    assert eq(left, right)


def test_bitwise_xor() -> None:
    left = cv.bitwise_xor(img1, img2)
    right = cv2.bitwise_xor(img1, img2)
    assert eq(left, right)


def test_min_max_loc() -> None:
    x = np.random.random(100)
    left = cv.min_max_loc(x)
    right = cv2.minMaxLoc(x)
    assert left == right
