## Getting started

See the getting started instructions by Google at: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start

This directory authenticates to the Google Cloud Agent Platform (Vertex AI) with OAuth (Application Default Credentials). Use `gemini.py` to access Gemini models, `claude.py` to access Anthropic's Claude models or `openweights.py` to access open-weights model deployments via the Vertex AI Model-as-a-Service endpoint.

## Authentication

Log in to your Google Cloud account from the command line (any credential supported by Application Default Credentials also works, e.g. a service account):

```bash
gcloud auth application-default login
```

Optionally, create and activate a named configuration for your profile first:

```bash
gcloud config configurations create your-profile-name
gcloud config configurations activate your-profile-name
```

To look up your project ID:

```bash
gcloud config get-value project
```

## Environment variables

All three scripts read the Google Cloud project ID from an environment variable
instead of a hard-coded value:

```bash
export GOOGLE_CLOUD_PROJECT="<your-project-id>"
```

`<your-project-id>` is the project ID (not the project number or display name),
e.g. `my-cloudbank-project`.

## Install python packages

pip package manager:

```bash
pip install "anthropic[vertex]" openai google-genai google-auth
```

uv package manager:

```bash
uv add "anthropic[vertex]" openai google-genai google-auth
```
