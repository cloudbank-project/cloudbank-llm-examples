## Getting started

See the getting started instructions by Microsoft at: https://learn.microsoft.com/en-us/azure/ai-foundry/

This directory authenticates to Azure AI Foundry with an OpenAI-Compatible API Key. Use `chatgpt.py` to access GPT deployments, `claude.py` to access Anthropic's Claude models or `openweights.py` to access open-weights model deployments via Azure AI Foundry.

## OpenAI-Compatible API Key

Get the API key and endpoint from the Azure AI Foundry portal under your
resource's **Keys and Endpoint** page.

Set the following environment variables. The `OPENAI_*` variables are read by the
`openai` SDK (used by `chatgpt.py` and `openweights.py`), and the
`ANTHROPIC_FOUNDRY_*` variables are read by the `anthropic` SDK (used by
`claude.py`) -- both use the same Foundry API key value.

```bash
export OPENAI_API_KEY="your-foundry-api-key"
export OPENAI_BASE_URL="https://<your-resource>.openai.azure.com/openai/v1/"
export ANTHROPIC_FOUNDRY_API_KEY="your-foundry-api-key"
export ANTHROPIC_FOUNDRY_RESOURCE="<your-resource>"
```

`OPENAI_BASE_URL` is your resource endpoint with `/openai/v1/` appended.
`ANTHROPIC_FOUNDRY_RESOURCE` is just the resource name (the `<your-resource>`
part of the endpoint host).

## Install python packages

pip package manager:

```bash
    pip install anthropic openai
```

uv package manager:

```bash
    uv add anthropic openai
```
