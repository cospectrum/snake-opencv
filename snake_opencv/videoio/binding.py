import cv2
import numpy as np

from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from .const import CAP_ANY


__all__ = [
    'VideoCapture',
    'VideoWriter',
]


class VideoCapture:
    _video: cv2.VideoCapture

    def __init__(
        self,
        filename: Union[str, int],
        api_preference: int = CAP_ANY,
        params: Optional[List[int]] = None,
    ) -> None:
        self._video = cv2.VideoCapture(filename, api_preference, params)

    def is_opened(self) -> bool:
        return self._video.isOpened()

    def read(self) -> Tuple[bool, np.ndarray]:
        return self._video.read()

    def release(self) -> None:
        self._video.release()

    def get_backend_name(self) -> str:
        return self._video.getBackendName()

    def get(self, prop_id: int) -> float:
        return self._video.get(prop_id)

    def set(self, prop_id: int, value: float) -> bool:
        return self._video.set(prop_id, value)

    def __iter__(self) -> Iterator[np.ndarray]:
        while self.is_opened():
            status, frame = self.read()
            if status is False:
                break
            yield frame

        self.release()


Width = int
Height = int


class VideoWriter:
    _writer: cv2.VideoWriter

    def __init__(
        self,
        filename: str,
        fourcc: int,
        fps: float,
        frame_size: Tuple[Width, Height],
    ) -> None:
        self._writer = cv2.VideoWriter(
            filename,
            fourcc,
            fps,
            frame_size,
        )

    def write(self, image: np.ndarray) -> None:
        self._writer.write(image)

    def release(self) -> None:
        self._writer.release()

    def is_opened(self) -> bool:
        return self._writer.isOpened()

    @staticmethod
    def fourcc(c1: str, c2: str, c3: str, c4: str) -> int:
        return cv2.VideoWriter.fourcc(c1, c2, c3, c4)

    def get_backend_name(self) -> str:
        return self._writer.getBackendName()

    def get(self, prop_id: int) -> float:
        return self._writer.get(prop_id)

    def set(self, prop_id: int, value: float) -> bool:
        return self._writer.set(prop_id, value)
