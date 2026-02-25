---
name: git-manager
description: 遵循 12 週計畫系統的 Git 分支管理與提交規範 (繁體中文條列式)。
---

# Git 管理執行邏輯

當使用者要求「執行 Git 相關作業」時，Agent 應遵循以下標準化流程：

## 第一階段：開發分支管理 (Branching)
1. **建立分支**：在開始實作新功能或修復前，建立一個明確命名的分支。
   - **格式**：`[feat|fix|refactor|ui]/[日期或功能描述]` (例如：`feat/system-optimization-20260225`)。
   - **指令**：`git checkout -b <branch-name>`。

## 第二階段：變更提交 (Commit Policy)
1. **暫存變更**：`git add .`。
2. **提交規格**：**必須** 使用繁體中文且為條列式說明。
   - **格式**：
     ```bash
     git commit -m "[類型]: 標題" -m "1. 條列詳細內容一
     2. 條列詳細內容二"
     ```
   - **Commit 標籤**：
     - `feat`: 新增功能/Skills
     - `fix`: 修補 Bug 或格式
     - `refactor`: 重構代碼或調整目錄結構
     - `ui`: 調整簡報網頁樣式
     - `doc`: 更新文件

## 第三階段：遠端推送與自動化 PR (Push & PR)
1. **推送分支**：`git push origin <branch-name>`。
2. **自動建立 PR**：
   - **偵測元件**：執行 `command -v gh` 檢查是否可調用。
   - **指令**：若存在，執行 `gh pr create --title "[類型]: 標題" --body "1. 條列說明內容"`。
   - **手動回歸**：若未安裝 `gh` 或未登入，則告知使用者：「由於環境缺少 GitHub CLI，請手動至 GitHub 網頁版建立 PR。」並提供 Git 分支推送成功的通知。
3. **通知使用者**：提供 PR 連結，並等待使用者完成線上審核。

## 第四階段：收尾與回歸 (Cleanup)
1. **切換回主分支**：`git checkout main`。
2. **拉取最新變更**：`git pull origin main` (確保遠端 Merge 過後的代碼同步回本地)。
3. **刪除本地分支**：`git branch -d <branch-name>`，保持工作區整潔。

---
