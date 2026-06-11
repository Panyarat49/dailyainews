# Local routine — dailyainews (Panyarat49/dailyainews)

The **primary production host**: a Windows Task Scheduler job runs both brief skills
on this machine each morning. Driver = [`scripts/run-daily-briefs.ps1`](scripts/run-daily-briefs.ps1).

## Why local? (the WebFetch-block circumvention)
Claude's **`WebFetch` is 403-blocked inside the claude.ai Web Routine** — there the
skills can only do degraded **Tier-2** verification (read a search *snippet*, never the
article body). On **this machine egress is open**, so `WebFetch` works and the skills
run full **Tier-1** verification: fetch the real article, read its own publish
timestamp, summarise from the body. Running locally is the simplest way to dodge the
block while using **your Claude subscription** (no API key, no GitHub Actions secrets).
*(GitHub Actions is also unblocked and always-on — kept as a documented backup in
`ACTIONS-SETUP.md` — but local is the chosen primary.)*

## Architecture (two workstreams, one shared engine)
```
.claude/skills/
  shared/engine.md          shared mechanics (freshness, dedup, tiered verify,
                            personas, length, write-only output) — edit ONCE
  shared/trusted-sources.md outlet allow-list (both skills)
  shared/defaults.json      repo owner/repo/branch + knobs (+ email hand-off note)
  daily-ai-news/      → articles/{DATE}-ainews.md     (GENERAL: any significant AI story)
  daily-ai-watchlist/ → articles/{DATE}-watchlist.md  (WATCHLIST: 20 cos / 2 tiers)
```
- **Skills are write-only.** They produce the brief + `sources.md` + `perspectives.md`
  and stop.
- **The runner commits + pushes** each brief (uses your stored git credentials).
- **The teammate's email sender delivers** from the committed briefs (LINE is retired;
  see the hand-off contract below). The runner does NOT send email.
- **Separate dedup streams:** general dedups vs prior `*-ainews.md`, watchlist vs prior
  `*-watchlist.md` — independent products.

## Prerequisites (one-time)
1. **Claude Code installed and logged in** with your subscription (this machine already
   is). Verify: `claude --version` and that `claude -p "hello"` runs without a login prompt.
2. **Git credentials for `Panyarat49`** — already in Windows Credential Manager (verified).
3. **Working clone** at `%USERPROFILE%\dailyainews` (NOT the OneDrive `build/` folder —
   keep `.git` out of OneDrive):
   ```powershell
   git clone https://github.com/Panyarat49/dailyainews.git $env:USERPROFILE\dailyainews
   ```
   (The refactored skills must be on `main` first — see the deploy step in STATUS.md.)

## Test it manually (before scheduling)
```powershell
# dry single brief for a chosen date, default model:
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\dailyainews\scripts\run-daily-briefs.ps1" -DateOverride 2026-06-11
```
Watch `…\dailyainews\logs\run-*.log`. Success = `articles/2026-06-11-ainews.md` and
`…-watchlist.md` produced, each committed `[kind=…] [verify=webfetch]`, and pushed.
Confirm `verify=webfetch` (proves Tier-1 / the block is bypassed).

## Schedule it (Task Scheduler, daily 07:15)
```cmd
schtasks /create /tn "dailyainews-brief" ^
  /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"%USERPROFILE%\dailyainews\scripts\run-daily-briefs.ps1\"" ^
  /sc daily /st 07:15
```
- `/st 07:15` is **local machine clock time**. If this machine's time zone is
  Asia/Bangkok (it is), 07:15 local = 07:15 BKK. The script computes the brief *date*
  in Asia/Bangkok regardless of machine TZ, so the filename is always correct.
- **Caveat — the machine must be awake at 07:15.** In Task Scheduler → the task →
  Conditions, tick **"Wake the computer to run this task"** (and untick "Start only on
  AC power" for a laptop). If the machine is off, that day is simply skipped (a gap, not
  an error). If gaps matter, enable the Actions backup.
- Edit the schedule: `schtasks /change /tn "dailyainews-brief" /st 08:00`.

## Email hand-off contract (teammate's scope)
The skills + runner stop at "committed brief." The email sender consumes:
- **Source files:** `articles/{DATE}-ainews.md`, `articles/{DATE}-watchlist.md`
- **Subject:** each brief's H1 (`# …`)
- **Body:** the brief Markdown (render to HTML or send as text)
- **Link:** commit-pinned permalink `https://github.com/Panyarat49/dailyainews/blob/{SHA}/{path}`
- The story headings are stable/parseable: `### N. … — [Publisher](URL)` (general) and
  `### N. Company (TICKER · Tier n) — Headline — [Publisher](URL)` + `**N.M … — [Pub](URL)**`
  roundup sub-items (watchlist). The existing `build_line_message.py` already parses both —
  a good starting point for an email renderer.
- To wire it in: pass `-EmailSender <path>` to the runner; it's invoked after a
  successful push with the date as `$args[0]`.

## Troubleshooting
| Symptom | Cause / fix |
|---|---|
| `'claude' CLI not found` | Not on PATH for the Task Scheduler user. Use the full path, or run the task as your user. |
| Login/permission prompt in the log | `claude` isn't logged in for that user, or a tool wasn't allow-listed. Re-run `claude` interactively once to log in. |
| `verify=search` in the commit | WebFetch was blocked even locally (rare) — check network/VPN/egress. The point of local is `verify=webfetch`. |
| `push failed` | Stale clone — the runner does `git pull --ff-only` first; if it diverged, reconcile manually. |
| Brief not produced | See the per-run log; the skill may have hit 0 stories (empty-day stub is still written + committed). |
| Day skipped entirely | Machine was off/asleep at 07:15. Enable wake-to-run, or use the Actions backup. |

## Host comparison
| | Local (this) | GitHub Actions | claude.ai Web Routine |
|---|---|---|---|
| WebFetch | open → **Tier-1** | open → Tier-1 | **403-blocked** → Tier-2 only |
| Always-on | no (machine must be up) | yes | yes |
| Billing | your subscription | API/OAuth + secrets | subscription |
| Secrets needed | none | repo secrets | none |
| Status | **primary** | backup (`ACTIONS-SETUP.md`) | fallback (`ROUTINE-SETUP.md`) |
