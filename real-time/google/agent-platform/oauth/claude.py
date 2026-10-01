import os

from anthropic import AnthropicVertex

# 1. Initialize the specialized Anthropic client for Vertex AI --
#    reads GOOGLE_CLOUD_PROJECT for the Google Cloud project ID
client = AnthropicVertex(
    project_id=os.environ["GOOGLE_CLOUD_PROJECT"],  # your Google Cloud project ID
    region="us-east5"
)

# 2. Use Anthropic's specific Messages API structure
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.content[0].text)
