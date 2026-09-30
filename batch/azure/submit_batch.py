import os
import time
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

# Authenticate with Microsoft Entra ID (uses your `az login` session)
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

# Foundry v1 API endpoint: https://<RESOURCE_NAME>.openai.azure.com/openai/v1/
client = OpenAI(
    base_url=os.getenv("ENDPOINT"),
    api_key=token_provider,
)

# Upload the input file (expires after 14 days)
with open("batch_requests.jsonl", "rb") as f:
    input_file = client.files.create(
        file=f,
        purpose="batch",
        extra_body={"expires_after": {"seconds": 1209600, "anchor": "created_at"}},
    )
print(f"Uploaded input file: {input_file.id}")

batch_job = client.batches.create(
    input_file_id=input_file.id,
    endpoint="/chat/completions",
    completion_window="24h",
)

print(f"Batch Job Submitted. Job Name: {batch_job.id}")

# Poll for completion
while True:
    job_status = client.batches.retrieve(batch_job.id)
    print(f"Current State: {job_status.status}")

    if job_status.status == "completed":
        print("Job Completed!")
        print(f"Request counts: {job_status.request_counts}")
        # Responses are not returned in input order; match them using custom_id
        with open("batch_output.jsonl", "w") as out:
            out.write(client.files.content(job_status.output_file_id).text)
        if job_status.error_file_id:
            with open("batch_errors.jsonl", "w") as err:
                err.write(client.files.content(job_status.error_file_id).text)
        print("Results written to batch_output.jsonl")
        break
    elif job_status.status in ["failed", "expired", "cancelled"]:
        print(f"Job Failed: {job_status.errors}")
        break

    time.sleep(60)  # Check every minute
