import os
import cv2
import snake_opencv as cv
import numpy as np


def test_imwrite(image_path: str) -> None:
    save_path = 'tmp.png'
    image = cv.imread(image_path)
    result = cv.imwrite(save_path, image)
    assert result is True, f'{result=}'
    os.remove(save_path)


def test_imread(image_path: str) -> None:
    left = cv.imread(image_path)
    right = cv2.imread(image_path)
    assert eq(left, right)


def eq(left: np.ndarray, right: np.ndarray) -> bool:
    return (left == right).all()
