import numpy as np


def eq(left: np.ndarray, right: np.ndarray) -> bool:
    return (left == right).all()


def random_image(height: int, width: int, channels: int = 3) -> np.ndarray:
    image = np.random.random((height, width, channels))
    image = image * 255
    return image.astype(np.uint8, copy=False)
