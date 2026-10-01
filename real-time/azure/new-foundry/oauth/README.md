## Getting started

See the getting started instructions by Microsoft at: https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal

This directory authenticates to Azure AI Foundry with OAuth (Microsoft Entra ID) credentials. Use `chatgpt.py` to access GPT deployments, `claude.py` to access Anthropic's Claude models or `openweights.py` to access open-weights model deployments via Azure AI Foundry.

## Authentication

Log in to your Azure account from the command line (any credential supported by
`DefaultAzureCredential` also works, e.g. a managed identity):

```bash
az login
```

## Environment variables

All three scripts read the Foundry resource name from an environment variable
instead of a hard-coded value:

```bash
export AZURE_FOUNDRY_RESOURCE="<your-resource>"
```

`<your-resource>` is the resource name (the host prefix of your endpoint, e.g.
`my-cloudbank` for `https://my-cloudbank.openai.azure.com/`).

## Install python packages

pip:

```bash
    pip install anthropic openai azure-identity
```

uv:

```bash
    uv add anthropic openai azure-identity
```
