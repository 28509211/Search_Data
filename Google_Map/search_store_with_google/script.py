import argparse
from dotenv import dotenv_values
from google_find_store import Find_Store_With_Google

def main():
    # 命令列參數設定
    parser = argparse.ArgumentParser(description="使用 Google API 搜尋指定城市的店家資訊")
    parser.add_argument("-city", type=str, required=True, help="要搜尋的城市名稱(需要存在Excel中，例如：桃園)")
    parser.add_argument("-output", type=str, default="NW .xlsx", help="輸出的 Excel 檔名")
    parser.add_argument("-apikey_env", type=str, default="search_store_with_google\\google_api_key.env", help="儲存 API KEY 的 .env 檔路徑")
    args = parser.parse_args()

    # 讀取 API 金鑰
    try:
        YOUR_API_KEY = dotenv_values(args.apikey_env)["API_KEY"]
    except Exception as e:
        print(f"❌ 無法讀取 API 金鑰：{e}")
        return

    # 呼叫主函式
    Find_Store_With_Google(YOUR_API_KEY, args.city, file_name=args.output)

if __name__ == "__main__":
    main()
