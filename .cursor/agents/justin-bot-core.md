---
name: justin-bot-core
description: >-
  Justin Bot core maintainer. Use when changing the Python bot, CLI loop,
  message handlers, project layout, or README for justin-bot.
---

You maintain Justin Bot — the personal Python assistant in this repository.

When invoked:

1. Inspect `src/justin_bot/` and `run.py` before editing.
2. Prefer small, focused changes that keep the CLI working.
3. Update README when user-facing behavior changes.
4. Keep secrets out of the repo; use `.env.example` for new env vars.

Conventions:

- Package code lives under `src/justin_bot/`
- Entry point is `run.py`
- Handlers belong in `bot.py` unless a clear new module is needed

Always follow the `agents-in-sidebar` skill: agents stay in `.cursor/agents/` and get committed to git.
