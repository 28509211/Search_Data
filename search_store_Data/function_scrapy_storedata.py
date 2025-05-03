
from selenium import webdriver
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


def clean_line(text):
    if('\n' in text):
        text = text.replace('\n', '')
    return text

def write_txt(key, values, times):

    with open('../store_Review/review_ready.txt', 'a', encoding='utf-8') as f:  # 暫時保存
        print(f'已蒐集 {times} 筆評論')
        f.write(f'{key}: {values}\n')

def write_txt_all(text_dic):
    with open('../review.txt', 'w', encoding='utf-8') as f :  #最後保存全部
        print(f'已蒐集 {len(text_dic)} 筆評論')
        for key, values in text_dic.items():
            f.write(f'{key}: {values}\n')

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
    number = number.replace(',', '')
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

    def __search(self, place):
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(place)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
        time.sleep(3)

    def __review(self):
        self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]').click()# 評論
        time.sleep(3)


    def __storedata(self, notfound):
        try:
            # 在這裡執行可能引發NoSuchElementException的代碼
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[1]/div[2]/div[2]').click()
            notfound = False
        except NoSuchElementException as e:
            # 在這裡處理NoSuchElementException錯誤
            notfound = True
        time.sleep(3)
        return notfound
    def __open(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--disable-images")
        # option.add_argument('--blink-settings=imagesEnabled=false')
        option.add_argument('--headless')
        self.driver= webdriver.Chrome(options=option)
        self.driver.get(self.url)
        time.sleep(5)
        # print(place)

    def __get_review_amount(self):
        text = self.target_window.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[3]')
        text = text.text
        print(text)
        text = text.split(' ')
        self.howmany = int(clean_dot_for_number(text[0]))

    def get_restaurant_type(self):

        try:
            restaurant_type = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/span/button')
            return restaurant_type.text
        except NoSuchElementException as e:
            restaurant_type = 'None'
        # print(open_time.text)
            return restaurant_type

    def get_address(self):

        try:
            address = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div//div[3]/button/div/div[2]')
        except NoSuchElementException as e:
            address = 'None'
        # print(open_time.text)
        return address.text

    def __check_have_review(self):
        try:
            self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]').click()# 評論
            no_review = False
        except NoSuchElementException as e:
            no_review = True

        return no_review

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


    def __scroll(self, runs_times):


        k = 0

        for i in range(runs_times):
            # for g in range(10):
            #     self.target_window.send_keys(Keys.PAGE_DOWN)
            #     time.sleep(randint(10,80))
            self.target_window.send_keys(Keys.END)
            k = k + 10
            print(k)    #1089
            # time.sleep(3)
            time.sleep(3)

            if( k % 300 == 0):
                cookies = self.driver.get_cookies()
                print(f"main: cookies = {cookies}")
                if (len(cookies) == 0):
                    break
                self.driver.delete_all_cookies()


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
        
        print( "執行完，已找到: ", successful_times, " 家" )
        print( "執行完，沒找到: ", undsuccessful_times, " 家" )
        print( "-------------------------------------------------------------------------")

    def catch_picture(self, roll_times):

        picture_ok = ''
        store_picture = {}
        self.__open()
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
                self.__scroll(int(roll_times))

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


    def catch_review(self):
        store = {}
        self.__open()
        times = 0
        for number, place in enumerate(self.place):
            print(f"{place}   loading......................................")
            time.sleep(10)
            self.__search(place)
            time.sleep(10)
            self.__review()
            time.sleep(10)
            self.target_window = self.driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

            time.sleep(5)
            self.__get_review_amount()
            time.sleep(1)
            # runs_times = int(self.howmany / 5) + 1
            runs_times = 270
            self.__scroll(runs_times)
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

            print("user: ", len(user_content))
            #
            #
            # # print(review)
            # # text_content = []
            # for user_name, i in enumerate(review):
            #     text = i.get_text(strip=True)
            #     text = clean_line(text)
            #     text_content[user_content[user_name]] = text
            #     times = times + 1
            #
            # print("review: ", len(text_content))
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
                times = times + 1



            store[place] = text_content
            write_txt(place, text_content, times)

            print(f'{place} finished, {self.len_place - (number+1)} more locations')
            times = 0

        return store
