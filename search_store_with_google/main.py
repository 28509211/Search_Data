from google_find_store import*
from dotenv import dotenv_values

YOUR_API_KEY = dotenv_values('search_store_with_google\\google_api_key.env')["API_KEY"]

city = "桃園"

Find_Store_With_Google( YOUR_API_KEY, city, file_name = "NW .xlsx" )
