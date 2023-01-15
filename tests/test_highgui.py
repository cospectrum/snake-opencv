import numpy as np
import snake_opencv as cv


def test_imshow(test_image: np.ndarray) -> None:
    window_name = 'tmp'
    cv.imshow(window_name, test_image)
    ms = 1000
    code = cv.wait_key(ms)
    assert isinstance(code, int)
    cv.destroy_window(window_name)


def test_named_window(test_image: np.ndarray) -> None:
    window_name = 'named_window'
    cv.named_window(window_name, cv.WINDOW_NORMAL)
    cv.resize_window(window_name, height=300, width=500)
    cv.imshow(window_name, test_image)
    cv.wait_key(1000)
