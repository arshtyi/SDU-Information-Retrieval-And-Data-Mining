# 实验2 深度学习

> 题目：https://www.nowcoder.com/exam/oj?page=1&tab=AI%E7%AF%87&topicId=380
>
> 模板：https://gwxzj3n0h7.feishu.cn/wiki/SHytw65Vgi6dhqkdSVgcUBDenig
>
> 源码：https://github.com/arshtyi/SDU-Information-Retrieval-And-Data-Mining
>
> 本文：https://tcnohkxjw4rb.feishu.cn/wiki/IQCOwkhzEiivjIkPcHvcoQaUnLf

## DL1 Sigmoid 激活函数实现

### 描述

实现sigmoid激活函数，这是神经网络中最常用的激活函数之一。Sigmoid函数将任意实数映射到 $(0,1)$ 区间，常用于神经网络的二分类问题。

### 输入描述：

一个浮点数 $z$，表示需要计算sigmoid值的输入。

### 输出描述：

返回一个浮点数，表示sigmoid函数的计算结果，结果保留 $4$ 位小数。

### 示例1

```txt
输入：
0.0
输出：
0.5000
```

### 分析

$$\sigma(z)=\frac{1}{1+\mathrm{e}^{-z}}$$

### 代码

[1.py]

## DL2 softmax激活函数实现

### 描述

实现softmax激活函数，该函数将一组数值转换为概率分布。Softmax函数常用于神经网络的多分类问题中，它将任意实数值转换为 $(0,1)$ 区间内的实数，并且转换后所有值的和为 $1$。

### 输入描述：

输入一个浮点数列表，表示需要进行softmax转换的原始分数

### 输出描述：

返回一个浮点数列表，表示softmax转换后的概率分布。结果保留四位小数。

### 示例1

```txt
输入：
[2.0, 2.0, 3.0]
输出：
[0.2119, 0.2119, 0.5761]
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

$$softmax(x)=\frac{\mathrm{e}^x}{\sum\mathrm{e}^x}$$

### 代码

[2.py]

## DL3 单神经元

### 描述

实现一个单神经元的前向传播函数，使用sigmoid激活函数进行二分类预测。这是深度学习中最基本的神经网络单元。

$$mse=\frac{1}{n}\sum_{i=1}^n(predictions_i-label_i)^2$$

### 输入描述：

函数接收 $4$ 个参数：

1. features：二维列表，每行是一个样本的特征向量
2. labels：一维列表，包含对应的二分类标签（$0$ 或 $1$）
3. weights：一维列表，权重向量
4. bias：浮点数，偏置值

### 输出描述：

返回一个元组，包含两个元素：

1. 预测概率列表：每个样本通过sigmoid函数后的预测概率（保留 $4$ 位小数）
2. MSE值：预测概率与真实标签之间的均方误差（保留 $4$ 位小数）

### 示例1

```txt
输入：
[[1, 2], [2, 3]]
[0, 1]
[0.5, 0.5]
0.0
输出：
([0.8176, 0.9241], 0.3371)
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

先计算线性组合，再经过 Sigmoid，最后计算 MSE

### 代码

[3.py]

## DL4 Log Softmax函数的实现

### 描述

实现log-softmax函数。log-softmax是softmax函数的对数形式，在深度学习中常用于提高数值计算的稳定性。
需要在运算之前减去最大值保证数值稳定性。

### 输入描述：

输入一个列表，列表中的元素为浮点数。

### 输出描述：

输出一个numpy数组，代表log-softmax的结果。

### 示例1

```txt
输入：
[1.0, 2.0, 3.0]
输出：
[-2.40760596 -1.40760596 -0.40760596]
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

$$log\_softmax(x_i)=x_i-\max(x)-\log\sum_j\mathrm{e}^{x_j-\max(x)}$$

### 代码

[4.py]

## DL5 实现ReLU激活函数

### 描述

实现ReLU（Rectified Linear Unit，线性整流单元）激活函数。ReLU是深度学习中最常用的激活函数之一，它对正数保持不变，对负数则输出零。

### 输入描述：

第一行输入一个浮点数，表示输入值。

### 输出描述：

返回一个浮点数，表示经过ReLU激活函数处理后的结果。

### 示例1

```txt
输入：
2.5
输出：
2.5
```

### 分析

$$ReLU(x)=max(x,0)$$

### 代码

[5.py]

## DL6 Leaky ReLU 激活函数

### 描述

实现Leaky ReLU（带泄漏的线性整流单元）激活函数。Leaky ReLU是ReLU的一个变体，它在输入为负时，不会完全将输出置为零，而是保留一个很小的斜率。

### 输入描述：

第一行输入输入值，第二行输入负数部分的斜率。

### 输出描述：

返回一个数值，表示经过Leaky ReLU激活函数处理后的结果。

### 示例1

```txt
输入：
2.0
0.01
输出：
2.0
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

$$leaky_relu(x)=\max(\alpha x,x)$$

### 代码

[6.py]
