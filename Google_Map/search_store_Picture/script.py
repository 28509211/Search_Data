import argparse
from function_scrapy_storedata import read_txt, scrapy_Data_google_map

def main():
    parser = argparse.ArgumentParser(description="自動從 Google Map 抓取店家圖片")
    parser.add_argument(
        "-input", type=str, default="search_store_Picture\\read.txt",
        help="想要搜尋的店家清單檔案txt"
    )
    parser.add_argument(
        "-found", type=str, default="search_store_Picture\\already_finded_store.txt",
        help="已經找過的店家清單檔案txt"
    )
    parser.add_argument(
        "-roll", type=int, default=1,
        help="要滑動幾次以載入圖片"
    )

    args = parser.parse_args()

    place = read_txt(args.input)
    already_finded_place = read_txt(args.found)

    # 還沒找過的店家
    place = place - already_finded_place
    place = list(place)

    print("正在搜尋的店家有:", len(place), "家")

    data = scrapy_Data_google_map(place)
    data.catch_picture(args.roll)

    print("________________end________________")

if __name__ == '__main__':
    main()
