import numpy as np


def calculate_loss(real_values, predicted_values, delta):
    error = real_values - predicted_values
    mse = np.mean(error**2)
    mae = np.mean(np.abs(error))
    abs_error = np.abs(error)
    huber_loss = np.where(abs_error <= delta, 0.5 * error**2, delta * (abs_error - 0.5 * delta))
    dot_product = np.dot(real_values, predicted_values)
    norm_real = np.linalg.norm(real_values)
    norm_predicted = np.linalg.norm(predicted_values)
    if norm_real == 0 or norm_predicted == 0:
        cosine_loss = 1.0
    else:
        cosine_similarity = dot_product / (norm_real * norm_predicted)
        cosine_loss = 1 - cosine_similarity
    return round(mse, 6), round(mae, 6), round(np.mean(huber_loss), 6), round(cosine_loss, 6)


# 从标准输入读取数据
n = int(input())
real_values = []
predicted_values = []

for _ in range(n):
    real, predicted = map(float, input().split())
    real_values.append(real)
    predicted_values.append(predicted)

delta = float(input())  # 读取阈值

# 调用计算损失函数的函数
results = calculate_loss(np.array(real_values), np.array(predicted_values), delta)
# 输出结果
for value in results:
    print(f"{value:.6f}")
