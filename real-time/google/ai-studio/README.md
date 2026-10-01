## Getting started

See the getting started instructions by Google at: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart

This directory authenticates to Google AI Studio with an API key. Use `gemini.py` to access Gemini models.

## API key

Get an API key from Google AI Studio at: https://aistudio.google.com/apikey

Set the following environment variable. `GEMINI_API_KEY` is read by the
`google-genai` SDK (used by `gemini.py`):

```bash
export GEMINI_API_KEY="your-ai-studio-api-key"
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
