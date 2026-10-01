## Getting started

See the getting started instructions for Amazon Bedrock batch inference at: https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html

**You must first contact CloudBank Support to have the BedrockBatchInferenceRole role created and the necessary permissions assigned to your account.**

Everything in this example is done with the AWS CLI (`aws`).

## Create the JSONL input file with the prompts

See the `batch_requests.jsonl` in this directory. Each line has a `recordId` and a `modelInput`. The `modelInput` must match the request body of the model's `InvokeModel` API. Bedrock requires a **minimum of 100 records** per job by default.

## Environment Setup

Install the AWS CLI and log in. Use either `aws login` or `aws configure` (access keys).

Verify which account you are using.

```bash
aws sts get-caller-identity
```

Set the environment variables for the bucket name, region, model, and IAM role name. S3 bucket names are globally unique, so pick your own.

```bash
export BUCKET_NAME="<YOUR_BUCKET_NAME>"
export AWS_REGION="us-east-1"
export MODEL_ID="amazon.nova-lite-v1:0"
export ROLE_NAME="BedrockBatchInferenceRole"
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --query Role.Arn --output text)
```

Confirm the model supports batch inference (`InvokeModel` and `Converse` batch support varies by model and Region) and that you have access to it.

```bash
aws bedrock list-foundation-models --region $AWS_REGION --query "modelSummaries[?modelId=='$MODEL_ID'].{id:modelId,name:modelName,status:modelLifecycle.status}" --output table
```

## Create the S3 bucket

Create the S3 bucket if it doesn't already exist. The bucket must be in the same Region as the batch job.

```bash
aws s3 mb s3://$BUCKET_NAME --region $AWS_REGION
```

## Upload the batch inference input file and submit the batch inference job

Upload the batch inference JSONL file to the S3 bucket.

```bash
aws s3 cp batch_requests.jsonl s3://$BUCKET_NAME/inputs/batch_requests.jsonl
```

Submit the batch inference job.

```bash
export JOB_ARN=$(aws bedrock create-model-invocation-job \
  --region $AWS_REGION \
  --job-name "batch-example-$(date +%Y%m%d%H%M%S)" \
  --model-id $MODEL_ID \
  --role-arn $ROLE_ARN \
  --input-data-config "s3InputDataConfig={s3Uri=s3://$BUCKET_NAME/inputs/}" \
  --output-data-config "s3OutputDataConfig={s3Uri=s3://$BUCKET_NAME/outputs/}" \
  --query jobArn --output text)
echo $JOB_ARN
```

Check the job status. It moves through `Submitted`, `Validating`, `Scheduled`, `InProgress`, and finally `Completed` (or `Failed`, `Stopped`, `PartiallyCompleted`). Jobs can take from several minutes to many hours.

```bash
aws bedrock get-model-invocation-job --region $AWS_REGION --job-identifier $JOB_ARN --query '{status:status,message:message}'
```

List your batch inference jobs.

```bash
aws bedrock list-model-invocation-jobs --region $AWS_REGION --query 'invocationJobSummaries[].{name:jobName,status:status,submitted:submitTime}' --output table
```

## Retrieve the batch inference results

When the job is `Completed`, list the results. Bedrock writes a folder named after the job ID under the output prefix, containing `<input file>.out` (the model responses), and `manifest.json.out` (a summary of record counts and token usage).

```bash
export JOB_ID=${JOB_ARN##*/}
aws s3 ls s3://$BUCKET_NAME/outputs/$JOB_ID/
```

Download the results.

```bash
aws s3 cp s3://$BUCKET_NAME/outputs/$JOB_ID/ ./results/ --recursive
head -n 1 results/batch_requests.jsonl.out
cat results/manifest.json.out
```

Each line of the `.out` file has the `recordId`, the original `modelInput`, and the `modelOutput` (or an `error`). The order of records is not guaranteed to match the input.

To cancel a job that is still running:

```bash
aws bedrock stop-model-invocation-job --region $AWS_REGION --job-identifier $JOB_ARN
```

## Clean up (optional)

```bash
aws s3 rm s3://$BUCKET_NAME --recursive
aws s3 rb s3://$BUCKET_NAME
```
