import os

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# 1. Initialize the OpenAI client -- reads AZURE_FOUNDRY_RESOURCE to build the
#    Foundry OpenAI v1 endpoint and authenticates with a Microsoft Entra ID
#    token provider
resource = os.environ["AZURE_FOUNDRY_RESOURCE"]  # your Foundry resource name
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)
client = OpenAI(
    base_url=f"https://{resource}.services.ai.azure.com/openai/v1",
    api_key=token_provider
)

# 2. Use the OpenAI Chat Completions API to call a Grok deployment on Azure Foundry
response = client.chat.completions.create(
    model=os.environ["MODEL"],  # your Foundry model deployment name
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.choices[0].message.content)
