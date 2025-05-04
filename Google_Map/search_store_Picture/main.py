from function_scrapy_storedata import read_txt
import  function_scrapy_storedata

if __name__ == '__main__':
    place = read_txt('search_store_Picture\\read.txt')  # 想要找的店家
    already_finded_place = read_txt('search_store_Picture\\already_finded_store.txt') # 已經找過店家

    place = place - already_finded_place   # 還未找過的店家

    place = list( place )

    print("正在搜尋的店家有: ", len(place), "家")
    data = function_scrapy_storedata.scrapy_Data_google_map(place)

    roll_times = 1 # 設置要下滑幾次


    data.catch_picture( roll_times )

    print("________________end________________")