import cv2
import numpy as np

from typing import Optional


__all__ = [
    'fast_nl_means_denoising_colored',
]


def fast_nl_means_denoising_colored(
    src: np.ndarray,
    dst: Optional[np.ndarray] = None,
    h: float = 3.0,
    h_color: float = 3.0,
    template_window_size: int = 7,
    search_window_size: int = 21,
) -> np.ndarray:
    """Modification of fast_nl_means_denoising function for colored images.

    The function converts image to CIELAB colorspace and then separately
    denoise L and AB components with given h parameters using
    fast_nl_means_denoising function.

    Args:
        src: Input 8-bit 3-channel image.
        dst: Output image with the same size and type as src .
        h:
            Parameter regulating filter strength for luminance component.
            Bigger h value perfectly removes noise but also removes image
            details, smaller h value preserves details but also preserves some
            noise
        hColor:
            The same as h but for color components. For most images value
            equals 10 will be enough to remove colored noise and do not
            distort colors
        template_window_size:
            Size in pixels of the template patch that is used to compute
            weights. Should be odd. Recommended value 7 pixels
        search_window_size:
            Size in pixels of the window that is used to compute weighted
            average for given pixel. Should be odd. Affect performance
            linearly: greater searchWindowsSize - greater denoising time.
            Recommended value 21 pixels
    """
    return cv2.fastNlMeansDenoisingColored(
        src,
        dst,
        h,
        h_color,
        template_window_size,
        search_window_size,
    )
