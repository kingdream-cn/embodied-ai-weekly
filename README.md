<div align="center">

# 🤖 具身智能周刊

**Embodied AI Weekly** — 人形机器人 · 灵巧操作 · 世界模型 · 自主导航

每周精选具身智能领域的前沿论文、开源项目、工程实践与行业动态，
以「核心亮点 + 团队参考」的工程视角解读，帮团队快速锁定值得跟进的信息。

[![Deploy](https://img.shields.io/github/actions/workflow/status/kingdream-cn/embodied-ai-weekly/deploy.yml?style=flat-square&label=Deploy&logo=githubactions&logoColor=white)](https://github.com/kingdream-cn/embodied-ai-weekly/actions/workflows/deploy.yml)
[![Website](https://img.shields.io/website?style=flat-square&url=https%3A%2F%2Fkingdream-cn.github.io%2Fembodied-ai-weekly%2F&up_message=online&down_message=offline&label=Website)](https://kingdream-cn.github.io/embodied-ai-weekly/)
[![VitePress](https://img.shields.io/github/package-json/dependency-version/kingdream-cn/embodied-ai-weekly/dev/vitepress?style=flat-square&label=VitePress&color=646CFF&logo=vite&logoColor=white)](https://vitepress.dev/)
[![Node](https://img.shields.io/badge/Node.js-%3E%3D%2020-339933?style=flat-square&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Last Commit](https://img.shields.io/github/last-commit/kingdream-cn/embodied-ai-weekly?style=flat-square&label=Last%20Commit)](https://github.com/kingdream-cn/embodied-ai-weekly/commits/main)
[![Stars](https://img.shields.io/github/stars/kingdream-cn/embodied-ai-weekly?style=social)](https://github.com/kingdream-cn/embodied-ai-weekly/stargazers)

🌐 **在线阅读：[kingdream-cn.github.io/embodied-ai-weekly](https://kingdream-cn.github.io/embodied-ai-weekly/)**

📮 **团队投稿：[打开周刊投稿表单](https://github.com/kingdream-cn/embodied-ai-weekly/issues/new?template=submission.yml)** · **开发协作：[AGENTS.md](AGENTS.md)**

</div>

---

## 📖 项目概述

**具身智能周刊** 是一个面向具身智能从业者与爱好者的每周内容精选站点，聚焦 **人形机器人、灵巧操作、世界模型、自主导航** 等方向。

每期从顶会论文、行业报告、技术社区与视频平台中筛选真正值得花时间的内容，按固定板块归档，并给出工程视角的解读：

- 🎯 **核心亮点**：一句话讲清这条内容到底讲透了什么；
- 🔧 **团队参考**：站在工程团队角度，说明这条内容对我们意味着什么、该怎么做。

站点基于 **VitePress** 构建，全站静态生成（SSG），内容以 Markdown 文件维护，推送 `main` 分支后由 **GitHub Actions** 自动构建并发布到 **GitHub Pages**。所有周刊归档均可在在线阅读站点中查阅与全文搜索。

> 💡 适合人群：具身智能 / 机器人方向的算法工程师、系统工程师、产品与研究者，以及希望快速跟进该领域的团队。

---

## 📸 项目截图

| 首页（Hero + 往期周刊网格） | 周刊详情页（板块卡片 + 侧栏大纲） |
| :---: | :---: |
| ![首页](screenshots/home.png) | ![周刊详情页](screenshots/issue-42.png) |

---

## ✨ 功能特性

- 🗂️ **七大内容板块**：行业洞察、精选教程 & 学习资源、开源项目 & 行业案例、工程实战 & 踩坑记录、硬件测评 & 选型雷达、极客茶水间 & 脑暴碰撞、顶会前沿 & 论文速递；
- 🎯 **「核心亮点 + 团队参考」双视角解读**：不止有摘要，更有落地参考价值；
- 🎨 **板块配色系统**：每个板块拥有独立淡彩底色与边框配色，卡片样式随之联动，一眼区分内容类型；
- 🌓 **明暗主题切换**：钉钉风浅色主题（品牌色 `#1677FF`）与深色主题自由切换；
- 🔍 **站内全文搜索**：基于 VitePress 本地索引，无需外部服务；
- 🧭 **右侧大纲精准跳转**：卡片内的条目标题（三级标题）会被大纲解析，长文阅读不迷路；
- 📚 **归档自动聚合**：`issues/*.md` 内容文件自动生成卡片网格（标题、日期、摘要、标签），无需手动维护列表；
- 📅 **更新节奏稳定**：以周为单位持续更新（当前已更新至第 46 期）；
- 📱 **响应式布局**：桌面与移动端均有良好阅读体验；
- 🚀 **CI/CD 自动部署**：推送到 `main` 即自动构建并上线 GitHub Pages。

---

## 🧰 技术栈

| 类别 | 技术 | 说明 |
| --- | --- | --- |
| 静态站点框架 | [VitePress](https://vitepress.dev/) `^1.6` | 基于 Vite 与 Vue 3 的静态站点生成器 |
| 内容增强 | [markdown-it-container](https://github.com/markdown-it/markdown-it-container) `^4.0` | 实现 `::: card`、`::: key-points` 周刊卡片容器 |
| 主题样式 | 原生 CSS（VitePress 设计令牌） | 钉钉风配色、板块强调色、明暗双主题 |
| 数据层 | VitePress Content Loader | 自动扫描 `issues/*.md`，生成归档卡片数据 |
| 构建运行时 | Node.js ≥ 20 | 本地与 CI（Node 20）构建环境 |
| 部署 | GitHub Actions + GitHub Pages | `main` 分支推送触发自动构建发布 |

---

## 🚀 快速开始

### 环境要求

- **Node.js ≥ 20**（推荐 LTS）
- npm（随 Node 附带即可）

### 本地运行

```bash
# 1. 克隆仓库
git clone git@github.com:kingdream-cn/embodied-ai-weekly.git
cd embodied-ai-weekly

# 2. 安装依赖
npm install

# 3. 启动开发服务器（热更新）
npm run docs:dev
# 打开 http://localhost:5173/embodied-ai-weekly/
```

### 常用命令

| 命令 | 说明 |
| --- | --- |
| `npm run docs:dev` | 启动本地开发服务器（支持热更新） |
| `npm run docs:build` | 构建生产产物到 `dist/` |
| `npm run docs:preview` | 本地预览构建产物 |

---

## 📦 部署方式

### 方式一：GitHub Actions 自动部署（推荐，本项目采用）

仓库已内置工作流 [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)，推送 `main` 分支后自动完成 **构建 → 发布 GitHub Pages** 全流程；也可在 Actions 页面手动触发（`workflow_dispatch`）。

**首次启用步骤：**

1. 进入仓库 `Settings → Pages`，将 **Source** 设置为 **GitHub Actions**；
2. 推送任意提交到 `main` 分支（或手动触发工作流）；
3. 构建完成后访问 `https://<owner>.github.io/<repo>/`。

**关于 `base` 路径：**

- 本项目部署为**项目站点**，`.vitepress/config.mjs` 默认使用 `base: '/embodied-ai-weekly/'`，CI 构建时会通过 `BASE` 环境变量按仓库名自动注入；
- 若部署为**用户/组织站点**（`<owner>.github.io` 根路径），将 `BASE` 设为 `'/'`（或直接修改配置中的默认值）。

### 方式二：手动构建，部署到任意静态托管

```bash
npm run docs:build      # 产物输出到 dist/
```

将 `dist/` 目录整体上传到 Nginx、Vercel、Netlify、OSS/COS 等任意静态托管服务即可（注意同步调整 `base` 路径）。

---

## 📖 使用说明

### 浏览站点

- 顶部导航切换 **首页 / 往期周刊**；
- 首页卡片网格展示全部期次（标题、日期、摘要、标签），点击进入对应期次；
- 周刊详情页左侧为**分期导航**，右侧为**本页目录**（可跳转到具体条目），支持明暗主题切换；
- 使用顶部搜索框（或 `Ctrl / ⌘ + K`）进行站内全文搜索。

### 撰写新一期周刊

**第 1 步：新建内容文件**，在 `issues/` 目录下创建 `issue-XX.md`，并填写 frontmatter：

```markdown
---
title: "2026具身周刊 - 第 43 期"
date: 2026-10-19
description: "本期一句话导读，将展示在首页卡片上。"
tags:
  - 顶会风向
  - 端侧部署
---

# 2026具身周刊 - 第 43 期

> 📅 **发布时间**：2026-10-19 &nbsp;|&nbsp; 🏷️ **核心议题**：xxx、yyy、zzz

---

## 💡 行业洞察

::: card insight
### 1. [端侧风向] [条目标题（指向原文的真实链接）](https://example.com)

- **核心亮点：** 提炼内容价值与关键结论。
- **团队参考：** 站在工程团队角度的行动建议。
- **载体：** B 站视频 · 10 分钟速览
:::
```

**第 2 步：使用卡片容器**。每个条目用 `::: card <板块标识>` 包裹，板块标识与配色对应关系如下：

| 板块 | 容器标识 | 卡片配色 |
| --- | --- | :---: |
| 💡 行业洞察 | `insight` | 暖黄 |
| 📚 精选教程 & 学习资源 | `tutorial` | 中性灰 |
| 🛠️ 开源项目 & 行业案例 | `opensource` | 浅粉 |
| ⚙️ 工程实战 & 踩坑记录 | `practice` | 浅蓝 |
| 🛒 硬件测评 & 选型雷达 | `review` | 浅紫 |
| ☕ 极客茶水间 & 脑暴碰撞 | `lounge` | 淡咖 |
| 📑 顶会前沿 & 论文速递 | `paper` | 浅绿 |

> 开关容器需成对书写（`::: card insight` … `:::`）；条目标题使用三级标题 `###`，确保能被右侧大纲解析并精准跳转。

**第 3 步：更新侧边栏**，在 `.vitepress/config.mjs` 的 `themeConfig.sidebar` 中补充新一期链接。

**第 4 步：本地运行 `npm run docs:build` 并预览确认无误后**，将改动提交到独立分支并发起 PR。经负责人审核合入 `main` 后，现有 GitHub Actions 自动构建并发布网站。

---

## 📂 项目结构

```text
embodied-ai-weekly/
├── .github/workflows/deploy.yml   # GitHub Actions 自动部署工作流
├── .vitepress/
│   ├── config.mjs                 # 站点配置（导航 / 侧边栏 / 搜索 / 卡片容器）
│   └── theme/
│       ├── index.ts               # 主题入口
│       ├── style.css              # 钉钉风设计令牌与卡片样式
│       ├── issues.data.ts         # 周刊数据加载器（扫描 issues/*.md）
│       └── components/
│           └── IssuesGrid.vue     # 「往期周刊」卡片网格组件
├── issues/                        # 周刊正文（Markdown，每期一个文件）
│   ├── index.md                   # 往期周刊归档页
│   ├── issue-37.md
│   └── ...                        # issue-XX.md
├── public/                        # 静态资源（logo 等，构建时原样拷贝）
├── screenshots/                   # README 项目截图
├── AGENTS.md                      # AI 编程助手的仓库协作指引
├── README.md                      # 项目介绍与团队投稿说明
├── index.md                       # 首页（Hero + 往期周刊网格）
└── package.json
```

---

## 🤝 贡献指南

欢迎任何形式的贡献，感谢你帮助这份周刊变得更好！

### 团队每周投稿

每位成员每周至少推荐 1 篇具身智能相关内容。**本周收集，供下周周刊审核选用；每周六 15:00 截止，统一使用北京时间（Asia/Shanghai）。** 审核负责人为 [@kingdream-cn](https://github.com/kingdream-cn)，有效投稿不等于入刊或自动发布。

#### 如何提交

1. 登录已登记的**本人 GitHub 账号**，打开 [周刊投稿表单](https://github.com/kingdream-cn/embodied-ai-weekly/issues/new?template=submission.yml)。也可从 `Issues → New issue → 周刊投稿` 进入，不选择 `Blank issue`。
2. 在 `Add a title` 填写 `[投稿] 具体内容名称`；表单版本保留 `v1`，再填写“内容标题”和一个公开 HTTPS 原文链接。
3. 选择推荐板块与载体类型，向下滚动补齐推荐理由、原始要点及团队参考建议。
4. 确认内容来源与公开声明均属实，勾选两项声明后点击 `Create`（部分页面显示 `Submit new issue`）。**每篇材料单独提交一个 Issue。**
5. 保存生成的 Issue 链接，核对作者为本人、正文完整且状态为 `Open`。成员无需运行 Actions，也无需访问私有台账。

| 字段 | 填写要求 |
| --- | --- |
| 内容标题 | 5–160 字符，写清文章、论文或项目名称 |
| 原文链接 | 一个公开 HTTPS 来源链接，不包含密码或访问令牌 |
| 一句话推荐理由 | 20–500 字符，说明为什么值得团队阅读 |
| 原始要点或可核对摘录 | 50–6000 字符；实验数据注明出处，不编造结论 |
| 对团队的参考建议 | 通常 20–1000 字符；确实无法判断时可准确填写“暂不确定” |
| 补充链接 | 选填，每行一个公开 HTTPS 链接，最多 5 个 |

站点支持七个内容板块，**当前投稿表单提供六类，暂不包含“极客茶水间 & 脑暴碰撞”**；请按表单现有选项选择。表单必填检查不等于后台长度、身份和去重校验全部通过。

#### 修改和完成统计

- 补充同一篇材料时编辑原 Issue，保留字段标题和两项声明。首次有效后不要把原文链接换成另一篇；推荐新来源时另建 Issue。
- 关闭 Issue 视为撤回，重新打开后会再次校验。跨周修改或重开同一篇投稿，不会自动计为新一周任务。
- 系统按 GitHub 作者数字 ID 核验身份，对有效、去重后的投稿统计完成情况；重复或历史已收录的内容不重复计数。
- 私有台账按小时对账，GitHub 定时任务可能延迟。创建成功不保证即时计数；有疑问请把 Issue 链接发给负责人核对。
- 逾期投稿单独统计并顺延计划入刊周；时间证据不足的记录由负责人核对。

#### 投稿与推送的分工

公开仓库承载投稿、周刊正文和原网站；成员配置、姓名映射及完成统计保存在独立私有台账，不写入公开 Issue、README 或网站。**投稿 Issue 本身公开可见**，只填写可公开资料，不包含内部信息、个人隐私或密钥。

截至 2026-11-11，投稿与私有台账对账已运行，钉钉已完成群内手动提醒。周五 08:00 为计划提醒时间，周六截止后计划汇总；**钉钉定时通知、真实 AI 编辑和周刊自动发布尚未启用**。周刊仍由负责人审核发布到本仓库及原网站。

#### 当前周期安排

以下为 2026-11-11 核对的安排，后续以负责人确认的收集周期及目标期号为准；ISO 周号与周刊期号不是同一概念。

| 收集日期 | 截止时间（北京时间） | 计划发布周 | 目标周刊 |
| --- | --- | --- | --- |
| 2026-11-09 至 11-15 | 11-14 周六 15:00 | 11-16 至 11-22 | 第 47 期 |
| 2026-11-16 至 11-22 | 11-21 周六 15:00 | 11-23 至 11-29 | 第 48 期 |

第 46 期已于 2026-11-09 发布。上表是审核选用安排，不表示相关期次已发布；私有运行配置和既有台账的期号修正仍需单独审查同步，公开说明不能替代台账迁移。

### 推荐选题 / 内容勘误

- 推荐文章、视频或开源项目时，请使用上方**周刊投稿表单**，按要求填写完整信息；
- 正文链接失效、描述有误或其他反馈，可提交 [Issue](https://github.com/kingdream-cn/embodied-ai-weekly/issues)。

### 代码与样式改进

开发者与 AI 编程助手请先阅读根目录 [AGENTS.md](AGENTS.md)，了解内容格式、验证命令与公开和私有数据边界。

1. **Fork** 本仓库并新建分支，如 `feat/card-hover`、`fix/sidebar-link`；
2. 提交时使用语义化前缀（与仓库历史风格保持一致）：`feat:` / `fix:` / `style:` / `docs:` / `chore:`；
3. 建议一次 PR 只做一件事，并在 PR 描述中说明**变更内容**与**验证方式**；
4. 发起 **Pull Request**，等待 Review 合入。

> 注意：周刊选题与文案保持统一的编辑口径，**新增/修改周刊内容**建议先通过 Issue 沟通，避免直接改动正文。

---

## 📬 联系方式

- **GitHub**：[@kingdream-cn](https://github.com/kingdream-cn)
- **问题反馈**：[提交 Issue](https://github.com/kingdream-cn/embodied-ai-weekly/issues)
- **在线阅读**：[https://kingdream-cn.github.io/embodied-ai-weekly/](https://kingdream-cn.github.io/embodied-ai-weekly/)

---

<div align="center">

**如果这份周刊对你有帮助，欢迎 ⭐ Star 支持一下！**

<sub>Made with ❤️ by kingdream-cn · Powered by VitePress</sub>

</div>
