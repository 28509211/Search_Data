import sys

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import psutil
import os
from lxml import etree
from random import randint
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import logging
import sys

def clean_line(text):
    if('\n' in text):
        text = text.replace('\n', '')
    return text


def write_review_txt(key, values):

        file_path = "search_store_Review\\review\\review_ready.txt"
        max_size = 2 * 1024 * 1024
        try:
            # 檢查文件大小是否超過閥值
            if os.path.exists(file_path) and os.path.getsize(file_path) <= max_size:
                print("文件未超過閥值，繼續使用")
            else:
                file_name, file_extension = os.path.splitext(file_path)
                count = 1
                while True:
                    new_file_path = f"{file_name}_{count}{file_extension}"
                    if os.path.exists(new_file_path) and os.path.getsize(new_file_path) < max_size :
                        file_path = new_file_path
                        break
                    elif not os.path.exists(new_file_path):
                        file_path = new_file_path
                        break
                    count += 1

            with open(file_path, 'a', encoding='utf-8') as f:
                total = sum(len(v) for v in values.values())
                print(f'已蒐集 {total} 筆評論')
                f.write(f'{key}: {values}\n')
            print("已寫入文件")
        except Exception as e:
            print("寫入時發生錯誤:", e)


        with open('search_store_Review\\already_finded_store.txt', 'a', encoding='utf-8') as w:  # 最後保存全部
            w.write(f'{key}\n')


def write_txt_store_notfound(text):
    with open('search_store_Data\\store_can_not_found.txt', 'a+', encoding='utf-8') as f :  #最後保存全部
        for place in text :
            f.write(f'{place}\n')

def write_storedata(store):
    with open('search_store_Data\\storedata.txt', 'a', encoding='utf-8') as f:  # 最後保存全部
        print(f'已找到 {len(store)} 間店家')
        for key, values in store.items():
            f.write(f'{key}: {values}\n')
    with open('search_store_Data\\already_finded_store.txt', 'a', encoding='utf-8') as f:
        for key, values in store.items():
            f.write(f'{key}\n')

def write_picture_adddress(place, pictures):
    with open('search_store_Picture\\store_pictures_found.txt', 'a', encoding='utf-8') as f :  #最後保存全部
        print(f'{place} {len(pictures)} 張')
        f.write(f'{place}: {pictures}\n')
    with open('search_store_Picture\\already_finded_store.txt', 'a', encoding='utf-8') as w:  # 最後保存全部
        w.write(f'{place}\n')

def clean_dot_for_number(number):
    print( "評論數:" , number )
    number = number.replace(',', '')
    if number == '' :
        return 0 
    return int(number)

def read_txt(readtxt):
    place  = []
    with open(readtxt, 'r', encoding='utf-8') as f:  # 暫時保存
            text = f.readlines()

    for i in text :
        temp  = clean_line(i)
        if temp != '\n' and temp != '':
            place.append(temp)
            
    return  set(place)


class scrapy_Data_google_map:
    def __init__(self, place):
        self.howmany = 0
        self.place = place
        self.url = "https://www.google.com.tw/maps/"
        self.target_window = None
        self.driver = None
        self.len_place = len(place)
        self.wrong = False

    def __open(self):   # 爬蟲的設定 並打開google map
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-images")
        # firefox_options.add_argument("--headless")
        # option = webdriver.ChromeOptions()
        # option.add_argument("--disable-images")
        # # option.add_argument('--blink-settings=imagesEnabled=false')
        # option.add_argument('--headless')
        # self.driver= webdriver.Chrome(options=option)
        try:
            self.driver =  webdriver.Firefox(options=firefox_options)
            self.driver.get(self.url)
            time.sleep(5)
        except WebDriverException as e:
            print(f"WebDriverException: {e}")

        # print(place)

    def __search(self, place):  # 把地點輸入到google map search上
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(place)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
        time.sleep(3)

    def __storedata(self, notfound):  #  點擊到商家資訊的頁面
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[1]/div[2]/div[2]').click()
            notfound = False
        except NoSuchElementException as e:
            notfound = True
        time.sleep(3)
        return notfound


    def __review(self, place): #  點擊到商家評論的頁面
        try :
            element = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]')
            text = element.text.strip()
            print(f"[DEBUG1] Text content: {text}")
            if text == "評論":
                element.click()
                time.sleep(3)
            else:
                element = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[3]/div[2]/div[2]')
                text = element.text.strip()
                print(f"[DEBUG2] Text content: {text}")
                if text == "評論":
                    element.click()
                    time.sleep(3)
                else:
                    print("不是評論，不點擊")

        except Exception as e:
            print("找不到評論", e)
            self.wrong = True



    def __get_review_amount(self):  #獲取有多少評論數(含只有星星)

        try:
            text = self.target_window.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[3]')
            text = text.text
            text = text.split(' ')
            self.howmany = int(clean_dot_for_number(text[0]))
            return True
        except NoSuchElementException as e:
            return False


    def get_address(self):  

        try:
            address = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div//div[3]/button/div/div[2]')
        except NoSuchElementException as e:
            address = 'None'
        # print(open_time.text)
        return address.text

    def get_phonenumber(self):
        try:
            phone_number = self.driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div//button[@class = 'CsEnBe'][@data-tooltip='複製電話號碼']").text
        except NoSuchElementException as e:
            phone_number = 'None'

        return phone_number

    def get_introduction(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[3]/div[2]/div[2]').click()
            time.sleep(3)
            introduction = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]//h2[@class="iL3Qke fontTitleSmall" and contains(text(), "服務項目")]/following-sibling::ul').text
        except NoSuchElementException as e :
            introduction = 'None'

        return introduction

    def get_store_time(self):
        open_time = ''
        try:
            page = self.driver.page_source
            # self.driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[4]/div[1]").click()
            # time.sleep(2)
            soup = BeautifulSoup(page, 'html.parser')
            # print(soup)
            review = soup.select("div div div div td.HuudEc button[data-value]")            # print(review)

            for i in review:
                # print(i['data-value'])
                open_time = open_time + (i['data-value']) + '/'

        except NoSuchElementException as e :
            open_time = 'None'

        return open_time

    def get_picture(self):
        try:
            time.sleep(3)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]//button[@aria-label='全部']").click()
            time.sleep(5)
            picture = 'ok'
        except NoSuchElementException as e :
            picture = 'None'

        return picture

    def __scroll_Picture(self, runs_times):


        k = 0

        for i in range(runs_times):
            # for g in range(10):
            #     self.target_window.send_keys(Keys.PAGE_DOWN)
            #     time.sleep(randint(10,80))
            self.target_window.send_keys(Keys.END)
            k = k + 10
            print(k)    #1089
            time.sleep(3)

            if( k % 300 == 0):
                cookies = self.driver.get_cookies()
                print(f"main: cookies = {cookies}")
                if (len(cookies) == 0):
                    break
                self.driver.delete_all_cookies()

    def __scroll_Review(self, runs_times, place, shared_dict, save_round=100):

        k = 0

        for i in range(runs_times):
            try:
     
                self.target_window.send_keys(Keys.END)
                k = k + 10
                print(k)  # 1089
                time.sleep(3)
                print("===========================================")
                cookies = self.driver.get_cookies()
                if (k % save_round == 0):
                    # store_temp.clear()
                    shared_dict.clear()
                    self.some_function(place, shared_dict)   # 把之前有獨到的評論放進緩存shared_dict
                    # print("child:", store_temp)
                    # print(shared_dict)
                    print("緩存區的評論人數(不含只有給星星): ", len(shared_dict[place]))
                    # sudict = store_temp
                    cookies = self.driver.get_cookies()   # 當cookie = [] 表示沒有新的評論
                    print(f"main: cookies = {cookies}")
                    if (len(cookies) == 0):
                        break
                    self.driver.delete_all_cookies()
                else:
                    pass
            except Exception as e:
                print("111111111111111111111111111111111111111111111")
                print(f"Exception caught: {str(e)}")

        shared_dict.clear()



    def catch_storedata(self):  # 抓取店家的基本資料
        text = []
        text_notfound = []
        store_data = {}
        self.__open()
        successful_times = 0
        undsuccessful_times = 0
        for number, place in enumerate(self.place):
            notfound = False
            self.__search(place)
            notfound = self.__storedata(notfound)
            if(notfound):
                print(f'{place} is not found')
                sen = place
                text_notfound.append(sen)
                undsuccessful_times = undsuccessful_times + 1
            else:
                print(f'{place} is found')
                restaurant_type = self.get_restaurant_type()
                open_time = self.get_store_time()
                # print(open_time)
                address = self.get_address()
                # print(address)
                phone_number = self.get_phonenumber()
                # print(phone_number)
                introduction = self.get_introduction()

                # print(introduction)

                open_time = clean_line(open_time)
                text.append(open_time)
                address = clean_line(address)
                text.append(address)
                phone_number = clean_line(phone_number)
                text.append(phone_number)
                introduction = clean_line(introduction)
                text.append(introduction)
                introduction = clean_line(restaurant_type)
                text.append(restaurant_type)

                successful_times = successful_times + 1



            if not notfound :
                store_data[place] = text
                # print(text)
                write_storedata(store_data)
                text = []
                store_data = {}
            else:
                write_txt_store_notfound(text_notfound)
                text_notfound = []
        
        print( "執行完catch_storedata，已找到: ", successful_times, " 家" )
        print( "執行完catch_storedata，沒找到: ", undsuccessful_times, " 家" )
        print( "-------------------------------------------------------------------------")



    def catch_picture(self, roll_times):  # 找店家圖片

        picture_ok = ''
        store_picture = {}
        self.__open()
        successful_times = 0 
        undsuccessful_times =  0


        for number, place in enumerate(self.place):
            print(f"{place}   loading......................................")
            picture_ok = ''
            self.__search(place)
            picture_ok = self.get_picture()


            pictures = []

            if picture_ok != 'None':
                self.target_window = self.driver.find_element(By.XPATH,
                                                              '//*[@id="QA0Szd"]//div[contains(@class, "m6QErb DxyBCb kA9KIf dS8AEf XiKgde")]')

                time.sleep(5)
                self.__scroll_Picture(int(roll_times))

                time.sleep(3)

                page = self.driver.page_source
                soup = BeautifulSoup(page, 'html.parser')
                review = soup.select('div.Uf0tqf.loaded')
                # print(review)


                for i in review:
                    picture = i['style']
                    url_start = picture.find('"') + 1
                    url_end = picture.find('"', url_start)
                    image_url = picture[url_start:url_end]

                    pictures.append(image_url)

            store_picture[place] = pictures
            write_picture_adddress(place, pictures)

        print( "執行完catch_picture" )
        print( "-------------------------------------------------------------------------")


    # def get_driver(self):
    #     D = self.driver
    #     return D

    def catch_review(self, shared_dict):  # 抓取商家評論, shared_dict是緩存區(存評論和留言者)



        store = {}
        self.__open()
       
        for number, place in enumerate(self.place):



            self.wrong = False
            print(f"{place}   loading......................................")
            time.sleep(10)
            self.__search(place)
            time.sleep(10)
            self.__review( place )
            if ( self.wrong ) :
                continue

            time.sleep(10)
            self.target_window = self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

            time.sleep(5)
            print("-----------------------------------------------------------------")
            rev_ok = self.__get_review_amount()
            if rev_ok:
                print("-----------------------------------------------------------------")
                time.sleep(1)
                runs_times = int(self.howmany / 5) + 1
                    # runs_times = 270
                self.__scroll_Review(runs_times, place, shared_dict)
                time.sleep(3)
                page =  self.driver.page_source
                soup = BeautifulSoup(page, 'html.parser')
                    # print(soup)
                review = soup.select('div.m6QErb div.MyEned span.wiI7pd')
                user = soup.select('div.m6QErb div.jJc9Ad  div.d4r55')
                    # user = soup.select('div.aria-label')
                    # print(user)

                text_content = {}

                user_content = []
                for i in user:
                    text = i.get_text(strip=True)
                    text = clean_line(text)
                    user_content.append(text)
                        # print(text)

                print("留言的人數(含只給星星): ", len(set(user_content)))

                number_user = 0
                review_list = []
                for user_name, i in enumerate(review):
                    out = False
                    review_list = []
                    while number_user < len(user_content):
                        text = i.get_text(strip=True)
                        text = clean_line(text)
                        review_list.append(text)
                        if user_content[user_name] not in text_content:
                            text_content[user_content[user_name]] = review_list
                        else:
                            text_content[user_content[user_name]].append(text)
                                # print(text_content[user_content[user_name]])
                            text_content[user_content[user_name]] = text_content[user_content[user_name]]
                        number_user = number_user + 1
                        out = True
                        if(out):
                            break
                

                print("留言的人數(不含只給星星): ", len(text_content))

                store[place] = text_content
                print("WRITEEEEEEEEE1")
                write_review_txt(place, text_content)
                print(shared_dict)


                print(f'{place} finished, {self.len_place - (number+1)} more locations')
            else:
                store[place] = {'None':['None']}
                text_content = {'None':['None']}
                print("WRITEEEEEEEEE1")
                write_review_txt(place, text_content)

        return shared_dict


    def some_function(self, place, shared_dict):  # 把評論放到緩存區shared_dict
        # global store_temp

        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup)
        review = soup.select('div.m6QErb div.MyEned span.wiI7pd')
        user = soup.select('div.m6QErb div.jJc9Ad  div.d4r55')
        # user = soup.select('div.aria-label')
        # print(user)

        text_content = {}

        user_content = []
        for i in user:
            text = i.get_text(strip=True)
            text = clean_line(text)
            user_content.append(text)
            # print(text)

        print("緩存區留言的人數(含只給星星): ", len(set(user_content)))
        number_user = 0
        review_list = []

        for user_name, i in enumerate(review):
            out = False
            review_list = []
            while number_user < len(user_content):
                text = i.get_text(strip=True)
                text = clean_line(text)
                review_list.append(text)
                if user_content[user_name] not in text_content:
                    text_content[user_content[user_name]] = review_list
                else:
                    text_content[user_content[user_name]].append(text)
                    # print(text_content[user_content[user_name]])
                    text_content[user_content[user_name]] = text_content[user_content[user_name]]
                number_user = number_user + 1
                out = True
                if (out):
                    break


        shared_dict[place] = text_content



    