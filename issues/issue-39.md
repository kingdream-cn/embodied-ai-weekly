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

> **原文归档**：[今日头条](https://www.toutiao.com/article/7686296704445940274/?utm_source=gemini) &nbsp;|&nbsp; [微信专栏](https://mp.weixin.qq.com/s?src=11&timestamp=1789951685&ver=6979&signature=luPsj4JCR-MKIZtV3Eb69LrTae11LP0hB9VE48XLd-hic4aITlZ7dq*clvYDAQ8Bc*f9q3SDyVSsJRKgMUWjPHs*hlLSFEUdPZyfYBSljT4pR0nJXweu8tGvFM16Em31&new=1&utm_source=gemini) &nbsp;|&nbsp; **载体**：多源参考 · 4分钟精读

#### 📌 核心亮点

远征 A3 Ultra 摆脱单点实验室演示，进驻 4S 展厅、酒店与便利店，依托全身协调控制完成**柔性铺床被褥平整、动态递水托举以及细粒度理货补货**等长程作业。

![智元远征 A3 Ultra 实景落地演示](/images/issue-39/zhiyuan-a3.png)

::: tip 团队参考
体现了双臂协同向“柔性物体操作（布料）”与“长程任务规划”落地的标杆路径，适合负责末端位姿估计与实际场景泛化的同学参考。
:::

---

### 2. [工业工艺落地] 工业具身从“能走”转向“能干工艺”：安努智能全栈六模型打通落地，富临精工产线验证

> **原文归档**：[产业特写](https://mp.weixin.qq.com/s/c8RWwl_nSpzlunxe9HgOvQ?utm_source=gemini) &nbsp;|&nbsp; **载体**：产业特写 · 5分钟精读

#### 📌 核心亮点

构建由 **Helios / SimLab / ActiWorld / EvoHIL / AnuVerse / Nexus** 组成的六模型闭环矩阵，全面覆盖**数据—认知—训练—动作—部署**流水线，在富临精工汽车零部件产线实机跑通高精装配工序。

![安努智能全栈六模型架构图](/images/issue-39/anu-six-models.png)

::: tip 团队参考
体现了工业具身从“基础移动搬运”向“精密工艺作业”演进的风向，做产线部署与全流程数采的同学可重点参考其模块化架构。
:::

---

### 3. [工业具身标杆] Agility Robotics 正式发布 Digit 5 人形机器人：破除安全防护笼与人类无界协作

> **原文归档**：[The Robot Report](https://www.therobotreport.com/agilitys-digit-5-humanoid-has-new-legs-batteries-safety-upgrades/?utm_source=gemini) &nbsp;|&nbsp; **载体**：行业特写 · 5分钟精读

#### 📌 核心亮点

首发新型摆线针轮执行器（Cycloidal Actuators），负载能力达 **50 磅（提升 40%）**，充电 9 分钟可连续作业 90 分钟；搭载三层独立安全系统与人机感知控制器，**正式脱离工业防护隔离笼，与产线工人实现无物理屏障混流作业**。

![Digit 5 人形机器人作业演示](/images/issue-39/digit-5.png)

::: tip 团队参考
标志着工业人形机器人由“受限示范”步入“主动合规协同”时代，对团队做人机混流安全感知避障、主动急停机制及高负荷执行器选型有关键指导价值。
:::

---

### 4. [系统基座] TypeSafe 推出 System One 模型 Jev：专为 Agent 极速决策而生，从根源消除大模型幻觉

> **原文归档**：[架构前沿](https://mp.weixin.qq.com/s/DNr2E1OW63GO0v9dMsrvSA?utm_source=gemini) &nbsp;|&nbsp; **载体**：架构前沿 · 5分钟精读

#### 📌 核心亮点

开创性提出“系统一”（System One）模型架构，彻底抛弃逐 Token 生成文本，而是直接输出带有置信度概率的类型化决策（单选、打分、是/否）。运行速度比前沿 LLM 快 40-200 倍，从数学原理上实现了工具调用的 0% 格式错误与幻觉率。

![TypeSafe Jev 模型机制图](/images/issue-39/typesafe-jev.png)

::: tip 团队参考
直击当前具身大模型与 Agent 架构中“大模型推理慢”和“输出 JSON 易出错崩溃”的痛点，建议组内评估将其作为状态判别与高频工具路由的底层基座。
:::

---

## 📚 精选教程 & 学习资源

### 1. [硬件科普] 人形机器人电机技术全解析：从关节驱动到全身控制

> **原文归档**：[CSDN 深度博客](https://blog.csdn.net/m0_63284825/article/details/162054649?utm_source=gemini) &nbsp;|&nbsp; **载体**：CSDN 深度博客 · 15分钟精读

#### 📌 核心亮点

CSDN 万字深度长文，通俗拆解了“无框力矩电机”作为机器人肌肉的工作原理，详细对比了谐波、行星与 RV 减速器在不同部位的应用逻辑。

![电机技术与减速器对比](/images/issue-39/motor-drive.png)

::: tip 团队参考
搞懂为什么仿真里的策略到了真机上会被“齿轮背隙”和“电机发热”影响，了解不同电机的区别。
:::

---

### 2. [概念科普] 机器人的“大脑”到底是什么？一分钟看懂 LLM、VLA 与 WM 的分工

> **原文归档**：[抖音短视频](https://v.douyin.com/XX64wj1A3ZA/?utm_source=gemini) &nbsp;|&nbsp; **载体**：抖音短视频 · 3分钟速览

#### 📌 核心亮点

SIC矽客机器人出品的可视化科普，直观拆解了具身智能中大语言模型（LLM，负责逻辑与常识）、视觉语言动作模型（VLA，负责小脑执行）与世界模型（WM，负责物理规律先验）的核心定义与协作关系。

![大脑 LLM / VLA / WM 分工架构图](/images/issue-39/brain-vla-wm.png)

::: tip 团队参考
非常适合刚接触具身大模型概念的新手快速扫盲，建立具身智能基础架构的直观宏观认知。
:::

---

## 🛠️ 开源项目 & 行业案例

> *本期暂无收录，持续追踪最新开源机械臂控制与具身数据集。*

---

## ⚙️ 工程实战 & 踩坑记录

> *本期暂无收录，欢迎团队内部提交 ROS 2 驱动与 Nav2 调优实战记录。*

---

## 📑 顶会前沿 & 论文速递

> *本期论文跟踪整合中，下一期集中呈现 CoRL / IROS 最新成果。*