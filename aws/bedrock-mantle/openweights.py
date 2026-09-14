from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the Amazon Bedrock Mantle endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call an open-weight model
#    (bedrock-mantle doesn't support the Converse/Invoke APIs, so open-weight
#    models are called the same way as OpenAI models)
completion = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
