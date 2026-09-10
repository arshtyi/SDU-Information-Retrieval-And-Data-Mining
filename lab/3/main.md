# 实验3 自然语言处理 & 计算机视觉

> 题目：https://www.nowcoder.com/exam/oj?page=1&tab=AI%E7%AF%87&topicId=381
>
> 模板：https://gwxzj3n0h7.feishu.cn/wiki/SHytw65Vgi6dhqkdSVgcUBDenig
>
> 源码：https://github.com/arshtyi/SDU-Information-Retrieval-And-Data-Mining
>
> 本文：https://tcnohkxjw4rb.feishu.cn/wiki/A07RwmyYFigpzIkYbkHcwIGYnYc

## NLP287624 最优字符串对齐距离

### 描述

实现最优字符串对齐（Optimal String Alignment，OSA）距离的计算。OSA距离是衡量两个字符串相似度的指标，表示将一个字符串转换为另一个字符串所需的最小编辑操作次数。

允许的编辑操作（每个操作代价为1）：

1. 插入一个字符
2. 删除一个字符
3. 替换一个字符
4. 交换相邻的两个字符

### 输入描述：

第一行输入源字符串。
第二行输入目标字符串。

### 输出描述：

返回一个整数，表示从源字符串转换到目标字符串所需的最小操作次数。

### 示例1

```txt
输入：
"caper"
"acer"
输出：
2
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

### 代码

[1.py]
