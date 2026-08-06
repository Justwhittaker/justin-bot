# Justin Bot

A personal Python bot starter for [JustWhittaker](https://github.com/JustWhittaker). Run it locally from the terminal, then extend it with APIs, webhooks, or chat platforms.

Lives under the parent workspace `~/Projects/JustinBot/` next to `MealDeals/` and other site ideas.

## Quick start

```bash
cd ~/Projects/JustinBot/justin-bot
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
├── .cursor/agents/     # Cursor Agents sidebar entries
└── src/justin_bot/
    ├── bot.py          # Core message handling
    └── main.py         # Interactive CLI loop
```

## Sibling projects

Related websites live beside this repo under `~/Projects/JustinBot/`:

- `MealDeals/` — [PRO4-Mealdeals](https://github.com/Justwhittaker/PRO4-Mealdeals)
- `ideas/` — scratch notes for new concepts
- Add more with `mkdir ~/Projects/JustinBot/My-New-Site`

## Next steps

- Add Discord, Slack, or Telegram adapters
- Wire in an LLM via OpenAI or Anthropic
- Deploy as a webhook on Render or Railway

## License

MIT
