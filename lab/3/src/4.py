import numpy as np


def calculate_contrast(img) -> int:
    """
    Calculate the contrast of a grayscale image.
    Args:
            img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
    """
    return np.max(img) - np.min(img)


if __name__ == "__main__":
    img = np.array(eval(input()))
    print(calculate_contrast(img))
