import argparse
from function_scrapy_storedata import read_txt, scrapy_Data_google_map

def main():
    parser = argparse.ArgumentParser(description="抓取 Google 地圖店家資料")
    parser.add_argument("-input", type=str, default="search_store_Data\\read.txt", help="店家列表檔案txt")
    parser.add_argument("-cant", type=str, default="search_store_Data\\store_can_not_found.txt", help="不能找到的店家txt")
    parser.add_argument("-found", type=str, default="search_store_Data\\already_finded_store.txt", help="已經找過的店家txt")
    args = parser.parse_args()

    place = read_txt(args.input)
    can_not_find_store = read_txt(args.cant)
    already_find_store = read_txt(args.found)

    new_place = place - (can_not_find_store | already_find_store)
    new_place = list(new_place)

    print("正在搜尋的新店家數量:", len(new_place))

    data = scrapy_Data_google_map(new_place)
    data.catch_storedata()

    print("________________end________________")

if __name__ == '__main__':
    main()
