import cv2
import snake_opencv as cv
import numpy as np


def test(image_path: str) -> None:
    left = cv.imread(image_path)
    right = cv2.imread(image_path)
    assert eq(left, right)


def eq(left: np.ndarray, right: np.ndarray) -> bool:
    return (left == right).all()
