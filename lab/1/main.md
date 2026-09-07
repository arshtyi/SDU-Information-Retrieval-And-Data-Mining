# 实验1 机器学习

> 题目：https://www.nowcoder.com/exam/oj?page=1&tab=AI%E7%AF%87&topicId=379
>
> 模板：https://gwxzj3n0h7.feishu.cn/wiki/SHytw65Vgi6dhqkdSVgcUBDenig
>
> 源码：https://github.com/arshtyi/SDU-Information-Retrieval-And-Data-Mining
>
> 本文：https://tcnohkxjw4rb.feishu.cn/wiki/MlInwWu3di3vfVk29Y3chjkEnOk

## ML1 使用正规方程的线性回归

### 描述

编写一个使用正规方程执行线性回归的函数。
函数输入是一个矩阵 $X$（特征）和向量 $y$（目标），返回线性回归模型的系数。
最后的答案四舍五入保留小数点后四位。

### 输入描述：

第 $1$ 行输入矩阵 $X$，第 $2$ 行输入向量 $y$。

### 输出描述：

输出线性回归模型的系数。函数返回类型是列表类型，第一个是权重，第二个是偏置。

### 示例1

```markdown
输入：
[[1, 1], [1, 2], [1, 3]]
[2, 2, 3]
输出：
[1.3333, 0.5]
```

### 备注：

1. Python3对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

最小化$$L(\theta)=\sum_{i=1}^{n}(y_i - \theta^T x_i)^2=(y-X\theta)^T(y-X\theta)$$令梯度为 $0$ 得到$$X^TX\theta = X^Ty\Rightarrow \theta = (X^TX)^{-1}X^Ty$$

### 代码

```python
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    return np.round((np.linalg.inv(X.T @ X) @ X.T @ y).flatten(), 4).tolist()
if __name__ == "__main__":
    import ast
    x = np.array(ast.literal_eval(input()))
    y = np.array(ast.literal_eval(input())).reshape(-1, 1)

    # Perform linear regression
    coefficients = linear_regression_normal_equation(x, y)

    # Print the coefficients
    print(coefficients)
```

## ML2 使用梯度下降的线性回归

### 描述

编写一个使用梯度下降执行线性回归的函数。该函数应将 NumPy 数组 $X$（具有一列截距的特征）和 $y$（目标）作为输入，以及学习率 $\alpha$ 和迭代次数，并返回一个 NumPy 数组，表示线性回归模型的系数。

### 输入描述：

第 $1$ 行输入 $X$，第 $2$ 行输入 $y$，第 $3$ 行输入 $\alpha$，第 $4$ 行输入迭代次数。

### 输出描述：

输出线性回归模型的系数，四舍五入到小数点后四位。返回类型是List类型

### 示例1

```markdown
输入：
[[1, 1], [1, 2], [1, 3], [1, 4]]
[2, 3, 4, 5]
0.01
1000
输出：
[0.8678 1.045 ]
```

### 备注：

1. Python3对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

模拟即可

### 代码

```python
import numpy as np
def linear_regression_gradient_descent(X, y, alpha, iterations):
    m, n = X.shape
    theta = np.zeros((n, 1), dtype=float)
    for _ in range(iterations):
        y_pred = X @ theta
        gradient = (1 / m) * X.T @ (y_pred - y)
        theta -= alpha * gradient
    return np.round(theta.flatten(), 4).tolist()
# 主程序
if __name__ == "__main__":
    # 输入矩阵和向量
    matrix_inputx = input()
    array_y = input()
    alpha = input()
    iterations = input()

    # 处理输入
    import ast
    matrix = np.array(ast.literal_eval(matrix_inputx))
    y = np.array(ast.literal_eval(array_y)).reshape(-1,1)
    alpha = float(alpha)
    iterations = int(iterations)

    # 调用函数计算逆矩阵
    output = linear_regression_gradient_descent(matrix,y,alpha,iterations)

    # 输出结果
    print(output)
```
