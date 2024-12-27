from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant. Response in Korean."},
        {
            "role": "user",
            "content": "Describe the type of cat."
        }
    ]
)

print(completion.choices[0].message)