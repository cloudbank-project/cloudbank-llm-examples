## Getting started

See the getting started instructions by Google at: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart

This directory authenticates to Google AI Studio with a Google Gen AI API Key. Use `gemini.py` to access Gemini models.

## Google Gen AI API Keys

Get a Google Gen AI API key from Google AI Studio at: https://aistudio.google.com/apikey

Set the following environment variable. `GEMINI_API_KEY` is read by the
`google-genai` SDK (used by `gemini.py`):

```bash
export GEMINI_API_KEY="your-google-gen-ai-api-key"
```

## Install python packages

pip package manager:

```bash
pip install google-genai
```

uv package manager:

```bash
uv add google-genai
```
