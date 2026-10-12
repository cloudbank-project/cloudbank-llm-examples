import os

from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the Azure Foundry OpenAI v1 endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call a Grok deployment on Azure Foundry
completion = client.chat.completions.create(
    model=os.environ["MODEL"],  # your Foundry model deployment name
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
