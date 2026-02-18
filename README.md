# Eternal Line - 來不及說的一句話 (AI 數位遺產與思念延續平台)

## 專案簡介
本專案旨在參加「2026 經濟部智慧創新大賞 (Best AI Awards)」。
透過先進的 AI 技術，將逝者的文字風格與聲音特徵轉化為具備溫度的數位存在，實現「數位永生」的情感聯結，並強調「可信任 AI (Trustworthy AI)」與資料主權。

## 核心價值
1. **情感撫慰**：解決失去親人的情感斷裂，重現家人的語氣與關懷。
2. **官方認證**：透過 LINE 官方認證系統，確保資料真實性並防止 AI 詐騙。
3. **資料安全**：所有數據加密儲存於 LINE 生態圈內，保障用戶隱私。

## 技術架構
- **多租戶靈魂工廠 (Multi-Tenant Soul Factory)**：
    - 支援「一人一箱 (Soul Box)」機制，確保每個用戶的訓練數據與機器人完全獨立且物理隔離。
    - 提供標準化 `.txt` 匯入流程，實現服務的可複製性與規模化。
- **人格鎖定與防禦 (Immutable Identity Manifest)**：
    - 每個數位靈魂具備專屬的 `manifest.json`，鎖定語助詞頻率、Emoji 密度與表達邏輯。
    - **防外力干擾機制**：內建「身份保護層 (Identity Clamp)」，防止用戶透過 Prompt Injection 更改機器人的個性或破壞人設。
    - **語言基準稽核 (Linguistic Baseline Audit)**：回覆生成後會自動對照 Manifest 基準，若偏離原有人格 DNA（如語氣突變）將觸發警告並重新生成。
- **文字風格引擎 (Stylistic Engine)**：
    - 使用 OpenClaw 與 Claude 進行 LINE 匯出文本 (.txt) 的特徵提取。
    - 採用 RAG (檢索增強生成) 結合歷史語境，重現特定回覆節奏。
- **語音克隆系統 (Voice Cloning)**：
    - 從語音訊息提取聲紋，整合 GPT-SoVITS 生成具情緒起伏的模擬語音。
- **悲傷守護機制 (Grief Guard)**：
    - 內建情緒監測中間件，偵測過度依賴或負面情緒時主動介入並提供建議。
- **全端平台**：
    - 前端/API：Next.js
    - 機器人介面：LINE Messaging API

## 目錄結構
- `src/api`：LINE Bot Webhook 與後端接口。
- `src/engine/stylistic`：文字風格清洗與檢索處理。
- `src/engine/voice`：語音特徵提取與 TTS 整合。
- `src/middleware/safety`：Grief Guard 情緒監測機制。

---
*Developed by 蝦妹 Assistant (Powered by OpenClaw)*
