#方便copy放到excel檔中

def Print_TXT( filename ) :

    with open( filename, 'r', encoding='utf-8') as f:
        points = f.readlines()


    point_list = []
    for point in points:
        if point != '' and point != '\n':
            if '\n' in point :
                point = point.replace('\n', '')

            if point not in  point_list:
                point_list.append(point)
            else:
                print(point)


    print(f"新的座鏢:{ len(point_list) }")
    print(point_list)

    print()
 

    point_list_L = []
    point_list_R = []

    for i in point_list:
        p = i.split(',')
        point_list_L.append(p[0])
        print(p)
        point_list_R.append(p[1])

    print("========================x座標===============================")

    for i in point_list_L:  # x 座標
        print( i)

    print("=======================y座標===============================")

    for i in point_list_R:  # y 座標
        print( i)