import requests
import json


def gpt1(question, answer):
    token = 't1.9euelZqRx8idy8KlYmUlo6Xz5jNm42PmMvl8_cKHFtW-e8tHnVl_t3z90pKWFb57y0edWX-zef1656VmseTjMnMyMnJxp7Lz8nLnY-c7_zF656VmseTjMnMyMnJxp7Lz8nLnY-c.Ra0f5IzDTmFgx0yKM7JAs4OcfGL5bx4xzKgvEqFqL9BCw7XZxW_ZlMUUYvnIu1TBrPGoxEdpzotAZLkxsE_YAw'

    folder_id = 'b1gn86cme9asj'

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
