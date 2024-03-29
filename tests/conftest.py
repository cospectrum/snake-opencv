import pytest

import numpy as np
import snake_opencv as cv


TEST_IMAGE_FILENAME = './tests/res/image_test.png'
CHESS_BOARD = './tests/res/chess_board.png'


@pytest.fixture
def image_path() -> str:
    return TEST_IMAGE_FILENAME


@pytest.fixture
def test_image(image_path) -> np.ndarray:
    image = cv.imread(image_path)
    assert image is not None
    return image


@pytest.fixture
def gray_image(image_path) -> np.ndarray:
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    assert image is not None
    return image


@pytest.fixture
def chess_board() -> np.ndarray:
    image = cv.imread(CHESS_BOARD)
    assert image is not None
    return image
