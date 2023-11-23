import requests


token = 'y0_AgAAAABwWTgMAATuwQAAAADrPRceyEB-EDR7TxyQA44AS6zYGos1Wis'

folder_id = 'b1gn86cknn9022me9asj'


headers = {
    'Authorization': f'Bearer {token}'
}

url = 'POST https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

data = {
        'folderId': folder_id,
        'text': 'Привет малышка',
        'lang': 'ru-RU',
        # 'voice':'alena', # премиум - жрет в 10 раз больше денег
        'voice':'jane', # oksana
        'emotion':'evil',
        'speed':'1.1',
        # по умолчанию конвертит в oggopus, кот никто не понимает, зато занимат мало места
        'format': 'lpcm',
        'sampleRateHertz': 48000,
    }

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)