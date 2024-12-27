import os
from dotenv import load_dotenv
# import openai
from openai import OpenAI

load_dotenv()
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "Translate the following Korean text to English: 사과"}
    ]
)

print(completion.choices[0].message)