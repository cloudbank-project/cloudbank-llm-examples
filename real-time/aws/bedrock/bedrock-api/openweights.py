import boto3

# 1. Initialize the Bedrock Runtime client for Amazon Bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# 2. Use Bedrock's Converse API to call an open-weight model
response = client.converse(
    modelId="openai.gpt-oss-120b-1:0",
    messages=[
        {"role": "user", "content": [{"text": "Hello World!"}]}
    ]
)

# gpt-oss is a reasoning model, so the first content block is often
# "reasoningContent" rather than "text" -- find the text block instead
# of assuming it's content[0].
for block in response["output"]["message"]["content"]:
    if "text" in block:
        print(block["text"])
        break
