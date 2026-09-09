import numpy as np


def cross_validation_split(data, k, seed=42):
    np.random.seed(seed)
    np.random.shuffle(data)
    n, m = data.shape
    sub_size = int(np.ceil(n / k))
    id_s = np.arange(0, n, sub_size)
    id_e = id_s + sub_size
    if id_e[-1] > n:
        id_e[-1] = n
    return [[np.concatenate([data[: id_s[i]], data[id_e[i] :]], axis=0).tolist(), data[id_s[i] : id_e[i]].tolist()] for i in range(k)]


# 主程序
if __name__ == "__main__":
    # 输入矩阵和向量
    matrix_inputx = input()
    k = input()

    # 处理输入
    import ast

    matrix = np.array(ast.literal_eval(matrix_inputx))
    k = int(k)

    # 调用函数计算逆矩阵
    output = cross_validation_split(matrix, k)

    # 输出结果
    print(output)
