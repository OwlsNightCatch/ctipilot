---
title: "Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines | Wiz Blog"
author: Rami McCarthy; Scott Piper; Benjamin Read
url: https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi
hostname: wiz.io
description: On November 17, 2026 at 20:35 UTC, versions 1.26.1 & 1.26.2 of the Microsoft PyPI package agent-framework were published with an added credential stealer. The package gets almost 200k downloads a month. The malicious versions have since been quarantined.
sitename: wiz.io
date: "2026-11-17"
tags: ['Research', 'Threat Intel']
fingerprint: "3c0eae8902c96443"
---
At 20:35 UTC on November 17, 2026, a malicious version (`1.26.1`) of the `agent-framework` package (Microsoft Agent Framework) was uploaded to PyPI. A second version, `1.26.2`, followed at 21:08 UTC. As of 21:30 UTC, both versions were no longer available on PyPI. The package gets about 41,000 downloads a week.

**The most recent safe version is 1.26.0.**

When a malicious version is installed, it drops a `.pth` file into the site-packages root (`agent_framework_meta.pth` in 1.26.1, `af_runtime_diag.pth` in 1.26.2). Python runs `.pth` files on every interpreter start, so the credential stealer runs whenever Python starts in that environment, even if `agent-framework` is never imported.

The root cause hasn't been confirmed. What we know so far:

- There is no python-1.26.1 tag or release in `microsoft/agent-framework`, and the main branch doesn't contain the malicious code.
- Legitimate releases publish a wheel and an sdist together with `agent-framework-core` of the same version. 1.26.1 was a wheel only, and still depends on agent-framework-core\[all\]==1.26.0.

This indicates 1.26.1 may have been built outside the project's normal release process and uploaded directly to PyPI.

Earlier this year, another Microsoft Python package, [durabletask](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack), was compromised after its PyPI token was stolen. We have not linked the two incidents.

| Time | Event | 
|---|---|
| 2026-11-12 18:25 | Legitimate 1.26.0 published (wheel + sdist, alongside agent-framework-core 1.26.0) | 
| 2026-11-17 20:35 | Malicious 1.26.1 published | 
| 2026-11-17 \~21:08 | Malicious 1.26.2 published | 
| 2026-11-17 \~21:30 | 1.26.1 & 1.26.2 no longer available on PyPI | 

`agent_framework_meta.pth` contains one line: `import agent_framework_meta`

In 1.26.1, `agent_framework_meta/__init__.py` then calls `_telemetry._start()`. The stealer forks into a detached session (`os.setsid())`, or falls back to a daemon thread where fork isn't available. It sets `_AF_TEL=1` to avoid running again in child processes.

The file and function names (`_telemetry`, "Lightweight runtime diagnostics hook", user-agent `af-runtime-diagnostics/1`) are made to look like legitimate SDK telemetry.

The stealer is focused on Azure and Azure DevOps. It collects:

- **Environment variables** with names containing strings such as TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, HF\_, FOUNDRY, NPM, PIP, NUGET, SYSTEM, BUILD, AGENT
- **Other processes' environments**: secret-looking values read from up to 300 /proc/\*/environ files
- **Credential files** (up to 60):
  - Azure CLI (\~/.azure/)
  - .npmrc, pip.conf, .netrc, .git-credentials, .docker/config.json
  - Hugging Face tokens
  - Azure DevOps agent .credentials
  - .env and JSON files under /app and /workspace
- **Azure DevOps OIDC tokens**: if `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` are set, it requests an OIDC token for `api://AzureADTokenExchange`
- **Azure managed-identity tokens** from IMDS or the App Service identity endpoint for 12 resources: ARM, Graph, Key Vault, Storage, Cognitive Services, Azure AI/ML, Search, Container Registry, Azure DevOps, and AzureADTokenExchange
- **Azure instance metadata**

Everything is put into one JSON document, zlib-compressed, base64-encoded, and sent in one HTTPS POST to `webhook[.]site`. The URL is hardcoded and the payload has no fallback channel. Failures are silently ignored and not retried.

`1.26.2` was uploaded at 21:08 UTC, 33 minutes after 1.26.1. It is a repacked `1.26.1` that sends to the same webhook.site URL, with these changes:

- **New trigger.** `agent_framework_meta/__init__.py` is restored to the clean 1.26.0 file. Instead, a new top-level `af_runtime_diag.pth` imports a new top-level module, `af_runtime_diag.py`, which starts the stealer as soon as it is imported. Searching only for the 1.26.1 file names will miss this version.
- **GitHub Actions OIDC theft.** In workflows with id-token: write, it requests OIDC tokens for `api://AzureADTokenExchange` and https://management.azure.com/. Where an Entra ID federated credential trusts the workflow, these tokens can be exchanged for Azure access, with no stored secret needed.
- **Wider collection.** Environment-variable matching now includes ACTIONS, OIDC, RUNNER and ARM\_. GitHub-hosted runner paths (`/home/runner/work/_temp/*`, `/home/runner/.azure/`) were added, and the file cap rose from 60 to 80.
- **New User-Agent:** `runtime-diagnostics/1`

webhook.site is a public request-inspection service. On its free tier, a URL that isn't attached to an account:

**We have confirmed the attackers token was on the free tier, and a maximum of 50 requests were captured.** However, those requests can contain working cloud, CI and registry credentials.

| Indicator | Description | Type | 
|---|---|---|
| [https://webhook\[.\]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb](https://webhook%5B.%5Dsite/d381fd80-ec62-42ad-8f5c-d1b15103c9bb) | Exfiltration endpoint (?t=telemetry) | Network | 
| af-runtime-diagnostics/1 | Exfil User-Agent (1.26.1) | Network | 
| runtime-diagnostics/1 | Exfil User-Agent (1.26.2) | Network | 
| agent\_framework\_meta.pth | Persistence hook in site-packages (1.26.1) | Host | 
| agent\_framework\_meta/\_telemetry.py | Credential stealer (1.26.1) | Host | 
| af\_runtime\_diag.pth | Persistence hook in site-packages (1.26.2) | Host | 
| af\_runtime\_diag.py | Credential stealer (1.26.2) | Host | 
| \_AF\_TEL=1 | Run-once environment variable | Host | 
| 0a013e4724c4437cf9b177def1d988113e167539 | \_telemetry.py (SHA1) | Hash | 
| 54d885b7d7161c9ed96489c66364c4bfbf635929166843bba10d97d46b5a2e1f | af\_runtime\_diag.py (SHA256) | Hash | 
| 325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93 | af\_runtime\_diag.pth (SHA256) | Hash | 

| File | SHA256 | 
|---|---|
| agent\_framework-1.26.1-py3-none-any.whl | d27fa34414e6201d5e03e559ef634f020057554d7b3f4898dd5d7cd3e989e110 | 
| agent\_framework-1.26.2-py3-none-any.whl | 3d20a8bc91351a9a16b6db243b848ceca0206b7a8623b02d2af553a9c9f7e0a9 | 

Wiz customers should refer to the [Wiz Threat Intelligence Center advisory](https://app.wiz.io/boards/threat-center/wiz-adv-2026-214) on this incident.

- **Identify exposure:** search lockfiles, CI logs, virtualenvs and container images for agent-framework 1.26.1 or 1.26.2. Pin to 1.26.0.
- **Check for execution**: look in site-packages for `agent_framework_meta.pth` and `agent_framework_meta/_telemetry.py` (1.26.1), or `af_runtime_diag.pth` and `af_runtime_diag.py` (1.26.2). Any Python process started in that environment ran the payload.
- **Check egress:** search proxy and DNS logs for `webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb`. A 200 means that host's data was accepted. A 410/429 suggests it was rejected.
- **Rotate credentials** on affected hosts and runners:
  - every secret that was in the environment
  - Azure CLI sessions, Azure DevOps PATs and service connections, npm/PyPI/NuGet/Docker/Hugging Face tokens, git credentials
- **Audit Azure identities:** review sign-in and activity logs for managed identities and federated credentials (workload identity federation) that were reachable from affected VMs, App Services, AKS nodes or ADO pipelines. Stolen managed-identity and OIDC-exchanged tokens are valid for up to 24 hours.
- **Audit GitHub Actions (1.26.2):** for workflows that installed 1.26.2 with `id-token: write`, treat GitHub OIDC tokens for `api://AzureADTokenExchange` and https://management.azure.com/ as exposed. Review the Entra ID federated credentials that trust those repositories and workflows, and sign-ins for the matching app registrations. Rotate repository and organization secrets that were exposed to the job.

For longer-term hardening guidance, see [Practical Package Security: The Unofficial Guide](https://www.wiz.io/blog/practical-package-security-the-unofficial-guide).
