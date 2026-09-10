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

## PROMPT4 诊疗数据解析

### 描述

你需要根据用户输入的自然语言文本，按照定义好的规则提取信息并输出 JSON。

1. 字段定义
   1. patient_mask：取出输入里的姓名首字符，拼接 \*\*。
   2. symptoms
      根据如下关键词到不同的symptoms，输出按 ASCII 升序 排列。
      |Enum | Keywords|
      |:-|:-|
      |CHEST_PAIN|胸痛, 心口痛, 胸闷, 心绞痛|
      |DYSPNEA|呼吸困难, 喘不上气, 气短, 憋气|
      |FEVER|发烧, 发热, 高烧|
      |TRAUMA|外伤, 车祸, 流血, 骨折, 摔伤|
      |DIZZINESS|头晕, 晕眩, 昏昏沉沉|
   3. temperature
      保留 $1$ 位的小数，没有 $0.0$。如果 $>39.0$，则symptoms里要增加FEVER症状。
2. 病情等级判定
   1. 含 CHEST_PAIN 或 DYSPNEA → L1 (RULE_CRITICAL)
   2. 含 TRAUMA 或 temperature > 39.0 → L2 (RULE_URGENT)
   3. 都不是的话，返回 L3 (RULE_NORMAL)

请你根据上述信息写出对应的prompt来解决问题。

### 输入描述：

一段自然语言描述的用户输入病情。

### 输出描述：

```json
{
    "patient_mask": "string", //拼接后的姓名
    "symptoms": ["ENUM"...], //症状列表
    "temperature": float, //温度
    "triage_result": "L1/L2/L3", //分诊结果
    "trigger_rule": "RULE_..." //触犯规则
}
```

### 示例1

```txt
输入：
患者赵卫华，说自己胸闷得厉害，站起来就头晕，体温 36.8 度。
输出：
{"patient_mask":"赵**","symptoms":["CHEST_PAIN","DYSPNEA"],"temperature":36.8,"triage_result":"L1","trigger_rule":"RULE_CRITICAL"}
```

### 示例2

```txt
输入：
患者王大锤，因为昨晚喝多了感觉昏昏沉沉的，刚才量体温是39度，不过没有胸痛，也没有受外伤。
输出：
{"patient_mask":"王**","symptoms":["DIZZINESS"],"temperature":39.0,"triage_result":"L3","trigger_rule":"RULE_NORMAL"}
```

### 提示词

[4.md]

## PROMPT5 食材解析系统

### 描述

你正在为一家智能厨房管理系统开发食材解析模块。用户会通过语音或文本输入食材信息，格式非常随意（如"来点面粉"、"切好的土豆200克"、"3个鸡蛋"等）。
你需要编写一个 Prompt，将用户的自然语言输入转换为标准的 JSON 格式。
返回格式定义：
数量提取：浮点数(float)，没有提及的话默认就是`1.0`。
单位分类：包括以下几个枚举类：`WEIGHT`（重量单位）、`VOLUME`（体积单位）、`COUNT`: 个数单位、`UNKNOWN`: 无法确定单位或没有单位
食材名称：全小写
处理状态：如果包含预先处理动作（如："切好"、"去皮"等）返回true，否则返回false。

### 输入描述：

一段用户描述的食材信息。

### 输出描述：

```json
{
 "qty": float,  //数量
"unit": "ENUM", //单位
 "ingredient": "string", //食材名称
 "is_prepped": boolean //是否包含预处理
}
```

### 示例1

```txt
输入：
来点盐
输出：
{"qty": 1.0, "unit": "UNKNOWN", "ingredient": "salt", "is_prepped": false}
```

### 示例2

```txt
输入：
切好的土豆500克
输出：
{"qty": 500.0, "unit": "WEIGHT", "ingredient": "potato", "is_prepped": true}
```

### 提示词

[5.md]
