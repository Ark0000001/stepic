import requests

import os

from dotenv import load_dotenv
load_dotenv()
tok=os.getenv('token_YA2')
fold=os.getenv('folder_id_YA')

token = tok

folder_id = fold

endpoint = 'https://300.ya.ru/api/sharing-url'
response = requests.post(
    endpoint,
    json = {
      'article_url': 'https://lenta.ru/news/2023/10/06/adam/'
    },
    headers = {'Authorization': f'OAuth {token}'}
)
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)