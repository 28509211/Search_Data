from geopy.distance import geodesic
import random
from tqdm import trange
import time
import math

# 計算兩個點經緯度上的距離
# x1 : 第一個緯度, y1 : 第一個經度 , x2 : 第二個緯度, y2 : 第二個經度
def distances(x1, y1, x2, y2):
    dist = geodesic((x1, y1), (x2, y2)).m
    return dist


# 隨機生成經緯度x1~x2 y1~y2  x1:緯度  x2:緯度    y1:經度     y2:經度   保留小數後4位
def generate_random_coordinates( start_x, start_y, end_x, end_y ):

    #例子
    # latitude = round(random.uniform(23.5667, 24.3333 ), 4)  #南投
    # longitude = round(random.uniform( 120.6167, 121.5), 4)

    latitude = round(random.uniform(start_x, end_x), 4)  
    longitude = round(random.uniform(start_y, end_y), 4)


    return latitude, longitude


# 得到一個經緯度與(x1,y1) 距離為d 誤差d_different
# x1 : 第一個緯度, y1 : 第一個經度
def getpoint(x_center, y_center, start_x, start_y, end_x, end_y, d=400, d_different = 50):
    x2, y2 = generate_random_coordinates( start_x, start_y, end_x, end_y )


    dis = distances(x_center, y_center, x2, y2)
    while  abs(dis - d) > d_different:
        # print( x2, y2 )
        x2, y2 = generate_random_coordinates( start_x, start_y, end_x, end_y )
        dis = distances(x_center, y_center, x2, y2)


    # time.sleep(10)
    # print("+++++++++++++++++++++++++++++++++++++++++++++")
    # print( x2, y2 )
    # time.sleep(10)
    return x2, y2

# 從一堆座標中找到與我距離最近的 緯度 和 經度
# coordinate_set 一堆座標
def find_small_distance(coordinate_set, x, y):
    small_two_set = set()
    smallest = 0
    small = 0
    smallest_set = None
    small_set = None
    big = -1
    big_set = None
    for number, point in enumerate(coordinate_set):
        if number == 0 :
            smallest = distances(point[0], point[1], x, y)
            smallest_set = point
        elif distances(point[0], point[1], x, y) <= smallest:
            small = smallest
            small_set = smallest_set
            smallest = distances(point[0], point[1], x, y)
            smallest_set = point
        elif distances(point[0], point[1], x, y) > smallest:
            if big == -1:
                big = distances(point[0], point[1], x, y)
                big_set = point
            else:
                if distances(point[0], point[1], x, y) <= big :
                    big = distances(point[0], point[1], x, y)
                    big_set = point


    small_two_set.add(smallest_set)
    if small_set == None:
        small_two_set.add(big_set)
    else:
        small_two_set.add(small_set)

    return small_two_set



#這兩個最近的點，離 (x, y) 的距離有沒有大概是 d 公尺？可以誤差 d_different 公尺。
def check_distance(small_two_set, x, y, d = 400, d_different=50 ):
    for point in small_two_set:
        dis = distances(point[0],point[1] , x, y)
        if abs(dis - d) > d_different:
            return False

    return True


#打開 之前new_point檔案 放到set()中
def open_txt():
    coordinate_set =set()
    with open('search_coordinate\\point_result\\new_point.txt', 'r', encoding='utf-8') as f:
        points = f.readlines()

    point_list = []
    for point in points:
        if point != '' and '\n':
            if '\n' in point:
                point = point.replace('\n', '')

            if point not in point_list:
                point_list.append(point)
            else:
                print(point)

    for i in point_list:
        p = i.split(',')
        coordinate_set.add((p[0], p[1]))

    return coordinate_set

#找另一個點 符合getpoint
def find_other_point(x_center, y_center, start_x, start_y, end_x, end_y, d=400, d_different = 50):

    x, y = getpoint(x_center, y_center, start_x, start_y, end_x, end_y, d, d_different)
    print( f"找到的座標:{x}, {y}" )
    return x, y


# 隨機生成點 與中心點符合距離 d , 誤差d_different
# 然後把這些合法的點寫進 new_point.txt
# 如果 重複找howmany//2次都發現在coordinate_set存在的話就會忽略，結束
# howmany:找幾個點符合以上條件
def find_all_point(howmany, coordinate_set, x_center, y_center, start_x, start_y, end_x, end_y, d=400, d_different = 50):
    with open('search_coordinate\\point_result\\new_point.txt', 'w', encoding='utf-8') as f:
        
        temp = (x_center, y_center)
        
        if temp not in coordinate_set :
            coordinate_set.add(temp)
            f.write(f"{x_center},{y_center}\n")

        print(f"你的new_point.txt原本有:{len(coordinate_set)}個座標")

        print("RUNNING>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        for n in range(howmany):
            ok = False
            times = 0

            while not ok and times < howmany//2:
                x, y = find_other_point(x_center, y_center, start_x, start_y, end_x, end_y, d, d_different)
                temp = (x, y)

                if temp in coordinate_set:
                    print("重複點！跳過：", temp)
                    times += 1
                    continue
                else:
                    coordinate_set.add(temp)
                    f.write(f"{x},{y}\n")
                    ok = True

            if not ok:
                print(f"第 {n+1} 個點找不到新點，已嘗試 {howmany//2} 次。 已結束")
            else:
                print(f"還剩下{ howmany - ( n + 1 ) }...........................")

    print( "已結束<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")




