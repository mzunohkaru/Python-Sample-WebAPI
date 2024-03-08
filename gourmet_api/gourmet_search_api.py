import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('GOURMET_API_KEY')

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

params = {
    'key': API_KEY,
    'keyword': '沖縄',
    'format': 'json',
    'count': 3
}

res = requests.get(URL, params)

print(res.status_code)

data = res.json()
result = data['results']

shops = result['shop']
print(shops)

items = len(shops)
print(items)
