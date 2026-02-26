# 技能索引總表 (Skill Registry Index)

為降低啟動時 Token 消耗，請依照本表索引，**僅在需要時 (Lazy Load) 才讀取對應的 .md 檔案**。

## 📅 目標與習慣管理 (`plan-system/`)
此清單內的技能負責核心的「12 週計畫」生命週期管理。

- **`plan-system/habit-tracker.md`**: 處理每日習慣詢問與打卡、情緒與能量紀錄。
  - 📌 *每日一問一答 → 存 `/data/daily/YYYYMMDD.md` → 嚴禁腦補未完成原因*

- **`plan-system/weekly-summarizer.md`**: 處理每週計畫回顧與執行分數計算，產出週報。
  - 📌 *流程：讀週計畫 → 逐條一問一答確認 → 阻礙詢問 → 金句 → 存 `/data/weekly/YYYY-Wxx.md` → 回寫週計畫狀態*
  - 📌 *深度回顧：引用日誌原文，禁 AI 評語，標注日期*

- **`plan-system/monthly-reporter.md`**: 處理跨週資料彙整與月報生成。
  - 📌 *流程：先掃週報關鍵區塊 → 月計畫逐條一問一答 → 標語提案 → 報表生成 → 存 `/data/monthly/YYYY-MM.md`*
  - 📌 *深度回顧：有機段落統整，禁 W0x 標籤拼接，禁 AI 評語*

- **`plan-system/monthly-visualizer.md`**: 接續產出純 HTML 儀表板視覺化介面。
  - 📌 *流程：先問格式偏好（條列/段落）→ 執行 UI/UX 腳本 → 揭露設計方案 → 產 HTML → 存 `/reports/YYYY-MM 每月總結.html`*
  - 📌 *所有 Section Headers 強制繁體中文；深度回顧 HTML 版每分類 3~5 條重點*

- **`plan-system/git-manager.md`**: 自動化 Git 狀態提交與 GitHub PR 協助，確保資料儲存一致性。
  - 📌 *流程：詢問執行方式（A 列指令/B 自動）→ 建分支 → commit（繁中）→ PR → 合併後 push framework*

- **`plan-system/skill-tester.md`**: 開發與沙盒測試工具，負責在非正式區塊模擬執行各項功能。
  - 📌 *所有操作限制在 `/sandbox/` 目錄內，嚴禁污染正式數據*

## 🎨 視覺與體驗設計 (`ui-ux-pro-max/`)
此模組支援 `monthly-visualizer` 等需要前端設計指導的場景。

- **`ui-ux-pro-max/SKILL.md`**: 大量前端排版樣式、調色盤與 UX 元件設計準則庫。遇到任何視覺化設計相關的操作時調用。
  - 📌 *使用方式：執行 `python .agent/skills/ui-ux-pro-max/scripts/search.py "<標語>" --design-system`*

---
*維護須知：若有新增技能檔案，請同步更新本索引表，並嚴格遵循 Lazy Loading 規範讀取對應檔案。*
