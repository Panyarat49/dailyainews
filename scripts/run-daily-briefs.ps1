<#
.SYNOPSIS
  Local daily routine for the dailyainews project (Panyarat49/dailyainews).
  Runs BOTH brief skills headless on this machine, commits each brief, pushes.

.WHY LOCAL
  Claude's WebFetch is 403-blocked inside the claude.ai Web Routine, forcing
  degraded Tier-2 (snippet-only) verification there. On THIS machine egress is
  open, so the skills run full Tier-1 verification (fetch the article body, read
  its real publish timestamp). Running locally is the simplest way to dodge that
  block while using your Claude subscription (no API key, no repo secrets).

.WHAT IT DOES
  1. git pull (ff-only) the working clone.
  2. claude -p  ->  daily-ai-news     (general)  -> articles/<TODAY>-ainews.md
  3. claude -p  ->  daily-ai-watchlist (watchlist)-> articles/<TODAY>-watchlist.md
  4. Per brief: if it changed, commit "brief: <TODAY> [kind=..] [verify=..]" and push.
  5. STOP. Email delivery is the teammate's email sender, which consumes the
     committed briefs (see shared/defaults.json -> _email_handoff). This script
     does not send email.

.SETUP
  See LOCAL-ROUTINE.md. Requires: Claude Code installed + logged in (subscription),
  git credentials for Panyarat49 (already in Windows Credential Manager), and a
  working clone of the repo. Schedule via Task Scheduler (07:15 Asia/Bangkok).
#>

[CmdletBinding()]
param(
  # Working clone of https://github.com/Panyarat49/dailyainews (NOT the OneDrive build/ folder).
  [string]$RepoPath = "$env:USERPROFILE\dailyainews",
  # Model for the daily run. Opus by default; drop to claude-sonnet-4-6 to save subscription budget.
  [string]$Model    = "claude-opus-4-8",
  # Optional: override the date (YYYY-MM-DD). Blank = today in Asia/Bangkok.
  [string]$DateOverride = "",
  # Optional path to the teammate's email-sender script. If set, invoked after a successful push.
  [string]$EmailSender = ""
)

# 'Continue' (not 'Stop'): this is a native-command-heavy automation script. In
# Windows PowerShell 5.1, git writes normal progress to stderr; under 'Stop' that can
# raise spurious terminating errors. We gate on explicit $LASTEXITCODE checks instead.
$ErrorActionPreference = "Continue"
$AllowedTools = "Read,Write,Edit,WebSearch,WebFetch,Glob,Grep"

# --- TODAY in Asia/Bangkok (independent of the machine's local TZ) ---
if ($DateOverride) {
  $Today = $DateOverride
} else {
  $bkk   = [System.TimeZoneInfo]::FindSystemTimeZoneById("SE Asia Standard Time") # UTC+7 (Bangkok)
  $Today = [System.TimeZoneInfo]::ConvertTimeFromUtc((Get-Date).ToUniversalTime(), $bkk).ToString("yyyy-MM-dd")
}

# --- logging ---
$logDir = Join-Path $RepoPath "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp  = [System.TimeZoneInfo]::ConvertTimeFromUtc((Get-Date).ToUniversalTime(),
            [System.TimeZoneInfo]::FindSystemTimeZoneById("SE Asia Standard Time")).ToString("yyyyMMdd-HHmmss")
$logFile = Join-Path $logDir "run-$stamp.log"
function Log($m) { $line = "[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $m; Write-Host $line; Add-Content -Path $logFile -Value $line -Encoding utf8 }

Log "=== daily-briefs run: TODAY=$Today  repo=$RepoPath  model=$Model ==="

# --- resolve claude CLI (npm global on Windows is usually claude.cmd) ---
$claude = (Get-Command claude -ErrorAction SilentlyContinue)
if (-not $claude) { $claude = (Get-Command claude.cmd -ErrorAction SilentlyContinue) }
if (-not $claude) { Log "FATAL: 'claude' CLI not found on PATH. Install @anthropic-ai/claude-code and ensure it's logged in."; exit 1 }
$claudeExe = $claude.Source

# --- sync ---
Push-Location $RepoPath
try {
  git rev-parse --is-inside-work-tree *> $null
  if ($LASTEXITCODE -ne 0) { Log "FATAL: $RepoPath is not a git repo. Clone Panyarat49/dailyainews there first."; exit 1 }
  Log "git pull --ff-only..."
  git pull --ff-only 2>&1 | ForEach-Object { Log "  git: $_" }

  git config user.name  "dailyainews-bot" *> $null
  git config user.email "panyarattangsripong@gmail.com" *> $null

  # --- the two workstreams: (skill name, output suffix, sources.md path, label) ---
  $jobs = @(
    @{ Skill="daily-ai-news";      Suffix="ainews";    Kind="ainews";
       Sources=".claude/skills/daily-ai-news/reference/sources.md";
       Persp=".claude/skills/daily-ai-news/reference/perspectives.md" },
    @{ Skill="daily-ai-watchlist"; Suffix="watchlist"; Kind="watchlist";
       Sources=".claude/skills/daily-ai-watchlist/reference/sources.md";
       Persp=".claude/skills/daily-ai-watchlist/reference/perspectives.md" }
  )

  $anyFailure = $false

  foreach ($j in $jobs) {
    $brief = "articles/$Today-$($j.Suffix).md"
    Log "--- $($j.Skill) -> $brief ---"

    $prompt = @"
You are running headless on a local machine (Task Scheduler). No human is watching.
Run the ``$($j.Skill)`` skill for today's scheduled brief: Read
.claude/skills/$($j.Skill)/SKILL.md, then Read and follow .claude/skills/shared/engine.md.
WebFetch works here (not blocked) — prefer Tier-1 verification.
Write the brief to $brief and the run's sources.md / perspectives.md. Do NOT commit,
push, or send anything — this script handles git, and the teammate's sender handles email.
Compute TODAY as the Asia/Bangkok date.
"@

    try {
      & $claudeExe -p $prompt --model $Model --permission-mode acceptEdits --allowedTools $AllowedTools 2>&1 |
        ForEach-Object { Add-Content -Path $logFile -Value $_ -Encoding utf8 }
      $code = $LASTEXITCODE
    } catch {
      Log "  claude invocation threw: $_"; $code = 1
    }

    if ($code -ne 0) { Log "  claude exited $code for $($j.Skill) — skipping commit for this brief."; $anyFailure = $true; continue }
    if (-not (Test-Path $brief)) { Log "  WARNING: $brief was not produced. Skipping commit."; $anyFailure = $true; continue }

    # verify tag from this brief's sources.md
    $verify = "webfetch"
    if (Test-Path $j.Sources) { if (Select-String -Path $j.Sources -Pattern "WEBFETCH_BLOCKED" -Quiet) { $verify = "search" } }

    git add -- $brief
    foreach ($f in @($j.Sources, $j.Persp)) { if (Test-Path $f) { git add -- $f } }

    git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) { Log "  NO-OP: $brief unchanged — no commit."; continue }

    $msg = "brief: $Today [kind=$($j.Kind)] [verify=$verify]"
    git commit -m $msg 2>&1 | ForEach-Object { Log "  commit: $_" }
    Log "  committed: $msg"
  }

  # --- push once at the end ---
  Log "git push..."
  git push 2>&1 | ForEach-Object { Log "  push: $_" }
  if ($LASTEXITCODE -ne 0) { Log "  push failed (exit $LASTEXITCODE)."; $anyFailure = $true }

  # --- email hand-off (teammate's sender) ---
  if ($EmailSender) {
    if (Test-Path $EmailSender) {
      Log "invoking email sender: $EmailSender"
      & $EmailSender $Today 2>&1 | ForEach-Object { Log "  email: $_" }
    } else {
      Log "EmailSender path '$EmailSender' not found - skipping (briefs are committed; teammate's sender can pick them up)."
    }
  } else {
    Log "email: not invoked here (teammate's sender consumes the committed briefs)."
  }

  Log "=== done. TODAY=$Today  failures=$anyFailure ==="
  if ($anyFailure) { exit 1 } else { exit 0 }
}
finally { Pop-Location }
