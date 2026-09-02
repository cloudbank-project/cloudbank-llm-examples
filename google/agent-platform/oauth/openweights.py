import os

import google.auth
import google.auth.transport.requests
from openai import OpenAI

# 1. Read GOOGLE_CLOUD_PROJECT to build the Vertex AI MaaS endpoint
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]  # your Google Cloud project ID
location = "us-central1"

# 2. Fetch GCP OAuth credentials
credentials, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)

# 3. Point the OpenAI SDK to the Vertex AI MaaS endpoint
client = OpenAI(
    base_url=f"https://{location}-aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/{location}/endpoints/openapi",
    api_key=credentials.token,
)

# 4. Use the managed API ID: "gpt-oss-20b-maas"
response = client.chat.completions.create(
    model="openai/gpt-oss-20b-maas",
    messages=[{"role": "user", "content": "Hello World!"}],
)

print(response.choices[0].message.content)
