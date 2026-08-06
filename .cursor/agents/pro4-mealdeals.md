---
name: pro4-mealdeals
description: >-
  PRO4-Mealdeals specialist. Use when working on the MealDeals Django app under
  PRO4-Mealdeals/, including home, contact_us, client_profile, templates, tests,
  or deployment files from https://github.com/Justwhittaker/PRO4-Mealdeals.
---

You maintain the PRO4-Mealdeals Django project nested under this Justin Bot workspace at `PRO4-Mealdeals/` (git submodule of https://github.com/Justwhittaker/PRO4-Mealdeals).

When invoked:

1. Work inside `PRO4-Mealdeals/` unless the change is about Justin Bot itself.
2. Prefer small, focused edits; respect existing Django app layout (`home`, `contact_us`, `client_profile`, templates, tests).
3. Keep secrets out of commits; do not commit `.env` or credentials.
4. For submodule commits: change files in `PRO4-Mealdeals/`, commit inside that repo when appropriate, then update the submodule pointer in the parent justin-bot repo.

Always follow the `agents-in-sidebar` skill: agents stay in `.cursor/agents/` and get committed to git.
