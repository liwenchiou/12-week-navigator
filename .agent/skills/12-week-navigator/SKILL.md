# 🎯 12 週計畫核心引擎 (12-Week Plan Engine)

## 🆕 初次安裝與自動掛載 (Bootstrap & Linking)
**若 Agent 偵測到本套裝已掛載但 `.agent/workflows/` 尚無對應連結，請執行：**
1. **主動詢問**：「偵測到 12-week-navigator 已加入，是否要將專屬工作流連結至系統目錄以啟用 `/` 指令選單？」
2. **執行掛載 (範例指令)**：
   ```bash
   ln -s "$(pwd)/.agent/skills/12-week-navigator/logic/init.md" .agent/workflows/init.md
   ln -s "$(pwd)/.agent/skills/12-week-navigator/logic/start.md" .agent/workflows/start.md
   ln -s "$(pwd)/.agent/skills/12-week-navigator/logic/report-guide.md" .agent/workflows/report-guide.md
   ln -s "$(pwd)/.agent/skills/12-week-navigator/logic/habit-fixer.md" .agent/workflows/habit-fixer.md
   ```

---

## 📋 核心資產依賴 (Data Assets)
本技能執行需依賴於 `workspace/config/` 下的以下實體檔案：
- **`週計畫.md`**：存放週度任務、日期區塊與達成狀態回寫。
- **`核心習慣.md`**：定義「## 核心習慣清單」及其對應項目。
- **`月計畫.md`**：存放月度預計達成目標。

> 💡 若尚未建立，請從 `resources/samples/` 複製範本後置於 `workspace/config/`。

---

## 🛰️ 模組 1：每日紀錄 (Daily Habit Tracker)

**觸發關鍵字**：「紀錄今天」、「開始紀錄」。

1. **讀取配置**：讀取 `workspace/config/核心習慣.md` 下的「## 核心習慣清單」。
2. **一問一答**：嚴格遵守「逐項互動原則」，次僅問一個習慣。
3. **快捷判定**：若回覆「完美達成」，後續項目直接標註 ✅。
4. **狀態評估**：詢問「能量/環境情緒 (1-5 分)」與「本日心得小結」。
5. **實體存檔**：存至 `workspace/data/YYYY/MM/daily/YYYYMMDD.md`。

---

## 📊 模組 2：週報復盤 (Weekly Summarizer)
**觸發關鍵字**：「產出週報」、「週日總結」。

1. **🛡️ JIT 校驗**：僅掃描當週 7 天日誌，確認 Schema 格式正確。
2. **任務確認**：讀取 `workspace/config/週計畫.md` 當週區塊，逐條詢問達成狀態。
3. **數據計算**：執行分 = (已達成 / 總項數) * 100。
4. **深度回顧**：依「主題」整合日誌原文。**🚫 禁 AI 評語**。
5. **對策提煉**：詢問「🚧 阻礙原因」與「🌟 核心金句」。
6. **狀態回寫**：將確認結果更新回 `workspace/config/週計畫.md`。

---

## 🏆 模組 3：月度戰略與視覺化 (Monthly Strategy & Visualizer)
**觸發關鍵字**：「執行月度總結」、「產出網頁」。

### 階段 A：數據彙整 (Reporter)
1. **🛡️ JIT 校驗**：僅掃描當月 4-5 份週報實體檔案。
2. **跨週整合**：擷取全月週報的評分、阻礙、獲益與金句。
3. **目標比對**：逐條確認 `workspace/config/月計畫.md` 達成現況並回寫狀態。
4. **靈魂提案**：根據數據提煉 3-5 組「兩字核心標語 (Slogan)」。

### 階段 B：視覺化封裝 (Visualizer)
1. **🛡️ JIT 校驗**：確認當月月報 MD 檔案存在。
2. **設計介入**：**必須**先執行 `ui-ux-pro-max` 腳本取得配色指南。
3. **網頁生成**：產出單一 HTML (React 18 + Tailwind + Framer Motion)。
4. **繁體中文強制**：所有區塊標題必須使用繁體中文。

---

## 🛡️ 核心開發者協定 (Consolidated Protocols)

1. **逐項互動原則 (Single-Question)**：在任何確認環節，嚴禁合併問題。
2. **忠實紀錄原則 (Faithful Recording)**：嚴禁 AI 評語、詮釋或美化。
3. **局部更新策略 (Partial Update)**：優先使用局部修改指令修改檔案。
4. **沙盒隔離原則 (Sandbox)**：測試請求一律限制在 `workspace/sandbox/` 目錄。
5. **PDCA 螺旋**：所有報告必須包含「阻礙分析」與「下一步對策」。

---
*Portable Module v2.1 | Designed for High-Output Engineers*
