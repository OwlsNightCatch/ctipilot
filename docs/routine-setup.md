# Routine setup — Claude Code on the web

This repository's daily and weekly briefs are produced by [Claude Code routines](https://claude.ai/code/routines), running on Anthropic-managed cloud infrastructure. This page documents the one-time setup needed for the routine to push back to this repo, and the choices that affect how briefs are published.

## Why the prompts default to `main`

Both [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) and [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) instruct the agent to commit and push to `origin/main`. That's the *publishing target* — wherever the routine actually pushes (a `claude/...` feature branch or `main` directly), the brief is considered published when it lands on `main`.

The prompts also explicitly defer to environment-level branch instructions: when the routine container assigns a `claude/<adjective>-<name>-<id>` branch, the agent honours that and lets the environment's PR / merge / auto-merge policy take the change to `main`.

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

### 2. Decide on the publishing model

By default, the routine pushes to a `claude/<adjective>-<name>-<id>` feature branch. From the [Claude Code routines docs](https://docs.claude.com/en/docs/claude-code/routines):

> By default, Claude can only push to branches prefixed with `claude/`. This prevents routines from accidentally modifying protected or long-lived branches. To remove this restriction for a specific repository, enable **Allow unrestricted branch pushes** for that repository when creating or editing the routine.

Two acceptable workflows:

| Workflow | Setup | Publishing latency |
|---|---|---|
| **Direct push to `main`** | Enable **Allow unrestricted branch pushes** in the routine's edit form for this repo | Brief is live the moment the routine commits |
| **Feature branch + auto-merge** | Leave default; configure GitHub repo auto-merge for `claude/*` branches | Brief is live a few moments after the routine pushes — GitHub fast-forwards into `main` automatically |

For a public CTI feed where every brief is meant to be live immediately, "direct push to `main`" is the simplest setup.

To enable it:

1. <https://claude.ai/code/routines> → click the brief routine.
2. Pencil icon → **Edit routine**.
3. Scroll to **Permissions** → enable **Allow unrestricted branch pushes** for this repo.
4. Save.

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
