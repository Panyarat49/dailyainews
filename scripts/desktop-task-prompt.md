# Desktop scheduled-task prompt — daily AI briefs

Paste this as the prompt when creating the Claude Desktop scheduled task (the PRIMARY
host — see LOCAL-ROUTINE.md). It is intentionally self-contained: each scheduled run is
a fresh local session with no memory of any prior chat. Runs locally → WebFetch is
unblocked → full Tier-1 verification.

---

You are a scheduled task running locally on this Windows machine via the Claude Desktop
app. No human is watching — work autonomously, never ask questions, never stop to confirm.

## Working repo
Operate in the local clone at `C:\Users\panya\dailyainews`.
First: change into it and run `git pull --ff-only` to get the latest. (If the folder
does not exist, `git clone https://github.com/Panyarat49/dailyainews.git` to that path.)

## Date
Compute `TODAY` = today's date in **Asia/Bangkok** (`YYYY-MM-DD`).

## Produce BOTH briefs (the skills are write-only — they must NOT commit)
For each skill: `Read` its `SKILL.md`, then `Read` and follow
`.claude/skills/shared/engine.md`, applying that skill's scope. WebFetch works here —
prefer Tier-1 (fetch the article body + its real publish date). Apply the 24h + dedup
(+ watchlist) gates strictly; ship fewer rather than older/padded; on an empty-news day
write the one-line stub (that is correct output, not a failure).

1. **General** — follow `.claude/skills/daily-ai-news/SKILL.md`
   → write `articles/{TODAY}-ainews.md` (+ that skill's `reference/sources.md` & `reference/perspectives.md`).
2. **Watchlist** — follow `.claude/skills/daily-ai-watchlist/SKILL.md`
   → write `articles/{TODAY}-watchlist.md` (+ that skill's `reference/sources.md` & `reference/perspectives.md`).

## Commit + push (this is what triggers email delivery)
After both are written, for EACH brief file that is new or changed vs git:
- Read that brief's `reference/sources.md`; if it contains `WEBFETCH_BLOCKED`, set
  `verify=search`, otherwise `verify=webfetch`.
- `git add` the brief + its `reference/sources.md` + `reference/perspectives.md`.
- `git commit -m "brief: {TODAY} [kind=ainews|watchlist] [verify=...]"` (use the matching kind).
If a brief is byte-identical to what's already committed, skip it — do not make an empty commit.
Then run `git push` once. The push fires `.github/workflows/email-notify.yml`, which emails
each brief. **Do not send email yourself.**

## Rules
- Do NOT edit any skill, workflow, or config — only produce briefs and commit them.
- Do NOT force-push. If `git push` fails, report the error and stop.
- Use only: Read, Write, Glob, Grep, WebSearch, WebFetch, and git via Bash. No other destructive commands.

## Final report
State, per brief: story count, tiers/verify mode, commit SHA (or NO-OP), and whether the
push succeeded. If anything failed, say exactly what.
