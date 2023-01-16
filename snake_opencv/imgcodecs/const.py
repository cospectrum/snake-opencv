# If set, the image is read in any possible color format.
IMREAD_ANYCOLOR = 4
# If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.
IMREAD_ANYDEPTH = 2
# If set, always convert image to the 3 channel BGR color image.
IMREAD_COLOR = 1
# If set, always convert image to the single channel grayscale image (codec internal conversion).
IMREAD_GRAYSCALE = 0
# If set, do not rotate the image according to EXIF's orientation flag.
IMREAD_IGNORE_ORIENTATION = 128
# If set, use the gdal driver for loading the image.
IMREAD_LOAD_GDAL = 8
# If set, always convert image to the 3 channel BGR color image and the image size reduced 1/2.
IMREAD_REDUCED_COLOR_2 = 17
# If set, always convert image to the 3 channel BGR color image and the image size reduced 1/4.
IMREAD_REDUCED_COLOR_4 = 33
# If set, always convert image to the 3 channel BGR color image and the image size reduced 1/8.
IMREAD_REDUCED_COLOR_8 = 65
# If set, always convert image to the single channel grayscale image and the image size reduced 1/2.
IMREAD_REDUCED_GRAYSCALE_2 = 16
# If set, always convert image to the single channel grayscale image and the image size reduced 1/4.
IMREAD_REDUCED_GRAYSCALE_4 = 32
# If set, always convert image to the single channel grayscale image and the image size reduced 1/8.
IMREAD_REDUCED_GRAYSCALE_8 = 64
# If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.
IMREAD_UNCHANGED = -1
