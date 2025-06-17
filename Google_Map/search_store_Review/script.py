import argparse
import subprocess
import time
import sys
import multiprocessing
from function_scrapy_storedata import *
import os

def read_txt(readtxt):
    place = []
    with open(readtxt, 'r', encoding='utf-8') as f:
        text = f.readlines()
    for i in text:
        temp = clean_line(i)
        if temp != '\n' and temp != '':
            place.append(temp)
    return set(place)

def howmany_store(shared_list_store_name, input_txt, found_txt):
    place = read_txt(input_txt) - read_txt(found_txt)
    shared_list_store_name = list(place)
    return shared_list_store_name

def delete_store(shared_list_store_name, found_txt):
    shared_list_store_name = set(shared_list_store_name) - read_txt(found_txt)
    return list(shared_list_store_name)

def clear_dict(shared_dict):
    shared_dict.clear()

def child_process(shared_dict, shared_list_store_name):
    place = shared_list_store_name
    data = scrapy_Data_google_map(place)
    shared_dict.update(data.catch_review({}))

def main():
    parser = argparse.ArgumentParser(description="Google 地圖評論爬蟲")
    parser.add_argument("-input", type=str, default="search_store_Review\\read.txt", help="待搜尋店家清單")
    parser.add_argument("-found", type=str, default="search_store_Review\\already_finded_store.txt", help="已經搜尋過的店家清單")
    parser.add_argument("-sleep", type=int, default=240, help="單次爬蟲的執行秒數限制（預防卡住）")
    args = parser.parse_args()

    input_txt = args.input
    found_txt = args.found
    sleep_times = args.sleep

    manager = multiprocessing.Manager()
    shared_dict = manager.dict()
    shared_list_store_name = manager.list()

    shared_list_store_name = howmany_store(shared_list_store_name, input_txt, found_txt)

    print("正在找:", len(shared_list_store_name), "間的評論(含只有給星星的)")
    
    while len(shared_list_store_name) != 0:
        store = shared_list_store_name.pop()
        print("現在要搜尋評論的店家:", store)

        child = multiprocessing.Process(target=child_process, args=(shared_dict, [store]))
        child.start()

        time.sleep(sleep_times)

        child.terminate()
        os.system('taskkill /im firefox.exe /F')

        if len(shared_dict) != 0:
            keys_list = list(shared_dict.keys())
            print("寫入評論:", keys_list[0])
            write_review_txt(keys_list[0], shared_dict[keys_list[0]])

        shared_list_store_name = delete_store(shared_list_store_name, found_txt)
        print("剩下:", len(shared_list_store_name), "間店家還未蒐集評論")

    print("---------------------------end----------------------------")

if __name__ == "__main__":
    main()
