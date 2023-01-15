import snake_opencv as cv
import numpy as np


def test_video_capture() -> None:
    cap = cv.VideoCapture(0)
    back_name = cap.get_backend_name()
    assert isinstance(back_name, str)

    fps = cap.get(cv.CAP_PROP_FPS)
    assert isinstance(fps, float)

    is_opened = cap.is_opened()
    assert isinstance(is_opened, bool)
    assert is_opened is True

    status, frame = cap.read()
    assert status is True
    assert isinstance(frame, np.ndarray)
    cap.release()
