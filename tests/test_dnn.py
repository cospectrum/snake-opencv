import cv2
import snake_opencv as cv


from .utils import random_image, eq


def test_blob_from_image() -> None:
    image = random_image(height=50, width=50)

    left = cv.dnn.blob_from_image(image)
    right = cv2.dnn.blobFromImage(image)
    assert eq(left, right)
