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

## PROMPT2 商品信息解析系统

### 描述

我们的交易平台要上线一个新的后端服务，用于解析用户乱七八糟的商品标题。
你需要写一个 Prompt，把用户的输入转换成我们规定的 JSON 格式。

### 输入描述：

一段用户描述。

### 输出描述：

```json
{
    "storage": "string", // 如 "256GB"，单位为GB
    "is_device": boolean, // 是手机填 true，否则是false
    "warning": boolean // 信息缺失的话填 true
｝
```

### 示例1

```txt
输入：
出的红米note12tpro，五一二的内存
输出：
{"storage": "512GB", "is_device": true, "warning": false}
```

### 示例2

```txt
输入：
出一台没有保修的苹果16手机
输出：
{"storage": "", "is_device": true, "warning": true}
```

### 示例3

```txt
输入：
华为手机入耳式耳机，9成新
输出：
{"storage": "", "is_device": false, "warning": true}
```

### 提示词

[2.md]
