# Routine setup — Claude Code on the web

This repository's daily and weekly briefs are produced by [Claude Code routines](https://claude.ai/code/routines), running on Anthropic-managed cloud infrastructure. This page documents the one-time setup needed for the routine to push back to this repo, and the choices that affect how briefs are published.

## How publishing works

The routine container always checks out a `claude/<adjective>-<name>-<id>` branch on session start — that's hardcoded environment behavior. The prompts don't fight this; instead they commit on whatever branch the environment assigned and then publish with:

```sh
git push origin HEAD:main
```

This pushes the current commit directly to remote `main`, regardless of the local branch name. With **Allow unrestricted branch pushes** enabled on the routine for this repo, the push succeeds and the brief is live immediately.

If that primary push is rejected (Path C below not enabled, branch protection rules, etc.), the prompt falls back to pushing the current `claude/...` branch as-is, so a GitHub auto-merge rule, a GitHub Action, or manual PR review can take it from there.

## What you need to do once

### 1. Install the Claude GitHub App on this repo

The routine container pushes through an internal git proxy that uses a scoped GitHub credential. By default the most reliable credential source is the **Claude GitHub App**.

1. Go to <https://github.com/apps/claude>.
2. **Configure** (or **Install** if it's not yet on your account).
3. Under **Repository access**, either:
    - **All repositories**, or
    - **Only select repositories** → add this repo.
4. Save.

If you'd rather use `gh`-token sync, the alternative is:

```sh
gh auth refresh -h github.com -s repo
# then in a Claude Code CLI session:
/web-setup
```

This widens your `gh` token to include `repo` write scope and syncs it to your claude.ai account. The Claude GitHub App route is more durable.

Either way, the credential the routine uses must have write access to this repo, otherwise the push step fails with HTTP 403 *(Permission to … denied)*.

### 2. Enable direct-push to `main`

From the [Claude Code routines docs](https://docs.claude.com/en/docs/claude-code/routines):

> By default, Claude can only push to branches prefixed with `claude/`. This prevents routines from accidentally modifying protected or long-lived branches. To remove this restriction for a specific repository, enable **Allow unrestricted branch pushes** for that repository when creating or editing the routine.

Enable that for this repo so the prompt's `git push origin HEAD:main` succeeds:

1. <https://claude.ai/code/routines> → click the brief routine.
2. Pencil icon → **Edit routine**.
3. Scroll to **Permissions** → enable **Allow unrestricted branch pushes** for this repo.
4. Save.

After this, every routine run lands the brief directly on `main` with no PR / merge step.

### 3. Auto-merge GitHub Action (required as safety net)

The workflow at [`.github/workflows/auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) is shipped with the repository. It triggers on any push to a `claude/**` branch, fast-forwards `main` from the feature branch, and deletes the feature branch. This is what catches the case where the routine's primary `git push origin HEAD:main` is rejected (Path C off, branch protection, transient auth) — the fallback push to a `claude/...` branch is enough to publish, because the Action handles the merge.

What the Action requires:

- It is committed to the repo at the path above. Pushing this repo to GitHub installs it automatically.
- The repo's default `GITHUB_TOKEN` permissions must allow `contents: write`. The workflow declares this in its `permissions:` block, so for most repositories it works without further configuration. If your repo or organization has set the default `GITHUB_TOKEN` permissions to **read-only**, the Action's `git push origin main` will be rejected and the brief will stay on the feature branch.
    - To check / fix: GitHub repo → **Settings** → **Actions** → **General** → under **Workflow permissions**, choose **Read and write permissions**, save.
- The Action only fast-forwards. If `main` has advanced since the routine started (rare for an unattended public feed), the Action exits cleanly and leaves the feature branch alone for human review.
- The Action also exposes a manual `workflow_dispatch` trigger with a `branch` input, so you can merge a `claude/...` branch that was pushed before the workflow existed (or re-run after fixing an issue). GitHub repo → **Actions** → **Auto-merge claude/\* branches to main** → **Run workflow** → enter the branch name.

### Two-stage publishing chain

With Path C and the auto-merge Action both in place, the publishing chain has redundancy at every step:

| Stage | What happens | Brief on main? |
|---|---|---|
| 1. Direct push (`git push origin HEAD:main`) | Path C is enabled and the credential has write scope | **Yes**, immediately |
| 2. Fallback to feature branch + auto-merge Action | Stage 1 was rejected; routine pushes `claude/...`; Action fast-forwards `main` | **Yes**, within a few seconds |
| 3. Both stages failed | Routine credential lacks any push scope | **No** — local commit preserved; investigate the App / token permissions |

## Setting up the routine itself

If you don't yet have the routine, create one as follows:

1. Visit <https://claude.ai/code/routines>.
2. **New routine**.
3. **Name**: `CTI daily brief` (or similar).
4. **Prompt**:
    ```
    Read prompts/daily-cti-brief.md and execute it.
    ```
5. **Repositories**: add this repo.
6. **Environment**: the **Default** cloud environment is fine for first runs. The brief workflow only needs network access to the source list, which is covered by the **Trusted** access level.
7. **Trigger**: choose any schedule that suits your team. The prompt does **not** hardcode times or days — every run reads `briefs/` and covers the gap since the previous published brief, with a 12-hour safety overlap (Prime Directive 7 in [`../prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md)). A common pattern is *weekday mornings* before the SOC shift handover (Mon–Fri, before working hours start); the next-Monday brief then naturally widens its window to cover Friday-late + the weekend on its own. Skipping days, public holidays, and failed runs are all auto-recovered by the next run — change the cron freely without touching the prompt.
8. **Connectors**: none needed. The brief workflow is self-contained.
9. **Permissions**: enable **Allow unrestricted branch pushes** for this repo if you want direct-to-`main` (recommended for a public feed).
10. **Create**.

Repeat for the weekly summary with prompt `Read prompts/weekly-summary.md and execute it.` and any cadence the operator prefers (typical: once per week). The weekly prompt uses the same gap-derivation rule against `briefs/weekly/` — change the cron freely; the next run catches up.

## Verifying the setup

After saving the routine, click **Run now** on its detail page once. A new session opens; you can watch it execute the workflow live. Successful end state:

- All sub-agents return (or partial-result mode triggers — see Prime Directive 12 in the daily prompt).
- The composition phase performs incremental writes (one `Write` for the skeleton, then one `Edit` per section).
- Phase 6 commits and pushes. The operator output's last line should read `push: ok`.
- Within a few minutes, the brief is visible at `https://github.com/<owner>/security-newsletter/blob/main/briefs/YYYY-MM-DD.md`.

If you instead see `push: failed (HTTP 403 — …)`, return to step 1 above — the credential doesn't have write access to this repo.

## Enable GitHub Pages

The repository ships with [`site/`](../site/) — a static reader for the briefs — and a [`deploy-site.yml`](../.github/workflows/deploy-site.yml) workflow that publishes it to GitHub Pages. The workflow runs automatically on every push to `main` that touches `briefs/`, `state/`, `sources/`, `docs/`, `README.md`, or `site/`. It does *not* fire on every routine commit unrelated to brief content.

One-time enable:

1. Push any change touching the trigger paths above (or run the **Deploy GitHub Pages site** workflow manually). The first run creates a `gh-pages` branch containing the built site.
2. GitHub repo → **Settings** → **Pages**.
3. Under **Build and deployment** → **Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose **`gh-pages`** and **`/ (root)`**. Save.
5. Refresh the Pages settings page — your live URL appears at the top.

The site is fully static and read-only. The deploy workflow uses only shell-level git commands so it works under organisations that restrict third-party GitHub Actions.

## Engagement metrics — none, by choice

The site does **not** collect aggregate visit counts. There are no
analytics scripts, beacons, cookies, fingerprinting, or third-party
trackers, and no on-device personal-history panel. The strict CSP
(`connect-src 'self'`) blocks any future regression that tries to add
cross-origin telemetry.

A previous version of this repo pulled the GitHub Repo Traffic API
into `state/engagement.json` (and required a `TRAFFIC_PAT` secret). It
was removed because the API exposes github.com repo views only — not
GitHub Pages site visits — so the metric was misleading for our
deployment shape. If the operator wants real Pages-site analytics
later, the realistic options are documented in
[`docs/improvements.md`](improvements.md) item S7b (Cloudflare Web
Analytics, GoatCounter, Plausible). None are enabled by default.

If a `TRAFFIC_PAT` secret was created during the previous version, you
can safely delete it from the repo's secrets — nothing reads it now.

## Sub-agent capability ceiling

The four research sub-agents the daily routine spawns are the single
most dangerous configuration surface: a sub-agent that follows an
injection-laced page could perform writes the parent never intended
([`docs/security-review.md`](security-review.md) § 2.4 / T4). When
configuring the routine in claude.ai, restrict the sub-agent toolset
to **read-only** operations:

| Allowed for sub-agents | `Read`, `Grep`, `Glob`, `WebFetch`, `WebSearch` |
| Forbidden for sub-agents | `Write`, `Edit`, `Bash`, `Task`, `NotebookEdit` |

The main agent retains the full toolset (it has to write the brief and
push the commit). Sub-agents return Markdown to the main context and
never touch the filesystem or git directly.

Verify the live routine config matches this list as a periodic
operator-checklist task. The prompt's own sub-agent section names
allowed tools, but the runtime is what enforces them.

## Rotation cadence (credentials)

Tokens that don't rotate eventually leak. Recommended cadence:

| Credential | Rotate every | How |
| --- | --- | --- |
| Claude GitHub App install | 90 days | Re-install the app on the repo (revoke old install at <https://github.com/settings/installations>). |
| Routine API trigger token | On-demand and whenever it appears in any logs / docs / chat | Routine settings → regenerate trigger token. |
| Repo `GITHUB_TOKEN` (workflow) | Automatic (per-run) | No action needed; GitHub rotates this for you. |

Add a calendar reminder for the App rotation. The first time a 403 lands
on `git push origin HEAD:main` is the wrong moment to remember.

## Limits to be aware of

- **Daily routine cap.** Claude Code routines have an account-wide daily run cap. See your current consumption at <https://claude.ai/code/routines>.
- **Subscription rate limits.** Routines draw from the same usage budget as interactive sessions.
- **Per-routine token regeneration.** API-trigger tokens are shown once. If you forgot one, regenerate from the routine's settings.

## When something goes wrong

- **`push: failed (HTTP 403)`** → GitHub-App / token doesn't have write access on the repo. Re-do step 1.
- **Brief never written** → sub-agent stalled past 10 min, or composition tripped a stream timeout. The current prompt versions handle both via partial-result fallback (v2.4) and incremental writes (v2.5). If you're still seeing this, check the routine session's log for the failure point and tell the prompt's maintainer.
- **Brief written but not on `main`** → routine pushed to a `claude/...` branch as expected; either enable **Allow unrestricted branch pushes** or configure GitHub auto-merge.
