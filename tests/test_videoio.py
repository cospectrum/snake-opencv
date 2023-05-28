import random
import snake_opencv as cv
import numpy as np

from .utils import random_image


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


def test_video_writer() -> None:
    h = random.randint(1, 2000)
    w = random.randint(1, 2000)

    writer = cv.VideoWriter(
        filename='./video_tmp.avi',
        fourcc=cv.VideoWriter.fourcc(*'MJPG'),
        fps=10,
        frame_size=(w, h),
    )

    for _ in range(20):
        image = random_image(height=h, width=w)
        writer.write(image)
