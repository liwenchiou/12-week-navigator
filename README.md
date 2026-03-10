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
├── data/               # 📝 數據層：存放執行資產 (按年/月封裝)
│   ├── YYYY/MM/daily/  # 基礎數據點與能量指標 (2026/02/daily)
│   ├── YYYY/weekly/    # 週度評分、失敗分析與資源彙整
│   └── YYYY/monthly/   # 月度戰略對比與成長紀實
├── reports/            # 📊 呈現層：自動生成的互動式 HTML 月報 (React/CDN)
├── sandbox/            # 🧪 隔離層：Skill 流程演練與全系統測試沙盒
├── _doc/               # 📂 文件層：系統流程紀錄與優化建議報告
├── .agent/             # 🤖 邏輯層：Antigravity Agent 核心技能 (Skills) 與指令
└── README.md
```

---

## 📖 使用範例 (Interaction Examples)

### 場景 A：每日夜間追蹤 (Daily Tracker)
> **User**: 「幫我紀錄今日習慣。」  
> **Antigravity**: 「好的，已讀取 `核心習慣.md`。今天飲水有過 3000ml 嗎？(一問一答模式)」  
> **User**: 「有」  
> **Antigravity**: 「太棒了！最後，今天給自己的『能量狀態』打幾分？(1-5)」
> **User**: 「4 分」  
> **Antigravity**: 「收到！那關於今天，有什麼想紀錄的小結或領悟嗎？」
> **User**: 「今天領悟到 React Hook 的閉包原理。」  
> **產出**: 自動在 `data/YYYY/MM/daily/` 生成包含能量指標與紀錄原文的 Markdown 日誌。

### 場景 B：週日戰略評估 (Weekly Appraisal)
> **User**: 「產出本週週報。」  
> **Antigravity**: 「掃描到『飛輪運動 2 次』未完成。請問阻礙的原因是？(一問一答模式)」  
> **User**: 「工作太累，下週會調整。」  
> **Antigravity**: 「收到！已紀錄。另外，本週有發現推薦的新資源或工具嗎？」
> **User**: 「推薦這個 AI 工具：xxx。」
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
# 若尚未安裝，請執行：brew install gh (Mac) 或參閱官方文件
gh auth login
```

### 3. 初始化計畫 (Config Setup)
開始之前，請更新以下 Markdown 配置檔，建立您的戰略目標：
- **`config/核心習慣.md`**: 定義每日基礎動作 (KPIs)。
- **`config/週計畫.md`**: 定義本週必須完成的 3-5 項關鍵任務。
- **`config/月計畫.md`**: 定義當月要攻克的戰略里程碑。

### 4. 開始導航 (First Run & Setup AI)
在新環境中，您需要讓 AI 助理 (Agent) 進入本系統的運作狀態。
如果您詢問「如何開始」，Agent 將會建議您執行以下指令：
> **「執行 /start」**

**Agent 將會自動完成以下初始化：**
- 讀取 `.agent/instructions.md` 定位核心原則。
- 載入 `.agent/skills/` 所有的自動化技能。
- 偵測數據現狀，告知您目前計畫的進度位置。

---

## �️ 指令速查 (Command Reference)

您可以透過以下自然語言指令引導 **Antigravity** 執行核心任務：

- **12 週計畫導覽總部**：`執行 /12-week-navigator` (啟動、診斷、報表、紀錄補記的單一旗艦入口)

- **日常習慣紀錄**：`紀錄今日習慣`
- **安全測試模式**：`進入測試模式` (啟動隔離沙盒，進行流程模擬)
- **Git 自律提交**：`執行 git 同步` (自動化分支與 PR 流程)

---

## �🔥 核心特性與優勢 (Core Features)

### 1. 互動式熱點與能量追蹤
系統不僅引導習慣紀錄，更關注 **「當下狀態」**。透過能量情緒指標與資源工具紀錄，讓日誌同時具備「狀態監測器」與「知識採集器」的功能。

### 2. 失敗學分析 (Action Bias Analysis)
針對「未達成」的計畫，Agent 會主動啟動「阻礙分析」流程。區分是環境因素、時間分配還是心理壓力，並在週報中自動提出下週的 **「進化對策卡片」**。

### 3. 戰略進度勾稽 (Strategic Alignment)
在月報中，系統會自動比對 12 週的總計畫里程碑，並呈現 **「12 週總進度條」**。確保您在關注當下成長時，也能精準掌握在長期戰略中的具體位置。

### 4. 隔離測試沙盒 (Sandbox Safety)
內建 **`sandbox/` 隔離測試體系**。您可以隨時進入「測試模式」，在不污染真實歷史數據的情況下，演練任何對話流程、模擬極端數據或預覽不同的視覺呈現。

### 5. 一問一答互動協定 (Single-Question Protocol)
系統嚴格執行「儀式感」紀錄。不論是日常習慣、能量評分還是週報確認，Agent 每次僅會針對單一項目發問。這能確保使用者在紀錄時擁有完整的專注力，不被資訊掃描式的問題淹沒，將「填表」轉化為真實的「覺察與對話」。

---

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

## 📜 最新動態 (Latest Update)

- **2026-03-03 21:30:00 (Architecture Refactoring & Interaction Protocol)**:
  - **核心準則憲法化**：重構 `.agent/instructions.md`，全域強制執行「逐項互動原則」與「忠實紀錄原則」。
  - **技能與工作流重組**：全面清理技能檔案冗餘，並新增 `/pre-check`, `/config-validator`, `/habit-fixer` 等專門工作流，實現職責分離。
  - **導航機制進化**：優化 `/start` 深度聯動預檢與校準機制，確保環境零痛點上手。

- **2026-03-01 19:30:00 (Data Architecture Refactoring)**:
  - **年份/月份分層化**：將 `data/` 下的所有檔案重整為 `data/YYYY/MM/daily/` (日誌) 與 `data/YYYY/[weekly|monthly]/` (報表) 結構。
  - **範本中心化**：建立 `config/samples/` 集中管理所有 `_sample.md` 檔案，降低數據層雜訊。
  - **系統連動優化**：同步更新 `habit-tracker`, `weekly-summarizer`, `monthly-reporter` 與 `@start` 的路徑邏輯，實現全自動歸位。


- **2026-02-26 15:34:00 (Token Optimization - 4 Improvements)**:
  - **HTML 格式確認**：`monthly-visualizer` 新增第零階段問答，避免格式不明造成多次重寫（最高節省 ~7,000 tokens/對話）。
  - **文件批次更新**：`instructions` 文件同步改為 Git 前一次性統整，減少高頻讀寫（最高節省 ~13,000 tokens/對話）。
  - **週報關鍵區塊讀取**：`monthly-reporter` 指定讀取優先區塊，跳過習慣熱點圖明細。
  - **Skill 速查摘要**：`skills-index` 加入 📌 速查行，輕量情境可跳過完整 Skill 讀取。

- **2026-02-26 15:19:00 (Monthly Report Narrative & Visualization Rules)**:
  - **月報統整規範**：`monthly-reporter` 新增禁止週次標籤拼接、要求自然段落融合；`monthly-visualizer` 明訂 HTML 版深度回顧每分類僅條列 3~5 重點。

- **2026-02-26 14:52:00 (Weekly Summarizer Faithful Text Fix)**:
  - **忠實原文規範強化**：`weekly-summarizer` 明確禁止 AI 自行添加評語，要求嚴格引用日誌原文並標注日期，列出具體禁止語句範例。

- **2026-02-26 14:32:00 (Known Issues Log)**:
  - **已知問題日誌機制**：建立 `_doc/執行發現問題.md` 結構化格式（日期區塊 + 表格），並在 `instructions.md` 中新增全局規則，讓 Agent 在診斷問題時能主動參閱，以及在使用者要求時直接追加填寫。

- **2026-02-26 14:27:00 (Monthly Reporter & Visualizer Fixes)**:
  - **月報互動確認補強**：重構 `monthly-reporter` 第一階段，強制先掃描週報、再逐條一問一答確認月計畫未完成目標。
  - **網頁區塊繁體中文化**：`monthly-visualizer` 新增強制規範，所有 HTML 區塊標題一律使用繁體中文，並提供明確的對應清單。

- **2026-02-26 13:40:00 (Zero-Generation Token Optimize)**:
  - **預載範本取代動態生成**：全面建立各目錄 (`config/`, `data/`, `reports/`, `sandbox/`) 之 `_sample` 檔案機制，並優化 `.gitignore`。此舉取代了 `/warmup` 開機時動態化生成 `.gitkeep` 或配置檔的浪費步驟。

- **2026-02-26 13:30:00 (Git Manager Upgrade)**:
  - **遠端分發 (Cross-Repo Sync)**：修訂 `git-manager` 流程，於 PR 結案後自動查核並推送至 `framework` 節點，維持私有資料庫與開源框架雙軌同步。

- **2026-02-26 13:25:00 (E2E Test Bug Fixes)**:
  - **環境補強與防呆**：升級 `/warmup`，強制建立空目錄時配置 `.gitkeep`，並修補 config 範本自動生成的 Checkbox 結構與日期格式。
  - **月報/網頁防閹割**：導入 No Omission Policy，禁止 Agent 於少樣本測試時私自裁減包含「三大獲益」、「阻礙分析」等核心版塊。
  - **強制問答與腳本**：嚴格化 `weekly-summarizer` 的問卷機制（一問一答），並強制 UI/UX 搜索腳本在生成月報網頁前被呼叫。

- **2026-02-26 13:20:00 (Token Optimization)**:
  - **導入 Lazy Loading 與 Index 機制**：重構 `/warmup` 啟動工作流，透過讀取輕量級的 `skills-index.md` 代替一次性載入所有技能檔案，大幅節省 80% 以上 Token 消耗。

- **2026-02-26 11:30:00 (Core Skills & Testing Fixes)**:
  - **效能防呆與強制存檔**：升級指令憲法，加入重複指令自動中斷機制與實體存檔強制驗證。
  - **技能體驗優化**：擴充 `habit-tracker` 快捷回覆；強制 `weekly-summarizer` 採一問一答且支援當週狀態回寫。
  - **視覺化修復與 E2E 測試**：解決 `monthly-visualizer` CDN 白屏衝突，並於 `skill-tester` 導入全工作流測試 (E2E Test)。
- **2026-02-26 09:50:00 (Workflow & Privacy Hardening)**:
  - 更新 **`.gitignore`**：排除 `_doc/` 資料夾，保護開發決策與優化建議報告。
  - 強化 **`/warmup` 工作流**：新增 `config/` 檔案完整性檢查。當設定檔缺失時，系統將自動建立具備「範例說明區塊」的標準模板。
- **2026-02-26 09:32:00 (Env Security)**:
  - 更新 **`.gitignore`**：將 `data/` (個人紀錄)、`reports/` (生成網頁) 與 `design-system/` 等非必要上傳之資產加入忽略清單，強化資料隱私。
- **2026-02-26 09:30:00 (Policy & Core Logic)**:
  - 確立 **「越權行為防範規範 (Action Boundary)」**：明確禁止 Agent 執行任何不在 Skill 定義內的自動化行為。
  - **核心邏輯變更政策**：確立涉及 `.agent/` 目錄的修改必須同步記錄於 `README.md` 與 `CHANGELOG.md` 以確保變更透明。
  - 清理 `template/` 殘餘，回歸純粹的專案結構。
- **2026-02-26 09:25:00 (Policy Hardening)**:
- **2026-02-26 09:12:45 (Portability & Env Hardening)**:

👉 [查看完整更新歷史與詳細日誌 (Full Changelog)](./CHANGELOG.md)
