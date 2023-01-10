import pytest

import numpy as np
import snake_opencv as cv


TEST_IMAGE_FILENAME = './tests/image_test.png'


@pytest.fixture
def image_path() -> str:
    return TEST_IMAGE_FILENAME


@pytest.fixture
def test_image(image_path) -> np.ndarray:
    return cv.imread(image_path)
