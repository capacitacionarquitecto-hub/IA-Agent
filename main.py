from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

resp = client.chat.completions.create(
    model='qwen3.5:397b-cloud',
    messages=[
        {
        "role": "system", 
        "content": "You are a helpful assistant."
        }
        ,{
        "role": "user", 
        "content": "hello, dime quien eres?"
        }

    ]
)

print(resp.choices[0].message.content)
print('My First Agent is Running!')