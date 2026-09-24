import os
import time
from google import genai
from google.genai.types import CreateBatchJobConfig

# Set vertexai=True to use Vertex AI on Google Cloud
client = genai.Client(vertexai=True, project=os.getenv("PROJECT_ID"), location=os.getenv("LOCATION"))

batch_job = client.batches.create(
    model="gemini-2.5-flash-lite",
    src=f"gs://{os.getenv('BUCKET_NAME')}/inputs/batch_requests.jsonl",
    config=CreateBatchJobConfig(
        dest=f"gs://{os.getenv('BUCKET_NAME')}/outputs/"
    ),
)

print(f"Batch Job Submitted. Job Name: {batch_job.name}")

# Poll for completion
while True:
    job_status = client.batches.get(name=batch_job.name)
    print(f"Current State: {job_status.state}")
    
    if job_status.state == "JOB_STATE_SUCCEEDED":
        print("Job Completed!")
        print(f"Results located at: {job_status}")
        break
    elif job_status.state in ["JOB_STATE_FAILED", "JOB_STATE_CANCELLED"]:
        print(f"Job Failed: {job_status.error}")
        break
        
    time.sleep(60) # Check every minute