---
name: git-manager
description: 遵循 12 週計畫系統的 Git 分支管理與提交規範 (繁體中文條列式)。
---

## 🚨 liwen 個人分支 SOP（強制遵守）

本專案維護**雙分支架構**，使用者 `liwen` 的個人資料（日誌、週報、月報、config、_doc）**僅存在於 `liwen` 分支**，`main` 分支僅為公開框架骨架。Agent **必須嚴格遵守以下規則**。

### 分支職責對照表

| 分支 | 包含內容 | 推送目標 |
|---|---|---|
| `main` | `.agent/`、`README.md`、`CHANGELOG.md`、範本檔 | `origin main` + `framework main` |
| `liwen` | `main` 的全部 + `data/`、`config/`、`reports/`、`_doc/` | `origin liwen` 只 |

> ⚠️ **嚴禁** 將 `liwen` 分支推送到 `framework`。個人資料絕對不能進公開框架。

---

### 🔁 日常使用 SOP（非 Skill 修改）

每次操作前確認分支：
```bash
git checkout liwen
```

改完個人紀錄後推送：
```bash
git add .
git commit -m "[personal]: 說明本次更新內容"
git push origin liwen
# ⛔ 不執行 git push framework
```

---

### 🔧 修改 Skill / .agent/ 時的 SOP（嚴格執行）

当 `.agent/` 內有變更且使用者要求 Git 時，Agent **必須依以下順序執行**：

#### Step 1：在 `liwen` 確認修改內容齊全
```bash
git checkout liwen
git add .agent/ CHANGELOG.md README.md
git commit -m "[feat|fix]: Skill 修改說明"
```

#### Step 2：將 Skill 變更同步到 `main`
```bash
git checkout main

# 從 liwen 取出 .agent/ 與文件（不含個人資料）
git checkout liwen -- .agent/
git checkout liwen -- CHANGELOG.md
git checkout liwen -- README.md

git add .agent/ CHANGELOG.md README.md
git commit -m "[feat|fix]: 同步 Skill 修改（liwen → main）"

# 僅推送私人 repo（my-12-week-goal）
git push origin main
# ⛔ 不自動推 framework，需等使用者說「發行」才執行
```

#### Step 3：回 `liwen`，合併 main 的更新
```bash
git checkout liwen
git merge main
git push origin liwen
```

#### ✅ 完成後 — 必問發行確認

**每次完成上述 Git 流程後，Agent 必須詢問：**

> 「Git 已完成 ✅
> 是否要將此版本發行到 `12-week-navigator`（公開框架）？
> **A. 發行**（執行 `git push framework main`）
> **B. 不發行**（保留在私人 repo 即可）」

收到回覆後再執行對應動作。若使用者選 A，執行發行 SOP；若選 B，直接結束。

---

### ⛔ 嚴禁事項

1. **禁止** 在 `main` 分支直接修改個人資料（data/config/reports）
2. **禁止** 執行 `git push framework liwen`
3. **禁止** 在 `liwen` 略過 Step 2，直接只 push liwen 而不同步 main（會造成 Skill 版本落差）
4. 若使用者只說「push」或「git」，**必須先詢問**：「請問這次是個人紀錄更新，還是有 Skill 修改需要同步到 main？」

---
# Git 管理執行邏輯

當使用者要求「執行 Git 相關作業」時，Agent 應遵循以下標準化流程：

## 第一階段：開發分支管理 (Branching)
0. **執行方式確認 (Token Optimization)**：
   - **關鍵步**：在開始任何 Git 流程前，**必須詢問使用者**：「請問接下來的 Git 指令是要『由 Agent 自動執行』還是『列出指令由使用者手動執行』？」
1. **建立分支**：在開始實作新功能或修復前，建立一個明確命名的分支。
   - **格式**：`[feat|fix|refactor|ui]/[日期或功能描述]` (例如：`feat/system-optimization-20260225`)。
   - **指令**：`git checkout -b <branch-name>`。

## 第二階段：變更提交 (Commit Policy)
1. **策略確認 (Strategy Confirmation)**：
   - **關鍵步**：在執行任何 `git add` 或 `git commit` 前，**必須詢問使用者**：「請問本次變更是要『發送 Pull Request (PR)』還是『直接合併 (Direct Merge)』？」
2. **暫存變更**：`git add .`。
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
1. **合併 PR 並清理遠端**：若使用者授權本地合併，優先使用 `gh pr merge --merge --delete-branch`。
   - **注意**：`--delete-branch` 會同時刪除遠端與本地的分支，是保持倉庫整潔的關鍵指令。
2. **切換回主分支**：`git checkout main`。
3. **拉取與修剪**：執行 `git pull origin main` 並配合 `git fetch --prune` 確保本地的遠端引用完全同步。
4. **刪除本地分支**：若分支仍存在，執行 `git branch -d <branch-name>`。
5. **開源節點同步 (Framework Sync)**：**不自動執行**。僅在使用者明確說「發行」或「推 framework」時才執行（見下方發行 SOP）。

---

## 🚀 發行 SOP（使用者說「發行」時才執行）

> **觸發條件**：使用者明確說「發行」、「推 framework」、「更新開源版本」。
> **目的**：將目前 `my-12-week-goal/main` 的穩定版本同步到 `12-week-navigator`（公開框架）。

```bash
# 確認目前在 main 且是最新狀態
git checkout main
git pull origin main

# 推送到公開框架 repo
git push framework main
```

> 發行後，`12-week-navigator` 即為最新穩定版，社群可以 fork/clone 使用。

---
