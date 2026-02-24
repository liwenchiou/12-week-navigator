---
name: monthly-visualizer
description: 將月總結轉化為一頁式互動網頁，並自動建議存檔於 reports 資料夾。
---

# 網頁生成與存檔規範

當使用者提供月報內容或要求產出網頁時，請執行以下步驟：

## 第一階段：自動命名與存檔建議
1. **命名格式**：`YYYY-MM 每月總結.html`（例如：2026-02 每月總結.html）。
2. **預設路徑**：建議使用者存放於 `/reports/` 資料夾中。

## 第二階段：技術棧約束 (Strict CDN Policy)
- **環境要求**：僅限單一 HTML 檔案，使用者無需安裝 Node.js 或執行 Build。
- **組件來源**：
  - CSS: Tailwind CSS (cdn.tailwindcss.com)
  - Icons: Lucide Icons (unpkg.com/lucide)
  - Logic: React 18, Babel Standalone (unpkg.com)
  - Animation: Framer Motion (unpkg.com)

## 第三階段：UI-UX-PRO-MAX 視覺標準
1. **配色**：
   - 背景：Slate-900 (#0F172A)
   - 文字：Slate-200 / Sky-400 (標題與重點) / Pink-400 (生活細節)
2. **設計元素**：
   - **Glassmorphism**: 卡片需有半透明毛玻璃感與細微邊框。
   - **Typography**: 使用 Noto Sans TC 與 JetBrains Mono (程式碼/數據)。
   - **Interactivity**: 
     - 入場時標題與數值需有漸顯動畫。
     - 點擊或懸停習慣表時需有發光效果。
     - 支援 Responsive Design (行動端與桌面端)。

## 第四階段：內容映射 (二月報範例)
- **Hero**: 呈現「守護與重構」核心標語。
- **Dashboard**: 以環狀或數字卡片呈現 87.4% 的執行評分。
- **Habits**: 將五項 100% 達成的習慣以高亮 Grid 呈現。
- **Journal**: 渲染精簡後的敘事回顧。

---
