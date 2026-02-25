---
name: monthly-visualizer
description: 將月總結轉化為一頁式互動網頁，並自動建議存檔於 reports 資料夾。
---

# 網頁生成與存檔規範

當使用者提供月報內容或要求產出網頁時，請執行以下步驟：

## 第一階段：自動命名與存檔建議
1. **命名格式**：`YYYY-MM 每月總結.html`（例如：2026-02 每月總結.html）。
2. **預設路徑**：建議使用者存放於 `/reports/` 資料夾中。

## 第二階段：技術棧規範 (Strict CDN Policy)
- **環境要求**：僅限單一 HTML 檔案，使用者無需安裝 Node.js 或執行 Build。
- **組件來源**：
  - CSS: Tailwind CSS (cdn.tailwindcss.com)
  - Icons: Lucide Icons (unpkg.com/lucide)
  - Logic: React 18, Babel Standalone (unpkg.com)
  - Animation: Framer Motion (unpkg.com)

## 第三階段：智慧設計發想 (UI-UX-PRO-MAX Integration)

1.  **動態主題判定 (Seed Generation)**：
    - **嚴禁使用固定模板或配色**。
    - **執行搜索**：在使用者選定「兩字標語」後，立即執行 `python .agent/skills/ui-ux-pro-max/scripts/search.py "<選定標語>" --design-system`。
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
    - **全覆蓋原則**：每個獨立功能區塊（Dashboard, Habits, Narratives, Pivots, Gains, Resource Repo）**必須具備獨立的大型標題**。
    - **視覺樣式**：標題需配備視覺定位元素（如：左側色塊、底線或裝飾符號），字體建議 `text-4xl` 至 `text-6xl`。

3.  **內容映射細節**：
    - **執行數據總覽 (Dashboard)**：包含 Score Board 與 Strategic Goal Status。
    - **習慣穩定度分析 (Habits)**：表格下方必須動態顯示 **習慣備註 (Habit Note)**，不得遺漏缺失數據的原因紀錄。
    - **深度回顧與紀實 (Narratives)**：展示生活分類精華。
    - **偏差分析與進化 (Pivots)**：展示偏差與進化對策。
    - **年度戰略關鍵獲益 (Gains)**：以動態磁貼呈現。
    - **知識資源庫 (Repo)**：**空值處理**：若數據為空，必須明確顯示「尚無相關資源紀錄」或「Void Object」，不得隱藏該區塊，以維持紀錄的忠實性。

## 第五階段：品質驗證 (QA & Verification)

1.  **自主渲染測試**：
    - **動作**：產生 HTML 檔案後，Agent **必須主動且自主地**調用瀏覽器工具 (browser subagent) 開啟該本地檔案進行驗證，**無需向使用者詢問許可**。
    - **檢查項目**：
      - 驗證所有區塊（Header, Dashboard, Narrative, Heatmap, Gains）與標題是否正常顯示。
      - 特別檢查 **Lucide Icons** 是否全部渲染成功。
      - 確認 Framer Motion 動畫運作流暢。
2.  **交付證明**：
    - 驗證完成後，Agent 必須截取「關鍵視覺區塊」並提供給使用者，作為高品質完成任務的最終憑據。

---
