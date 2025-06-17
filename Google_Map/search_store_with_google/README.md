# search_store_with_google - Google API 店家搜尋

這個模組用於自動化透過 Google Places API 及經緯度座標，搜尋附近的餐廳店家，並將結果輸出到對應檔案，方便後續分析與應用。

---

## 📁 目錄結構

```
search_store_with_google/
├── google_find_store.py           # Google API 搜尋主程式
├── main.py                        # 主程式，執行店家搜尋流程
├── script.py                      # 參數化執行腳本
├── google_api_key.env             # Google API 金鑰（需自行填入）
├── NW .xlsx                       # 範例座標 Excel 檔案
├── store_name_address.txt         # 找到的店家名稱與地址
└── README.md
```

---

## 🚀 功能說明

- **main.py**  
  執行 Google API 店家搜尋主程式，會自動讀取 Excel 檔案中的經緯度座標，並搜尋每個座標附近的餐廳。

- **script.py**  
  允許用指令列參數自訂城市、Excel 檔案、API 金鑰路徑，彈性更高，適合批次或自動化作業。

- **google_find_store.py**  
  主要搜尋邏輯，負責呼叫 Google Places API，並將搜尋到的店家名稱與地址寫入檔案。

---

## 🛠️ 如何使用

### 1. 準備 Google API 金鑰

請將你的 Google Places API 金鑰填入 `google_api_key.env`，格式如下：
```
API_KEY=你的金鑰
```

### 2. 準備座標 Excel 檔案

請準備一個 Excel 檔案（如 `NW .xlsx`），內容需包含兩欄，分別為 `[城市名]N` 和 `[城市名]W`，例如：
- 桃園N
- 桃園W

每一列為一組經緯度座標。

### 3. 執行主程式（預設檔案）

1. 進入 `search_store_with_google` 資料夾
2. 編輯 `main.py`，設定你要搜尋的城市名稱與 Excel 檔案名稱，例如：
   ```python
   city = "桃園"
   Find_Store_With_Google(YOUR_API_KEY, city, file_name="NW .xlsx")
   ```
3. 執行主程式：
   ```bash
   python main.py
   ```
   程式會自動搜尋每個座標附近的餐廳，並將結果寫入 `store_name_address.txt`。

### 4. 參數化執行（進階用法）

你可以用 `script.py` 指定不同的城市、Excel 檔案與 API 金鑰路徑：

```bash
python script.py -city 桃園 -output my_points.xlsx -apikey_env my_api.env
```

- `-city`：要搜尋的城市名稱（需與 Excel 欄位一致，必填）
- `-output`：Excel 檔案名稱（預設：NW .xlsx）
- `-apikey_env`：API 金鑰 .env 檔路徑（預設：search_store_with_google/google_api_key.env）

---

## ⚙️ 參數與自訂

- `city`：Excel 檔案中座標欄位的城市名稱（如 `"桃園"`）
- `file_name`/`-output`：Excel 檔案名稱（如 `"NW .xlsx"`）
- `r`：搜尋半徑（公尺，預設 200），可在 `google_find_store.py` 內自訂
- `apikey_env`：API 金鑰 .env 檔路徑

> **建議**  
> Google Places API 每個座標最多只能找到 60 家店家。建議將搜尋半徑 `r` 設小一點（如 200），並在產生座標時（search_coordinate）將座標間距 `d` 設小一點（如 400），以獲得更完整的資料。

---

## 📄 輸出檔案說明

- `store_name_address.txt`  
  每一行為一間店家，包含：店名與地址（重複自動排除）

---

## 💡 小提醒

- 本模組需安裝 `googlemaps`、`pandas`、`python-dotenv` 等套件
- 請確保 Google API 金鑰有效且有啟用 Places API
- 所有 txt 檔案皆為 UTF-8 編碼

透過收集的經緯度 放在excel檔中 ex: NW.xslx
main.py 就會 把每個經緯度當作中心點以圓的方式 畫半徑去尋找店家
google的這個套件 一個經緯度最多只能找到60個店家，所以在找經緯度時的d設小一點(search_coordinate) 然後在找店家時的r設小一點 建議 r: 200, d = 400

執行main.py 結果存在 store_name_address.txt  