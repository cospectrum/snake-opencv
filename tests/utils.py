import numpy as np


def eq(left: np.ndarray, right: np.ndarray) -> bool:
    return (left == right).all()
