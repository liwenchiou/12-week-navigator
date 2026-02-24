# 🎯 12-Week Goal Management System

> **A self-hosted, AI-collaborative framework for high-output lifecycle management.**

本專案是一套基於 **12 週計畫 (The 12 Week Year)** 方法論建構的個人管理系統。透過 **AI Agent** 的自動化處理，將繁瑣的紀錄流程轉化為結構化的數據與沉浸式回顧，旨在為身處高壓環境的開發者提供一套穩定、可擴展的成長指揮塔。

---

## 🛠️ 核心設計理念 (Core Methodology)

本系統的核心在於「意圖與執行」的完全解耦，並引入 AI 作為數據處理器：

- **配置化治理 (Config-as-Strategy)**：將習慣、週計畫、月計畫定義於配置檔案中，建立明確的目標層級。
- **紀錄自動化 (AI-Driven Logging)**：透過 AI Agent 的對話引導，將非結構化的生活感悟轉化為結構化的 Markdown 日誌。
- **沈浸式視覺化 (Rich Presentation)**：自動生成互動式 Web 報表，整合執行評分 (Scorecard) 與趨勢分析，支援簡報級別的成果展示。

---

## 📂 系統架構 (Directory Structure)

專案結構遵循模組化開發原則，確保資料的可移植性與透明度：

```bash
.
├── config/             # �️ 配置層：定義戰略指標 (核心習慣、週/月計畫)
├── log/                # 📝 紀錄層：存放執行數據 (日、週、月度 Markdown 日誌)
│   ├── daily/          # 基礎數據點
│   ├── weekly/         # 週度執行評分與彙整
│   └── monthly/        # 月度深度回顧與戰略對比
├── reports/            # 📊 呈現層：自動生成的互動式 HTML 月報
├── .agent/             # 🤖 邏輯層：AI Agent 執行腳本與視覺化引擎
└── README.md
```

---

## �️ 如何使用 (Getting Started)

本系統完全透過單純的 Markdown 進行配置與運行。

### 1. 設定計畫 (Config)
在開始執行前，你需要更新位於 `config/` 資料夾下的三個核心配置檔：
- **`核心習慣.md`**：定義你每天必須完成的基礎項目（如：飲水、閱讀、運動）。
- **`週計畫.md`**：定義該週的具體執行任務，使用 `[ ]` 與 `[x]` 管理狀態。
- **`月計畫.md`**：定義該月份的戰略目標與期望達成的里程碑。

### 2. 啟動 Agent 運作
透過與 AI Agent 對話執行以下操作：
- **紀錄習慣**：系統會讀取「核心習慣」，引導你完成今日小結並產出日誌。
- **產出總結**：系統會自動對比「週/月計畫」達成度，計算評分並生成深度回顧報表。
- **生成網頁**：當月報產出時，系統會在 `reports/` 自動產出互動式網站。

---

## �🚀 核心功能與開發者體驗

### 1. 互動式熱點紀錄
系統自動讀取 `config/` 下的配置，透過 Agent 引導式對話完成每日習慣追蹤。開發者只需專注於內容輸出，無需手動調整繁瑣的表格格式。

### 2. 多層級數據彙整
- **週度評分**：自動計算任務達成率，量化執行力水位。
- **月度敘事**：系統會自動掃描週與日的紀錄點，將零散片段重構為具備時間厚度的月度記事，並根據基調提煉「核心標語」。

### 3. UI/UX PRO MAX 視覺化引擎
內建自動化視覺生成模組，當系統產出月結時，可一併生成具備以下特性的互動網頁：
- **基於 React 與 Framer Motion** 的流暢入場動效。
- **Glassmorphism (玻璃擬態)** 視覺風格。
- **SVG 動態趨勢線** 與 **環狀評分儀表板**。

---

## 📈 實戰範例 (Live Example: 2026-02)

- **月平均執行分 (Monthly Score)**：87.4%
- **核心標語 (Core Tagline)**：守護與重構
- **達成項目 (Key Results)**：
  - AI Skills 自動紀錄系統模組完開發。
  - 書房開發環境重整與 12 週目標體系建立。
  - 在多重環境變動下，維持 100% 的核心習慣達成率。

---

## � 技術棧 (Technology Stack)

- **Workflow**: 12 Week Year Method
- **Logic Engine**: AI Agent (Markdown-based skill modules)
- **Frontend**: React 18, Tailwind CSS, Framer Motion, Lucide Icons
- **Data Format**: YAML & Markdown (Git-friendly)
