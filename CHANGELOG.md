# 📜 更新日誌 (Changelog)

所有關於 12 週計畫系統的功能變更、修復與架構優化皆記錄於此。

---

## [2026-02-26] - Navigation & UX Refinement
### 交互與導航優化 (Interaction/Nav)
- 確立「明確指令原則」，移除模糊的自動觸發邏輯，改為引導式建議執行 `/warmup`。
- 在 `.agent/instructions.md` 中實作「文件自動同步機制」，確保系統異動自動反映至文檔。
- 新增「逾時自檢機制 (Timeout Self-Check)」：執行等待超過 5 秒時，Agent 必須主動診斷原因並回報。
- 確立文件權責分離：將詳細日誌移至 `CHANGELOG.md`，README.md 僅保留最新動態。
- 調整更新日誌為降序排列 (Latest First)，並實作每日內容統整機制。
- **安全性增強 (Security)**：更新 `.gitignore`，將包含個人隱私的 `data/` 目錄、生成的 `reports/` 以及測試用的 `design-system/` 納入忽略清單，落實「代碼與數據分離」原則。
- **專案瘦身 (Project Cleanup)**：完全移除 `template/` 目錄及相關殘餘，確保專案目錄與 `.agent/instructions.md` 定義一致。
- **核心邏輯管理方針**：確立涉及 `.agent/` 目錄的所有修改必須同步更新至 README 與 CHANGELOG；暫緩強制開立分支之執行，優先確保變更的可追蹤性。
- **越權行為防範 (Policy Hardening)**：在指令憲法中建立 `Action Boundary` 條款，明確規定凡不在 Skill 內的主動行為必須事先詢問。
- **環境強化 (Env Hardening)**：升級 `/warmup` 工作流，新增具體的目錄結構完整性檢查。
- **模板一致性修復 (Template Alignment)**：修正 `template/config/` 中的週計畫、月計畫與核心習慣模板，使其與實際運作的檔案格式（包含週次標題、範例說明、純列表格式）完全對齊。
- **技能協議強化 (Skill Hardening)**：更新 `weekly-summarizer` 與 `habit-tracker` 技能，明確其對設定檔 Header (`## 第 XX 週`, `## 核心習慣清單`) 的搜尋邏輯，消除解析歧義。
- **可攜式套件化 (Portability)**：建立 `template/` 資料夾，封裝「開箱即用」的 12 週計畫框架，包含核心技能、指令與清空內容的配置模板，便於分享給其他工程師。


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
