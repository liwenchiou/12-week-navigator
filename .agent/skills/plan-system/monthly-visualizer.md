---
name: monthly-visualizer
description: 將月總結轉化為一頁式互動網頁，並自動建議存檔於 reports 資料夾。
---

# 網頁生成與存檔規範

當使用者提供月報內容或要求產出網頁時，請執行以下步驟：

## 第零階段：格式確認（Token 節省關鍵步）
在動筆前，先詢問使用者「深度生活回顧」的展示偏好：

> 「深度生活回顧在網頁中，請問您偏好哪種形式？
> **A. 條列重點式**（每分類 3~5 項，適合簡報說明）
> **B. 段落統整式**（完整融合段落，適合閱覽分享）」

**收到回覆後再進入第一階段**，若使用者未特別說明，預設使用 **A（條列重點式）**。

## 第一階段：自動命名與存檔建議
1. **命名格式**：`YYYY-MM 每月總結.html`（例如：2026-02 每月總結.html）。
2. **預設路徑**：建議使用者存放於 `/reports/` 資料夾中。

## 第二階段：技術棧規範 (Strict CDN Policy)
- **環境要求**：僅限單一 HTML 檔案，使用者無需安裝 Node.js 或執行 Build。
- **組件來源 (確保無衝突)**：
  - CSS: Tailwind CSS (透過 `https://cdn.tailwindcss.com` 引入)
  - Icons: Lucide Icons (請透過 `unpkg` 或 `jsdelivr` 引入 UMD 版本，並透過 `window.lucide` 初始化渲染)
  - Logic: React 18 (`react@18/umd/react.production.min.js`, `react-dom@18/umd/react-dom.production.min.js`) 與 Babel Standalone
  - Animation: Framer Motion (必須對應 React 18 可用的 UMD 版本，並透過 `window.Motion` 呼叫)

## 第三階段：智慧設計發想 (UI-UX-PRO-MAX Integration)

1.  **動態主題判定 (Seed Generation)**：
    - **嚴禁使用固定模板或配色**。
    - **執行腳本強制性**：在使用者選定「兩字標語」後，**必須且一定要**先執行 `python .agent/skills/ui-ux-pro-max/scripts/search.py "<選定標語>" --design-system` 來取得設計指南，才可進行後續 HTML 撰寫。
2.  **設計方案揭露 (Design Transparency)**：
    - **關鍵步**：在生成 HTML 代碼前，必須向使用者簡述本次設計的 **Pattern, Style, Colors**。
    - **意境契合**：確保視覺風格與標語意境高度一致（例如：標語是【交付】，風格應偏向專業、利索、區塊感）。
3.  **基礎互動架構** (一致性要求)：
    - **Glassmorphism**: 基礎容器需維持半透明毛玻璃感。
    - **Interactivity**: 
      - 入場時標題、數值與卡片需有 **Framer Motion** 的 staggered 動畫。
      - 所有數據卡片需具備穩定且細緻的懸停彈出與發光效果。
    - **結構化標題 (Section Headers)**: 
      - 除了首屏 Hero 區塊外，每個獨立功能區塊（Dashboard, Heatmap, Narrative, Gains）**必須**配備清晰的大型標題（建議 text-4xl 以上）。
      - 標題旁建議輔以水平漸層裝飾線或裝飾點，建立明確的視覺導航。
    - **Responsiveness**: 完美適配從 375px (手機) 到 1440px (桌面) 的佈局變化。

## 第四階段：內容映射與簡報結構 (Dynamic Template Strategy)

本階段旨在將 Markdown 月報中的數據與文字，精準轉化為具備「故事性」的簡報網頁。請依據以下動態欄位進行映射：

1.  **標語與靈魂 (Identity)**：
    - **Hero Title**: 從月報提取 `#️⃣ 月度核心標語`，**必須呈現為「兩字標語」格式**（例如：【交付】）。
    - **Sub-headline**: 提取其下方的感性敘述或副標題。
    - **Strategic Progress**：建立一個 **「12 週總進度條 (Total Blueprint Progressbar)」**。
      - **計算邏輯**：根據目前月份在 12 週計畫中的比例進行視覺呈現（如二月為 66%）。

2.  **區域化標題 (Section Headers - Mandatory)**：
    - **全覆蓋原則**：每個獨立功能區塊**必須具備獨立的大型標題**。
    - **🚨 繁體中文強制要求**：網頁中所有區塊標題（含 Hero Title 以外的 Section Headers）**一律必須使用繁體中文**，嚴禁出現英文標題（如 Dashboard, Habits, Gains 等）。建議的繁體中文對應如下：
      - Dashboard → **📊 執行數據總覽**
      - Habits → **🗓️ 習慣達成分析**
      - Narratives → **📖 深度生活回顧**
      - Pivots → **🚧 偏差分析與進化對策**
      - Gains → **💎 月度三大獲益**
      - Resource Repo → **🔗 知識資源庫**
    - **視覺樣式**：標題需配備視覺定位元素（如：左側色塊、底線或裝飾符號），字體建議 `text-4xl` 至 `text-6xl`。

3.  **內容映射細節與完整度強制要求 (No Omission Policy)**：
    產出的網頁**必須完整包含以下所有區塊**，標題全數使用**繁體中文**，即使內容短少也不得省略：
    - **📊 執行數據總覽**：包含 Score Board 與 12 週總進度條。
    - **🗓️ 習慣達成分析**：表格下方必須動態顯示習慣備註，不得遺漏缺失數據的原因紀錄。
    - **📖 深度生活回顧**：**簡報格式規範**：HTML 網頁版每個分類僅條列 **3~5 條最重要的紀錄**，供發表者在現場補充說明；完整段落版本保留在 `data/monthly/YYYY-MM.md`。
    - **🚧 偏差分析與進化對策**：展示偏差分析與具體的進化對策。
    - **💎 月度三大獲益**：以動態磁貼呈現三大獲益。
    - **🔗 知識資源庫**：**空值處理**：若數據為空，必須明確顯示「尚無相關資源紀錄」，不得隱藏該區塊，以維持紀錄的忠實性。

## 第五階段：品質驗證 (QA & Verification)

1.  **瀏覽器渲染授權**：
    - **動作**：產生 HTML 檔案後，Agent **必須主動詢問使用者**：「網頁已初步生成，是否需要調用 Browser Subagent 進行渲染測試與截圖？」
    - 取得明確同意後，才可開啟本地檔案進行後續驗證。
2.  **自主渲染測試 (若取得授權)**：
    - **檢查項目**：
      - 驗證所有區塊（Header, Dashboard, Narrative, Heatmap, Gains）與標題是否正常顯示。
      - 特別檢查 **Lucide Icons** 與 **React/Framer Motion** 是否成功載入無白屏。
3.  **交付證明**：
    - 測試完成後，提供截圖並交付最終 HTML 源碼。

---
