# 🎯 12-Week Navigator: AI-Native Strategic Management Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version: v2.1-flagship](https://img.shields.io/badge/Version-v2.1--flagship-blueviolet.svg)](#)
[![Methodology: 12-Week Year](https://img.shields.io/badge/Methodology-12--Week--Year-success.svg)](#)

> **Elevate your execution from survival to strategy. A zero-footprint, AI-collaborative cockpit for the 12 Week Year methodology.**

## 🌟 為什麼選擇 12-Week Navigator？

在「AI 代理 (Agentic Workflow)」的時代，我們不需要更多的筆記軟體，我們需要的是一個能與 AI 深度協作的**執行引擎**。

本專案將著名的 **「12 週計畫 (The 12 Week Year)」** 方法論轉化為一套模組化的 AI 技能組。它不只是記錄你的習慣，更是你的戰略分析師、失敗學教練與視覺化報表組長。

---

## 🔥 核心亮點 (Key Features)

- **🤖 AI-Native Interaction**: 專為 Antigravity/Cursor 等代理設計的單一指令入口 (`/12-week-navigator`)。
- **📦 Modular Architecture**: 100% 邏輯與數據分離。核心引擎封裝於 `.agent/skills/`，數據完全自主掌控。
- **📊 Interactive Visualizer**: 內建 `ui-ux-pro-max` 引擎，產出具備 React/Tailwind/Framer Motion 質感的互動式 glassmorphism 報表。
- **🛡️ Sandbox Safety**: 內建 A/B/C 三模式隔離測試沙盒，在不污染正式數據的情況下模擬任何執行場景。
- **🧠 Strategic Alignment**: 自動執行 JIT (Just-In-Time) 校驗，從日誌、週報到月度戰略目標進行精準勾稽。

---

## 📂 系統架構 (Architecture)

模組化封裝確保了系統的潔淨與極致的可攜性：

```bash
.
├── .agent/
│   ├── instructions.md         # 🧠 AI 核心行為準則
│   ├── workflows/              # 🚀 任務指令傳送門
│   └── skills/
│       └── 12-week-navigator/  # 📦 旗艦模組核心包
│           ├── logic/          # Init, Start, Report... 核心邏輯
│           ├── lib/            # ui-ux-pro-max 視覺化引擎
│           ├── resources/      # 配置範本庫
│           └── workspace/      # 🔐 資料特區 (Data Area)
│               ├── config/     # 戰略配置
│               ├── data/       # 執行紀錄 (Markdown)
│               ├── reports/    # 自動化視覺化報表
│               └── sandbox/    # 隔離實驗場
└── README.md
```

---

## 🚀 快速上手 (Quick Start)

### 1. 複製並建立環境
```bash
git clone https://github.com/liwenchiou/12-week-navigator.git
cd 12-week-navigator
```

### 2. 初始化核心配置
從 `resources/samples/` 複製範本到 `workspace/config/`，並依個人需求修改：
- `核心習慣.md` (KPIs)
- `週計畫.md` (Weekly Strategy)
- `月計畫.md` (Milestones)

### 3. 喚醒 AI 指揮塔
在您的 AI 助理 (Antigravity / Cursor Agent) 中輸入：
> **「執行 /12-week-navigator」**

系統將呈現旗艦模組選單，指引您完成初始化預檢。

---

## 📈 視覺化產出 (Visual Showcase)

系統會根據你的 Markdown 日誌，自動產出具備專業設計感的 HTML 報表。包含：
- **12 週戰略進度條**
- **行為熱點矩陣**
- **失敗阻礙分析 (Action Bias Analysis)**
- **進化對策卡片**

---

## 💻 技術棧 (Technology Stack)

- **AI Logic**: Agentic Skill Templates (Instruction Tuning Ready)
- **Frontend**: React 18 / Tailwind CSS / Framer Motion
- **Management**: Git / Markdown / Python 3 (Visualization Engine)

---

## 🤝 參與貢獻 (Contributing)

這是一個由開發者為開發者設計的工具。如果你有更好的美學提案或邏輯優化，歡迎提交 PR。

1. Fork 本專案
2. 建立您的特性分支 (`git checkout -b feat/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送至分支 (`git push origin feat/AmazingFeature`)
5. 開啟 Pull Request

---

## 📜 授權條款 (License)

Distributed under the **MIT License**. See `LICENSE` for more information.

---
*Built with ❤️ for High-Output Engineers.*
