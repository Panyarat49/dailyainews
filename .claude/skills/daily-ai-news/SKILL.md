---
name: daily-ai-news
description: Generate a daily Thai-language AI/tech news brief that MONITORS a configured company watchlist (defined in `reference/watchlist.json`) across priority tiers. Surface up to 5 significant, AI/tech-relevant stories from the last 24 hours (rolling window, Asia/Bangkok), prioritizing Tier-1 companies and descending to Tier 2 only to top up to 5; deduplicate URLs against the last 7 days; enrich each story with three expert perspectives (professor / AI specialist / professional programmer); commit it to this repository via the GitHub connector; and deliver it by email. Use this when the user asks for a "daily AI news brief", a "สรุปข่าว AI วันนี้", triggers this skill by name, or when it runs on schedule via Claude Web Routine.
---

# Daily AI News Brief — Watchlist Edition

End-to-end routine that produces **one Markdown article per day** at `articles/YYYY-MM-DD-brief.md`, commits it via the GitHub connector, then emails it. Runs entirely inside Claude (Web / Routine) — **no shell, no git CLI, no Bash**.

This edition is **entity-driven**: instead of "any AI news," it monitors a configured universe of companies defined in `reference/watchlist.json`, split into **Tier 1 (primary)** and **Tier 2 (fallback)**. Each day it surfaces up to 5 **significant, AI/tech-relevant** stories — taking Tier 1 first and descending to Tier 2 only to top up to 5.

## Versioning

- **V1.5 (current):** significance is judged **qualitatively** from web sources (WebSearch/WebFetch). Tickers are not used for selection; company **keywords / cn_terms** drive the search.
- **V2 (gated on Bloomberg entitlement):** adds a **Tier-0 Bloomberg stream** (pre-verified, authoritatively-timestamped company news + market-data enrichment) and a **quantitative** significance leg (abnormal price move / volume / news-volume / sentiment). All V2 logic in this file is **inert** until `BLOOMBERG_ENABLED = true`.

## Runtime contract

- **Timezone:** Asia/Bangkok. Compute `YYYY-MM-DD` from this TZ.
- **Tools allowed:** `WebSearch`, `WebFetch`, `Read`, `Write`, `Edit`, and the configured GitHub MCP connector.
- **Tools FORBIDDEN:** `Bash`, any shell, any `git` CLI. If you catch yourself reaching for `Bash`, stop — this skill must run on Claude Remote Routine where shell is unavailable.
- **No fabrication:** every news item MUST have a real, fetched-or-searched URL from the trusted-source list in `reference/trusted-sources.md`. If you cannot verify a URL, drop the item.
- **Watchlist-bounded:** every selected story MUST be about a company in `reference/watchlist.json`. The watchlist governs *which companies*; `trusted-sources.md` governs *which outlets*. Both gates apply.
- **Significance-bounded:** only **significant, AI/tech-relevant** stories qualify (see Step 1b-bis). Never pad the count with routine or off-topic items.

## Definitions & invariants (single source of truth)

Defined once here. Every step refers to these by NAME and must NOT re-derive them inline. To re-tune the workflow later, change them here only.

- **NOW** — current instant in Asia/Bangkok (UTC+7). All dates/times are computed in this timezone.
- **WINDOW** — the rolling freshness window = `[NOW - 24h, NOW]`. "Within 24h" / "fresh" everywhere means inside WINDOW. This is a HARD gate (Gate A); research MUST come strictly from inside WINDOW.
- **TODAY** — NOW's calendar date (`YYYY-MM-DD`); used for the filename, commit message, and article title.
- **DEDUP_WINDOW** — the last `dedup_window_days` (default 7) briefs.
- **Scheduled run time** is owned by the HOST (Routine / GitHub cron / Task Scheduler), NOT this file — currently **07:15 Asia/Bangkok**. The skill is time-agnostic: it always evaluates against NOW, so changing the host schedule never requires editing the skill.

Longevity: this block is the ONLY place the 24h rule and timezone are stated in full. Downstream steps say "within WINDOW," never "now - 24h." One knob, not twelve — so the base always works and stays easy to adjust later.

## Required environment

The Routine needs very little env — email delivery moved out to GitHub Actions (Step 6). The skill reads:

| Var | Purpose | Required | Source |
|---|---|---|---|
| `GITHUB_OWNER` | GitHub account / org owning the target repo | yes | inline prompt, or `reference/defaults.json` fallback |
| `GITHUB_REPO` | Target repo name | yes | inline prompt, or `reference/defaults.json` fallback |
| `GITHUB_BRANCH` | Branch to commit on (default `main`) | no | inline prompt, or `reference/defaults.json` fallback |
| `BLOOMBERG_ENABLED` | Turn on the V2 Tier-0 Bloomberg stream | no (default `false`) | `reference/watchlist.json` `_meta`, or inline prompt |

The `MAIL_*` secrets (`MAIL_USERNAME` / `MAIL_PASSWORD` / `MAIL_TO`, etc.) are **not read by the skill** — they live in GitHub repo secrets and are consumed by `.github/workflows/email-notify.yml`.

### Env resolution order (apply per variable, first hit wins)

1. **Inline in the skill invocation prompt** (e.g. `GITHUB_OWNER = thannob`).
2. **`reference/defaults.json`** — read once with the `Read` tool (canonical fallback for the `GITHUB_*` vars).
3. **Missing** → hard abort.

Do **not** invent values, and do **not** treat placeholders like `{{GITHUB_OWNER}}` as real.

---

## Step 0 — Preflight (fail fast, log loudly)

1. **GitHub connector check.** Confirm the GitHub MCP connector is connected (tools like `create_or_update_file`, `push_files`, `get_file_contents`). If none are available:
   - Print: `ABORT: GitHub connector is not connected. Enable the GitHub MCP connector in Claude settings and re-run.`
   - **Stop immediately.** Do not research, do not write any files.
2. **Resolve env.** Walk the resolution order for each variable. `Read` `reference/defaults.json` exactly once and cache it.
3. **Load the watchlist.** `Read` `reference/watchlist.json`. Validate it parses and has `tiers.1` and `tiers.2`. Cache `WATCHLIST` and `_meta` (`target_story_count`, `roundup_update_cap`, `dedup_window_days`, `tier_descent`, `bloomberg_enabled`). **`watchlist.json` is the SINGLE SOURCE OF TRUTH** for the monitored universe (companies, tiers, tickers, keywords, cn_terms) AND its tuning knobs (`_meta`) — the skill reads these, never hardcodes them; to change the universe or any knob, edit `watchlist.json` only, no skill edit needed. If it is missing or unparseable → abort with a clear log.
4. **Print a resolution table** so failures are obvious:
   ```
   Env resolution:
     GITHUB_OWNER   = thannob       (source: defaults.json)
     GITHUB_REPO    = dailyainews   (source: defaults.json)
     GITHUB_BRANCH  = main          (source: defaults.json)
   Watchlist: 10 Tier-1, 10 Tier-2 companies (target 5 stories, dedup 7d). BLOOMBERG_ENABLED=false.
   ```
5. **GitHub gate.** If `GITHUB_OWNER` or `GITHUB_REPO` is missing → abort.
6. **Date.** Compute `TODAY = YYYY-MM-DD` in `Asia/Bangkok`. Use it for the filename, commit message, and article body.
7. **(V2, inert when `BLOOMBERG_ENABLED=false`)** Detect the Bloomberg Tier-0 candidate feed at `reference/bloomberg_candidates.json`; if fresh, mark `TIER0_AVAILABLE`. Skip entirely in V1.5.

---

## Step 1 — Research (watchlist-driven, last 24h, significant)

Open `reference/trusted-sources.md` (the outlet allow-list) and `WATCHLIST` (the company universe). Both bound selection.

### 1a. Load recent URLs (rolling N-day dedup)

Read the last `_meta.dedup_window_days` briefs (number set in watchlist.json; do not hardcode) — `articles/{TODAY−1}-brief.md` … `articles/{TODAY−7}-brief.md` — via the GitHub connector's `get_file_contents`. For each found file, extract every URL with `\[[^\]]+\]\((https?://[^)]+)\)` plus plain URLs. Build a set `RECENT_URLS`. Missing files (skipped days, first runs) are fine — just skip them. Lowercase host for comparison; keep the full URL otherwise.

Print: `Recent URL count (7d): N`.

> Change vs prior versions: dedup is now a **rolling 7-day** window, not yesterday-only. A story covered any time in the last week is a repeat.

### 1b-0. Search strategy — wide first, then narrow (coverage + efficiency)

Do NOT blindly run one search per company (20 searches/day is wasteful). Instead:

1. **Wide pass (~2-4 searches):** broad WebSearches for the day's significant AI/tech stories — e.g. `AI news today`, `AI chip / model launch today`, Thai `ข่าว AI วันนี้`, one CN `AI 新闻`. One day's big stories usually surface several watchlist names at once.
2. **Map** each surfaced story to a watchlist company via its `keywords` / `cn_terms`; discard anything off-watchlist.
3. **Gap-fill (targeted):** for each **Tier-1** company NOT yet covered by a candidate, run ONE keyword search. Skip companies already covered.
4. **Tier-2 descent:** only if Tier 1 still cannot reach `target_story_count` significant stories.

Budget guide: ~4 wide + up to ~6 gap-fill = **under 10 searches on a normal day**; Tier-2 days add a few more. Verification fetches (1b-ver) are separate — one per *selected* story, not per candidate.

### 1b. Gather candidates per company (Tier 1 first)

Iterate `WATCHLIST.tiers.1`. For each company, run `WebSearch` with rolling-24h queries built from its `keywords` (and `cn_terms` for Chinese-language coverage), e.g. `"Nvidia" OR "Blackwell" AI`, `site:techcrunch.com Nvidia`, `腾讯 混元`. Add a date hint when supported (`qdr:d`).

Capture for each candidate: URL, title, **company** (from the watchlist entry that matched), publisher (domain vs `trusted-sources.md`), and the **search-result snippet verbatim** — including any timestamp string ("3 hours ago", "วันนี้", "2026-06-05").

Only descend to `WATCHLIST.tiers.2` **if** Tier 1 will not yield `target_story_count` significant stories (see 1c). When you do, gather Tier-2 candidates the same way.

### 1b-ver. Verification — tiered (Tier 1 preferred; handles egress-blocked runtimes)

Probe `WebFetch` once on a control URL (e.g. `https://example.com`) at the start. Label the runtime `WEBFETCH_OK` (2xx) or `WEBFETCH_BLOCKED` (403 / network error — the default in Claude Web Routine today).

| Tier | Requirements | Allowed when |
|---|---|---|
| **Tier 0 — Bloomberg** *(V2, inert in V1.5)* | Item comes from `bloomberg_candidates.json`; pre-verified with an authoritative timestamp | `BLOOMBERG_ENABLED` and `TIER0_AVAILABLE` |
| **Tier 1 — Full fetch** | `WebFetch` returns 2xx; body confirms headline + an explicit publish date within 24h (Asia/Bangkok) | `WEBFETCH_OK` |
| **Tier 2 — Search snippet** | URL domain is on `trusted-sources.md`; `WebSearch` snippet is substantive AND carries a timestamp resolvable to within 24h; summary paraphrases **only** the snippet | always — and the **sole** option when `WEBFETCH_BLOCKED` |
| **Drop** | Can't satisfy a tier above | — |

**Tier 1 is the target; Tier 2 is a fallback, not the default.** Prefer real verification. Per-story flow:

1. **Headline** — you have a candidate (from the wide / gap-fill search in 1b-0).
2. **Confirm** — is it real, AI/tech-relevant, significant, and inside WINDOW?
3. **Find it on a trusted source** — locate the SAME story on a `trusted-sources.md` outlet and `WebFetch` that URL (Tier 1). Use the body's own publish timestamp.
4. **Fallback** — only if that fetch genuinely fails (egress-blocked or paywalled) *for this story*, accept Tier 2 (snippet) for it.

Probe first; do NOT pre-emptively default the run to Tier 2 just because past runs were blocked. Tag the commit `[verify=search]` **only when the whole run was forced to Tier 2** (`WEBFETCH_BLOCKED`); otherwise `[verify=webfetch]`.

**Freshness date — prefer the body, then the slug.** When you can read the article body (Tier 0/1), use its explicit publish timestamp **in any format** — including Thai Buddhist-era years (พ.ศ. 2569 = 2026 CE) and Chinese dates — and normalize it. Only fall back to the URL slug date when no body is available (Tier 2). Do not drop a story whose body clearly shows a <24h date merely because the date isn't in the URL.

**Never** cite a URL you could not at least see in a `WebSearch` result for a trusted-source domain.

### 1b-bis. Four gates — apply ALL before selection

Drop a candidate on any failure.

**Gate A — Rolling 24h freshness.** Publish time within `[now − 24h, now]` Asia/Bangkok. `วันนี้` / `Today` / `N hours ago` (N ≤ 24) / explicit <24h date → pass. Older, or ambiguous/not-surfaced → **drop, never guess**.

**Gate B — Not in `RECENT_URLS`.** URL-level dedup across the last 7 days. Same URL = drop. Different article on an evolving story (different URL) is fair game.

**Gate C — AI/tech relevance.** The story must be a genuine **AI or technology** development involving the company (model/product, compute/chips, cloud/AI infra, AI research, AI-driven business move, AI regulation). A non-AI corporate story (e.g. a generic Goldman earnings line with no AI angle) → drop. This keeps the brief's AI/tech identity even though some watchlist names are not AI-pure.

**Gate D — Significance (V1.5 qualitative checklist).** The story must match a **material** event type:
- model / product launch or major update
- M&A, strategic investment, or funding round
- major partnership, customer, or contract
- chips / compute / data-center capex or capacity
- earnings or guidance **with an AI angle**
- regulatory / legal / antitrust / export-control touching AI
- executive or org change in an AI unit
- security, safety, or major outage incident
- notable research / benchmark result

Explicitly **NOT significant** (drop): routine analyst rating or price-target changes, recycled rumor, opinion/listicles, minor feature tweaks, generic market commentary.

> V2 adds a quantitative corroboration leg here (Bloomberg abnormal move / news-volume / sentiment). Inert in V1.5.

### 1b-tris. Hard rules — DO NOT bend Gate A or Gate D

Gates A (24h) and D (significance) are **hard gates**, not guidelines. Forbidden patterns from past runs:

- ❌ "Couldn't find 5 from today, so I included older items." → **NO.** Ship fewer; never older.
- ❌ "Most-recent indexed stories are from 3–5 days ago." → **NO.** "Most recent on the index" ≠ "within 24h." Try other queries / companies / Thai-CN sources, then ship the stub.
- ❌ "Nothing truly significant in Tier 1, so I promoted a minor item to fill the slot." → **NO.** A minor item is not significant just because the slot is empty. Descend to Tier 2 (Step 1c) or ship fewer.
- ❌ Including an item dated "last quarter / last month" because it resurfaced today. → drop.

Before writing `sources.md`, re-check every selected story against `now − 24h` and the significance checklist one more time. Failures are dropped silently — no apology note, no inclusion-with-caveat. If 0 remain, write the stub and commit. **The empty-day signal is correct output; a padded brief erodes trust in every future run.**

### 1c. Selection — tiers, top-up, roundup (the core algorithm)

Let `TARGET = _meta.target_story_count` (value set in watchlist.json).

1. From **Tier 1** candidates that passed all four gates, group by company. Rank companies by significance (most material first). Select **one slot per company**, strongest first, up to `TARGET`.
2. **Top-up descent.** If fewer than `TARGET` slots are filled, take **Tier 2** candidates (gathered in 1b), apply the same four gates, and top up — strongest first, one slot per company — until you reach `TARGET` or run out of significant items. *(`tier_descent = "top-up-to-target"`.)*
3. **Roundup block.** If a selected company has **≥2** significant updates today, keep it as **one slot** but render it as a roundup (Step 4), capped at `roundup_update_cap` (default **3**) updates, strongest first.
4. If fewer than `TARGET` significant stories exist across both tiers, **ship what you have** (even 1). Never pad.
5. If **0** stories pass → write a one-line stub (Step 1d / Step 5a) explaining whether the shortfall was Gate A (no fresh news), Gate B (all already covered), Gate C (nothing AI/tech-relevant), or Gate D (nothing significant). The empty-day signal is information.

Record which tiers were used → `TIERS_USED` (`1`, or `1+2`).

### 1d. Write `reference/sources.md`

Overwrite with this template. The **significance ledger** and **tier-descent record** are required:

```markdown
# Sources — {TODAY}

Generated: {TODAY} (Asia/Bangkok)
Runtime: {WEBFETCH_OK | WEBFETCH_BLOCKED}
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: last {N} briefs ({M} URLs loaded)
Tiers used: {1 | 1+2}

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | ✅ | model launch (Rubin) | yes (slot 1) |
| Microsoft | 1 | ✅✅ | 2 items: MAI model + Azure deal | yes (roundup, slot 2) |
| Apple | 1 | ❌ | only routine analyst note | no |
| ... | | | | |

## Tier-descent record
Tier 1 yielded {X} significant stories; {"target met — Tier 2 not consulted" | "descended to Tier 2 for {Y} slots"}.

## Selected stories
1. **{Headline}**
   - Company: {Company}  ·  Ticker: {ticker}  ·  Tier: {1|2}
   - Publisher: {Publisher}
   - URL: {final URL}
   - Published: {explicit timestamp or relative phrase as it appeared}
   - FreshnessCheck: ✅ within last 24h via {evidence}
   - DedupCheck: ✅ URL not in last-7-day set
   - Relevance: ✅ AI/tech — {why}
   - Significance: ✅ {event type from Gate D}
   - Verification: {Tier 0 — Bloomberg | Tier 1 — WebFetch | Tier 2 — WebSearch snippet}
   - Summary: {1–2 sentences, strictly from fetched body or snippet}

2. ...

## Dropped
- {URL} — Gate A (>24h): "..."
- {URL} — Gate C (not AI/tech): "..."
- {URL} — Gate D (not significant): "routine analyst rating change"
```

If 0 stories passed → skip Steps 2–4, write a minimal stub (Step 5 still commits) naming which gate(s) blocked everything.

---

## Step 2 — Draft the article

Create the first draft in memory (don't commit yet). Structure:

```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}

> TL;DR
> - {bullet 1 — one sentence}
> - {bullet 2}
> - {bullet 3}

## ข่าวเด่น 24 ชั่วโมงที่ผ่านมา

### 1. {Company} ({TICKER} · Tier {n}) — {Headline} — [{Publisher}]({URL})
{2–4 sentences. Every factual claim traces to that URL.}

### 2. ...
```

Rules:
- Story heading format is fixed: `### N. {Company} ({TICKER} · Tier {n}) — {Headline} — [{Publisher}]({URL})`. The trailing ` — [{Publisher}]({URL})` must be present for single-story slots (keeps the source link visible in the rendered email).
- Every story references its source URL at least once via an inline markdown link.
- Do **not** invent quotes, numbers, dates, or names. If the source (Tier 1 body) or snippet (Tier 2) didn't say it, don't write it.
- Thai-first prose; technical terms can stay in English.
- **Verification-mode visibility (deterministic rule):** the article body carries **exactly one** short status line **only when the run is degraded** (`WEBFETCH_BLOCKED` / Tier-2-only). Place it as a single blockquote directly under the H1:
  > _หมายเหตุ: รอบนี้ตรวจสอบข่าวผ่าน WebSearch (snippet) เท่านั้น_

  When the run is **not** degraded (Tier 0/1 available), include **no** such line. Never add multiple banners, italic tags, or footers about sourcing. The commit `[verify=...]` tag and `sources.md` remain the full operator record.

---

## Step 3 — Three perspectives

For each selected story (and each update inside a roundup), produce a short reaction from **three personas**. Write them to `reference/perspectives.md` (overwrite):

```markdown
# Perspectives — {TODAY}

## 1. {Company} — {Headline}

**อาจารย์ (มหาวิทยาลัย):** {1–2 sentences — pedagogical framing}
**ผู้เชี่ยวชาญด้าน AI:** {1–2 sentences — technical substance, caveats, what's genuinely new}
**โปรแกรมเมอร์มืออาชีพ:** {1–2 sentences — practical impact on engineering, tooling, cost}

## 2. ...
```

Keep each persona's voice distinct. No filler.

---

## Step 4 — Rewrite (integrated)

Produce the **final article body** by weaving the three perspectives into each story. Append an **Action items** section and a **watchlist-coverage footer**.

Single-story slot:
```markdown
### 1. {Company} ({TICKER} · Tier {n}) — {Headline} — [{Publisher}]({URL})
{2–4 sentences of reporting, then a paragraph integrating the professor / AI-expert / programmer angles naturally. No "persona:" labels.}
```

Roundup slot (a company with ≥2 significant updates — still **one** of the 5 slots):
```markdown
### 2. {Company} ({TICKER} · Tier {n}) — อัปเดตสำคัญ {k} รายการ
**2.1 {Headline A} — [{Publisher}]({URL})**
{2–3 sentences + integrated perspectives}
**2.2 {Headline B} — [{Publisher}]({URL})**
{2–3 sentences + integrated perspectives}
```

*(V2, inert in V1.5: when `BLOOMBERG_ENABLED` and a ticker has data, you may append one market line per story, e.g. `หุ้น NVDA +3.2% วันนี้`.)*

Target full-file structure:
```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}

> TL;DR
> - {bullet 1}
> - {bullet 2}
> - {bullet 3}

## ข่าวเด่น 24 ชั่วโมงที่ผ่านมา

### 1. ...
### 2. ...

## Action items

- **สำหรับอาจารย์/นักเรียน:** {1 concrete action}
- **สำหรับผู้เชี่ยวชาญ AI:** {1 concrete action}
- **สำหรับโปรแกรมเมอร์:** {1 concrete action}

## การครอบคลุม watchlist
> คัดจาก Tier {1 | 1+2} · บริษัทที่มีข่าวสำคัญวันนี้: {list} · {"Tier 2 ไม่ถูกเรียกใช้" | "เติมจาก Tier 2: {list}"}

---
_Generated by the `daily-ai-news` skill on {TODAY} (Asia/Bangkok)._
```

**Length budget (per story):** ~**80-160 Thai words** — about one short reporting paragraph plus one integrated-perspective paragraph. Roundup sub-items: ~50-90 words each. TL;DR bullets: one line each. Keep the whole brief skimmable on a phone.

**Priority order (which stories lead):** rank by, in order — (1) **tier** (Tier 1 above Tier 2), (2) **significance** (M&A / launch / regulatory / earnings-with-AI-angle outrank incremental updates), (3) **breadth** (prefer distinct companies over stacking one). Story 1 is the day's single most material item; the TL;DR mirrors the top three.

Save the final markdown as `ARTICLE_BODY` for the commit step.

---

## Step 5 — Commit via GitHub connector

**Never use git CLI.** Use the connector tool (`create_or_update_file` with `owner`, `repo`, `path`, `branch`, `message`, `content`, optional `sha`; or `push_files`).

### 5a. Idempotency check

Call `get_file_contents` for `articles/{TODAY}-brief.md` on `branch`:
- **Not found.** Create it. Proceed.
- **Found, byte-for-byte identical to `ARTICLE_BODY`.** Skip the commit. Log `Run status: NO-OP (idempotent)`. Capture the existing SHA as `COMMIT_SHA` and still proceed to Step 6.
- **Found, content differs.** Update with the returned `sha` (a meaningful re-run).

### 5b. Commit

1. Set:
   - `path = articles/{TODAY}-brief.md`
   - `branch = GITHUB_BRANCH or "main"`
   - `message = "brief: {TOPIC} {TODAY} [tier={TIERS_USED}] [verify={webfetch|search}]"` — `{TOPIC}` ≤40 chars (dominant theme), `tier=` from `TIERS_USED`, `verify=` from the runtime label. *(V2 adds `[src=bbg|web]`.)*
   - `content = ARTICLE_BODY`
2. Call the create-or-update tool.
3. Capture the commit SHA (`commit.sha` or `sha`); else read it back via `get_file_contents`.
4. Form `PERMALINK = https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{COMMIT_SHA}/articles/{TODAY}-brief.md`. Pin to the SHA, never `/blob/main/...`.
5. If the commit fails: print the full error, do **not** retry, do **not** proceed to delivery.

> Note for operators: commit `sources.md` / `perspectives.md` **in the same commit** as the brief when the connector allows, so the brief is the HEAD of the push (the email workflow resolves the notify target from the pushed brief).

---

## Step 6 — Email delivery (handled externally)

**This skill does NOT send the email.** `WebFetch` in Claude Web Routine accepts only `(url, prompt)` — no method/headers/body — so it cannot open an authenticated SMTP connection.

Email dispatch is handled by `.github/workflows/email-notify.yml`, which triggers on pushes affecting `articles/*-brief.md`, renders the **full** brief to HTML via `.github/scripts/send_email.py`, and sends it over Office 365 SMTP. Email has no 5000-char limit, so the complete brief is delivered with no truncation.

What the skill does here:
1. Nothing that talks to the mail server directly.
2. Print: `Email: dispatched by .github/workflows/email-notify.yml (see Actions tab for delivery status)`.
3. A NO-OP commit (5a) means no push → the workflow does not fire. Correct.

To force a re-send: `gh workflow run email-notify.yml -f file=articles/{TODAY}-brief.md`.

---

## Step 7 — Final report

```
✅ Committed: articles/{TODAY}-brief.md @ {COMMIT_SHA_short}  [tier={TIERS_USED}] [verify={...}]
   {PERMALINK}
   Coverage: {N} stories — {company list}. Tier 2 {"not consulted" | "topped up {Y}"}.
Email: dispatched by .github/workflows/email-notify.yml (see Actions tab)
```

NO-OP variant:
```
Run status: NO-OP (idempotent) — today's brief already at {COMMIT_SHA_short}
   {PERMALINK}
Email: not re-sent (no new commit → workflow does not fire)
```

---

## Error-handling summary

| Condition | Action |
|---|---|
| GitHub connector missing | Abort before any work. Log clearly. |
| `watchlist.json` missing / unparseable | Abort. The universe is required. |
| `WEBFETCH_BLOCKED` (whole runtime) | Tier 2 (WebSearch snippet) for every story; commit `[verify=search]`; add the single degraded-mode note (Step 2). |
| Story > 24h ago | DROP (Gate A). List in "Dropped". |
| Story URL in last-7-day set | DROP (Gate B). |
| Story not AI/tech-relevant | DROP (Gate C). |
| Story not significant | DROP (Gate D) — never promote a minor item to fill a slot. |
| Tier 1 yields < target significant | Descend to Tier 2; top up to target (1c). |
| < target stories across both tiers | Ship fewer (1–4). Record the gate breakdown. |
| 0 stories across both tiers | Skip Steps 2–4. Write a one-line stub naming the blocking gate(s). |
| Company has ≥2 significant updates | One slot, render as roundup (cap `roundup_update_cap`). |
| Date ambiguous / unparseable | DROP — never guess. |
| Recent brief unreadable (404 / other) | Continue with a smaller dedup set. Log it. |
| GitHub commit fails | Surface the error. Stop. |
| Today's article identical | NO-OP. Email does not fire (intentional). |
| Email issues | Not this skill's concern — see `.github/workflows/email-notify.yml`. |

## Files this skill touches

- `reference/sources.md` — overwritten each run (working artifact; now includes the significance ledger)
- `reference/perspectives.md` — overwritten each run (working artifact)
- `articles/{TODAY}-brief.md` — the single committed output

Read-only for this skill: `reference/trusted-sources.md`, `reference/defaults.json`, `reference/watchlist.json`, and `reference/bloomberg_candidates.json` (V2 input, produced externally on the Bloomberg ingestion node).
