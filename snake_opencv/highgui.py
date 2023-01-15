import cv2
import numpy as np


__all__ = [
    'destroy_all_windows',
    'destroy_window',
    'named_window',
    'imshow',
    'resize_window',
    'wait_key',
    'EVENT_FLAG_ALTKEY',
    'EVENT_FLAG_CTRLKEY',
    'EVENT_FLAG_LBUTTON',
    'EVENT_FLAG_MBUTTON',
    'EVENT_FLAG_RBUTTON',
    'EVENT_FLAG_SHIFTKEY',
    'EVENT_LBUTTONDBLCLK',
    'EVENT_LBUTTONDOWN',
    'EVENT_LBUTTONUP',
    'EVENT_MBUTTONDBLCLK',
    'EVENT_MBUTTONDOWN',
    'EVENT_MBUTTONUP',
    'EVENT_MOUSEHWHEEL',
    'EVENT_MOUSEMOVE',
    'EVENT_MOUSEWHEEL',
    'EVENT_RBUTTONDBLCLK',
    'EVENT_RBUTTONDOWN',
    'EVENT_RBUTTONUP',
    'QT_CHECKBOX',
    'QT_FONT_BLACK',
    'QT_FONT_BOLD',
    'QT_FONT_DEMIBOLD',
    'QT_FONT_LIGHT',
    'QT_FONT_NORMAL',
    'QT_NEW_BUTTONBAR',
    'QT_PUSH_BUTTON',
    'QT_RADIOBOX',
    'QT_STYLE_ITALIC',
    'QT_STYLE_NORMAL',
    'QT_STYLE_OBLIQUE',
    'WINDOW_AUTOSIZE',
    'WINDOW_FREERATIO',
    'WINDOW_FULLSCREEN',
    'WINDOW_GUI_EXPANDED',
    'WINDOW_GUI_NORMAL',
    'WINDOW_KEEPRATIO',
    'WINDOW_NORMAL',
    'WINDOW_OPENGL',
    'WND_PROP_ASPECT_RATIO',
    'WND_PROP_AUTOSIZE',
    'WND_PROP_FULLSCREEN',
    'WND_PROP_OPENGL',
    'WND_PROP_TOPMOST',
    'WND_PROP_VISIBLE',
    'WND_PROP_VSYNC',
]

# indicates that ALT Key is pressed.
EVENT_FLAG_ALTKEY = 32
# indicates that CTRL Key is pressed.
EVENT_FLAG_CTRLKEY = 8
# indicates that the left mouse button is down.
EVENT_FLAG_LBUTTON = 1
# indicates that the middle mouse button is down.
EVENT_FLAG_MBUTTON = 4
# indicates that the right mouse button is down.
EVENT_FLAG_RBUTTON = 2
# indicates that SHIFT Key is pressed.
EVENT_FLAG_SHIFTKEY = 16
# indicates that left mouse button is double clicked.
EVENT_LBUTTONDBLCLK = 7
# indicates that the left mouse button is pressed.
EVENT_LBUTTONDOWN = 1
# indicates that left mouse button is released.
EVENT_LBUTTONUP = 4
# indicates that middle mouse button is double clicked.
EVENT_MBUTTONDBLCLK = 9
# indicates that the middle mouse button is pressed.
EVENT_MBUTTONDOWN = 3
# indicates that middle mouse button is released.
EVENT_MBUTTONUP = 6
# positive and negative values mean right and left scrolling, respectively.
EVENT_MOUSEHWHEEL = 11
# indicates that the mouse pointer has moved over the window.
EVENT_MOUSEMOVE = 0
# positive and negative values mean forward and backward scrolling, respectively.
EVENT_MOUSEWHEEL = 10
# indicates that right mouse button is double clicked.
EVENT_RBUTTONDBLCLK = 8
# indicates that the right mouse button is pressed.
EVENT_RBUTTONDOWN = 2
# indicates that right mouse button is released.
EVENT_RBUTTONUP = 5
# Checkbox button.
QT_CHECKBOX = 1
# Weight of 87
QT_FONT_BLACK = 87
# Weight of 75
QT_FONT_BOLD = 75
# Weight of 63
QT_FONT_DEMIBOLD = 63
# Weight of 25
QT_FONT_LIGHT = 25
# Weight of 50
QT_FONT_NORMAL = 50
# Button should create a new buttonbar
QT_NEW_BUTTONBAR = 1024
# Push button.
QT_PUSH_BUTTON = 0
# Radiobox button.
QT_RADIOBOX = 2
# Italic font.
QT_STYLE_ITALIC = 1
# Normal font.
QT_STYLE_NORMAL = 0
# Oblique font.
QT_STYLE_OBLIQUE = 2
# the user cannot resize the window, the size is constrainted by the image displayed.
WINDOW_AUTOSIZE = 1
# the image expends as much as it can (no ratio constraint).
WINDOW_FREERATIO = 256
# change the window to fullscreen.
WINDOW_FULLSCREEN = 1
# status bar and tool bar
WINDOW_GUI_EXPANDED = 0
# old fashious way
WINDOW_GUI_NORMAL = 16
# the ratio of the image is respected.
WINDOW_KEEPRATIO = 0
# the user can resize the window (no constraint) / also use to switch a fullscreen window to a normal size.
WINDOW_NORMAL = 0
# window with opengl support.
WINDOW_OPENGL = 4096
# window's aspect ration (can be set to WINDOW_FREERATIO or WINDOW_KEEPRATIO).
WND_PROP_ASPECT_RATIO = 2
# autosize property      (can be WINDOW_NORMAL or WINDOW_AUTOSIZE).
WND_PROP_AUTOSIZE = 1
# fullscreen property    (can be WINDOW_NORMAL or WINDOW_FULLSCREEN).
WND_PROP_FULLSCREEN = 0
# opengl support.
WND_PROP_OPENGL = 3
# property to toggle normal window being topmost or not
WND_PROP_TOPMOST = 5
# checks whether the window exists and is visible
WND_PROP_VISIBLE = 4
# enable or disable VSYNC (in OpenGL mode)
WND_PROP_VSYNC = 6


def imshow(window_name: str, image: np.ndarray) -> None:
    cv2.imshow(window_name, image)


def destroy_all_windows() -> None:
    cv2.destroyAllWindows()


def destroy_window(window_name: str) -> None:
    cv2.destroyWindow(window_name)


def named_window(window_name: str, flag: int = WINDOW_AUTOSIZE) -> None:
    cv2.namedWindow(window_name, flag)


def resize_window(window_name: str, width: int, height: int) -> None:
    cv2.resizeWindow(window_name, width, height)


def wait_key(delay: int = 0) -> int:
    return cv2.waitKey(delay)
