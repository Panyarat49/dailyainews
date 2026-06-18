# Daily-brief ENGINE (shared contract)

**Single source of truth for the mechanics shared by both brief skills**
(`daily-ai-news` = general, `daily-ai-watchlist` = watchlist). Each skill's
`SKILL.md` is **thin**: it defines only its *scope, search strategy, extra gates,
selection rule, heading format, and output path*, then says "follow this engine."

> **Editability rule:** mechanics that are common to both briefs live HERE and
> nowhere else. To re-tune freshness, dedup, verification, personas, length, or
> output handling, edit THIS file once — both briefs inherit it. Per-skill
> specifics live in that skill's `SKILL.md`. Where they conflict, **`SKILL.md`
> wins for scope/selection/heading/paths; the engine wins for everything else.**

The skill that loaded this engine supplies these **bindings** (named in its SKILL.md):

| Binding | Meaning | Example |
|---|---|---|
| `BRIEF_KIND` | short id for this workstream | `ainews` / `watchlist` |
| `OUTPUT_PATH` | the one committed file | `articles/{TODAY}-ainews.md` |
| `DEDUP_GLOB` | prior briefs to dedup against (THIS stream only) | `articles/*-ainews.md` |
| `SCOPE` | what stories qualify | see SKILL.md |
| `SEARCH_STRATEGY` | how candidates are gathered | see SKILL.md |
| `EXTRA_GATES` | gates beyond A/B (may be none) | watchlist adds C, D, membership |
| `SELECTION` | how the final set is chosen | see SKILL.md |
| `HEADING_FORMAT` | the `### N.` story-heading shape | see SKILL.md |
| `ARTIFACT_DIR` | where sources.md / perspectives.md go | `.claude/skills/<this-skill>/reference/` |

---

## Runtime contract

- **Timezone:** Asia/Bangkok. Compute all dates/times in this TZ.
- **Host:** runs headless on a local machine (Task Scheduler) via `claude -p`, where
  **WebFetch is NOT egress-blocked** → prefer full Tier-1 verification. (It may also
  run in other hosts; the skill never assumes one.)
- **This skill is WRITE-ONLY.** It produces files and stops. It does **not** commit,
  push, POST, or send email. The **host runner** commits the output and the
  **email sender** (separate, teammate-owned) delivers it. Do not call git or any
  network-send tool. Reading the web (WebSearch/WebFetch) and reading/writing local
  files is the whole job.
- **No fabrication:** every news item MUST have a real URL whose domain is on
  `.claude/skills/shared/trusted-sources.md`. If you cannot verify it (per the
  tiered rule below), drop it.

## Definitions & invariants (stated once, here)

- **NOW** — current instant, Asia/Bangkok (UTC+7).
- **WINDOW** — rolling freshness window `[NOW − freshness_window_days, NOW]` (default
  **7 days**, from `CONFIG.freshness_window_days`). "Within WINDOW" / "fresh" / "recent"
  everywhere means inside it. **Hard gate (Gate A).** (Widened from 24h → 7d so quiet or
  deduped days still fill 4–5 from the week's significant, not-yet-covered stories;
  freshest-first. To go back to strict daily, set `freshness_window_days: 1`.)
- **TODAY** — NOW's calendar date `YYYY-MM-DD`; used for `OUTPUT_PATH`, the article
  title, and the commit message the runner will write.
- **DEDUP_WINDOW** — the last `dedup_window_days` (default **7**) briefs matching
  `DEDUP_GLOB`. Dedup is **per-stream**: the general and watchlist briefs never
  dedup against each other.
- **STORY_COUNT** — count policy from `CONFIG.story_count` (`min` 3 / `prefer` 4 /
  `max` 5). Every brief should land at **`prefer`–`max` (4–5)** and **try hard never to
  go below `min` (3)**; never exceed `max`. You reach it by relaxing *significance*
  (include relevant-but-less-major in-window items), **never** by relaxing *freshness*
  (Gate A stays hard). See Step 1c. Runs daily but WINDOW = ~7 days; per-stream dedup
  (last `dedup_window_days` briefs) means every qualifying story is published once.
- **CONFIG** — `.claude/skills/shared/defaults.json` (repo owner/repo/branch +
  knobs). Read once, cache.

---

## Step 0 — Preflight

1. **Resolve config.** `Read` `.claude/skills/shared/defaults.json` exactly once;
   cache `GITHUB_OWNER`, `GITHUB_REPO`, `GITHUB_BRANCH`, and any knobs
   (`dedup_window_days`, `freshness_window_days`, `model`, …). Inline prompt values override the file (first hit wins).
   These are used only to form the PERMALINK in the final report — the runner does
   the actual commit. Do **not** invent values or treat `{{PLACEHOLDER}}` as real.
2. **Date.** Compute `TODAY` (Asia/Bangkok).
3. **Load the allow-list.** `Read` `.claude/skills/shared/trusted-sources.md`.
4. **Per-skill preflight** (e.g. the watchlist skill loads `watchlist.json` here —
   see its SKILL.md). If a required per-skill input is missing/unparseable → abort
   with a clear log.
5. **Print a resolution line** so failures are obvious:
   `Engine: BRIEF_KIND=<…> OUTPUT_PATH=<…> window=<N>d dedup=<N>d model=<CONFIG.model> owner/repo=<…/…> TODAY=<…>`.
   If `CONFIG.model` is missing, default to `claude-opus-4-8` (Opus 4.8 — the standard for this project; every run must use it).

---

## Step 0.5 — Universe pre-load (optional RSS acceleration)

Before running SEARCH_STRATEGY, check for a pre-built RSS candidate file produced by
the data pipeline (`pboat-data.yml` runs 05:57 Asia/Bangkok, ~1 h before this routine):

**Check:** `.github/scripts/output/universe_{TODAY}_{BRIEF_KIND}.json`

| Scenario | Action |
|---|---|
| File exists AND `generated_at` ≤ 4 h before NOW | **Use START_POOL.** Print: `Universe pre-load: N candidates from RSS funnel (generated_at: …)` |
| File absent OR stale (> 4 h old) | **Skip.** Print: `Universe pre-load: not found — falling back to WebSearch` then proceed to Step 1 normally |

Each candidate carries: `title`, `url`, `source` (real publisher domain), `publisher`,
`on_allowlist`, `age_h`, `keywords_matched`, `score`, **and — load-bearing when WebFetch
is blocked — `description` (the outlet's own RSS snippet, ≤300 chars), `published_raw`
(the feed's explicit publish timestamp), and `has_timestamp` (bool).** The funnel runs in
GitHub Actions, where egress is **open**, so those three fields are real first-party
evidence even on a run where *this* routine's own `WebFetch` is 403-blocked — that is what
makes a blocked run still publishable (see item 4 + Step 1b-ver "Tier 2 — funnel snippet").
The funnel **pre-filters to `trusted-sources.md` by default**, so candidates should already
be on the allowlist (`on_allowlist: true`) — but you re-check anyway (see gate 3 below);
never assume.

**When START_POOL is available:**
1. `Read` the JSON. Parse `candidates[]` into START_POOL.
2. Apply Gates A + B to each candidate immediately — drop stale (> 24 h), drop URLs already in `RECENT_URLS`.
3. **Trusted-source gate (unchanged, still mandatory).** A story may only be **cited** if its domain is on `trusted-sources.md`. The funnel pre-filters to the allowlist, but verify each `source` yourself; if `--all-sources` was used (or a domain slips through), an off-allowlist item is **discovery-only** — locate the same story on a trusted outlet and cite THAT, or drop it. Never cite a `news.google.com` redirect or any off-allowlist domain directly.
4. If START_POOL has **≥ 8 candidates** after gates → skip WebSearch calls (SEARCH_STRATEGY) and go to Step 1b-ver. Then **branch on the `WebFetch` probe**:
   - **`WEBFETCH_OK`** → `WebFetch` each surviving candidate for **Tier-1** (the body's own publish timestamp + headline). This is the target.
   - **`WEBFETCH_BLOCKED`** → **do NOT fall back to WebSearch** (in a blocked host it is usually unavailable too, and the funnel is better anyway). Verify each candidate at **Tier-2 directly from the funnel**: its `source` is an allowlist-matched real publisher, `published_raw` + `has_timestamp` give the in-WINDOW timestamp, and `description` is the citeable snippet — all first-party RSS evidence gathered in an unblocked runner. Summarize **only** from `description`; never invent beyond it. A blocked run is therefore still a real, citeable brief (Tier-2 from funnel), not a degraded stub. (See Step 1b-ver row "Tier 2 — funnel snippet".)
5. If START_POOL has **< 8 candidates** after gates → supplement with WebSearch per SEARCH_STRATEGY to fill gaps (when WebFetch — and thus often WebSearch — is blocked, ship the funnel-backed items you have rather than padding). Print: `START_POOL thin after gates (N items) — supplementing with WebSearch`.
6. All engine quality gates (Gate A freshness, Gate B dedup, **trusted-source allowlist**, Tier-1 WebFetch verify) still apply to every story regardless of whether it came from START_POOL or WebSearch. This step is a *source substitution*, not a quality bypass.

**This step is fully optional scaffolding.** If the JSON is absent (pipeline missed, first run, weekend manual trigger), Steps 1–6 proceed exactly as before. No error; no stub.

---

## Step 1 — Research (fresh, deduplicated, in-scope)

`SCOPE` (from SKILL.md) bounds *which stories qualify*. `trusted-sources.md` bounds
*which outlets*. Both apply.

### 1a. Load recent URLs (rolling dedup, per-stream)
Read the last `dedup_window_days` briefs matching `DEDUP_GLOB` from the local
working tree (use `Glob` then `Read` — the repo is checked out; do NOT use any
connector). For each found file, extract every URL via `\[[^\]]+\]\((https?://[^)]+)\)`
plus plain URLs into a set `RECENT_URLS`. Missing files (skipped/first runs) are
fine. Lowercase host for comparison; keep the full URL otherwise.
Print: `Recent URL count ({dedup_window_days}d): N`.

### 1b. Gather candidates
Run `SEARCH_STRATEGY` (from SKILL.md). For each candidate capture: URL, title,
publisher (domain vs trusted-sources), and the **search-result snippet verbatim**
— including any timestamp string ("3 hours ago", "วันนี้", "2026-06-05").

### 1b-ver. Verification — tiered (Tier-1 preferred)
Probe `WebFetch` once on a control URL (e.g. `https://example.com`) at the start.
Label the runtime `WEBFETCH_OK` (2xx) or `WEBFETCH_BLOCKED` (403 / network error).

| Tier | Requirements | Allowed when |
|---|---|---|
| **Tier 1 — Full fetch** | `WebFetch` 2xx; body confirms headline + explicit publish date within WINDOW | `WEBFETCH_OK` |
| **Tier 2 — Snippet (funnel ▸ or WebSearch)** | domain on trusted-sources; a substantive snippet carrying a timestamp resolvable to within WINDOW; summary paraphrases **only** that snippet. The snippet may come from the **RSS funnel** — a START_POOL candidate's `description` + `published_raw` (**preferred**: first-party, fetched in an unblocked runner, needs no egress from here) — **or** from a live WebSearch result. | always — and the **sole** non-Tier-1 path when `WEBFETCH_BLOCKED` (use the funnel snippet first) |
| **Drop** | can't satisfy a tier above | — |

**Tier 1 is the target.** Per selected story: confirm it's real & in-scope, find it
on a trusted outlet, `WebFetch` that URL, use the body's own publish timestamp.
Only if that fetch genuinely fails for *this* story, accept Tier 2 for it. Do not
pre-emptively default to Tier 2. The runner tags the commit `[verify=search]` only
when the whole run was forced to Tier 2 (`WEBFETCH_BLOCKED`); else `[verify=webfetch]`
— record which in `sources.md` so the runner can read it.

**Freshness date — prefer the body, then the funnel timestamp, then the slug.** Use the
body's explicit publish timestamp in any format (incl. Thai Buddhist-era พ.ศ. 2569 = 2026
CE, Chinese dates); normalize it. When no body is available (Tier 2), use the funnel
candidate's `published_raw` (the feed's own timestamp — authoritative) over the URL-slug
date; fall back to the slug only when neither exists.
**Never** cite a URL whose provenance you can't point to: it must appear **either** in the
RSS funnel's START_POOL (a `candidates[]` entry in `universe_*.json`) **or** in a live
WebSearch result, for a trusted-source domain. A funnel entry is sufficient provenance on
its own — it was fetched first-party from the outlet's feed.

### 1b-gates. Gates — apply ALL before selection (drop on any failure)
**Gate A — Rolling freshness (WINDOW; default 7 days; of the WRITE-UP).** The gate is on the **article's own
publish time** within WINDOW — when the *write-up* was published — within WINDOW (`วันนี้` / `Today` /
`N hours ago`, N ≤ 24 / explicit <24h date → pass). **The underlying event may be older:**
a freshly-published (≤24h) article reporting a genuine **new development / situation
update** on an older story PASSES — freshness is about when it was *reported*, not when the
situation began. What fails: an article whose **own publish time is >24h** (a stale
write-up), a verbatim rehash with no new development, or a date that's ambiguous/
not-surfaced → **drop, never guess**.
**Gate B — Not in `RECENT_URLS`.** URL-level dedup across the dedup window. Same URL =
drop. A different article (different URL) on an evolving story is fair game.
**`EXTRA_GATES`** — apply any additional gates this skill defines (see SKILL.md).

### 1b-hard. Gate A is a HARD gate — DO NOT bend it
Forbidden patterns from past runs:
- ❌ "Couldn't find enough from today, so I included older **write-ups**." → **NO.** Fill with relevant in-window items (Step 1c); never include an article whose own publish time is >24h.
- ❌ "Most-recent indexed stories are from 3–5 days ago." → **NO.** "Most recent on the index" ≠ "within 24h." Try other queries / sources, then fill / ship the stub.
- ❌ Including an item **whose own write-up is dated last week** (stale publish time) just because the topic resurfaced. → drop.
- ✅ ALLOWED: a **freshly-published (≤24h) update** on an older situation — Gate A is on the *write-up's* publish time, not the event's age. Test: *is the reporting new?* Genuine new development → keep; verbatim rehash or old article → drop.

Before writing `sources.md`, re-check every selected story against `NOW − 24h` once
more. Failures are dropped silently. **"Never older" governs *freshness* only** — you
still fill to `STORY_COUNT` (4–5, floor 3) with *relevant in-window* items per Step 1c;
what you must never do is reach **past** the window to pad. If, after genuine effort,
fewer than `min` (3) in-window items exist, ship what you have and flag the shortfall; if
0, write the stub. **Padding with stale/off-topic items erodes trust; filling with
relevant in-window items does not.**

### 1c. Selection — fill to STORY_COUNT (4–5, floor 3)
Run `SELECTION` (from SKILL.md) over the candidates that passed Gates A + B (+ EXTRA_GATES).
Land at **`prefer`–`max` (4–5)**; **try hard never below `min` (3)**.

Fill in this order:
1. Take the **significant** items first (rank by materiality / SKILL.md priority).
2. **Backfill to 4–5 with merely AI/tech-relevant in-window items** — real, fresh
   (within WINDOW), on a trusted source (and on-watchlist where applicable), just
   *less major*. Relaxing the **significance** bar to fill is expected and fine.
3. If still short of `min`, **search harder first** — more / different queries, more
   trusted outlets, Thai + CN angles, watchlist per-company gap-fill — before settling.

**Never** relax *freshness* to fill: do not reach past WINDOW, do not pad with stale,
duplicate, or off-topic items (Gate A is hard — see 1b-hard). Only a genuinely dead
WINDOW ships **< `min`** (note the shortfall in `sources.md`); **0** pass → one-line stub
(Step 1d / Step 5) naming the blocking gate. Never exceed `max`.

### 1d. Write `sources.md`
Overwrite `{ARTIFACT_DIR}/sources.md`. The per-story ledger is required so the runner
and an operator can audit the run:

```markdown
# Sources — {TODAY} ({BRIEF_KIND})

Generated: {TODAY} (Asia/Bangkok)
Runtime: {WEBFETCH_OK | WEBFETCH_BLOCKED}
Model: {CONFIG.model}
Freshness window: rolling {freshness_window_days}d (Asia/Bangkok)
Dedup against: last {N} {BRIEF_KIND} briefs ({M} URLs loaded)
{per-skill summary line — e.g. watchlist tiers used; general source mix}

## Selected stories
1. **{Headline}**
   - {per-skill identity line — general: Publisher; watchlist: Company · Ticker · Tier}
   - URL: {final URL}
   - Published: {explicit timestamp or relative phrase as it appeared}
   - FreshnessCheck: ✅ within last 24h via {evidence}
   - DedupCheck: ✅ URL not in last-{N}-day set
   - Verification: {Tier 1 — WebFetch | Tier 2 — funnel snippet | Tier 2 — WebSearch snippet}
   - Summary: {1–2 sentences, strictly from fetched body or snippet}
2. ...

## Dropped
- {URL} — Gate A (>24h): "..."
- {URL} — Gate B (dedup): "..."
- {URL} — {extra gate}: "..."
```

If 0 stories passed → skip Steps 2–4; write a minimal stub article (Step 5 still
writes the file) naming the blocking gate(s).

---

## Step 2 — Draft the article
First draft in memory. Structure:
```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}{ — per-skill title suffix, e.g. " (Watchlist)"}

> TL;DR
> - {bullet 1 — one sentence}
> - {bullet 2}
> - {bullet 3}

## ข่าวเด่น AI ล่าสุด

{HEADING_FORMAT for story 1}
{2–4 sentences. Every factual claim traces to that story's URL.}
```
Rules:
- The story heading uses this skill's `HEADING_FORMAT` exactly. The trailing
  ` — [{Publisher}]({URL})` link is **load-bearing** (the email sender parses it).
- Every story references its source URL ≥ once via an inline markdown link.
- Do **not** invent quotes, numbers, dates, or names beyond the Tier-1 body / Tier-2
  snippet.
- Thai-first prose; technical terms may stay in English.
- **Verification-mode visibility:** the article body carries **exactly one** short
  status blockquote directly under the H1 **only when the run is degraded**
  (`WEBFETCH_BLOCKED` / Tier-2-only). Word it to match where the Tier-2 evidence
  actually came from:
  - Verified from the **RSS funnel** snippets (START_POOL — the normal blocked-mode path):
    > _หมายเหตุ: รอบนี้ตรวจสอบข่าวจากฟีด RSS (snippet) ของสำนักข่าวต้นทาง เนื่องจาก WebFetch ถูกบล็อก_
  - Verified from **live WebSearch** snippets (no funnel available that day):
    > _หมายเหตุ: รอบนี้ตรวจสอบข่าวผ่าน WebSearch (snippet) เท่านั้น_

  When not degraded (Tier-1 `WebFetch`), include **no** such line. Verification detail
  otherwise lives only in `sources.md` and the commit tag — never multiple banners/footers.

## Step 3 — Three perspectives
For each selected story (and each update inside a roundup, if this skill has them),
write three personas to `{ARTIFACT_DIR}/perspectives.md` (overwrite):
```markdown
# Perspectives — {TODAY} ({BRIEF_KIND})

## 1. {Headline}
**อาจารย์ (มหาวิทยาลัย):** {1–2 sentences — pedagogical framing}
**ผู้เชี่ยวชาญด้าน AI:** {1–2 sentences — technical substance, caveats, what's new}
**โปรแกรมเมอร์มืออาชีพ:** {1–2 sentences — practical impact on engineering, tooling, cost}
```
Distinct voices. No filler.

## Step 4 — Rewrite (integrated) → the final body
Weave the three perspectives into each story (no "persona:" labels). Append an
**Action items** section. Save the final markdown as `ARTICLE_BODY`.
```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}{ — per-skill suffix}

> TL;DR
> - …(mirror the top 3)…

## ข่าวเด่น AI ล่าสุด
{stories, each in HEADING_FORMAT, reporting + integrated perspectives}

## Action items
- **สำหรับอาจารย์/นักเรียน:** {1 concrete action}
- **สำหรับผู้เชี่ยวชาญ AI:** {1 concrete action}
- **สำหรับโปรแกรมเมอร์:** {1 concrete action}

{per-skill footer if any — e.g. watchlist coverage line}

---
_Generated by the `{this skill}` skill on {TODAY} (Asia/Bangkok) · model {CONFIG.model}._
```
**Length budget:** ~80–160 Thai words per story (one reporting paragraph + one
integrated-perspective paragraph). Roundup sub-items ~50–90 words. TL;DR bullets one
line each. Keep the whole brief skimmable on a phone.

## Step 5 — Output (write-only; the host commits)
Write `ARTICLE_BODY` to `OUTPUT_PATH` with the `Write` tool. That is the deliverable.
Do **not** commit, push, or send anything. The runner detects the change, commits
`brief: {TOPIC} {TODAY} [kind={BRIEF_KIND}] [verify={webfetch|search}]`, pushes, and
the email sender delivers from the committed file. A run that produced an identical
file to what's already on disk is fine — the runner will no-op the commit.

## Step 6 — Final report
```
✅ Wrote {OUTPUT_PATH}  [kind={BRIEF_KIND}] [verify={…}]
   Coverage: {N} stories — {per-skill summary}.
   (Runner will commit + the email sender will deliver.)
```
Stub/empty-day variant: state which gate(s) blocked everything.

---

## Error-handling summary
| Condition | Action |
|---|---|
| Required per-skill input missing/unparseable | Abort before research. Log clearly. |
| `WEBFETCH_BLOCKED` (whole runtime) | Tier 2 for every story — **prefer the funnel snippet** (START_POOL `description` + `published_raw`) over WebSearch; note it in sources.md so the runner tags `[verify=search]`; add the matching degraded-mode blockquote (Step 2). A funnel-backed blocked run is a real brief, not a stub. |
| Story > 24h ago | DROP (Gate A). List in "Dropped". |
| Story URL in dedup set | DROP (Gate B). |
| An EXTRA_GATE fails | DROP per that skill's rule. |
| < target stories qualify | Ship fewer. Record the gate breakdown. |
| 0 stories qualify | Skip Steps 2–4. Write the stub (Step 5 still writes the file). |
| Date ambiguous / unparseable | DROP — never guess. |
| A prior brief unreadable | Continue with a smaller dedup set. Log it. |

## Files an engine-driven skill touches
- `{ARTIFACT_DIR}/sources.md` — overwritten each run (audit artifact + runner reads verify mode)
- `{ARTIFACT_DIR}/perspectives.md` — overwritten each run (working artifact)
- `OUTPUT_PATH` — the single committed output
- Read-only: `.claude/skills/shared/trusted-sources.md`, `.claude/skills/shared/defaults.json`, and any per-skill reference (e.g. `watchlist.json`).
