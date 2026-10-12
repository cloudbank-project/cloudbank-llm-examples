## Getting started

See the getting started instructions by Microsoft at: https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources

This directory authenticates to Azure Foundry with OAuth / User SSO (Microsoft Entra ID). Use `chatgpt.py` to access GPT deployments, `claude.py` to access Anthropic's Claude models, `grok.py` to access xAI's Grok deployments or `openweights.py` to access open-weights model deployments via Azure Foundry.

## Create the Foundry resources

If you don't already have a Foundry resource, project and model deployments, follow the Azure CLI instructions in [SETUP.md](../SETUP.md). The `AZURE_FOUNDRY_RESOURCE` variable used there is the same one set below.

## OAuth / User SSO

Log in to your Azure account from the command line (any credential supported by
`DefaultAzureCredential` also works, e.g. a managed identity):

```bash
az login
```

## Environment variables

All scripts read the Foundry resource name and the model deployment name from environment variables instead of hard-coded values:

```bash
export AZURE_FOUNDRY_RESOURCE="<your-resource>"
export MODEL="<your-model-deployment>"
```

`<your-resource>` is the resource name (the host prefix of your endpoint, e.g.
`my-cloudbank` for `https://my-cloudbank.openai.azure.com/`).

## Install python packages

pip package manager:

```bash
pip install anthropic openai azure-identity
```

uv package manager:

```bash
uv add anthropic openai azure-identity
```
