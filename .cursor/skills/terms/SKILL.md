---
name: terms
description: >-
  Creates or updates the Dine A Deal Terms and Conditions page at /terms,
  footer Terms link, venue registration acceptance checkbox, and Terms
  acceptance audit fields. Use when the user invokes /terms, asks for Terms
  and Conditions, T&Cs, legal terms page, or venue Terms acceptance.
disable-model-invocation: true
---

# /terms — Terms and Conditions

## Goal

Create or replace the **Terms and Conditions** page for Dine A Deal (or the
current MealDeals / dineadeal.com project) so merchants and consumers have a
permanent, accurate legal page at `/terms`, with registration acceptance and
acceptance logging for venues.

Prefer matching existing Privacy Notice / Cookie Policy page patterns in the
repo (`/privacy`, `/cookies`).

## When this skill applies

- User invokes `/terms`
- Asks for Terms and Conditions / T&Cs / legal terms page
- Venue registration Terms checkbox or acceptance storage
- Footer “Terms” link

## Implementation checklist

```
Terms progress:
- [ ] 1. Create or replace /terms page (full legal copy, no paraphrase)
- [ ] 2. SEO metadata + H1 title
- [ ] 3. Table of contents → numbered sections
- [ ] 4. Match site design system (header/footer/fonts/colours/responsive)
- [ ] 5. Footer permanent link labeled “Terms” → /terms
- [ ] 6. Link Privacy Notice → /privacy and Cookie Policy → /cookies in copy
- [ ] 7. Venue/business registration: required unticked Terms+Privacy checkbox
- [ ] 8. Keep marketing consent separate (optional, unticked) — never via Terms
- [ ] 9. Store venue Terms acceptance (id, version, datetime, source, user)
- [ ] 10. Resolve [PLACEHOLDERS] from config or leave visible placeholders
```

## Page requirements (FORCE)

1. **Route:** `/terms`
2. **H1:** `Dine A Deal Terms and Conditions`
3. **SEO**
   - Title: `Terms and Conditions | Dine A Deal`
   - Description: `Terms governing the use of Dine A Deal by consumers, venues, advertisers and business users.`
4. **TOC** linking to each numbered section (1–34).
5. **UX / a11y**
   - Responsive (mobile, tablet, desktop)
   - Keyboard accessible
   - Print-friendly
   - Reasonable max content width
   - Semantic HTML headings (`h1`/`h2`)
6. **Legal copy:** Do **not** paraphrase or shorten. Use the verbatim text in
   [reference.md](reference.md).
7. **Cross-links:** Wherever Privacy Notice or Cookie Policy are mentioned,
   link to `/privacy` and `/cookies`.
8. **Placeholders:** Replace `[SQUARE BRACKET PLACEHOLDERS]` from site config /
   env when known. If unknown, **keep the visible placeholder** (do not invent
   company numbers or addresses).

## Venue registration (FORCE)

On venue / business registration forms, include a **required**, **unticked**
checkbox:

> I have read and agree to the Dine A Deal Terms and Conditions and
> acknowledge the Privacy Notice.

With links to `/terms` and `/privacy`. Block submit until checked.

### Marketing must stay separate

Do **not** treat Terms acceptance as permission for:

- Newsletter marketing
- Third-party marketing
- Selling or sharing customer email addresses
- Promotional text messages

Marketing permission must use a **separate, optional, unticked** consent control.

## Store venue Terms acceptance

When a venue accepts the Terms, persist at least:

| Field | Example |
|-------|---------|
| Venue account ID | `merchant_id` |
| Terms version | `1.0` (from `TERMS_VERSION`) |
| Date and time | UTC timestamp |
| Acceptance source | e.g. `merchant_registration` |
| User accepting on behalf of the venue | email / user id / name |

Prefer DB fields on `merchants` or a `terms_acceptances` table + Alembic
migration. Wire create/register API + frontend payload.

## Config helper

Use or create `frontend/lib/legal-config.ts` (or equivalent) with:

- `TERMS_VERSION = "1.0"`
- Effective / last-updated dates (env or placeholders)
- Company name, number, addresses, support / complaints / reporting / billing
  emails, phone — from `NEXT_PUBLIC_*` / existing contact constants, else
  keep `[PLACEHOLDER]` strings

## Stack notes (Dine A Deal)

- Frontend: Next.js App Router under `frontend/app/terms/`
- Mirror structure of `frontend/app/privacy/` and cookies pages
- Footer: `frontend/components/landing/SiteFooter.tsx` — add **Terms**
- Backend: FastAPI merchant create/register path in MealDeals `backend/`

## Smoke-check

- [ ] `/terms` renders all 34 sections + TOC anchors work
- [ ] Footer **Terms** opens `/terms`
- [ ] Privacy / Cookie links work
- [ ] Registration blocked without Terms checkbox; succeeds when checked
- [ ] Marketing checkbox (if any) remains optional and separate
- [ ] Acceptance row/fields written for venue signup
- [ ] Print stylesheet / readable width OK on mobile

## Legal copy

Verbatim Terms text (sections 1–34) lives in [reference.md](reference.md).
Copy from there into the page — do not rewrite.
