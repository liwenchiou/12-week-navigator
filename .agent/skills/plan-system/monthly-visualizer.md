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

1.  **動態主題判定**：
    - **嚴禁使用固定配色**。請根據該月報生成的「核心標語 (Slogan)」作為關鍵字。
    - **調用技能**：執行 `python .agent/skills/ui-ux-pro-max/scripts/search.py "<Slogan 關鍵字>" --design-system`。
2.  **視覺標準套用**：
    - 從 Python 指令的回傳結果中，提取 **Pattern, Style, Colors, Typography** 作為當月網頁的視覺基調。
    - **情感對應**：若標語偏向「暖心/守護」，設計應具備溫柔與高對比；若偏向「衝刺/成長」，則應具備科技感與力量感。
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
    - **Hero Title**: 從月報提取 `#️⃣ 月度核心標語`，作為網頁開場。
    - **Sub-headline**: 提取其下方的感性敘述或副標題。
    - **Strategic Progress (NEW)**：建立一個 **「12 週總進度條 (Total Blueprint Progressbar)」**。
      - **計算邏輯**：根據目前月份（如：二月為第 5-8 週）在 12 週計畫中的比例進行視覺呈現，確保戰略勾稽。
2.  **量化指標 (Performance Metrics)**：
    - **Section Title**: 「執行數據總覽」。
    - **Score Board**: 提取 `📊 月平均執行評分`，以大型動態環狀圖或數字卡片呈現。
    - **Strategic Goal Status**: 掃描 `🎯 月計畫目標達成狀況`。
3.  **趨勢分析 (Trend Visualization)**：
    - **Section Title**: 「習慣穩定度分析」。
    - **Habit Heatmap**: 視覺化習慣表格。
    - **Energy/Mood Flow**: 視覺化本月心境變化。
4.  **深度敘事與偏差分析 (Narratives & Pivots)**：
    - **Section Title**: 「深度回顧與進化對策」。
    - **Narrative Cards**: 呈現精選生活回顧。
    - **Pivots Block (NEW)**：將 `🚧 阻礙與偏差分析` 轉化為「進化對策卡片」，強調如何克服難點。
5.  **靈魂金句與資源 (Wisdom & Repo)**：
    - **Section Title**: 「核心金句與資源」。
    - **Quote Block**: 呈現大引言。
    - **Resource Repo (NEW)**：將 `🔗 知識資源庫` 轉化為磁貼或清單展示。
6.  **結尾獲益 (Strategic Gains)**：
    - **Section Title**: 「月度三大獲益」。
    - **Monthly Gains**: 三個獨立的動態磁貼。

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
