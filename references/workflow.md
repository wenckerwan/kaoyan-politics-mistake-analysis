# 执行流程

## A. 接收任务

先建立本批任务卡：

```yaml
candidate_id: <候选人代号>
relationship: <本人/朋友/其他>
module: <马原/毛中特/习思想/史纲/思法>
source_type: <720/肖1000/真题/模拟题/混合>
input_files:
  - <path>
upstream_sources:
  - <教材或笔记>
  - <题库与解析>
  - <真题索引或真题卷>
  - <时政资料>
```

如果 `candidate_id` 或 `relationship` 不明确，先确认，不猜。

## B. 解析导出件

Markdown 优先。PDF 或图片作为补充。

题目级记录建议包含：

```yaml
export_number: <导出件题号>
question_type: <single/multiple>
stem: <题干>
options: <选项>
my_answer: <我的答案或空>
correct_answer: <正确答案>
explanation: <解析>
knowledge_point: <考点>
notes: <刷题笔记和真题思维点拨>
status: <include/exclude/pending>
```

## C. 纳入规则

```text
答案集合相等？
├─ 是 → 剔除，记录为混入的做对题
└─ 否 → 纳入错题

我的答案为空？
├─ 用户已声明“导出时删除了错选项”或来源明确为错题本 → 纳入错题
└─ 否 → 待确认，不进入最终统计
```

多选题先把选项转成集合，再比较；不要按字符串顺序比较。

## D. 题库核对

用题干长前缀、关键词、选项结构和解析交叉匹配。

不要使用：

- 导出件题号直接映射
- 只凭章节内序号映射
- 只凭一个模糊关键词映射

每个最终纳入题至少保存：

```text
导出题号 → 题库真实题号 → 题型 → 正确答案 → 匹配依据
```

## E. 错因聚类

建议先按以下候选标签扫描，再根据材料合并：

- concept-confusion：概念混淆
- relation-direction：关系方向错误
- qualifier-upgrade：限定词升级
- stage-time-confusion：阶段和时间错位
- multiple-choice-under-screening：多选未逐项筛选
- correct-but-not-responsive：选项本身正确但不回应题干
- calculation-template：政经计算模板错误
- source-memory-gap：教材原文或固定表述缺失

最后每章保留 3—5 个最能解释错题的标签，不要制造过多分类。

## F. 真题回归

优先找与个人错题同一知识点、同一关系词、同一错误选项结构的真题。

每条真题说明三点：

1. 真题在问什么
2. 个人错题与它哪里相同
3. 下一次用什么动作识别

## G. 写作和交付

先写提分手册，再写回访清单，最后更新索引或批次明细。

如果批次中有待核题目：

- 主报告明确标注待核
- 不把待核题计入确定统计，除非用户明确指定
- 不要用推测答案生成个人错因
