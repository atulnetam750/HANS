# HANS — AI Automation Assistant

> A practical, Hindi-friendly foundation for AI assistance, automation, voice interaction, and API workflows.

## What is HANS?

HANS is an early-stage personal AI assistant project designed to connect natural-language commands with useful digital tools and repeatable automation. The project is being developed incrementally with a lightweight Python core.

## Current features

- Interactive command-line assistant
- Hindi-friendly commands and responses
- Built-in help, date, time, and status commands
- Environment-based configuration
- Optional n8n webhook integration
- Optional Hindi text-to-speech scaffold
- Basic automated tests
- Secret-safe `.env.example` and `.gitignore`

## Architecture

```text
User
  ↓
CLI / Voice / Future Web UI
  ↓
Command Router
  ↓
HANS Core
  ├── Local Commands
  ├── AI Provider (planned)
  └── Tools / Skills
        ├── n8n Webhooks
        ├── APIs
        ├── Voice
        └── Future News/Content Workflows
```

## Repository structure

```text
HANS/
├── main.py
├── hans/
│   ├── __init__.py
│   ├── n8n.py
│   └── voice.py
├── tests/
│   └── test_core.py
├── .env.example
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## Quick start

```bash
git clone https://github.com/atulnetam750/HANS.git
cd HANS
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run HANS:

```bash
python main.py
```

Try:

```text
help
time
date
status
नमस्ते
exit
```

## Environment configuration

Copy `.env.example` to `.env` for local configuration. Never commit real API keys, passwords, tokens, or private data.

## n8n integration

The `hans.n8n` module provides a small JSON webhook helper. Set `N8N_WEBHOOK_URL` in your local environment and use the helper from your own workflow or application code.

## Voice

`hans.voice` provides an optional text-to-speech scaffold using gTTS. Voice input and full conversational speech interaction are planned features.

## Roadmap

- [x] Initial CLI foundation
- [x] Hindi-friendly command handling
- [x] n8n webhook helper
- [x] Optional voice/TTS scaffold
- [x] Basic tests
- [ ] AI provider abstraction
- [ ] Tool/plugin registry
- [ ] Speech-to-text input
- [ ] Full Hindi voice assistant
- [ ] Web dashboard
- [ ] News/content automation workflows
- [ ] Authentication and permissions
- [ ] Docker deployment
- [ ] CI/CD and release automation

## Project philosophy

HANS is intended to be useful, modular, transparent, and easy to extend. Features should be added as real working functionality rather than simulated usage or inflated project metrics.

## Open-source status

This is an early development project. Public usage, downloads, contributors, and community impact are not claimed until they actually exist.

## License

MIT License. See [LICENSE](LICENSE).
