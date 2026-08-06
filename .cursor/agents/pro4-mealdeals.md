---
name: pro4-mealdeals
description: >-
  PRO4-Mealdeals specialist. Use for the Meal Deals platform under
  PRO4-Mealdeals/: new FastAPI backend/ and Next.js frontend/ (global
  multi-region), plus the legacy Django apps (home, memberships, etc.).
---

You maintain the PRO4-Mealdeals project (git repo / submodule of
https://github.com/Justwhittaker/PRO4-Mealdeals).

## Current architecture (target)

Greenfield global multi-region stack lives alongside the legacy Django app:

- `backend/` — FastAPI (Python 3.12+), async SQLAlchemy, PostGIS, Redis, Celery, Docker Compose
- `frontend/` — Next.js App Router, TypeScript, Tailwind, shadcn/ui, Stripe, AdSense
- Legacy Django (`home/`, `memberships/`, `mealdeals/`, etc.) remains until migration is complete

### Backend highlights

- Country subdirectory routing via ISO-3166-1 alpha-2 (`/us/`, `/uk/`, …)
- Models: locations (PostGIS), merchants, deals, deal_items, deal_translations, currencies
- Affiliate cloaker: `GET /go/{deal_id}` → 302
- Feed: `GET /api/v1/deals/feed` with geo + ranking
- Value calculator: `GET /api/v1/deals/{deal_id}/value-calculator`

### Frontend highlights

- Routes: `app/[country]/`, city pages, deal detail, `/go/[deal_id]`
- Merchant dashboard under `(dashboard)/dashboard/` with Stripe Checkout + Billing Portal
- Global feed ranking in `lib/priority.ts`; AdSense in-feed after every 5th deal
- Root page geo-IP banner via `x-vercel-ip-country` / Cloudflare headers

## When invoked

1. Prefer `backend/` and `frontend/` for new work; only touch Django when explicitly maintaining legacy.
2. Keep secrets out of commits; never commit `.env` or credentials.
3. For submodule commits: change files in `PRO4-Mealdeals/`, commit inside that repo when appropriate, then update the submodule pointer in the parent justin-bot repo.
4. Docker: `backend/` uses `docker compose up --build` (PostGIS, Redis, API, Celery).

Always follow the `agents-in-sidebar` skill: agents stay in `.cursor/agents/` and get committed to git.
