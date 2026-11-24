<!-- HEADER: swap the desc= text for variant A or B (see header-variants.md) -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=12355B&height=180&section=header&text=Augustine%20Chukwu&fontSize=48&fontAlignY=36&desc=Software%20engineer%20building%20for%20African%20businesses&descAlignY=60&descSize=18&fontColor=FAF6EF" width="100%" alt="Augustine Chukwu, software engineer" />

I'm Augustine (Austin), a software engineer in Enugu, Nigeria. I build backend systems and AI features for products where money, bookings or voice notes have to land correctly the first time: ledgers, payment webhooks, job queues and LLM pipelines with a human in the loop.

Co-founder and engineering lead at **[KekeVest](https://kekevest.com)**. Open to remote Software Engineer and AI Engineer roles (UTC+1, overlaps with Europe and US mornings).

[Website](https://chukwuaugust.tech) · [LinkedIn](https://www.linkedin.com/in/augustine-chukwu-/) · [Email](mailto:chukwuaugust0@gmail.com)

---

### What I've built

**[KekeVest](https://kekevest.com)** · *private repo* 
Fleet and rider-ownership platform for keke (tricycle) riders in Enugu: lease-to-own instead of informal "work-and-pay" hire purchase. Double-entry ledger, Paystack dedicated virtual accounts with a 90/10 split, dual-approval payouts and a live fleet map. I lead a team of 5 and own the domain model, contracts, ledger and rider portal (about 59% of 1,438 commits). 317 merged PRs, ~1,670 API tests, CI on every PR. 
`FastAPI` `PostgreSQL/PostGIS/TimescaleDB` `Celery` `Redis` `MQTT` `Next.js` `Playwright`

**[VoiceDesk](https://github.com/Austin-Deccentric/VoiceDesk)** · [live demo](https://voice-desk-two.vercel.app) 
Voice-note inbox for Nigerian small businesses: transcribe → translate → tag intent → draft a reply grounded in the business's knowledge base → a human approves before anything is sent. WhatsApp and Telegram channels, Postgres job queue (`SKIP LOCKED`), live updates over SSE. Built solo in 17 days; 183 pytest + 30 Playwright tests. 
`FastAPI` `Next.js` `PostgreSQL` `ElevenLabs Scribe` `OpenAI-compatible LLMs` `SSE`

**[NaijaStay](https://github.com/Austin-Deccentric/naijastay)** · [live API](https://naijastay-api.onrender.com) 
Hotel booking API that can't double-book a room: pessimistic row locking, Redis room holds, 4-role RBAC, SSE and rate limiting. About 87% of 111 commits on a team of 3; 101 tests. 
`FastAPI` `PostgreSQL` `Redis` `SQLAlchemy 2 (async)` `Docker`

**[Clinic booking app](https://clinic-app-mh31.onrender.com)** 
FastAPI + React app built to a published OpenAPI contract; passes all 5 levels with 72 contract tests.

---

### Stack

**Backend:** Python, FastAPI, SQLAlchemy 2 (async), SQLModel, Pydantic, PostgreSQL (PostGIS, TimescaleDB), Redis, Celery, Alembic, MQTT 
**AI:** speech-to-text, provider-agnostic LLM adapters, knowledge-base-grounded drafting with human approval, Nigerian-language voice pipelines 
**Frontend:** TypeScript, React 19, Next.js, Tailwind CSS, shadcn/ui, Astro 
**Infra & quality:** Docker, Linux, GitHub Actions, Render, Vercel, pytest (Hypothesis), Playwright, Ruff, mypy 
**Payments:** Paystack (virtual accounts, webhooks), Stripe

---

### What I care about

- Pipelines that are safe to retry: idempotent webhooks, resumable jobs, no double charges
- Concurrency done right: row locks and `SKIP LOCKED` queues instead of hoping
- AI that works in Nigerian languages, with a person still making the call

Outside work: football.

<!-- Optional: keep the contribution snake (the workflow already exists in .github) -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Austin-Deccentric/Austin-Deccentric/output/github-contribution-grid-snake-dark.svg" />
  <img alt="Contribution graph animation" src="https://raw.githubusercontent.com/Austin-Deccentric/Austin-Deccentric/output/github-contribution-grid-snake.svg" />
</picture>
