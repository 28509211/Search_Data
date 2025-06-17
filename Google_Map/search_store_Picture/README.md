# search_store_Picture - 店家圖片爬蟲

這個模組用於自動化從 Google Maps 擷取店家圖片網址，並將結果輸出到對應檔案，方便後續分析與應用。

---

## 📁 目錄結構

```
search_store_Picture/
├── function_scrapy_storedata.py   # 圖片爬蟲主程式
├── main.py                       # 主程式，執行圖片抓取流程
├── script.py                     # 參數化執行腳本
├── already_finded_store.txt      # 已經找過的店家
├── store_pictures_found.txt      # 找到的店家圖片網址
├── read.txt                      # 要搜尋的店家清單
└── README.md
```

---

## 🚀 功能說明

- **main.py**  
  執行店家圖片搜尋主程式，會自動比對哪些店家尚未搜尋，並進行圖片網址抓取。

- **script.py**  
  允許用指令列參數自訂輸入/輸出檔案與滑動次數，彈性更高，適合批次或自動化作業。

- **function_scrapy_storedata.py**  
  主要爬蟲邏輯，負責自動化瀏覽 Google Maps，擷取店家圖片網址並寫入檔案。

---

## 🛠️ 如何使用

### 1. 準備搜尋清單

請將你要搜尋的店家名稱，每行一個，寫入 `read.txt`。

### 2. 執行主程式（預設檔案）

1. 進入 `search_store_Picture` 資料夾
2. 執行主程式：
   ```bash
   python main.py
   ```
   程式會自動比對 `already_finded_store.txt`，只搜尋尚未處理過的店家。

### 3. 參數化執行（進階用法）

你可以用 `script.py` 指定不同的輸入/輸出檔案與滑動次數：

```bash
python script.py -input my_store_list.txt -found my_already_found.txt -roll 3
```

- `-input`：要搜尋的店家清單（預設：search_store_Picture/read.txt）
- `-found`：已經找過的店家（預設：search_store_Picture/already_finded_store.txt）
- `-roll`：要滑動幾次以載入更多圖片（預設：1，數字越大抓取圖片越多）

---

## 📄 輸出檔案說明

- `store_pictures_found.txt`  
  每一行為一間店家，包含：店名與所有圖片網址

- `already_finded_store.txt`  
  已經成功搜尋過的店家名稱

---

## 💡 小提醒

- 本爬蟲使用 Selenium，請確保已安裝 ChromeDriver 並可正常啟動
- 建議適當調整滑動次數與搜尋間隔，避免觸發 Google 反爬蟲機制
- 所有 txt 檔案皆為 UTF-8 編碼