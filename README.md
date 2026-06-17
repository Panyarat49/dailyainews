# dailyainews

Two Claude Code skills that produce **two Thai-language AI news briefs each day** — a general
AI/tech brief and a company-watchlist brief — commit them to this repo, and email each **full
brief** to the configured recipients.

The entire flow is executable from inside Claude — **no shell, no git CLI, no cron on your laptop**. The intended host is [Claude Web Routine](https://claude.ai), so it survives your machine being asleep.

```
05:57 Asia/Bangkok  ──▶  pboat-data.yml (GitHub Actions, pure Python — no API key)
                         RSS funnel: pboat_universe.py
                         fetch RSS + Google News → keyword-filter → dedup → score
                         → commits .github/scripts/output/universe_{DATE}_ainews.json
                                                  + universe_{DATE}_watchlist.json   [skip email]
                                                        │
                                                        │  pre-screened candidate pool waits in the repo
                                                        ▼
07:00 Asia/Bangkok  ──▶  Claude Routine fires
                         engine Step 0.5: reads today's universe JSON as START_POOL
                            ├─ JSON fresh (≤4h)  → skip WebSearch, WebFetch-verify the pool
                            └─ JSON missing/stale → fall back to WebSearch (original flow)
                                                        │
                                                        ▼
                                  draft → 3 perspectives → rewrite
                                  (TWO briefs: daily-ai-news + daily-ai-watchlist)
                                                        │
                                                        ▼
                                  commits the briefs to a claude/* branch:
                                  articles/YYYY-MM-DD-ainews.md + …-watchlist.md
                                                        │
                                                        ▼
                         promote-brief.yml  copies the briefs to main using PROMOTE_PAT
                         (a real-credential push — this is what makes the email fire)
                                                        │  push to main
                                                        ▼
                                       GitHub Actions (.github/workflows/email-notify.yml)
                                                        │
                                                        ▼
                                  send_email.py renders the FULL brief → HTML
                                  → SMTP send via Gmail (smtp.gmail.com:587)
                                  (using repo secrets MAIL_USERNAME / MAIL_PASSWORD / MAIL_TO)
```

> **The RSS funnel is a speed/breadth upgrade, not a dependency.** It pre-gathers a wide
> candidate pool so Claude sources from more outlets and spends less time searching. If it
> doesn't run (weekend, outage, first day), the Routine silently falls back to its original
> WebSearch flow — every freshness/dedup/verification gate still applies either way. Full
> change history: [`DEVLOG.md`](./DEVLOG.md).

**Why email dispatch lives in GitHub Actions, not the skill:** Claude Web Routine's `WebFetch` tool accepts only `(url, prompt)` — it cannot open an authenticated SMTP connection. Rather than fight a tool-schema limit, we moved delivery to Actions, which has a real Python runtime and real secrets. Email also has no 5000-char limit (the reason we moved off LINE), so the **complete** brief is delivered with no truncation.

## Repo layout

```
.
├── .claude/
│   └── skills/
│       ├── shared/
│       │   ├── engine.md               # shared mechanics — incl. Step 0.5 (RSS pre-load)
│       │   ├── trusted-sources.md      # publisher allow-list (read-only, both skills)
│       │   └── defaults.json           # repo identity + tuning knobs
│       ├── daily-ai-news/              # GENERAL brief → articles/{DATE}-ainews.md
│       │   ├── SKILL.md
│       │   └── reference/              # sources.md + perspectives.md (overwritten each run)
│       └── daily-ai-watchlist/         # WATCHLIST brief → articles/{DATE}-watchlist.md
│           ├── SKILL.md
│           └── reference/              # watchlist.json + sources.md + perspectives.md
├── .github/
│   ├── workflows/
│   │   ├── pboat-data.yml              # NEW — 05:57 BKK RSS funnel → universe JSON
│   │   ├── email-notify.yml            # fires on new brief → emails it
│   │   ├── promote-brief.yml           # copies briefs claude/* → main
│   │   └── daily-brief.yml             # cloud backup (gap-fill if Routine misses)
│   └── scripts/
│       ├── pboat_universe.py           # NEW — RSS funnel: fetch → filter → score → JSON
│       ├── send_email.py               # renders brief → HTML, sends via SMTP
│       └── output/                     # NEW — universe_{DATE}_{stream}.json land here
├── articles/                           # committed briefs: YYYY-MM-DD-{ainews,watchlist}.md
├── DEVLOG.md                           # NEW — change history (start here for the RSS upgrade)
├── LOCAL-ROUTINE.md                    # how the alternate local-machine host runs the skills
├── .env.example
├── .gitignore
└── README.md
```

## RSS pre-screening — the universe funnel (new)

Previously Claude discovered stories by running web searches one at a time, site by site.
The funnel front-loads that work in plain Python so Claude starts from a wide, already-filtered pool.

**What runs:** [`.github/scripts/pboat_universe.py`](./.github/scripts/pboat_universe.py),
driven daily by [`.github/workflows/pboat-data.yml`](./.github/workflows/pboat-data.yml) at
**05:57 Asia/Bangkok** — ~1 hour before the Routine.

**What it does, in five steps:**

1. **Fetch** — pulls ~14 direct RSS feeds (TechCrunch, The Verge, Blognone, Techsauce, …)
   plus Google News RSS searches (AI/tech, Thai, and one query per Tier-1 watchlist company).
2. **Keyword filter** — keeps only items matching AI/tech keywords (for the `ainews` stream) or a
   watchlist company's keywords (for the `watchlist` stream); drops sports/crime/entertainment noise.
3. **Dedup** — removes the same story arriving from multiple feeds (URL-normalised).
4. **Trusted-source filter** — drops any item whose real publisher isn't on
   [`trusted-sources.md`](./.claude/skills/shared/trusted-sources.md), so the pool only contains
   citeable outlets (Reuters, AP, TechCrunch, Blognone, the company blogs, …). Each item's real
   publisher is recovered from the feed's `<source>` element — so Google News redirect URLs resolve
   to the true domain. *(Run with `--all-sources` to keep off-allowlist items, tagged `on_allowlist:false`,
   for wider discovery.)*
5. **Score** — ranks each survivor by recency + how many keywords it hit.
6. **Write** — commits the top ~40 per stream to
   `.github/scripts/output/universe_{DATE}_ainews.json` and `…_watchlist.json`,
   with `[skip email]` so no email fires.

**How Claude uses it:** engine **Step 0.5** checks for today's JSON. If it's there and fresh
(≤ 4 h old), Claude loads it as the starting candidate pool and skips most web searches —
then **still WebFetch-verifies every story** (headline + publish timestamp) before writing.
The JSON is a *pre-screen*, never a trust bypass: Gate A (freshness ≤ 24 h), Gate B (7-day dedup),
the **trusted-source allowlist**, and Tier-1 verification all still run on every story.

**Two streams, two keyword sets:**

| Stream | Output file | Keywords come from |
|---|---|---|
| `ainews` (general) | `universe_{DATE}_ainews.json` | `AI_KEYWORDS` in `pboat_universe.py` (AI/tech terms, EN + Thai + CN) |
| `watchlist` (companies) | `universe_{DATE}_watchlist.json` | every `keywords` / `cn_terms` in [`watchlist.json`](./.claude/skills/daily-ai-watchlist/reference/watchlist.json) |

**Common tweaks** (all in `pboat_universe.py` unless noted):

- **Add an RSS feed** → append to `DIRECT_FEEDS`.
- **Add a search query** → append to `GNEWS_AI_QUERIES` or `GNEWS_TH_QUERIES`.
- **Change which companies are tracked** → edit `watchlist.json` only (the funnel reads it automatically).
- **Allow/deny a publisher** → edit `trusted-sources.md` — the funnel's trusted-source filter reads it live.
- **Include off-allowlist publishers** (wider discovery) → run the funnel with `--all-sources`; items are
  kept and tagged `on_allowlist: false`, and Claude treats those as discovery-only.
- **Change the run time** → edit the `cron` in `pboat-data.yml`. Keep it ≥ 1 h before the Routine and
  avoid UTC minute `:00` (top-of-hour queue congestion); note 06:00 BKK = 23:00 UTC is itself a busy slot.
- **Turn the pre-screen off for a run** → delete/rename the JSON before the Routine; it falls back to WebSearch.

> **Run it locally to preview the JSON** (no secrets needed):
> ```bash
> python3 .github/scripts/pboat_universe.py --stream both --hours 24
> # → writes .github/scripts/output/universe_<today>_{ainews,watchlist}.json
> ```

## What the skills do, in short

There are **two skills** sharing one engine ([`shared/engine.md`](./.claude/skills/shared/engine.md)):
`daily-ai-news` (general AI/tech) and `daily-ai-watchlist` (the company watchlist). Each run, per skill:

1. **Preflight.** Read the shared config + the publisher allow-list ([`shared/trusted-sources.md`](./.claude/skills/shared/trusted-sources.md)); the watchlist skill also loads [`watchlist.json`](./.claude/skills/daily-ai-watchlist/reference/watchlist.json).
2. **Pre-load (Step 0.5).** If today's RSS `universe_{DATE}_{stream}.json` is present and fresh, use it as the candidate pool (see [RSS pre-screening](#rss-pre-screening--the-universe-funnel-new) above); otherwise fall back to `WebSearch`.
3. **Research.** Gather 4–5 in-window stories, then `WebFetch`-verify each (Tier-1: confirm headline + publish timestamp). Write the per-run `reference/sources.md`.
4. **Three perspectives.** Each story gets a short reaction from a university professor, an AI specialist, and a professional programmer → `reference/perspectives.md`.
5. **Rewrite.** Weave the three angles into each story as prose; append an **Action items** section.
6. **Write the brief (write-only).** The skill writes one Markdown file — `articles/{DATE}-ainews.md` or `articles/{DATE}-watchlist.md` — and stops. It does **not** commit or email. The host runner commits + pushes; the push to `main` triggers the email workflow. The skill itself sends nothing.

Full mechanics: [`shared/engine.md`](./.claude/skills/shared/engine.md). Per-skill scope/selection lives in each skill's `SKILL.md`.

## Hosts — who runs the skills, and how a brief reaches `main`

The skills are write-only, so a **host** runs them and lands the result on `main`. The **live host
today is the Claude Web Routine**; the others are backups. The one rule that governs all of them:

> **`email-notify.yml` only fires when a brief is pushed to `main` with *real* credentials.**
> A push made by a workflow's built-in `GITHUB_TOKEN` does **not** trigger it (GitHub's recursion
> guard). Every host is designed around that rule.

| Host | When | How the brief reaches `main` | Why the email fires |
|---|---|---|---|
| **Claude Web Routine** — *live* | ~07:00 BKK | writes briefs → commits to a `claude/*` branch → [`promote-brief.yml`](./.github/workflows/promote-brief.yml) copies them to `main` using `PROMOTE_PAT` | the promote push uses a **real PAT** → triggers `email-notify.yml` |
| **Local desktop task** — *alternate* | ~07:1x BKK | runs the skills and pushes straight to `main` with stored git credentials (see [`LOCAL-ROUTINE.md`](./LOCAL-ROUTINE.md)) | a **real-credential** push triggers it |
| **GitHub Actions backup** — [`daily-brief.yml`](./.github/workflows/daily-brief.yml) | 13:49 BKK | only if the day's briefs are missing — generates + commits with `GITHUB_TOKEN` | that push *can't* trigger email-notify, so this job **emails itself** directly |

**Takeaway:** the `claude/*` branch + `promote-brief.yml` step is not cruft — it's the piece that makes
the Web Routine's email fire. Don't remove it unless the host starts pushing to `main` with a real PAT.
Required secret for this path: **`PROMOTE_PAT`** (a fine-grained PAT with `contents: write` on this repo).

## Email delivery (how it works)

Email is **unchanged by the RSS upgrade** — it runs exactly as before. Delivery lives in GitHub
Actions, not in Claude, because Claude's `WebFetch` tool can't open an authenticated SMTP connection.

**Trigger → send, step by step:**

1. A brief lands on `main` — `articles/{DATE}-ainews.md` and/or `articles/{DATE}-watchlist.md` change.
2. [`email-notify.yml`](./.github/workflows/email-notify.yml) fires on that push (it watches exactly those two path globs). Data-only commits use `[skip email]`, so the RSS funnel's `universe_*.json` commits never trigger it.
3. The workflow resolves which brief file(s) changed and loops [`send_email.py`](./.github/scripts/send_email.py) over each one.
4. `send_email.py` renders the brief Markdown → styled, Thai-friendly **HTML** (plus a plain-text fallback), using the brief's H1 (`# …`) as the email subject, and appends a commit-pinned GitHub permalink.
5. It sends over **SMTP via Gmail** (`smtp.gmail.com:587`, STARTTLS) to every address in `MAIL_TO`.

**Each day = two emails** (one per brief), with distinct H1 subjects so they're easy to tell apart in an inbox.

**Secrets** (set in **Repo → Settings → Secrets and variables → Actions** — these are the same as before, nothing new to add):

| Secret | Required | Default if unset |
|---|---|---|
| `MAIL_USERNAME` | yes | — (sending account + default From) |
| `MAIL_PASSWORD` | yes | — (Gmail **app password**, not the login password) |
| `MAIL_TO` | yes | — (comma-separate for multiple recipients) |
| `MAIL_FROM` | no | falls back to `MAIL_USERNAME` |
| `MAIL_HOST` | no | `smtp.gmail.com` |
| `MAIL_PORT` | no | `587` |

If `MAIL_USERNAME` / `MAIL_PASSWORD` / `MAIL_TO` aren't all set, the workflow **warns and exits cleanly** — the brief still commits, it just isn't emailed. (See [Diagnosing email issues](#diagnosing-email-issues) below to test or replay a send.)

## Guardrails (enforced in SKILL.md)

- **Routine-compatible only.** No `Bash`, no shell, no `git` CLI, ever. If the tool isn't on the allow-list in the skill, don't use it.
- **GitHub connector missing → abort.** The skill refuses to run without commit capability and logs why.
- **Mail secrets missing → skip cleanly.** The workflow emits a warning and exits 0; the commit still lands, just no email goes out.
- **SMTP send fails → loud failure.** The workflow step exits non-zero so the run is marked failed in the Actions tab; no retry.
- **No fabricated URLs.** Every cited URL is either fetched (Tier 1) or present in a live `WebSearch` result for a trusted-source domain (Tier 2). A URL never appears unless a search engine also returned it.
- **Verification mode is visible.** Commit messages include `[verify=webfetch]` or `[verify=search]`; when the whole runtime is egress-blocked (`WEBFETCH_BLOCKED`), the article itself carries a banner.
- **Idempotent.** Re-runs on the same day don't duplicate: identical content is a NO-OP, different content updates via SHA.
- **Timezone is `Asia/Bangkok`** everywhere the date is computed.

## Running in Claude Web Routine

### 1. Push this repo to GitHub

You are reading the finished repo. If you're setting up your own fork, make sure `articles/` exists and `.claude/skills/` (both skills + `shared/`) is committed to the default branch — that's where Claude will look for skills when it opens the repo.

### 2. Connect the GitHub MCP connector

In Claude (web): **Settings → Connectors → GitHub → Connect**, then authorize access to the repo you want the brief committed into. The connector exposes the file tools the Routine uses to read this repo and land the committed briefs.

Without this connector, Step 0 of the skill aborts on purpose.

### 3. Set environment — two surfaces, two purposes

**A. Routine config (for the skill that writes the brief):**

The skill only needs three GitHub-identity vars. It reads them in this order:

1. Inline in the invocation prompt (e.g. `GITHUB_OWNER = Panyarat49`).
2. [`shared/defaults.json`](./.claude/skills/shared/defaults.json) — committed fallback.

| Var | Example | Required | Where |
|---|---|---|---|
| `GITHUB_OWNER` | `Panyarat49` | yes | prompt or `defaults.json` |
| `GITHUB_REPO` | `dailyainews` | yes | prompt or `defaults.json` |
| `GITHUB_BRANCH` | `main` | no (default `main`) | prompt or `defaults.json` |

Cloud Environment on the Routine is **not required** — `defaults.json` covers the fallback. In this deployment we observed Cloud Environment does not inject values into the model's prompt context, so we don't depend on it.

**B. GitHub repo secrets (for the Actions workflow that sends the email):**

| Secret | Example | Where to set |
|---|---|---|
| `MAIL_USERNAME` | `you@gmail.com` (the sending account / default From) | **Repo → Settings → Secrets and variables → Actions → New repository secret** |
| `MAIL_PASSWORD` | app password for that account (not the normal login password) | same place |
| `MAIL_TO` | `recipient@example.com` (comma-separate for several) | same place |
| `MAIL_FROM` | optional — defaults to `MAIL_USERNAME` | same place |
| `MAIL_HOST` | optional — defaults to `smtp.gmail.com`; use `smtp-mail.outlook.com` (personal Outlook) or `smtp.office365.com` (M365 business) | same place |
| `MAIL_PORT` | optional — defaults to `587` (STARTTLS) | same place |

The workflow at [`.github/workflows/email-notify.yml`](./.github/workflows/email-notify.yml) reads these directly. If `MAIL_USERNAME` / `MAIL_PASSWORD` / `MAIL_TO` aren't all set, the workflow emits a warning and exits cleanly — commits still land, just no email.

> **App password note:** `MAIL_PASSWORD` must be an **app password**, not the account's normal login password. For Gmail, enable 2-Step Verification, then create an app password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords). (Outlook personal accounts now largely reject basic-auth SMTP, which is why Gmail is the default.)

See [`.env.example`](./.env.example) for inline notes on each var.

### 4. Create the Routine

1. In Claude web, go to **Routines → New Routine**.
2. Attach this repo (the GitHub connector must already be authorized for it).
3. Set the schedule — **every day at ~07:00 Asia/Bangkok**, after the 05:57 RSS funnel has committed today's `universe_*.json` (so Step 0.5 can use it).
4. Paste the prompt (runs **both** briefs):
   > Run the `daily-ai-news` skill. Today is the scheduled daily brief. Then run the `daily-ai-watchlist` skill.
5. Save. The first run is the best sanity check.

### 5. What you get

Each day produces:

- **Two new briefs on `main`:** `articles/YYYY-MM-DD-ainews.md` (general) and `articles/YYYY-MM-DD-watchlist.md` (watchlist), each committed `brief: {DATE} [kind=…] [verify=webfetch|search]`.
- Regenerated per-skill working artifacts (`reference/sources.md`, `reference/perspectives.md`).
- **Two emails** — one per brief — each the **full brief** rendered as HTML, with a permalink pinned to that commit's SHA (so the link never drifts if history is rewritten).

## Running it interactively in Claude Code

You can also invoke either skill from a local Claude Code session — same flow, same guardrails. The same GitHub connector and env vars are required. Open this repo in Claude Code and ask:

> run the daily-ai-news skill

(or `run the daily-ai-watchlist skill`). Claude will load that skill's [`SKILL.md`](./.claude/skills/daily-ai-news/SKILL.md), follow [`shared/engine.md`](./.claude/skills/shared/engine.md), and execute the steps.

## Diagnosing email issues

Email delivery happens in GitHub Actions, not in Claude, so diagnose it there:

```bash
# Manually re-email an existing brief (replace ainews with watchlist as needed)
gh workflow run email-notify.yml -f file=articles/<YYYY-MM-DD>-ainews.md
# With no -f input, a manual run emails BOTH of today's briefs.

# Watch / inspect
gh run list --workflow=email-notify.yml --limit 5
gh run view <run-id> --log
```

The "Send email" step prints the SMTP host it connected to and the final subject/recipients on success. To preview the rendered HTML locally without sending:

```bash
pip install markdown
python3 .github/scripts/send_email.py articles/<YYYY-MM-DD>-ainews.md "https://example/permalink" --dry-run > preview.html
```

## Troubleshooting

- **"GitHub connector is not connected" on every run.** The connector authorization expired or was scoped to a different repo. Reconnect in **Settings → Connectors** and re-authorize for this repo.
- **Commit lands but no email.** Email is dispatched by `.github/workflows/email-notify.yml` — check the Actions tab of the repo, not the Routine log. If the workflow didn't even fire, the push may have been a NO-OP (skill detected identical content and skipped the commit — intentional).
- **SMTP login fails (`535` / `Authentication unsuccessful`).** `MAIL_PASSWORD` isn't a valid app password, or basic-auth SMTP is disabled for that account. For Gmail: confirm 2-Step Verification is on and regenerate the app password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
- **Workflow ran but the step failed.** Open the run log — the Python sender prints the host/port and the failing exception. Common causes: wrong password, SMTP AUTH disabled, recipient rejected.
- **Every WebFetch returns 403 from a single Routine run.** May be a transient tool issue; the skill auto-falls-back to `WEBFETCH_BLOCKED` (Tier 2 — WebSearch snippets), commits with `[verify=search]`, and the article carries a banner saying so. If it's persistent across many runs, the fix is at the Routine platform level (egress policy / `WebFetch` schema), not the skill.
- **`WebFetch` tool signature is `(url, prompt)` only — can't open SMTP.** Not a bug. That's the tool shape in Claude Web Routine. Anything requiring an authenticated network connection (like email) must live outside the Routine — see the GH Actions workflow.
- **"No verifiable stories" in sources.md.** Means the candidate pool (RSS funnel and/or `WebSearch`) returned zero usable items from trusted-source domains. Genuinely quiet news day or search quota issue. Re-run later; don't loosen [`shared/trusted-sources.md`](./.claude/skills/shared/trusted-sources.md) just to fill the quota.
- **The brief repeats yesterday's stories.** Check `Published:` in that skill's `reference/sources.md`. Tier-2 stories derive the date from the search snippet, which can be stale on slow news days.

## License

No license chosen yet. Treat as all-rights-reserved until a `LICENSE` file lands.
