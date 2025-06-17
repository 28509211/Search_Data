# search_coordinate - 座標點搜尋工具

這個模組用於自動化產生、比對地理座標點，並將結果輸出到對應檔案，方便後續用於 Google Maps 店家資料收集。

---

## 📁 目錄結構

```
search_coordinate/
├── compare.py            # 比對新舊座標，產生未出現過的新座標
├── main.py               # 主程式，執行座標搜尋流程
├── map_place_point.py    # 輸出座標到檔案，方便複製到 Excel
├── map_point.py          # 座標搜尋工具
├── point_result/
│   ├── new_point.txt         # 這次找到的座標點
│   ├── point.txt             # 歷史所有找過的座標點
│   └── real_new_point.txt    # 之前從未出現過的新座標點
└── README.md
```

---

## 🚀 功能說明

- **main.py**  
  執行座標搜尋主程式，根據設定條件自動產生座標點，並將結果寫入 `point_result/` 相關檔案。

- **map_point.py**  
  提供搜尋座標的工具函式。

- **map_place_point.py**  
  讀取指定 txt 檔案，分別印出 x/y 座標，方便複製到 Excel。

- **compare.py**  
  比對新舊座標，產生 `real_new_point.txt`，顯示從未出現過的新座標。

---

## 🛠️ 如何使用

### 1. 直接執行 main.py

1. 進入 `search_coordinate` 資料夾
2. 執行主程式：
   ```bash
   python main.py
   ```
   預設會根據程式內設定的範圍與參數，自動產生座標點，並輸出到 `point_result/` 目錄下。

### 2. 自訂搜尋參數

打開 `main.py`，你可以修改以下參數來調整搜尋範圍與條件：

```python
start_x = 23.5667   # 搜尋範圍左下角緯度
start_y = 120.6167  # 搜尋範圍左下角經度
end_x = 25.3333     # 搜尋範圍右上角緯度
end_y = 122.5       # 搜尋範圍右上角經度

d = 400             # 目標距離（公尺）
d_different = 50    # 距離容差（公尺）
n = 5               # 要產生的座標點數
```

### 3. 進階：用 script.py 參數化執行（如有）

如果有 `script.py`，可用指令列參數執行：
```bash
python script.py -start_x 23.5 -start_y 120.6 -end_x 25.3 -end_y 122.5 -d 400 -diff 50 -n 5
```
這樣可以不用修改程式碼，直接指定搜尋範圍與條件。

---

## 📄 輸出檔案說明

- `point_result/new_point.txt`  
  這次新找到的座標點（覆蓋寫入）。

- `point_result/point.txt`  
  歷史所有找過的座標點（累加寫入）。

- `point_result/real_new_point.txt`  
  之前從未出現過的新座標點（覆蓋寫入）。

---

## 💡 小提醒

- 可搭配 `map_place_point.py` 輸出座標，方便複製到 Excel。
- 使用 `compare.py` 可快速比對新舊座標，找出真正的新座標點。
- 所有 txt 檔案皆為 UTF-8 編碼。