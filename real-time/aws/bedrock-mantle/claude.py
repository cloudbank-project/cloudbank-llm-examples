from anthropic import AnthropicBedrockMantle

# 1. Initialize the specialized Anthropic client for the AWS Bedrock Mantle endpoint
client = AnthropicBedrockMantle(
    aws_region="us-east-1"
)

# 2. Use Anthropic's specific Messages API structure
response = client.messages.create(
    model="anthropic.claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.content[0].text)
