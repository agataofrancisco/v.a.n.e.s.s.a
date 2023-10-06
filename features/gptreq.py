import os
import openai

openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)