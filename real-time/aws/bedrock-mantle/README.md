## Getting started

See the getting started instructions by AWS at: https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html

This directory authenticates to AWS Bedrock Mantle using the OpenAI API. First, create a Bedrock API key then install the required python packages. Use `chatgpt.py` to access OpenAI models, `claude.py` to access Anthropic's Claude models or `openweights.py` to access other open weight models via AWS Bedrock Mantle.

## OpenAI API

Create a Bedrock API key from the console or CLI: https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html. Note short term API keys are only valid in the region they were created in.

Set the following environment variables. The `OPENAI_*` variables are read by the `openai` SDK (used by `chatgpt.py` and `openweights.py`), and `AWS_BEARER_TOKEN_BEDROCK` is read by the `anthropic` SDK (used by `claude.py`) -- both use the same Bedrock API key value.

```bash
export OPENAI_API_KEY="your-bedrock-api-key"
export OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/v1"
export AWS_BEARER_TOKEN_BEDROCK="your-bedrock-api-key"
```

## Install python packages

pip package manager:

```bash
pip install anthropic openai
```

uv package manager:

```bash
uv add anthropic openai
```
