import os

from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# 1. Initialize the Azure OpenAI client -- reads AZURE_FOUNDRY_RESOURCE to
#    build the Azure OpenAI resource endpoint
resource = os.environ["AZURE_FOUNDRY_RESOURCE"]  # your Foundry resource name
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)
client = AzureOpenAI(
    azure_endpoint=f"https://{resource}.openai.azure.com/",
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21"
)

# 2. Send the "Hello World" message to your deployed GPT model
response = client.chat.completions.create(
    model="gpt-5.6-luna",  # your Azure OpenAI deployment name
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(response.choices[0].message.content)
