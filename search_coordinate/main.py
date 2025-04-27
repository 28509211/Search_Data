from compare import Have_New_point
from map_point import*
from map_place_point import Print_TXT

coordinate_set = set()
coordinate_set = open_txt()  # 打開


start_x=23.5667
start_y=120.6167
end_x= 25.3333
end_y = 122.5

x_center = format((start_x + end_x) / 2, '.4f')

y_center = format( ( start_y + end_y ) / 2,  '.4f' )

print( f"x_center: {x_center}, y_center: {y_center}" )

d = 400
d_different = 50 

n = 5

# 嘗試找到n個點 符合 距離d, 和誤差 d_different
find_all_point(n, coordinate_set, x_center, y_center, start_x, start_y, end_x, end_y, d, d_different )

# 把新的座標產生到real_new_point.open_txt
# 也會記錄到point.txt中
Have_New_point()

#印出指定檔案txt的座別 分別印出x座標 和 y座標 方便copy到 excel中
Print_TXT("search_coordinate\\point_result\\real_new_point.txt")


