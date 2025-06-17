# Search_data - Google Maps Data Collection System

這是一個完整的 Google Maps 資料收集系統，用於自動化收集餐廳資訊、圖片、評論等資料。

## 📁 專案結構

```
Search_data/
├── Google_Map/
│   ├── search_coordinate/          # 座標點搜尋工具
│   ├── search_store_Data/          # 店家基本資料爬蟲
│   ├── search_store_Picture/       # 店家圖片爬蟲
│   ├── search_store_Review/        # 店家評論爬蟲
│   └── search_store_with_google/   # Google API 店家搜尋
└── README.md
```

## 🚀 功能模組

### 1. search_coordinate - 座標點搜尋
**功能**: 尋找符合條件的座標點

**主要檔案**:
- `main.py` - 主執行檔
- `map_point.py` - 座標搜尋工具
- `map_place_point.py` - 座標輸出工具（方便複製到 Excel）
- `compare.py` - 比較工具，產生新的座標點

**輸出檔案**:
- `point_result/real_new_point.txt` - 之前從未出現的座標點
- `point_result/new_point.txt` - 這次找到的座標點
- `point_result/point.txt` - 之前找過的所有座標點

### 2. search_store_Data - 店家基本資料爬蟲
**功能**: 使用爬蟲技術從 Google Maps 抓取店家基本資訊

**輸入檔案**:
- `read.txt` - 要搜尋的店家清單

**輸出檔案**:
- `storedata.txt` - 店家詳細資料（營業時間、電話、地址、內用外帶、餐廳類型）
- `already_finded_store.txt` - 已經搜尋過的店家
- `store_can_not_found.txt` - 找不到或搜尋錯誤的店家

### 3. search_store_Picture - 店家圖片爬蟲
**功能**: 從 Google Maps 抓取店家圖片

**輸入檔案**:
- `read.txt` - 要搜尋圖片的店家清單

**輸出檔案**:
- `store_pictures_found.txt` - 找到的店家圖片 URL
- `already_finded_store.txt` - 已經搜尋過的店家

### 4. search_store_Review - 店家評論爬蟲
**功能**: 收集店家的評論資料

**特色**:
- 自動防反爬蟲機制（time.sleep）
- 自動刪除舊 process 並重新啟動
- 可調整滑動次數和搜尋時間

**輸入檔案**:
- `read.txt` - 要收集評論的店家清單

**輸出檔案**:
- `review/` - 評論資料夾，包含評論者和評論內容
- `already_finded_store.txt` - 已經搜尋過的店家

**可調整參數**:
- `__scroll_Review` 中的 `save_round`: 每次滑動次數 × 10 = 緩存評論的頻率
- `main.py` 中的 `sleep_times`: 控制每個店家搜尋評論的時間

### 5. search_store_with_google - Google API 店家搜尋
**功能**: 使用 Google Places API 透過經緯度搜尋附近店家

**特色**:
- 使用官方 Google API，更穩定可靠
- 以經緯度為中心點，圓形範圍搜尋
- 每個經緯度最多可找到 60 個店家

**輸入檔案**:
- Excel 檔案（如 `NW.xlsx`）- 包含經緯度座標

**輸出檔案**:
- `store_name_address.txt` - 店家名稱和地址

**建議參數**:
- 搜尋半徑 `r`: 200 公尺
- 座標間距 `d`: 400 公尺

## 🛠️ 使用方式

### 基本流程
1. **準備座標**: 使用 `search_coordinate` 產生經緯度座標
2. **搜尋店家**: 使用 `search_store_with_google` 或 `search_store_Data` 找到店家
3. **收集資料**: 使用 `search_store_Data` 收集詳細店家資訊
4. **收集圖片**: 使用 `search_store_Picture` 收集店家圖片
5. **收集評論**: 使用 `search_store_Review` 收集店家評論

### 執行方式
每個模組都有 `main.py` 檔案，直接執行即可：
```bash
cd Google_Map/search_coordinate
python main.py
```

## 📋 注意事項

1. **API 限制**: Google Places API 有使用限制，建議適當調整搜尋參數
2. **反爬蟲**: 爬蟲模組已內建防反爬蟲機制，請勿過度頻繁執行
3. **檔案編碼**: 所有文字檔案使用 UTF-8 編碼
4. **座標精度**: 建議使用較小的搜尋半徑以獲得更好的結果

## 🔧 技術需求

- Python 3.x
- 相關套件：
  - `googlemaps` - Google Places API
  - `pandas` - Excel 檔案處理
  - `selenium` - 網頁爬蟲
  - `dotenv` - 環境變數管理

## 📝 授權

此專案僅供學習和研究使用，請遵守相關網站的使用條款和 API 使用規範。
