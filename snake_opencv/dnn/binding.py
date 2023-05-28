import cv2
import numpy as np


from typing import List, Optional, Tuple

from ..core import CV_32F


__all__ = [
    'blob_from_image',
    'blob_from_images',
]


W = int
H = int


def blob_from_image(
    image: np.ndarray,
    scalefactor: float = 1.0,
    size: Optional[Tuple[W, H]] = None,
    mean: Optional[Tuple[float, ...]] = None,
    swap_rb: bool = False,
    crop: bool = False,
    ddepth: int = CV_32F,
) -> np.ndarray:
    """Creates 4-dimensional blob from image. Optionally resizes and crops
    image from center, subtract mean values, scales values by scalefactor,
    swap Blue and Red channels.

    Args:
        image: input image (with 1-, 3- or 4-channels).
        scalefactor: multiplier for image values.
        size: spatial size for output image
        mean:
            scalar with mean values which are subtracted from channels. Values
            are intended to be in (mean-R, mean-G, mean-B) order if image has
            BGR ordering and swap_rb is true.
        swap_rb:
            flag which indicates that swap first and last channels in
            3-channel image is necessary.
        crop:
            flag which indicates whether image will be cropped after resize or
            not
        ddepth:
            Depth of output blob. Choose CV_32F or CV_8U. If crop is true,
            input image is resized so one side after resize is equal to
            corresponding dimension in size and another one is equal or
            larger. Then, crop from the center is performed. If crop is false,
            direct resize without cropping and preserving aspect ratio is
            performed.

    Returns: 4-dimensional np.array with NCHW dimensions order.
    """
    return cv2.dnn.blobFromImage(  # type: ignore
        image,
        scalefactor,
        size,
        mean=mean,
        swapRB=swap_rb,
        crop=crop,
        ddepth=ddepth,
    )


def blob_from_images(
    images: List[np.ndarray],
    scalefactor: float = 1.0,
    size: Optional[Tuple[W, H]] = None,
    mean: Optional[Tuple[float, ...]] = None,
    swap_rb: bool = False,
    crop: bool = False,
    ddepth: int = CV_32F,
) -> np.ndarray:
    """Creates 4-dimensional blob from image. Optionally resizes and crops
    image from center, subtract mean values, scales values by scalefactor,
    swap Blue and Red channels.

    Args:
        image: input image (with 1-, 3- or 4-channels).
        scalefactor: multiplier for image values.
        size: spatial size for output image
        mean:
            scalar with mean values which are subtracted from channels. Values
            are intended to be in (mean-R, mean-G, mean-B) order if image has
            BGR ordering and swap_rb is true.
        swap_rb:
            flag which indicates that swap first and last channels in
            3-channel image is necessary.
        crop:
            flag which indicates whether image will be cropped after resize or
            not
        ddepth:
            Depth of output blob. Choose CV_32F or CV_8U. If crop is true,
            input image is resized so one side after resize is equal to
            corresponding dimension in size and another one is equal or
            larger. Then, crop from the center is performed. If crop is false,
            direct resize without cropping and preserving aspect ratio is
            performed.

    Returns: 4-dimensional np.array with NCHW dimensions order.
    """
    return cv2.dnn.blobFromImages(  # type: ignore
        images,
        scalefactor,
        size,
        mean=mean,
        swapRB=swap_rb,
        crop=crop,
        ddepth=ddepth,
    )
