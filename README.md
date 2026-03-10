# 🎯 12-Week Goal Management System

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **A self-hosted, AI-collaborative framework for high-output lifecycle management.**

本專案是一套基於 **12 週計畫 (The 12 Week Year)** 方法論建構的個人管理系統。透過 AI 助理 **Antigravity** 的自動化處理，將繁瑣的紀錄流程轉化為結構化的數據、失敗學分析與沉浸式視覺回顧。旨在為追求卓越的開發者提供一套穩定、具戰略深度且視覺精美的成長指揮塔。

---

## 🛠️ 核心設計理念 (Core Methodology)

本系統的核心在於「意圖、執行與反思」的完全導航，並引入 AI 作為深度戰略夥伴：

- **配置化治理 (Config-as-Strategy)**：將習慣、週計畫、月計畫定義於配置檔中，建立明確的目標層級構建。
- **數據全紀錄 (Deep Analytics)**：除了基礎習慣，更引入 **能量/情緒指標 (Energy Index)** 與 **資源工具庫 (Resource Repo)**。
- **失敗學反思 (Pivots & Countermeasures)**：自動分析未達成項目的阻礙與偏差，將挫折轉化為具體的下一週進化對策。
- **沉浸式視覺化 (Visual IQ)**：自動生成具備頂尖設計感的互動式 Web 報表，整合 12 週總進度條與戰略獲益展示。

---

## 📂 系統架構 (Directory Structure)

專案結構遵循**模組化封裝 (Skill Encapsulation)** 原則，所有邏輯與數據完整收納於 `.agent/skills/12-week-navigator/` 之中：

```bash
.
├── .agent/
│   ├── instructions.md         # 🧠 AI 核心行為準則
│   ├── workflows/
│   │   └── 12-week-navigator.md  # 🚀 系統唯一旗艦入口（五大模組選單）
│   └── skills/
│       └── 12-week-navigator/    # 📦 完整封裝套件
│           ├── SKILL.md          # 核心引擎與協定
│           ├── logic/            # 模組邏輯：init, start, report-guide, habit-fixer, skill-tester
│           ├── lib/
│           │   └── ui-ux-pro-max/  # 🎨 視覺化引擎（內部依賴）
│           ├── resources/
│           │   └── samples/      # 配置範本 (config 初始化用)
│           └── workspace/
│               ├── config/       # ⚙️ 使用者戰略配置
│               ├── data/         # 📝 執行數據 (daily/weekly/monthly)
│               ├── reports/      # 📊 自動生成 HTML 報表
│               └── sandbox/      # 🧪 隔離測試沙盒
├── CHANGELOG.md
└── README.md
```

---

## 📖 使用範例 (Interaction Examples)

### 場景 A：每日夜間追蹤 (Daily Tracker)
> **User**: 「幫我紀錄今日習慣。」  
> **Antigravity**: 「好的，已讀取 `核心習慣.md`。今天飲水有過 3000ml 嗎？另外，今天給自己的『能量狀態』打幾分？(1-5)」  
> **User**: 「有，全部達成，能量 4 分。今天領悟到 React Hook 的閉包原理。」  
> **產出**: 自動在 `workspace/data/daily/` 生成包含能量指標與技術收穫的 Markdown 日誌。

### 場景 B：週日戰略評估 (Weekly Appraisal)
> **User**: 「產出本週週報。」  
> **Antigravity**: 「掃描到『飛輪運動 2 次』未完成。請問是阻礙的原因是？另外本週有發現推薦的工具嗎？」  
> **User**: 「工作太累，下週會調整。另外推薦這個 AI 工具：xxx。」  
> **產出**: 生成週報並包含 **「🚧 阻礙分析」** 與 **「🔗 資源清單」**，並自動發送 Git PR 紀錄變更。

### 場景 C：月度視覺化演說 (Monthly Visualizer)
> **User**: 「幫我產出 2 月份總結網頁。」  
> **Antigravity**: 「分析本月數據完成。二月核心標語建議為『守護者進化』。正在將戰略進度條與進化對策卡片封裝至網頁中...」  
> **產出**: 在 `workspace/reports/` 生成具備毛玻璃發光質感與 12 週進度勾稽的互動式 HTML 檔案。

---

## 🚀 快速上手 (Quick Start)

### 1. 環境需求 (Prerequisites)
在開始之前，請確保您的系統已安裝以下工具：
- **Git 2.x**: 基礎版本控制工具。
- **GitHub CLI (gh)**: **強烈建議**，用於讓 Agent 自動發送及管理 Pull Request。
- **現代化瀏覽器**: 用於渲染互動式 HTML 報表。

### 2. 複製專案與初始化
```bash
# 複製專案
git clone https://github.com/<YOUR_USERNAME>/12-week-navigator.git
cd 12-week-navigator

# 登入 GitHub CLI (以啟用自動 PR 功能)
gh auth login
```

### 3. 初始化計畫 (Config Setup)
複製 `resources/samples/` 中的範本到 `workspace/config/`：
```bash
cp .agent/skills/12-week-navigator/resources/samples/核心習慣_sample.md \
   .agent/skills/12-week-navigator/workspace/config/核心習慣.md
# 同樣複製 週計畫_sample.md 與 月計畫_sample.md
```
接著編輯這三份配置檔，填入您的個人目標。

### 4. 開始導航 (First Run)
在您的 AI 助理 (Antigravity / Cursor Agent 等) 中輸入：

> **「執行 /12-week-navigator」**

系統將呈現五大功能模組選單，引導您開始第一次紀錄。

---

## 🗺️ 指令速查 (Command Reference)

所有功能透過 **單一旗艦入口** 進行導航：

| 輸入指令 | 功能 |
| :--- | :--- |
| `執行 /12-week-navigator` | 開啟五大模組選單（推薦入口）|
| `執行初始化` / `Init` | 環境檢查、目錄建立、格式校準 |
| `啟動導航` / `Start` | 喚醒 Agent、查看進度、今日行動 |
| `紀錄今天` | 啟動每日習慣紀錄 |
| `產出週報` | 生成本週週度復盤報告 |
| `執行月度總結` | 生成月度戰略報告 |
| `產出網頁` / `視覺化` | 生成互動式 HTML 月報網頁 |
| `補記` / `Fix` | 補填過去日期的遺漏紀錄 |
| `啟動測試` / `Test` | 進入隔離沙盒測試模式 |

---

## 🔥 核心特性與優勢 (Core Features)

### 1. 互動式熱點與能量追蹤
系統不僅引導習慣紀錄，更關注 **「當下狀態」**。透過能量情緒指標與資源工具紀錄，讓日誌同時具備「狀態監測器」與「知識採集器」的功能。

### 2. 失敗學分析 (Action Bias Analysis)
針對「未達成」的計畫，Agent 會主動啟動「阻礙分析」流程，並在週報中自動提出 **「進化對策卡片」**。

### 3. 戰略進度勾稽 (Strategic Alignment)
在月報中，系統會自動比對 12 週的總計畫里程碑，確保您在關注當下成長時，也能精準掌握長期位置。

### 4. JIT 階層化校驗 (Just-In-Time Validation)
採用「即時觸發」數據校驗策略：**週報時只掃當週 7 天、月報時只掃當月週報、網頁時只確認月報 MD**。極大化 Token 節省效率。

### 5. 三模式隔離測試沙盒 (Sandbox Safety)
內建 **A / B / C 三模式**測試門戶，在 `workspace/sandbox/` 中安全演練，絕不污染正式數據。

### 6. Git 自動化管理 (Git Manager Skill)
內建標準化 Git 工作法，Agent 自動建立分支、撰寫**繁體中文條列式 Commit**，並透過 GitHub CLI 自動發送 Pull Request。

---

## 💻 技術棧 (Technology Stack)

- **邏輯引擎**: AI Agent (基於 Antigravity 核心技能模組)
- **視覺化**: React 18 / Tailwind CSS / Framer Motion / Lucide Icons (全 CDN 載入，零 Node.js 依賴)
- **版本控制**: Git / GitHub CLI
- **資料格式**: 純粹 Markdown (Git-friendly，資料完全自主掌控)

---

## 📈 實戰成果範例

- **月平均執行分**: XX.X% (Efficiency Rating)
- **核心標語**: [當月總結標語]
- **關鍵核心獲益**: [獲益項目 A]、[獲益項目 B]、[獲益項目 C]

---

## 📦 版本說明 (Release Notes)

目前版本：**v2.1-flagship**  
本版本實現「完整模組化封裝 (Skill Encapsulation)」，所有邏輯、數據、視覺引擎收納於單一套件包。新增 JIT 校驗機制與三模式沙盒。您可以放心 Fork 使用。

👉 [查看完整技術變更細節 (Full Changelog)](./CHANGELOG.md)
