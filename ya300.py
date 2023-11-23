import requests

token = 'y0_AgAAAABwWTgMAAoX4wAAAADudldZIfeB5XuWQEu12MctHvShSg0po7U'

folder_id = 'b1gn86cknn9022me9asj'

endpoint = 'https://300.ya.ru/api/sharing-url'
response = requests.post(
    endpoint,
    json = {
      'article_url': 'https://lenta.ru/news/2023/10/06/adam/'
    },
    headers = {'Authorization': 'OAuth y0_AgAAAABwWTgMAAoX4wAAAADudldZIfeB5XuWQEu12MctHvShSg0po7U'}
)
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)