import cv2
import numpy as np

from typing import List, Optional

from .const import IMREAD_COLOR


__all__ = [
    'imread',
    'imwrite',
]


def imread(filename: str, flag: int = IMREAD_COLOR) -> Optional[np.ndarray]:
    """Loads an image from a file.

    The function imread loads an image from the specified file and returns it.
    If the image cannot be read (because of missing file, improper
    permissions, unsupported or invalid format), the function returns an
    empty matrix.

    Currently, the following file formats are supported:
        Windows bitmaps - *.bmp, *.dib (always supported)
        JPEG files - *.jpeg, *.jpg, *.jpe (see the Note section)
        JPEG 2000 files - *.jp2 (see the Note section)
        Portable Network Graphics - *.png (see the Note section)
        WebP - *.webp (see the Note section)
        Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm (always supported)
        PFM files - *.pfm (see the Note section)
        Sun rasters - *.sr, *.ras (always supported)
        TIFF files - *.tiff, *.tif (see the Note section)
        OpenEXR Image files - *.exr (see the Note section)
        Radiance HDR - *.hdr, *.pic (always supported)
        Raster and Vector geospatial data supported by GDAL (see the Note section)

    Note:
        The function determines the type of an image by the content, not by
        the file extension.

        In the case of color images, the decoded images will have the channels
        stored in B G R order.

        When using IMREAD_GRAYSCALE, the codec’s internal grayscale conversion
        will be used, if available. Results may differ to the output of
        cvt_color()

        On Microsoft Windows* OS and MacOSX*, the codecs shipped with an
        OpenCV image (libjpeg, libpng, libtiff, and libjasper) are used by
        default. So, OpenCV can always read JPEGs, PNGs, and TIFFs.
        On MacOSX, there is also an option to use native MacOSX image readers.
        But beware that currently these native image loaders give images with
        different pixel values because of the color management embedded into
        MacOSX.

        On Linux*, BSD flavors and other Unix-like open-source operating
        systems, OpenCV looks for codecs supplied with an OS image. Install
        the relevant packages (do not forget the development files, for
        example, “libjpeg-dev”, in Debian* and Ubuntu*) to get the codec
        support or turn on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.

        In the case you set WITH_GDAL flag to true in CMake and
        IMREAD_LOAD_GDAL to load the image, then the GDAL driver will be used
        in order to decode the image, supporting the following formats:
        Raster, Vector.

        If EXIF information is embedded in the image file, the EXIF
        orientation will be taken into account and thus the image will be
        rotated accordingly except if the flags IMREAD_IGNORE_ORIENTATION or
        IMREAD_UNCHANGED are passed.

        Use the IMREAD_UNCHANGED flag to keep the floating point values from
        PFM image.

        By default number of pixels must be less than 2^30. Limit can be set
        using system variable OPENCV_IO_MAX_IMAGE_PIXELS

    Args:
        filename: Name of file to be loaded.
        flag: Flag that can take values of cv::ImreadModes
    """
    return cv2.imread(filename, flag)


def imwrite(
    filename: str,
    image: np.ndarray,
    params: Optional[List[int]] = None,
) -> bool:
    """Saves an image to a specified file.

    The function imwrite saves the image to the specified file. The image
    format is chosen based on the filename extension (see cv.imread for the
    list of extensions). In general, only 8-bit single-channel or 3-channel
    (with ‘BGR’ channel order) images can be saved using this function, with
    these exceptions:
        16-bit unsigned (CV_16U) images can be saved in the case of PNG, JPEG
        2000, and TIFF formats

        32-bit float (CV_32F) images can be saved in PFM, TIFF, OpenEXR, and
        Radiance HDR formats; 3-channel (CV_32FC3) TIFF images will be saved
        using the LogLuv high dynamic range encoding (4 bytes per pixel)

        PNG images with an alpha channel can be saved using this function. To
        do this, create 8-bit (or 16-bit) 4-channel image BGRA, where the
        alpha channel goes last. Fully transparent pixels should have alpha
        set to 0, fully opaque pixels should have alpha set to 255/65535.

        Multiple images (vector of Mat) can be saved in TIFF format.

    If the image format is not supported, the image will be converted to 8-bit
    unsigned (CV_8U) and saved that way.

    If the format, depth or channel order is different, use cv.cvt_color to
    convert it before saving. Or, use the universal FileStorage I/O functions
    to save the image to XML or YAML format.

    Args:
        filename: Name of the file.
        image: Image or Images to be saved.
        params:
            Format-specific parameters encoded as pairs
            (paramId_1, paramValue_1, paramId_2, paramValue_2, … .)
    """
    return cv2.imwrite(filename, image, params)
