## Set up Azure Foundry with the Azure CLI

These steps are shared by the `oauth` and `openai-api` examples. They use the Azure CLI (`az`) to create the Foundry resource, project and model deployments that the example scripts call. See the Microsoft quickstart at: https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources

Install the Azure CLI (`az`), then log in and select the subscription to use.

```bash
az login
az account list --output table
az account set --subscription "<YOUR_SUBSCRIPTION_ID_OR_NAME>"
```

## Check if the Foundry resources already exist

If you already have an Azure Foundry resource, look up its name and resource group instead of creating new ones. (In the new Foundry, resources are of kind `AIServices`; older standalone Azure OpenAI resources are kind `OpenAI`.)

```bash
az cognitiveservices account list --query "[?kind=='AIServices' || kind=='OpenAI'].{name:name, kind:kind, resourceGroup:resourceGroup, location:location}" --output table
```

Check which models it already has deployed.

```bash
az cognitiveservices account deployment list --name <EXISTING_RESOURCE> --resource-group <EXISTING_RESOURCE_GROUP> --query "[].{name:name, model:properties.model.name, sku:sku.name}" --output table
```

If the deployments you need are listed, skip to the step that gets the endpoint. The resource must have a custom subdomain, so that `https://<AZURE_FOUNDRY_RESOURCE>.openai.azure.com` resolves.

## Create the Foundry resource and project

Skip this section if they already exist.

```bash
export AZURE_RESOURCE_GROUP="<YOUR_RESOURCE_GROUP>"
export AZURE_FOUNDRY_RESOURCE="<YOUR_UNIQUE_RESOURCE>"
export LOCATION="eastus2"
```

Create the resource group if it doesn't already exist.

```bash
az group create --name $AZURE_RESOURCE_GROUP --location $LOCATION
```

Create the Foundry resource (kind `AIServices`) with project management enabled. The `--custom-domain` flag is required so the resource gets the `https://<AZURE_FOUNDRY_RESOURCE>.openai.azure.com` endpoint the scripts use and so Microsoft Entra token authentication works.

```bash
az cognitiveservices account create \
  --name $AZURE_FOUNDRY_RESOURCE \
  --resource-group $AZURE_RESOURCE_GROUP \
  --location $LOCATION \
  --kind AIServices \
  --sku S0 \
  --custom-domain $AZURE_FOUNDRY_RESOURCE \
  --allow-project-management
```

Create a Foundry project in the resource. The project is what you see in the new Foundry portal (https://ai.azure.com); the scripts call the resource endpoint directly.

```bash
az cognitiveservices account project create \
  --name $AZURE_FOUNDRY_RESOURCE \
  --resource-group $AZURE_RESOURCE_GROUP \
  --project-name ${AZURE_FOUNDRY_RESOURCE}-project \
  --location $LOCATION
```

## Deploy a model

List the models available in your region, with their versions and SKUs.

```bash
az cognitiveservices model list --location $LOCATION \
  --query "[?kind=='AIServices'].{format:model.format, name:model.name, version:model.version, skus:model.skus[].name}" --output table
```

Deploy a model, using the model name (the `name` column above, e.g. `gpt-5.6-luna`, `claude-haiku-4-5`, `grok-4.6` or `Ministral-3B`) as the deployment name too. The example scripts (`chatgpt.py`, `claude.py`, `grok.py` and `openweights.py`) read this value from the `MODEL` environment variable and pass it as `model=`, so keep `MODEL` set to the deployment you want to call. Set `MODEL_FORMAT` to the `format` column from the list above (e.g. `OpenAI`, `Anthropic`, `xAI`, `Mistral AI`) and use a SKU that the model lists. For real-time calls use a `GlobalStandard` or `Standard` SKU, not `GlobalBatch`.

```bash
export MODEL="<MODEL_NAME>"
export MODEL_VERSION="<MODEL_VERSION>"
export MODEL_FORMAT="OpenAI"

az cognitiveservices account deployment create \
  --name $AZURE_FOUNDRY_RESOURCE \
  --resource-group $AZURE_RESOURCE_GROUP \
  --deployment-name $MODEL \
  --model-name $MODEL \
  --model-version $MODEL_VERSION \
  --model-format $MODEL_FORMAT \
  --sku-name GlobalStandard \
  --sku-capacity 50
```

Repeat for each model you want to try (changing `MODEL`, `MODEL_VERSION` and `MODEL_FORMAT`). Some third-party models (for example Anthropic's Claude) may require accepting the provider's terms or have extra access requirements in your subscription; if the deployment fails, create it once in the Foundry portal and re-run.

## Get the endpoint and credentials

The endpoint of the resource is:

```bash
echo "https://$AZURE_FOUNDRY_RESOURCE.openai.azure.com/"
```

For the **openai-api** example, also get an API key.

```bash
az cognitiveservices account keys list --name $AZURE_FOUNDRY_RESOURCE --resource-group $AZURE_RESOURCE_GROUP --query key1 --output tsv
```

For the **oauth** example, no key is needed.

## Clean up (optional)

Delete the project first (the resource can't be deleted while it has nested projects), then the resource, and purge it so the name can be reused. Deleting the resource also removes its model deployments.

```bash
az cognitiveservices account project delete --name $AZURE_FOUNDRY_RESOURCE --resource-group $AZURE_RESOURCE_GROUP --project-name ${AZURE_FOUNDRY_RESOURCE}-project
az cognitiveservices account delete --name $AZURE_FOUNDRY_RESOURCE --resource-group $AZURE_RESOURCE_GROUP
az cognitiveservices account purge --name $AZURE_FOUNDRY_RESOURCE --resource-group $AZURE_RESOURCE_GROUP --location $LOCATION
```
