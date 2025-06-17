# search_store_Data - 店家基本資料爬蟲

這個模組用於自動化從 Google Maps 擷取店家資訊（營業時間、電話、地址、內用外帶、餐廳類型），並將結果輸出到對應檔案，方便後續分析與應用。

---

## 📁 目錄結構

```
search_store_Data/
├── function_scrapy_storedata.py   # 店家資料爬蟲主程式
├── main.py                       # 主程式，執行資料抓取流程
├── script.py                     # 參數化執行腳本
├── already_finded_store.txt      # 已經找過的店家
├── store_can_not_found.txt       # 找不到或搜尋錯誤的店家
├── storedata.txt                 # 找到的店家詳細資料
├── read.txt                      # 要搜尋的店家清單
└── README.md
```

---

## 🚀 功能說明

- **main.py**  
  執行店家資料搜尋主程式，會自動比對哪些店家尚未搜尋，並進行資料抓取。

- **script.py**  
  允許用指令列參數自訂輸入/輸出檔案，彈性更高，適合批次或自動化作業。

- **function_scrapy_storedata.py**  
  主要爬蟲邏輯，負責自動化瀏覽 Google Maps，擷取店家資訊並寫入檔案。

---

## 🛠️ 如何使用

### 1. 準備搜尋清單

請將你要搜尋的店家名稱，每行一個，寫入 `read.txt`。

### 2. 執行主程式（預設檔案）

1. 進入 `search_store_Data` 資料夾
2. 執行主程式：
   ```bash
   python main.py
   ```
   程式會自動比對 `already_finded_store.txt` 和 `store_can_not_found.txt`，只搜尋尚未處理過的店家。

### 3. 參數化執行（進階用法）

你可以用 `script.py` 指定不同的輸入/輸出檔案：

```bash
python script.py -input my_store_list.txt -cant my_cannot_find.txt -found my_already_found.txt
```

- `-input`：要搜尋的店家清單（預設：search_store_Data/read.txt）
- `-cant`：找不到或搜尋錯誤的店家（預設：search_store_Data/store_can_not_found.txt）
- `-found`：已經找過的店家（預設：search_store_Data/already_finded_store.txt）

---

## 📄 輸出檔案說明

- `storedata.txt`  
  每一行為一間店家，包含：店名、營業時間、地址、電話、內用外帶、餐廳類型等資訊

- `already_finded_store.txt`  
  已經成功搜尋過的店家名稱

- `store_can_not_found.txt`  
  找不到或搜尋失敗的店家名稱

---

## 💡 小提醒

- 本爬蟲使用 Selenium，請確保已安裝 ChromeDriver 並可正常啟動
- 建議適當調整搜尋間隔，避免觸發 Google 反爬蟲機制
- 所有 txt 檔案皆為 UTF-8 編碼

already_finded_store.txt: 放入已經找過的店家
store_can_not_found.txt: 放入找不到或是搜尋遇到error的店家
storedata.txt: 放找到店家+店家資料(營業時間，電話，地址，內用外帶，餐廳類型)
read.txt:  放要找的店家


執行main.py即可