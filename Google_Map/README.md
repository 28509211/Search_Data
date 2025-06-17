# Google_Map - Google 地圖自動化資料收集系統

本專案整合多種自動化工具，協助你從 Google Maps 批次收集座標、店家資訊、圖片、評論等資料，並支援 Google Places API 搜尋。

---

## 📦 安裝依賴套件

建議先建立虛擬環境（如 venv、conda），再安裝所有所需 Python 套件：

```bash
pip install -r requirements.txt
```

請在 Google_Map 資料夾下執行上述指令。

---

## 📁 目錄結構與功能簡介

| 資料夾名稱                  | 功能簡介                                               |
|-----------------------------|--------------------------------------------------------|
| `search_coordinate`         | 產生、比對、管理經緯度座標點，供後續資料收集使用       |
| `search_store_Data`         | 使用爬蟲自動化抓取 Google Maps 店家基本資料             |
| `search_store_Picture`      | 使用爬蟲自動化抓取 Google Maps 店家圖片                 |
| `search_store_Review`       | 使用爬蟲自動化抓取 Google Maps 店家評論                 |
| `search_store_with_google`  | 使用 Google Places API 透過經緯度搜尋附近餐廳           |

---

## 🛠️ 整體使用方式

### 1. 產生座標點

進入 `search_coordinate`，根據需求產生目標區域的經緯度座標點，並輸出到 txt 檔案。

#### (A) 預設方式
```bash
cd Google_Map/search_coordinate
python main.py
```

#### (B) 參數化方式（推薦！）
你可以用 `script.py` 自訂搜尋範圍與條件：
```bash
python script.py -start_x 23.5 -start_y 120.6 -end_x 25.3 -end_y 122.5 -d 400 -diff 50 -n 5
```
- `-start_x`：搜尋範圍左下角緯度
- `-start_y`：搜尋範圍左下角經度
- `-end_x`：搜尋範圍右上角緯度
- `-end_y`：搜尋範圍右上角經度
- `-d`：目標距離（公尺）
- `-diff`：距離容差（公尺）
- `-n`：要產生的座標點數

---

### 2. 搜尋店家

有兩種方式可選：

- **A. 使用 Google Places API**  
  進入 `search_store_with_google`，根據 Excel 經緯度批次搜尋附近店家，結果會寫入 `store_name_address.txt`。

  ```bash
  cd ../search_store_with_google
  python main.py
  # 或用 script.py 參數化
  python script.py -city 桃園 -output my_points.xlsx -apikey_env my_api.env
  ```

- **B. 使用爬蟲搜尋指定店家**  
  進入 `search_store_Data`，將要搜尋的店家名稱寫入 `read.txt`，執行主程式自動抓取店家基本資料。

  ```bash
  cd ../search_store_Data
  python main.py
  # 或用 script.py 參數化
  python script.py -input my_store_list.txt -cant my_cannot_find.txt -found my_already_found.txt
  ```

---

### 3. 收集圖片與評論

- **收集圖片**  
  進入 `search_store_Picture`，將要搜尋的店家名稱寫入 `read.txt`，執行主程式自動抓取圖片網址。

  ```bash
  cd ../search_store_Picture
  python main.py
  # 或用 script.py 參數化
  python script.py -input my_store_list.txt -found my_already_found.txt -roll 3
  ```

- **收集評論**  
  進入 `search_store_Review`，將要搜尋的店家名稱寫入 `read.txt`，執行主程式自動抓取評論。

  ```bash
  cd ../search_store_Review
  python main.py
  # 或用 script.py 參數化
  python script.py -input my_store_list.txt -found my_already_found.txt -sleep 300
  ```

---

## 📄 各模組詳細說明

- 各子資料夾內皆有獨立的 `README.md`，包含安裝、參數、執行方式與輸出說明。
- 請依需求進入對應資料夾閱讀詳細說明與操作指引。

---

## 💡 小提醒

- 各模組皆需安裝對應 Python 套件，詳見各自 README。
- 請遵守 Google Maps 與 Google Places API 的使用規範。
- 所有 txt 檔案皆為 UTF-8 編碼。
