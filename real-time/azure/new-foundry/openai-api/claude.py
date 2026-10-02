from anthropic import AnthropicFoundry

# 1. Initialize the Anthropic client for Azure Foundry -- reads
#    ANTHROPIC_FOUNDRY_API_KEY and ANTHROPIC_FOUNDRY_RESOURCE
client = AnthropicFoundry()

# 2. Use Anthropic's specific Messages API structure
response = client.messages.create(
    model="claude-haiku-4-5",  # your Foundry model deployment name
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.content[0].text)
