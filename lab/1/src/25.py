import numpy as np


def pca(data, k):
    data = np.array(data, dtype=float)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std
    covariance_matrix = np.cov(standardized_data, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    indices = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, indices]
    components = eigenvectors[:, :k]
    # for i in range(components.shape[1]):
    #     if np.sum(components[:, i]) < 0:
    #         components[:, i] *= -1
    return np.round(components, 4)


# 主程序
if __name__ == "__main__":
    # 输入数组
    data = input()
    k = input()

    # 处理输入
    import ast

    data = ast.literal_eval(data)
    k = int(k)

    # 调用函数计算
    output = pca(data, k)

    # 输出结果
    print(output)
