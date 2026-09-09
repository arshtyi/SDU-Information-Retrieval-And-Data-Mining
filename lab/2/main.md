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

### 代码

[2.py]
