import cv2
import numpy as np

from typing import Tuple, Optional


__all__ = [
    'INTER_AREA',
    'INTER_BITS',
    'INTER_BITS2',
    'INTER_CUBIC',
    'INTER_LANCZOS4',
    'INTER_LINEAR',
    'INTER_LINEAR_EXACT',
    'INTER_MAX',
    'INTER_NEAREST',
    'INTER_NEAREST_EXACT',
    'INTER_TAB_SIZE',
    'INTER_TAB_SIZE2',
    'resize',
]


Width = int
Height = int


# resampling using pixel area relation. It may be a preferred method for image decimation, as
# it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_AREA = 3
INTER_BITS = 5
INTER_BITS2 = 10
# bicubic interpolation
INTER_CUBIC = 2
# Lanczos interpolation over 8x8 neighborhood
INTER_LANCZOS4 = 4
# bilinear interpolation
INTER_LINEAR = 1
# Bit exact bilinear interpolation
INTER_LINEAR_EXACT = 5
# mask for interpolation codes
INTER_MAX = 7
# nearest neighbor interpolation
INTER_NEAREST = 0
# Bit exact nearest neighbor interpolation. This will produce same results as
# the nearest neighbor method in PIL, scikit-image or Matlab.
INTER_NEAREST_EXACT = 6
INTER_TAB_SIZE = 32
INTER_TAB_SIZE2 = 1024


def resize(
    src: np.ndarray,
    dsize: Optional[Tuple[Width, Height]] = None,
    dst: Optional[np.ndarray] = None,
    fx: float = 0.,
    fy: float = 0.,
    interpolation: int = INTER_LINEAR,
) -> np.ndarray:
    return cv2.resize(
        src,
        dsize,
        dst,
        fx=fx,
        fy=fy,
        interpolation=interpolation,
    )
