# 🎭 The Agency：AI 专家，随时待命，变革你的工作流程

> **一站式完整 AI 机构尽在指尖** — 从前端魔法师到 Reddit 社区达人，从趣味注入师到现实检验员。每个代理都是拥有个性、流程和经过验证可交付成果的专业专家。

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)](https://github.com/sponsors/msitarzewski)

---

## 🚀 这是什么？

诞生于一个 Reddit 帖子和数月的迭代打磨，**The Agency** 是一个不断壮大的精心打造的 AI 代理性格集合。每个代理都是：

- **🎯 专业化的**：在自身领域拥有深厚专业知识（而非泛泛的提示词模板）
- **🧠 个性驱动的**：独特的话风、沟通风格和行事方式
- **📋 以可交付成果为导向**：真实的代码、流程和可衡量的成果
- **✅ 可直接投产**：久经考验的工作流程和成功指标

**这样理解**：组建你的梦之队——只是这些 AI 专家不用睡觉、从不抱怨、使命必达。

---

## ⚡ 快速开始

### 方案一：与 Claude Code 配合使用（推荐）

```bash
# 将所有代理安装到你的 Claude Code 目录
./scripts/install.sh --tool claude-code

# 如果你只需要一个部门，也可以手动复制单个类别
cp engineering/*.md ~/.claude/agents/

# 然后在你的 Claude Code 会话中激活任意代理：
# "Hey Claude, 激活前端开发模式，帮我构建一个 React 组件"
```

### 方案二：作为参考使用

每个代理文件包含：
- 身份与个性特质
- 核心使命与工作流程
- 包含代码示例的技术交付物
- 成功指标与沟通风格

浏览下方代理，复制或适配你需要的！

### 方案三：与其他工具配合使用（GitHub Copilot、Antigravity、Gemini CLI、OpenCode、OpenClaw、Cursor、Aider、Windsurf、Kimi Code、Codex）

```bash
# 第 1 步 -- 为所有支持的工具生成集成文件
./scripts/convert.sh

# 第 2 步 -- 交互式安装（自动检测你已安装的工具）
./scripts/install.sh

# 或直接指定某个工具
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool opencode
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool cursor
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool kimi
./scripts/install.sh --tool codex
```

**仅安装你需要的团队**（不是每个人都需要全部 16 个部门）：

```bash
./scripts/install.sh                                    # 交互式向导：选择工具 + 团队
./scripts/install.sh --tool claude-code --division engineering,security
./scripts/install.sh --tool cursor --agent frontend-developer,ui-designer
./scripts/install.sh --list teams                       # 查看每个团队及代理数量
./scripts/install.sh --tool opencode --division engineering --dry-run
```

> **OpenCode 注意：** OpenCode 运行时目前只注册约 119 个代理并会静默丢弃其余代理（[上游 bug](https://github.com/anomalyco/opencode/issues/27988)）。使用 `--division` 安装子集可保持在限制以内。当你的选择会超限时，安装器会警告你。

详情参见下方的[多工具集成](#-多工具集成)部分。

---

## 🎨 机构阵容

### 💻 工程部

一次提交接一次提交，构建未来。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎨 [前端开发](engineering/engineering-frontend-developer.md) | React/Vue/Angular、UI 实现、性能优化 | 现代 Web 应用、像素级精确 UI、Core Web Vitals 优化 |
| 🏗️ [后端架构师](engineering/engineering-backend-architect.md) | API 设计、数据库架构、可扩展性 | 服务端系统、微服务、云基础设施 |
| 📱 [移动应用构建者](engineering/engineering-mobile-app-builder.md) | iOS/Android、React Native、Flutter | 原生及跨平台移动应用 |
| 🤖 [AI 工程师](engineering/engineering-ai-engineer.md) | 机器学习模型、部署、AI 集成 | 机器学习功能、数据管道、AI 驱动的应用 |
| 🚀 [DevOps 自动化工程师](engineering/engineering-devops-automator.md) | CI/CD、基础设施自动化、云运维 | 流水线开发、部署自动化、监控 |
| ⚡ [快速原型师](engineering/engineering-rapid-prototyper.md) | 快速 POC 开发、MVP | 快速概念验证、黑客松项目、快速迭代 |
| 💎 [高级开发](engineering/engineering-senior-developer.md) | Laravel/Livewire、高级模式 | 复杂实现、架构决策 |
| 🔧 [Filament 优化专家](engineering/engineering-filament-optimization-specialist.md) | Filament PHP 管理后台 UX、结构化表单重构、资源优化 | 重构 Filament 资源/表单/表格，实现更快更清晰的管理工作流 |
| ⚡ [自主优化架构师](engineering/engineering-autonomous-optimization-architect.md) | LLM 路由、成本优化、影子测试 | 需要智能 API 选择和成本守护的自主系统 |
| 🔩 [嵌入式固件工程师](engineering/engineering-embedded-firmware-engineer.md) | 裸机、RTOS、ESP32/STM32/Nordic 固件开发 | 生产级嵌入式系统和物联网设备 |
| 🚨 [事故响应指挥官](engineering/engineering-incident-response-commander.md) | 事故管理、事后复盘、值班管理 | 管理生产事故和建设事故响应能力 |
| ⛓️ [Solidity 智能合约工程师](engineering/engineering-solidity-smart-contract-engineer.md) | EVM 合约、Gas 优化、DeFi | 安全、Gas 优化的智能合约和 DeFi 协议 |
| 🧭 [代码库入门引导工程师](engineering/engineering-codebase-onboarding-engineer.md) | 开发者快速上手、只读代码探索、基于事实的讲解 | 通过阅读代码、追踪代码路径、陈述结构行为事实，帮助新开发者快速理解陌生代码库 |
| 📚 [技术文档工程师](engineering/engineering-technical-writer.md) | 开发者文档、API 参考、教程 | 清晰准确的技术文档 |
| 💬 [微信小程序开发](engineering/engineering-wechat-mini-program-developer.md) | 微信生态、小程序、支付集成 | 为微信生态构建高性能应用 |
| 👁️ [代码评审员](engineering/engineering-code-reviewer.md) | 建设性代码审查、安全、可维护性 | PR 审查、代码质量门禁、通过审查进行指导 |
| 🗄️ [数据库优化师](engineering/engineering-database-optimizer.md) | Schema 设计、查询优化、索引策略 | PostgreSQL/MySQL 调优、慢查询调试、迁移规划 |
| 🌿 [Git 工作流大师](engineering/engineering-git-workflow-master.md) | 分支策略、约定式提交、高级 Git 操作 | Git 工作流设计、历史清理、CI 友好的分支管理 |
| 🏛️ [软件架构师](engineering/engineering-software-architect.md) | 系统设计、DDD、架构模式、权衡分析 | 架构决策、领域建模、系统演进策略 |
| 🛡️ [SRE](engineering/engineering-sre.md) | SLO、错误预算、可观测性、混沌工程 | 生产可靠性、减少 toil、容量规划 |
| 🧬 [AI 数据修复工程师](engineering/engineering-ai-data-remediation-engineer.md) | 自愈管道、断网 SLM、语义聚类 | 零数据丢失的大规模数据修复 |
| 🔧 [数据工程师](engineering/engineering-data-engineer.md) | 数据管道、湖仓架构、ETL/ELT | 构建可靠的数据基础设施和数仓 |
| 🔗 [飞书集成开发](engineering/engineering-feishu-integration-developer.md) | 飞书/Lark 开放平台、机器人、工作流 | 为飞书生态构建集成 |
| 🧱 [CMS 开发](engineering/engineering-cms-developer.md) | WordPress 与 Drupal 主题、插件/模块、内容架构 | 代码优先的 CMS 实现与定制 |
| 📧 [邮件智能工程师](engineering/engineering-email-intelligence-engineer.md) | 邮件解析、MIME 提取、为 AI 代理生成结构化数据 | 将原始邮件线程转为可供推理的上下文 |
| 🎙️ [语音 AI 集成工程师](engineering/engineering-voice-ai-integration-engineer.md) | 语音转文本管道、Whisper、ASR、说话人分离 | 端到端转录管道、音频预处理、结构化转录稿交付 |
| 🖧 [IT 服务经理](engineering/engineering-it-service-manager.md) | ITIL 4 服务管理 | 事件/问题/变更管理、SLA、CMDB |
| 🪡 [最小变更工程师](engineering/engineering-minimal-change-engineer.md) | 最小可行 diff | 只修复被要求的，不扩大范围 |
| 📜 [OrgScript 工程师](engineering/engineering-orgscript-engineer.md) | OrgScript 语法与 AST 验证 | 设计/解析 OrgScript 业务逻辑定义 |
| 🧬 [提示工程师](engineering/engineering-prompt-engineer.md) | LLM 提示词设计与优化 | 将模糊指令转化为可靠的 AI 行为 |
| 🕸️ [多代理系统架构师](engineering/engineering-multi-agent-systems-architect.md) | 多代理管道设计与治理 | 代理系统的拓扑、上下文、信任、故障恢复 |
| 🛒 [Drupal 购物车工程师](engineering/engineering-drupal-shopping-cart.md) | Drupal Commerce 店面 | Drupal 10/11 上的目录、支付、结账、订单管理 |
| 🛍️ [WordPress 购物车工程师](engineering/engineering-wordpress-shopping-cart.md) | WooCommerce 店面 | WordPress 上的目录、支付、结账、转化优化 |

### 🎨 设计部

让它美丽、易用、令人愉悦。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [UI 设计师](design/design-ui-designer.md) | 视觉设计、组件库、设计系统 | 界面创建、品牌一致性、组件设计 |
| 🔍 [UX 研究员](design/design-ux-researcher.md) | 用户测试、行为分析、研究 | 理解用户、可用性测试、设计洞见 |
| 🏛️ [UX 架构师](design/design-ux-architect.md) | 技术架构、CSS 系统、实现 | 开发者友好的框架、实现指导 |
| 🎭 [品牌守护者](design/design-brand-guardian.md) | 品牌识别、一致性、定位 | 品牌策略、识别开发、规范指南 |
| 📖 [视觉叙事师](design/design-visual-storyteller.md) | 视觉叙事、多媒体内容 | 有感染力的视觉故事、品牌叙事 |
| ✨ [趣味注入师](design/design-whimsy-injector.md) | 个性、愉悦感、趣味交互 | 增添快乐、微交互、彩蛋、品牌个性 |
| 📷 [图像提示工程师](design/design-image-prompt-engineer.md) | AI 图像生成提示词、摄影 | Midjourney、DALL-E、Stable Diffusion 摄影提示词 |
| 🌈 [包容性视觉专家](design/design-inclusive-visuals-specialist.md) | 代表性、偏差缓解、真实图像 | 生成文化属性准确的 AI 图片和视频 |
| 🎭 [角色走查专家](design/design-persona-walkthrough.md) | 以角色为驱动的认知走查 | 模拟用户在每个滚动位置的互动反应和摩擦点 |

### 💰 付费媒体部

将广告支出转化为可衡量的业务成果。

| 代理 | 专长 | 使用场景 |
| --- | --- | --- |
| 💰 [PPC 广告策略师](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon Ads、账户架构、出价策略 | 账户搭建、预算分配、扩量、效果诊断 |
| 🔍 [搜索词分析师](paid-media/paid-media-search-query-analyst.md) | 搜索词分析、否定关键词、意图映射 | 搜索词审计、消除浪费支出、关键词发现 |
| 📋 [付费媒体审计师](paid-media/paid-media-auditor.md) | 200+ 项账户审计、竞品分析 | 账户交接、季度审核、竞品比稿 |
| 📡 [追踪与衡量专家](paid-media/paid-media-tracking-specialist.md) | GTM、GA4、转化追踪、CAPI | 新系统实施、追踪审计、平台迁移 |
| ✍️ [广告创意策略师](paid-media/paid-media-creative-strategist.md) | RSA 文案、Meta 创意、Performance Max 素材 | 创意发布、测试项目、广告疲劳刷新 |
| 📺 [程序化与展示广告投手](paid-media/paid-media-programmatic-buyer.md) | GDN、DSP、合作伙伴媒体、ABM 展示 | 展示广告规划、合作伙伴拓展、ABM 项目 |
| 📱 [付费社交媒体策略师](paid-media/paid-media-paid-social-strategist.md) | Meta、LinkedIn、TikTok、跨平台社交 | 社交广告项目、平台选择、受众策略 |

### 💼 销售部

将销售管道转化为收入——靠的是手艺，而非 CRM 填鸭式操作。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [外拓策略师](sales/sales-outbound-strategist.md) | 基于信号的商机开发、多渠道序列、ICP 定位 | 通过研究驱动而非数量驱动的方式构建销售管道 |
| 🔍 [探索教练](sales/sales-discovery-coach.md) | SPIN、Gap Selling、Sandler — 问题设计与通话结构 | 准备探索通话、商机验证、辅导销售代表 |
| ♟️ [交易策略师](sales/sales-deal-strategist.md) | MEDDPICC 验证、竞争定位、赢单规划 | 交易评分、暴露管道风险、制定赢单策略 |
| 🛠️ [售前工程师](sales/sales-engineer.md) | 技术演示、POC 范围界定、竞争作战卡 | 售前技术赢单、演示准备、竞争定位 |
| 🏹 [提案策略师](sales/sales-proposal-strategist.md) | RFP 应标、赢单主题、叙事结构 | 撰写有说服力而非仅合规的提案 |
| 📊 [管道分析师](sales/sales-pipeline-analyst.md) | 预测、管道健康度、交易速度、RevOps | 管道评审、预测准确性、收入运营 |
| 🗺️ [客户策略师](sales/sales-account-strategist.md) | 立足-扩展、QBR、干系人映射 | 售后扩展、客户规划、NRR 增长 |
| 🏋️ [销售教练](sales/sales-coach.md) | 销售人员发展、通话辅导、管道评审引导 | 通过结构化辅导让每个销售和每笔交易变得更好 |
| 🎯 [销售外拓](specialized/sales-outreach.md) | 冷拓客、多触点节奏、异议处理、提案 | B2B 漏斗上游外拓——从冷邮件到成功预约探索通话 |
| 🧲 [权益与获客线索策略师](sales/sales-offer-lead-gen-strategist.md) | 权益方案与线索磁铁 | 漏斗上游权益构建与线索生成 |

### 📢 市场部

通过每一次真诚互动壮大你的受众。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🚀 [增长黑客](marketing/marketing-growth-hacker.md) | 快速用户获取、病毒循环、实验 | 爆发式增长、用户获取、转化优化 |
| 📝 [内容创作者](marketing/marketing-content-creator.md) | 多平台内容、编辑日历 | 内容策略、文案、品牌叙事 |
| 🐦 [Twitter 互动者](marketing/marketing-twitter-engager.md) | 实时互动、思想领导力 | Twitter 策略、LinkedIn 活动、专业社交 |
| 🛰️ [X/Twitter 情报分析师](marketing/marketing-x-twitter-intelligence-analyst.md) | 社交聆听、趋势检测、账户监控 | X/Twitter 品牌风险、竞品和受众情报 |
| 📱 [TikTok 策略师](marketing/marketing-tiktok-strategist.md) | 病毒内容、算法优化 | TikTok 增长、病毒内容、Z 世代/千禧一代受众 |
| 📸 [Instagram 策展人](marketing/marketing-instagram-curator.md) | 视觉叙事、社区建设 | Instagram 策略、美学塑造、视觉内容 |
| 🤝 [Reddit 社区建设者](marketing/marketing-reddit-community-builder.md) | 真诚互动、价值驱动内容 | Reddit 策略、社区信任、真诚营销 |
| 📱 [应用商店优化师](marketing/marketing-app-store-optimizer.md) | ASO、转化优化、可发现性 | 应用营销、商店优化、应用增长 |
| 🌐 [社交媒体策略师](marketing/marketing-social-media-strategist.md) | 跨平台策略、活动策划 | 整体社交策略、多平台活动 |
| 📕 [小红书专家](marketing/marketing-xiaohongshu-specialist.md) | 生活方式内容、趋势驱动策略 | 小红书增长、美学叙事、Z 世代受众 |
| 💬 [微信公众号运营](marketing/marketing-wechat-official-account.md) | 关注者互动、内容营销 | 微信公众号策略、社区建设、转化优化 |
| 🧠 [知乎策略师](marketing/marketing-zhihu-strategist.md) | 思想领导力、知识驱动互动 | 知乎权威建设、问答策略、线索生成 |
| 🇨🇳 [百度 SEO 专家](marketing/marketing-baidu-seo-specialist.md) | 百度优化、中国 SEO、ICP 合规 | 在百度获得排名并触达中国搜索市场 |
| 🎬 [Bilibili 内容策略师](marketing/marketing-bilibili-content-strategist.md) | B 站算法、弹幕文化、UP 主增长 | 通过社区优先的内容在 B 站建立受众 |
| 🎠 [轮播增长引擎](marketing/marketing-carousel-growth-engine.md) | TikTok/Instagram 轮播内容、自主发布 | 生成并发布病毒轮播内容 |
| 💼 [LinkedIn 内容创作者](marketing/marketing-linkedin-content-creator.md) | 个人品牌、思想领导力、专业内容 | LinkedIn 增长、专业受众建设、B2B 内容 |
| 🛒 [中国电商运营](marketing/marketing-china-ecommerce-operator.md) | 淘宝、天猫、拼多多、直播电商 | 在中国运营多平台电商 |
| 🎥 [快手策略师](marketing/marketing-kuaishou-strategist.md) | 快手、老铁文化、草根增长 | 在低线城市建立真实受众 |
| 🔍 [SEO 专家](marketing/marketing-seo-specialist.md) | 技术 SEO、内容策略、链接建设 | 推动可持续的有机搜索增长 |
| 📘 [图书合著伙伴](marketing/marketing-book-co-author.md) | 思想领导力图书、代笔、出版 | 为创始人和专家提供策略性书籍合作 |
| 🌏 [跨境电商专家](marketing/marketing-cross-border-ecommerce.md) | Amazon、Shopee、Lazada、跨境物流 | 全链路跨境电商策略 |
| 🎵 [抖音策略师](marketing/marketing-douyin-strategist.md) | 抖音平台、短视频营销、算法 | 在中国头号短视频平台上增长受众 |
| 🎙️ [直播电商教练](marketing/marketing-livestream-commerce-coach.md) | 主播培训、直播间优化、转化 | 打造高绩效直播电商运营 |
| 🎧 [播客策略师](marketing/marketing-podcast-strategist.md) | 播客内容策略、平台优化 | 中国播客市场策略与运营 |
| 🔒 [私域运营](marketing/marketing-private-domain-operator.md) | 企业微信、私域流量、社群运营 | 构建企业微信私域生态 |
| 🎬 [短视频剪辑教练](marketing/marketing-short-video-editing-coach.md) | 后期制作、剪辑工作流、平台规范 | 实操短视频剪辑培训与优化 |
| 🔥 [微博策略师](marketing/marketing-weibo-strategist.md) | 新浪微博、热搜话题、粉丝互动 | 全谱系微博运营与增长 |
| 🎙️ [全球播客策略师](marketing/marketing-global-podcast-strategist.md) | 节目定位、受众增长、变现 | 播客发布、平台算法、赞助、社区建设 |
| 🔮 [AI 引用策略师](marketing/marketing-ai-citation-strategist.md) | AEO/GEO、AI 推荐可见性、引用审计 | 提升品牌在 ChatGPT、Claude、Gemini、Perplexity 中的可见性 |
| 🇨🇳 [中国市场本地化策略师](marketing/marketing-china-market-localization-strategist.md) | 全栈中国市场本地化、抖音/小红书/WeChat GTM | 将趋势信号转化为可执行的中国市场进入策略 |
| 🎬 [视频优化专家](marketing/marketing-video-optimization-specialist.md) | YouTube 算法策略、章节化、缩略图概念 | YouTube 频道增长、视频 SEO、观众留存优化 |
| 🏗️ [AEO 基础架构师](marketing/marketing-aeo-foundations.md) | AI 引擎优化基础设施 | llms.txt、AI 感知 robots.txt、代理发现文件 |
| 🤖 [代理搜索优化师](marketing/marketing-agentic-search-optimizer.md) | WebMCP 与代理任务完成 | 让网站能被 AI 浏览代理使用 |
| 📧 [邮件营销策略师](marketing/marketing-email-strategist.md) | 生命周期邮件与送达率 | CRM 活动、自动化、细分 |
| 📡 [多平台发布者](marketing/marketing-multi-platform-publisher.md) | 一键中文多平台发布 | 将一篇文章分发到知乎/小红书/CSDN/B 站/公众号/掘金 |
| 📣 [公关与传播经理](marketing/marketing-pr-communications-manager.md) | 公关、媒体关系与危机传播 | 新闻稿、思想领导力、声誉 |

### 📊 产品部

在正确的时间构建正确的东西。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [迭代优先级师](product/product-sprint-prioritizer.md) | 敏捷规划、功能优先级排序 | 迭代规划、资源分配、待办列表管理 |
| 🔍 [趋势研究员](product/product-trend-researcher.md) | 市场情报、竞争分析 | 市场研究、机会评估、趋势识别 |
| 💬 [反馈整合师](product/product-feedback-synthesizer.md) | 用户反馈分析、洞见提取 | 反馈分析、用户洞见、产品优先级 |
| 🧠 [行为助推引擎](product/product-behavioral-nudge-engine.md) | 行为心理学、助推设计、参与度 | 通过行为科学最大化用户激励 |
| 🧭 [产品经理](product/product-manager.md) | 全生命周期产品管理 | 探索、PRD、路线图规划、GTM、成果衡量 |

### 🎬 项目管理部

让列车准时运行（且在预算内）。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎬 [版房制作人](project-management/project-management-studio-producer.md) | 高层统筹、项目组合管理 | 多项目监督、战略对齐、资源分配 |
| 🐑 [项目牧羊人](project-management/project-management-project-shepherd.md) | 跨职能协调、时间线管理 | 端到端项目协调、干系人管理 |
| ⚙️ [版房运营](project-management/project-management-studio-operations.md) | 日常效率、流程优化 | 运营卓越、团队支持、生产力 |
| 🧪 [实验追踪者](project-management/project-management-experiment-tracker.md) | A/B 测试、假设验证 | 实验管理、数据驱动决策、测试 |
| 👔 [高级项目经理](project-management/project-manager-senior.md) | 现实范围界定、任务转化 | 将规格转化为任务、范围管理 |
| 📋 [Jira 工作流管家](project-management/project-management-jira-workflow-steward.md) | Git 工作流、分支策略、可追溯性 | 共守 Jira 链接的 Git 纪律和交付 |
| 📋 [会议纪要专家](project-management/project-management-meeting-notes-specialist.md) | 结构化会议摘要 | 提取决策、行动项、待决问题 |

### 🧪 测试部

替用户踩坑排雷。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📸 [证据收集员](testing/testing-evidence-collector.md) | 基于截图的 QA、视觉证明 | UI 测试、视觉验证、Bug 记录 |
| 🔍 [现实检查员](testing/testing-reality-checker.md) | 基于证据的认证、质量关卡 | 生产就绪性、质量审批、发布认证 |
| 📊 [测试结果分析师](testing/testing-test-results-analyzer.md) | 测试评估、指标分析 | 测试输出分析、质量洞见、覆盖率报告 |
| ⚡ [性能基准师](testing/testing-performance-benchmarker.md) | 性能测试、优化 | 速度测试、负载测试、性能调优 |
| 🔌 [API 测试员](testing/testing-api-tester.md) | API 验证、集成测试 | API 测试、端点验证、集成 QA |
| 🛠️ [工具评估师](testing/testing-tool-evaluator.md) | 技术评估、工具选择 | 评估工具、软件推荐、技术决策 |
| 🔄 [工作流优化师](testing/testing-workflow-optimizer.md) | 流程分析、工作流改进 | 流程优化、效率提升、自动化机会 |
| ♿ [无障碍审计师](testing/testing-accessibility-auditor.md) | WCAG 审计、辅助技术测试 | 无障碍合规、屏幕阅读器测试、包容性设计验证 |

### 🔒 安全部

守卫全栈——从安全设计架构到入侵响应。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🛡️ [安全架构师](security/security-architect.md) | 威胁建模、安全设计、信任边界 | 系统安全模型、架构评审、纵深防御 |
| 🔐 [应用安全工程师](security/security-appsec-engineer.md) | SDLC 安全、SAST/DAST、安全代码审查 | 保障开发全生命周期安全、代码级漏洞 |
| 🗡️ [渗透测试员](security/security-penetration-tester.md) | 授权渗透测试、红队行动、漏洞利用 | 在攻击者之前发现可被利用的弱点 |
| ☁️ [云安全架构师](security/security-cloud-security-architect.md) | 零信任、云原生纵深防御 | 保障云基础设施和架构安全 |
| 🚨 [事故响应员](security/security-incident-responder.md) | DFIR、入侵调查、威胁遏制 | 活跃入侵、取证、危机响应 |
| 🔍 [威胁情报分析师](security/security-threat-intelligence-analyst.md) | 攻击者追踪、活动映射、ATT&CK | 了解谁在攻击以及如何攻击 |
| 🎯 [威胁检测工程师](security/security-threat-detection-engineer.md) | SIEM 规则、威胁狩猎、ATT&CK 映射 | 构建检测层和威胁狩猎 |
| 🛡️ [高级安全运维工程师](security/security-senior-secops.md) | 密钥扫描、默认安全的提交 | 每次变更的防守型代码级安全 |
| 📋 [合规审计师](security/security-compliance-auditor.md) | SOC 2、ISO 27001、HIPAA、PCI-DSS | 引导组织通过合规认证 |
| 🛡️ [区块链安全审计师](security/security-blockchain-security-auditor.md) | 智能合约审计、漏洞利用分析 | 在部署前发现合约中的漏洞 |

### 🛟 支持部

运营的中流砥柱。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 💬 [支持响应员](support/support-support-responder.md) | 客户服务、问题解决 | 客户支持、用户体验、支持运营 |
| 📊 [分析报告员](support/support-analytics-reporter.md) | 数据分析、仪表板、洞见 | 商业智能、KPI 追踪、数据可视化 |
| 💰 [财务追踪员](support/support-finance-tracker.md) | 财务规划、预算管理 | 财务分析、现金流、业务表现 |
| 🏗️ [基础设施管理员](support/support-infrastructure-maintainer.md) | 系统可靠性、性能优化 | 基础设施管理、系统运维、监控 |
| ⚖️ [法律合规检查员](support/support-legal-compliance-checker.md) | 合规、法规、法律审查 | 法律合规、监管要求、风险管理 |
| 📑 [执行摘要生成器](support/support-executive-summary-generator.md) | 高管层沟通、战略摘要 | 高管报告、战略沟通、决策支持 |

### 🥽 空间计算部

构建沉浸式未来。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [XR 界面架构师](spatial-computing/xr-interface-architect.md) | 空间交互设计、沉浸式 UX | AR/VR/XR 界面设计、空间计算用户体验 |
| 💻 [macOS 空间/Metal 工程师](spatial-computing/macos-spatial-metal-engineer.md) | Swift、Metal、高性能 3D | macOS 空间计算、Vision Pro 原生应用 |
| 🌐 [XR 沉浸式开发](spatial-computing/xr-immersive-developer.md) | WebXR、基于浏览器的 AR/VR | 基于浏览器的沉浸式体验、WebXR 应用 |
| 🎮 [XR 驾驶舱交互专家](spatial-computing/xr-cockpit-interaction-specialist.md) | 基于驾驶舱的控制、沉浸式系统 | 驾驶舱控制系统、沉浸式控制界面 |
| 🍎 [visionOS 空间工程师](spatial-computing/visionos-spatial-engineer.md) | Apple Vision Pro 开发 | Vision Pro 应用、空间计算体验 |
| 🔌 [终端集成专家](spatial-computing/terminal-integration-specialist.md) | 终端集成、命令行工具 | CLI 工具、终端工作流、开发者工具 |

### 🎯 专家部

不适合归类的独特专家。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎭 [代理编排师](specialized/agents-orchestrator.md) | 多代理协调、工作流管理 | 需要多个代理协调的复杂项目 |
| 🔍 [LSP/索引工程师](specialized/lsp-index-engineer.md) | 语言服务器协议、代码智能 | 代码智能系统、LSP 实现、语义索引 |
| 📥 [销售数据提取代理](specialized/sales-data-extraction-agent.md) | Excel 监控、销售指标提取 | 销售数据采集、MTD/YTD/年末指标 |
| 📈 [数据合并代理](specialized/data-consolidation-agent.md) | 销售数据聚合、仪表板报告 | 区域汇总、销售代表绩效、管道快照 |
| 📬 [报告分发代理](specialized/report-distribution-agent.md) | 自动化报告分发 | 按区域分发报告、定时发送 |
| 🔐 [代理身份与信任架构师](specialized/agentic-identity-trust.md) | 代理身份、认证、信任验证 | 多代理身份系统、代理授权、审计追踪 |
| 🔗 [身份图谱操作员](specialized/identity-graph-operator.md) | 多代理系统的共享身份解析 | 实体去重、合并提案、跨代理身份一致性 |
| 💸 [应付账款代理](specialized/accounts-payable-agent.md) | 付款处理、供应商管理、审计 | 加密货币、法币、稳定币的自主付款执行 |
| 🌍 [文化情报策略师](specialized/specialized-cultural-intelligence-strategist.md) | 全球用户体验、代表性、文化排斥 | 确保软件跨文化产生共鸣 |
| 🗣️ [开发者布道师](specialized/specialized-developer-advocate.md) | 社区建设、开发者体验、开发者内容 | 连接产品与开发者社区 |
| 🔬 [模型 QA 专家](specialized/specialized-model-qa.md) | 机器学习审计、特征分析、可解释性 | 机器学习模型端到端 QA |
| 🗃️ [ZK 管家](specialized/zk-steward.md) | 知识管理、卡片盒笔记法、笔记 | 构建相互关联、经过验证的知识库 |
| 🔌 [MCP 构建者](specialized/specialized-mcp-builder.md) | 模型上下文协议服务器、AI 代理工具 | 构建扩展 AI 代理能力的 MCP 服务器 |
| 📄 [文档生成器](specialized/specialized-document-generator.md) | 通过代码生成 PDF、PPTX、DOCX、XLSX | 专业文档生成、报告、数据可视化 |
| ⚙️ [自动化治理架构师](specialized/automation-governance-architect.md) | 自动化治理、n8n、工作流审计 | 评估和治理规模化业务自动化 |
| 📚 [企业培训设计师](specialized/corporate-training-designer.md) | 企业培训、课程开发 | 设计培训系统和学习项目 |
| 🌱 [个人成长导师](specialized/personal-growth-mentor.md) | 目标清晰、习惯系统、问责、生活策略 | 跨领域个人发展，拒绝空洞激励 |
| 🏛️ [政府数字化售前顾问](specialized/government-digital-presales-consultant.md) | 中国 ToG 售前、数字化转型 | 政府数字化转型方案与投标 |
| ⚕️ [医疗营销合规](specialized/healthcare-marketing-compliance.md) | 中国医疗广告合规 | 医疗营销监管合规 |
| 🎯 [招聘专员](specialized/recruitment-specialist.md) | 人才获取、招聘运营 | 招聘策略、人才寻源与雇佣流程 |
| 🎓 [留学顾问](specialized/study-abroad-advisor.md) | 国际教育、申请规划 | 美国、英国、加拿大、澳大利亚留学规划 |
| 🔗 [供应链策略师](specialized/supply-chain-strategist.md) | 供应链管理、采购策略 | 供应链优化与采购规划 |
| 🗺️ [工作流架构师](specialized/specialized-workflow-architect.md) | 工作流发现、映射与规格制定 | 在编码前映射系统中的每条路径 |
| ☁️ [Salesforce 架构师](specialized/specialized-salesforce-architect.md) | 多云 Salesforce 设计、治理限制、集成 | 企业 Salesforce 架构、组织策略、部署管道 |
| 🇫🇷 [法国咨询市场导航者](specialized/specialized-french-consulting-market.md) | ESN/SI 生态、portage salarial、费率定位 | 法国 IT 市场的独立咨询业务 |
| 🇰🇷 [韩国商务导航者](specialized/specialized-korean-business-navigator.md) | 韩国商业文化、품의 流程、关系机制 | 外国专业人士驾驭韩国商务关系 |
| 🏗️ [土木工程师](specialized/specialized-civil-engineer.md) | 结构分析、岩土设计、全球建筑规范 | 跨 Eurocode、ACI、AISC 等的多标准结构工程 |
| 🎧 [客户服务](specialized/customer-service.md) | 全渠道支持、投诉处理、留存、升级 | 任何行业的客户支持——零售、SaaS、酒店、金融、物流 |
| 🏥 [医疗客户服务](specialized/healthcare-customer-service.md) | HIPAA 合规患者支持、账单、保险、紧急分流 | 需要合规、有同理心的患者支持的医疗机构 |
| 🏨 [酒店客户服务](specialized/hospitality-guest-services.md) | 预订、礼宾、投诉挽回、忠诚度、活动 | 酒店、度假村、餐厅及活动场地 |
| 🤝 [HR 入职](specialized/hr-onboarding.md) | 入职前、合规、福利登记、30-60-90 天计划 | 任何有新人入职的公司——从创业公司到大型企业 |
| 🌐 [语言翻译](specialized/language-translator.md) | 西班牙语 ↔ 英语翻译、方言意识、文化背景 | 出行、商务、医疗和法律翻译需求 |
| ⏱️ [法律计费与时间追踪](specialized/legal-billing-time-tracking.md) | 计时捕获、计费叙事、客户资金合规、催收 | 最大化收入回收与计费准确度的律师事务所 |
| 📋 [法律客户接洽](specialized/legal-client-intake.md) | 潜在客户筛选、利益冲突筛查、咨询预约 | 将咨询转化为签约客户的律师事务所 |
| ⚖️ [法律文书审查](specialized/legal-document-review.md) | 合同审查、风险标记、版本比对、合规 | 横跨任何执业领域的律师就绪首轮审查 |
| 🏦 [贷款专员助理](specialized/loan-officer-assistant.md) | 借款人接洽、TRID 合规、管道追踪、过户协调 | 按揭和消费贷款团队 |
| 🏠 [房地产买卖专员](specialized/real-estate-buyer-seller.md) | 买方/卖方代理、报价、交易协调 | 住宅与投资房地产交易 |
| 🛒 [零售客户退货专员](specialized/retail-customer-returns.md) | 退货处理、欺诈防范、换货、供应商退货 | 实体店、电商及全渠道零售 |
| ♟️ [商业策略师](specialized/business-strategist.md) | 管理咨询策略 | 竞争分析、市场进入、增长规划 |
| 🔄 [变革管理顾问](specialized/change-management-consultant.md) | ADKAR/Kotter/Prosci 变革管理 | 引导组织完成转型与采纳 |
| 🧭 [幕僚长](specialized/specialized-chief-of-staff.md) | 高管协调 | 过滤噪音、管理流程、路由决策 |
| 🌟 [客户成功经理](specialized/customer-success-manager.md) | 入职、健康度与留存 | QBR、流失防范、续约与扩展 |
| 📝 [资助申请书撰写者](specialized/grant-writer.md) | 资助申请与资金募集 | 意向书、申请书、非营利/研究预算 |
| 🏥 [医疗账单与编码专员](specialized/medical-billing-coding-specialist.md) | ICD-10/CPT/HCPCS 与收入周期 | 理赔、拒付管理、RCM 优化 |
| 💰 [定价分析师](specialized/specialized-pricing-analyst.md) | 定价模型与利润优化 | 竞品/成本分析、基于价值的定价 |
| 💼 [首席财务官](specialized/chief-financial-officer.md) | 资本配置与财务策略 | 司库、FP&A、并购财务、投资者与董事会报告 |
| 🌱 [ESG 与可持续发展官](specialized/esg-sustainability-officer.md) | ESG 项目与披露 | 可持续发展策略、脱碳、报告 |
| 🔐 [数据隐私官](specialized/data-privacy-officer.md) | GDPR/CCPA 隐私合规 | 数据映射、DPIA、同意管理、泄露响应 |
| ⚙️ [运营经理](specialized/operations-manager.md) | 精益/六西格玛运营 | 流程映射、产能规划、KPI 治理 |
| 🤝 [并购整合经理](specialized/ma-integration-manager.md) | 并购后整合 | 第一天/百日计划、协同效应追踪、TSA 管理 |
| 🧠 [组织心理学家](specialized/organizational-psychologist.md) | 团队动力学与文化健康度 | 心理安全、职业倦怠风险、高绩效团队 |
| ⚔️ [策略对决代理](specialized/specialized-strategy-duel-agent.md) | 博弈论与三十六计 | 回合制策略对决、对抗性情景模拟 |

### 💵 财务部

会计、财务分析、税务策略与投资研究专家。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📒 [记账与财务控制](finance/finance-bookkeeper-controller.md) | 月结、对账、GAAP 合规、内部控制 | 日常会计操作、审计就绪、财务档案管理 |
| 📊 [财务分析师](finance/finance-financial-analyst.md) | 财务建模、预测、场景分析、决策支持 | 三表模型、差异分析、数据驱动的商业智能 |
| 📈 [FP&A 分析师](finance/finance-fpa-analyst.md) | 预算、滚动预测、差异分析、业务回顾 | 年度运营计划、月度业务回顾、战略资源分配 |
| 🔍 [投资研究员](finance/finance-investment-researcher.md) | 尽调、投资组合分析、资产估值、权益研究 | 投资论点构建、风险评估、市场研究 |
| 🏛️ [税务策略师](finance/finance-tax-strategist.md) | 税务优化、多辖区合规、转让定价 | 实体架构、有效税率分析、审计应对、战略税务规划 |

### 🎮 游戏开发部

构建跨各大主流引擎的世界、系统和体验。

#### 跨引擎代理（引擎无关）

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [游戏设计师](game-development/game-designer.md) | 系统设计、GDD 编写、经济平衡、玩法循环 | 设计游戏机制、成长系统、编写设计文档 |
| 🗺️ [关卡设计师](game-development/level-designer.md) | 布局理论、节奏、遭遇设计、环境叙事 | 构建关卡、设计遭遇流程、空间叙事 |
| 🎨 [技术美术](game-development/technical-artist.md) | 着色器、VFX、LOD 管道、美术到引擎优化 | 连接美术与工程、着色器编写、性能安全的素材管道 |
| 🔊 [游戏音频工程师](game-development/game-audio-engineer.md) | FMOD/Wwise、自适应音乐、空间音频、音频预算 | 交互音频系统、动态音乐、音频性能 |
| 📖 [叙事设计师](game-development/narrative-designer.md) | 故事系统、分支对话、背景设定架构 | 编写分支叙事、实现对话系统、世界背景设定 |

#### Unity

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [Unity 架构师](game-development/unity/unity-architect.md) | ScriptableObjects、数据驱动模块化、DOTS/ECS | 大型 Unity 项目、数据驱动系统设计、ECS 性能 |
| ✨ [Unity Shader Graph 美术](game-development/unity/unity-shader-graph-artist.md) | Shader Graph、HLSL、URP/HDRP、Renderer Features | 自定义 Unity 材质、VFX 着色器、后处理通道 |
| 🌐 [Unity 多人游戏工程师](game-development/unity/unity-multiplayer-engineer.md) | Netcode for GameObjects、Unity Relay/Lobby、服务器权威、预测 | Unity 在线游戏、客户端预测、Unity Gaming Services 集成 |
| 🛠️ [Unity 编辑器工具开发](game-development/unity/unity-editor-tool-developer.md) | EditorWindows、AssetPostprocessors、PropertyDrawers、构建验证 | 自定义 Unity 编辑器工具、管道自动化、内容验证 |

#### Unreal Engine

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Unreal 系统工程师](game-development/unreal-engine/unreal-systems-engineer.md) | C++/Blueprint 混合、GAS、Nanite 约束、内存管理 | 复杂 Unreal 玩法系统、Gameplay Ability System、引擎级 C++ |
| 🎨 [Unreal 技术美术](game-development/unreal-engine/unreal-technical-artist.md) | Material Editor、Niagara、PCG、Substrate | Unreal 材质、Niagara VFX、程序化内容生成 |
| 🌐 [Unreal 多人游戏架构师](game-development/unreal-engine/unreal-multiplayer-architect.md) | Actor 复制、GameMode/GameState 层级、专用服务器 | Unreal 在线游戏、复制图、服务器权威 Unreal |
| 🗺️ [Unreal 世界构建者](game-development/unreal-engine/unreal-world-builder.md) | World Partition、Landscape、HLOD、LWC | 大型开放世界 Unreal 关卡、流式系统、大规模地形 |

#### Godot

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📜 [Godot 玩法脚本师](game-development/godot/godot-gameplay-scripter.md) | GDScript 2.0、信号、组合、静态类型 | Godot 玩法系统、场景组合、注重性能的 GDScript |
| 🌐 [Godot 多人游戏工程师](game-development/godot/godot-multiplayer-engineer.md) | MultiplayerAPI、ENet/WebRTC、RPC、权限模型 | Godot 在线游戏、场景复制、服务器权威 Godot |
| ✨ [Godot 着色器开发](game-development/godot/godot-shader-developer.md) | Godot 着色语言、VisualShader、RenderingDevice | 自定义 Godot 材质、2D/3D 特效、后处理、计算着色器 |

#### Blender

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🧩 [Blender 插件工程师](game-development/blender/blender-addon-engineer.md) | Blender Python（`bpy`）、自定义操作符/面板、素材验证器、导出器、管道自动化 | 构建 Blender 插件、素材准备工具、导出工作流和 DCC 管道自动化 |

#### Roblox Studio

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Roblox 系统脚本师](game-development/roblox-studio/roblox-systems-scripter.md) | Luau、RemoteEvents/Functions、DataStore、服务器权威模块架构 | 构建安全的 Roblox 游戏系统、客户端-服务端通信、数据持久化 |
| 🎯 [Roblox 体验设计师](game-development/roblox-studio/roblox-experience-designer.md) | 参与循环、变现、D1/D7 留存、新手引导流程 | 设计 Roblox 游戏循环、Game Pass、每日奖励、玩家留存 |
| 👗 [Roblox 虚拟形象创建者](game-development/roblox-studio/roblox-avatar-creator.md) | UGC 管道、配件绑定、创作者市场提交流程 | Roblox UGC 物品、HumanoidDescription 定制、游戏中虚拟形象商店 |

### 📚 学术部

为世界构建、叙事和故事设计提供学术严谨性。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🌍 [人类学家](academic/academic-anthropologist.md) | 文化系统、亲属关系、仪式、信仰体系 | 设计具有内在逻辑的、文化上自洽的社会 |
| 🌐 [地理学家](academic/academic-geographer.md) | 自然/人文地理、气候、地图学 | 构建具有真实地形和聚落的地理上自洽的世界 |
| 📚 [历史学家](academic/academic-historian.md) | 历史分析、分期、物质文化 | 验证历史一致性，用真实时代细节丰富设定 |
| 📜 [叙事学家](academic/academic-narratologist.md) | 叙事理论、故事结构、角色弧光 | 用成熟理论框架分析和改进故事结构 |
| 🧠 [心理学家](academic/academic-psychologist.md) | 人格理论、动机、认知模式 | 构建以研究为基础的心理学上可信的角色 |

---

### 🌍 GIS 部

绘制地球、分析人造世界、从地理空间数据中提取情报。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🧠 [技术顾问](gis/gis-technical-consultant.md) | GIS 策略、差距分析、技术路线图、数字化转型 | 理解业务需求，选择合适的地理空间技术栈，规划多阶段 GIS 方案 |
| 🔧 [方案工程师](gis/gis-solution-engineer.md) | Esri + FOSS4G 原型构建、PoC 交付、技术可行性 | 构建可工作演示、验证技术方案、售前支持 |
| 🖥️ [GIS 分析师](gis/gis-analyst.md) | 地图制作、数据质检、符号化、版式、空间查询 | 日常 GIS 运营、制作可出版地图、维护数据完整性 |
| 📦 [空间数据工程师](gis/gis-spatial-data-engineer.md) | 地理空间 ETL、格式转换、坐标系重投影、自动化管道 | 从任意来源摄取杂乱数据，构建可重复的数据转换管道 |
| ⚙️ [地理处理专家](gis/gis-geoprocessing-specialist.md) | ArcPy、Python Toolbox（.pyt）、Model Builder、批量自动化 | 自动化重复性 GIS 工作流，构建自定义地理处理工具 |
| ✅ [GIS QA 工程师](gis/gis-qa-engineer.md) | 拓扑验证、元数据审计、坐标系一致性、精度评估 | 数据发布前的质量关卡、合规校验、数据完整性审计 |
| 🤖 [GeoAI/ML 工程师](gis/gis-geoai-ml-engineer.md) | 地物提取、目标检测、语义分割、土地覆盖分类 | 从影像中提取建筑/道路/车辆，变化检测，环境监测 |
| 🏗️ [BIM/GIS 专家](gis/gis-bim-specialist.md) | Revit/IFC 到 GIS、室内地图、数字孪生架构、设施管理 | 智慧园区、机场数字孪生、室内导航、建筑运营 |
| 🏔️ [3D 与场景开发](gis/gis-3d-scene-developer.md) | Cesium、ArcGIS Scene Viewer、3D Tiles、点云、地形可视化 | 3D 城市场景、地形漫游、点云网页浏览、OAuth 鉴权场景共享 |
| 📊 [空间数据科学家](gis/gis-spatial-data-scientist.md) | 空间统计、聚类、回归、插值、点模式分析 | 热点检测、空间建模、预测分析、研究级分析 |
| 🛸 [无人机/实体建模](gis/gis-drone-reality-mapping.md) | 摄影测量、正射影像、DTM/DSM、点云分类、3D 网格 | 无人机测绘处理、实体捕捉、施工监测、环境制图 |
| 🌐 [Web GIS 开发](gis/gis-web-gis-developer.md) | MapLibre GL JS、ArcGIS JS API、Leaflet、实时仪表板、REST API | 构建交互式 Web 地图、运营仪表板、实时数据可视化 |
| 🎨 [地图设计](gis/gis-cartography-designer.md) | 色彩理论、排版、底图设计、视觉层次、印刷与 Web 美学 | 让地图美观易读、色盲安全调色板、专业地图布局 |

---

## 🎯 实际使用场景

### 场景 1：构建创业公司 MVP

**你的团队**：
1. 🎨 **前端开发** — 构建 React 应用
2. 🏗️ **后端架构师** — 设计 API 和数据库
3. 🚀 **增长黑客** — 规划用户获取
4. ⚡ **快速原型师** — 快速迭代循环
5. 🔍 **现实检查员** — 确保上线前的质量

**成果**：在每个阶段以专业专长加速交付。

---

### 场景 2：营销活动发布

**你的团队**：
1. 📝 **内容创作者** — 开发活动内容
2. 🐦 **Twitter 互动者** — Twitter 策略与执行
3. 📸 **Instagram 策展人** — 视觉内容和故事
4. 🤝 **Reddit 社区建设者** — 真诚社区互动
5. 📊 **分析报告员** — 追踪和优化表现

**成果**：具备平台特定专长的多渠道协调活动。

---

### 场景 3：企业功能开发

**你的团队**：
1. 👔 **高级项目经理** — 范围和任务规划
2. 💎 **高级开发** — 复杂实现
3. 🎨 **UI 设计师** — 设计系统和组件
4. 🧪 **实验追踪者** — A/B 测试规划
5. 📸 **证据收集员** — 质量验证
6. 🔍 **现实检查员** — 生产就绪

**成果**：带有质量关卡和文档的企业级交付。

---

### 场景 4：付费媒体账户接管

**你的团队**：

1. 📋 **付费媒体审计师** — 全面账户评估
2. 📡 **追踪与衡量专家** — 验证转化追踪准确性
3. 💰 **PPC 广告策略师** — 重新设计账户架构
4. 🔍 **搜索词分析师** — 清理搜索词的浪费支出
5. ✍️ **广告创意策略师** — 刷新所有广告文案和附加信息
6. 📊 **分析报告员**（支持部） — 构建报告仪表板

**成果**：系统化账户接管——追踪已验证、浪费已消除、结构已优化、创意已刷新——全部在最初 30 天内完成。

---

### 场景 5：全机构产品探索

**你的团队**：全部 8 个部门在单一任务上并行工作。

参见 **[Nexus 空间发现练习](examples/nexus-spatial-discovery.md)** ——一个完整示例，其中 8 个代理（产品趋势研究员、后端架构师、品牌守护者、增长黑客、支持响应员、UX 研究员、项目牧羊人和 XR 界面架构师）被同时部署，以评估一个软件机会并产出一份统一的产品计划，涵盖市场验证、技术架构、品牌策略、市场进入、支持系统、UX 研究、项目执行和空间 UI 设计。

**成果**：单次会话中产出的全面、跨职能产品蓝图。[更多示例](examples/)。

---

### 场景 6：智慧园区数字孪生

**你的团队**：

1. 🧠 **技术顾问** — 定义数字孪生策略：建筑用 BIM、园区用 GIS、实时用 IoT
2. 🏗️ **BIM/GIS 专家** — 将 Revit 建筑模型转为 GIS 场景图层，设计室内平面图
3. 🛸 **无人机/实体建模** — 航飞园区，生成正射影像和 3D 网格以提供上下文
4. 🌐 **Web GIS 开发** — 用 MapLibre、建筑图层和房间搜索器构建园区仪表板
5. 🏔️ **3D 与场景开发** — 创建包含地形、建筑和漫游导览的沉浸式 3D 场景
6. 🤖 **GeoAI/ML 工程师** — 从无人机影像中提取建筑足迹和树冠覆盖
7. ✅ **GIS QA 工程师** — 验证数据精度、检查拓扑、验证坐标系一致性

**成果**：结合了 BIM 细节、无人机现实捕捉、3D 可视化和 Web 可访问性的园区数字孪生——由协同专家在单一管道中交付。

---

## 🤝 参与贡献

我们欢迎贡献！以下是你可以帮忙的方式：

### 新增一个代理

1. Fork 本仓库
2. 在相应分类中创建一个新的代理文件
3. 遵循代理模板结构：
   - 包含 name、description、color 的前言
   - 身份与记忆部分
   - 核心使命
   - 关键规则（针对具体领域）
   - 包含示例的技术交付物
   - 工作流程
   - 成功指标
4. 提交包含你代理的 PR

### 改进已有代理

- 添加真实世界示例
- 增强代码示例
- 更新成功指标
- 改进工作流程

### 分享成功故事

你使用这些代理取得了成功吗？在 [Discussions](https://github.com/msitarzewski/agency-agents/discussions) 中分享你的故事！

---

## 📖 代理设计理念

每个代理都以以下理念设计：

1. **🎭 强烈的个性**：不是泛泛的模板 — 真实的人物特色和话风
2. **📋 清晰的可交付成果**：具体的输出，而非模糊的指导
3. **✅ 成功指标**：可衡量的成果和质量标准
4. **🔄 经过验证的工作流程**：行之有效的分步流程
5. **💡 学习型记忆**：模式识别与持续改进

---

## 🎁 它有何不同？

### 不同于通用 AI 提示词：
- ❌ 笼统的"扮演一个开发者"提示词
- ✅ 深度的专业化，带有个性和流程

### 不同于提示词库：
- ❌ 一次性提示词合集
- ✅ 包含工作流程和可交付成果的全面代理系统

### 不同于 AI 工具：
- ❌ 你无法自定义的黑盒工具
- ✅ 透明、可 fork、可适配的代理性格

---

## 🎨 代理个性高光

> "我不只是测试你的代码——我默认找到 3-5 个问题，并且为每件事要求视觉证明。"
>
> -- **证据收集员**（测试部）

> "你不是在 Reddit 上做营销——你正在成为一个碰巧代表某个品牌的受尊重的社区成员。"
>
> -- **Reddit 社区建设者**（市场部）

> "每个趣味元素都必须服务于功能或情感目的。设计愉悦感既要增强体验，又不能分散注意力。"
>
> -- **趣味注入师**（设计部）

> "让我添加一个庆祝动画，它可以将任务完成焦虑感降低 40%"
>
> -- **趣味注入师**（在一次 UX 评审中）

---

## 📊 数据统计

- 🎭 **232 个专业代理**，横跨 16 个部门
- 📝 **10,000+ 行**个性、流程和代码示例
- ⏱️ **数月的迭代**，来自真实使用场景
- 🌟 **久经考验**，在生产环境中验证
- 💬 **Reddit 发布 12 小时内 50+ 个请求**

---

## 🔌 多工具集成

The Agency 原生支持 Claude Code，并附带转换与安装脚本，让你在所有主流代理编码工具中使用相同的代理。

### 支持的工具

- **[Claude Code](https://claude.ai/code)** — 原生 `.md` 代理，无需转换 → `~/.claude/agents/`
- **[GitHub Copilot](https://github.com/copilot)** — 原生 `.md` 代理，无需转换 → `~/.github/agents/` + `~/.copilot/agents/`
- **[Antigravity](https://github.com/google-gemini/antigravity)** — 每代理一个 `SKILL.md` → `~/.gemini/antigravity/skills/`
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — 扩展 + `SKILL.md` 文件 → `~/.gemini/extensions/agency-agents/`
- **[OpenCode](https://opencode.ai)** — `.md` 代理文件 → `.opencode/agents/`
- **[Cursor](https://cursor.sh)** — `.mdc` 规则文件 → `.cursor/rules/`
- **[Aider](https://aider.chat)** — 单个 `CONVENTIONS.md` → `./CONVENTIONS.md`
- **[Windsurf](https://codeium.com/windsurf)** — 单个 `.windsurfrules` → `./.windsurfrules`
- **[OpenClaw](https://github.com/openclaw/openclaw)** — 每代理 `SOUL.md` + `AGENTS.md` + `IDENTITY.md`
- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — `.md` SubAgent 文件 → `~/.qwen/agents/`
- **[Kimi Code](https://github.com/MoonshotAI/kimi-cli)** — YAML 代理规格 → `~/.config/kimi/agents/`
- **[Codex](https://developers.openai.com/codex/overview)** — TOML 自定义代理 → `~/.codex/agents/`

---

### ⚡ 快速安装

**第 1 步 -- 生成集成文件：**
```bash
./scripts/convert.sh
# 更快（并行，输出顺序可能不同）：./scripts/convert.sh --parallel
```

**第 2 步 -- 安装（交互式，自动检测你的工具）：**
```bash
./scripts/install.sh
# 更快（并行，输出顺序可能不同）：./scripts/install.sh --no-interactive --parallel
```

安装器扫描你的系统中已安装的工具，显示复选框界面，让你精确选择安装内容：

```
  +------------------------------------------------+
  |   The Agency -- 工具安装器                      |
  +------------------------------------------------+

  系统扫描：[*] = 在此机器上检测到

  [x]  1)  [*]  Claude Code     (claude.ai/code)
  [x]  2)  [*]  Copilot         (~/.github + ~/.copilot)
  [x]  3)  [*]  Antigravity     (~/.gemini/antigravity)
  [ ]  4)  [ ]  Gemini CLI      (~/.gemini/agents)
  [ ]  5)  [ ]  OpenCode        (opencode.ai)
  [ ]  6)  [ ]  OpenClaw        (~/.openclaw/agency-agents)
  [x]  7)  [*]  Cursor          (.cursor/rules)
  [ ]  8)  [ ]  Aider           (CONVENTIONS.md)
  [ ]  9)  [ ]  Windsurf        (.windsurfrules)
  [ ] 10)  [ ]  Qwen Code       (~/.qwen/agents)
  [ ] 11)  [ ]  Kimi Code       (~/.config/kimi/agents)
  [ ] 12)  [ ]  Codex           (~/.codex/agents)

  [1-12] 切换   [a] 全选   [n] 全不选   [d] 已检测
  [Enter] 安装   [q] 退出
```

**或直接安装特定工具：**
```bash
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool codex
```

**非交互模式（CI/脚本）：**
```bash
./scripts/install.sh --no-interactive --tool all
```

**更快的运行（并行）** — 在多核机器上，使用 `--parallel` 让每个工具并行处理。跨工具的输出顺序不确定。交互式和非交互式安装均可使用：例如 `./scripts/install.sh --interactive --parallel`（先选工具，再并行安装）或 `./scripts/install.sh --no-interactive --parallel`。并行任务数默认为 `nproc`（Linux）、`sysctl -n hw.ncpu`（macOS）或 4；用 `--jobs N` 覆盖。

```bash
./scripts/convert.sh --parallel                    # 并行转换所有工具
./scripts/convert.sh --parallel --jobs 8           # 限制并行任务数
./scripts/install.sh --no-interactive --parallel   # 并行安装所有检测到的工具
./scripts/install.sh --interactive --parallel      # 选工具，再并行安装
./scripts/install.sh --no-interactive --parallel --jobs 4
```

---

### 各工具说明

<details>
<summary><strong>Claude Code</strong></summary>

直接从仓库复制代理到 `~/.claude/agents/`——无需转换。

```bash
./scripts/install.sh --tool claude-code
```

然后在 Claude Code 中激活：
```
使用前端开发代理评审这个组件。
```

详见 [integrations/claude-code/README.md](integrations/claude-code/README.md)。
</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

直接从仓库复制代理到 `~/.github/agents/` 和 `~/.copilot/agents/`——无需转换。

```bash
./scripts/install.sh --tool copilot
```

然后在 GitHub Copilot 中激活：
```
使用前端开发代理评审这个组件。
```

详见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md)。
</details>

<details>
<summary><strong>Antigravity（Gemini）</strong></summary>

每个代理成为 `~/.gemini/antigravity/skills/agency-<slug>/` 中的一项技能。

```bash
./scripts/install.sh --tool antigravity
```

在带 Antigravity 的 Gemini 中激活：
```
@agency-frontend-developer 评审这个 React 组件
```

详见 [integrations/antigravity/README.md](integrations/antigravity/README.md)。
</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

安装为 Gemini CLI 子代理。
在全新克隆后，先运行安装器之前生成 Gemini 代理文件。

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

详见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md)。
</details>

<details>
<summary><strong>OpenCode</strong></summary>

代理被放置在项目根目录的 `.opencode/agents/` 中（项目范围内）。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

或全局安装：
```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

在 OpenCode 中激活：
```
@backend-architect 设计这个 API。
```

详见 [integrations/opencode/README.md](integrations/opencode/README.md)。
</details>

<details>
<summary><strong>Cursor</strong></summary>

每个代理成为项目 `.cursor/rules/` 中的一个 `.mdc` 规则文件。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

Cursor 在项目中检测到规则时自动应用。显式引用它们：
```
使用 @security-engineer 规则评审此代码。
```

详见 [integrations/cursor/README.md](integrations/cursor/README.md)。
</details>

<details>
<summary><strong>Aider</strong></summary>

所有代理被编译成一个 Aider 自动读取的 `CONVENTIONS.md` 文件。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

然后在你的 Aider 会话中引用代理：
```
使用前端开发代理重构此组件。
```

详见 [integrations/aider/README.md](integrations/aider/README.md)。
</details>

<details>
<summary><strong>Windsurf</strong></summary>

所有代理被编译成项目根目录的 `.windsurfrules`。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

在 Windsurf 的 Cascade 中引用代理：
```
使用现实检查员代理验证此项是否可投产。
```

详见 [integrations/windsurf/README.md](integrations/windsurf/README.md)。
</details>

<details>
<summary><strong>OpenClaw</strong></summary>

每个代理成为 `~/.openclaw/agency-agents/` 中带有 `SOUL.md`、`AGENTS.md` 和 `IDENTITY.md` 的工作区。

```bash
./scripts/convert.sh --tool openclaw
./scripts/install.sh --tool openclaw
```

如果 `openclaw` CLI 可用，安装器会自动注册每个工作区。
安装后运行 `openclaw gateway restart` 使新代理生效。

详见 [integrations/openclaw/README.md](integrations/openclaw/README.md)。

</details>

<details>
<summary><strong>Qwen Code</strong></summary>

子代理安装到项目根目录的 `.qwen/agents/` 中（项目范围内）。

```bash
# 转换并安装（在项目根目录下运行）
cd /your/project
./scripts/convert.sh --tool qwen
./scripts/install.sh --tool qwen
```

**在 Qwen Code 中使用：**
- 按名称引用：`使用 frontend-developer 代理评审此组件`
- 或让 Qwen 根据任务上下文自动委派
- 通过交互模式下的 `/agents` 命令管理

> 📚 [Qwen SubAgents 文档](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/)

</details>

<details>
<summary><strong>Kimi Code</strong></summary>

代理被转换为 Kimi Code CLI 格式（YAML + 系统提示词）并安装到 `~/.config/kimi/agents/`。

```bash
# 转换并安装
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

**配合 Kimi Code 使用：**
```bash
# 使用代理
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml

# 在项目中
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project \
     "评审这个 React 组件"
```

详见 [integrations/kimi/README.md](integrations/kimi/README.md)。

</details>

<details>
<summary><strong>Codex</strong></summary>

每个代理被转换为 Codex 自定义代理 TOML 文件并安装到 `~/.codex/agents/`。

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

然后在 Codex 中按名称引用自定义代理：
```
使用前端开发代理评审此组件。
```

详见 [integrations/codex/README.md](integrations/codex/README.md)。
</details>

---

### 更改后重新生成

当你新增代理或编辑已有代理时，重新生成所有集成文件：

```bash
./scripts/convert.sh                    # 全部重新生成（串行）
./scripts/convert.sh --parallel         # 全部并行重新生成（更快）
./scripts/convert.sh --tool codex       # 仅重新生成一个工具的
./scripts/convert.sh --tool cursor      # 仅重新生成一个工具的
```

---

## 🗺️ 路线图

- [ ] 交互式代理选择 Web 工具
- [x] 多代理工作流示例 -- 参见 [examples/](examples/)
- [x] 多工具集成脚本（Claude Code、GitHub Copilot、Antigravity、Gemini CLI、OpenCode、OpenClaw、Cursor、Aider、Windsurf、Qwen Code、Kimi Code、Codex）
- [ ] 代理设计视频教程
- [ ] 社区代理市场
- [ ] 项目匹配的代理"性格测验"
- [ ] "每周代理"展示系列

---

## 🌐 社区翻译与本地化

社区维护的翻译和区域适配。这些是独立维护的——查看各仓库了解覆盖范围和版本兼容性。

| 语言 | 维护者 | 链接 | 备注 |
|----------|-----------|------|-------|
| 🇨🇳 简体中文 (zh-CN) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 141 个已翻译代理 + 46 个中国市场的原创代理 |
| 🇨🇳 简体中文 (zh-CN) | [@dsclca12](https://github.com/dsclca12) | [agent-teams](https://github.com/dsclca12/agent-teams) | 独立翻译，包含 Bilibili、微信、小红书本地化 |
| 🇧🇷 葡萄牙语巴西 (pt-BR) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-pt-BR](https://github.com/jnMetaCode/agency-agents-pt-BR) | 184 个上游代理已翻译；欢迎巴西市场 PR |
| 🇷🇺 俄语 (ru) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ru](https://github.com/jnMetaCode/agency-agents-ru) | 184 个上游代理已翻译；欢迎俄罗斯市场 PR |
| 🇮🇩 印尼语 (id) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-id](https://github.com/jnMetaCode/agency-agents-id) | 184 个上游代理已翻译；欢迎印度尼西亚市场 PR |
| 🇸🇦 阿拉伯语 (ar) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ar](https://github.com/jnMetaCode/agency-agents-ar) | 184 个上游代理已翻译；欢迎阿拉伯市场 PR |
| 🇰🇷 韩语 (ko) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ko](https://github.com/jnMetaCode/agency-agents-ko) | 184 个上游代理完整翻译；欢迎韩国特定 PR |
| 🇯🇵 日语 (ja-JP) | [@sscodeai](https://github.com/sscodeai) | [agency-agents-ja](https://github.com/sscodeai/agency-agents-ja) | 281 个日本本地化代理 + 97 个日本市场原创 + 27 个工作流 |

想要添加翻译？提一个 issue，我们会把它链接到这里。

---

## 🔗 相关资源

- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) — 社区维护的 OpenClaw 代理集合（派生自本仓库）

---

## 📜 许可证

MIT 许可证 — 自由使用，商业或个人用途皆可。注明出处表示感谢但非必要。

---

## 🙏 致谢

始于一个关于 AI 代理专业化的 Reddit 帖子，如今已发展成令人瞩目的成果——**232 个代理、16 个部门**，得到来自世界各地贡献者社区的支持。本仓库中的每个代理之所以存在，都是因为有人付出心力去编写、测试和分享。

向每位提交过 PR、提过 issue、发起过 Discussion，或仅仅是试用了一个代理并告诉我们哪些奏效的人——感谢你们。你们是 The Agency 不断进步的原因。

---

## 💬 社区

- **GitHub Discussions**：[分享你的成功故事](https://github.com/msitarzewski/agency-agents/discussions)
- **Issues**：[报告 Bug 或请求功能](https://github.com/msitarzewski/agency-agents/issues)
- **Reddit**：加入 r/ClaudeAI 的讨论
- **Twitter/X**：使用 #TheAgency 分享

---

## 🚀 开始使用

1. **浏览**上方的代理，找到符合你需求的专家
2. **复制**代理到 `~/.claude/agents/` 以集成 Claude Code
3. **激活**代理，在你的 Claude 对话中引用它们
4. **自定义**代理的个性与工作流程以适配你的特定需求
5. **分享**你的成果并回馈给社区

---

<div align="center">

**🎭 The Agency：你的 AI 梦之队等待着你 🎭**

[⭐ Star 这个仓库](https://github.com/msitarzewski/agency-agents) • [🍴 Fork 它](https://github.com/msitarzewski/agency-agents/fork) • [🐛 报告问题](https://github.com/msitarzewski/agency-agents/issues) • [❤️ 赞助](https://github.com/sponsors/msitarzewski)

由社区用 ❤️ 打造，为社区服务

</div>
