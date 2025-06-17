# search_store_Review - 店家評論爬蟲

這個模組用於自動化從 Google Maps 擷取店家評論，並將結果輸出到對應檔案，方便後續分析與應用。具備自動防反爬蟲機制，能自動分批、限時抓取評論。

---

## 📁 目錄結構

```
search_store_Review/
├── function_scrapy_storedata.py   # 評論爬蟲主程式
├── main.py                       # 主程式，執行評論抓取流程
├── script.py                     # 參數化執行腳本
├── already_finded_store.txt      # 已經找過的店家
├── read.txt                      # 要搜尋評論的店家清單
├── review/                       # 存放每家店家評論的資料夾
└── README.md
```

---

## 🚀 功能說明

- **main.py**  
  執行店家評論搜尋主程式，會自動比對哪些店家尚未搜尋，並進行評論抓取。每家店家會限時執行，防止 Google 反爬蟲。

- **script.py**  
  允許用指令列參數自訂輸入/輸出檔案與單次執行秒數，彈性更高，適合批次或自動化作業。

- **function_scrapy_storedata.py**  
  主要爬蟲邏輯，負責自動化瀏覽 Google Maps，擷取店家評論並寫入檔案。

---

## 🛠️ 如何使用

### 1. 準備搜尋清單

請將你要搜尋評論的店家名稱，每行一個，寫入 `read.txt`。

### 2. 執行主程式（預設檔案）

1. 進入 `search_store_Review` 資料夾
2. 執行主程式：
   ```bash
   python main.py
   ```
   程式會自動比對 `already_finded_store.txt`，只搜尋尚未處理過的店家。每家店家評論會限時抓取，避免卡住或被 Google 限制。

### 3. 參數化執行（進階用法）

你可以用 `script.py` 指定不同的輸入/輸出檔案與單次執行秒數：

```bash
python script.py -input my_store_list.txt -found my_already_found.txt -sleep 300
```

- `-input`：要搜尋評論的店家清單（預設：search_store_Review/read.txt）
- `-found`：已經找過的店家（預設：search_store_Review/already_finded_store.txt）
- `-sleep`：單次爬蟲的執行秒數限制（預設：240，數字越大可抓更多評論，但風險也較高）

---

## 📄 輸出檔案說明

- `review/`  
  每家店家一個檔案，內容為評論者與評論內容

- `already_finded_store.txt`  
  已經成功搜尋過評論的店家名稱

---

## ⚙️ 參數與自訂

- 若要調整每家店家評論抓取的時間，請修改 `main.py` 或 `script.py` 的 `sleep_times` 參數
- 若要重複搜尋某些店家，請先從 `already_finded_store.txt` 移除對應名稱

---

## 💡 小提醒

- 本爬蟲使用 Selenium，請確保已安裝 ChromeDriver 並可正常啟動
- 建議適當調整搜尋間隔與單次執行秒數，避免觸發 Google 反爬蟲機制
- 所有 txt 檔案皆為 UTF-8 編碼