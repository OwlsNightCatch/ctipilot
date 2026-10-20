---
title: Glassworm Hacks OVH Clouds CLI tool
author: OpenSourceMalware com; C
url: https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool
hostname: opensourcemalware.com
description: On 2026-10-19, the official OVHcloud CLI tool was compromised by the Glassworm threat actors who published five malicious versions to GitHub and Brew
sitename: OpenSourceMalware
date: "2026-10-19"
tags: ['malware, npm security, package security, open source security, threat intelligence, vulnerability reporting']
fingerprint: bdad10df47f73786
---
BLOG

# Glassworm Hacks OVH Clouds CLI tool

On 2026-10-19, the official OVHcloud CLI tool was compromised by the Glassworm threat actors who published five malicious versions to GitHub and Brew

By c0a15726-c5b1-4b0d-85e6-fe15553df9e2 ·

# OVHcloud CLI supply chain compromise: release assets replaced through a GlassWorm-hijacked contributor account

Oct 20, 2026 · @6mile

## Summary

On 19 October 2026, between 12:47 and 13:12 UTC, an attacker replaced the release binaries of five already-published versions of OVHcloud’s official CLI (`ovh/ovhcloud-cli`, v0.11.0 to v0.15.0) with a secret-stealing build. The uploads were made through the GitHub account `HassenBF`, a legitimate OVH contributor, using the ordinary GitHub Releases API. No tag was pushed and no GitHub Actions workflow ran. The malicious binary was a `go build` from a workstation with uncommitted changes, dropped straight onto existing releases. A downstream user whose CI pinned a SHA-256 caught it within 94 minutes. OVHcloud deleted the files at 14:21 UTC and shipped a clean, immutable v0.16.0 about three hours later.

The `HassenBF` account was already compromised and had been for seven months. Its public repositories show a scripted history rewrite on 5 March 2026 and a hidden `preinstall.js` loader that decodes to a second stage using a Solana memo dead drop. The wallet is a known GlassWorm indicator, and the amend-and-force-push technique matches the ForceMemo campaign. The earliest server-verified use of the account by the attacker is 5 March 2026, about 228 days before the asset replacement. Whether the same actor did both is our inference, and we cover its limits below.

This is a release-asset replacement attack. The source repository was never touched, so anyone verifying against the Go module proxy or building from source was fine. But anyone who ran `install.sh`, `brew install --cask ovh/tap/ovhcloud-cli`, or downloaded a tarball from GitHub in that window on macOS, Linux x86\_64/arm64 or Windows x86\_64 got the malware.

## Scope and limits

We built the timeline from server-side GitHub data (the repository Activity API, Actions run records and release records), not from git author, committer or tagger dates, which the pusher controls. OVHcloud deleted the replaced binaries before anyone archived them, so we have not analyzed the payload, and we could not independently confirm the 12:47 to 13:12 replacement times. Those come from the reporter’s capture in issue #300. The link between the March account compromise and the October asset replacement rests on the shared account identity, not on anything we observed directly. We found no PolinRider markers, no malicious workflow additions and no GhostAction indicators. The affected versions come from OVHcloud’s statements and the public issue, which lists v0.13.0 to v0.15.0. Release timestamps and the assets left behind show v0.11.0 and v0.12.0 were also touched.

## Timeline

OVHcloud’s public statements use Paris time (UTC+2), so we converted everything to UTC. By our math the attacker was swapping files for about 25 minutes, and the bad files were available to download for 94. Every row below is a GitHub server-side timestamp unless the source column says otherwise.

Time (UTC)

Event

Source

2026-03-05 02:41:17

Force push to `HassenBF/treasure-hunt-game`. The new tip adds `preinstall.js`.

Activity API

02:41:23

Force push to `crwn-clothing`. The payload is inlined in `src/index.js`.

Activity API

02:41:59

Force push to `next-dashboard`. The new tip adds `preinstall.js`.

Activity API

2026-03-06 22:49:53

Force push to `padel-bot`. The new tip adds `preinstall.js`.

Activity API

2026-05-25 to 2026-09-07

`HassenBF` keeps pushing branches and landing ordinary pull requests in `ovh/ovhcloud-docs` (release script, changelog format, linter, PDF generation).

Activity API

2026-10-13 08:35:05

Commit `5ead8ef` merged to `main` (PR #296) by `FrostByte0x`. The malicious binary was later built from a checkout at this commit.

Activity API, Actions run at 08:35:08

2026-10-15 14:34:11 to 14:34:13

`HassenBF` deletes branches `dev/test-changest` and `test/trigger-probe` in `ovh/ovhcloud-docs`.

Activity API

2026-10-16 14:38:11

Commit `6ef70c2` merged to `main`, ending the window in which `5ead8ef` was the tip.

Activity API

2026-10-19 12:47

First replaced assets land on v0.15.0 (Linux arm64, Linux x86\_64, Darwin arm64, Darwin x86\_64, Windows x86\_64). Klaba’s “14h47” is this moment.

12:57

v0.15.0 `checksums.txt` replaced, so the new hashes match the new binaries.

Issue #300

13:01 to 13:04

v0.14.0 Linux arm64 and checksums replaced.

Issue #300

13:08 to 13:11

v0.13.0 Linux arm64 and checksums replaced. v0.11.0 and v0.12.0 replaced in the same pass per OVHcloud.

Issue #300, OVHcloud

\~13:12

Replacement ends.

Issue #300

13:50:09

Issue #300 opened. A downstream CI job that pins the SHA-256 of `ovhcloud-cli_Linux_arm64.tar.gz` failed. The reporter checked `go version -m`, found a dirty build, and filed publicly (no private reporting enabled on the repo).

Issues API

14:21

OVHcloud deletes every replaced asset across the five releases (“16:21 GMT+2”).

rbeuque74 in #300

16:00:23

v0.16.0 tag push starts `Build and test` (actor `rbeuque74`) and `release` (triggering actor `FrostByte0x`). The `release` run fails.

Actions API

16:54:32

`HassenBF` profile record updated. This field changes on any profile edit, so we don’t read it as a credential reset.

Users API

17:16:43 to 17:16:54

v0.16.0 assets uploaded by the `ovh-cds` service account, including a `Release attestation (json)` asset, and the release published as immutable. Klaba posts the alert on X.

Releases API

2026-10-20

OVHcloud says first checks show no other repo affected. A post-mortem is promised “in the coming days”.

X, #300

## What was replaced

The attacker was selective. Each GoReleaser release ships 9 platform archives plus `checksums.txt`. Only the mainstream targets were swapped: both macOS builds, Linux x86\_64 and arm64, Windows x86\_64, and the checksum file. The i386 builds, Windows arm64 and the WASM build were left alone. You can see this on the release pages today. v0.11.0 through v0.15.0 each have exactly four binaries left (i386 ×2, Windows arm64, WASM) with their original upload timestamps, because OVHcloud deleted the six replaced files from each release.

Release

Originally published

Original uploader

Assets replaced on 19 Oct

Assets untouched (still live)

v0.15.0

2026-09-16

`amstuta`

Darwin arm64, Darwin x86\_64, Linux arm64, Linux x86\_64, Windows x86\_64, checksums.txt

Linux i386, Windows i386, Windows arm64, Js wasm

v0.14.0

2026-08-31

`amstuta`

Linux arm64 and checksums confirmed by the reporter; same six as v0.15.0 inferred from what remains

Linux i386, Windows i386, Windows arm64, Js wasm

v0.13.0

2026-08-25

`amstuta`

Linux arm64 and checksums confirmed; same six inferred

Linux i386, Windows i386, Windows arm64, Js wasm

v0.12.0

2026-05-29

`amstuta`

Six inferred from what remains (OVHcloud lists it as affected)

Linux i386, Windows i386, Windows arm64, Js wasm

v0.11.0

2026-04-14

`amstuta`

Six inferred from what remains (OVHcloud lists it as affected)

Linux i386, Windows i386, Windows arm64, Js wasm

v0.10.0

2026-03-02

`amstuta`

None. All 10 assets intact with original 2026-03-02 timestamps

All

v0.16.0

2026-10-19

`ovh-cds`

Clean rebuild, immutable, with release attestation

All

We think this shows what the attacker was after. They skipped the platforms almost nobody runs and the WASM target that can’t read a filesystem. This looks like credential harvesting aimed at developer and ops workstations, not a random defacement.

The one known-bad hash we have comes from the reporter’s pinned CI check:

File

Original SHA-256

Replaced SHA-256

v0.15.0 `ovhcloud-cli_Linux_arm64.tar.gz`

`5c2beb56e6d83a4b426565a1557791ef759316abcc4effb38dd627c90aeb80e0`

`3833daffcaaaab27e4e0e0833240ffcb1df8df648f4ec0bc4a75c176e28933cb`

## The binary was built on a laptop, not in a pipeline

Go binaries carry their own build info, and the reporter pulled it out with `go version -m` before OVHcloud deleted the files:

```
mod   github.com/ovh/ovhcloud-cli  v0.15.1-0.20261013083505-5ead8ef9b43d+dirty
build -ldflags="-s -w"
build vcs.revision=5ead8ef9b43d354dfb5caadff803b11afc8c5c58
build vcs.time=2026-10-13T08:35:05Z
build vcs.modified=true
```
Now compare that with how the project actually builds releases. `.goreleaser.yaml` sets `-trimpath` and `-ldflags "-s -w -extldflags -static -X github.com/ovh/ovhcloud-cli/internal/version.Version={{.Tag}}"`. Four things don’t match.

1. **No** `version.Version` **ldflag.** A real v0.15.0 binary reports `v0.15.0`, but this one reports a pseudo-version. Running `ovhcloud version` on the malicious build would have given it away.
2. **VCS stamping is present.** GoReleaser’s `-trimpath` strips the `vcs.*` metadata, so seeing it means someone ran a plain `go build` in a git checkout.
3. `vcs.modified=true` (the `+dirty` suffix). The working tree had uncommitted changes when it was built, so the malware was patched into a local checkout and never committed anywhere.
4. **Wrong commit.** The build is from `5ead8ef` (13 Oct, after v0.15.0’s `760fd72`), so it includes the API v2 instance migration from PRs #292 and #293 that v0.15.0 never had. It’s a v0.16-era tree wearing a v0.15.0 filename. `5ead8ef` was the tip of `main` from 13 Oct 08:35:05 UTC until `6ef70c2` merged on 16 Oct at 14:38:11 UTC. If the attacker built from current `main`, their last fetch came before that second time. A stale clone would also fit.

Klaba described the binary as looking for secrets stored on the user’s disk and called its quality mediocre but functional. OVHcloud hasn’t published what paths it reads or where it sends them. If you have a sample, the hash above will identify it.

## How it got in: a hijacked contributor account, not the build system

When a release gets tampered with, the first guess is usually CI, like a poisoned Action, a leaked workflow secret, or a tag pushed to trigger a build. The evidence rules that out here.

**The release workflow never ran.** `.github/workflows/release.yml` only fires on `push: tags: v*`. Tagger dates are set by whoever pushes, so we didn’t rely on them. The Actions run list is server-side. It shows no workflow run of any kind between 16 Oct 14:38:14 UTC and 19 Oct 16:00:23 UTC, which is the v0.16.0 tag push. A `v*` tag push on any of the older versions would have started the `release` workflow. Nothing ran during the replacement window, so GoReleaser was not invoked for these versions, which is also why the binary lacks GoReleaser’s ldflags. One caveat is that repo admins can delete workflow runs.

**The uploads came from a human account via the Releases API.** The reporter captured the uploader field on the replaced assets before deletion. It was `HassenBF`, not a bot, not a workflow identity, and not the `amstuta` account that originally published those releases. The account has merged pull requests in `ovh/ovhcloud-docs` and `ovh/manager`, but it isn’t a public member of the `ovh` org and has no commits in `ovh/ovhcloud-cli`. Uploading a release asset requires `contents: write`, so it had Write on the repo, most likely through the `@ovh/ovhcloud-cli-owners` team that `CODEOWNERS` grants `*`. Klaba confirmed this in his announcement, saying the attacker used one of the developers’ GitHub accounts and added a binary.

**The cadence looks like a script.** Five releases, six assets each, uploaded one at a time with `checksums.txt` last so the published hashes matched the new binaries, all inside 25 minutes. That’s most likely a loop over `DELETE /repos/{owner}/{repo}/releases/assets/{id}` and `POST .../releases/{id}/assets` with a token in hand.

### The account was already compromised

`HassenBF` has six public repositories, all personal learning projects. Four were force-pushed in March 2026. We got the push times from GitHub’s repository Activity API, which records every force push with the server’s timestamp. The commit’s own author and committer dates are set by the pusher, so we don’t use them.

Repository

Old tip

New tip

Force push (server time, UTC)

Author date on new tip

`treasure-hunt-game`

`0934f29d`

`8ac376cf`

2026-03-05 02:41:17

2020-01-20

`crwn-clothing`

`c9d20ea5`

`624c056a`

2026-03-05 02:41:23

2020-04-26

`next-dashboard`

`9cb916f1`

`227207ce`

2026-03-05 02:41:59

2024-12-11

`padel-bot`

`90368a08`

`d261665c`

2026-03-06 22:49:53

2025-07-28

A force push alone isn’t the indicator, because this account force-pushes routinely. `padel-bot` had seven in July 2025. What marks these four is that each new tip shares its parent with the old tip (the API reports `ahead_by 1, behind_by 1`), keeps the original author date and message, and carries the payload. It’s an amend. Three of the new tips (`treasure-hunt-game`, `next-dashboard`, `padel-bot`) add `preinstall.js` and a `"preinstall": "node preinstall.js"` entry to `package.json`. In `crwn-clothing` the same decoder is inlined into `src/index.js`, which grew from 262 bytes to 36,936.

The first three repositories were rewritten within 42 seconds, which looks like a script, not a person. The fourth followed about 44 hours later. The pushes came at 03:41 Paris time on 5 March and 23:49 on 6 March. The account’s other pushes cluster around 10:40 to 14:40 and 20:00 to 22:00 UTC, so the first push is outside its usual hours. That’s a weak signal.

The profile looked benign on a standard OSINT pass: no stealer-related stars, one commit email, activity consistent with Europe/Paris, and real contributions to OVH repositories. A clean-looking profile doesn’t rule out a hijacked account.

### The loader

All three `preinstall.js` files are byte-identical, and the `crwn-clothing` variant uses the same decoder. The visible code is a short decoder that maps Unicode variation-selector characters (U+FE00 to U+FE0F and U+E0100 to U+E01EF) back to bytes and passes the result to `eval`. The rest of the file looks empty because the payload is made of invisible characters.

We decoded it statically without executing anything. Stage one decrypts a hex blob with AES-256-CBC, and the key and IV sit in the same file (both are in the IOC table below).

Stage two is 4,407 bytes and does the following:

- Waits 10 seconds, then exits if the system looks Russian. The check requires a Russian language indicator together with a Russian timezone or a UTC offset between +2 and +12.
- Writes a throttle file named `init.json` into the home directory on macOS and re-runs at most every two days.
- Fetches that link with an `os` header, reads `ivbase64` and `secretkey` response headers, and `eval`s the response body. On Linux and Windows it runs inside a `vm` context with `require` exposed.
- Queries a list of public Solana RPC endpoints for the transaction signatures of wallet `BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC` and reads the memo field of the latest one. The memo is JSON containing a base64 `link`.

Because the next stage is delivered through the blockchain memo, the operator can change the payload URL at any time without touching the repositories.

### Attribution and the limits of the link

The Solana wallet appears in public GlassWorm indicator lists, including `trailofbits/vsix-audit`, `perplexityai/bumblebee`, `afine-com/glassworm-hunter` and `westackai/glassworm-scanner`. A `tstromberg/supplychain-attack-data` entry titled “forcememo-python-repos” matches the amend-and-force-push technique. We did not observe PolinRider markers or malicious workflow additions, so we don’t attribute this to PolinRider or GhostAction.

What we can’t prove is that whoever force-pushed those repositories on 5 March is the person who uploaded the binaries in October. The shared account is the link. The 5 March push is the earliest server-verified use of the account by the attacker, so it’s an upper bound on when they had a token. The theft could predate it. The account’s ordinary activity in `ovh/ovhcloud-docs` continues through September, and GitHub’s data can’t tell us whether the owner or the attacker was behind any given push. That includes the 15 October deletion of two branches, `test/trigger-probe` and `dev/test-changest`. Both were created by the account on 29 May and 7 September, and we read their deletion as cleanup, not reconnaissance. We also don’t know how the credentials were taken. An infostealer on the developer’s machine or a stolen token are the likeliest paths. The loader sitting in the developer’s own repositories means anyone who ran an install in them, including the owner, would have run it too.

Whichever it was, the attacker didn’t need the workflow’s own long-lived PAT (`TAP_GITHUB_TOKEN`, used in place of the ephemeral `GITHUB_TOKEN`) to pull this off. OVHcloud hasn’t said whether it was exposed. The reporter asked directly in #300, so hopefully the answer shows up in the post-mortem.

## Why it was cheap: mutable releases and human publishers

None of the following let the attacker in, but all of it made the attack easy once they were. It’s also all common, so check your own repos against this list.

Weakness

Where

Effect

Releases were mutable

GitHub default until “immutable releases” is turned on

Anyone with Write could delete and re-upload assets on a release published months earlier. Downstream installers fetched the new file from the same URL with no warning.

Overwriting is a normal operation

`.goreleaser.yaml`: `release: mode: keep-existing` and `replace_existing_artifacts: true`

Replacing assets on an existing release is the project’s own documented behaviour, so nothing about it looks anomalous in an audit log.

Releases published under personal accounts

v0.10.0 to v0.15.0 published by `amstuta` and later `FrostByte0x`, both humans

Every maintainer’s personal account is a release-signing key. Compromise one and you can publish.

Write access for a peripheral contributor

`HassenBF` could upload release assets without being a public org member or having commits in the repo

A contributor whose work is docs and tooling still held the permission that mattered most.

Long-lived PAT in the release workflow

`release.yml` passes `secrets.TAP_GITHUB_TOKEN` as `GITHUB_TOKEN`

A PAT with cross-repo write (it also pushes to `ovh/homebrew-tap`) sits in repo secrets indefinitely instead of the per-run `GITHUB_TOKEN`. Not used here, but a second path to the same outcome.

No provenance on binaries

No `checksums.txt` signature, no SLSA/GitHub attestation, no cosign, before v0.16.0

A consumer had no way to tell a GoReleaser artifact from a laptop build. The one person who noticed had hand-pinned a SHA-256 in their own CI.

Installers trust the release URL

`install.sh` downloads `releases/download/{tag}/{asset}` and runs `install`; the Homebrew cask does the same

Every install path except `go install` and Docker pulled the swapped file. `install.sh` does not verify `checksums.txt`, and the checksums were swapped anyway.

No private vulnerability reporting

Repo settings

The reporter had to disclose publicly in an issue, which is why we have the forensic detail at all.

OVHcloud’s v0.16.0 release addresses the first and third rows directly. It’s marked immutable, carries a GitHub release attestation, was tagged and signed by a maintainer’s key, and was published by the `ovh-cds` service account instead of a person. Those are the right fixes. We’d like to see the remaining rows covered in the post-mortem.

## Am I affected, and what to do

You are affected if, between 12:47 and 14:21 UTC on 19 October 2026, you installed or updated the OVHcloud CLI on macOS, Linux x86\_64/arm64 or Windows x86\_64 by any of these routes:

- `curl -fsSL https://raw.githubusercontent.com/ovh/ovhcloud-cli/main/install.sh | sh` (with or without a version argument; it fetches from the release URL)
- `brew install --cask ovh/tap/ovhcloud-cli` or `brew upgrade`
- A direct download from the GitHub Releases page for v0.11.0 to v0.15.0
- Any CI job or Dockerfile that fetches the tarball from `github.com/ovh/ovhcloud-cli/releases/download/`

You are not affected if you used `go install github.com/ovh/ovhcloud-cli/cmd/ovhcloud@latest`, built from source, pulled the `ovhcom/ovhcloud-cli` Docker image (built by OVHcloud’s internal CDS pipeline, not from GitHub assets), or installed before 12:47 UTC and did not update during the window. i386, Windows arm64 and WASM builds were not replaced.

To check a binary you still have:

1. `go version -m ./ovhcloud` (or `go version -m ovhcloud.exe`). A clean release build has no `vcs.*` lines and no `+dirty`. A line reading `vcs.modified=true` or a module version of `v0.15.1-0.20261013083505-5ead8ef9b43d+dirty` is the malicious build.
2. `./ovhcloud version`. Clean builds print the tag (`v0.15.0`); the malicious build was compiled without the version ldflag.
3. `sha256sum` of the archive against the table above, or against the clean checksums in the v0.16.0 release.

If you ran it, treat every secret readable from that machine as exposed. That includes OVHcloud API keys and consumer keys, `~/.ovh.conf`, cloud provider credentials, SSH keys, `.npmrc`/`.pypirc`/`.netrc` tokens, Kubernetes configs, and anything in a `.env`. Rotate from a different machine, then remove the binary and install v0.16.0 or later. OVHcloud’s own guidance says the same thing: change all secrets on the disk.

Going forward, pin hashes in CI and verify them. v0.16.0 ships a `Release attestation (json)` you can check with `gh attestation verify`.

### For OVHcloud

- Revoke every credential the `HassenBF` account could reach, including GitHub tokens, SSH keys and CDS secrets, and review what that account could do in the release process.
- Audit every ref and release asset the account touched since March 2026, across all OVH repositories. Review the `scripts/release.ts` and PDF build scripts it authored in `ovh/ovhcloud-docs`.
- Check the developer’s machine for GlassWorm persistence and for `~/init.json`.

### For defenders

- Alert on force pushes to long-idle repositories. The Activity API logs them with server timestamps, and a force push whose new tip shares the old tip’s parent is an amend. Commit dates can be faked, so don’t alert on them.
- Block or review `preinstall` scripts in anything you install, and flag files with long runs of variation-selector characters.
- Block outbound requests to Solana RPC endpoints from build hosts that have no reason to use them.

## Indicators of compromise

Type

Value

GitHub account (hijacked)

`HassenBF` (ID 4911006)

File

`preinstall.js`, SHA-256 `43df42fd79f6f81e530892b54634598770d6e496796a863c596e616bcb3fec70`

Inline variant

`src/index.js` in `HassenBF/crwn-clothing` at `624c056a`, variation-selector decoder plus `eval`

Decrypted stage two

SHA-256 `0f79989912572a24ba13baabb32b3fd084496271c51448d47b66fe1aedbf293c`

AES-256-CBC key

`zetqHyfDfod88zloncfnOaS9gGs90ONX`

AES IV

`a041fdaa0521fb5c3e26b217aaf24115`

Solana wallet (dead drop)

`BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC`

Local file

`~/init.json` (macOS throttle marker)

Package script

`"preinstall": "node preinstall.js"`

Replaced asset (original)

v0.15.0 `ovhcloud-cli_Linux_arm64.tar.gz` `5c2beb56e6d83a4b426565a1557791ef759316abcc4effb38dd627c90aeb80e0`

Replaced asset (malicious)

v0.15.0 `ovhcloud-cli_Linux_arm64.tar.gz` `3833daffcaaaab27e4e0e0833240ffcb1df8df648f4ec0bc4a75c176e28933cb`

Build metadata of replaced asset

`vcs.revision=5ead8ef9b43d354dfb5caadff803b11afc8c5c58`, `vcs.modified=true`

## Open questions

OVHcloud has promised a detailed post-mortem. These are the questions we still want answered, and we’ll update this post when we get them:

- **Initial access.** How were the `HassenBF` credentials taken in March 2026: infostealer, stolen token, something else? Was the dirty build made on the developer’s own machine or the attacker’s?
- **Dwell time.** Did the same actor hold the account from 5 March to 19 October, or did access change hands?
- **Token exposure.** Did the attacker also obtain `TAP_GITHUB_TOKEN` or any other org-level secret? Did anything change in `ovh/homebrew-tap`, which that token can write to?
- **The payload.** What does the binary read, and where does it send it? Sample hashes for the other eight replaced archives. Any command-and-control indicators.
- **Blast radius.** How many downloads of the replaced assets occurred in the 94-minute window, by platform? GitHub has these numbers.
- **Scope.** Klaba said first checks show no other OVHcloud repository affected. Which repos could the account write to, and was that checked by audit log or by hash?
- **The branch cleanup.** Who deleted `test/trigger-probe` and `dev/test-changest` on 15 October, and why then?

If you have a copy of any replaced archive, or download logs from the window, we’d like to hear from you.

## Sources

- [Issue #300: Release assets of v0.13.0–v0.15.0 replaced on 2026-10-19 with a dirty build of a later commit](https://github.com/ovh/ovhcloud-cli/issues/300), the reporter’s forensic write-up and maintainer responses
- [ovh/ovhcloud-cli](https://github.com/ovh/ovhcloud-cli): `.github/workflows/release.yml`, `.goreleaser.yaml`, `install.sh`, `CODEOWNERS`, tag objects (cloned 2026-10-19 UTC)
- GitHub release pages for [v0.10.0](https://github.com/ovh/ovhcloud-cli/releases/tag/v0.10.0), [v0.15.0](https://github.com/ovh/ovhcloud-cli/releases/tag/v0.15.0) and [v0.16.0](https://github.com/ovh/ovhcloud-cli/releases/tag/v0.16.0), including current asset lists and timestamps
- [HassenBF on GitHub](https://github.com/HassenBF): repository histories and commit metadata
- GlassWorm indicator lists: `trailofbits/vsix-audit`, `perplexityai/bumblebee`, `afine-com/glassworm-hunter`, `westackai/glassworm-scanner`, and the `tstromberg/supplychain-attack-data` “forcememo-python-repos” entry
- Octave Klaba’s announcement on X, 19 October 2026, as quoted by [cyberattaque.org](https://www.cyberattaque.org/ovhcloud-un-hacker-piege-plusieurs-versions-de-son-cli-officiel/) and [top10hebergeurs.com](https://www.top10hebergeurs.com/guide/infos-industrie/cli-ovhcloud-compromise-un-binaire-voleur-de-secrets-diffuse-ce-lundi-mettez-a-jour-ou-supprimez)
