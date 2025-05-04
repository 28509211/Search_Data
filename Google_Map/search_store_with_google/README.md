透過收集的經緯度 放在excel檔中 ex: NW.xslx
main.py 就會 把每個經緯度當作中心點以圓的方式 畫半徑去尋找店家
google的這個套件 一個經緯度最多只能找到60個店家，所以在找經緯度時的d設小一點(search_coordinate) 然後在找店家時的r設小一點 建議 r: 200, d = 400

執行main.py 結果存在 store_name_address.txt  