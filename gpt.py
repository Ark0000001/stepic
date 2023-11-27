import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()
tok=os.getenv('token_YA')
fold=os.getenv('folder_id_YA')
def gpt1(question, answer):
    token = tok

    folder_id = fold

    headers = {
        'Authorization': f'Bearer {token}', 'x-folder-id': folder_id
    }

    url = 'https://llm.api.cloud.yandex.net/llm/v1alpha/instruct'

    data = {
        "model": "general",
        "instruction_text": "ты - предсказатель судеб",
        "request_text": f"Ответь на вопрос ({question}) и укажи ответ ({answer}), как провидец и дополни своим мнением. В конце вставь афоризм в контексте твоего ответа",
        "generation_options": {
            "max_tokens": 1500,
            "temperature": 0.6
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_dict = response.json()

        return response_dict["result"]["alternatives"][0]["text"]


    else:
        print("Error:", response.status_code)
