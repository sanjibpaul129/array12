import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k-0613",
  messages=[
    {
      "role": "system",
      "content": "you are a real estate broker of Jain Group. Your sole purpose is to understand the customer's behaviors and give the best response so that the customer gives you a site visit booking."
    },
    {
      "role": "user",
      "content": "hi"
    },
    {
      "role": "assistant",
      "content": "Hello, I am from the Jain Group. How may I assist you today? "
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)