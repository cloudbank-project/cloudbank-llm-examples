## Getting started

See the getting started instructions for Microsoft Foundry (new) by Azure at: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/batch

The Azure CLI (`az`) has no commands for the Azure OpenAI Files and Batch APIs, so this example uses `az` for everything it can (login, Foundry resource and project creation, model deployment, role assignment) and the Python SDKs for uploading the file and running the batch job.

## Create the JSONL input file with the prompts

See the `batch_requests.jsonl` in this directory. The `model` field on every line must be the name of your **GlobalBatch deployment** (created below as `gpt-4.1-mini-batch`), and all lines must use the same model and URL. The file must be UTF-8 without a Byte Order Mark (BOM). 

## Environment Setup

Install the required dependencies using UV package manager.

```bash
uv sync
```

Login to your Azure account using the az command-line tool.

```bash
az login
```

List your subscriptions and select the one to use.

```bash
az account list --output table
az account set --subscription "<YOUR_SUBSCRIPTION_ID_OR_NAME>"
```

## Check if the Foundry resources already exist

If you already have a Microsoft Foundry resource, look up its name and resource group instead of creating new ones. (In the new Foundry, resources are of kind `AIServices`; older standalone Azure OpenAI resources are kind `OpenAI`.)

```bash
az cognitiveservices account list --query "[?kind=='AIServices' || kind=='OpenAI'].{name:name, kind:kind, resourceGroup:resourceGroup, location:location}" --output table
```

Then set `RESOURCE_GROUP`, `RESOURCE_NAME` and `LOCATION` below to the values listed. Check whether it already has a `GlobalBatch` deployment.

```bash
az cognitiveservices account deployment list --name <EXISTING_RESOURCE_NAME> --resource-group <EXISTING_RESOURCE_GROUP> --query "[].{name:name, model:properties.model.name, sku:sku.name}" --output table
```

If one is listed, set `DEPLOYMENT_NAME` to its name (and update the `model` field in `batch_requests.jsonl` to match), then skip to the step that gets the endpoint. The resource must have a custom subdomain, so that `https://<RESOURCE_NAME>.openai.azure.com` resolves.

## Create the Foundry resource, project and Global Batch deployment, if they don't already exist.

Set the environment variables for the resource group, Foundry resource name, location, and model. See https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/batch for which models support the Global Batch deployment.

```bash
export RESOURCE_GROUP="<YOUR_RESOURCE_GROUP>"
export RESOURCE_NAME="<YOUR_UNIQUE_RESOURCE_NAME>"
export LOCATION="eastus2"
export DEPLOYMENT_NAME="gpt-4.1-mini-batch"
export MODEL="gpt-4.1-mini"
export MODEL_VERSION="2025-04-14"
```

Create the resource group if it doesn't already exist.

```bash
az group create --name $RESOURCE_GROUP --location $LOCATION
```

Create the Foundry resource (kind `AIServices`) with project management enabled. The `--custom-domain` flag is required so the resource gets the `https://<RESOURCE_NAME>.openai.azure.com` endpoint that batch needs and so Microsoft Entra token authentication works.

```bash
az cognitiveservices account create \
  --name $RESOURCE_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --kind AIServices \
  --sku S0 \
  --custom-domain $RESOURCE_NAME \
  --allow-project-management
```

Create a Foundry project in the resource. The project is what you see in the new Foundry portal (https://ai.azure.com); the batch API itself is called on the resource endpoint.

```bash
az cognitiveservices account project create \
  --name $RESOURCE_NAME \
  --resource-group $RESOURCE_GROUP \
  --project-name ${RESOURCE_NAME}-project \
  --location $LOCATION
```

## Deploy the model

Deploy the model with the `GlobalBatch` SKU. Check that your region supports Global Batch for the model in the model availability table in the documentation above.

```bash
az cognitiveservices account deployment create \
  --name $RESOURCE_NAME \
  --resource-group $RESOURCE_GROUP \
  --deployment-name $DEPLOYMENT_NAME \
  --model-name $MODEL \
  --model-version $MODEL_VERSION \
  --model-format OpenAI \
  --sku-name GlobalBatch \
  --sku-capacity 50
```

## Upload the batch inference input file and submit the batch inference job

Set the Foundry v1 API endpoint of the resource. 

```bash
export ENDPOINT="https://$RESOURCE_NAME.openai.azure.com/openai/v1/"
```

Upload the input file (set to expire after 14 days), submit the batch inference job, poll until it finishes, and download the results. The output is written to `batch_output.jsonl` (and failed requests to `batch_errors.jsonl`). Responses are not returned in input order; match them using `custom_id`.

```bash
uv run ./submit_batch.py
```

## Clean up (optional)

Delete the project first (the resource can't be deleted while it has nested projects), then the resource, and purge it so the name can be reused. Deleting the resource also removes its model deployments.

```bash
az cognitiveservices account project delete --name $RESOURCE_NAME --resource-group $RESOURCE_GROUP --project-name ${RESOURCE_NAME}-project
az cognitiveservices account delete --name $RESOURCE_NAME --resource-group $RESOURCE_GROUP
az cognitiveservices account purge --name $RESOURCE_NAME --resource-group $RESOURCE_GROUP --location $LOCATION
```
