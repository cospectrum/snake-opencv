import cv2
import numpy as np

from typing import Optional, Tuple


__all__ = [
    'absdiff',
    'add',
    'add_weighted',
    'bitwise_and',
    'bitwise_not',
    'bitwise_or',
    'bitwise_xor',
    'min_max_loc',
]


def absdiff(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Calculates the per-element absolute difference between two arrays or
    between an array and a scalar.

    The function cv::absdiff calculates: Absolute difference between two arrays
    when they have the same size and type:

        dst(I) = saturate(|src1(I) − src2(I)|)

    Absolute difference between an array and a scalar when the second array is
    constructed from Scalar or has as many elements as the number of channels
    in src1:

        dst(I) = saturate(|src1(I) − src2|)

    Absolute difference between a scalar and an array when the first array is
    constructed from Scalar or has as many elements as the number of channels
    in src2:

        dst(I) = saturate(|src1 − src2(I)|)

    where I is a multi-dimensional index of array elements. In case of
    multi-channel arrays, each channel is processed independently.

    Note: Saturation is not applied when the arrays have the depth CV_32S.
    You may even get a negative value in the case of overflow.

    Args:
        src1: first input array or a scalar.
        src2: second input array or a scalar.
        dst: output array that has the same size and type as input arrays.
    """
    return cv2.absdiff(src1, src2, dst=dst)


def add(
    src1: np.ndarray,
    src2: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
    dtype: int = -1,
) -> np.ndarray:
    """Calculates the per-element sum of two arrays or an array and a scalar.

    The function add calculates: Sum of two arrays when both input arrays have
    the same size and the same number of channels:

        dst(I) = saturate(src1(I) + src2(I))  if mask(I)≠0

    Sum of an array and a scalar when src2 is constructed from Scalar or has
    the same number of elements as src1.channels():

        dst(I) = saturate(src1(I) + src2)  if mask(I)≠0

    Sum of a scalar and an array when src1 is constructed from Scalar or has
    the same number of elements as src2.channels():

        dst(I) = saturate(src1 + src2(I))  if mask(I)≠0

    where I is a multi-dimensional index of array elements. In case of
    multi-channel arrays, each channel is processed independently.

    The first function in the list above can be replaced with matrix
    expressions:

       dst = src1 + src2;
       dst += src1; // equivalent to add(dst, src1, dst);

    The input arrays and the output array can all have the same or different
    depths. For example, you can add a 16-bit unsigned array to a 8-bit signed
    array and store the sum as a 32-bit floating-point array. Depth of the
    output array is determined by the dtype parameter. In the second and third
    cases above, as well as in the first case, when
    src1.depth() == src2.depth(), dtype can be set to the default -1. In this
    case, the output array will have the same depth as the input array, be it
    src1, src2 or both.

    Note: Saturation is not applied when the output array has the depth CV_32S.
    You may even get result of an incorrect sign in the case of overflow.

    Args:
        src1: first input array or a scalar.
        src2: second input array or a scalar.
        dst:
            output array that has the same size and number of channels as the
            input array(s); the depth is defined by dtype or src1/src2.
        mask:
            optional operation mask - 8-bit single channel array, that
            specifies elements of the output array to be changed.
        dtype: optional depth of the output array (see the discussion below).
    """
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
    """Calculates the weighted sum of two arrays.

    The function addWeighted calculates the weighted sum of two arrays as
    follows:

        dst(I) = saturate(src1(I)∗alpha + src2(I)∗beta + gamma)

    where I is a multi-dimensional index of array elements. In case of
    multi-channel arrays, each channel is processed independently. The function
    can be replaced with a matrix expression:

        dst = src1*alpha + src2*beta + gamma;

    Note: Saturation is not applied when the output array has the depth CV_32S.
    You may even get result of an incorrect sign in the case of overflow.

    Args:
        src1: first input array.
        alpha: weight of the first array elements.
        src2: second input array of the same size and channel number as src1.
        beta: weight of the second array elements.
        gamma: scalar added to each sum.
        dst:
            output array that has the same size and number of channels as the
            input arrays.
        dtype:
            optional depth of the output array; when both input arrays have the
            same depth, dtype can be set to -1, which will be equivalent to
            src1.depth().
    """
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
    """computes bitwise conjunction of the two arrays (dst = src1 & src2)
    Calculates the per-element bit-wise conjunction of two arrays or an array
    and a scalar.

    The function cv::bitwise_and calculates the per-element bit-wise logical
    conjunction for: Two arrays when src1 and src2 have the same size:

        dst(I) = src1(I) ∧ src2(I)  if mask(I)≠0

    An array and a scalar when src2 is constructed from Scalar or has the same
    number of elements as src1.channels():

        dst(I) = src1(I) ∧ src2  if mask(I)≠0

    A scalar and an array when src1 is constructed from Scalar or has the same
    number of elements as src2.channels():

        dst(I) = src1 ∧ src2(I)  if mask(I)≠0

    In case of floating-point arrays, their machine-specific bit
    representations (usually IEEE754-compliant) are used for the operation. In
    case of multi-channel arrays, each channel is processed independently. In
    the second and third cases above, the scalar is first converted to the
    array type.

    Args:
        src1: first input array or a scalar.
        src2: second input array or a scalar.
        dst: output array that has the same size and type as the input arrays.
        mask:
            optional operation mask, 8-bit single channel array, that specifies
            elements of the output array to be changed.
    """
    return cv2.bitwise_and(src1, src2, dst=dst, mask=mask)


def bitwise_not(
    src: np.ndarray,
    dst: Optional[np.ndarray] = None,
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Inverts every bit of an array.

    The function cv::bitwise_not calculates per-element bit-wise inversion of
    the input array:

        dst(I) = ¬src(I)

    In case of a floating-point input array, its machine-specific bit
    representation (usually IEEE754-compliant) is used for the operation. In
    case of multi-channel arrays, each channel is processed independently.

    Args:
        src: input array.
        dst: output array that has the same size and type as the input array.
        mask:
            optional operation mask, 8-bit single channel array, that specifies
            elements of the output array to be changed.
    """
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
    """Calculates the per-element bit-wise "exclusive or" operation on two
    arrays or an array and a scalar.

    The function cv::bitwise_xor calculates the per-element bit-wise logical
    "exclusive-or" operation for: Two arrays when src1 and src2 have the same
    size:

        dst(I) = src1(I) ⊕ src2(I)  if mask(I)≠0

    An array and a scalar when src2 is constructed from Scalar or has the same
    number of elements as src1.channels():

        dst(I) = src1(I) ⊕ src2  if mask(I)≠0

    A scalar and an array when src1 is constructed from Scalar or has the same
    number of elements as src2.channels():

        dst(I) = src1 ⊕ src2(I)  if mask(I)≠0

    In case of floating-point arrays, their machine-specific bit
    representations (usually IEEE754-compliant) are used for the operation. In
    case of multi-channel arrays, each channel is processed independently. In
    the 2nd and 3rd cases above, the scalar is first converted to the array
    type.

    Args:
        src1: first input array or a scalar.
        src2: second input array or a scalar.
        dst: output array that has the same size and type as the input arrays.
        mask:
            optional operation mask, 8-bit single channel array, that specifies
            elements of the output array to be changed.
    """
    return cv2.bitwise_xor(src1, src2, dst=dst, mask=mask)


X = int
Y = int

MinVal = float
MaxVal = float
MinLoc = Tuple[X, Y]
MaxLoc = Tuple[X, Y]


def min_max_loc(
    src: np.ndarray,
    mask: Optional[np.ndarray] = None,
) -> Tuple[MinVal, MaxVal, MinLoc, MaxLoc]:
    """Finds the global minimum and maximum in an array.

    The function cv::minMaxLoc finds the minimum and maximum element values and
    their positions. The extremums are searched across the whole array or, if
    mask is not an empty array, in the specified array region.

    The function do not work with multi-channel arrays. If you need to find
    minimum or maximum elements across all the channels, use Mat::reshape first
    to reinterpret the array as single-channel. Or you may extract the
    particular channel using either extractImageCOI, or mixChannels, or split.

    Args:
        src: input single-channel array.
        minVal:
            pointer to the returned minimum value; NULL is used if not
            required.
        maxVal:
            pointer to the returned maximum value; NULL is used if not
            required.
        minLoc:
            pointer to the returned minimum location (in 2D case); NULL is used
            if not required.
        maxLoc:
            pointer to the returned maximum location (in 2D case); NULL is used
            if not required.
        mask: optional mask used to select a sub-array.
    """
    return cv2.minMaxLoc(src, mask)
