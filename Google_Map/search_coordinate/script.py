import argparse
from compare import Have_New_point
from map_point import open_txt, find_all_point
from map_place_point import Print_TXT

def main():
    parser = argparse.ArgumentParser(description="搜尋範圍內的點並輸出結果")
    parser.add_argument("-start_x", type=float, required=True, help="起始 x 座標")
    parser.add_argument("-start_y", type=float, required=True, help="起始 y 座標")
    parser.add_argument("-end_x", type=float, required=True, help="結束 x 座標")
    parser.add_argument("-end_y", type=float, required=True, help="結束 y 座標")
    parser.add_argument("-d", type=float, required=True, help="目標距離 d")
    parser.add_argument("-diff", type=float, required=True, help="距離容差 d_different")
    parser.add_argument("-n", type=int, required=True, help="要找到的點數")

    args = parser.parse_args()

    coordinate_set = open_txt()

    x_center = format((args.start_x + args.end_x) / 2, '.4f')
    y_center = format((args.start_y + args.end_y) / 2, '.4f')

    print(f"x_center: {x_center}, y_center: {y_center}")

    find_all_point(args.n, coordinate_set, x_center, y_center, args.start_x, args.start_y, args.end_x, args.end_y, args.d, args.diff)

    Have_New_point()
    Print_TXT("search_coordinate\\point_result\\real_new_point.txt")

if __name__ == "__main__":
    main()
