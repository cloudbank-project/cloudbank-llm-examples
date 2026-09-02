import os

from google import genai

# 1. Initialize the client for Google Cloud Agent Platform -- reads
#    GOOGLE_CLOUD_PROJECT for the Google Cloud project ID
client = genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],  # your Google Cloud project ID
    location="us"
)

# 2. Create a chat session
# Use a Google model ID (e.g., "gemini-3.1-flash-lite")
chat = client.chats.create(model="gemini-3.1-flash-lite")

# 3. Send the "Hello World" message
response = chat.send_message("Hello World!")

print(response.text)
