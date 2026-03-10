---
name: skill-tester
description: 負責 Skills 的測試沙盒管理。提供隔離的測試環境，防止測試數據污染正式資料夾。
---

# 沙盒測試執行邏輯 (Skill Tester - Sandbox)

當使用者發起「測試 [Skill 名稱]」或「進入測試模式」時，請執行以下流程：

## 第一階段：環境初始化 (Setup)
1. **建立沙盒**：確保 `workspace/sandbox/` 目錄及其完整子目錄已建立：
   - `workspace/config/`
   - `workspace/data/YYYY/MM/daily/`
   - `workspace/data/YYYY/weekly/`
   - `workspace/data/YYYY/monthly/`
   - `workspace/reports/`
2. **數據同步**（可選）：詢問使用者是否需要從正式資料夾複製現有配置作為測試樣本。
   - 若需要，執行：`cp -r workspace/config/* workspace/sandbox/config/`。

## 第二階段：模擬執行 (Execution)
1. **路徑重定向**：在執行該 Skill 的過程中，**所有** 文件讀寫操作必須強制導向 `workspace/sandbox/`。
   - 正式：`/workspace/data/YYYY/MM/daily/` -> 測試：`workspace/sandbox/workspace/data/YYYY/MM/daily/`
   - 正式：`/workspace/reports/` -> 測試：`workspace/sandbox/workspace/reports/`

2. **模式選擇**：
    - **A. 自動生成測試 (Automation Test)**：**全自動一鍵完成**。AI 將主動判斷語境並自動產出全鏈條模擬檔案（Daily x10 -> Weekly x1 -> Monthly x1 -> HTML），內容以「一句話模擬」為主。過程中 **不需詢問使用者**，用於快速驗證系統路徑與渲染。
    - **B. 完整互動測試 (Live Interactive Test)**：AI 真的啟動詢問流程，與使用者進行一問一答的對話，最後將結果存入沙盒。
    - **C. 全場景模擬測試 (Full Lifecycle Simulation)**：**全自動深度模擬**。AI 將主動判斷語境並產出具備「高度真實感」的豐富模擬數據（含具體心得、各週偏差分析與靈魂金句提煉）。過程中 **不需詢問使用者**，用於在不活動的情況下，完整預覽系統在「數據飽和」狀態下的報表內容與美學表現。

3. **執行步驟 (針對互動測試)**：
    - 宣告：「進入 [Skill 名稱] 互動測試模式」。
    - 嚴格依照該 Skill 的「互動機制」進行問答。
    - 最終驗證：將對話結果寫入沙盒檔案，並呈報結果。

## 第三階段：環境清理 (Teardown)
1. **詢問清理**：測試完成後，主動詢問「測試已結束，是否要清空沙盒環境？」
2. **執行刪除**：使用者確認後，執行 `rm -rf workspace/sandbox/*` 並重新建立空的子目錄，保持整潔。

---

## 🛡️ 執行準則
- **隔離原則**：嚴格遵循 `instructions.md` 中的 **「沙盒隔離原則」**。
- **透明度**：開始前應告知使用者：「已啟動沙盒測試模式，所有變動僅限於 workspace/sandbox/ 目錄。」
- **防錯機制**：若未進入沙盒模式即進行 Skill 修改後的執行，應主動建議先進行 `skill-tester` 驗證。
