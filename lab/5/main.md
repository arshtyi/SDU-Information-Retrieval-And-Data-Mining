# 实验5 提示词题

> 题目：https://www.nowcoder.com/exam/oj?page=1&tab=AI%E6%96%B0%E9%A2%98%E5%9E%8B%E7%AF%87&topicId=408
>
> 模板：https://gwxzj3n0h7.feishu.cn/wiki/SHytw65Vgi6dhqkdSVgcUBDenig
>
> 源码：https://github.com/arshtyi/SDU-Information-Retrieval-And-Data-Mining
>
> 本文：https://tcnohkxjw4rb.feishu.cn/wiki/C0T7wDQdtiqu0DklMACcNGC1nfb

## PROMPT1 情感倾向标注

### 描述

作为一名产品运营同学，后台每天会收到成千上万条用户反馈。
由于数据量巨大，我们需要一个模型对每一条反馈进行情感倾向自动化打标。
总共分成三类：POS (Positive)、NEG (Negative)、NEU (Neutral)。
你需要编写一个Prompt，使得大模型可以处理这个问题。

### 输入描述：

一段自然语言描述的用户反馈。

### 输出描述：

```json
{
    "feeling": String //对应的情感
}
```

### 示例1

```txt
输入：
这家餐厅太好吃了，服务也很棒，下次还会来。
输出：
{"feeling": "POS"}
```

### 示例2

```txt
输入：
我的订单号是 20240501，请帮我查询一下物流状态。
输出：
{"feeling": "NEU"}
```

### 示例3

```txt
输入：
I really want to like this phone, but the battery life makes it unusable.
输出：
{"feeling": "NEG"}
```

### 提示词

[1.md]
