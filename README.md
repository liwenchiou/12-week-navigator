# 🎯 12-Week Goal Management System

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

專案結構遵循模組化開發原則，並透過 Git 進行版本化管理：

```bash
.
├── config/             # ⚙️ 配置層：定義戰略指標 (核心習慣、週/月計畫)
├── log/                # 📝 紀錄層：存放執行數據 (含日、週、月度日誌)
│   ├── daily/          # 基礎數據點與能量指標
│   ├── weekly/         # 週度評分、失敗分析與資源匯整
│   └── monthly/        # 月度戰略對比與成長紀實
├── reports/            # 📊 呈現層：自動生成的互動式 HTML 月報 (React/CDN)
├── _doc/               # 📂 文件層：系統流程紀錄與優化建議報告
├── .agent/             # 🤖 邏輯層：Antigravity Agent 核心技能 (Skills) 與指令
└── README.md
```

---

## 📖 使用範例 (Interaction Examples)

### 場景 A：每日夜間追蹤 (Daily Tracker)
> **User**: 「幫我紀錄今日習慣。」  
> **Antigravity**: 「好的，已讀取 `核心習慣.md`。今天飲水有過 3000ml 嗎？另外，今天給自己的『能量狀態』打幾分？(1-5)」  
> **User**: 「有，全部達成，能量 4 分。今天領悟到 React Hook 的閉包原理。」  
> **產出**: 自動在 `log/daily/` 生成包含能量指標與技術收穫的 Markdown 日誌。

### 場景 B：週日戰略評估 (Weekly Appraisal)
> **User**: 「產出本週週報。」  
> **Antigravity**: 「掃描到『飛輪運動 2 次』未完成。請問是阻礙的原因是？另外本週有發現推薦的工具嗎？」  
> **User**: 「工作太累，下週會調整。另外推薦這個 AI 工具：xxx。」  
> **產出**: 生成週報並包含 **「🚧 阻礙分析」** 與 **「🔗 資源清單」**，並自動發送 Git PR 紀錄變更。

### 場景 C：月度視覺化演說 (Monthly Visualizer)
> **User**: 「幫我產出 2 月份總結網頁。」  
> **Antigravity**: 「分析本月數據完成。二月核心標語建議為『守護者進化』。正在將戰略進度條與進化對策卡片封裝至網頁中...」  
> **產出**: 在 `reports/` 生成具備毛玻璃發光質感與 12 週進度勾稽的互動式 HTML 檔案。

---

## 🚀 快速上手 (Quick Start)

### 1. 環境需求 (Prerequisites)
在開始之前，請確保您的系統已安裝以下工具：
- **Python 3.10+**: 用於執行系統同步與數據處理腳本。
- **Git 2.x**: 基礎版本控制工具。
- **GitHub CLI (gh)**: **強烈建議**，用於讓 Agent 自動發送及管理 Pull Request。
- **現代化瀏覽器**: 用於渲染互動式 HTML 報表。

### 2. 複製專案與初始化
```bash
# 複製專案
git clone https://github.com/liwenchiou/my-12-week-goal.git
cd my-12-week-goal

# 登入 GitHub CLI (以啟用自動 PR 功能)
gh auth login
```

### 3. 初始化計畫 (Config Setup)
開始之前，請更新以下 Markdown 配置檔，建立您的戰略目標：
- **`config/核心習慣.md`**: 定義每日基礎動作 (KPIs)。
- **`config/週計畫.md`**: 定義本週必須完成的 3-5 項關鍵任務。
- **`config/月計畫.md`**: 定義當月要攻克的戰略里程碑。

### 4. 開始導航 (First Run)
現在，您可以呼叫 **Antigravity** 並輸入：
> 「幫我紀錄今日習慣。」

Agent 會自動讀取您的配置並展開對話導引。

---

## 🔥 核心特性與優勢 (Core Features)

### 1. 互動式熱點與能量追蹤
系統不僅引導習慣紀錄，更關注 **「當下狀態」**。透過能量情緒指標與資源工具紀錄，讓日誌同時具備「狀態監測器」與「知識採集器」的功能。

### 2. 失敗學分析 (Action Bias Analysis)
針對「未達成」的計畫，Agent 會主動啟動「阻礙分析」流程。區分是環境因素、時間分配還是心理壓力，並在週報中自動提出下週的 **「進化對策卡片」**。

### 3. 戰略進度勾稽 (Strategic Alignment)
在月報中，系統會自動比對 12 週的總計畫里程碑，並呈現 **「12 週總進度條」**。確保您在關注當下成長時，也能精準掌握在長期戰略中的具體位置。

### 4. Git 自動化管理 (Git Manager Skill)
內建標準化 Git 工作法。Agent 會自動建立開發分支、撰寫**繁體中文條列式 Commit**，並透過 GitHub CLI 自動發送 Pull Request (PR)。

---

## 💻 技術棧 (Technology Stack)

本系統追求極致的前端體驗與數據的可攜性：
- **邏輯引擎**: AI Agent (基於 Antigravity 核心技能模組)
- **視覺化**: React 18 / Tailwind CSS / Framer Motion / Lucide Icons (全 CDN 載入，零 Node.js 依賴)
- **版本控制**: Git / GitHub CLI (用於自動化 PR 流程)
- **資料格式**: 純粹 Markdown 與 YAML (Git-friendly，資料完全自主掌控)

---

## 📈 實戰成果範例 (2026-02: 守護者進化)

- **月平均執行分**: 82.7% (Efficiency Rating)
- **核心標語**: 守護者進化：從硬體升級到心境蛻變 (HARDWARE EVO)
- **關鍵核心獲益**: 家庭穩定 (System Integrity)、技術質變 (Architecture Update)、自律體力 (Operation Success)
- **視覺呈現**: [查看二月月報演示影片/截圖](./_doc/20260225_月報驗證報告.md)

---

## 📜 更新日誌 (Changelog)

- **2026-02-25 (System 2.0 Upgrade)**:
  - **戰略分析層**: 引入「失敗學分析」邏輯與「能量指標」追蹤，強化回顧深度。
  - **知識管理層**: 新增「日/週/月三級資源庫匯整」功能。
  - **自動化維護**: 建立 `git-manager` 技能，整合 GitHub CLI 實現自動化分支管理與發送 PR。
  - **視覺化震撼**: 
    *   新增「12 週戰略進度條」勾稽總體目標。
    *   補齊簡報網頁標題與裝飾體系，提升專業感。
    *   新增「進化對策卡片」呈現偏差修正方案。
  - **文檔標準化**: 全面改版 `README.md` 提供從零開始的完整引導。

---
