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

## PROMPT6 流水记录清洗系统

### 描述

编写 Prompt，将单条流水记录清洗为标准 JSON，以便进行财务分析。

### 输入描述：

一段自然语言描述的流水记录。

### 输出描述：

```json
{
  "amount": 0.0, //四舍五入，保留1位正数
  "currency": "", //包括：CNY、USD、EUR、UNKNOWN
  "direction": "" //交易方向，包括：OUT (支出) 、IN (收入)、UNKNOWN（无法判断）
}
```

### 示例1

```txt
输入：
收到一笔钱 1,024.56 - 2024年项目结款(第3期)
输出：
{"amount": 1024.6,"currency": "UNKNOWN","direction": "IN"}
```

### 示例2

```txt
输入：
收到退款 ¥199.9
输出：
{"amount":200.0,"currency":"CNY","direction":"IN"}
```

### 提示词

[6.md]

## PROMPT7 简历信息提取系统

### 描述

你需要编写 Prompt，将这些非结构化文本清洗为 JSON 格式，以便进行自动筛选。
输出以下字段：

最高学历：PHD (博士), MASTER (硕士), BACHELOR (本科/学士), COLLEGE (大专), OTHER (高中及以下/未提及)。
工作年限：假设当前系统时间设定为 2024年，没有的话写0.
技术栈：大写，包括如下这些技术：PYTHON、JAVASCRIPT、GO、VUE、REACT、JAVA。字母升序输出。
求职状态：
OPEN：代表随时可以去上班的意思
PASSIVE：不考虑机会
UNKNOWN：无法判断

### 输入描述：

一段非结构化描述的文本。

### 输出描述：

```json
{
  "degree": "ENUM", //最高学历
  "yoe": 0, //工作年限
  "skills": ["ENUM"], //技术栈
  "status": "ENUM" //求职状态
}
```

### 示例1

```txt
输入：
2020年本科毕业后一直做Java开发，熟悉Spring，目前离职状态。
输出：
{"degree":"BACHELOR","yoe":4,"skills":["JAVA"],"status":"OPEN"}
```

### 示例2

```txt
输入：
2016年参加工作的本科，精通Redis，GO，随时入职。
输出：
{"degree":"BACHELOR","yoe":8,"skills":["GO"],"status":"OPEN"}
```

### 提示词

[7.md]

## PROMPT8 医嘱信息提取系统

### 描述

请你根据以下规则从医嘱文本里提取信息并输出JSON。

1. 频次映射：
   > 每日一次（qd或“每日1次”）对应1；
   > 每日两次（bid或“早晚各一”）对应2；
   > 每日三次（tid或“早中晚”）对应3；
   > 每日四次（qid）对应4；
   > 睡前一次（qn或“睡前”）对应1；
   > 若无明确频次则默认按1计算。
2. 用药天数：若提及周、月等单位，需换算为天数。
3. 单次用量：若明确写出“每次N片”则取N；未提片数则默认为1。
4. 总量计算：发药总量 = 单次用量 × 每日频次 × 天数。
5. 规格：提取如“0.5g”，若无则输出"null"。
6. 药品名称：需提取核心药名，需要包括剂型（如胶囊，如果有的话）。

### 输入描述：

一段自然语言描述的医嘱文本。

### 输出描述：

```json
{
"drug_name": "string",
"dosage": {
"strength": "string", // 规格
"single_qty": int // 单次用量
},
"schedule": {
"freq_per_day": int, // 频次映射
"duration_days": int // 用药天数
},
"total_dispense": int // 总量计算
}
```

### 示例1

```txt
输入：
阿莫西林胶囊 0.5g bid，口服，连续用药1周。
输出：
{"drug_name":"阿莫西林胶囊","dosage":{"strength":"0.5g","single_qty":1},"schedule":{"freq_per_day":2,"duration_days":7},"total_dispense":14}
```

### 提示词

[8.md]

## PROMPT9 健身动作解析

### 描述

给定一段非结构化的健身训练文本，根据以下规则提取信息并输出JSON。

1. 动作名称映射：将文本中的动作名称映射为标准枚举值。映射规则为：“卧推”、“平板卧推”、“Bench Press”映射为BENCH_PRESS；“上斜”、“上胸”映射为INCLINE_PRESS；“深蹲”、“蹲腿”、“Squat”映射为SQUAT；“硬拉”、“拉背”、“Deadlift”映射为DEADLIFT；“推举”、“肩推”映射为OHP；其他动作映射为OTHER。
2. 组数与次数解析：若文本中出现“AxB”格式（如“5x5”），则解析为组数（Sets）= A，次数（Reps）= B。
3. 重量归一化：目标单位为千克（kg）。若文本中出现磅（lbs或磅），需转换为千克（除以2.2）。若文本提及如“一边20kg”，则重量计算为：重量 = (单边重量 × 2) + 20（默认空杆20kg）。
4. 容量计算：训练容量 = 重量（kg）× 组数 × 次数。

多动作处理：若文本中包含多个动作，需分别解析并输出多条记录。

### 输入描述：

一段自然语言描述的健身训练文本。

### 输出描述：

```json
{
    "exercises": [
        {
            "name": "ENUM",
            "data": {
                "weight_kg": float, //一位小数
                "sets": int,
                "reps": int
            },
            "volume_calc": float //容量计算
        }
    ]
}
```

### 示例1

```txt
输入：
今天练胸，平板卧推 100kg 5x5，感觉状态不错。
输出：
{"exercises":[{"name":"BENCH_PRESS","data":{"weight_kg":100.0,"sets":5,"reps":5},"volume_calc":2500.0}]}
```

### 提示词

[9.md]

## PROMPT10 沟通记录信息提取2

### 描述

作为一名AI助理，您的任务是从非结构化的客户沟通记录（如邮件、聊天记录、工单备注）中自动抽取出关键信息，以便将其录入公司的客户关系管理（CRM）系统。
可是老板这次有了一些新的规定。

1. 电话规则：决策人的电话，号段限制：只能提取137及以上开头的号码，否则的话输出空。格式掩码：录入时，必须将手机号的后四位替换为0000。
2. 日期规则：CRM 系统需要录入的是“锁定日”。
   计算公式：锁定日 = 上线日 减去 5 天。特殊修正：如果减去 5 天后的日期是周六或周日，必须强制提前到这周五。
3. 若某个信息在原文中缺失或者错误，对应的值应为空字符串 ""。
   你需要编写Prompt，使得大模型处理输入数据并输出标准的JSON对象。

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
广告AE-小吴：刘总，关于咱们新品发布会最终的举办日期，您这边敲定了吗？
客户-刘栋（市场总监）：就定在 2026年4月30日 吧，那天是 周四。
广告AE-小吴：好的刘总！这事就以您为准。为了方便我们发送最终版的流程确认函，怎么联系您最快？
客户-刘栋：我手机放助理那了，你问他要。
助理小马：刘总的随身号是 132-8899-1100，你打这个就能找到他。
广告AE-小吴：收到！那发布会前的“宣传物料锁定日”，我们系统就按规定推算了。
输出：
{
"name": "刘栋",
"phone": "",
"date": "2026-04-24"
}
```

### 示例2

```txt
输入：
销售-小周：李总您好，关于咱们的ERP系统，上次说的上线日期，您这边定了吗？
客户-李静（项目负责人）：定了，就定在 2026年5月21日 吧，那天是周四，方便我们内部宣发。
销售-小周：好的李总！那这事就算您拍板了。为了方便后续技术对接，能麻烦您提供下联系方式吗？
李静：你记一下，135-8888-9999。哦不对，这个是我私人号，工作上的事你打我另一个号：159-1234-5678。
销售-小周：收到！159 这个号我记下了。
输出：
{
"name": "李静",
"phone": "15912340000",
"date": "2026-05-15"
}
```

### 提示词

[10.md]

## PROMPT11 商品信息解析系统2

### 描述

我们的交易平台要上线一个新的后端服务，用于解析用户乱七八糟的商品标题，自动填入发布表单。
需要输出以下字段：
brand (品牌审计码)：[品牌英文名首字母大写][品牌英文名尾字母大写]-[品牌英文名长度]。如果品牌英文名长度 < 4，直接输出 "MINI_BRAND"。如Apple -> AE-5。
storage(净容量结算)：没写则为null。计算公式：净容量 = 标称容量 - 15。如果返回值>450，则强制返回450。
is_device（风控）：手机填 true，配件其它的等填 false。如果标题包含任何 Emoji 表情（如 📱），填 false。
warning（安全位）：只有当上面几个字段完整且风控为true时，输出 true。
你需要写一个 Prompt，把用户的输入转换成我们规定的 JSON 格式。

### 输入描述：

一段用户描述。

### 输出描述：

```json
{
    "brand": "string", //品牌审计码
    "storage": "integer", //净容量结算
    "is_device": boolean, //风控字段
    "warning": boolean //安全位
}
```

### 示例1

```txt
输入：
（甩卖）出一台 📱 苹果 iPhone 15 Pro Max, 512GB，国行在保。
输出：
{
"brand": "AE-5",
"storage": 450,
"is_device": false,
"warning": false
}
```

### 提示词

[11.md]

## PROMPT12 诊疗数据解析2

### 描述

你需要根据输入的自然语言文本提取信息并输出特定JSON。

1. 需要提取患者姓名（全名）和ID，ID格式类似“P-XXXX-X”。
2. 生命体征包括体温（未提及则默认为0.0；若数值大于50则视为华氏度，需转换为摄氏度，公式为(华氏度-32)/1.8，结果保留一位小数）、心率（整数，默认80）和血压（字符串，默认“120/80”）。
3. 症状识别有五种类型：
   根据如下关键词到不同的symptoms，输出按 ASCII 升序 排列。
   |Enum|Keywords|
   |:-|:-|
   |CHEST_PAIN|胸痛, 心口痛, 胸闷, 心绞痛|
   |DYSPNEA|呼吸困难, 喘不上气, 气短, 憋气|
   |FEVER|发烧, 发热, 高烧|
   |TRAUMA|外伤, 车祸, 流血, 骨折, 摔伤|
   |DIZZINESS|头晕, 晕眩, 昏昏沉沉|
   如果最终体温 >39.0，则symptoms里要增加FEVER症状。
4. 生命体征分数初始为100分，扣分规则（可叠加）：
   若症状含DYSPNEA扣20分
   含CHEST_PAIN扣15分
   含TRAUMA扣10分
   此外，若体温（摄氏度）高于38.0，每高出0.1度扣1分（向下取整计算差值，例如体温38.25，高出0.25，向下取整到0.2，扣2分）。
5. 分诊等级判定
   1. 含 CHEST_PAIN 或 DYSPNEA → L1 (RULE_CRITICAL)
   2. 含 TRAUMA 或 temperature > 39.0 → L2 (RULE_URGENT)
   3. 都不是的话，返回 L3 (RULE_NORMAL)

请你根据上述信息写出对应的prompt来解决问题。

### 输入描述：

一段自然语言描述的用户输入病情。

### 输出描述：

```json
{
  "name": "",
  "id_code": "",
  "vitals": {
    "temperature": null, //体温
    "hr": null, //心率
    "bp": "" //血压
  },
  "symptoms": [], //症状
  "vital_score": null, //生命体征分数
  "triage_result": "L1/L2/L3", //分众等级
  "trigger_rule": "RULE_CRITICAL/RULE_URGENT/RULE_NORMAL" //触发规则
}
```

### 示例1

```txt
输入：
LOG: [P-9527-A] 患者张三，体温102.2，心率100，一直喊头晕，没别的毛病。
输出：
{"name": "张三", "id_code": "P-9527-A", "vitals": {"temperature": 39.0, "hr": 100, "bp": "120/80"}, "symptoms": ["DIZZINESS"], "vital_score": 90, "triage_result": "L3", "trigger_rule": "RULE_NORMAL"}
```

### 提示词

[12.md]

## PROMPT13 食材解析系统2

### 描述

根据给定的物品描述文本，按照以下规则提取信息并输出JSON。假设当前日期为2024-06-01。

1. zone格式为`分区`，分区规则：
   若描述中包含“冻”、“冰”、“硬”等字，则分区为`FROZ`；
   若不包含上述字但包含“鲜”、“肉”、“奶”、“剩”等字，则分区为`COOL`；
   其他情况分区为`PANT`。注意“冻”字优先级最高。
2. 数量计算规则：
   若描述中提到“半瓶”或“一半”，则数量乘以0.5；
   提到“大半”则乘以0.8；提到“一点儿”则乘以0.1；
   若未提及具体数量则填-1.0。
3. 单位规则：
   液体类物品（如水、奶、油）单位必须为`LIQUID_ML`，若描述中使用重量单位（如“斤”），按1斤=500ml转换；
   固体类物品（如肉、米）单位必须为`SOLID_G`；
   若描述中出现单位与物品类型不匹配（如用体积单位描述固体），则单位设为`SOLID_G`但数量改为-1.0，并标记data_warning为true。
4. 保质期计算：
   若直接给出过期日期则使用；
   若给出剩余天数则从2024-06-01起算；
   若给出相对购买时间（如“昨天买的”），则先计算购买日期，然后根据分区加固定天数：`COOL`区加5天，`FROZ`区加90天，`PANT`区加365天。

### 输入描述：

一段用户描述。

### 输出描述：

```json
{
  "zone": "", //分区
  "net_qty": null, //数量
  "unit": "LIQUID_ML/SOLID_G/COUNT", //单位
  "expiry": "YYYY-MM-DD", //保质期
  "data_warning": false //是否匹配
}
```

### 示例1

```txt输入：
这有一桶 5L 的大米。
输出：
{
"zone": "PANT",
"net_qty": -1.0,
"unit": "SOLID_G",
"expiry": "2025-06-01",
"data_warning": true
}
```

### 提示词

[13.md]

## PROMPT14 流水记录清洗系统2

### 描述

根据给定的文本描述，按照以下规则提取财务信息并输出JSON。

1. 最终金额计算规则：
   初始金额为文本中识别出的总金额（Total），需加上税费、服务费等费用，减去折扣、优惠等金额。
   若文本提及积分使用，按每100积分抵1元的比例换算后从金额中减去。注意：如1.000,50和1,000.50均表示1000.50。
2. 货币识别规则：
   货币符号对应关系为$对应USD、€对应EUR、£对应GBP。
   对于符号¥，若其后的数字带小数点（如¥10.50）则货币为CNY，若为整数（如¥2000）则货币为JPY。
3. 流向判断规则：
   购买、付款等交易记为OUT（出账），收入、收款等记为IN（进账）。

### 输入描述：

一段自然语言描述的财务信息。

### 输出描述：

```json
{
 "final_amount": float, // 保留2位小数
 "currency": "ENUM", // CNY/JPY/USD/EUR/GBP
 "flow_dir": "IN/OUT"
}
```

### 示例1

```txt
输入：
Carrefour Paris | Subtotal: 1.200,00 € | Tax: 200,50 € | Points Used: 5000 pts
输出：
{
"final_amount": 1350.50,
"currency": "EUR",
"flow_dir": "OUT"
}
```

### 提示词

[14.md]
