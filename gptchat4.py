from openai import OpenAI

client = OpenAI(
  organization='YOUR_ORG_ID',
)
print(client.models.list())