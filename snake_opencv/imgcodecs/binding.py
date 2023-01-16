import cv2
import numpy as np

from typing import Optional

from .const import IMREAD_COLOR


__all__ = [
    'imread',
    'imwrite',
]


def imread(filename: str, flag: int = IMREAD_COLOR) -> Optional[np.ndarray]:
    return cv2.imread(filename, flag)


def imwrite(filename: str, image: np.ndarray) -> bool:
    return cv2.imwrite(filename, image)
