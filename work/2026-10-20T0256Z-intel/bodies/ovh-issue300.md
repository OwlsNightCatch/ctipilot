---
title: "Release assets of v0.13.0–v0.15.0 replaced on 2026-10-19 with a dirty build of a later commit · Issue #300 · ovh/ovhcloud-cli"
author: Alink-Tothepast
url: https://github.com/ovh/ovhcloud-cli/issues/300
hostname: github.com
description: Hi, The release assets of v0.13.0, v0.14.0 and v0.15.0 were replaced today (2026-10-19, ~12:47–13:12 UTC), weeks after those releases were published. We noticed because our CI pins the SHA-256 of o...
sitename: GitHub
date: "2026-10-19"
categories: ['issue:5925117353']
fingerprint: fdef54bd596075c2
---
## Repository navigation

# Release assets of v0.13.0–v0.15.0 replaced on 2026-10-19 with a dirty build of a later commit #300

## Description

Hi,

The release assets of v0.13.0, v0.14.0 and v0.15.0 were replaced today (2026-10-19, \~12:47–13:12 UTC), weeks after those releases were published. We noticed because our CI pins the SHA-256 of `ovhcloud-cli_Linux_arm64.tar.gz` and started failing. Could you confirm whether this was intentional?

**What changed** (from the GitHub releases API):

| Release | Originally uploaded by | Replaced assets (uploader `HassenBF`) | 
|---|---|---|
| v0.15.0 (published 2026-09-16) | amstuta | Linux\_arm64, Linux\_x86\_64, Darwin\_arm64, Darwin\_x86\_64, Windows\_x86\_64, `checksums.txt` — 12:47–12:57 UTC | 
| v0.14.0 |  | Linux\_arm64 13:01, checksums 13:04 (others not checked) | 
| v0.13.0 |  | Linux\_arm64 13:08, checksums 13:11 (others not checked) | 

The i386 / Windows arm64 / wasm assets of v0.15.0 are untouched.

- v0.15.0 `ovhcloud-cli_Linux_arm64.tar.gz`: was `5c2beb56e6d83a4b426565a1557791ef759316abcc4effb38dd627c90aeb80e0`, now `3833daffcaaaab27e4e0e0833240ffcb1df8df648f4ec0bc4a75c176e28933cb`

**The new "v0.15.0" binary is not built from the v0.15.0 tag.** `go version -m ovhcloud` on the new Linux arm64 binary:

```
mod   github.com/ovh/ovhcloud-cli  v0.15.1-0.20261013083505-5ead8ef9b43d+dirty
build -ldflags="-s -w"
build vcs.revision=5ead8ef9b43d354dfb5caadff803b11afc8c5c58
build vcs.time=2026-10-13T08:35:05Z
build vcs.modified=true
```
So it is a local `go build` of a commit from 2026-10-13 (after the release, and including the instance API v2 migration from [#292](https://github.com/ovh/ovhcloud-cli/pull/292)/[#293](https://github.com/ovh/ovhcloud-cli/pull/293)) with **uncommitted changes**. It also lacks the `-X .../internal/version.Version` ldflag from `.goreleaser.yaml`, so it did not come from the release pipeline. The `v0.15.0` tag itself still points to `760fd72d`, and the Go module proxy serves that same commit.

`HassenBF` is not a public member of the `ovh` org and doesn't show up among the repo's contributors. That may just be a private membership, but together with the dirty build it seemed worth flagging rather than assuming.

If this was a legitimate rebuild, it would help to know why, and to have release assets treated as immutable (or new versions published instead). If it wasn't, the affected assets should probably be pulled.

We have switched to building from the module proxy in the meantime. There was no private vulnerability reporting channel enabled on this repo, hence a public issue. Happy to move it elsewhere if you prefer.

## Activity

1. Hi [@alink-tothepast](https://github.com/alink-tothepast) thank you for the report, we are on it.
Reacted by Laurent Humez
2. Hello,
Thanks for letting us know.
All binaries involved have been deleted at 16:21 GMT+2.
We will release a new version soon to make sure that people downloading the latest release have a fresh binary.
Thanks
Romain
3. Thanks for the quick cleanup, confirmed on our side: only the original assets remain on v0.13.0–v0.15.0. To decide how much to trust upcoming releases, could you share a bit more once you know? 
  - How were these uploads possible: a compromised account or token, or an internal rebuild that went wrong?
  - If an account or token was involved, did it also have write access to the repository itself (pushes, tags, workflows), and have you checked that nothing else was changed?
  - Are you planning to sign the release artifacts or publish provenance (e.g. GitHub artifact attestations or cosign) for the next release? That would let users check a binary independently of the release page.
Thanks again. Reacted by Maxime Quandalle
4. Hello, We have released a new version of the CLI, v0.16.0, tag is signed with my account.
This release is immutable, so the assets attached to it can be trusted.
A first communication has been done here: [https://x.com/olesovhcom/status/2112225308589834260](https://x.com/olesovhcom/status/2112225308589834260)
A more detailed post-mortem will be released in the coming days. Sorry for the inconvenience,
Romain
Reacted by Nikolai Mishin and Alink Tothepast

## FrostByte0x commentedon Oct 19, 2026 

## rbeuque74 commentedon Oct 19, 2026 

## alink-tothepast commentedon Oct 19, 2026 

## rbeuque74 commentedon Oct 19, 2026 

to join this conversation on GitHub.Already have an account? Sign in to comment
