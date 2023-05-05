import cv2
import numpy as np

from typing import Optional


__all__ = [
    'absdiff',
    'add',
    'add_weighted',
    'bitwise_and',
    'bitwise_not',
    'bitwise_or',
    'bitwise_xor',
]


def absdiff(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
) -> np.ndarray:
    return cv2.absdiff(src1, src2, dst=dst)


def add(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
    dtype: int = -1,
) -> np.ndarray:
    return cv2.add(src1, src2, dst=dst, mask=mask, dtype=dtype)


def add_weighted(
    src1: np.ndarray,
    alpha: float,
    src2: np.ndarray,
    beta: float,
    gamma: float,
    dst: Optional[np.ndarray] = None,
    dtype: int = -1,
) -> np.ndarray:
    return cv2.addWeighted(
        src1,
        alpha=alpha,
        src2=src2,
        beta=beta,
        gamma=gamma,
        dst=dst,
        dtype=dtype,
    )


def bitwise_and(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    return cv2.bitwise_and(src1, src2, dst=dst, mask=mask)


def bitwise_not(
    src: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    return cv2.bitwise_not(src, dst=dst, mask=mask)


def bitwise_or(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Calculates the per-element bit-wise disjunction of two arrays or an
    array and a scalar.

    The function cv::bitwise_or calculates the per-element bit-wise logical
    disjunction for: Two arrays when src1 and src2 have the same size:

        dst(I) = src1(I) ∨ src2(I)  if mask(I)≠0

    An array and a scalar when src2 is constructed from Scalar or has the same
    number of elements as src1.channels():

        dst(I) = src1(I) ∨ src2  if mask(I)≠0

    A scalar and an array when src1 is constructed from Scalar or has the same
    number of elements as src2.channels():

        dst(I) = src1 ∨ src2(I)  if mask(I)≠0

    In case of floating-point arrays, their machine-specific bit
    representations (usually IEEE754-compliant) are used for the operation.
    In case of multi-channel arrays, each channel is processed independently.
    In the second and third cases above, the scalar is first converted to the
    array type.

    Args:
        src1: first input array or a scalar.
        src2: second input array or a scalar.
        dst: output array that has the same size and type as the input arrays.
        mask:
            optional operation mask, 8-bit single channel array, that specifies
            elements of the output array to be changed.
    """
    return cv2.bitwise_or(src1, src2, dst=dst, mask=mask)


def bitwise_xor(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    return cv2.bitwise_xor(src1, src2, dst=dst, mask=mask)
