import time
import numpy as np
import snake_opencv as cv


def test_imshow(test_image: np.ndarray) -> None:
    window_name = 'tmp'
    result = cv.imshow(window_name, test_image)  # type: ignore
    time.sleep(2)
    assert result is None, f'{result=}'
