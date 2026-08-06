#!/usr/bin/env python3
"""Run Justin Bot from the project root."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from justin_bot.main import main

if __name__ == "__main__":
    raise SystemExit(main())
