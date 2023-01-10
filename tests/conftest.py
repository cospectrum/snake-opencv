import pytest


TEST_IMAGE_FILENAME = './tests/test_image.png'


@pytest.fixture
def image_path() -> str:
    return TEST_IMAGE_FILENAME
