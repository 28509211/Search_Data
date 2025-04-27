# 產生這次新加的座標
# 並會把它寫入到point.txt中紀錄
def Have_New_point() :
    with open('search_coordinate\\point_result\\point.txt', encoding='utf-8') as f:
        point = set(line.strip() for line in f)

    with open('search_coordinate\\point_result\\new_point.txt', encoding='utf-8') as d:
        newpoint = set(line.strip() for line in d)

    # 找出兩者共同的
    same = point & newpoint

    # 找出 newpoint 裡有、但 point 裡沒有的
    different = newpoint - point

    # 把不同的寫進檔案
    with open('search_coordinate\\point_result\\real_new_point.txt', 'w', encoding='utf-8') as g:
        for line in different:
            g.write(line + '\n')

    with open('search_coordinate\\point_result\\point.txt', 'a', encoding='utf-8') as g:
        for line in different:
            g.write(line + '\n')

    print(f"之前找過的座標點有:{len(same)}")
