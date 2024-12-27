import os
from dotenv import load_dotenv
# import openai
from openai import OpenAI

load_dotenv()
client = OpenAI()

# api_key = os.getenv("OPENAI_API_KEY")

def access_openai(prompt_value):
    # openai.api_key = api_key
    # response = openai.Completion.create(
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo-instruct",
    #     prompt=prompt_value,
    #     max_tokens=100,
    #     temperature=0.8,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     stop=["\n"]
    # )
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Translate the following Korean text to English: {prompt_value}",
        max_tokens=100,
    )
    result = response.choices[0].text.strip()
    print(result)

if __name__ == '__main__':
    input_tet = input("텍스트를 입력하세요: ")
    access_openai(input_tet)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo-instruct",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )