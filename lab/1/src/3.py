import numpy as np


def feature_scaling(data):
    data = np.asarray(data, dtype=float)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    std_safe = np.where(std == 0, 1, std)
    standardized = (data - mean) / std_safe
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    value_range = max_val - min_val
    range_safe = np.where(value_range == 0, 1, value_range)
    min_max_scaled = (data - min_val) / range_safe
    return np.round(standardized, 4), np.round(min_max_scaled, 4)


# 主程序
if __name__ == "__main__":
    # 输入数组
    data = input()

    # 处理输入
    import ast

    data = ast.literal_eval(data)

    # 调用函数计算
    output = feature_scaling(data)

    # 输出结果
    print(output)
