import cv2
import snake_opencv as cv


from .utils import random_image, eq


def test_fast_nl_means_denoising_colored() -> None:
    image = random_image(height=70, width=60)

    left = cv.fast_nl_means_denoising_colored(image)
    right = cv2.fastNlMeansDenoisingColored(image)
    assert eq(left, right)
