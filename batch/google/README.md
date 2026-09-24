## Getting started

See the getting started instructions by Google at: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-cloud-storage

## Create the JSONL input file with the prompts

See the the `batch_requests.jsonl` in this directory. Full documentation is available at: https://ai.google.dev/gemini-api/docs/batch-api?utm_source=gemini

## Environment Setup

Install the required dependencies using UV package manager.

```bash
uv sync
```

Login to your Google Cloud account using the gcloud command-line tool.

```bash
gcloud auth login
```

Get the project ID.

```bash
gcloud config get-value project
```

Set the environment variables for the bucket name, project ID, location, and model.

```bash
export BUCKET_NAME="<YOUR_BUCKET_NAME>"
export PROJECT_ID="<YOUR_PROJECT_ID>"
export LOCATION="us-central1"
export MODEL="gemini-2.5-flash-lite"
```

## Create the Cloud Storage bucket

Create the Cloud Storage bucket if it doesn't already exist.

```bash
gcloud storage buckets create gs://$BUCKET_NAME --location=$LOCATION --uniform-bucket-level-access
```

## Upload the batch inference input file and submit the batch inference job

Upload the batch inference JSONL file to the Cloud Storage bucket.

```bash
gcloud storage cp batch_requests.jsonl gs://$BUCKET_NAME/inputs/batch_requests.jsonl
```

Submit the batch inference job.

```bash
uv run ./submit_batch.py 
```

List batch inference results.

```bash
gcloud storage ls gs://$BUCKET_NAME/outputs/
```
