# CloudBank LLM Examples

Working examples of calling large language models on AWS, Azure and Google Cloud, using either real-time or batch inference. Each directory has its own `README.md` with setup instructions.

## Real-time inference

Short "Hello World" Python scripts that send a single prompt and print the response. Each directory contains one script per model family (`chatgpt.py`, `claude.py`, `gemini.py` and/or `openweights.py`).

| Service | Directory | Authentication |
|---------|-----------|----------------|
| AWS Bedrock | [`real-time/aws/bedrock/bedrock-api`](real-time/aws/bedrock/bedrock-api) | Bedrock API Keys, OAuth / User SSO, Key / Secret Pairs |
| AWS Bedrock | [`real-time/aws/bedrock/openai-api`](real-time/aws/bedrock/openai-api) | OpenAI API |
| AWS Bedrock Mantle | [`real-time/aws/bedrock-mantle`](real-time/aws/bedrock-mantle) | OpenAI API |
| Azure Foundry | [`real-time/azure/new-foundry/oauth`](real-time/azure/new-foundry/oauth) | OAuth / User SSO |
| Azure Foundry | [`real-time/azure/new-foundry/openai-api`](real-time/azure/new-foundry/openai-api) | OpenAI API |
| Google Agent Platform | [`real-time/google/agent-platform/oauth`](real-time/google/agent-platform/oauth) | OAuth / User SSO |
| Google AI Studio | [`real-time/google/ai-studio`](real-time/google/ai-studio) | Google Gen AI API Keys |

## Batch inference

Step-by-step walkthroughs for submitting a JSONL file of prompts as a batch job and retrieving the results.

| Service | Directory | Tools |
|---------|-----------|-------|
| AWS Bedrock | [`batch/aws`](batch/aws) | AWS CLI |
| Azure Foundry | [`batch/azure`](batch/azure) | Azure CLI and Python |
| Google Agent Platform | [`batch/google`](batch/google) | gcloud CLI and Python |
