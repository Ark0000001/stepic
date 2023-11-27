import openai

openai.api_key = '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'
# organization='org-PKAZMf23yXZvOloR9Mepr2wt',
client = openai.OpenAI(
  api_key=openai.api_key,
)

response = client.images.generate(
  model="dall-e-3",
  prompt="нарисуй как в описании: изображен человек за рулем небольшого, необычного, винтажного "
         "микроавтобуса с характерным красным кузовом и прозрачным куполом. Транспортное средство "
         "представляет собой трехколесный автомобиль с одним колесом, видимым спереди, "
         "и обтекаемой, округлой формой кузова. Регистрационный знак и конкретные детали модели "
         "не относятся к описанию. Водитель одет в очки и что-то похожее на клетчатую рубашку и "
         "активно управляет автомобилем. Ощущение движения передается через задний план и дорогу, "
         "которые размыты из-за технологии панорамирования камеры, в то время как автомобиль и "
         "водитель остаются в фокусе. Обстановка выглядит как солнечный день с ясным небом, "
         "который подходит для приятной поездки в таком открытом и просторном автомобиле. На "
         "фотографии запечатлен момент досуга и удовольствия от вождения классического, "
         "самобытного экземпляра автомобильной истории.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# completion = client.chat.completions.create(
#   model="gpt-4-1106-preview",
#   messages=[
#     {"role": "system", "content": "Вы философ-шутник. Ваш ответ должен быть в формате JSON."},
#     {"role": "user", "content": "Что будем делать вечером?"}
#   ],
#   response_format={"type": "json_object"}
# )
#
# print(completion.choices[0].message.content)
# system_prompt = "You are an expert analyzing images."
# response = client.chat.completions.create(
#     model="gpt-4-vision-preview",
#     messages=[
#         {
#             "role": "system",
#             "content": [
#                 {"type": "text", "text": system_prompt},
#             ],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url":"https://thecode.media/wp-content/uploads/2023/06/1-4.jpg",
#                     }
#                 },
#             ],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "Что изображено на изображении?"},
#             ],
#         }
#     ],
#     max_tokens=1000,
# )
#
# print(response.choices[0].message.content)