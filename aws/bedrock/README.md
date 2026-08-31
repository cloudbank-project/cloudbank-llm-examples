## Getting started

See the getting started instructions by AWS at: https://aws.amazon.com/bedrock/getting-started/

AWS Bedrock supports authentication via OAuth / User SSO or Key / Secret Pairs. First, select an authentication method then install the required python packages. Use `claude.py` to access Anthropic's Claude models or `openweights.py` to access open-weights models via AWS Bedrock.

## OAuth / User SSO

Login to your AWS account from the command line:

```bash
aws login --profile your-profile-name
```

Set the default profile for the current session:

```bash
export AWS_PROFILE=your-profile-name
```

## Key / Secret Pairs

```bash
export AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

## Install python packages

pip package manager:

```bash
    pip install "anthropic[bedrock]" boto3 "botocore[crt]"
```

uv package manager:

```bash
    uv add "anthropic[bedrock]" boto3 "botocore[crt]"
```
