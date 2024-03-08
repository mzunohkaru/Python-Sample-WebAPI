import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('RAKUTEN_API_KEY')

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'

params = {
    'applicationId': API_KEY,
    'keyword': 'ヘッドフォン',
    'format': 'json',
    'hits': 2,
    'minPrice': 10000,
    'maxPrice': 20000
}

res = requests.get(URL, params)

print(res.status_code)

data = res.json()
print(data)

items = data['Items']
print(items)

