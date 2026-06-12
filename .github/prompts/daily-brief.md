You are running headless inside a GitHub Actions runner (cloud) — the BACKUP host for
the dailyainews routine. You run only when the local machine missed its daily run.
No human is watching; work autonomously. WebFetch works here (NOT 403-blocked).

The repo is already checked out at the working directory. Compute TODAY = today's date
in Asia/Bangkok (the runner TZ is Asia/Bangkok).

Produce today's two briefs, but ONLY the ones not already present (gap-fill):
1. If `articles/{TODAY}-ainews.md` does NOT already exist → Read
   `.claude/skills/daily-ai-news/SKILL.md`, then Read and follow
   `.claude/skills/shared/engine.md`, and write `articles/{TODAY}-ainews.md`
   (+ that skill's `reference/sources.md` & `reference/perspectives.md`).
2. If `articles/{TODAY}-watchlist.md` does NOT already exist → Read
   `.claude/skills/daily-ai-watchlist/SKILL.md`, then Read and follow
   `.claude/skills/shared/engine.md`, and write `articles/{TODAY}-watchlist.md`
   (+ its `reference/sources.md` & `reference/perspectives.md`).
If a brief already exists for TODAY, leave it untouched (the local host produced it).

Apply the gates strictly: 24h freshness on the WRITE-UP, URL dedup (read prior briefs
from the local `articles/` dir), and for the watchlist the AI-relevance / significance /
membership gates. Aim for 4–5 stories, hard floor 3 — fill toward 4–5 with relevant
in-window items, never reach past 24h to pad. Prefer Tier-1 (fetch the article body +
real publish date); cross-match to an allow-listed outlet if a primary 403s. On a
genuinely empty day, write the one-line stub.

This is WRITE-ONLY: do NOT commit, push, or send email — the workflow handles git and
email. Do NOT use Bash or git. Stop after writing the file(s) and print a short report
(which briefs you wrote, story counts, tiers/verify mode).
