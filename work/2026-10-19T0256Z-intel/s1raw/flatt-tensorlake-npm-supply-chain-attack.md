---
title: "Software Supply Chain Attack on tensorlake: Overview and Response Guidance"
url: https://flatt.tech/research/posts/tensorlake-npm-supply-chain-attack/
hostname: flatt.tech
description: Note) This post is a direct translation of this post . On October 8, 2026, malicious code was injected into the npm package tensorlake. The injected malicious code is malware with infostealer functionality. Executed via a preinstall hook, it has been observed stealing credentials for AWS, GitHub, Kubernetes, Vault, etc. and exfiltrating them. In addition, a background service spawned by the malware periodically checks whether the stolen GitHub token is still valid, and if it detects that the token has become invalid — for example, because it was rotated as part of the initial response — it has been observed deleting files on the infected host. Therefore, first back up your data so that you are covered even if files get deleted, and then disable that service before rotating the stolen tokens.
sitename: GMO Flatt Security Research
date: "2026-10-08"
categories: ['posts']
tags: ['Security', 'Supply Chain', 'Npm', 'Malware', 'Infostealer', 'C2']
fingerprint: "92461c78f66cc47"
---
# Software Supply Chain Attack on tensorlake: Overview and Response Guidance

##### Posted on October 8, 2026 • 3 minutes • 509 words

## Table of contents

Note) This post is a direct translation of [this post](https://blog.flatt.tech/entry/tensorlake_compromise)
.

On October 8, 2026, malicious code was injected into the npm package `tensorlake`.

The injected malicious code is malware with infostealer functionality. Executed via a `preinstall` hook, it has been observed stealing credentials for AWS, GitHub, Kubernetes, Vault, etc. and exfiltrating them. In addition, a background service spawned by the malware periodically checks whether the stolen GitHub token is still valid, and if it detects that the token has become invalid — for example, because it was rotated as part of the initial response — it has been observed deleting files on the infected host. Therefore, first back up your data so that you are covered even if files get deleted, and then **disable that service before rotating the stolen tokens**.

This article goes into detail on this malicious package based on information we observed and analyzed on the analysis infrastructure behind Takumi Guard, focusing on its impact as well as the countermeasures to take.

The purpose of this article is to help readers understand the situation and respond; it is not intended to assist or encourage any illegal activity.

Some descriptions may contain inaccuracies. Please bear in mind that we have prioritized getting this report out quickly.

## TL;DR — Response Guidance

- If you ran `npm install` for `tensorlake@0.5.144`, your environment may be infected with malware. The safe version is `0.5.143` (you can confirm that it has no `preinstall` script with `npm view tensorlake@0.5.143 scripts`).
- Immediate actions:
  1. The malware runs a background service called `gh-token-monitor`. This service periodically checks whether the GitHub token it obtained is still valid, and if it detects that the token has become invalid, it has been observed deleting files on the infected host. Therefore, first back up your data.
  2. Stop the service (`gh-token-monitor`).
  3. Rotate the passwords saved in your browsers. We have observed HackBrowserData being used to steal all passwords saved in the browser in JSON format.
  4. **Immediately rotate** the AWS IAM credentials (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`) of any environment where the package was installed. AWS SSM Parameter Store and Secrets Manager were enumerated and read across all regions. Also revoke and reissue GitHub tokens (anything obtainable via `gh auth token`, the `GITHUB_TOKEN` in GitHub Actions, and PATs in the `ghp_`/`gho_` format). Sensitive files on the installation environment’s filesystem — SSH private keys, `.env`, `.npmrc`, Docker config, Kubernetes config, Vault tokens, and so on — were targeted for reading. Take stock of the potential impact and reissue all of them.

Persistence: on Windows environments, there are traces of this malware registering an ONLOGON task via `schtasks.exe`.

## How the Compromise Works

We are currently investigating the detailed behavior and will update this post with details later.

## IoCs

### Hashes (SHA-256)

| File | Hash | 
|---|---|
| `artifact.tar.gz` | `33108f494dad71369a9aa7cd6daa5402335d1a718b78320b9b687c0b2174fa67` | 
| `lib/setup.mjs` | `25a0735d0db7dc40e5d45ce42d9c106067e6a66e184d967cfecfab17c3bcb5ef` | 
| `lib/Math_Symbol.js` | `b50a00900399ba99fb6ce1fc151519cb99d44320ef2a631f2237e1aea0ad6fec` | 
| `package.json` | `4aa26f2a54ac8d93aa702d87c415b059f42d688cd4b9b99095f93ee07693bbbe` | 

### Network

| Type | Value | Notes | 
|---|---|---|
| Domain | `iseekaigogo.com` | Primary C2 | 
| IP | `172.67.207.33` | Cloudflare IP for `iseekaigogo.com` | 
| IP | `104.21.22.217` | Cloudflare IP for `iseekaigogo.com` | 
| Domain | `eth.llamarpc.com` | Ethereum RPC (for ENS-based C2 resolution) | 
| Domain | `rpc.ankr.com` | Ethereum RPC (for ENS-based C2 resolution) | 
| Domain | `ethereum.publicnode.com` | Ethereum RPC (for ENS-based C2 resolution) |
