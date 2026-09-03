import os

from google import genai

# 1. Initialize the client for Google AI Studio -- reads GEMINI_API_KEY for the
#    AI Studio API key
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"],  # your Google AI Studio API key
)

# 2. Create a chat session
# Use a Google model ID (e.g., "gemini-3.1-flash-lite")
chat = client.chats.create(model="gemini-3.1-flash-lite")

# 3. Send the "Hello World" message
response = chat.send_message("Hello World!")

print(response.text)
