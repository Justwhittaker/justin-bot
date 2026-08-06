# Justin Bot

A personal Python bot starter for [JustWhittaker](https://github.com/JustWhittaker). Run it locally from the terminal, then extend it with APIs, webhooks, or chat platforms.

## Quick start

```bash
cd ~/Projects/justin-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Try: `hello`, `help`, `time`, `echo your message here`

## Project layout

```
justin-bot/
├── run.py              # Entry point
├── requirements.txt
├── .env.example        # Copy to .env for secrets
├── PRO4-Mealdeals/     # Git submodule — MealDeals Django app
├── .cursor/agents/     # Cursor Agents sidebar entries
└── src/justin_bot/
    ├── bot.py          # Core message handling
    └── main.py         # Interactive CLI loop
```

## Nested projects

[PRO4-Mealdeals](https://github.com/Justwhittaker/PRO4-Mealdeals) is included as a git submodule at `PRO4-Mealdeals/`.

```bash
git submodule update --init --recursive
```

## Next steps

- Add Discord, Slack, or Telegram adapters
- Wire in an LLM via OpenAI or Anthropic
- Deploy as a webhook on Render or Railway

## License

MIT
