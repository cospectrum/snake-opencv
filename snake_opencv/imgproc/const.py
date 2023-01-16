# #getGaussianKernel
ADAPTIVE_THRESH_GAUSSIAN_C = 1
# the threshold value ![inline formula](https://latex.codecogs.com/png.latex?T%28x%2Cy%29) is a mean of the ![inline formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7BblockSize%7D%20%5Ctimes%0A%5Ctexttt%7BblockSize%7D) neighborhood of ![inline formula](https://latex.codecogs.com/png.latex?%28x%2C%20y%29) minus C
ADAPTIVE_THRESH_MEAN_C = 0
# Same as CCL_GRANA. It is preferable to use the flag with the name of the algorithm (CCL_BBDT) rather than the one with the name of the first author (CCL_GRANA).
CCL_BBDT = 4
# Spaghetti [Bolelli2019](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2019) algorithm for 8-way connectivity, Spaghetti4C [Bolelli2021](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2021) algorithm for 4-way connectivity. The parallel implementation described in [Bolelli2017](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2017) is available for both Spaghetti and Spaghetti4C.
CCL_BOLELLI = 2
# Spaghetti [Bolelli2019](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2019) algorithm for 8-way connectivity, Spaghetti4C [Bolelli2021](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2021) algorithm for 4-way connectivity.
CCL_DEFAULT = -1
# BBDT [Grana2010](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Grana2010) algorithm for 8-way connectivity, SAUF algorithm for 4-way connectivity. The parallel implementation described in [Bolelli2017](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2017) is available for both BBDT and SAUF.
CCL_GRANA = 1
# Same as CCL_WU. It is preferable to use the flag with the name of the algorithm (CCL_SAUF) rather than the one with the name of the first author (CCL_WU).
CCL_SAUF = 3
# Same as CCL_BOLELLI. It is preferable to use the flag with the name of the algorithm (CCL_SPAGHETTI) rather than the one with the name of the first author (CCL_BOLELLI).
CCL_SPAGHETTI = 5
# SAUF [Wu2009](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Wu2009) algorithm for 8-way connectivity, SAUF algorithm for 4-way connectivity. The parallel implementation described in [Bolelli2017](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Bolelli2017) is available for SAUF.
CCL_WU = 0
# The total area (in pixels) of the connected component
CC_STAT_AREA = 4
# The vertical size of the bounding box
CC_STAT_HEIGHT = 3
# The leftmost (x) coordinate which is the inclusive start of the bounding
# box in the horizontal direction.
CC_STAT_LEFT = 0
# Max enumeration value. Used internally only for memory allocation
CC_STAT_MAX = 5
# The topmost (y) coordinate which is the inclusive start of the bounding
# box in the vertical direction.
CC_STAT_TOP = 1
# The horizontal size of the bounding box
CC_STAT_WIDTH = 2
# stores absolutely all the contour points. That is, any 2 subsequent points (x1,y1) and
# (x2,y2) of the contour will be either horizontal, vertical or diagonal neighbors, that is,
# max(abs(x1-x2),abs(y2-y1))==1.
CHAIN_APPROX_NONE = 1
# compresses horizontal, vertical, and diagonal segments and leaves only their end points.
# For example, an up-right rectangular contour is encoded with 4 points.
CHAIN_APPROX_SIMPLE = 2
# applies one of the flavors of the Teh-Chin chain approximation algorithm [TehChin89](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_TehChin89)
CHAIN_APPROX_TC89_KCOS = 4
# applies one of the flavors of the Teh-Chin chain approximation algorithm [TehChin89](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_TehChin89)
CHAIN_APPROX_TC89_L1 = 3
# ![autumn](https://docs.opencv.org/4.7.0/colorscale_autumn.jpg)
COLORMAP_AUTUMN = 0
# ![bone](https://docs.opencv.org/4.7.0/colorscale_bone.jpg)
COLORMAP_BONE = 1
# ![cividis](https://docs.opencv.org/4.7.0/colorscale_cividis.jpg)
COLORMAP_CIVIDIS = 17
# ![cool](https://docs.opencv.org/4.7.0/colorscale_cool.jpg)
COLORMAP_COOL = 8
# ![deepgreen](https://docs.opencv.org/4.7.0/colorscale_deepgreen.jpg)
COLORMAP_DEEPGREEN = 21
# ![hot](https://docs.opencv.org/4.7.0/colorscale_hot.jpg)
COLORMAP_HOT = 11
# ![HSV](https://docs.opencv.org/4.7.0/colorscale_hsv.jpg)
COLORMAP_HSV = 9
# ![inferno](https://docs.opencv.org/4.7.0/colorscale_inferno.jpg)
COLORMAP_INFERNO = 14
# ![jet](https://docs.opencv.org/4.7.0/colorscale_jet.jpg)
COLORMAP_JET = 2
# ![magma](https://docs.opencv.org/4.7.0/colorscale_magma.jpg)
COLORMAP_MAGMA = 13
# ![ocean](https://docs.opencv.org/4.7.0/colorscale_ocean.jpg)
COLORMAP_OCEAN = 5
# ![parula](https://docs.opencv.org/4.7.0/colorscale_parula.jpg)
COLORMAP_PARULA = 12
# ![pink](https://docs.opencv.org/4.7.0/colorscale_pink.jpg)
COLORMAP_PINK = 10
# ![plasma](https://docs.opencv.org/4.7.0/colorscale_plasma.jpg)
COLORMAP_PLASMA = 15
# ![rainbow](https://docs.opencv.org/4.7.0/colorscale_rainbow.jpg)
COLORMAP_RAINBOW = 4
# ![spring](https://docs.opencv.org/4.7.0/colorscale_spring.jpg)
COLORMAP_SPRING = 7
# ![summer](https://docs.opencv.org/4.7.0/colorscale_summer.jpg)
COLORMAP_SUMMER = 6
# ![turbo](https://docs.opencv.org/4.7.0/colorscale_turbo.jpg)
COLORMAP_TURBO = 20
# ![twilight](https://docs.opencv.org/4.7.0/colorscale_twilight.jpg)
COLORMAP_TWILIGHT = 18
# ![twilight shifted](https://docs.opencv.org/4.7.0/colorscale_twilight_shifted.jpg)
COLORMAP_TWILIGHT_SHIFTED = 19
# ![viridis](https://docs.opencv.org/4.7.0/colorscale_viridis.jpg)
COLORMAP_VIRIDIS = 16
# ![winter](https://docs.opencv.org/4.7.0/colorscale_winter.jpg)
COLORMAP_WINTER = 3
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
# ![block formula](https://latex.codecogs.com/png.latex?I%5F1%28A%2CB%29%20%3D%20%20%5Csum%20%5F%7Bi%3D1%2E%2E%2E7%7D%20%20%5Cleft%20%7C%20%20%5Cfrac%7B1%7D%7Bm%5EA%5Fi%7D%20%2D%20%20%5Cfrac%7B1%7D%7Bm%5EB%5Fi%7D%20%5Cright%20%7C)
CONTOURS_MATCH_I1 = 1
# ![block formula](https://latex.codecogs.com/png.latex?I%5F2%28A%2CB%29%20%3D%20%20%5Csum%20%5F%7Bi%3D1%2E%2E%2E7%7D%20%20%5Cleft%20%7C%20m%5EA%5Fi%20%2D%20m%5EB%5Fi%20%20%5Cright%20%7C)
CONTOURS_MATCH_I2 = 2
# ![block formula](https://latex.codecogs.com/png.latex?I%5F3%28A%2CB%29%20%3D%20%20%5Cmax%20%5F%7Bi%3D1%2E%2E%2E7%7D%20%20%5Cfrac%7B%20%5Cleft%7C%20m%5EA%5Fi%20%2D%20m%5EB%5Fi%20%5Cright%7C%20%7D%7B%20%5Cleft%7C%20m%5EA%5Fi%20%5Cright%7C%20%7D)
CONTOURS_MATCH_I3 = 3
# distance = max(|x1-x2|,|y1-y2|)
DIST_C = 3
# distance = c^2(|x|/c-log(1+|x|/c)), c = 1.3998
DIST_FAIR = 5
# distance = |x|<c ? x^2/2 : c(|x|-c/2), c=1.345
DIST_HUBER = 7
# distance = |x1-x2| + |y1-y2|
DIST_L1 = 1
# L1-L2 metric: distance = 2(sqrt(1+x*x/2) - 1))
DIST_L12 = 4
# the simple euclidean distance
DIST_L2 = 2
# each connected component of zeros in src (as well as all the non-zero pixels closest to the
# connected component) will be assigned the same label
DIST_LABEL_CCOMP = 0
# each zero pixel (and all the non-zero pixels closest to it) gets its own label.
DIST_LABEL_PIXEL = 1
# mask=3
DIST_MASK_3 = 3
# mask=5
DIST_MASK_5 = 5
DIST_MASK_PRECISE = 0
# User defined distance
DIST_USER = -1
# distance = c^2/2(1-exp(-(x/c)^2)), c = 2.9846
DIST_WELSCH = 6
FILLED = -1
FILTER_SCHARR = -1
# If set, the difference between the current pixel and seed pixel is considered. Otherwise,
# the difference between neighbor pixels is considered (that is, the range is floating).
FLOODFILL_FIXED_RANGE = 65536
# If set, the function does not change the image ( newVal is ignored), and only fills the
# mask with the value specified in bits 8-16 of flags as described above. This option only make
# sense in function variants that have the mask parameter.
FLOODFILL_MASK_ONLY = 131072
# normal size serif font
FONT_HERSHEY_COMPLEX = 3
# smaller version of FONT_HERSHEY_COMPLEX
FONT_HERSHEY_COMPLEX_SMALL = 5
# normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)
FONT_HERSHEY_DUPLEX = 2
# small size sans-serif font
FONT_HERSHEY_PLAIN = 1
# more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SCRIPT_COMPLEX = 7
# hand-writing style font
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
# normal size sans-serif font
FONT_HERSHEY_SIMPLEX = 0
# normal size serif font (more complex than FONT_HERSHEY_COMPLEX)
FONT_HERSHEY_TRIPLEX = 4
# flag for italic font
FONT_ITALIC = 16
# an obvious background pixels
GC_BGD = 0
# The value means that the algorithm should just resume.
GC_EVAL = 2
# The value means that the algorithm should just run the grabCut algorithm (a single iteration) with the fixed model
GC_EVAL_FREEZE_MODEL = 3
# an obvious foreground (object) pixel
GC_FGD = 1
# The function initializes the state using the provided mask. Note that GC_INIT_WITH_RECT
# and GC_INIT_WITH_MASK can be combined. Then, all the pixels outside of the ROI are
# automatically initialized with GC_BGD .
GC_INIT_WITH_MASK = 1
# The function initializes the state and the mask using the provided rectangle. After that it
# runs iterCount iterations of the algorithm.
GC_INIT_WITH_RECT = 0
# a possible background pixel
GC_PR_BGD = 2
# a possible foreground pixel
GC_PR_FGD = 3
# Bhattacharyya distance
# (In fact, OpenCV computes Hellinger distance, which is related to Bhattacharyya coefficient.)
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%20%5Csqrt%7B1%20%2D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B%5Cbar%7BH%5F1%7D%20%5Cbar%7BH%5F2%7D%20N%5E2%7D%7D%20%5Csum%5FI%20%5Csqrt%7BH%5F1%28I%29%20%5Ccdot%20H%5F2%28I%29%7D%7D)
HISTCMP_BHATTACHARYYA = 3
# Chi-Square
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%20%5Csum%20%5FI%20%20%5Cfrac%7B%5Cleft%28H%5F1%28I%29%2DH%5F2%28I%29%5Cright%29%5E2%7D%7BH%5F1%28I%29%7D)
HISTCMP_CHISQR = 1
# Alternative Chi-Square
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%202%20%2A%20%5Csum%20%5FI%20%20%5Cfrac%7B%5Cleft%28H%5F1%28I%29%2DH%5F2%28I%29%5Cright%29%5E2%7D%7BH%5F1%28I%29%2BH%5F2%28I%29%7D)
# This alternative formula is regularly used for texture comparison. See e.g. [Puzicha1997](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Puzicha1997)
HISTCMP_CHISQR_ALT = 4
# Correlation
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%20%5Cfrac%7B%5Csum%5FI%20%28H%5F1%28I%29%20%2D%20%5Cbar%7BH%5F1%7D%29%20%28H%5F2%28I%29%20%2D%20%5Cbar%7BH%5F2%7D%29%7D%7B%5Csqrt%7B%5Csum%5FI%28H%5F1%28I%29%20%2D%20%5Cbar%7BH%5F1%7D%29%5E2%20%5Csum%5FI%28H%5F2%28I%29%20%2D%20%5Cbar%7BH%5F2%7D%29%5E2%7D%7D)
# where
# ![block formula](https://latex.codecogs.com/png.latex?%5Cbar%7BH%5Fk%7D%20%3D%20%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum%20%5FJ%20H%5Fk%28J%29)
# and ![inline formula](https://latex.codecogs.com/png.latex?N) is a total number of histogram bins.
HISTCMP_CORREL = 0
# Synonym for HISTCMP_BHATTACHARYYA
HISTCMP_HELLINGER = 3
# Intersection
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%20%5Csum%20%5FI%20%20%5Cmin%20%28H%5F1%28I%29%2C%20H%5F2%28I%29%29)
HISTCMP_INTERSECT = 2
# Kullback-Leibler divergence
# ![block formula](https://latex.codecogs.com/png.latex?d%28H%5F1%2CH%5F2%29%20%3D%20%5Csum%20%5FI%20H%5F1%28I%29%20%5Clog%20%5Cleft%28%5Cfrac%7BH%5F1%28I%29%7D%7BH%5F2%28I%29%7D%5Cright%29)
HISTCMP_KL_DIV = 5
# basically *21HT*, described in [Yuen90](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Yuen90)
HOUGH_GRADIENT = 3
# variation of HOUGH_GRADIENT to get better accuracy
HOUGH_GRADIENT_ALT = 4
# multi-scale variant of the classical Hough transform. The lines are encoded the same way as
# HOUGH_STANDARD.
HOUGH_MULTI_SCALE = 2
# probabilistic Hough transform (more efficient in case if the picture contains a few long
# linear segments). It returns line segments rather than the whole line. Each segment is
# represented by starting and ending points, and the matrix must be (the created sequence will
# be) of the CV_32SC4 type.
HOUGH_PROBABILISTIC = 1
# classical or standard Hough transform. Every line is represented by two floating-point
# numbers ![inline formula](https://latex.codecogs.com/png.latex?%28%5Crho%2C%20%5Ctheta%29) , where ![inline formula](https://latex.codecogs.com/png.latex?%5Crho) is a distance between (0,0) point and the line,
# and ![inline formula](https://latex.codecogs.com/png.latex?%5Ctheta) is the angle between x-axis and the normal to the line. Thus, the matrix must
# be (the created sequence will be) of CV_32FC2 type
HOUGH_STANDARD = 0
# One of the rectangle is fully enclosed in the other
INTERSECT_FULL = 2
# No intersection
INTERSECT_NONE = 0
# There is a partial intersection
INTERSECT_PARTIAL = 1
# resampling using pixel area relation. It may be a preferred method for image decimation, as
# it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST
# method.
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
# 4-connected line
LINE_4 = 4
# 8-connected line
LINE_8 = 8
# antialiased line
LINE_AA = 16
# Advanced refinement. Number of false alarms is calculated, lines are
# refined through increase of precision, decrement in size, etc.
LSD_REFINE_ADV = 2
# No refinement applied
LSD_REFINE_NONE = 0
# Standard refinement is applied. E.g. breaking arches into smaller straighter line approximations.
LSD_REFINE_STD = 1
# A crosshair marker shape
MARKER_CROSS = 0
# A diamond marker shape
MARKER_DIAMOND = 3
# A square marker shape
MARKER_SQUARE = 4
# A star marker shape, combination of cross and tilted cross
MARKER_STAR = 2
# A 45 degree tilted crosshair marker shape
MARKER_TILTED_CROSS = 1
# A downwards pointing triangle marker shape
MARKER_TRIANGLE_DOWN = 6
# An upwards pointing triangle marker shape
MARKER_TRIANGLE_UP = 5
# "black hat"
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%3D%20%5Cmathrm%7Bblackhat%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%3D%20%5Cmathrm%7Bclose%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%2D%20%5Ctexttt%7Bsrc%7D)
MORPH_BLACKHAT = 6
# a closing operation
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%3D%20%5Cmathrm%7Bclose%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%3D%20%5Cmathrm%7Berode%7D%20%28%20%5Cmathrm%7Bdilate%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%29)
MORPH_CLOSE = 3
# a cross-shaped structuring element:
# ![block formula](https://latex.codecogs.com/png.latex?E%5F%7Bij%7D%20%3D%20%5Cbegin%7Bcases%7D%201%20%26%20%5Ctexttt%7Bif%20%7D%20%7Bi%3D%5Ctexttt%7Banchor%2Ey%20%7D%20%7Bor%20%7D%20%7Bj%3D%5Ctexttt%7Banchor%2Ex%7D%7D%7D%20%5C%5C0%20%26%20%5Ctexttt%7Botherwise%7D%20%5Cend%7Bcases%7D)
MORPH_CROSS = 1
# see #dilate
MORPH_DILATE = 1
# an elliptic structuring element, that is, a filled ellipse inscribed
# into the rectangle Rect(0, 0, esize.width, 0.esize.height)
MORPH_ELLIPSE = 2
# see #erode
MORPH_ERODE = 0
# a morphological gradient
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%3D%20%5Cmathrm%7Bmorph%5C%5Fgrad%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%3D%20%5Cmathrm%7Bdilate%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%2D%20%5Cmathrm%7Berode%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29)
MORPH_GRADIENT = 4
# "hit or miss"
# .- Only supported for CV_8UC1 binary images. A tutorial can be found in the documentation
MORPH_HITMISS = 7
# an opening operation
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%3D%20%5Cmathrm%7Bopen%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%3D%20%5Cmathrm%7Bdilate%7D%20%28%20%5Cmathrm%7Berode%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%29)
MORPH_OPEN = 2
# a rectangular structuring element:  ![block formula](https://latex.codecogs.com/png.latex?E%5F%7Bij%7D%3D1)
MORPH_RECT = 0
# "top hat"
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%3D%20%5Cmathrm%7Btophat%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29%3D%20%5Ctexttt%7Bsrc%7D%20%2D%20%5Cmathrm%7Bopen%7D%20%28%20%5Ctexttt%7Bsrc%7D%20%2C%20%5Ctexttt%7Belement%7D%20%29)
MORPH_TOPHAT = 5
# retrieves all of the contours and organizes them into a two-level hierarchy. At the top
# level, there are external boundaries of the components. At the second level, there are
# boundaries of the holes. If there is another contour inside a hole of a connected component, it
# is still put at the top level.
RETR_CCOMP = 2
# retrieves only the extreme outer contours. It sets `hierarchy[i][2]=hierarchy[i][3]=-1` for
# all the contours.
RETR_EXTERNAL = 0
RETR_FLOODFILL = 4
# retrieves all of the contours without establishing any hierarchical relationships.
RETR_LIST = 1
# retrieves all of the contours and reconstructs a full hierarchy of nested contours.
RETR_TREE = 3
Subdiv2D_NEXT_AROUND_DST = 34
Subdiv2D_NEXT_AROUND_LEFT = 19
Subdiv2D_NEXT_AROUND_ORG = 0
Subdiv2D_NEXT_AROUND_RIGHT = 49
Subdiv2D_PREV_AROUND_DST = 51
Subdiv2D_PREV_AROUND_LEFT = 32
Subdiv2D_PREV_AROUND_ORG = 17
Subdiv2D_PREV_AROUND_RIGHT = 2
# Point location error
Subdiv2D_PTLOC_ERROR = -2
# Point inside some facet
Subdiv2D_PTLOC_INSIDE = 0
# Point on some edge
Subdiv2D_PTLOC_ON_EDGE = 2
# Point outside the subdivision bounding rect
Subdiv2D_PTLOC_OUTSIDE_RECT = -1
# Point coincides with one of the subdivision vertices
Subdiv2D_PTLOC_VERTEX = 1
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%28x%2Cy%29%20%3D%20%20%5Cfork%7B%5Ctexttt%7Bmaxval%7D%7D%7Bif%20%5C%28%5Ctexttt%7Bsrc%7D%28x%2Cy%29%20%3E%20%5Ctexttt%7Bthresh%7D%5C%29%7D%7B0%7D%7Botherwise%7D)
THRESH_BINARY = 0
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%28x%2Cy%29%20%3D%20%20%5Cfork%7B0%7D%7Bif%20%5C%28%5Ctexttt%7Bsrc%7D%28x%2Cy%29%20%3E%20%5Ctexttt%7Bthresh%7D%5C%29%7D%7B%5Ctexttt%7Bmaxval%7D%7D%7Botherwise%7D)
THRESH_BINARY_INV = 1
THRESH_MASK = 7
# flag, use Otsu algorithm to choose the optimal threshold value
THRESH_OTSU = 8
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%28x%2Cy%29%20%3D%20%20%5Cfork%7B%5Ctexttt%7Bsrc%7D%28x%2Cy%29%7D%7Bif%20%5C%28%5Ctexttt%7Bsrc%7D%28x%2Cy%29%20%3E%20%5Ctexttt%7Bthresh%7D%5C%29%7D%7B0%7D%7Botherwise%7D)
THRESH_TOZERO = 3
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%28x%2Cy%29%20%3D%20%20%5Cfork%7B0%7D%7Bif%20%5C%28%5Ctexttt%7Bsrc%7D%28x%2Cy%29%20%3E%20%5Ctexttt%7Bthresh%7D%5C%29%7D%7B%5Ctexttt%7Bsrc%7D%28x%2Cy%29%7D%7Botherwise%7D)
THRESH_TOZERO_INV = 4
# flag, use Triangle algorithm to choose the optimal threshold value
THRESH_TRIANGLE = 16
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bdst%7D%20%28x%2Cy%29%20%3D%20%20%5Cfork%7B%5Ctexttt%7Bthreshold%7D%7D%7Bif%20%5C%28%5Ctexttt%7Bsrc%7D%28x%2Cy%29%20%3E%20%5Ctexttt%7Bthresh%7D%5C%29%7D%7B%5Ctexttt%7Bsrc%7D%28x%2Cy%29%7D%7Botherwise%7D)
THRESH_TRUNC = 2
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%28T%27%28x%27%2Cy%27%29%20%5Ccdot%20I%27%28x%2Bx%27%2Cy%2By%27%29%29)
# where
# ![block formula](https://latex.codecogs.com/png.latex?%5Cbegin%7Barray%7D%7Bl%7D%20T%27%28x%27%2Cy%27%29%3DT%28x%27%2Cy%27%29%20%2D%201%2F%28w%20%5Ccdot%20h%29%20%5Ccdot%20%5Csum%20%5F%7B%0A%20%20%20x%27%27%2Cy%27%27%7D%20T%28x%27%27%2Cy%27%27%29%20%5C%5C%20I%27%28x%2Bx%27%2Cy%2By%27%29%3DI%28x%2Bx%27%2Cy%2By%27%29%20%2D%201%2F%28w%20%5Ccdot%20h%29%0A%20%20%20%5Ccdot%20%5Csum%20%5F%7Bx%27%27%2Cy%27%27%7D%20I%28x%2Bx%27%27%2Cy%2By%27%27%29%20%5Cend%7Barray%7D)
# with mask:
# ![block formula](https://latex.codecogs.com/png.latex?%5Cbegin%7Barray%7D%7Bl%7D%20T%27%28x%27%2Cy%27%29%3DM%28x%27%2Cy%27%29%20%5Ccdot%20%5Cleft%28%20T%28x%27%2Cy%27%29%20%2D%0A%20%20%20%5Cfrac%7B1%7D%7B%5Csum%20%5F%7Bx%27%27%2Cy%27%27%7D%20M%28x%27%27%2Cy%27%27%29%7D%20%5Ccdot%20%5Csum%20%5F%7Bx%27%27%2Cy%27%27%7D%0A%20%20%20%28T%28x%27%27%2Cy%27%27%29%20%5Ccdot%20M%28x%27%27%2Cy%27%27%29%29%20%5Cright%29%20%5C%5C%20I%27%28x%2Bx%27%2Cy%2By%27%29%3DM%28x%27%2Cy%27%29%0A%20%20%20%5Ccdot%20%5Cleft%28%20I%28x%2Bx%27%2Cy%2By%27%29%20%2D%20%5Cfrac%7B1%7D%7B%5Csum%20%5F%7Bx%27%27%2Cy%27%27%7D%20M%28x%27%27%2Cy%27%27%29%7D%0A%20%20%20%5Ccdot%20%5Csum%20%5F%7Bx%27%27%2Cy%27%27%7D%20%28I%28x%2Bx%27%27%2Cy%2By%27%27%29%20%5Ccdot%20M%28x%27%27%2Cy%27%27%29%29%20%5Cright%29%0A%20%20%20%5Cend%7Barray%7D%20)
TM_CCOEFF = 4
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Cfrac%7B%20%5Csum%5F%7Bx%27%2Cy%27%7D%20%28T%27%28x%27%2Cy%27%29%20%5Ccdot%20I%27%28x%2Bx%27%2Cy%2By%27%29%29%20%7D%7B%0A%5Csqrt%7B%5Csum%5F%7Bx%27%2Cy%27%7DT%27%28x%27%2Cy%27%29%5E2%20%5Ccdot%20%5Csum%5F%7Bx%27%2Cy%27%7D%20I%27%28x%2Bx%27%2Cy%2By%27%29%5E2%7D%0A%7D)
TM_CCOEFF_NORMED = 5
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%20%5Ccdot%20I%28x%2Bx%27%2Cy%2By%27%29%29)
# with mask:
# ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%20%5Ccdot%20I%28x%2Bx%27%2Cy%2By%27%29%20%5Ccdot%20M%28x%27%2Cy%27%29%0A%20%20%20%5E2%29)
TM_CCORR = 2
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Cfrac%7B%5Csum%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%20%5Ccdot%20I%28x%2Bx%27%2Cy%2By%27%29%29%7D%7B%5Csqrt%7B%0A%20%20%20%5Csum%5F%7Bx%27%2Cy%27%7DT%28x%27%2Cy%27%29%5E2%20%5Ccdot%20%5Csum%5F%7Bx%27%2Cy%27%7D%20I%28x%2Bx%27%2Cy%2By%27%29%5E2%7D%7D)
# with mask:
# ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Cfrac%7B%5Csum%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%20%5Ccdot%20I%28x%2Bx%27%2Cy%2By%27%29%20%5Ccdot%0A%20%20%20M%28x%27%2Cy%27%29%5E2%29%7D%7B%5Csqrt%7B%5Csum%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20T%28x%27%2Cy%27%29%20%5Ccdot%20M%28x%27%2Cy%27%29%0A%20%20%20%5Cright%29%5E2%20%5Ccdot%20%5Csum%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20I%28x%2Bx%27%2Cy%2By%27%29%20%5Ccdot%20M%28x%27%2Cy%27%29%0A%20%20%20%5Cright%29%5E2%7D%7D)
TM_CCORR_NORMED = 3
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%2DI%28x%2Bx%27%2Cy%2By%27%29%29%5E2)
# with mask:
# ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20%28T%28x%27%2Cy%27%29%2DI%28x%2Bx%27%2Cy%2By%27%29%29%20%5Ccdot%0A%20%20%20M%28x%27%2Cy%27%29%20%5Cright%29%5E2)
TM_SQDIFF = 0
# !< ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Cfrac%7B%5Csum%5F%7Bx%27%2Cy%27%7D%20%28T%28x%27%2Cy%27%29%2DI%28x%2Bx%27%2Cy%2By%27%29%29%5E2%7D%7B%5Csqrt%7B%5Csum%5F%7B%0A%20%20%20x%27%2Cy%27%7DT%28x%27%2Cy%27%29%5E2%20%5Ccdot%20%5Csum%5F%7Bx%27%2Cy%27%7D%20I%28x%2Bx%27%2Cy%2By%27%29%5E2%7D%7D)
# with mask:
# ![block formula](https://latex.codecogs.com/png.latex?R%28x%2Cy%29%3D%20%5Cfrac%7B%5Csum%20%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20%28T%28x%27%2Cy%27%29%2DI%28x%2Bx%27%2Cy%2By%27%29%29%20%5Ccdot%0A%20%20%20M%28x%27%2Cy%27%29%20%5Cright%29%5E2%7D%7B%5Csqrt%7B%5Csum%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20T%28x%27%2Cy%27%29%20%5Ccdot%0A%20%20%20M%28x%27%2Cy%27%29%20%5Cright%29%5E2%20%5Ccdot%20%5Csum%5F%7Bx%27%2Cy%27%7D%20%5Cleft%28%20I%28x%2Bx%27%2Cy%2By%27%29%20%5Ccdot%0A%20%20%20M%28x%27%2Cy%27%29%20%5Cright%29%5E2%7D%7D)
TM_SQDIFF_NORMED = 1
# flag, fills all of the destination image pixels. If some of them correspond to outliers in the
# source image, they are set to zero
WARP_FILL_OUTLIERS = 8
# flag, inverse transformation
#
# For example, #linearPolar or #logPolar transforms:
# - flag is __not__ set: ![inline formula](https://latex.codecogs.com/png.latex?dst%28%20%5Crho%20%2C%20%5Cphi%20%29%20%3D%20src%28x%2Cy%29)
# - flag is set: ![inline formula](https://latex.codecogs.com/png.latex?dst%28x%2Cy%29%20%3D%20src%28%20%5Crho%20%2C%20%5Cphi%20%29)
WARP_INVERSE_MAP = 16
# Remaps an image to/from polar space.
WARP_POLAR_LINEAR = 0
# Remaps an image to/from semilog-polar space.
WARP_POLAR_LOG = 256
