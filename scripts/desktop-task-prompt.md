# Desktop scheduled-task prompt — daily AI briefs

This is the versioned copy of the prompt run by the local Desktop scheduled task
`dailyainews-daily` (daily ~11:49 Asia/Bangkok). Each run is a fresh local session
(WebFetch unblocked → Tier-1). Keep this in sync with the live task; to edit the live
task, update it via the scheduled-tasks tool, then mirror the change here.

Permissions: the user's `~/.claude/settings.json` allow-list pre-approves the tools the
run uses (`Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Bash`) so the unattended
run never pauses on a prompt. Pushes authenticate via the clone's remote (fine-grained
PAT scoped to this repo).

---

You are the daily dailyainews routine, running locally via the Claude Desktop app. No human is watching — work fully autonomously, never ask questions, never stop to confirm.

Repo = the local clone at C:\Users\panya\dailyainews. Use git with `-C "C:\Users\panya\dailyainews"` for ALL git commands (do NOT use `cd`). Use absolute paths under that folder for Read/Write.

First: run `git -C "C:\Users\panya\dailyainews" pull --ff-only` (if it fails due to local changes, run `git -C "C:\Users\panya\dailyainews" stash` then pull).

Compute TODAY = today's date in Asia/Bangkok (YYYY-MM-DD).

Produce BOTH briefs (WRITE-ONLY; gap-fill — the skills must NOT commit). For EACH brief, if the file already exists for TODAY, SKIP it untouched; otherwise produce it:
- GENERAL — if C:\Users\panya\dailyainews\articles\{TODAY}-ainews.md does NOT exist: Read C:\Users\panya\dailyainews\.claude\skills\daily-ai-news\SKILL.md, then Read and follow C:\Users\panya\dailyainews\.claude\skills\shared\engine.md → write C:\Users\panya\dailyainews\articles\{TODAY}-ainews.md (+ that skill's reference\sources.md & reference\perspectives.md).
- WATCHLIST — if C:\Users\panya\dailyainews\articles\{TODAY}-watchlist.md does NOT exist: Read C:\Users\panya\dailyainews\.claude\skills\daily-ai-watchlist\SKILL.md, then follow the shared engine → write C:\Users\panya\dailyainews\articles\{TODAY}-watchlist.md (+ its reference files).
WebFetch works here — prefer Tier-1 (fetch body + real publish date); cross-match to an allow-listed outlet if a primary 403s. Gates: 24h freshness on the WRITE-UP, URL dedup, (watchlist) AI-relevance/significance/membership. Aim 4–5 stories, hard floor 3 — fill toward 4–5 with relevant in-window items; never reach past 24h. Empty day → stub.

Commit + push (triggers email). For EACH brief you NEWLY wrote: read its reference\sources.md (if it contains WEBFETCH_BLOCKED set verify=search else verify=webfetch); `git -C "C:\Users\panya\dailyainews" add <brief> <its sources.md> <its perspectives.md>`; `git -C "C:\Users\panya\dailyainews" commit -m "brief: {TODAY} [kind=ainews|watchlist] [verify=...]"`. Then `git -C "C:\Users\panya\dailyainews" push`. If the push is REJECTED (non-fast-forward), run `git -C "C:\Users\panya\dailyainews" pull --rebase` then push again (retry up to 3 times). The push fires .github/workflows/email-notify.yml → emails each brief.

Rules: do NOT send email yourself; do NOT edit any skill/workflow/config; do NOT force-push. Use only Read, Write, Glob, Grep, WebSearch, WebFetch, and git via Bash (every git command as `git -C "C:\Users\panya\dailyainews" ...`, never `cd`).

Final report: per brief — produced or skipped(exists), story count, tiers/verify mode, commit SHA (or NO-OP), and whether the push succeeded.
