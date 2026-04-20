# Content Creator Flow

An AI-powered multi-agent marketing system built with CrewAI that analyzes product pages and generates high-converting marketing content, including ad copy, social posts, and strategic insights.

This project simulates a full digital marketing team that takes a product URL and turns it into actionable marketing intelligence and viral-ready content.

---

## What This Project Does

Given a product (e.g., an Amazon listing), the system:

- Analyzes product positioning and messaging
- Extracts target audience and emotional drivers
- Evaluates UX and conversion structure
- Identifies trust signals and weaknesses
- Generates marketing content (ads, captions, hooks, posts)

---

## 🏗️ Architecture

This project uses a **sequential multi-agent pipeline**:

### 1. Website Analysis Agent
- Scrapes and analyzes product page
- Extracts key features and positioning
- Evaluates messaging clarity and UX flow

### 2. Market Research Agent
- Identifies ideal customer profile
- Finds emotional triggers and motivations
- Defines positioning opportunities

### 3. Content Creation Agent
- Generates high-conversion ad copy
- Writes social media posts (Instagram, LinkedIn, TikTok style)
- Creates viral hooks and captions

---

## Tech Stack

- CrewAI (multi-agent orchestration)
- Python 3.12+
- Ollama (local LLM support)
- Google Gemini (optional cloud fallback)
- dotenv for environment management

---

## Setup

git clone https://github.com/itzskoala/content-creator-flow.git

cd content-creator-flow

python -m venv .venv

## Mac/Linux
source .venv/bin/activate

## Windows
.venv\Scripts\activate

##
uv sync or pip install -r requirements.txt

crewai run

## Example input

Product URL:
https://www.amazon.com/...

Extra context:
Premium kitten food focused on early development, brain health, and immune support.



