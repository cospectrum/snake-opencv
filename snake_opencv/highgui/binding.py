import cv2
import numpy as np

from .const import WINDOW_AUTOSIZE


__all__ = [
    'destroy_all_windows',
    'destroy_window',
    'named_window',
    'imshow',
    'resize_window',
    'wait_key',
]


def imshow(window_name: str, image: np.ndarray) -> None:
    cv2.imshow(window_name, image)


def destroy_all_windows() -> None:
    cv2.destroyAllWindows()


def destroy_window(window_name: str) -> None:
    cv2.destroyWindow(window_name)


def named_window(window_name: str, flag: int = WINDOW_AUTOSIZE) -> None:
    cv2.namedWindow(window_name, flag)


def resize_window(window_name: str, width: int, height: int) -> None:
    cv2.resizeWindow(window_name, width, height)


def wait_key(delay: int = 0) -> int:
    return cv2.waitKey(delay)
