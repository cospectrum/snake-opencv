import cv2
import numpy as np

from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from .const import CAP_ANY, CAP_PROP_FPS


__all__ = [
    'VideoCapture',
    'VideoWriter',
]


class VideoCapture:
    _reader: cv2.VideoCapture

    def __init__(
        self,
        filename: Union[str, int],
        api_preference: int = CAP_ANY,
        params: Optional[List[int]] = None,
    ) -> None:
        """Opens a video file or a capturing device or an IP video stream for
        video capturing with API Preference and parameters.

        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        The params parameter allows to specify extra parameters encoded as
        pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ...).
        """
        self._reader = cv2.VideoCapture(filename, api_preference, params)

    def is_opened(self) -> bool:
        """Returns True if video capturing has been initialized already."""
        return self._reader.isOpened()

    def read(self) -> Tuple[bool, np.ndarray]:
        """Grabs, decodes and returns the next video frame."""
        return self._reader.read()

    def release(self) -> None:
        """Closes video file or capturing device."""
        self._reader.release()

    def get_backend_name(self) -> str:
        """Returns used backend API name.

        Note:
            Stream should be opened.
        """
        return self._reader.getBackendName()

    def get(self, prop_id: int) -> float:
        """Returns the specified VideoCapture property.

        Note:
            Reading / writing properties involves many layers. Some unexpected
            result might happens along this chain.
            VideoCapture -> API Backend -> Operating System -> Device Driver
            -> Device Hardware
            The returned value might be different from what really used by the
            device or it could be encoded using device dependent rules
            (eg. steps or percentage). Effective behaviour depends from device
            driver and API Backend

        Args:
            prop_id:
                Property identifier (eg. cv.CAP_PROP_POS_MSEC,
                cv.CAP_PROP_POS_FRAMES, ...) or one from Additional flags for
                video I/O API backends

        Returns:
            Value for the specified property. Value 0 is returned when
            querying a property that is not supported by the backend used by
            the VideoCapture instance.
        """
        return self._reader.get(prop_id)

    def set(self, prop_id: int, value: float) -> bool:
        """Sets a property in the VideoCapture.

        Note:
            Even if it returns True this doesn't ensure that the property
            value has been accepted by the capture device. See note in
            VideoCapture.get()

        Args:
            prop_id:
                Property identifier (eg. cv.CAP_PROP_POS_MSEC,
                cv.CAP_PROP_POS_FRAMES, ...) or one from Additional flags
                for video I/O API backends
            value: Value of the property.

        Returns:
            True if the property is supported by backend used by the
            VideoCapture instance.
        """
        return self._reader.set(prop_id, value)

    def fps(self) -> float:
        """Returns CAP_PROP_FPS property."""
        return self.get(CAP_PROP_FPS)

    def __iter__(self) -> Iterator[np.ndarray]:
        """Iterate over frames."""
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
        """Video writer class.

        Args:
            filename: Name of the output video file.
            fourcc:
                4-character code of codec used to compress the frames.
                For example, VideoWriter.fourcc(*'PIM1') is a MPEG-1 codec,
                VideoWriter.fourcc(*'MJPG') is a motion-jpeg codec etc.
                List of codes can be obtained at MSDN page or with this
                archived page of the fourcc site for a more complete list).
                FFMPEG backend with MP4 container natively uses other values
                as fourcc code: see http://mp4ra.org/#/codecs, so you may
                receive a warning message from OpenCV about fourcc code
                conversion.
            fps: Framerate of the created video stream.
            frame_size: Size (width, height) of the video frames
        """
        self._writer = cv2.VideoWriter(
            filename,
            fourcc,
            fps,
            frame_size,
        )

    def write(self, image: np.ndarray) -> None:
        """Writes the next video frame.

        The function/method writes the specified image to video file. It must
        have the same size as has been specified when opening the video writer

        Args:
            image:
                The written frame. In general, color images are expected in
                BGR format.
        """
        self._writer.write(image)

    def release(self) -> None:
        """Closes the video writer."""
        self._writer.release()

    def is_opened(self) -> bool:
        """Returns True if video writer has been successfully initialized."""
        return self._writer.isOpened()

    @staticmethod
    def fourcc(c1: str, c2: str, c3: str, c4: str) -> int:
        """Concatenates 4 chars to a fourcc code.

        This static method constructs the fourcc code of the codec to be used
        in the VideoWriter constructor.

        Returns: a fourcc code
        """
        return cv2.VideoWriter.fourcc(c1, c2, c3, c4)

    def get_backend_name(self) -> str:
        """Returns used backend API name.
        Note:
            Stream should be opened.
        """
        return self._writer.getBackendName()

    def get(self, prop_id: int) -> float:
        """Returns the specified VideoWriter property.

        Args:
            prop_id:
                Property identifier (eg. cv.VIDEOWRITER_PROP_QUALITY) or one
                of Additional flags for video I/O API backends

        Returns:
            Value for the specified property. Value 0 is returned when
            querying a property that is not supported by the backend used by
            the VideoWriter instance.
        """
        return self._writer.get(prop_id)

    def set(self, prop_id: int, value: float) -> bool:
        """Sets a property in the VideoWriter.

        Args:
            prop_id:
                Property identifier (eg. cv.VIDEOWRITER_PROP_QUALITY) or one
                of Additional flags for video I/O API backends
            value: Value of the property.

        Returns:
            True if the property is supported by the backend used by the
            VideoWriter instance.
        """
        return self._writer.set(prop_id, value)
