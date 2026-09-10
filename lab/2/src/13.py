import numpy as np


def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    padded_input = np.pad(input_matrix, pad_width=((padding, padding), (padding, padding)), mode="constant", constant_values=0)
    input_h, input_w = padded_input.shape
    kernel_h, kernel_w = kernel.shape
    output_h = (input_h - kernel_h) // stride + 1
    output_w = (input_w - kernel_w) // stride + 1
    output_matrix = np.zeros((output_h, output_w))
    for i in range(output_h):
        for j in range(output_w):
            start_h = i * stride
            start_w = j * stride
            region = padded_input[start_h : start_h + kernel_h, start_w : start_w + kernel_w]
            output_matrix[i, j] = np.sum(region * kernel)
    return output_matrix


if __name__ == "__main__":
    input_matrix = np.array(eval(input()))
    kernel = np.array(eval(input()))
    padding = eval(input())
    stride = eval(input())
    print(simple_conv2d(input_matrix, kernel, padding, stride))
