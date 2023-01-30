import cv2
import numpy as np

from .const import WINDOW_AUTOSIZE


__all__ = [
    'destroy_all_windows',
    'destroy_window',
    'named_window',
    'imshow',
    'resize_window',
    'wait_key',
]


def imshow(window_name: str, image: np.ndarray) -> None:
    """Displays an image in the specified window.

    The function imshow displays an image in the specified window. If the
    window was created with the cv.WINDOW_AUTOSIZE flag, the image is shown
    with its original size, however it is still limited by the screen
    resolution. Otherwise, the image is scaled to fit the window. The function
    may scale the image, depending on its depth:
        If the image is 8-bit unsigned, it is displayed as is.

        If the image is 16-bit unsigned, the pixels are divided by 256. That
        is, the value range [0, 255*256] is mapped to [0, 255].

        If the image is 32-bit or 64-bit floating-point, the pixel values are
        multiplied by 255. That is, the value range [0, 1] is mapped to
        [0, 255].

        32-bit integer images are not processed anymore due to ambiguouty of
        required transform. Convert to 8-bit unsigned matrix using a custom
        preprocessing specific to image’s context.

    If the window was not created before this function, it is assumed creating
    a window with cv.WINDOW_AUTOSIZE.

    If you need to show an image that is bigger than the screen resolution,
    you will need to call named_window(“”, WINDOW_NORMAL) before the imshow.

    Note: This function should be followed by a call to cv.wait_key to perform
    GUI housekeeping tasks that are necessary to actually show the given image
    and make the window respond to mouse and keyboard events. Otherwise, it
    won’t display the image and the window might lock up. For example,
    wait_key(0) will display the window infinitely until any keypress (it is
    suitable for image display). wait_key(25) will display a frame and wait
    approximately 25 ms for a key press (suitable for displaying a video
    frame-by-frame). To remove the window, use cv.destroy_window.

    Args:
        window_name: Name of the window.
        image: Image to be shown.
    """
    cv2.imshow(window_name, image)


def destroy_all_windows() -> None:
    """Destroys all of the HighGUI windows.

    The function destroy_all_windows destroys all of the opened HighGUI
    windows.
    """
    cv2.destroyAllWindows()


def destroy_window(window_name: str) -> None:
    """Destroys the specified window.

    The function destroy_window destroys the window with the given name.

    Args:
        window_name: Name of the window to be destroyed.
    """
    cv2.destroyWindow(window_name)


def named_window(window_name: str, flag: int = WINDOW_AUTOSIZE) -> None:
    """Creates a window.

    The function named_window creates a window that can be used as a
    placeholder for images and trackbars. Created windows are referred to by
    their names.

    If a window with the same name already exists, the function does nothing.

    You can call cv.destroy_window or cv.destroy_all_windows to close the
    window and de-allocate any associated memory usage. For a simple program,
    you do not really have to call these functions because all the resources
    and windows of the application are closed automatically by the operating
    system upon exit.

    Args:
        window_name:
            Name of the window in the window caption that may be used as a
            window identifier.
        flag: Flag of the window.
    """
    cv2.namedWindow(window_name, flag)


def resize_window(window_name: str, width: int, height: int) -> None:
    """Resizes the window to the specified size

    Note:
        The specified window size is for the image area. Toolbars are not
        counted.
        Only windows created without cv.WINDOW_AUTOSIZE flag can be resized.

    Args:
        window_name: Window name.
        width: The new window width.
        height: The new window height.
    """
    cv2.resizeWindow(window_name, width, height)


def wait_key(delay: int = 0) -> int:
    """Waits for a pressed key.

    The function wait_key waits for a key event infinitely (when inline
    formula) or for delay milliseconds, when it is positive. Since the OS has
    a minimum time between switching threads, the function will not wait
    exactly delay ms, it will wait at least delay ms, depending on what else
    is running on your computer at that time. It returns the code of the
    pressed key or -1 if no key was pressed before the specified time had
    elapsed.

    Note: The function only works if there is at least one HighGUI window
    created and the window is active. If there are several HighGUI windows,
    any of them can be active.

    Args:
        delay:
            Delay in milliseconds. 0 is the special value that means “forever”
    """
    return cv2.waitKey(delay)
