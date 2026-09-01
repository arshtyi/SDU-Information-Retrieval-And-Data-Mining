# 实验1 机器学习

> 题目：https://www.nowcoder.com/exam/oj?page=1&tab=AI%E7%AF%87&topicId=379
>
> 模板：https://gwxzj3n0h7.feishu.cn/wiki/SHytw65Vgi6dhqkdSVgcUBDenig
>
> 源码：https://github.com/arshtyi/SDU-Information-Retrieval-And-Data-Mining/blob/main/lab/1/main.md
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
输入：[[1, 1], [1, 2], [1, 3]]
[2, 2, 3]
输出：[1.3333, 0.5]
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
