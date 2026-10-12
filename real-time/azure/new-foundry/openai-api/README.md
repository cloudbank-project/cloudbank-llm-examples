## Getting started

See the getting started instructions by Microsoft at: https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources

This directory authenticates to Azure Foundry using the OpenAI API. Use `chatgpt.py` to access GPT deployments, `claude.py` to access Anthropic's Claude models, `grok.py` to access xAI's Grok deployments or `openweights.py` to access open-weights model deployments via Azure Foundry.

## Create the Foundry resources

If you don't already have a Foundry resource, project and model deployments, follow the Azure CLI instructions in [SETUP.md](../SETUP.md), which also shows how to get the API key.

## OpenAI API

Get the API key and endpoint with the `az` commands in [SETUP.md](../SETUP.md), or from the Azure Foundry portal under your resource's **Keys and Endpoint** page.

Set the following environment variables. The `OPENAI_*` variables are read by the
`openai` SDK (used by `chatgpt.py`, `grok.py` and `openweights.py`), and the
`ANTHROPIC_FOUNDRY_*` variables are read by the `anthropic` SDK (used by
`claude.py`) -- both use the same Foundry API key value.

```bash
export OPENAI_API_KEY="your-foundry-api-key"
export OPENAI_BASE_URL="https://$AZURE_FOUNDRY_RESOURCE.openai.azure.com/openai/v1/"
export ANTHROPIC_FOUNDRY_API_KEY="your-foundry-api-key"
export ANTHROPIC_FOUNDRY_RESOURCE="$AZURE_FOUNDRY_RESOURCE"
export MODEL="<your-model-deployment>"
```

`MODEL` is the name of the model deployment to call (e.g. `gpt-5.6-luna` for
`chatgpt.py`, `claude-haiku-4-5` for `claude.py`); all scripts read it.

`AZURE_FOUNDRY_RESOURCE` is the Foundry resource name (the host prefix of your
endpoint), the same variable used in [SETUP.md](../SETUP.md); set it first, e.g.
`export AZURE_FOUNDRY_RESOURCE="<your-resource>"`.
`OPENAI_BASE_URL` is your resource endpoint with `/openai/v1/` appended.

## Install python packages

pip package manager:

```bash
pip install anthropic openai
```

uv package manager:

```bash
uv add anthropic openai
```
