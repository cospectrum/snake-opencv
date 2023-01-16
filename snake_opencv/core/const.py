ACCESS_FAST = 67108864
ACCESS_MASK = 50331648
ACCESS_READ = 16777216
ACCESS_RW = 50331648
ACCESS_WRITE = 33554432
# `iiiiii|abcdefgh|iiiiiii`  with some specified `i`
BORDER_CONSTANT = 0
# same as BORDER_REFLECT_101
BORDER_DEFAULT = 4
# do not look outside of ROI
BORDER_ISOLATED = 16
# `fedcba|abcdefgh|hgfedcb`
BORDER_REFLECT = 2
# same as BORDER_REFLECT_101
BORDER_REFLECT101 = 4
# `gfedcb|abcdefgh|gfedcba`
BORDER_REFLECT_101 = 4
# `aaaaaa|abcdefgh|hhhhhhh`
BORDER_REPLICATE = 1
# `uvwxyz|abcdefgh|ijklmno`
BORDER_TRANSPARENT = 5
# `cdefgh|abcdefgh|abcdefg`
BORDER_WRAP = 3
# incorrect input align
BadAlign = -21
BadAlphaChannel = -18
# input COI is not supported
BadCOI = -24
BadCallBack = -22
BadDataPtr = -12
# input image depth is not supported by the function
BadDepth = -17
# image size is invalid
BadImageSize = -10
BadModelOrChSeq = -14
BadNumChannel1U = -16
# bad number of channels, for example, some functions accept only single channel matrices.
BadNumChannels = -15
# offset is invalid
BadOffset = -11
# number of dimensions is out of range
BadOrder = -19
# incorrect input origin
BadOrigin = -20
# incorrect input roi
BadROISize = -25
# image step is wrong, this may happen for a non-continuous matrix.
BadStep = -13
BadTileSize = -23
# src1 is equal to src2.
CMP_EQ = 0
# src1 is greater than or equal to src2.
CMP_GE = 2
# src1 is greater than src2.
CMP_GT = 1
# src1 is less than or equal to src2.
CMP_LE = 4
# src1 is less than src2.
CMP_LT = 3
# src1 is unequal to src2.
CMP_NE = 5
# If the flag is
# specified, all the input vectors are stored as columns of the samples matrix. mean should be a
# single-column vector in this case.
COVAR_COLS = 16
# The output covariance matrix is calculated as:
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bscale%7D%20%20%20%5Ccdot%20%20%5B%20%20%5Ctexttt%7Bvects%7D%20%20%5B0%5D%2D%20%20%5Ctexttt%7Bmean%7D%20%20%2C%20%5Ctexttt%7Bvects%7D%20%20%5B1%5D%2D%20%20%5Ctexttt%7Bmean%7D%20%20%2C%2E%2E%2E%5D%20%20%5Ccdot%20%20%5B%20%5Ctexttt%7Bvects%7D%20%20%5B0%5D%2D%20%5Ctexttt%7Bmean%7D%20%20%2C%20%5Ctexttt%7Bvects%7D%20%20%5B1%5D%2D%20%5Ctexttt%7Bmean%7D%20%20%2C%2E%2E%2E%5D%5ET%2C)
# covar will be a square matrix of the same size as the total number of elements in each input
# vector. One and only one of #COVAR_SCRAMBLED and #COVAR_NORMAL must be specified.
COVAR_NORMAL = 1
# If the flag is
# specified, all the input vectors are stored as rows of the samples matrix. mean should be a
# single-row vector in this case.
COVAR_ROWS = 8
# If the flag is specified, the covariance matrix is scaled. In the
# "normal" mode, scale is 1./nsamples . In the "scrambled" mode, scale is the reciprocal of the
# total number of elements in each input vector. By default (if the flag is not specified), the
# covariance matrix is not scaled ( scale=1 ).
COVAR_SCALE = 4
# The output covariance matrix is calculated as:
# ![block formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bscale%7D%20%20%20%5Ccdot%20%20%5B%20%20%5Ctexttt%7Bvects%7D%20%20%5B0%5D%2D%20%20%5Ctexttt%7Bmean%7D%20%20%2C%20%5Ctexttt%7Bvects%7D%20%20%5B1%5D%2D%20%20%5Ctexttt%7Bmean%7D%20%20%2C%2E%2E%2E%5D%5ET%20%20%5Ccdot%20%20%5B%20%5Ctexttt%7Bvects%7D%20%20%5B0%5D%2D%20%5Ctexttt%7Bmean%7D%20%20%2C%20%5Ctexttt%7Bvects%7D%20%20%5B1%5D%2D%20%5Ctexttt%7Bmean%7D%20%20%2C%2E%2E%2E%5D%2C)
# The covariance matrix will be nsamples x nsamples. Such an unusual covariance matrix is used
# for fast PCA of a set of very large vectors (see, for example, the EigenFaces technique for
# face recognition). Eigenvalues of this "scrambled" matrix match the eigenvalues of the true
# covariance matrix. The "true" eigenvectors can be easily calculated from the eigenvectors of
# the "scrambled" covariance matrix.
COVAR_SCRAMBLED = 0
# If the flag is specified, the function does not calculate mean from
# the input vectors but, instead, uses the passed mean vector. This is useful if mean has been
# pre-calculated or known in advance, or if the covariance matrix is calculated by parts. In
# this case, mean is not a mean vector of the input sub-set of vectors but rather the mean
# vector of the whole set.
COVAR_USE_AVG = 2
CPU_AVX = 10
CPU_AVX2 = 11
# Cascade Lake with AVX-512F/CD/BW/DQ/VL/VNNI
CPU_AVX512_CLX = 261
# Cannon Lake with AVX-512F/CD/BW/DQ/VL/IFMA/VBMI
CPU_AVX512_CNL = 260
# Common instructions AVX-512F/CD for all CPUs that support AVX-512
CPU_AVX512_COMMON = 257
# Ice Lake with AVX-512F/CD/BW/DQ/VL/IFMA/VBMI/VNNI/VBMI2/BITALG/VPOPCNTDQ
CPU_AVX512_ICL = 262
# Knights Landing with AVX-512F/CD/ER/PF
CPU_AVX512_KNL = 258
# Knights Mill with AVX-512F/CD/ER/PF/4FMAPS/4VNNIW/VPOPCNTDQ
CPU_AVX512_KNM = 259
# Skylake-X with AVX-512F/CD/BW/DQ/VL
CPU_AVX512_SKX = 256
CPU_AVX_5124FMAPS = 27
CPU_AVX_5124VNNIW = 26
CPU_AVX_512BITALG = 24
CPU_AVX_512BW = 14
CPU_AVX_512CD = 15
CPU_AVX_512DQ = 16
CPU_AVX_512ER = 17
CPU_AVX_512F = 13
CPU_AVX_512IFMA = 18
CPU_AVX_512IFMA512 = 18
CPU_AVX_512PF = 19
CPU_AVX_512VBMI = 20
CPU_AVX_512VBMI2 = 22
CPU_AVX_512VL = 21
CPU_AVX_512VNNI = 23
CPU_AVX_512VPOPCNTDQ = 25
CPU_FMA3 = 12
CPU_FP16 = 9
CPU_LASX = 230
CPU_MAX_FEATURE = 512
CPU_MMX = 1
CPU_MSA = 150
CPU_NEON = 100
CPU_NEON_DOTPROD = 101
CPU_POPCNT = 8
CPU_RISCVV = 170
CPU_RVV = 210
CPU_SSE = 2
CPU_SSE2 = 3
CPU_SSE3 = 4
CPU_SSE4_1 = 6
CPU_SSE4_2 = 7
CPU_SSSE3 = 5
CPU_VSX = 200
CPU_VSX3 = 201
CV_16S = 3
CV_16SC1 = 3
CV_16SC2 = 11
CV_16SC3 = 19
CV_16SC4 = 27
CV_16U = 2
CV_16UC1 = 2
CV_16UC2 = 10
CV_16UC3 = 18
CV_16UC4 = 26
CV_2PI = 6.283185307179586476925286766559
CV_32F = 5
CV_32FC1 = 5
CV_32FC2 = 13
CV_32FC3 = 21
CV_32FC4 = 29
CV_32S = 4
CV_32SC1 = 4
CV_32SC2 = 12
CV_32SC3 = 20
CV_32SC4 = 28
CV_64F = 6
CV_64FC1 = 6
CV_64FC2 = 14
CV_64FC3 = 22
CV_64FC4 = 30
CV_8S = 1
CV_8SC1 = 1
CV_8SC2 = 9
CV_8SC3 = 17
CV_8SC4 = 25
CV_8U = 0
CV_8UC1 = 0
CV_8UC2 = 8
CV_8UC3 = 16
CV_8UC4 = 24
CV_AVX = 0
CV_AVX2 = 0
CV_AVX512_CLX = 0
CV_AVX512_CNL = 0
CV_AVX512_COMMON = 0
CV_AVX512_ICL = 0
CV_AVX512_KNL = 0
CV_AVX512_KNM = 0
CV_AVX512_SKX = 0
CV_AVX_5124FMAPS = 0
CV_AVX_5124VNNIW = 0
CV_AVX_512BITALG = 0
CV_AVX_512BW = 0
CV_AVX_512CD = 0
CV_AVX_512DQ = 0
CV_AVX_512ER = 0
CV_AVX_512F = 0
CV_AVX_512IFMA = 0
CV_AVX_512IFMA512 = CV_AVX_512IFMA
CV_AVX_512PF = 0
CV_AVX_512VBMI = 0
CV_AVX_512VBMI2 = 0
CV_AVX_512VL = 0
CV_AVX_512VNNI = 0
CV_AVX_512VPOPCNTDQ = 0
CV_CN_MAX = 512
CV_CN_SHIFT = 3
CV_CPU_AVX = 10
CV_CPU_AVX2 = 11
CV_CPU_AVX512_CLX = 261
CV_CPU_AVX512_CNL = 260
CV_CPU_AVX512_COMMON = 257
CV_CPU_AVX512_ICL = 262
CV_CPU_AVX512_KNL = 258
CV_CPU_AVX512_KNM = 259
CV_CPU_AVX512_SKX = 256
CV_CPU_AVX_5124FMAPS = 27
CV_CPU_AVX_5124VNNIW = 26
CV_CPU_AVX_512BITALG = 24
CV_CPU_AVX_512BW = 14
CV_CPU_AVX_512CD = 15
CV_CPU_AVX_512DQ = 16
CV_CPU_AVX_512ER = 17
CV_CPU_AVX_512F = 13
CV_CPU_AVX_512IFMA = 18
CV_CPU_AVX_512IFMA512 = 18
CV_CPU_AVX_512PF = 19
CV_CPU_AVX_512VBMI = 20
CV_CPU_AVX_512VBMI2 = 22
CV_CPU_AVX_512VL = 21
CV_CPU_AVX_512VNNI = 23
CV_CPU_AVX_512VPOPCNTDQ = 25
CV_CPU_FMA3 = 12
CV_CPU_FP16 = 9
CV_CPU_LASX = 230
CV_CPU_MMX = 1
CV_CPU_MSA = 150
CV_CPU_NEON = 100
CV_CPU_NEON_DOTPROD = 101
CV_CPU_NONE = 0
CV_CPU_POPCNT = 8
CV_CPU_RISCVV = 170
CV_CPU_RVV = 210
CV_CPU_SSE = 2
CV_CPU_SSE2 = 3
CV_CPU_SSE3 = 4
CV_CPU_SSE4_1 = 6
CV_CPU_SSE4_2 = 7
CV_CPU_SSSE3 = 5
CV_CPU_VSX = 200
CV_CPU_VSX3 = 201
CV_CXX11 = 1
CV_CXX_MOVE_SEMANTICS = 1
CV_CXX_STD_ARRAY = 1
CV_DEPTH_MAX = (1<<CV_CN_SHIFT)
CV_ENABLE_UNROLLED = 1
CV_FMA3 = 0
CV_FP16 = 0
CV_FP16_TYPE = 0
CV_HAL_BORDER_CONSTANT = 0
CV_HAL_BORDER_ISOLATED = 16
CV_HAL_BORDER_REFLECT = 2
CV_HAL_BORDER_REFLECT_101 = 4
CV_HAL_BORDER_REPLICATE = 1
CV_HAL_BORDER_TRANSPARENT = 5
CV_HAL_BORDER_WRAP = 3
CV_HAL_CMP_EQ = 0
CV_HAL_CMP_GE = 2
CV_HAL_CMP_GT = 1
CV_HAL_CMP_LE = 4
CV_HAL_CMP_LT = 3
CV_HAL_CMP_NE = 5
CV_HAL_DFT_COMPLEX_OUTPUT = 16
CV_HAL_DFT_INVERSE = 1
CV_HAL_DFT_IS_CONTINUOUS = 512
CV_HAL_DFT_IS_INPLACE = 1024
CV_HAL_DFT_REAL_OUTPUT = 32
CV_HAL_DFT_ROWS = 4
CV_HAL_DFT_SCALE = 2
CV_HAL_DFT_STAGE_COLS = 128
CV_HAL_DFT_TWO_STAGE = 64
CV_HAL_ERROR_NOT_IMPLEMENTED = 1
CV_HAL_ERROR_OK = 0
CV_HAL_ERROR_UNKNOWN = -1
CV_HAL_GEMM_1_T = 1
CV_HAL_GEMM_2_T = 2
CV_HAL_GEMM_3_T = 4
CV_HAL_SVD_FULL_UV = 8
CV_HAL_SVD_MODIFY_A = 4
CV_HAL_SVD_NO_UV = 1
CV_HAL_SVD_SHORT_UV = 2
CV_HARDWARE_MAX_FEATURE = 512
CV_IMPL_IPP = 0x04
CV_IMPL_MT = 0x10
CV_IMPL_OCL = 0x02
CV_IMPL_PLAIN = 0x01
CV_LASX = 0
CV_LOG2 = 0.69314718055994530941723212145818
CV_LOG_LEVEL_DEBUG = 5
CV_LOG_LEVEL_ERROR = 2
CV_LOG_LEVEL_FATAL = 1
CV_LOG_LEVEL_INFO = 4
CV_LOG_LEVEL_SILENT = 0
CV_LOG_LEVEL_VERBOSE = 6
CV_LOG_LEVEL_WARN = 3
CV_LOG_STRIP_LEVEL = CV_LOG_LEVEL_VERBOSE
CV_MAT_CN_MASK = ((CV_CN_MAX-1)<<CV_CN_SHIFT)
CV_MAT_CONT_FLAG_SHIFT = 14
CV_MAT_DEPTH_MASK = (CV_DEPTH_MAX-1)
CV_MAT_TYPE_MASK = (CV_DEPTH_MAX*CV_CN_MAX-1)
CV_MMX = 1
CV_MSA = 0
CV_NEON = 0
CV_PI = 3.1415926535897932384626433832795
CV_POPCNT = 0
CV_RVV = 0
CV_RVV071 = 0
CV_SSE = 1
CV_SSE2 = 1
CV_SSE3 = 0
CV_SSE4_1 = 0
CV_SSE4_2 = 0
CV_SSSE3 = 0
CV_STRONG_ALIGNMENT = 0
CV_SUBMAT_FLAG_SHIFT = 15
CV__EXCEPTION_PTR = 1
# performs an inverse 1D or 2D transform instead of the default forward transform.
DCT_INVERSE = 1
# performs a forward or inverse transform of every individual row of the input
# matrix. This flag enables you to transform multiple vectors simultaneously and can be used to
# decrease the overhead (which is sometimes several times larger than the processing itself) to
# perform 3D and higher-dimensional transforms and so forth.
DCT_ROWS = 4
# Cholesky ![inline formula](https://latex.codecogs.com/png.latex?LL%5ET) factorization the matrix src1 must be symmetrical and positively
# defined
DECOMP_CHOLESKY = 3
# eigenvalue decomposition the matrix src1 must be symmetrical
DECOMP_EIG = 2
# Gaussian elimination with the optimal pivot element chosen.
DECOMP_LU = 0
# while all the previous flags are mutually exclusive, this flag can be used together with
# any of the previous it means that the normal equations
# ![inline formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bsrc1%7D%5ET%5Ccdot%5Ctexttt%7Bsrc1%7D%5Ccdot%5Ctexttt%7Bdst%7D%3D%5Ctexttt%7Bsrc1%7D%5ET%5Ctexttt%7Bsrc2%7D) are
# solved instead of the original system
# ![inline formula](https://latex.codecogs.com/png.latex?%5Ctexttt%7Bsrc1%7D%5Ccdot%5Ctexttt%7Bdst%7D%3D%5Ctexttt%7Bsrc2%7D)
DECOMP_NORMAL = 16
# QR factorization the system can be over-defined and/or the matrix src1 can be singular
DECOMP_QR = 4
# singular value decomposition (SVD) method the system can be over-defined and/or the matrix
# src1 can be singular
DECOMP_SVD = 1
# specifies that input is complex input. If this flag is set, the input must have 2 channels.
# On the other hand, for backwards compatibility reason, if input has 2 channels, input is
# already considered complex.
DFT_COMPLEX_INPUT = 64
# performs a forward transformation of 1D or 2D real array the result,
# though being a complex array, has complex-conjugate symmetry (*CCS*, see the function
# description below for details), and such an array can be packed into a real array of the same
# size as input, which is the fastest option and which is what the function does by default
# however, you may wish to get a full complex array (for simpler spectrum analysis, and so on) -
# pass the flag to enable the function to produce a full-size complex output array.
DFT_COMPLEX_OUTPUT = 16
# performs an inverse 1D or 2D transform instead of the default forward
# transform.
DFT_INVERSE = 1
# performs an inverse transformation of a 1D or 2D complex array the
# result is normally a complex array of the same size, however, if the input array has
# conjugate-complex symmetry (for example, it is a result of forward transformation with
# DFT_COMPLEX_OUTPUT flag), the output is a real array while the function itself does not
# check whether the input is symmetrical or not, you can pass the flag and then the function
# will assume the symmetry and produce the real output array (note that when the input is packed
# into a real array and inverse transformation is executed, the function treats the input as a
# packed complex-conjugate symmetrical array, and the output will also be a real array).
DFT_REAL_OUTPUT = 32
# performs a forward or inverse transform of every individual row of the input
# matrix this flag enables you to transform multiple vectors simultaneously and can be used to
# decrease the overhead (which is sometimes several times larger than the processing itself) to
# perform 3D and higher-dimensional transformations and so forth.
DFT_ROWS = 4
# scales the result: divide it by the number of array elements. Normally, it is
# combined with DFT_INVERSE.
DFT_SCALE = 2
DYNAMIC_PARALLELISM = 35
Detail_CV__LAST_TEST_OP = 7
Detail_TEST_CUSTOM = 0
Detail_TEST_EQ = 1
Detail_TEST_GE = 5
Detail_TEST_GT = 6
Detail_TEST_LE = 3
Detail_TEST_LT = 4
Detail_TEST_NE = 2
Device_EXEC_KERNEL = 1
Device_EXEC_NATIVE_KERNEL = 2
Device_FP_CORRECTLY_ROUNDED_DIVIDE_SQRT = 128
Device_FP_DENORM = 1
Device_FP_FMA = 32
Device_FP_INF_NAN = 2
Device_FP_ROUND_TO_INF = 16
Device_FP_ROUND_TO_NEAREST = 4
Device_FP_ROUND_TO_ZERO = 8
Device_FP_SOFT_FLOAT = 64
Device_LOCAL_IS_GLOBAL = 2
Device_LOCAL_IS_LOCAL = 1
Device_NO_CACHE = 0
Device_NO_LOCAL_MEM = 0
Device_READ_ONLY_CACHE = 1
Device_READ_WRITE_CACHE = 2
Device_TYPE_ACCELERATOR = 8
Device_TYPE_ALL = -1
Device_TYPE_CPU = 2
Device_TYPE_DEFAULT = 1
Device_TYPE_DGPU = 65540
Device_TYPE_GPU = 4
Device_TYPE_IGPU = 131076
Device_UNKNOWN_VENDOR = 0
Device_VENDOR_AMD = 1
Device_VENDOR_INTEL = 2
Device_VENDOR_NVIDIA = 3
ENUM_LOG_LEVEL_FORCE_INT = 2147483647
FEATURE_SET_COMPUTE_10 = 10
FEATURE_SET_COMPUTE_11 = 11
FEATURE_SET_COMPUTE_12 = 12
FEATURE_SET_COMPUTE_13 = 13
FEATURE_SET_COMPUTE_20 = 20
FEATURE_SET_COMPUTE_21 = 21
FEATURE_SET_COMPUTE_30 = 30
FEATURE_SET_COMPUTE_32 = 32
FEATURE_SET_COMPUTE_35 = 35
FEATURE_SET_COMPUTE_50 = 50
FLAGS_EXPAND_SAME_NAMES = 2
FLAGS_MAPPING = 1
FLAGS_NONE = 0
# empty structure (sequence or mapping)
FileNode_EMPTY = 16
# synonym or REAL
FileNode_FLOAT = 2
# compact representation of a sequence or mapping. Used only by YAML writer
FileNode_FLOW = 8
# an integer
FileNode_INT = 1
# mapping
FileNode_MAP = 5
# the node has a name (i.e. it is element of a mapping).
FileNode_NAMED = 32
# empty node
FileNode_NONE = 0
# floating-point number
FileNode_REAL = 2
# sequence
FileNode_SEQ = 4
# text string in UTF-8 encoding
FileNode_STR = 3
# synonym for STR
FileNode_STRING = 3
FileNode_TYPE_MASK = 7
# if set, means that all the collection elements are numbers of the same type (real's or int's).
# UNIFORM is used only when reading FileStorage FLOW is used only when writing. So they share the same bit
FileNode_UNIFORM = 8
# transposes src1
GEMM_1_T = 1
# transposes src2
GEMM_2_T = 2
# transposes src3
GEMM_3_T = 4
GLOBAL_ATOMICS = 11
# GPU API call error
GpuApiCallError = -217
# no CUDA support
GpuNotSupported = -216
# image header is NULL
HeaderIsNull = -9
IMPL_IPP = 1
IMPL_OPENCL = 2
IMPL_PLAIN = 0
# Use kmeans++ center initialization by Arthur and Vassilvitskii [Arthur2007].
KMEANS_PP_CENTERS = 2
# Select random initial centers in each attempt.
KMEANS_RANDOM_CENTERS = 0
# During the first (and possibly the only) attempt, use the
# user-supplied labels instead of computing them from the initial centers. For the second and
# further attempts, use the random or semi-random centers. Use one of KMEANS_\*_CENTERS flag
# to specify the exact method.
KMEANS_USE_INITIAL_LABELS = 1
KernelArg_CONSTANT = 8
KernelArg_LOCAL = 1
KernelArg_NO_SIZE = 256
KernelArg_PTR_ONLY = 16
KernelArg_READ_ONLY = 2
KernelArg_READ_WRITE = 6
KernelArg_WRITE_ONLY = 4
LINES = 1
LINE_LOOP = 2
LINE_STRIP = 3
# Debug message. Disabled in the "Release" build.
LOG_LEVEL_DEBUG = 5
# Error message
LOG_LEVEL_ERROR = 2
# Fatal (critical) error (unrecoverable internal error)
LOG_LEVEL_FATAL = 1
# Info message
LOG_LEVEL_INFO = 4
# for using in setLogVevel() call
LOG_LEVEL_SILENT = 0
# Verbose (trace) messages. Requires verbosity level. Disabled in the "Release" build.
LOG_LEVEL_VERBOSE = 6
# Warning message
LOG_LEVEL_WARNING = 3
MaskIsTiled = -26
Mat_AUTO_STEP = 0
Mat_CONTINUOUS_FLAG = 16384
Mat_DEPTH_MASK = 7
Mat_MAGIC_MASK = -65536
Mat_MAGIC_VAL = 1124007936
Mat_SUBMATRIX_FLAG = 32768
Mat_TYPE_MASK = 4095
NATIVE_DOUBLE = 13
# In the case of one input array, calculates the Hamming distance of the array from zero,
# In the case of two input arrays, calculates the Hamming distance between the arrays.
NORM_HAMMING = 6
# Similar to NORM_HAMMING, but in the calculation, each two bits of the input sequence will
# be added and treated as a single bit to be used in the same calculation as NORM_HAMMING.
NORM_HAMMING2 = 7
# ![block formula](https://latex.codecogs.com/png.latex?%0Anorm%20%3D%20%20%5Cforkthree%0A%7B%5C%7C%5Ctexttt%7Bsrc1%7D%5C%7C%5F%7BL%5F%7B%5Cinfty%7D%7D%20%3D%20%20%5Cmax%20%5FI%20%7C%20%5Ctexttt%7Bsrc1%7D%20%28I%29%7C%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FINF%7D%5C%29%20%7D%0A%7B%5C%7C%5Ctexttt%7Bsrc1%7D%2D%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F%7B%5Cinfty%7D%7D%20%3D%20%20%5Cmax%20%5FI%20%7C%20%5Ctexttt%7Bsrc1%7D%20%28I%29%20%2D%20%20%5Ctexttt%7Bsrc2%7D%20%28I%29%7C%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FINF%7D%5C%29%20%7D%0A%7B%5Cfrac%7B%5C%7C%5Ctexttt%7Bsrc1%7D%2D%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F%7B%5Cinfty%7D%7D%20%20%20%20%7D%7B%5C%7C%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F%7B%5Cinfty%7D%7D%20%7D%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FRELATIVE%20%7C%20NORM%5FINF%7D%5C%29%20%7D%0A)
NORM_INF = 1
# ![block formula](https://latex.codecogs.com/png.latex?%0Anorm%20%3D%20%20%5Cforkthree%0A%7B%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%5C%7C%20%5F%7BL%5F1%7D%20%3D%20%20%5Csum%20%5FI%20%7C%20%5Ctexttt%7Bsrc1%7D%20%28I%29%7C%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL1%7D%5C%29%7D%0A%7B%20%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%2D%20%5Ctexttt%7Bsrc2%7D%20%5C%7C%20%5F%7BL%5F1%7D%20%3D%20%20%5Csum%20%5FI%20%7C%20%5Ctexttt%7Bsrc1%7D%20%28I%29%20%2D%20%20%5Ctexttt%7Bsrc2%7D%20%28I%29%7C%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL1%7D%5C%29%20%7D%0A%7B%20%5Cfrac%7B%5C%7C%5Ctexttt%7Bsrc1%7D%2D%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F1%7D%20%7D%7B%5C%7C%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F1%7D%7D%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FRELATIVE%20%7C%20NORM%5FL1%7D%5C%29%20%7D%0A)
NORM_L1 = 2
# ![block formula](https://latex.codecogs.com/png.latex?%0Anorm%20%3D%20%20%5Cforkthree%0A%7B%20%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%5C%7C%20%5F%7BL%5F2%7D%20%3D%20%20%5Csqrt%7B%5Csum%5FI%20%5Ctexttt%7Bsrc1%7D%28I%29%5E2%7D%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL2%7D%5C%29%20%7D%0A%7B%20%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%2D%20%5Ctexttt%7Bsrc2%7D%20%5C%7C%20%5F%7BL%5F2%7D%20%3D%20%20%5Csqrt%7B%5Csum%5FI%20%28%5Ctexttt%7Bsrc1%7D%28I%29%20%2D%20%5Ctexttt%7Bsrc2%7D%28I%29%29%5E2%7D%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL2%7D%5C%29%20%7D%0A%7B%20%5Cfrac%7B%5C%7C%5Ctexttt%7Bsrc1%7D%2D%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F2%7D%20%7D%7B%5C%7C%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F2%7D%7D%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FRELATIVE%20%7C%20NORM%5FL2%7D%5C%29%20%7D%0A)
NORM_L2 = 4
# ![block formula](https://latex.codecogs.com/png.latex?%0Anorm%20%3D%20%20%5Cforkthree%0A%7B%20%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%5C%7C%20%5F%7BL%5F2%7D%20%5E%7B2%7D%20%3D%20%5Csum%5FI%20%5Ctexttt%7Bsrc1%7D%28I%29%5E2%7D%20%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL2SQR%7D%5C%29%7D%0A%7B%20%5C%7C%20%5Ctexttt%7Bsrc1%7D%20%2D%20%5Ctexttt%7Bsrc2%7D%20%5C%7C%20%5F%7BL%5F2%7D%20%5E%7B2%7D%20%3D%20%20%5Csum%5FI%20%28%5Ctexttt%7Bsrc1%7D%28I%29%20%2D%20%5Ctexttt%7Bsrc2%7D%28I%29%29%5E2%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FL2SQR%7D%5C%29%20%7D%0A%7B%20%5Cleft%28%5Cfrac%7B%5C%7C%5Ctexttt%7Bsrc1%7D%2D%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F2%7D%20%7D%7B%5C%7C%5Ctexttt%7Bsrc2%7D%5C%7C%5F%7BL%5F2%7D%7D%5Cright%29%5E2%20%7D%7Bif%20%20%5C%28%5Ctexttt%7BnormType%7D%20%3D%20%5Ctexttt%7BNORM%5FRELATIVE%20%7C%20NORM%5FL2SQR%7D%5C%29%20%7D%0A)
NORM_L2SQR = 5
# flag
NORM_MINMAX = 32
# flag
NORM_RELATIVE = 8
# bit-mask which can be used to separate norm type from norm flags
NORM_TYPE_MASK = 7
OCL_VECTOR_DEFAULT = 0
OCL_VECTOR_MAX = 1
OCL_VECTOR_OWN = 0
OPENCV_ABI_COMPATIBILITY = 400
OPENCV_USE_FASTMATH_BUILTINS = 1
# OpenCL API call error
OpenCLApiCallError = -220
OpenCLDoubleNotSupported = -221
# OpenCL initialization error
OpenCLInitError = -222
OpenCLNoAMDBlasFft = -223
# OpenGL API call error
OpenGlApiCallError = -219
# no OpenGL support
OpenGlNotSupported = -218
POINTS = 0
POLYGON = 9
Param_ALGORITHM = 6
Param_BOOLEAN = 1
Param_FLOAT = 7
Param_INT = 0
Param_MAT = 4
Param_MAT_VECTOR = 5
Param_REAL = 2
Param_SCALAR = 12
Param_STRING = 3
Param_UCHAR = 11
Param_UINT64 = 9
Param_UNSIGNED_INT = 8
QUADS = 7
QUAD_STRIP = 8
# the output is the mean vector of all rows/columns of the matrix.
REDUCE_AVG = 1
# the output is the maximum (column/row-wise) of all rows/columns of the matrix.
REDUCE_MAX = 2
# the output is the minimum (column/row-wise) of all rows/columns of the matrix.
REDUCE_MIN = 3
# the output is the sum of all rows/columns of the matrix.
REDUCE_SUM = 0
RNG_NORMAL = 1
RNG_UNIFORM = 0
# Rotate 180 degrees clockwise
ROTATE_180 = 1
# Rotate 90 degrees clockwise
ROTATE_90_CLOCKWISE = 0
# Rotate 270 degrees clockwise
ROTATE_90_COUNTERCLOCKWISE = 2
SHARED_ATOMICS = 12
# there are multiple maxima for target function - the arbitrary one is returned
SOLVELP_MULTI = 1
# there is only one maximum for target function
SOLVELP_SINGLE = 0
# problem is unbounded (target function can achieve arbitrary high values)
SOLVELP_UNBOUNDED = -2
# problem is unfeasible (there are no points that satisfy all the constraints imposed)
SOLVELP_UNFEASIBLE = -1
# each matrix row is sorted in the ascending
# order.
SORT_ASCENDING = 0
# each matrix row is sorted in the
# descending order this flag and the previous one are also
# mutually exclusive.
SORT_DESCENDING = 16
# each matrix column is sorted
# independently this flag and the previous one are
# mutually exclusive.
SORT_EVERY_COLUMN = 1
# each matrix row is sorted independently
SORT_EVERY_ROW = 0
SparseMat_HASH_BIT = -2147483648
SparseMat_HASH_SCALE = 1540483477
SparseMat_MAGIC_VAL = 1123876864
SparseMat_MAX_DIM = 32
# assertion failed
StsAssert = -215
# tracing
StsAutoTrace = -8
# pseudo error for back trace
StsBackTrace = -1
# function arg/param is bad
StsBadArg = -5
# flag is wrong or not supported
StsBadFlag = -206
# unsupported function
StsBadFunc = -6
# bad format of mask (neither 8uC1 nor 8sC1)
StsBadMask = -208
# an allocated block has been corrupted
StsBadMemBlock = -214
# bad CvPoint
StsBadPoint = -207
# the input/output structure size is incorrect
StsBadSize = -201
# division by zero
StsDivByZero = -202
# unknown /unspecified error
StsError = -2
# incorrect filter offset value
StsFilterOffsetErr = -31
# incorrect filter structure content
StsFilterStructContentErr = -29
# in-place operation is not supported
StsInplaceNotSupported = -203
# internal error (bad state)
StsInternal = -3
# incorrect transform kernel content
StsKernelStructContentErr = -30
# iteration didn't converge
StsNoConv = -7
# insufficient memory
StsNoMem = -4
# the requested function/feature is not implemented
StsNotImplemented = -213
# null pointer
StsNullPtr = -27
# request can't be completed
StsObjectNotFound = -204
# everything is ok
StsOk = 0
# some of parameters are out of range
StsOutOfRange = -211
# invalid syntax/structure of the parsed file
StsParseError = -212
# formats of input/output arrays differ
StsUnmatchedFormats = -205
# sizes of input/output structures do not match
StsUnmatchedSizes = -209
# the data format/type is not supported by the function
StsUnsupportedFormat = -210
# incorrect vector length
StsVecLengthErr = -28
TRIANGLES = 4
TRIANGLE_FAN = 6
TRIANGLE_STRIP = 5
TYPE_FUN = 3
TYPE_GENERAL = 0
TYPE_MARKER = 1
TYPE_WRAPPER = 2
UMat_AUTO_STEP = 0
UMat_CONTINUOUS_FLAG = 16384
UMat_DEPTH_MASK = 7
UMat_MAGIC_MASK = -65536
UMat_MAGIC_VAL = 1124007936
UMat_SUBMATRIX_FLAG = 32768
UMat_TYPE_MASK = 4095
USAGE_ALLOCATE_DEVICE_MEMORY = 2
USAGE_ALLOCATE_HOST_MEMORY = 1
USAGE_ALLOCATE_SHARED_MEMORY = 4
USAGE_DEFAULT = 0
WARP_SHUFFLE_FUNCTIONS = 30
__UMAT_USAGE_FLAGS_32BIT = 2147483647
