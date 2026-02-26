# 技能索引總表 (Skill Registry Index)

為降低啟動時 Token 消耗，請依照本表索引，**僅在需要時 (Lazy Load) 才讀取對應的 .md 檔案**。

## 📅 目標與習慣管理 (`plan-system/`)
此清單內的技能負責核心的「12 週計畫」生命週期管理。

- **`plan-system/habit-tracker.md`**: 處理每日習慣詢問與打卡、情緒與能量紀錄。
- **`plan-system/weekly-summarizer.md`**: 處理每週計畫回顧與執行分數計算，產出週報。
- **`plan-system/monthly-reporter.md`**: 處理跨週資料彙整與月報生成。
- **`plan-system/monthly-visualizer.md`**: 接續產出純 HTML 儀表板視覺化介面。
- **`plan-system/git-manager.md`**: 自動化 Git 狀態提交與 GitHub PR 協助，確保資料儲存一致性。
- **`plan-system/skill-tester.md`**: 開發與沙盒測試工具，負責在非正式區塊模擬執行各項功能。

## 🎨 視覺與體驗設計 (`ui-ux-pro-max/`)
此模組支援 `monthly-visualizer` 等需要前端設計指導的場景。

- **`ui-ux-pro-max/SKILL.md`**: 大量前端排版樣式、調色盤與 UX 元件設計準則庫。遇到任何視覺化設計相關的操作時調用。

---
*維護須知：若有新增技能檔案，請同步更新本索引表，並嚴格遵循 Lazy Loading 規範讀取對應檔案。*
