# 📜 更新日誌 (Changelog)

所有關於 12 週計畫系統的功能變更、修復與架構優化皆記錄於此。

---

## [2026-02-26] - Navigation & UX Refinement
### 交互與導航優化 (Interaction/Nav)
- 確立「明確指令原則」，移除模糊的自動觸發邏輯，改為引導式建議執行 `/warmup`。
- 在 `.agent/instructions.md` 中實作「文件自動同步機制」，確保系統異動自動反映至文檔。
- 確立文件權責分離：將詳細日誌移至 `CHANGELOG.md`，README.md 僅保留最新動態。
- 調整更新日誌為降序排列 (Latest First)。

### 指令權威化 (Agent Policy)
- 定義自然語言指令映射 (Command Mapping) 與啟動協定。

---

## [2026-02-25] - System 2.0 & Resilience Upgrade
### 架構與資產 (Architecture)
- 將 `log/` 全面更名為 `data/`，確立「數據即資產」的治理邏輯。
- 建立 `sandbox/` 隔離測試系統，支援全自動化與互動式 Skill 演練，確保正式紀錄零污染。

### 自動化進化 (Workflow)
- 引入「執行授權」機制，默認許可已知 Skill 流程指令，大幅提升協作流暢度。
- 強化「二字標語」提案與視覺設計連動，確保網頁靈魂與數據意境一致。

### 紀錄誠實性 (Integrity)
- 在所有 Skill 中埋入「不猜測」防錯條款，針對數據缺失僅進行事實紀錄或主動詢問。

### 視覺化震撼 (Visuals)
- 新增「設計方案揭露」預展步驟。
- 實作「標語即種子」的動態設計模式，產出 Neo-Brutalism (紮根) 與 Aurora Gradient (蓄力) 等多風格報表。
