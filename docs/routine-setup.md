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

### 3. Optional fallback — GitHub Action that merges `claude/*` to `main`

If you'd like a safety net that catches the cases where the primary push to `main` fails (Path C accidentally disabled, etc.), add this workflow at `.github/workflows/auto-merge-claude.yml`:

```yaml
name: Auto-merge claude/* to main
on:
  push:
    branches:
      - "claude/**"

jobs:
  merge:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          ref: main
      - name: Fast-forward main from feature branch
        env:
          BRANCH: ${{ github.ref_name }}
        run: |
          git config user.name "Claude Code"
          git config user.email "noreply@anthropic.com"
          git fetch origin "$BRANCH"
          # Allow only if the branch is a strict ancestor + descendant of main
          # (i.e., it's a fast-forward).
          if git merge-base --is-ancestor main "origin/$BRANCH"; then
            git merge --ff-only "origin/$BRANCH"
            git push origin main
            git push origin --delete "$BRANCH" || true
          else
            echo "Branch $BRANCH is not a fast-forward of main; skipping."
            exit 0
          fi
```

With this Action in place, even a failed primary push still publishes the brief — the fallback push lands on `claude/...`, the Action fast-forwards `main`, and the feature branch is cleaned up. It's a redundant safety net; with Path C correctly enabled, the Action just sits idle.

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
7. **Trigger**: choose a schedule. A reasonable starting cadence is **Daily, weekday mornings, 06:30 Europe/Zurich** (the form converts automatically).
8. **Connectors**: none needed. The brief workflow is self-contained.
9. **Permissions**: enable **Allow unrestricted branch pushes** for this repo if you want direct-to-`main` (recommended for a public feed).
10. **Create**.

Repeat for the weekly summary with prompt `Read prompts/weekly-summary.md and execute it.` and a Sunday-evening schedule.

## Verifying the setup

After saving the routine, click **Run now** on its detail page once. A new session opens; you can watch it execute the workflow live. Successful end state:

- All sub-agents return (or partial-result mode triggers — see Prime Directive 12 in the daily prompt).
- The composition phase performs incremental writes (one `Write` for the skeleton, then one `Edit` per section).
- Phase 6 commits and pushes. The operator output's last line should read `push: ok`.
- Within a few minutes, the brief is visible at `https://github.com/<owner>/security-newsletter/blob/main/briefs/YYYY-MM-DD.md`.

If you instead see `push: failed (HTTP 403 — …)`, return to step 1 above — the credential doesn't have write access to this repo.

## Limits to be aware of

- **Daily routine cap.** Claude Code routines have an account-wide daily run cap. See your current consumption at <https://claude.ai/code/routines>.
- **Subscription rate limits.** Routines draw from the same usage budget as interactive sessions.
- **Per-routine token regeneration.** API-trigger tokens are shown once. If you forgot one, regenerate from the routine's settings.

## When something goes wrong

- **`push: failed (HTTP 403)`** → GitHub-App / token doesn't have write access on the repo. Re-do step 1.
- **Brief never written** → sub-agent stalled past 10 min, or composition tripped a stream timeout. The current prompt versions handle both via partial-result fallback (v2.4) and incremental writes (v2.5). If you're still seeing this, check the routine session's log for the failure point and tell the prompt's maintainer.
- **Brief written but not on `main`** → routine pushed to a `claude/...` branch as expected; either enable **Allow unrestricted branch pushes** or configure GitHub auto-merge.
