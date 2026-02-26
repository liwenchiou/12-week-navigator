# 📜 更新日誌 (Changelog)

所有關於 12 週計畫系統的功能變更、修復與架構優化皆記錄於此。

---

## [2026-02-26] - Core Skills & Sandbox Testing Fixes
### 系統穩定性與防呆 (System Resilience)
- **預載範本優化 (Zero-Generation Warmup)**：重構 `/warmup` 腳本，改由內建 `_sample` 檔案群自動維持 Git 目錄結構並提供標準化配置範本。廢除開機時的動態生成與 `.gitkeep` 操作，進一步省下高昂的 Token 盲目消耗。
- **環境補強與防呆 (Env Hardening)**：升級 `/warmup` 腳本，增強對缺失目錄的 `.gitkeep` 自動保護。修補配置檔 (週/月計畫) 生成邏輯，強制規範日期格式與 `- [ ]` Checkbox 生成。
- **Token 消耗最佳化 (Lazy Loading)**：優化 `/warmup` 啟動工作流，導入 `skills-index.md` 延遲加載機制，系統只在需要時讀取對應技能檔案，減少逾 80% 的初始 Token 消耗。
- **效能防呆 (Fail-Safe)**：新增指令逾時與重複執行（超過2次）自動中斷機制，防止無限迴圈卡死。
- **強制存檔驗證 (Persistent Save Check)**：於多輪問答或狀態轉換前，強制驗證實體 Markdown 檔案是否已確實寫入。

### 技能與體驗優化 (Skill & UX Refinement)
- **已知問題日誌規範 (Known Issues Log)**：在 `instructions.md` 第 7.1 節新增全局規則，定義 `_doc/執行發現問題.md` 的兩種觸發時機：診斷問題時主動參閱、使用者要求紀錄時直接以表格格式追加，無需詢問。
- **月報互動確認補強 (monthly-reporter)**：重構第一階段執行順序，改為先掃描週報彙整數據，再讀取月計畫，並針對每條 `- [ ]` 未完成目標以「一問一答」方式逐條向使用者確認，禁止一次性精簡帶過。
- **網頁區塊繁體中文化 (monthly-visualizer)**：新增「🚨 繁體中文強制要求」規範，要求所有區塊標題（Dashboard → 執行數據總覽、Habits → 習慣達成分析等）一律使用繁體中文，嚴禁英文標題出現在 HTML 輸出中。
- **抗拒越權條款 (Conflict Override Protocol)**：在 `instructions.md` 中新增全局最高準則，當使用者語氣急迫（如「立刻執行」）與 Skill 強制詢問流程牴觸時，必須無視急迫語氣，優先遵守 Skill 規範並暫停確認。
- **範本隔離防護 (Template Exclusion)**：修改 `weekly-summarizer` 與 `monthly-reporter` 的掃描邏輯，強制要求在讀取 `data/` 歷史日誌時，必須略過所有 `data_sample.md` 或 `_sample` 結尾的檔案，避免範本內容污染報表與熱點圖。
- **多遠端庫跨域同步 (Cross-Repo Sync)**：擴充 `git-manager` 收尾邏輯，當判定存在名為 `framework` 的遠端庫（專供 `12-week-navigator` 開源框架）時，自動呼叫推送指令確保本地、私人與開源庫三方合一。
- **月報完整性防護 (No Omission Policy)**：強制 `monthly-reporter` 與 `monthly-visualizer` 在測試數據稀少時不得私自閹割報表區塊，確保「12週進度條、習慣矩陣、阻礙偏差、三大獲益」全數強制輸出。
- **強制腳本呼叫 (Script Binding)**：強化 `monthly-visualizer` 規定，嚴格要求在撰寫 HTML 前必須呼叫 UI/UX python 腳本。
- **嚴格專注詢問 (weekly-summarizer)**：強制掃描 `- [ ]` 項目並要求 Agent 放棄批量提問，徹底落實一次一問一答的互動體驗。
- **語意寬容 (habit-tracker)**：支援「完美達成」快捷標記，直接將剩餘核心習慣標註為完成並跳轉情緒評估。
- **專注詢問 (weekly-summarizer)**：導入嚴格「一問一答」互動流程，避免一次列出多個提問。
- **狀態同步 (weekly-summarizer)**：完成週報後，主動將已確認完成之項目更新回當週的 `config/週計畫.md` (僅更新狀態，不複製未完成項目)。

### 視覺化與測試 (Visualizer & Testing)
- **渲染穩定化 (monthly-visualizer)**：明確指定 React 18 與 Tailwind CSS，並修復 Lucide/Framer Motion 等 UMD 組件的全域變數呼叫方式，解決 CDN 衝突白屏問題。
- **授權優化 (monthly-visualizer)**：產出 HTML 檔案後，改為必須先徵詢使用者同意方可啟動 Browser 進行渲染驗證截圖。
- **端到端測試 (skill-tester)**：新增「全工作流測試 (End-to-End Test)」選項，支援連續串接 `habit-tracker` -> `weekly-summarizer` -> `monthly-visualizer` 的全流程演練。

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
