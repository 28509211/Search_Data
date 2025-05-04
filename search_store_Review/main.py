
import subprocess
import time
import sys
import multiprocessing
from function_scrapy_storedata import *
import time
import os
import signal
import pickle
import re
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

def read_txt(readtxt):
    place  = []
    with open(readtxt, 'r', encoding='utf-8') as f:  # 暫時保存
            text = f.readlines()

    for i in text :
        temp  = clean_line(i)
        if temp != '\n' and temp != '':
            place.append(temp)
            
    return  set(place)


def howmany_sotre(shared_list_store_name):  # 還未讀取評論的店家

    place = read_txt("search_store_Review\\read.txt") - read_txt("search_store_Review\\already_finded_store.txt") 
   
    shared_list_store_name = list(place)


    return shared_list_store_name



def delete_sotre( shared_list_store_name ):  # 刪除之前已讀過的店家

    shared_list_store_name = set( shared_list_store_name ) - read_txt("search_store_Review\\already_finded_store.txt") 

    shared_list_store_name = list(shared_list_store_name)

    return shared_list_store_name

def clear_dict(shared_dict):
    shared_dict = {}
    return shared_dict


def child_process(shared_dict, shared_list_store_name):


    place = shared_list_store_name
    data = scrapy_Data_google_map(place)
    shared_dict = data.catch_review(shared_dict)
    shared_list_store_name = delete_sotre(shared_list_store_name)
 


# 為了防止google反爬蟲(當評論一直往下滑太多時會一直轉圈圈) 所以設計使用time的方式
# 當遇到轉圈圈時，時間依樣會繼續跑直到跑完後，直接砍掉process，把之前的緩存shared_dict評論，寫入review_ready
# 然後使用delete_sotre把該家刪除
# 下一次再重新開一個process從下一家開始繼續收集評論

if __name__ == "__main__":

    sleep_times = 242

    manager = multiprocessing.Manager()
    shared_dict = manager.dict()

    shared_list_store_name = manager.list()

    shared_list_store_name = howmany_sotre(shared_list_store_name)

    print("正在找:", len(shared_list_store_name), "間的評論(含只有給星星評論的數量)")


    print('hellllllllllllllllllo')


    while len(shared_list_store_name) != 0:

        store = shared_list_store_name.pop() 

        print("現在要搜尋評論的店家: ", store)

        child = multiprocessing.Process(target=child_process, args=(shared_dict,[store]))
        child.start()

        child_pid = child.pid


        time.sleep( sleep_times )  

       
        child.terminate()
        os.system('taskkill /im firefox.exe /F')
    

        if len(shared_dict) != 0:
            # test4.write_txt_all(shared_dict)
            keys_list = list(shared_dict.keys())
            # print(keys_list[0])

            print("WRITEEEEEEEEE2")
            write_review_txt(keys_list[0], shared_dict[keys_list[0]])
            # shared_list_store_name = delete_sotre(shared_list_store_name)

        shared_list_store_name = delete_sotre(shared_list_store_name)
        print("剩下: ", len(shared_list_store_name),  "間店家還未蒐集評論")


    print("---------------------------end----------------------------")






