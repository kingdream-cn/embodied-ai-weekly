---
title: "2026具身周刊 - 第 39 期"
date: 2026-09-21
description: "智元远征 A3 Ultra 商业落地、安努六模型产线装配、Digit 5 无界协作、TypeSafe 极速决策模型。"
tags:
  - 具身落地
  - 工业工艺
  - 人形机器人
  - Agent架构
  - 电机硬件
  - VLA
---

# 2026具身周刊 - 第 39 期

> 📅 **发布时间**：2026-09-21 &nbsp;|&nbsp; ⏱️ **预计阅读**：12 分钟 &nbsp;|&nbsp; 🏷️ **核心议题**：双臂柔性操作、人机混流安全、System One 决策、关节电机与减速器

---

## 💡 行业洞察

### 1. [商业落地] 智元远征 A3 Ultra 商业实景落地：进驻 4S 店/酒店/便利店跑通铺床、理货与服务

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">商业落地</span><span class="tag">多源参考</span><span class="tag">4 分钟</span>

**核心结论**：远征 A3 Ultra 走出实验室，在 4S 展厅、酒店与便利店跑通柔性铺床、动态递水与细粒度理货等长程作业。

</summary>

> **原文归档**：[今日头条](https://www.toutiao.com/article/7686296704445940274/?utm_source=gemini) &nbsp;|&nbsp; [微信专栏](https://mp.weixin.qq.com/s?src=11&timestamp=1789951685&ver=6979&signature=luPsj4JCR-MKIZtV3Eb69LrTae11LP0hB9VE48XLd-hic4aITlZ7dq*clvYDAQ8Bc*f9q3SDyVSsJRKgMUWjPHs*hlLSFEUdPZyfYBSljT4pR0nJXweu8tGvFM16Em31&new=1&utm_source=gemini) &nbsp;|&nbsp; **载体**：多源参考

#### 📌 核心亮点

远征 A3 Ultra 摆脱单点实验室演示，进驻 4S 展厅、酒店与便利店，依托全身协调控制完成**柔性铺床被褥平整、动态递水托举以及细粒度理货补货**等长程作业。

![智元远征 A3 Ultra 实景落地演示](/images/issue-39/zhiyuan-a3.png)

#### 📖 原文要点（据今日头条实景案例报道）

- **4S 店场景**：多台机器人协同完成迎宾、递水、车型讲解与交车服务，并承担递花、合影、放礼炮、日报生成及直播带货。
- **酒店场景**：协同完成铺床、整理客房、叠毛巾、入住办理、带路乘梯与夜间巡检。
- **便利店场景**：执行理货、巡逻、补货、大件搬运与顾客服务。
- **硬件配置**：搭载 360° 全域感知系统、UWB 与 RTK 融合定位系统，以及 **700 TOPS 算力平台**；支持自主充电与极速换电，实现 7×24 小时不间断自主值守。
- **末端能力**：配备 **20 自由度全向触觉灵巧手**，可完成递送、搬运、整理、补货，并适应弯腰、下蹲、倒退、推车、开启后备箱等复杂动作。
- **多模态交互**：支持语音、视觉、触觉与姿态四类通道，可按环境变化与任务需求实时响应。

::: tip 团队参考
体现了双臂协同向“柔性物体操作（布料）”与“长程任务规划”落地的标杆路径，适合负责末端位姿估计与实际场景泛化的同学参考。
:::

</details>

### 2. [工业工艺落地] 工业具身从“能走”转向“能干工艺”：安努智能全栈六模型打通落地，富临精工产线验证

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">工业工艺</span><span class="tag">产业特写</span><span class="tag">5 分钟</span>

**核心结论**：六模型闭环矩阵覆盖“数据—认知—训练—动作—部署”全流水线，在富临精工汽车零部件产线实机跑通高精装配工序。

</summary>

> **原文归档**：[产业特写](https://mp.weixin.qq.com/s/c8RWwl_nSpzlunxe9HgOvQ?utm_source=gemini) &nbsp;|&nbsp; **载体**：产业特写

<!-- ⚠️ 待确认：该微信链接指向的文章实为《PhyAgentOS v1.0.0 发布：为物理智能体打造可执行、可验证、可演进的 Harness》
     （全文出现 PhyAgentOS 60 次，未出现“安努 / AnuVerse / EvoHIL / ActiWorld / SimLab / Helios / 富临精工”）
     与本条“安努智能六模型”正文不匹配，因此配图暂不采用该文封面，保留主题占位图 -->

#### 📌 核心亮点

构建由 **Helios / SimLab / ActiWorld / EvoHIL / AnuVerse / Nexus** 组成的六模型闭环矩阵，全面覆盖**数据—认知—训练—动作—部署**流水线，在富临精工汽车零部件产线实机跑通高精装配工序。

![安努智能全栈六模型架构图](/images/issue-39/anu-six-models.png)

::: tip 团队参考
体现了工业具身从“基础移动搬运”向“精密工艺作业”演进的风向，做产线部署与全流程数采的同学可重点参考其模块化架构。
:::

</details>

### 3. [工业具身标杆] Agility Robotics 正式发布 Digit 5 人形机器人：破除安全防护笼与人类无界协作

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">工业具身标杆</span><span class="tag">行业特写</span><span class="tag">5 分钟</span>

**核心结论**：首发摆线针轮执行器，负载达 50 磅（+40%），充电 9 分钟作业 90 分钟；三层安全系统使其脱离防护笼与工人混流作业。

</summary>

> **原文归档**：[The Robot Report](https://www.therobotreport.com/agilitys-digit-5-humanoid-has-new-legs-batteries-safety-upgrades/?utm_source=gemini) &nbsp;|&nbsp; **载体**：行业特写

#### 📌 核心亮点

首发新型摆线针轮执行器（Cycloidal Actuators），负载能力达 **50 磅（提升 40%）**，充电 9 分钟可连续作业 90 分钟；搭载三层独立安全系统与人机感知控制器，**正式脱离工业防护隔离笼，与产线工人实现无物理屏障混流作业**。

![Agility Robotics Digit 5 实机作业](/images/issue-39/digit-5.png)

#### 📖 原文要点（据 The Robot Report 报道）

- Agility 将 Digit 5 定位为“面向规模化部署的协作安全作业”，新增腿部结构、升级电池与更完整的安全架构。
- 该机型可在**无物理屏障**的情况下紧邻人员作业，安全体系由三层独立机制叠加构成。
- 报道同期披露：公司正推进与 **Churchill Capital Corp. XI** 的 SPAC 合并，以登陆公开市场。

::: tip 团队参考
标志着工业人形机器人由“受限示范”步入“主动合规协同”时代，对团队做人机混流安全感知避障、主动急停机制及高负荷执行器选型有关键指导价值。
:::

</details>

### 4. [系统基座] TypeSafe 推出 System One 模型 Jev：专为 Agent 极速决策而生，从根源消除大模型幻觉

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">Agent 架构</span><span class="tag">架构前沿</span><span class="tag">5 分钟</span>

**核心结论**：抛弃逐 Token 生成文本，直接输出带置信度的类型化决策，比前沿 LLM 快 40–200 倍，工具调用 0% 格式错误与幻觉率。

</summary>

> **原文归档**：[架构前沿](https://mp.weixin.qq.com/s/DNr2E1OW63GO0v9dMsrvSA?utm_source=gemini) &nbsp;|&nbsp; **载体**：架构前沿

#### 📌 核心亮点

开创性提出“系统一”（System One）模型架构，彻底抛弃逐 Token 生成文本，而是直接输出带有置信度概率的类型化决策（单选、打分、是/否）。运行速度比前沿 LLM 快 40-200 倍，从数学原理上实现了工具调用的 0% 格式错误与幻觉率。

![TypeSafe Jev 模型机制图](/images/issue-39/typesafe-jev.png)

#### 📖 原文要点（据架构前沿专栏）

- 写作视角很直白：过去 AI 的默认形态是“聊天机器人”，但**软件需要的是决策，不是作文**——从一段分析文字里抠结论，既慢又容易抠错。
- Jev 由 **TypeSafe AI** 推出，该公司由前 OpenAI 研究员 **Diogo Almeida** 于 2026 年 9 月创办，主打“做一个不会聊天的 AI”：不写小作文、不解释推理，只回一个带置信度的结构化结果。
- 文章末尾还给出了在 TraeCode 中接入使用的实践指引。

::: tip 团队参考
直击当前具身大模型与 Agent 架构中“大模型推理慢”和“输出 JSON 易出错崩溃”的痛点，建议组内评估将其作为状态判别与高频工具路由的底层基座。
:::

</details>

---

## 📚 精选教程 & 学习资源

### 1. [硬件科普] 人形机器人电机技术全解析：从关节驱动到全身控制

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">硬件科普</span><span class="tag">CSDN 长文</span><span class="tag">15 分钟</span>

**核心结论**：万字长文拆解无框力矩电机原理，并横向对比谐波 / 行星 / RV 减速器在不同受力关节的选型逻辑。

</summary>

> **原文归档**：[CSDN 深度博客](https://blog.csdn.net/m0_63284825/article/details/162054649?utm_source=gemini) &nbsp;|&nbsp; **载体**：CSDN 深度博客

<!-- ⚠️ 该文为纯文字长文，页面内可用图均为 CSDN 运营位图片（i-operation.csdnimg.cn），非文章配图，
     故本条保留主题占位图；如需实拍/结构图请手动补入 motor-drive.png -->

#### 📌 核心亮点

CSDN 万字深度长文，通俗拆解了“无框力矩电机”作为机器人肌肉的工作原理，详细对比了谐波、行星与 RV 减速器在不同部位的应用逻辑。

![机器人关节驱动与减速器对比](/images/issue-39/motor-drive.png)

#### 📖 原文要点（据 CSDN 长文结构）

- **人形机器人对电机的核心需求**：高功率密度与高扭矩密度、高动态响应与带宽、高精度与高分辨率、高效率与低热耗、高可靠性与鲁棒性。
- **覆盖的主流电机类型**：无刷直流电机（BLDC）、永磁同步电机（PMSM）、伺服电机、步进电机、直线电机。
- **还包含**：关键配套技术与组件、选型考量与趋势、典型人形机器人电机配置实例。

::: tip 团队参考
搞懂为什么仿真里的策略到了真机上会被“齿轮背隙”和“电机发热”影响，了解不同电机的区别。
:::

</details>

### 2. [概念科普] 机器人的“大脑”到底是什么？一分钟看懂 LLM、VLA 与 WM 的分工

<details class="issue-item">
<summary class="issue-summary">

<span class="tag">概念科普</span><span class="tag">抖音短视频</span><span class="tag">3 分钟</span>

**核心结论**：用 3 分钟可视化讲清 LLM（逻辑常识）、VLA（小脑执行）、WM（物理先验）三者的分工协作。

</summary>

> **原文归档**：[抖音短视频](https://v.douyin.com/XX64wj1A3ZA/?utm_source=gemini) &nbsp;|&nbsp; **载体**：抖音短视频

#### 📌 核心亮点

SIC矽客机器人出品的可视化科普，直观拆解了具身智能中大语言模型（LLM，负责逻辑与常识）、视觉语言动作模型（VLA，负责小脑执行）与世界模型（WM，负责物理规律先验）的核心定义与协作关系。

![大脑 LLM / VLA / WM 分工架构图](/images/issue-39/brain-vla-wm.png)

#### 📖 原文要点（视频章节，共 5 类模型）

- **00:12 LLM**：大语言模型，擅长理解文字、回答问题、逻辑推理、生成方案，但不能直接控制机器人身体动作。
- **00:34 VLM**：视觉语言模型，能识别物体、理解场景，但主要负责理解与描述，不一定能直接让机器人动手。
- **00:59 VLA**：视觉语言动作模型，能把思考变成行动，是当前人形机器人落地最主流的模型方向。
- **01:30 WM**：世界模型，让机器人能预判物理世界的变化，增加空间与物理想象力和预判能力。
- **02:02 WAM**：世界动作模型，WM 与 VLA 的结合体，先预判世界变化、再决定如何行动，让机器人更稳更安全。
- **02:32 总结**：LLM 负责语言与思考，VLM 负责看懂环境，VLA 负责直接干活，WM 负责预判世界，WAM 负责先预判再行动。

<!-- 视频演示：抖音视频流为 blob 加密流（无公开 mp4/m3u8 直链），请手动将视频保存为
     public/videos/issue-39/brain-vla-wm.mp4 后，删除本段注释包裹即可启用播放器
<video controls width="100%" style="border-radius: 8px; margin: 12px 0;">
  <source src="/videos/issue-39/brain-vla-wm.mp4" type="video/mp4">
  您的浏览器不支持 HTML5 视频播放。
</video>
-->

::: tip 团队参考
非常适合刚接触具身大模型概念的新手快速扫盲，建立具身智能基础架构的直观宏观认知。
:::

</details>

---

## 🛠️ 开源项目 & 行业案例

> *本期暂无收录，持续追踪最新开源机械臂控制与具身数据集。*

---

## ⚙️ 工程实战 & 踩坑记录

> *本期暂无收录，欢迎团队内部提交 ROS 2 驱动与 Nav2 调优实战记录。*

---

## 📑 顶会前沿 & 论文速递

> *本期论文跟踪整合中，下一期集中呈现 CoRL / IROS 最新成果。*