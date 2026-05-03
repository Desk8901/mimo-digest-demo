# MiMo Digest Demo

A lightweight Streamlit demo built on the Xiaomi MiMo API for turning long-form text into structured outputs: concise summaries, action items, and Mermaid mind maps.

## What It Does

This project is designed for product, research, and knowledge-work scenarios where raw text is long, messy, and time-consuming to process manually. Instead of generic chat, it focuses on a fixed workflow:

1. Read long-form unstructured text
2. Extract key points into an actionable summary
3. Generate action items
4. Produce Mermaid mind map code for downstream use

## Demo Features

- MiMo API integration via OpenAI-compatible client
- Configurable `API Key`, `Base URL`, and `Model Name`
- Structured output for summary, actions, and Mermaid map
- Basic validation info including latency and input/output length
- Streamlit UI for quick testing and iteration

## Tech Stack

- Python 3.10+
- Streamlit
- OpenAI Python SDK
- Xiaomi MiMo API

## Project Structure

```text
mimo-digest-demo/
├── README.md
├── requirements.txt
├── .gitignore
├── streamlit_app.py
└── docs/
    ├── project-brief.md
    └── evidence-notes.md
```

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Optional environment variables

You can set these in your shell before running:

```bash
export MIMO_API_KEY="your-api-key"
export MIMO_BASE_URL="https://api.xiaomimimo.com/v1"
export MIMO_MODEL="mimo-v2.5-pro"
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

## Use Cases

- Summarizing long product requirement documents
- Converting meeting notes into action items
- Organizing research material into structured outputs
- Transforming long text into reusable knowledge artifacts

## Why This Project Applies for MiMo 100T

This demo is intended for real workflow validation rather than casual chat usage. If granted MiMo 100T credits, the next step is to expand testing in three directions:

1. Longer document stability testing
2. Prompt iteration and output-quality comparison
3. Higher-frequency usage in real product and research workflows

## Suggested Submission Evidence

For the MiMo 100T application form, the strongest supporting materials are:

1. A screenshot of the code/editor view
2. A screenshot of the running Streamlit page
3. A screenshot of the generated output
4. A GitHub repository link to this project

## Notes

- The current demo is intentionally small and focused.
- It is designed to show a real MiMo-powered workflow prototype, not a static mockup.
- Supporting project notes are available in the `docs/` folder.
