# Eternal Line - 專案開發里程碑 (Project Roadmap)

## 🏁 Phase 1: 地基與大腦 (已完成)
- [x] **專案初始化**：搭建 Next.js + Python + OpenClaw 混合架構。
- [x] **文字風格引擎 (Stylistic Engine)**：完成 LINE `.txt` 清洗與特徵分析。
- [x] **靈魂工廠 (Soul Factory)**：實現「一人一箱」多租戶機制，確保各用戶數據隔離。
- [x] **身分保護層 (Identity Clamp)**：實作 Manifest 鎖定機制，防止個性被外力更改。
- [x] **悲傷守護 (Grief Guard)**：建立情緒監測中間件，確保 Trustworthy AI 倫理。

## 🚀 Phase 2: 感官與串接 (進行中)
- [ ] **語音克隆 (Voice Engine)**：
    - [x] 收到 Mico 素材。
    - [ ] 待做：執行聲紋提取 (Embedding) 與 TTS 推理測試。
- [ ] **視覺延續 (Visual Factory)**：
    - [x] 制定影像生成規範 (`IMAGE_GEN_SPEC.md`)。
    - [ ] 待做：串接 Gemini Vision 進行「視覺 DNA」提取 (等待照片素材)。
- [x] **GitHub 倉庫建立**：已成功建立並推送至 https://github.com/kenhuangch/line-ai-memorial
- [ ] **LINE 實戰串接**：
    - [x] 刻好 Webhook API 骨架。
    - [x] 配置 LINE Developers 憑證：已收到 Channel ID 與 Secret。
    - [ ] 待做：獲取 **Channel Access Token (Long-lived)** 並部署到 Vercel 進行真機測試。

## 🏆 Phase 3: 比賽衝刺 (待啟動)
- [ ] **作品說明書撰寫**：整合技術優勢（可信任 AI、靈魂隔離、Grief Guard）。
- [ ] **Demo 影片製作**：展示從「文字模仿」到「擬真新生活照」的完整貼心體驗。

---
*Last Updated: 2026-02-19 00:05*
