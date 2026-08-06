from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

from justin_bot.bot import JustinBot


def main() -> int:
    load_dotenv()

    bot = JustinBot()
    print("Justin Bot — type a message (Ctrl+C or 'quit' to exit)\n")

    while True:
        try:
            message = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return 0

        if message.lower() in {"quit", "exit", "q"}:
            print("Bye!")
            return 0

        response = bot.handle(message)
        print(f"bot> {response.text}\n")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    raise SystemExit(main())
