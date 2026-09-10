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

## NLP287602 实现TF-IDF

### 描述

实现一个函数来计算TF-IDF（词频-逆文档频率）分数。TF-IDF是一种用于信息检索和文本挖掘的常用加权技术，用于评估一个词对于文档集中的某个文档的重要程度。

### 输入描述：

函数接收两个参数：

1. corpus：文档集合，是一个二维列表，每个元素是一个文档（词语列表）
2. query：查询词列表，需要计算这些词的TF-IDF分数

### 输出描述：

返回一个二维列表，表示每个查询词在每个文档中的TF-IDF分数：

- 行数等于文档数
- 列数等于查询词数
- 结果保留 $5$ 位小数
- 按照文档顺序和查询词顺序排列

### 示例1

```txt
输入：
[["hello", "world"], ["hello", "python"]]
["hello", "python"]
输出：
[[0.5, 0.0], [0.5, 0.70273]]
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

### 代码

[2.py]

## NLP287418 实现一个简化版的 GPT-2 风格文本生成函数

### 描述

你的任务是用 Python 实现一个简化版的 GPT-2 风格文本生成函数。该函数将包含以下最小 GPT-2 架构的组件：

词嵌入：将输入的词元映射到稠密的向量表示。
位置嵌入：为词嵌入添加位置信息。
多头注意力：关注序列的不同部分。
前馈网络：通过稠密层处理注意力输出。
层归一化：稳定训练过程。
该函数必须接受以下参数：

prompt：引导生成过程的初始文本。
生成的词数量：指定要输出多少个词。
你的函数应输出生成的文本。
实现时需要注意以下细节：
激活函数使用GELU： `GELU(x) = 0.5 *x * (1 + tanh(√(2/π) * (x + 0.044715x^3)))`
词嵌入使用固定位置，由随机wpe给出
多头注意力中，mask采用下三角矩阵： `(1 - np.tri(x.shape[0], dtype=x.dtype)) * -1e10 `； 并且分数计算需要除以 `sqrt(d_k)`进行缩放
Transformer Block 的顺序是
输入先经过多头注意力层，再加残差。
接着经过前馈网络，再加残差。
每一步都有对应的层归一化
输出词选择最大概率的输出
此外，利用辅助函数 load_encoder_hparams_and_params 来检索：

一个虚拟编码器。
模型超参数。
模型参数。

### 输入描述：

第一行输入prompt，第二行输入生成的词数量。

### 输出描述：

输出生成的文本

### 示例1

```txt
输入：
hello
6
输出：
hello hello hello <UNK> <UNK> <UNK>
```

### 备注：

1. 对应的输入、输出已给出，您只用实现核心功能函数即可。
2. 支持numpy、scipy、pandas、scikit-learn库。

### 分析

### 代码

[3.py]
