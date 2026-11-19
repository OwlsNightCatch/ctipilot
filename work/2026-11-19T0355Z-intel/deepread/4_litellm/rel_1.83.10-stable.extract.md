---
title: Release v1.83.10-stable · BerriAI/litellm
url: https://github.com/BerriAI/litellm/releases/tag/v1.83.10-stable
hostname: github.com
description: Verify Docker Image Signature All LiteLLM Docker images are signed with cosign. Every release is signed with the same key introduced in commit 0112e53. Verify using the pinned commit hash (recommen...
sitename: GitHub
date: "2026-04-27"
categories: ['repository:671269505']
fingerprint: "3f14179a207e7781"
---
## Repository navigation

# v1.83.10-stable

## Verify Docker Image Signature

All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). Every release is signed with the same key introduced in [commit `0112e53`](https://github.com/BerriAI/litellm/commit/0112e53046018d726492c814b3644b7d376029d0).

**Verify using the pinned commit hash (recommended):**

A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the original signing key:

```
cosign verify \
  --key https://raw.githubusercontent.com/BerriAI/litellm/0112e53046018d726492c814b3644b7d376029d0/cosign.pub \
  ghcr.io/berriai/litellm:v1.83.10-stable
```
**Verify using the release tag (convenience):**

Tags are protected in this repository and resolve to the same key. This option is easier to read but relies on tag protection rules:

```
cosign verify \
  --key https://raw.githubusercontent.com/BerriAI/litellm/v1.83.10-stable/cosign.pub \
  ghcr.io/berriai/litellm:v1.83.10-stable
```
Expected output:

```
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key
```
**Full Changelog**: `v1.83.10-nightly...v1.83.10-stable`
