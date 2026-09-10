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

## PROMPT3 沟通记录信息提取

### 描述

作为一名AI助理，您的任务是从非结构化的客户沟通记录（如邮件、聊天记录、工单备注）中自动抽取出关键信息，以便将其录入公司的客户关系管理（CRM）系统。
你需要编写Prompt，使得大模型可以精准处理输入数据并输出标准的JSON对象。
若某个信息在原文中缺失或者错误，对应的值应为空字符串 ""，phone字段内容为标准的 $11$ 位手机号。

### 输入描述：

一段自然语言描述的客户沟通记录。

### 输出描述：

```json
{
  "name": "",
  "phone": "",
  "date": ""
}
```

### 示例1

```txt
输入：
客户名叫赵铁柱，原本登记的号码是 13722228888……哎不对，这个号已经注销了。那先记这个备用的：15966667777。预约本来是安排在今天的，结果他那边临时有变动，需要把时间往前提两天（设定当前参考日期为 2023年8月15日）。
输出：
{"name": "赵铁柱", "phone": "15966667777", "date": "2023-08-13"}
```

### 示例2

```txt
输入：
那个预约的时间咱们确认一下，原本是打算定在下个月初 5 号的，结果刚查了下行程那天走不开，必须得往后延个三天。对了，今天是 2025 年 11 月。客户名字叫李小龙。电话先记这个 13611112222……哎不对，他刚发消息说那手机欠费停机了，要把中间这四位 1111换成 6666 才是对的。
输出：
{"name": "李小龙", "phone": "13666662222", "date": "2025-12-08"}
```

### 提示词

[3.md]
