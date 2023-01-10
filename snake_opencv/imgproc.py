import cv2
import numpy as np

from typing import Tuple, Optional, Literal


__all__ = [
    'resize',
    'cvt_color',
    'rectangle',
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
    'COLOR_BGR2BGR555',
    'COLOR_BGR2BGR565',
    'COLOR_BGR2BGRA',
    'COLOR_BGR2GRAY',
    'COLOR_BGR2HLS',
    'COLOR_BGR2HLS_FULL',
    'COLOR_BGR2HSV',
    'COLOR_BGR2HSV_FULL',
    'COLOR_BGR2Lab',
    'COLOR_BGR2Luv',
    'COLOR_BGR2RGB',
    'COLOR_BGR2RGBA',
    'COLOR_BGR2XYZ',
    'COLOR_BGR2YCrCb',
    'COLOR_BGR2YUV',
    'COLOR_BGR2YUV_I420',
    'COLOR_BGR2YUV_IYUV',
    'COLOR_BGR2YUV_YV12',
    'COLOR_BGR5552BGR',
    'COLOR_BGR5552BGRA',
    'COLOR_BGR5552GRAY',
    'COLOR_BGR5552RGB',
    'COLOR_BGR5552RGBA',
    'COLOR_BGR5652BGR',
    'COLOR_BGR5652BGRA',
    'COLOR_BGR5652GRAY',
    'COLOR_BGR5652RGB',
    'COLOR_BGR5652RGBA',
    'COLOR_BGRA2BGR',
    'COLOR_BGRA2BGR555',
    'COLOR_BGRA2BGR565',
    'COLOR_BGRA2GRAY',
    'COLOR_BGRA2RGB',
    'COLOR_BGRA2RGBA',
    'COLOR_BGRA2YUV_I420',
    'COLOR_BGRA2YUV_IYUV',
    'COLOR_BGRA2YUV_YV12',
    'COLOR_BayerBG2BGR',
    'COLOR_BayerBG2BGRA',
    'COLOR_BayerBG2BGR_EA',
    'COLOR_BayerBG2BGR_VNG',
    'COLOR_BayerBG2GRAY',
    'COLOR_BayerBG2RGB',
    'COLOR_BayerBG2RGBA',
    'COLOR_BayerBG2RGB_EA',
    'COLOR_BayerBG2RGB_VNG',
    'COLOR_BayerBGGR2BGR',
    'COLOR_BayerBGGR2BGRA',
    'COLOR_BayerBGGR2BGR_EA',
    'COLOR_BayerBGGR2BGR_VNG',
    'COLOR_BayerBGGR2GRAY',
    'COLOR_BayerBGGR2RGB',
    'COLOR_BayerBGGR2RGBA',
    'COLOR_BayerBGGR2RGB_EA',
    'COLOR_BayerBGGR2RGB_VNG',
    'COLOR_BayerGB2BGR',
    'COLOR_BayerGB2BGRA',
    'COLOR_BayerGB2BGR_EA',
    'COLOR_BayerGB2BGR_VNG',
    'COLOR_BayerGB2GRAY',
    'COLOR_BayerGB2RGB',
    'COLOR_BayerGB2RGBA',
    'COLOR_BayerGB2RGB_EA',
    'COLOR_BayerGB2RGB_VNG',
    'COLOR_BayerGBRG2BGR',
    'COLOR_BayerGBRG2BGRA',
    'COLOR_BayerGBRG2BGR_EA',
    'COLOR_BayerGBRG2BGR_VNG',
    'COLOR_BayerGBRG2GRAY',
    'COLOR_BayerGBRG2RGB',
    'COLOR_BayerGBRG2RGBA',
    'COLOR_BayerGBRG2RGB_EA',
    'COLOR_BayerGBRG2RGB_VNG',
    'COLOR_BayerGR2BGR',
    'COLOR_BayerGR2BGRA',
    'COLOR_BayerGR2BGR_EA',
    'COLOR_BayerGR2BGR_VNG',
    'COLOR_BayerGR2GRAY',
    'COLOR_BayerGR2RGB',
    'COLOR_BayerGR2RGBA',
    'COLOR_BayerGR2RGB_EA',
    'COLOR_BayerGR2RGB_VNG',
    'COLOR_BayerGRBG2BGR',
    'COLOR_BayerGRBG2BGRA',
    'COLOR_BayerGRBG2BGR_EA',
    'COLOR_BayerGRBG2BGR_VNG',
    'COLOR_BayerGRBG2GRAY',
    'COLOR_BayerGRBG2RGB',
    'COLOR_BayerGRBG2RGBA',
    'COLOR_BayerGRBG2RGB_EA',
    'COLOR_BayerGRBG2RGB_VNG',
    'COLOR_BayerRG2BGR',
    'COLOR_BayerRG2BGRA',
    'COLOR_BayerRG2BGR_EA',
    'COLOR_BayerRG2BGR_VNG',
    'COLOR_BayerRG2GRAY',
    'COLOR_BayerRG2RGB',
    'COLOR_BayerRG2RGBA',
    'COLOR_BayerRG2RGB_EA',
    'COLOR_BayerRG2RGB_VNG',
    'COLOR_BayerRGGB2BGR',
    'COLOR_BayerRGGB2BGRA',
    'COLOR_BayerRGGB2BGR_EA',
    'COLOR_BayerRGGB2BGR_VNG',
    'COLOR_BayerRGGB2GRAY',
    'COLOR_BayerRGGB2RGB',
    'COLOR_BayerRGGB2RGBA',
    'COLOR_BayerRGGB2RGB_EA',
    'COLOR_BayerRGGB2RGB_VNG',
    'COLOR_COLORCVT_MAX',
    'COLOR_GRAY2BGR',
    'COLOR_GRAY2BGR555',
    'COLOR_GRAY2BGR565',
    'COLOR_GRAY2BGRA',
    'COLOR_GRAY2RGB',
    'COLOR_GRAY2RGBA',
    'COLOR_HLS2BGR',
    'COLOR_HLS2BGR_FULL',
    'COLOR_HLS2RGB',
    'COLOR_HLS2RGB_FULL',
    'COLOR_HSV2BGR',
    'COLOR_HSV2BGR_FULL',
    'COLOR_HSV2RGB',
    'COLOR_HSV2RGB_FULL',
    'COLOR_LBGR2Lab',
    'COLOR_LBGR2Luv',
    'COLOR_LRGB2Lab',
    'COLOR_LRGB2Luv',
    'COLOR_Lab2BGR',
    'COLOR_Lab2LBGR',
    'COLOR_Lab2LRGB',
    'COLOR_Lab2RGB',
    'COLOR_Luv2BGR',
    'COLOR_Luv2LBGR',
    'COLOR_Luv2LRGB',
    'COLOR_Luv2RGB',
    'COLOR_RGB2BGR',
    'COLOR_RGB2BGR555',
    'COLOR_RGB2BGR565',
    'COLOR_RGB2BGRA',
    'COLOR_RGB2GRAY',
    'COLOR_RGB2HLS',
    'COLOR_RGB2HLS_FULL',
    'COLOR_RGB2HSV',
    'COLOR_RGB2HSV_FULL',
    'COLOR_RGB2Lab',
    'COLOR_RGB2Luv',
    'COLOR_RGB2RGBA',
    'COLOR_RGB2XYZ',
    'COLOR_RGB2YCrCb',
    'COLOR_RGB2YUV',
    'COLOR_RGB2YUV_I420',
    'COLOR_RGB2YUV_IYUV',
    'COLOR_RGB2YUV_YV12',
    'COLOR_RGBA2BGR',
    'COLOR_RGBA2BGR555',
    'COLOR_RGBA2BGR565',
    'COLOR_RGBA2BGRA',
    'COLOR_RGBA2GRAY',
    'COLOR_RGBA2RGB',
    'COLOR_RGBA2YUV_I420',
    'COLOR_RGBA2YUV_IYUV',
    'COLOR_RGBA2YUV_YV12',
    'COLOR_RGBA2mRGBA',
    'COLOR_XYZ2BGR',
    'COLOR_XYZ2RGB',
    'COLOR_YCrCb2BGR',
    'COLOR_YCrCb2RGB',
    'COLOR_YUV2BGR',
    'COLOR_YUV2BGRA_I420',
    'COLOR_YUV2BGRA_IYUV',
    'COLOR_YUV2BGRA_NV12',
    'COLOR_YUV2BGRA_NV21',
    'COLOR_YUV2BGRA_UYNV',
    'COLOR_YUV2BGRA_UYVY',
    'COLOR_YUV2BGRA_Y422',
    'COLOR_YUV2BGRA_YUNV',
    'COLOR_YUV2BGRA_YUY2',
    'COLOR_YUV2BGRA_YUYV',
    'COLOR_YUV2BGRA_YV12',
    'COLOR_YUV2BGRA_YVYU',
    'COLOR_YUV2BGR_I420',
    'COLOR_YUV2BGR_IYUV',
    'COLOR_YUV2BGR_NV12',
    'COLOR_YUV2BGR_NV21',
    'COLOR_YUV2BGR_UYNV',
    'COLOR_YUV2BGR_UYVY',
    'COLOR_YUV2BGR_Y422',
    'COLOR_YUV2BGR_YUNV',
    'COLOR_YUV2BGR_YUY2',
    'COLOR_YUV2BGR_YUYV',
    'COLOR_YUV2BGR_YV12',
    'COLOR_YUV2BGR_YVYU',
    'COLOR_YUV2GRAY_420',
    'COLOR_YUV2GRAY_I420',
    'COLOR_YUV2GRAY_IYUV',
    'COLOR_YUV2GRAY_NV12',
    'COLOR_YUV2GRAY_NV21',
    'COLOR_YUV2GRAY_UYNV',
    'COLOR_YUV2GRAY_UYVY',
    'COLOR_YUV2GRAY_Y422',
    'COLOR_YUV2GRAY_YUNV',
    'COLOR_YUV2GRAY_YUY2',
    'COLOR_YUV2GRAY_YUYV',
    'COLOR_YUV2GRAY_YV12',
    'COLOR_YUV2GRAY_YVYU',
    'COLOR_YUV2RGB',
    'COLOR_YUV2RGBA_I420',
    'COLOR_YUV2RGBA_IYUV',
    'COLOR_YUV2RGBA_NV12',
    'COLOR_YUV2RGBA_NV21',
    'COLOR_YUV2RGBA_UYNV',
    'COLOR_YUV2RGBA_UYVY',
    'COLOR_YUV2RGBA_Y422',
    'COLOR_YUV2RGBA_YUNV',
    'COLOR_YUV2RGBA_YUY2',
    'COLOR_YUV2RGBA_YUYV',
    'COLOR_YUV2RGBA_YV12',
    'COLOR_YUV2RGBA_YVYU',
    'COLOR_YUV2RGB_I420',
    'COLOR_YUV2RGB_IYUV',
    'COLOR_YUV2RGB_NV12',
    'COLOR_YUV2RGB_NV21',
    'COLOR_YUV2RGB_UYNV',
    'COLOR_YUV2RGB_UYVY',
    'COLOR_YUV2RGB_Y422',
    'COLOR_YUV2RGB_YUNV',
    'COLOR_YUV2RGB_YUY2',
    'COLOR_YUV2RGB_YUYV',
    'COLOR_YUV2RGB_YV12',
    'COLOR_YUV2RGB_YVYU',
    'COLOR_YUV420p2BGR',
    'COLOR_YUV420p2BGRA',
    'COLOR_YUV420p2GRAY',
    'COLOR_YUV420p2RGB',
    'COLOR_YUV420p2RGBA',
    'COLOR_YUV420sp2BGR',
    'COLOR_YUV420sp2BGRA',
    'COLOR_YUV420sp2GRAY',
    'COLOR_YUV420sp2RGB',
    'COLOR_YUV420sp2RGBA',
    'COLOR_mRGBA2RGBA',
    'FILLED',
    'LINE_4',
    'LINE_8',
    'LINE_AA',
]

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

# convert between RGB/BGR and BGR555 (16-bit images)
COLOR_BGR2BGR555 = 22
# convert between RGB/BGR and BGR565 (16-bit images)
COLOR_BGR2BGR565 = 12
# add alpha channel to RGB or BGR image
COLOR_BGR2BGRA = 0
# convert between RGB/BGR and grayscale, @ref color_convert_rgb_gray "color conversions"
COLOR_BGR2GRAY = 6
# convert RGB/BGR to HLS (hue lightness saturation) with H range 0..180 if 8 bit image, @ref color_convert_rgb_hls "color conversions"
COLOR_BGR2HLS = 52
# convert RGB/BGR to HLS (hue lightness saturation) with H range 0..255 if 8 bit image, @ref color_convert_rgb_hls "color conversions"
COLOR_BGR2HLS_FULL = 68
# convert RGB/BGR to HSV (hue saturation value) with H range 0..180 if 8 bit image, @ref color_convert_rgb_hsv "color conversions"
COLOR_BGR2HSV = 40
# convert RGB/BGR to HSV (hue saturation value) with H range 0..255 if 8 bit image, @ref color_convert_rgb_hsv "color conversions"
COLOR_BGR2HSV_FULL = 66
# convert RGB/BGR to CIE Lab, @ref color_convert_rgb_lab "color conversions"
COLOR_BGR2Lab = 44
# convert RGB/BGR to CIE Luv, @ref color_convert_rgb_luv "color conversions"
COLOR_BGR2Luv = 50
COLOR_BGR2RGB = 4
# convert between RGB and BGR color spaces (with or without alpha channel)
COLOR_BGR2RGBA = 2
# convert RGB/BGR to CIE XYZ, @ref color_convert_rgb_xyz "color conversions"
COLOR_BGR2XYZ = 32
# convert RGB/BGR to luma-chroma (aka YCC), @ref color_convert_rgb_ycrcb "color conversions"
COLOR_BGR2YCrCb = 36
# convert between RGB/BGR and YUV
COLOR_BGR2YUV = 82
# RGB to YUV 4:2:0 family
COLOR_BGR2YUV_I420 = 128
# RGB to YUV 4:2:0 family
COLOR_BGR2YUV_IYUV = 128
# RGB to YUV 4:2:0 family
COLOR_BGR2YUV_YV12 = 132
COLOR_BGR5552BGR = 24
COLOR_BGR5552BGRA = 28
COLOR_BGR5552GRAY = 31
COLOR_BGR5552RGB = 25
COLOR_BGR5552RGBA = 29
COLOR_BGR5652BGR = 14
COLOR_BGR5652BGRA = 18
COLOR_BGR5652GRAY = 21
COLOR_BGR5652RGB = 15
COLOR_BGR5652RGBA = 19
# remove alpha channel from RGB or BGR image
COLOR_BGRA2BGR = 1
COLOR_BGRA2BGR555 = 26
COLOR_BGRA2BGR565 = 16
COLOR_BGRA2GRAY = 10
COLOR_BGRA2RGB = 3
COLOR_BGRA2RGBA = 5
# RGB to YUV 4:2:0 family
COLOR_BGRA2YUV_I420 = 130
# RGB to YUV 4:2:0 family
COLOR_BGRA2YUV_IYUV = 130
# RGB to YUV 4:2:0 family
COLOR_BGRA2YUV_YV12 = 134
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2BGR = 46
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2BGRA = 139
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2BGR_EA = 135
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2BGR_VNG = 62
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2GRAY = 86
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2RGB = 48
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2RGBA = 141
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2RGB_EA = 137
# equivalent to RGGB Bayer pattern
COLOR_BayerBG2RGB_VNG = 64
COLOR_BayerBGGR2BGR = 48
COLOR_BayerBGGR2BGRA = 141
COLOR_BayerBGGR2BGR_EA = 137
COLOR_BayerBGGR2BGR_VNG = 64
COLOR_BayerBGGR2GRAY = 88
COLOR_BayerBGGR2RGB = 46
COLOR_BayerBGGR2RGBA = 139
COLOR_BayerBGGR2RGB_EA = 135
COLOR_BayerBGGR2RGB_VNG = 62
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2BGR = 47
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2BGRA = 140
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2BGR_EA = 136
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2BGR_VNG = 63
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2GRAY = 87
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2RGB = 49
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2RGBA = 142
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2RGB_EA = 138
# equivalent to GRBG Bayer pattern
COLOR_BayerGB2RGB_VNG = 65
COLOR_BayerGBRG2BGR = 49
COLOR_BayerGBRG2BGRA = 142
COLOR_BayerGBRG2BGR_EA = 138
COLOR_BayerGBRG2BGR_VNG = 65
COLOR_BayerGBRG2GRAY = 89
COLOR_BayerGBRG2RGB = 47
COLOR_BayerGBRG2RGBA = 140
COLOR_BayerGBRG2RGB_EA = 136
COLOR_BayerGBRG2RGB_VNG = 63
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2BGR = 49
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2BGRA = 142
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2BGR_EA = 138
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2BGR_VNG = 65
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2GRAY = 89
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2RGB = 47
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2RGBA = 140
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2RGB_EA = 136
# equivalent to GBRG Bayer pattern
COLOR_BayerGR2RGB_VNG = 63
COLOR_BayerGRBG2BGR = 47
COLOR_BayerGRBG2BGRA = 140
COLOR_BayerGRBG2BGR_EA = 136
COLOR_BayerGRBG2BGR_VNG = 63
COLOR_BayerGRBG2GRAY = 87
COLOR_BayerGRBG2RGB = 49
COLOR_BayerGRBG2RGBA = 142
COLOR_BayerGRBG2RGB_EA = 138
COLOR_BayerGRBG2RGB_VNG = 65
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2BGR = 48
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2BGRA = 141
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2BGR_EA = 137
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2BGR_VNG = 64
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2GRAY = 88
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2RGB = 46
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2RGBA = 139
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2RGB_EA = 135
# equivalent to BGGR Bayer pattern
COLOR_BayerRG2RGB_VNG = 62
COLOR_BayerRGGB2BGR = 46
COLOR_BayerRGGB2BGRA = 139
COLOR_BayerRGGB2BGR_EA = 135
COLOR_BayerRGGB2BGR_VNG = 62
COLOR_BayerRGGB2GRAY = 86
COLOR_BayerRGGB2RGB = 48
COLOR_BayerRGGB2RGBA = 141
COLOR_BayerRGGB2RGB_EA = 137
COLOR_BayerRGGB2RGB_VNG = 64
COLOR_COLORCVT_MAX = 143
COLOR_GRAY2BGR = 8
# convert between grayscale and BGR555 (16-bit images)
COLOR_GRAY2BGR555 = 30
# convert between grayscale to BGR565 (16-bit images)
COLOR_GRAY2BGR565 = 20
COLOR_GRAY2BGRA = 9
COLOR_GRAY2RGB = 8
COLOR_GRAY2RGBA = 9
# backward conversions HLS to RGB/BGR with H range 0..180 if 8 bit image
COLOR_HLS2BGR = 60
# backward conversions HLS to RGB/BGR with H range 0..255 if 8 bit image
COLOR_HLS2BGR_FULL = 72
COLOR_HLS2RGB = 61
COLOR_HLS2RGB_FULL = 73
# backward conversions HSV to RGB/BGR with H range 0..180 if 8 bit image
COLOR_HSV2BGR = 54
# backward conversions HSV to RGB/BGR with H range 0..255 if 8 bit image
COLOR_HSV2BGR_FULL = 70
COLOR_HSV2RGB = 55
COLOR_HSV2RGB_FULL = 71
COLOR_LBGR2Lab = 74
COLOR_LBGR2Luv = 76
COLOR_LRGB2Lab = 75
COLOR_LRGB2Luv = 77
COLOR_Lab2BGR = 56
COLOR_Lab2LBGR = 78
COLOR_Lab2LRGB = 79
COLOR_Lab2RGB = 57
COLOR_Luv2BGR = 58
COLOR_Luv2LBGR = 80
COLOR_Luv2LRGB = 81
COLOR_Luv2RGB = 59
COLOR_RGB2BGR = 4
COLOR_RGB2BGR555 = 23
COLOR_RGB2BGR565 = 13
COLOR_RGB2BGRA = 2
COLOR_RGB2GRAY = 7
COLOR_RGB2HLS = 53
COLOR_RGB2HLS_FULL = 69
COLOR_RGB2HSV = 41
COLOR_RGB2HSV_FULL = 67
COLOR_RGB2Lab = 45
COLOR_RGB2Luv = 51
COLOR_RGB2RGBA = 0
COLOR_RGB2XYZ = 33
COLOR_RGB2YCrCb = 37
COLOR_RGB2YUV = 83
# RGB to YUV 4:2:0 family
COLOR_RGB2YUV_I420 = 127
# RGB to YUV 4:2:0 family
COLOR_RGB2YUV_IYUV = 127
# RGB to YUV 4:2:0 family
COLOR_RGB2YUV_YV12 = 131
COLOR_RGBA2BGR = 3
COLOR_RGBA2BGR555 = 27
COLOR_RGBA2BGR565 = 17
COLOR_RGBA2BGRA = 5
COLOR_RGBA2GRAY = 11
COLOR_RGBA2RGB = 1
# RGB to YUV 4:2:0 family
COLOR_RGBA2YUV_I420 = 129
# RGB to YUV 4:2:0 family
COLOR_RGBA2YUV_IYUV = 129
# RGB to YUV 4:2:0 family
COLOR_RGBA2YUV_YV12 = 133
# alpha premultiplication
COLOR_RGBA2mRGBA = 125
COLOR_XYZ2BGR = 34
COLOR_XYZ2RGB = 35
COLOR_YCrCb2BGR = 38
COLOR_YCrCb2RGB = 39
COLOR_YUV2BGR = 84
# YUV 4:2:0 family to RGB
COLOR_YUV2BGRA_I420 = 105
# YUV 4:2:0 family to RGB
COLOR_YUV2BGRA_IYUV = 105
# YUV 4:2:0 family to RGB
COLOR_YUV2BGRA_NV12 = 95
# YUV 4:2:0 family to RGB
COLOR_YUV2BGRA_NV21 = 97
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_UYNV = 112
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_UYVY = 112
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_Y422 = 112
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_YUNV = 120
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_YUY2 = 120
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_YUYV = 120
# YUV 4:2:0 family to RGB
COLOR_YUV2BGRA_YV12 = 103
# YUV 4:2:2 family to RGB
COLOR_YUV2BGRA_YVYU = 122
# YUV 4:2:0 family to RGB
COLOR_YUV2BGR_I420 = 101
# YUV 4:2:0 family to RGB
COLOR_YUV2BGR_IYUV = 101
# YUV 4:2:0 family to RGB
COLOR_YUV2BGR_NV12 = 91
# YUV 4:2:0 family to RGB
COLOR_YUV2BGR_NV21 = 93
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_UYNV = 108
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_UYVY = 108
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_Y422 = 108
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_YUNV = 116
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_YUY2 = 116
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_YUYV = 116
# YUV 4:2:0 family to RGB
COLOR_YUV2BGR_YV12 = 99
# YUV 4:2:2 family to RGB
COLOR_YUV2BGR_YVYU = 118
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_420 = 106
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_I420 = 106
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_IYUV = 106
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_NV12 = 106
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_NV21 = 106
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_UYNV = 123
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_UYVY = 123
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_Y422 = 123
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_YUNV = 124
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_YUY2 = 124
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_YUYV = 124
# YUV 4:2:0 family to RGB
COLOR_YUV2GRAY_YV12 = 106
# YUV 4:2:2 family to RGB
COLOR_YUV2GRAY_YVYU = 124
COLOR_YUV2RGB = 85
# YUV 4:2:0 family to RGB
COLOR_YUV2RGBA_I420 = 104
# YUV 4:2:0 family to RGB
COLOR_YUV2RGBA_IYUV = 104
# YUV 4:2:0 family to RGB
COLOR_YUV2RGBA_NV12 = 94
# YUV 4:2:0 family to RGB
COLOR_YUV2RGBA_NV21 = 96
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_UYNV = 111
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_UYVY = 111
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_Y422 = 111
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_YUNV = 119
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_YUY2 = 119
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_YUYV = 119
# YUV 4:2:0 family to RGB
COLOR_YUV2RGBA_YV12 = 102
# YUV 4:2:2 family to RGB
COLOR_YUV2RGBA_YVYU = 121
# YUV 4:2:0 family to RGB
COLOR_YUV2RGB_I420 = 100
# YUV 4:2:0 family to RGB
COLOR_YUV2RGB_IYUV = 100
# YUV 4:2:0 family to RGB
COLOR_YUV2RGB_NV12 = 90
# YUV 4:2:0 family to RGB
COLOR_YUV2RGB_NV21 = 92
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_UYNV = 107
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_UYVY = 107
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_Y422 = 107
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_YUNV = 115
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_YUY2 = 115
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_YUYV = 115
# YUV 4:2:0 family to RGB
COLOR_YUV2RGB_YV12 = 98
# YUV 4:2:2 family to RGB
COLOR_YUV2RGB_YVYU = 117
# YUV 4:2:0 family to RGB
COLOR_YUV420p2BGR = 99
# YUV 4:2:0 family to RGB
COLOR_YUV420p2BGRA = 103
# YUV 4:2:0 family to RGB
COLOR_YUV420p2GRAY = 106
# YUV 4:2:0 family to RGB
COLOR_YUV420p2RGB = 98
# YUV 4:2:0 family to RGB
COLOR_YUV420p2RGBA = 102
# YUV 4:2:0 family to RGB
COLOR_YUV420sp2BGR = 93
# YUV 4:2:0 family to RGB
COLOR_YUV420sp2BGRA = 97
# YUV 4:2:0 family to RGB
COLOR_YUV420sp2GRAY = 106
# YUV 4:2:0 family to RGB
COLOR_YUV420sp2RGB = 92
# YUV 4:2:0 family to RGB
COLOR_YUV420sp2RGBA = 96
# alpha premultiplication
COLOR_mRGBA2RGBA = 126

FILLED = -1
# 4-connected line
LINE_4 = 4
# 8-connected line
LINE_8 = 8
# antialiased line
LINE_AA = 16

LineType = Literal[-1, 4, 8, 16]


Width = int
Height = int


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


def cvt_color(
    src: np.ndarray,
    code: int,
    dst: Optional[np.ndarray] = None,
    dst_cn: int = 0,
) -> np.ndarray:
    return cv2.cvtColor(src, code, dst, dst_cn)


X = int
Y = int


def rectangle(
    image: np.ndarray,
    start_point: Tuple[X, Y],
    end_port: Tuple[X, Y],
    color: Tuple,
    thickness: int = 1,
    line_type: LineType = 8,
    shift: int = 0,
) -> np.ndarray:
    return cv2.rectangle(
        image,
        start_point,
        end_port,
        color,
        thickness,
        line_type,
        shift=shift,
    )
