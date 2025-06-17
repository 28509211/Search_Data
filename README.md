# Search_data - Google Maps 批次資料收集系統

本專案為一套完整的 Google Maps 自動化資料收集工具，支援批次產生座標、搜尋店家、抓取店家資訊、圖片、評論，並可用 Google Places API 進行高效搜尋。適合地理資訊、商業分析、資料科學等應用。

---

## 📁 目錄結構

```
Search_data/
├── Google_Map/
│   ├── search_coordinate/         # 產生、比對經緯度座標點
│   ├── search_store_Data/         # 爬蟲抓取店家基本資料
│   ├── search_store_Picture/      # 爬蟲抓取店家圖片
│   ├── search_store_Review/       # 爬蟲抓取店家評論
│   └── search_store_with_google/  # Google API 搜尋附近店家
│   ├── README.md                  # Google_Map 詳細說明
│   ├── requirements.txt           # 依賴套件清單
└── README.md                      # 本檔案
```

---

## 🚀 快速開始

1. **安裝依賴套件**  
   進入 `Google_Map` 資料夾，安裝所有 Python 依賴：
   ```bash
   pip install -r requirements.txt
   ```

2. **依需求選擇模組**  
   - 產生座標：`search_coordinate`
   - 搜尋店家：`search_store_with_google` 或 `search_store_Data`
   - 收集店家資訊：`search_store_Data`
   - 收集圖片：`search_store_Picture`
   - 收集評論：`search_store_Review`

3. **每個模組皆有詳細 README**  
   請進入對應子資料夾，參考其 `README.md` 取得參數、執行方式與範例。

---

## 📝 推薦流程

1. 用 `search_coordinate` 產生目標區域的經緯度座標。
2. 用 `search_store_with_google` 搜尋店家。
3. 用 `search_store_Data`、`search_store_Picture`、`search_store_Review` 收集店家詳細資料、圖片與評論。

---

## 💡 小提醒

- 強烈建議使用虛擬環境（venv、conda）安裝依賴。
- 請遵守 Google Maps 與 Google Places API 的使用規範。
- 各模組皆有獨立 README，請依需求詳閱。
