import cv2
import snake_opencv as cv


from .utils import random_image, eq


def test_blob_from_image() -> None:
    image = random_image(height=50, width=50)

    left = cv.dnn.blob_from_image(image)
    right = cv2.dnn.blobFromImage(image)
    assert eq(left, right)


def test_blob_from_images() -> None:
    images = [
        random_image(height=45, width=45)
        for _ in range(3)
    ]
    left = cv.dnn.blob_from_images(images)
    right = cv2.dnn.blobFromImages(images)
    assert eq(left, right)
