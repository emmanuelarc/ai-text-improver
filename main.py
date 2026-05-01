from openai import OpenAI

client = OpenAI()

print("Write something:")
user_input = input()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)