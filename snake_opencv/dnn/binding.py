import cv2
import numpy as np


from typing import Optional, Tuple

from ..core import CV_32F


__all__ = [
    'blob_from_image',
]


def blob_from_image(
    image: np.ndarray,
    scalefactor: float = 1.0,
    size: Optional[Tuple[int, int]] = None,
    mean: Optional[Tuple[float, ...]] = None,
    swap_rb: bool = False,
    crop: bool = False,
    ddepth: int = CV_32F,
) -> np.ndarray:
    return cv2.dnn.blobFromImage(
        image,
        scalefactor,
        size,
        mean=mean,
        swapRB=swap_rb,
        crop=crop,
        ddepth=ddepth,
    )
