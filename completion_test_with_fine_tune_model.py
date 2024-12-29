from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:personal::Ajo5kvNY",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant. Response in Korean."},
        {
            "role": "user",
            "content": "Describe the type of cat."
        }
    ]
)

print(completion.choices[0].message)