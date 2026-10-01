from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the AWS Bedrock OpenAI v1 endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call an open-weight model
#    on AWS Bedrock.
completion = client.chat.completions.create(
    model="openai.gpt-oss-120b-1:0",  # your Bedrock model ID
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
