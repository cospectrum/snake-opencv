# Use Navier-Stokes based method
INPAINT_NS = 0
# Use the algorithm proposed by Alexandru Telea [Telea04](https://docs.opencv.org/4.7.0/d0/de3/citelist.html#CITEREF_Telea04)
INPAINT_TELEA = 1
LDR_SIZE = 256
# The classic method, color-based selection and alpha masking might be time consuming and often leaves an undesirable
# halo. Seamless cloning, even averaged with the original image, is not effective.
# Mixed seamless cloning based on a loose selection proves effective.
MIXED_CLONE = 2
# Monochrome transfer allows the user to easily replace certain features of one object by alternative features.
MONOCHROME_TRANSFER = 3
# The power of the method is fully expressed when inserting objects with complex outlines into a new background
NORMAL_CLONE = 1
# Normalized Convolution Filtering
NORMCONV_FILTER = 2
# Recursive Filtering
RECURS_FILTER = 1
