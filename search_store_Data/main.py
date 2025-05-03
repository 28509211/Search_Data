from function_scrapy_storedata import read_txt
import  function_scrapy_storedata



if __name__ == '__main__':
    place = read_txt('search_store_Data\\read.txt')  #所有店家
    can_not_find_store = read_txt('search_store_Data\\store_can_not_found.txt')  # 不能找到的店家( 有error )
    already_find_store = read_txt('search_store_Data\\already_finded_store.txt')  # 已經找過的店家
    new_place = place - ( can_not_find_store | already_find_store )  # 還未找過的店家
  

    new_place = list( new_place )

    print("正在搜尋的新店家: ", len(new_place))
    data = function_scrapy_storedata.scrapy_Data_google_map(new_place)
    data.catch_storedata()  # 抓取 店家資料 (營業時間，電話，地址，內用外帶，餐廳類型)



    print("________________end________________")