import os

from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# 1. Initialize the specialized Anthropic client for Azure Foundry --
#    reads AZURE_FOUNDRY_RESOURCE for the Foundry resource name
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)
client = AnthropicFoundry(
    resource=os.environ["AZURE_FOUNDRY_RESOURCE"],  # your Foundry resource name
    azure_ad_token_provider=token_provider
)

# 2. Use Anthropic's specific Messages API structure
response = client.messages.create(
    model="claude-haiku-4-5",  # your Foundry model deployment name
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.content[0].text)
