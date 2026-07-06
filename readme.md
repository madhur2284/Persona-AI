# Persona Chatbot — Hitesh Choudhary & Piyush Garg

A CLI-based AI chatbot that simulates conversations with two well-known Indian tech educators, Hitesh Choudhary and Piyush Garg, replicating their distinct speaking style, teaching approach, and personality using LLM-based persona prompting.

## Features
- **Switch between two personas**: Hitesh Choudhary (calm, Hinglish, chai-loving mentor) and Piyush Garg (energetic, Gen-Z, "X is dead" series creator).
- **Persona-consistent responses**: Driven by detailed system prompts built from studying each person's public content (YouTube videos, talks).
- **Structured JSON-based response pipeline**: Built for reliable parsing.
- **Conversation context**: Maintained seamlessly across the session.

## Tech Stack
* Python 3
* OpenAI-compatible async client (`openai` SDK) — works with any OpenAI-compatible provider (OpenRouter, Groq, NVIDIA NIM, Gemini, etc.)
* `json5` for lenient JSON parsing
* `python-dotenv` for environment configuration

## Project Structure
```text
.
├── chat.py                          # Main CLI entry point
├── hitesh_chaudhary_system_prompt.py   # Hitesh persona system prompt
├── piyush_garg_system_prompt.py     # Piyush persona system prompt
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
└── .env                             # Your local environment config (not committed)
```

## Setup & Run Instructions

### 1. Clone the repository
```bash
git clone https://github.com/madhur2284/Persona-AI.git
cd PERSONA_AI
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Set up environment variables
```bash
cp .env.example .env
```

Open `.env` and fill in your values:
```ini
API_KEY=your_api_key_here
BASE_URL=your_provider_base_url_here
MODEL=your_model_name_here
```

This project works with any OpenAI-compatible provider. Recommended options:
* **OpenRouter**: `BASE_URL=https://openrouter.ai/api/v1` (get a key at openrouter.ai/keys)
* **Groq**: `BASE_URL=https://api.groq.com/openai/v1` (get a key at console.groq.com/keys)
* **Google Gemini**: via AI Studio (aistudio.google.com)

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the chatbot
```bash
python chat.py
```

You'll be prompted to choose a persona (Hitesh or Piyush). Type your messages and press enter to chat. Type a closing message like `bye` to end the session.
