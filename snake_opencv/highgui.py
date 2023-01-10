import cv2
import numpy as np


__all__ = [
    'imshow',
]


def imshow(window_name: str, image: np.ndarray) -> None:
    return cv2.imshow(window_name, image)
