# Project Brief

## One-Line Summary

A Xiaomi MiMo API demo for converting long-form text into structured outputs including summaries, action items, and Mermaid mind maps.

## Problem

Product documents, research notes, and meeting records are often long and unstructured. Manual extraction takes time and the output format is inconsistent. This demo focuses on reducing that friction by converting raw text directly into reusable working artifacts.

## Current Scope

- Input: long-form text such as PRDs, meeting notes, and research materials
- Output:
  - executive summary
  - action items
  - Mermaid mind map code
- Interface: Streamlit demo with configurable API connection fields

## Why MiMo

- Long-context handling is important for document-heavy scenarios
- Structured output quality matters for downstream use
- The project needs enough credits for prompt iteration and repeated workflow testing

## Current Status

- A runnable Streamlit prototype is ready
- MiMo API integration is set up through an OpenAI-compatible client
- Output validation info is shown in the UI
- The next phase is larger-scale testing with longer inputs and prompt comparisons

## Intended Use of MiMo 100T

1. Stability testing on longer inputs
2. Prompt-template iteration
3. Repeated usage in realistic product and research workflows
