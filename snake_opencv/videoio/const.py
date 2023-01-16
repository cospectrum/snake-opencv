# Android - not used
CAP_ANDROID = 1000
# Auto detect == 0
CAP_ANY = 0
# Aravis SDK
CAP_ARAVIS = 2100
# AVFoundation framework for iOS (OS X Lion will have the same API)
CAP_AVFOUNDATION = 1200
# Same value as CAP_FIREWIRE
CAP_CMU1394 = 300
# Same value as CAP_FIREWIRE
CAP_DC1394 = 300
# DirectShow (via videoInput)
CAP_DSHOW = 700
# Open and record video file or stream using the FFMPEG library
CAP_FFMPEG = 1900
# Same value as CAP_FIREWIRE
CAP_FIREWARE = 300
# IEEE 1394 drivers
CAP_FIREWIRE = 300
# Smartek Giganetix GigEVisionSDK
CAP_GIGANETIX = 1300
# gPhoto2 connection
CAP_GPHOTO2 = 1700
# GStreamer
CAP_GSTREAMER = 1800
# Same value as CAP_FIREWIRE
CAP_IEEE1394 = 300
# OpenCV Image Sequence (e.g. img_%02d.jpg)
CAP_IMAGES = 2000
# RealSense (former Intel Perceptual Computing SDK)
CAP_INTELPERC = 1500
CAP_INTELPERC_DEPTH_GENERATOR = 536870912
# Each pixel is a 16-bit integer. The value indicates the distance from an object to the camera's XY plane or the Cartesian depth.
CAP_INTELPERC_DEPTH_MAP = 0
CAP_INTELPERC_GENERATORS_MASK = 939524096
CAP_INTELPERC_IMAGE = 3
CAP_INTELPERC_IMAGE_GENERATOR = 268435456
CAP_INTELPERC_IR_GENERATOR = 134217728
# Each pixel is a 16-bit integer. The value indicates the intensity of the reflected laser beam.
CAP_INTELPERC_IR_MAP = 2
# Each pixel contains two 32-bit floating point values in the range of 0-1, representing the mapping of depth coordinates to the color coordinates.
CAP_INTELPERC_UVDEPTH_MAP = 1
# Intel MediaSDK
CAP_INTEL_MFX = 2300
# Microsoft Media Foundation (via videoInput)
CAP_MSMF = 1400
# For Orbbec 3D-Sensor device/module (Astra+, Femto)
CAP_OBSENSOR = 2600
# Data given from BGR stream generator
CAP_OBSENSOR_BGR_IMAGE = 1
CAP_OBSENSOR_DEPTH_GENERATOR = 536870912
# Depth values in mm (CV_16UC1)
CAP_OBSENSOR_DEPTH_MAP = 0
CAP_OBSENSOR_GENERATORS_MASK = 939524096
CAP_OBSENSOR_IMAGE_GENERATOR = 268435456
CAP_OBSENSOR_IR_GENERATOR = 134217728
# Data given from IR stream generator(CV_16UC1)
CAP_OBSENSOR_IR_IMAGE = 2
# Built-in OpenCV MotionJPEG codec
CAP_OPENCV_MJPEG = 2200
# OpenNI (for Kinect)
CAP_OPENNI = 900
# OpenNI2 (for Kinect)
CAP_OPENNI2 = 1600
# OpenNI2 (for Orbbec Astra)
CAP_OPENNI2_ASTRA = 1620
# OpenNI2 (for Asus Xtion and Occipital Structure sensors)
CAP_OPENNI2_ASUS = 1610
# OpenNI (for Asus Xtion)
CAP_OPENNI_ASUS = 910
# Data given from RGB image generator
CAP_OPENNI_BGR_IMAGE = 5
CAP_OPENNI_DEPTH_GENERATOR = -2147483648
CAP_OPENNI_DEPTH_GENERATOR_BASELINE = -2147483546
CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH = -2147483545
CAP_OPENNI_DEPTH_GENERATOR_PRESENT = -2147483539
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION = -2147483544
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION_ON = -2147483544
# Depth values in mm (CV_16UC1)
CAP_OPENNI_DEPTH_MAP = 0
# Disparity in pixels (CV_8UC1)
CAP_OPENNI_DISPARITY_MAP = 2
# Disparity in pixels (CV_32FC1)
CAP_OPENNI_DISPARITY_MAP_32F = 3
CAP_OPENNI_GENERATORS_MASK = -536870912
# Data given from RGB image generator
CAP_OPENNI_GRAY_IMAGE = 6
CAP_OPENNI_IMAGE_GENERATOR = 1073741824
CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE = 1073741924
CAP_OPENNI_IMAGE_GENERATOR_PRESENT = 1073741933
CAP_OPENNI_IR_GENERATOR = 536870912
CAP_OPENNI_IR_GENERATOR_PRESENT = 536871021
# Data given from IR image generator
CAP_OPENNI_IR_IMAGE = 7
# XYZ in meters (CV_32FC3)
CAP_OPENNI_POINT_CLOUD_MAP = 1
CAP_OPENNI_QVGA_30HZ = 3
CAP_OPENNI_QVGA_60HZ = 4
CAP_OPENNI_SXGA_15HZ = 1
CAP_OPENNI_SXGA_30HZ = 2
# CV_8UC1
CAP_OPENNI_VALID_DEPTH_MASK = 4
CAP_OPENNI_VGA_30HZ = 0
# Aperture. Can be readonly, depends on camera program.
CAP_PROP_APERTURE = 17008
# Automatically trigger frame capture if camera is configured with software trigger
CAP_PROP_ARAVIS_AUTOTRIGGER = 600
# (read-only) Index of the first audio channel for .retrieve() calls. That audio channel number continues enumeration after video channels.
CAP_PROP_AUDIO_BASE_INDEX = 63
# (open, read) Alternative definition to bits-per-sample, but with clear handling of 32F / 32S
CAP_PROP_AUDIO_DATA_DEPTH = 61
# (read-only) Audio position is measured in samples. Accurate audio sample timestamp of previous grabbed fragment. See CAP_PROP_AUDIO_SAMPLES_PER_SECOND and CAP_PROP_AUDIO_SHIFT_NSEC.
CAP_PROP_AUDIO_POS = 59
# (open, read) determined from file/codec input. If not specified, then selected audio sample rate is 44100
CAP_PROP_AUDIO_SAMPLES_PER_SECOND = 62
# (read only) Contains the time difference between the start of the audio stream and the video stream in nanoseconds. Positive value means that audio is started after the first video frame. Negative value means that audio is started before the first video frame.
CAP_PROP_AUDIO_SHIFT_NSEC = 60
# (**open-only**) Specify stream in multi-language media files, -1 - disable audio processing or microphone. Default value is -1.
CAP_PROP_AUDIO_STREAM = 58
# (open, read) Enables audio synchronization.
CAP_PROP_AUDIO_SYNCHRONIZE = 66
# (read-only) Number of audio channels in the selected audio stream (mono, stereo, etc)
CAP_PROP_AUDIO_TOTAL_CHANNELS = 64
# (read-only) Number of audio streams.
CAP_PROP_AUDIO_TOTAL_STREAMS = 65
CAP_PROP_AUTOFOCUS = 39
# DC1394: exposure control done by camera, user can adjust reference level using this feature.
CAP_PROP_AUTO_EXPOSURE = 21
# enable/ disable auto white-balance
CAP_PROP_AUTO_WB = 44
# Current backend (enum VideoCaptureAPIs). Read-only property
CAP_PROP_BACKEND = 42
CAP_PROP_BACKLIGHT = 32
# (read-only) Video bitrate in kbits/s
CAP_PROP_BITRATE = 47
# Brightness of the image (only for those cameras that support).
CAP_PROP_BRIGHTNESS = 10
CAP_PROP_BUFFERSIZE = 38
# Video input or Channel Number (only for those cameras that support)
CAP_PROP_CHANNEL = 43
# Positive index indicates that returning extra data is supported by the video back end.  This can be retrieved as cap.retrieve(data, <returned index>).  E.g. When reading from a h264 encoded RTSP stream, the FFmpeg backend could return the SPS and/or PPS if available (if sent in reply to a DESCRIBE request), from calls to cap.retrieve(data, <returned index>).
CAP_PROP_CODEC_EXTRADATA_INDEX = 68
# (read-only) codec's pixel format. 4-character code - see VideoWriter::fourcc . Subset of [AV_PIX_FMT_*](https://github.com/FFmpeg/FFmpeg/blob/master/libavcodec/raw.c) or -1 if unknown
CAP_PROP_CODEC_PIXEL_FORMAT = 46
# Contrast of the image (only for cameras).
CAP_PROP_CONTRAST = 11
# Boolean flags indicating whether images should be converted to RGB. <br/>
# *GStreamer note*: The flag is ignored in case if custom pipeline is used. It's user responsibility to interpret pipeline output.
CAP_PROP_CONVERT_RGB = 16
CAP_PROP_DC1394_MAX = 31
CAP_PROP_DC1394_MODE_AUTO = -2
# set automatically when a value of the feature is set by the user.
CAP_PROP_DC1394_MODE_MANUAL = -3
CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO = -1
# turn the feature off (not controlled manually nor automatically).
CAP_PROP_DC1394_OFF = -4
# Exposure (only for those cameras that support).
CAP_PROP_EXPOSURE = 15
# Camera exposure program.
CAP_PROP_EXPOSUREPROGRAM = 17009
CAP_PROP_FOCUS = 28
# Format of the %Mat objects (see Mat::type()) returned by VideoCapture::retrieve().
# Set value -1 to fetch undecoded RAW video streams (as Mat 8UC1).
CAP_PROP_FORMAT = 8
# 4-character code of codec. see VideoWriter::fourcc .
CAP_PROP_FOURCC = 6
# Frame rate.
CAP_PROP_FPS = 5
# Number of frames in the video file.
CAP_PROP_FRAME_COUNT = 7
# Height of the frames in the video stream.
CAP_PROP_FRAME_HEIGHT = 4
# (read-only) FFmpeg back-end only - Frame type ascii code (73 = 'I', 80 = 'P', 66 = 'B' or 63 = '?' if unknown) of the most recently read frame.
CAP_PROP_FRAME_TYPE = 69
# Width of the frames in the video stream.
CAP_PROP_FRAME_WIDTH = 3
# Gain of the image (only for those cameras that support).
CAP_PROP_GAIN = 14
CAP_PROP_GAMMA = 22
CAP_PROP_GIGA_FRAME_HEIGH_MAX = 10004
CAP_PROP_GIGA_FRAME_OFFSET_X = 10001
CAP_PROP_GIGA_FRAME_OFFSET_Y = 10002
CAP_PROP_GIGA_FRAME_SENS_HEIGH = 10006
CAP_PROP_GIGA_FRAME_SENS_WIDTH = 10005
CAP_PROP_GIGA_FRAME_WIDTH_MAX = 10003
# Collect messages with details.
CAP_PROP_GPHOTO2_COLLECT_MSGS = 17005
# Readonly, returns (const char *).
CAP_PROP_GPHOTO2_FLUSH_MSGS = 17006
# Capture only preview from liveview mode.
CAP_PROP_GPHOTO2_PREVIEW = 17001
# Trigger, only by set. Reload camera settings.
CAP_PROP_GPHOTO2_RELOAD_CONFIG = 17003
# Reload all settings on set.
CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE = 17004
# Readonly, returns (const char *).
CAP_PROP_GPHOTO2_WIDGET_ENUMERATE = 17002
# Default is 1
CAP_PROP_GSTREAMER_QUEUE_LENGTH = 200
CAP_PROP_GUID = 29
# Hue of the image (only for cameras).
CAP_PROP_HUE = 13
# (**open-only**) Hardware acceleration type (see #VideoAccelerationType). Setting supported only via `params` parameter in cv::VideoCapture constructor / .open() method. Default value is backend-specific.
CAP_PROP_HW_ACCELERATION = 50
# (**open-only**) If non-zero, create new OpenCL context and bind it to current thread. The OpenCL context created with Video Acceleration context attached it (if not attached yet) for optimized GPU data copy between HW accelerated decoder and cv::UMat.
CAP_PROP_HW_ACCELERATION_USE_OPENCL = 52
# (**open-only**) Hardware device index (select GPU if multiple available). Device enumeration is acceleration type specific.
CAP_PROP_HW_DEVICE = 51
CAP_PROP_IMAGES_BASE = 18000
CAP_PROP_IMAGES_LAST = 19000
CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD = 11005
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ = 11006
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT = 11007
CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE = 11003
CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE = 11004
CAP_PROP_INTELPERC_PROFILE_COUNT = 11001
CAP_PROP_INTELPERC_PROFILE_IDX = 11002
CAP_PROP_IOS_DEVICE_EXPOSURE = 9002
CAP_PROP_IOS_DEVICE_FLASH = 9003
CAP_PROP_IOS_DEVICE_FOCUS = 9001
CAP_PROP_IOS_DEVICE_TORCH = 9005
CAP_PROP_IOS_DEVICE_WHITEBALANCE = 9004
CAP_PROP_IRIS = 36
CAP_PROP_ISO_SPEED = 30
# FFmpeg back-end only - Indicates whether the Last Raw Frame (LRF), output from VideoCapture::read() when VideoCapture is initialized with VideoCapture::open(CAP_FFMPEG, {CAP_PROP_FORMAT, -1}) or VideoCapture::set(CAP_PROP_FORMAT,-1) is called before the first call to VideoCapture::read(), contains encoded data for a key frame.
CAP_PROP_LRF_HAS_KEY_FRAME = 67
# Backend-specific value indicating the current capture mode.
CAP_PROP_MODE = 9
CAP_PROP_MONOCHROME = 19
# (**open-only**) Set the maximum number of threads to use. Use 0 to use as many threads as CPU cores (applicable for FFmpeg back-end only).
CAP_PROP_N_THREADS = 70
CAP_PROP_OBSENSOR_INTRINSIC_CX = 26003
CAP_PROP_OBSENSOR_INTRINSIC_CY = 26004
CAP_PROP_OBSENSOR_INTRINSIC_FX = 26001
CAP_PROP_OBSENSOR_INTRINSIC_FY = 26002
CAP_PROP_OPENNI2_MIRROR = 111
CAP_PROP_OPENNI2_SYNC = 110
CAP_PROP_OPENNI_APPROX_FRAME_SYNC = 105
# In mm
CAP_PROP_OPENNI_BASELINE = 102
CAP_PROP_OPENNI_CIRCLE_BUFFER = 107
# In pixels
CAP_PROP_OPENNI_FOCAL_LENGTH = 103
# In mm
CAP_PROP_OPENNI_FRAME_MAX_DEPTH = 101
CAP_PROP_OPENNI_GENERATOR_PRESENT = 109
CAP_PROP_OPENNI_MAX_BUFFER_SIZE = 106
CAP_PROP_OPENNI_MAX_TIME_DURATION = 108
CAP_PROP_OPENNI_OUTPUT_MODE = 100
# Flag that synchronizes the remapping depth map to image map
# by changing depth generator's view point (if the flag is "on") or
# sets this view point to its normal one (if the flag is "off").
CAP_PROP_OPENNI_REGISTRATION = 104
CAP_PROP_OPENNI_REGISTRATION_ON = 104
# (**open-only**) timeout in milliseconds for opening a video capture (applicable for FFmpeg and GStreamer back-ends only)
CAP_PROP_OPEN_TIMEOUT_MSEC = 53
# if true - rotates output frames of CvCapture considering video file's metadata  (applicable for FFmpeg and AVFoundation back-ends only)
# (https://github.com/opencv/opencv/issues/15499)
CAP_PROP_ORIENTATION_AUTO = 49
# (read-only) Frame rotation defined by stream meta (applicable for FFmpeg and AVFoundation back-ends only)
CAP_PROP_ORIENTATION_META = 48
CAP_PROP_PAN = 33
# Relative position of the video file: 0=start of the film, 1=end of the film.
CAP_PROP_POS_AVI_RATIO = 2
# 0-based index of the frame to be decoded/captured next.
CAP_PROP_POS_FRAMES = 1
# Current position of the video file in milliseconds.
CAP_PROP_POS_MSEC = 0
# Horizontal binning factor.
CAP_PROP_PVAPI_BINNINGX = 304
# Vertical binning factor.
CAP_PROP_PVAPI_BINNINGY = 305
# Horizontal sub-sampling of the image.
CAP_PROP_PVAPI_DECIMATIONHORIZONTAL = 302
# Vertical sub-sampling of the image.
CAP_PROP_PVAPI_DECIMATIONVERTICAL = 303
# FrameStartTriggerMode: Determines how a frame is initiated.
CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE = 301
# IP for enable multicast master mode. 0 for disable multicast.
CAP_PROP_PVAPI_MULTICASTIP = 300
# Pixel format.
CAP_PROP_PVAPI_PIXELFORMAT = 306
# (**open-only**) timeout in milliseconds for reading from a video capture (applicable for FFmpeg and GStreamer back-ends only)
CAP_PROP_READ_TIMEOUT_MSEC = 54
# Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).
CAP_PROP_RECTIFICATION = 18
CAP_PROP_ROLL = 35
# Sample aspect ratio: num/den (den)
CAP_PROP_SAR_DEN = 41
# Sample aspect ratio: num/den (num)
CAP_PROP_SAR_NUM = 40
# Saturation of the image (only for cameras).
CAP_PROP_SATURATION = 12
# Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. The property value is ignored)
CAP_PROP_SETTINGS = 37
CAP_PROP_SHARPNESS = 20
# Exposure speed. Can be readonly, depends on camera program.
CAP_PROP_SPEED = 17007
CAP_PROP_STREAM_OPEN_TIME_USEC = 55
CAP_PROP_TEMPERATURE = 23
CAP_PROP_TILT = 34
CAP_PROP_TRIGGER = 24
CAP_PROP_TRIGGER_DELAY = 25
# (**open-only**) Specify video stream, 0-based index. Use -1 to disable video stream from file or IP cameras. Default value is 0.
CAP_PROP_VIDEO_STREAM = 57
# (read-only) Number of video channels
CAP_PROP_VIDEO_TOTAL_CHANNELS = 56
# Enter liveview mode.
CAP_PROP_VIEWFINDER = 17010
# white-balance color temperature
CAP_PROP_WB_TEMPERATURE = 45
# Currently unsupported.
CAP_PROP_WHITE_BALANCE_BLUE_U = 17
CAP_PROP_WHITE_BALANCE_RED_V = 26
# Acquisition buffer size in buffer_size_unit. Default bytes.
CAP_PROP_XI_ACQ_BUFFER_SIZE = 548
# Acquisition buffer size unit in bytes. Default 1. E.g. Value 1024 means that buffer_size is in KiBytes.
CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT = 549
# Sets number of frames acquired by burst. This burst is used only if trigger is set to FrameBurstStart.
CAP_PROP_XI_ACQ_FRAME_BURST_COUNT = 499
# Type of sensor frames timing.
CAP_PROP_XI_ACQ_TIMING_MODE = 538
# Number of buffers to commit to low level.
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT = 552
# Acquisition transport buffer size in bytes.
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE = 550
# Automatic exposure/gain.
CAP_PROP_XI_AEAG = 415
# Average intensity of output signal AEAG should achieve(in %).
CAP_PROP_XI_AEAG_LEVEL = 419
# Automatic exposure/gain ROI Height.
CAP_PROP_XI_AEAG_ROI_HEIGHT = 442
# Automatic exposure/gain ROI offset X.
CAP_PROP_XI_AEAG_ROI_OFFSET_X = 439
# Automatic exposure/gain ROI offset Y.
CAP_PROP_XI_AEAG_ROI_OFFSET_Y = 440
# Automatic exposure/gain ROI Width.
CAP_PROP_XI_AEAG_ROI_WIDTH = 441
# Maximum limit of exposure in AEAG procedure.
CAP_PROP_XI_AE_MAX_LIMIT = 417
# Maximum limit of gain in AEAG procedure.
CAP_PROP_XI_AG_MAX_LIMIT = 418
# Enable applying of CMS profiles to xiGetImage (see XI_PRM_INPUT_CMS_PROFILE, XI_PRM_OUTPUT_CMS_PROFILE).
CAP_PROP_XI_APPLY_CMS = 471
# Automatic bandwidth calculation.
CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION = 573
# Automatic white balance.
CAP_PROP_XI_AUTO_WB = 414
# Calculate and returns available interface bandwidth(int Megabits).
CAP_PROP_XI_AVAILABLE_BANDWIDTH = 539
# Horizontal Binning - number of horizontal photo-sensitive cells to combine together.
CAP_PROP_XI_BINNING_HORIZONTAL = 429
# Binning pattern type.
CAP_PROP_XI_BINNING_PATTERN = 430
# Binning engine selector.
CAP_PROP_XI_BINNING_SELECTOR = 427
# Vertical Binning - number of vertical photo-sensitive cells to combine together.
CAP_PROP_XI_BINNING_VERTICAL = 428
# Correction of bad pixels.
CAP_PROP_XI_BPC = 445
# Queue of field/frame buffers.
CAP_PROP_XI_BUFFERS_QUEUE_SIZE = 551
# Data move policy.
CAP_PROP_XI_BUFFER_POLICY = 540
# Color Correction Matrix element [0][0].
CAP_PROP_XI_CC_MATRIX_00 = 479
# Color Correction Matrix element [0][1].
CAP_PROP_XI_CC_MATRIX_01 = 480
# Color Correction Matrix element [0][2].
CAP_PROP_XI_CC_MATRIX_02 = 481
# Color Correction Matrix element [0][3].
CAP_PROP_XI_CC_MATRIX_03 = 482
# Color Correction Matrix element [1][0].
CAP_PROP_XI_CC_MATRIX_10 = 483
# Color Correction Matrix element [1][1].
CAP_PROP_XI_CC_MATRIX_11 = 484
# Color Correction Matrix element [1][2].
CAP_PROP_XI_CC_MATRIX_12 = 485
# Color Correction Matrix element [1][3].
CAP_PROP_XI_CC_MATRIX_13 = 486
# Color Correction Matrix element [2][0].
CAP_PROP_XI_CC_MATRIX_20 = 487
# Color Correction Matrix element [2][1].
CAP_PROP_XI_CC_MATRIX_21 = 488
# Color Correction Matrix element [2][2].
CAP_PROP_XI_CC_MATRIX_22 = 489
# Color Correction Matrix element [2][3].
CAP_PROP_XI_CC_MATRIX_23 = 490
# Color Correction Matrix element [3][0].
CAP_PROP_XI_CC_MATRIX_30 = 491
# Color Correction Matrix element [3][1].
CAP_PROP_XI_CC_MATRIX_31 = 492
# Color Correction Matrix element [3][2].
CAP_PROP_XI_CC_MATRIX_32 = 493
# Color Correction Matrix element [3][3].
CAP_PROP_XI_CC_MATRIX_33 = 494
# Camera sensor temperature.
CAP_PROP_XI_CHIP_TEMP = 468
# Mode of color management system.
CAP_PROP_XI_CMS = 470
# Returns color filter array type of RAW data.
CAP_PROP_XI_COLOR_FILTER_ARRAY = 475
# Correction of column FPN.
CAP_PROP_XI_COLUMN_FPN_CORRECTION = 555
# Start camera cooling.
CAP_PROP_XI_COOLING = 466
# Select counter.
CAP_PROP_XI_COUNTER_SELECTOR = 536
# Counter status.
CAP_PROP_XI_COUNTER_VALUE = 537
# Output data format.
CAP_PROP_XI_DATA_FORMAT = 401
# Enable/Disable debounce to selected GPI.
CAP_PROP_XI_DEBOUNCE_EN = 507
# Debounce polarity (pol = 1 t0 - falling edge, t1 - rising edge).
CAP_PROP_XI_DEBOUNCE_POL = 510
# Debounce time (x * 10us).
CAP_PROP_XI_DEBOUNCE_T0 = 508
# Debounce time (x * 10us).
CAP_PROP_XI_DEBOUNCE_T1 = 509
# Set debug level.
CAP_PROP_XI_DEBUG_LEVEL = 572
# Horizontal Decimation - horizontal sub-sampling of the image - reduces the horizontal resolution of the image by the specified vertical decimation factor.
CAP_PROP_XI_DECIMATION_HORIZONTAL = 433
# Decimation pattern type.
CAP_PROP_XI_DECIMATION_PATTERN = 434
# Decimation engine selector.
CAP_PROP_XI_DECIMATION_SELECTOR = 431
# Vertical Decimation - vertical sub-sampling of the image - reduces the vertical resolution of the image by the specified vertical decimation factor.
CAP_PROP_XI_DECIMATION_VERTICAL = 432
# Set default Color Correction Matrix.
CAP_PROP_XI_DEFAULT_CC_MATRIX = 495
# Returns device model id.
CAP_PROP_XI_DEVICE_MODEL_ID = 521
# Resets the camera to default state.
CAP_PROP_XI_DEVICE_RESET = 554
# Returns device serial number.
CAP_PROP_XI_DEVICE_SN = 522
# Change image resolution by binning or skipping.
CAP_PROP_XI_DOWNSAMPLING = 400
# Change image downsampling type.
CAP_PROP_XI_DOWNSAMPLING_TYPE = 426
# Exposure time in microseconds.
CAP_PROP_XI_EXPOSURE = 421
# Sets the number of times of exposure in one frame.
CAP_PROP_XI_EXPOSURE_BURST_COUNT = 422
# Exposure priority (0.5 - exposure 50%, gain 50%).
CAP_PROP_XI_EXP_PRIORITY = 416
# Setting of key enables file operations on some cameras.
CAP_PROP_XI_FFS_ACCESS_KEY = 583
# File number.
CAP_PROP_XI_FFS_FILE_ID = 594
# Size of file.
CAP_PROP_XI_FFS_FILE_SIZE = 580
# Define framerate in Hz.
CAP_PROP_XI_FRAMERATE = 535
# Size of free camera FFS.
CAP_PROP_XI_FREE_FFS_SIZE = 581
# Gain in dB.
CAP_PROP_XI_GAIN = 424
# Gain selector for parameter Gain allows to select different type of gains.
CAP_PROP_XI_GAIN_SELECTOR = 423
# Chromaticity gamma.
CAP_PROP_XI_GAMMAC = 477
# Luminosity gamma.
CAP_PROP_XI_GAMMAY = 476
# Get general purpose level.
CAP_PROP_XI_GPI_LEVEL = 408
# Set general purpose input mode.
CAP_PROP_XI_GPI_MODE = 407
# Selects general purpose input.
CAP_PROP_XI_GPI_SELECTOR = 406
# Set general purpose output mode.
CAP_PROP_XI_GPO_MODE = 410
# Selects general purpose output.
CAP_PROP_XI_GPO_SELECTOR = 409
# Enable High Dynamic Range feature.
CAP_PROP_XI_HDR = 559
# The number of kneepoints in the PWLR.
CAP_PROP_XI_HDR_KNEEPOINT_COUNT = 560
# Position of first kneepoint(in % of XI_PRM_EXPOSURE).
CAP_PROP_XI_HDR_T1 = 561
# Position of second kneepoint (in % of XI_PRM_EXPOSURE).
CAP_PROP_XI_HDR_T2 = 562
# Height of the Image provided by the device (in pixels).
CAP_PROP_XI_HEIGHT = 452
# Camera housing back side temperature.
CAP_PROP_XI_HOUS_BACK_SIDE_TEMP = 590
# Camera housing temperature.
CAP_PROP_XI_HOUS_TEMP = 469
# Returns hardware revision number.
CAP_PROP_XI_HW_REVISION = 571
# Last image black level counts. Can be used for Offline processing to recall it.
CAP_PROP_XI_IMAGE_BLACK_LEVEL = 565
# bitdepth of data returned by function xiGetImage.
CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH = 462
# Output data format.
CAP_PROP_XI_IMAGE_DATA_FORMAT = 435
# The alpha channel of RGB32 output image format.
CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA = 529
# Returns 1 for color cameras.
CAP_PROP_XI_IMAGE_IS_COLOR = 474
# Buffer size in bytes sufficient for output image returned by xiGetImage.
CAP_PROP_XI_IMAGE_PAYLOAD_SIZE = 530
# Returns 1 for cameras that support cooling.
CAP_PROP_XI_IS_COOLED = 465
# Returns 1 if camera connected and works properly.
CAP_PROP_XI_IS_DEVICE_EXIST = 547
# Value of first kneepoint (% of sensor saturation).
CAP_PROP_XI_KNEEPOINT1 = 563
# Value of second kneepoint (% of sensor saturation).
CAP_PROP_XI_KNEEPOINT2 = 564
# Define camera signalling LED functionality.
CAP_PROP_XI_LED_MODE = 412
# Selects camera signalling LED.
CAP_PROP_XI_LED_SELECTOR = 411
# Current lens aperture value in stops. Examples: 2.8, 4, 5.6, 8, 11.
CAP_PROP_XI_LENS_APERTURE_VALUE = 512
# Allows access to lens feature value currently selected by XI_PRM_LENS_FEATURE_SELECTOR.
CAP_PROP_XI_LENS_FEATURE = 518
# Selects the current feature which is accessible by XI_PRM_LENS_FEATURE.
CAP_PROP_XI_LENS_FEATURE_SELECTOR = 517
# Lens focal distance in mm.
CAP_PROP_XI_LENS_FOCAL_LENGTH = 516
# Lens focus distance in cm.
CAP_PROP_XI_LENS_FOCUS_DISTANCE = 515
# Moves lens focus motor by steps set in XI_PRM_LENS_FOCUS_MOVEMENT_VALUE.
CAP_PROP_XI_LENS_FOCUS_MOVE = 514
# Lens current focus movement value to be used by XI_PRM_LENS_FOCUS_MOVE in motor steps.
CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE = 513
# Status of lens control interface. This shall be set to XI_ON before any Lens operations.
CAP_PROP_XI_LENS_MODE = 511
# Set/get bandwidth(datarate)(in Megabits).
CAP_PROP_XI_LIMIT_BANDWIDTH = 459
# Activates LUT.
CAP_PROP_XI_LUT_EN = 541
# Control the index (offset) of the coefficient to access in the LUT.
CAP_PROP_XI_LUT_INDEX = 542
# Value at entry LUTIndex of the LUT.
CAP_PROP_XI_LUT_VALUE = 543
# Calculates White Balance(must be called during acquisition).
CAP_PROP_XI_MANUAL_WB = 413
# Horizontal offset from the origin to the area of interest (in pixels).
CAP_PROP_XI_OFFSET_X = 402
# Vertical offset from the origin to the area of interest (in pixels).
CAP_PROP_XI_OFFSET_Y = 403
# Device output data bit depth.
CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH = 461
# Device output data packing (or grouping) enabled. Packing could be enabled if output_data_bit_depth > 8 and packing capability is available.
CAP_PROP_XI_OUTPUT_DATA_PACKING = 463
# Data packing type. Some cameras supports only specific packing type.
CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE = 464
# GetImage returns most recent frame.
CAP_PROP_XI_RECENT_FRAME = 553
# Activates/deactivates Region selected by Region Selector.
CAP_PROP_XI_REGION_MODE = 595
# Selects Region in Multiple ROI which parameters are set by width, height, ... ,region mode.
CAP_PROP_XI_REGION_SELECTOR = 589
# Correction of row FPN.
CAP_PROP_XI_ROW_FPN_CORRECTION = 591
# Camera sensor board temperature.
CAP_PROP_XI_SENSOR_BOARD_TEMP = 596
# Sensor clock frequency in Hz.
CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ = 532
# Sensor clock frequency index. Sensor with selected frequencies have possibility to set the frequency only by this index.
CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX = 533
# Sensor output data bit depth.
CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH = 460
# Selects the current feature which is accessible by XI_PRM_SENSOR_FEATURE_VALUE.
CAP_PROP_XI_SENSOR_FEATURE_SELECTOR = 585
# Allows access to sensor feature value currently selected by XI_PRM_SENSOR_FEATURE_SELECTOR.
CAP_PROP_XI_SENSOR_FEATURE_VALUE = 586
# Current sensor mode. Allows to select sensor mode by one integer. Setting of this parameter affects: image dimensions and downsampling.
CAP_PROP_XI_SENSOR_MODE = 558
# Number of output channels from sensor used for data transfer.
CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT = 534
# Number of taps.
CAP_PROP_XI_SENSOR_TAPS = 437
# Sharpness Strength.
CAP_PROP_XI_SHARPNESS = 478
# Change sensor shutter type(CMOS sensor).
CAP_PROP_XI_SHUTTER_TYPE = 436
# Set sensor target temperature for cooling.
CAP_PROP_XI_TARGET_TEMP = 467
# Selects which test pattern type is generated by the selected generator.
CAP_PROP_XI_TEST_PATTERN = 588
# Selects which test pattern generator is controlled by the TestPattern feature.
CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR = 587
# Image capture timeout in milliseconds.
CAP_PROP_XI_TIMEOUT = 420
# Current format of pixels on transport layer.
CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT = 531
# Specifies the delay in microseconds (us) to apply after the trigger reception before activating it.
CAP_PROP_XI_TRG_DELAY = 544
# Selects the type of trigger.
CAP_PROP_XI_TRG_SELECTOR = 498
# Generates an internal trigger. PRM_TRG_SOURCE must be set to TRG_SOFTWARE.
CAP_PROP_XI_TRG_SOFTWARE = 405
# Defines source of trigger.
CAP_PROP_XI_TRG_SOURCE = 404
# Defines how time stamp reset engine will be armed.
CAP_PROP_XI_TS_RST_MODE = 545
# Defines which source will be used for timestamp reset. Writing this parameter will trigger settings of engine (arming).
CAP_PROP_XI_TS_RST_SOURCE = 546
# Size of used camera FFS.
CAP_PROP_XI_USED_FFS_SIZE = 582
# White balance blue coefficient.
CAP_PROP_XI_WB_KB = 450
# White balance green coefficient.
CAP_PROP_XI_WB_KG = 449
# White balance red coefficient.
CAP_PROP_XI_WB_KR = 448
# Width of the Image provided by the device (in pixels).
CAP_PROP_XI_WIDTH = 451
CAP_PROP_ZOOM = 27
# PvAPI, Prosilica GigE SDK
CAP_PVAPI = 800
# 2 out of 16 decimation
CAP_PVAPI_DECIMATION_2OUTOF16 = 8
# 2 out of 4 decimation
CAP_PVAPI_DECIMATION_2OUTOF4 = 2
# 2 out of 8 decimation
CAP_PVAPI_DECIMATION_2OUTOF8 = 4
# Off
CAP_PVAPI_DECIMATION_OFF = 1
# FixedRate
CAP_PVAPI_FSTRIGMODE_FIXEDRATE = 3
# Freerun
CAP_PVAPI_FSTRIGMODE_FREERUN = 0
# Software
CAP_PVAPI_FSTRIGMODE_SOFTWARE = 4
# SyncIn1
CAP_PVAPI_FSTRIGMODE_SYNCIN1 = 1
# SyncIn2
CAP_PVAPI_FSTRIGMODE_SYNCIN2 = 2
# Bayer16
CAP_PVAPI_PIXELFORMAT_BAYER16 = 4
# Bayer8
CAP_PVAPI_PIXELFORMAT_BAYER8 = 3
# Bgr24
CAP_PVAPI_PIXELFORMAT_BGR24 = 6
# Bgra32
CAP_PVAPI_PIXELFORMAT_BGRA32 = 8
# Mono16
CAP_PVAPI_PIXELFORMAT_MONO16 = 2
# Mono8
CAP_PVAPI_PIXELFORMAT_MONO8 = 1
# Rgb24
CAP_PVAPI_PIXELFORMAT_RGB24 = 5
# Rgba32
CAP_PVAPI_PIXELFORMAT_RGBA32 = 7
# QuickTime (obsolete, removed)
CAP_QT = 500
# Synonym for CAP_INTELPERC
CAP_REALSENSE = 1500
# uEye Camera API
CAP_UEYE = 2500
# Unicap drivers (obsolete, removed)
CAP_UNICAP = 600
# V4L/V4L2 capturing support
CAP_V4L = 200
# Same as CAP_V4L
CAP_V4L2 = 200
# Video For Windows (obsolete, removed)
CAP_VFW = 200
# Microsoft Windows Runtime using Media Foundation
CAP_WINRT = 1410
# XIMEA Camera API
CAP_XIAPI = 1100
# XINE engine (Linux)
CAP_XINE = 2400
CV__CAP_PROP_LATEST = 71
CV__VIDEOWRITER_PROP_LATEST = 9
# Defaults to CV_8U.
VIDEOWRITER_PROP_DEPTH = 5
# (Read-only): Size of just encoded video frame. Note that the encoding order may be different from representation order.
VIDEOWRITER_PROP_FRAMEBYTES = 2
# (**open-only**) Hardware acceleration type (see #VideoAccelerationType). Setting supported only via `params` parameter in VideoWriter constructor / .open() method. Default value is backend-specific.
VIDEOWRITER_PROP_HW_ACCELERATION = 6
# (**open-only**) If non-zero, create new OpenCL context and bind it to current thread. The OpenCL context created with Video Acceleration context attached it (if not attached yet) for optimized GPU data copy between cv::UMat and HW accelerated encoder.
VIDEOWRITER_PROP_HW_ACCELERATION_USE_OPENCL = 8
# (**open-only**) Hardware device index (select GPU if multiple available). Device enumeration is acceleration type specific.
VIDEOWRITER_PROP_HW_DEVICE = 7
# If it is not zero, the encoder will expect and encode color frames, otherwise it
# will work with grayscale frames.
VIDEOWRITER_PROP_IS_COLOR = 4
# Number of stripes for parallel encoding. -1 for auto detection.
VIDEOWRITER_PROP_NSTRIPES = 3
# Current quality (0..100%) of the encoded videostream. Can be adjusted dynamically in some codecs.
VIDEOWRITER_PROP_QUALITY = 1
# Prefer to use H/W acceleration. If no one supported, then fallback to software processing.
#
# Note: H/W acceleration may require special configuration of used environment.
#
# Note: Results in encoding scenario may differ between software and hardware accelerated encoders.
VIDEO_ACCELERATION_ANY = 1
# DirectX 11
VIDEO_ACCELERATION_D3D11 = 2
# libmfx (Intel MediaSDK/oneVPL)
VIDEO_ACCELERATION_MFX = 4
# Do not require any specific H/W acceleration, prefer software processing.
# Reading of this value means that special H/W accelerated handling is not added or not detected by OpenCV.
VIDEO_ACCELERATION_NONE = 0
# VAAPI
VIDEO_ACCELERATION_VAAPI = 3
