## Getting started

See the getting started instructions by AWS at: https://aws.amazon.com/bedrock/getting-started/

AWS Bedrock supports authentication via OpenAI-Compatible API Key. First, install the required python packages. Use `openweights.py` to access open-weights models via AWS Bedrock.

## OpenAI-Compatible API Key

Get the API key and region from the AWS Bedrock console. Note short term API keys are only valid in the region they were created in.

```bash
export OPENAI_API_KEY="bedrock-api-key-<bedrock-api-key>"
export OPENAI_BASE_URL="https://bedrock-runtime.<aws-region>.amazonaws.com/openai/v1"
```

## Install python packages

pip package manager:

```bash
    pip install openai
```

uv package manager:

```bash
    uv add openai
```
