---
title: Microsoft agent-framework Compromised Twice on PyPI
author: SafeDep Team
url: https://safedep.io/blog/microsoft-agent-framework-pypi-compromise
hostname: safedep.io
description: agent-framework 1.26.1 and 1.26.2 on PyPI steal CI secrets and mint Azure and GitHub OIDC tokens from a .pth startup hook. Timeline, code and IOCs.
sitename: SafeDep
date: "2026-11-18"
tags: ['supply-chain', 'pypi', 'malware', 'credential-stealer', 'azure', 'threat-intel']
fingerprint: "3c946d43e6804297"
---
# Microsoft agent-framework Compromised Twice on PyPI

On this page

Two releases of `agent-framework`, Microsoft’s official Python metapackage for its Agent Framework, steal credentials from any environment that installs them. Nothing has to import the package. A `.pth` file runs the stealer each time Python starts, so a `pip install` in a CI job is enough. It takes environment variables and credential files. It also asks Azure DevOps, Azure managed identity and, in the second release, GitHub Actions for fresh tokens, and sends those out too.

SafeDep flagged version 1.26.1 22 minutes after it was published on 17 November 2026. By then the attacker was close to publishing again. Once 1.26.1 came off PyPI, 1.26.2 shipped the same stealer under different file names, and SafeDep flagged it 4 minutes after upload. Removing one version did not stop an attacker who could still publish. The last clean release is 1.26.0.

## Affected versions

| Version | Files | Wheel SHA-256 | Status | 
|---|---|---|---|
| **1.26.1** | wheel only, 10,402 bytes | `d27fa344…3e989e110` | Malicious, removed from PyPI | 
| **1.26.2** | wheel only, 10,449 bytes | `3d20a8bc…a9c9f7e0a9` | Malicious, removed from PyPI | 
| 1.26.0 | wheel and sdist | `14267ec8…199b6d71` | Last clean release | 

The project is published under the `microsoft` account on PyPI and gets about 192,000 downloads a month. How many installs the two bad versions got is not known yet.

## Timeline

## How the releases differed from real ones

Every release from 1.20.0 through 1.26.0 shipped a wheel and an sdist. Both malicious versions are a single wheel. The 1.26.1 wheel is 10,402 bytes, up from 6,681 in 1.26.0. A metapackage that always shipped both files now ships one.

Missing provenance does not set the bad wheels apart. PyPI has no attestation for 1.26.0 either, so a consumer had no cryptographic way to tell Microsoft’s uploads from the attacker’s.

How the attacker got publishing access is not known yet. This is the second Microsoft package on PyPI to get rogue releases in six months. In May, [durabletask 1.4.1 to 1.4.3](https://safedep.io/blog/malicious-durabletask-pypi-supply-chain-attack) were uploaded with a stolen API token and had no matching commits or tags. The payloads and infrastructure share nothing, so there is no evidence the two incidents are linked.

## How the payload runs

Python’s `site` module executes any line beginning with `import` in a `.pth` file under `site-packages` at interpreter startup. 1.26.1 ships `agent_framework_meta.pth`, a 28-byte file holding one line. Hashing that line plus a newline reproduces the file’s SHA-256 (`21f28e85…98eb5e`).

That import runs `agent_framework_meta/__init__.py`, where 1.26.1 appends a hook to the otherwise clean file.

`_start()` sets `_AF_TEL` so child interpreters skip it, then forks and detaches with `setsid()`. The host process returns at once, so a test run or build shows no delay. Where `fork` is missing, it uses a daemon thread.

The same shape, a one-line `.pth` that imports a module which forks a collector, appeared in [LiteLLM 1.107.0](https://safedep.io/blog/litellm-pypi-compromise-credential-stealer-backdoor) in October.

## What it steals

The collector works through four sources.

1. **Environment variables** whose names contain any of 31 substrings, including `TOKEN`, `SECRET`, `KEY`, `AZURE`, `AWS`, `GITHUB`, `HF_`, `OPENAI`, `NPM`, `PIP`, `SYSTEM` and `BUILD`. Each value is kept up to 8,000 characters.
2. **Credential files**, up to 60 under 256 KB each. These cover Azure CLI JSON under `~/.azure` and `/home/*/.azure`, `pip.conf`, `.npmrc`, `.netrc`, `.git-credentials`, Docker `config.json`, the Hugging Face token, the Azure AI Foundry configuration, and Azure DevOps self-hosted agent `.credentials` under `_work`, `vss-agent` and `/mnt/azure_nvme_temp` paths. It also takes `/app/.env`, `/app/*.json`, `/workspace/.env` and `~/.config/*/token*.json`.
3. **Other processes’ environments**, from up to 300 `/proc/<pid>/environ` files. On a shared or self-hosted runner, that reaches secrets belonging to other jobs.
4. **New tokens it requests from the platform**, covered in the next section.

It also records the hostname, user, working directory and `sys.argv`.

## Tokens it requests

Besides reading credentials already on disk, the code asks the platform to issue new ones. Rotating stored secrets does not cover those.

In an Azure DevOps pipeline, `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` are enough to request a federated token for `api://AzureADTokenExchange`. That is the token a pipeline uses to sign in to Azure through a workload identity federation service connection.

On Azure compute, it asks the managed identity endpoint for an access token to each of these resources. It uses `IDENTITY_ENDPOINT` or `MSI_ENDPOINT` on App Service and Functions, and `169.254.169.254` elsewhere. It also pulls instance metadata.

`499b84ac-1321-427f-aa17-267ca6975798` is the Azure DevOps resource ID. A workload with a managed identity hands over tokens for Resource Manager, Key Vault, Storage, Graph and Azure DevOps, scoped to whatever that identity can reach.

## Exfiltration

The endpoint is base64 in `_ENC` and decodes to `hxxps://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb`. `_post()` compresses the collected JSON with zlib, base64-encodes it and sends it with a 25-second timeout. Errors are swallowed.

The data goes to `?t=telemetry`. A webhook.site bin is anonymous and needs no infrastructure, which leaves the URL as the only network indicator. Proxy and egress logs that show a POST to it mark the hosts that sent data.

## What changed in 1.26.2

1.26.2 restores `agent_framework_meta/__init__.py` to the clean file. Its SHA-256 (`5f04333f…49f1`) matches the one in the 1.26.0 wheel. The stealer moves into a new top-level module that starts itself on import.

|  | 1.26.1 | 1.26.2 | 
|---|---|---|
| Startup file | `agent_framework_meta.pth` (28 bytes) | `af_runtime_diag.pth` (23 bytes) | 
| Stealer | `agent_framework_meta/_telemetry.py` | `af_runtime_diag.py` | 
| `agent_framework_meta/__init__.py` | hook appended | same as 1.26.0 | 
| User-Agent | `af-runtime-diagnostics/1` | `runtime-diagnostics/1` | 
| GitHub Actions OIDC | no | yes | 
| Webhook | `d381fd80-…` | `d381fd80-…` | 

As with 1.26.1, hashing the one line plus a newline reproduces the published SHA-256 of the startup file (`325e7e9f…7f452f93`).

A check for 1.26.1’s file names or hashes misses 1.26.2. The webhook is the one indicator both share.

The new GitHub Actions block requests ID tokens for the two audiences Azure federated credentials accept. Any job with `id-token: write` that installed 1.26.2 handed both over.

The rest of the collector is unchanged. The release went up after 1.26.1 had been removed, so whoever controls the publishing path still held it at 21:08.

## Check your environments

Look for the versions in lockfiles and requirement files.

On machines, images and runners, look for either startup file without starting the environment’s Python. Starting it would run the stealer again.

Treat every secret reachable from an environment that installed either version as exposed. That covers environment secrets, Azure CLI sessions, and Azure DevOps PATs and service connections. It also covers PyPI, npm, NuGet, Docker and Hugging Face tokens, git credentials, and secrets of other jobs on the same self-hosted runner. Rotation does not undo the tokens it had issued. Review sign-in and activity logs for the managed identities and federated credentials that environment could use, from the install time onward. Pin `agent-framework==1.26.0` with `--require-hashes`, and hold off on any newer release until Microsoft confirms it is clean.

## Indicators of compromise

| Row | type | value | package | context | first\_seen\_utc | 
|---|---|---|---|---|---|
| 1 | pypi\_package\_version | agent-framework==1.26.1 | agent-framework | Malicious release; wheel only; payload runs at every Python start via agent\_framework\_meta.pth | 2026-11-17T20:35:20Z | 
| 2 | pypi\_package\_version | agent-framework==1.26.2 | agent-framework | Malicious release; wheel only; payload moved to af\_runtime\_diag.pth and af\_runtime\_diag.py | 2026-11-17T21:08:39Z | 
| 3 | sha256 | d27fa34414e6201d5e03e559ef634f020057554d7b3f4898dd5d7cd3e989e110 | agent-framework | agent\_framework-1.26.1-py3-none-any.whl (10402 bytes) | 2026-11-17T20:35:20Z | 
| 4 | sha256 | 21f28e8517a10ffe431f8d68f5875c85eca4001ae6d118322b0a41873998eb5e | agent-framework | agent\_framework\_meta.pth @ 1.26.1 (28 bytes) | 2026-11-17T20:35:20Z | 
| 5 | sha256 | c275ccbe520ef3c0f02dc6a35389e427f9f1b4e0b12e140cd7bf7179ce143f02 | agent-framework | agent\_framework\_meta/\_\_init\_\_.py @ 1.26.1 (calls \_telemetry.\_start) | 2026-11-17T20:35:20Z | 
| 6 | sha256 | 39fa329f2a93f734b0bb8f5adb203ea3331d1ae479832a5015a54cb17aabd663 | agent-framework | agent\_framework\_meta/\_telemetry.py @ 1.26.1 (stealer) | 2026-11-17T20:35:20Z | 
| 7 | sha256 | 3d20a8bc91351a9a16b6db243b848ceca0206b7a8623b02d2af553a9c9f7e0a9 | agent-framework | agent\_framework-1.26.2-py3-none-any.whl (10449 bytes) | 2026-11-17T21:08:39Z | 
| 8 | sha256 | 325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93 | agent-framework | af\_runtime\_diag.pth @ 1.26.2 (23 bytes) | 2026-11-17T21:08:39Z | 
| 9 | sha256 | 54d885b7d7161c9ed96489c66364c4bfbf635929166843bba10d97d46b5a2e1f | agent-framework | af\_runtime\_diag.py @ 1.26.2 (stealer) | 2026-11-17T21:08:39Z | 
| 10 | url | hxxps://webhook\[.\]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb?t=telemetry | agent-framework | Exfiltration endpoint in both versions (base64 constant \_ENC) | 2026-11-17T20:35:20Z | 
| 11 | user\_agent | af-runtime-diagnostics/1 | agent-framework | Exfiltration User-Agent @ 1.26.1 | 2026-11-17T20:35:20Z | 
| 12 | user\_agent | runtime-diagnostics/1 | agent-framework | Exfiltration and GitHub OIDC request User-Agent @ 1.26.2 | 2026-11-17T21:08:39Z | 
| 13 | env\_var | \_AF\_TEL | agent-framework | Run-once marker set by \_start() in both versions | 2026-11-17T20:35:20Z | 

## References

- supply-chain
- pypi
- malware
- credential-stealer
- azure
- threat-intel
