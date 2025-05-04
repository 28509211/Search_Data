import googlemaps
import time
from dotenv import dotenv_values

import pandas as pd
import numpy as np
import time 
import os

# 選擇excel表中的 第一欄位 ex: NW.xlsx 的格式
# city 第一欄位 的名稱
def load_data( city, file_name ):

    print( "--------------------------------載入座標------------------------------------------")

    location = []

    df = pd.read_excel(f"search_store_with_google\\{file_name}",
                         usecols=[f"{city}N", f"{city}W"])

    df = df.dropna()

    print( f"共有多少個座標: { len(df) } ")

    for number in range(len(df)):

        location.append([df[f"{city}N"][number], df[f"{city}W"][number]])


    return location

# 把找到的店家名稱和店家地址寫入store_name_address.txt 並進行排除重複
def place(places_result, times):
   
    existing_name_address = set()

    if os.path.exists('search_store_with_google\\store_name_address.txt'):
        with open('search_store_with_google\\store_name_address.txt', 'r', encoding='utf-8') as f:
            for line in f:
                existing_name_address.add(line.strip())

    for place_item in places_result['results']:
        name = place_item['name']
        address = place_item['vicinity']
        
        name_only = name.strip()
        name_address = f"{name}\t{address}".strip()


        # 如果名字+地址已經存在，也跳過
        if name_address in existing_name_address:
            continue

        times = times + 1
        print(times)
        print(f"餐廳名稱: {name}")
        print(f"地址: {address}")
        print("------")


        existing_name_address.add(name_address)

        with open('search_store_with_google\\store_name_address.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name_address}\n")

    return times


# 使用google的服務去找該經緯度附近多少公尺為圓，附近的店家名稱 地址
# city 就是在excel檔中的第一欄的名稱 可以參考NW.xlsx
def Find_Store_With_Google( YOUR_API_KEY, city, file_name, r=200 ) :

 
    gmaps = googlemaps.Client(key=YOUR_API_KEY)

    times = 0


    all_location = load_data(city, file_name)
    all_times = 0

    for i in all_location:

        location = f"{i[0]},{i[1]}"
        print(f"==============================={city} {location}{r}m searching START===============================\n")
        print(f"在目前位置的附近餐廳:")
        places_result = gmaps.places_nearby(location=location, radius=r, type='restaurant', open_now=False, language='zh-TW')

        times = place(places_result, times)

        page = None
        try:
            page = places_result['next_page_token']
        except Exception as e:
            pass
            

        while page and page != None:

            time.sleep(10)

            try:
                places_result2 = gmaps.places_nearby(page_token=page, type='restaurant', language='zh-TW')
                times = place(places_result2, times)

                page = places_result2['next_page_token']
            except Exception as e:
                break


        print(f"==============================={city} {location}{r}m searching END 找到{times}個店家===============================\n")
        all_times = all_times + times
        times = 0 


    print(f"總共找到了{all_times}家的店家(排除重複)")

