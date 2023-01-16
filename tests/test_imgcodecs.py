import os
import cv2
import snake_opencv as cv

from .utils import eq


def test_imwrite(image_path: str) -> None:
    save_path = 'tmp.png'
    image = cv.imread(image_path)
    assert image is not None
    result = cv.imwrite(save_path, image)
    assert result is True, f'{result=}'
    os.remove(save_path)


def test_imread(image_path: str) -> None:
    left = cv.imread(image_path)
    assert left is not None
    right = cv2.imread(image_path)
    assert eq(left, right)
