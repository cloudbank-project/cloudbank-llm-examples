from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the Azure Foundry OpenAI v1 endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call a GPT deployment on Azure Foundry
completion = client.chat.completions.create(
    model="gpt-5.6-luna",  # your Foundry model deployment name
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
