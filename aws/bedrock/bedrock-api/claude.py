from anthropic import AnthropicBedrock

# 1. Initialize the specialized Anthropic client for Amazon Bedrock
client = AnthropicBedrock(
    aws_region="us-east-1"
)

# 2. Use Anthropic's specific Messages API structure
response = client.messages.create(
    model="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.content[0].text)
