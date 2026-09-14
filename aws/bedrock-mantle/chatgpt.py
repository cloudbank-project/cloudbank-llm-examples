from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the Amazon Bedrock Mantle endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call an OpenAI model hosted on Bedrock
completion = client.chat.completions.create(
    model="openai.gpt-5.6-luna",
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
