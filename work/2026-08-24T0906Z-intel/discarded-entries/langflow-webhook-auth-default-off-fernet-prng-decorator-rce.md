---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — three more Langflow paths: webhook authentication that shipped off by default for three minor releases, a credential key derived from a non-cryptographic PRNG, and a code-validation endpoint that runs decorators"
headline: "The product with three already-exploited pre-auth paths adds a webhook endpoint that was public by default across three releases"
summary: >
  Langflow published three security advisories on 2026-08-12, carried by BSI's CERT-Bund the following day, all
  distinct from the auto-login and code-validation flaw this pipeline covered on 2026-08-05 when it reached the CISA
  exploited-vulnerabilities catalog. The webhook authentication path skipped API-key validation entirely whenever
  WEBHOOK_AUTH_ENABLE was false — the shipped default from v1.7.0 through v1.9.0 — so anyone who knows a flow's UUID
  could execute that flow as its owner, reaching code execution through components that run Python. Separately,
  Langflow derived the Fernet key protecting every stored credential either by seeding Python's Mersenne Twister with
  the SECRET_KEY or by using that key's raw bytes, so an attacker who reads the secret_key file decrypts every stored
  provider key and database password offline with no brute force. No CVE identifiers have been assigned to any of the
  three.
discovered_at: "2026-08-14T05:02:00Z"
event_date: "2026-08-12"
run_id: 2026-08-14T0417Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - pre-auth
  - rce
  - default-config
  - patch-available
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
  - technology
entities: []
techniques:
  - T1190
  - T1059.006
  - T1552.001
  - T1552.004
affected_products:
  - "Langflow"
cves: []
sources:
  - url: "https://github.com/langflow-ai/langflow/security/advisories/GHSA-cf6m-vc3m-7cgm"
    publisher: "Langflow (GHSA-cf6m-vc3m-7cgm)"
    date: "2026-08-12"
    role: primary
  - url: "https://github.com/langflow-ai/langflow/security/advisories/GHSA-jxw3-mjmx-3pqm"
    publisher: "Langflow (GHSA-jxw3-mjmx-3pqm)"
    date: "2026-08-12"
    role: primary
  - url: "https://github.com/langflow-ai/langflow/security/advisories/GHSA-w584-2h2r-2hvf"
    publisher: "Langflow (GHSA-w584-2h2r-2hvf)"
    date: "2026-08-12"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2828"
    publisher: "BSI CERT-Bund"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This allows a remote attacker who knows a flow's UUID to execute it as if they were the owner, potentially leading to Remote Code Execution (RCE) or Denial of Service (DoS)."
    publisher: "Langflow (GHSA-cf6m-vc3m-7cgm)"
  - quote: "By default (v1.7.0 through v1.9.0), Langflow treats `WEBHOOK_AUTH_ENABLE` as `False`, meaning all webhook endpoints are public."
    publisher: "Langflow (GHSA-cf6m-vc3m-7cgm)"
  - quote: "An attacker who obtains the `SECRET_KEY` (e.g., via the MCP path traversal in this repo) can reconstruct the exact Fernet key offline and decrypt every credential stored in the database with no brute force required."
    publisher: "Langflow (GHSA-jxw3-mjmx-3pqm)"
verification: multi-source
sourcing_note: "The three advisories are the vendor's own; BSI CERT-Bund's WID-SEC-2026-2828 republishes them for German constituents rather than assessing them independently, so corroboration confirms distribution, not a second assessment. No CVE identifiers had been assigned when this entry was composed — cite the advisory identifiers."
confidence: high
update_of: 2026-08-05/cve-2026-9198-langflow-auto-login-validate-code-kev
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Langflow to v1.10.1 — it is the release that fixes both the Fernet key derivation and the code-validation sink, and v1.9.1 (which fixes only the webhook default) is not sufficient. On instances that ran a SECRET_KEY shorter than 32 characters, re-enter every stored credential after upgrading: the vendor states the new derivation produces a different key, and any credential encrypted under the old one should be treated as recoverable by anyone who ever read the secret_key file."
migrated_from: null
---

**UPDATE (originally covered 2026-08-05):** Langflow disclosed three further security advisories on 2026-08-12, republished by BSI's CERT-Bund on 2026-08-13. All three are distinct root causes from CVE-2026-9198, the auto-login-to-code-validation path that CISA added to its Known Exploited Vulnerabilities catalog and that this pipeline covered on 2026-08-05.

**The webhook path was public by design for three minor releases.** Langflow's webhook authentication logic skipped API-key validation whenever the `WEBHOOK_AUTH_ENABLE` setting was false, and the vendor is explicit that ["By default (v1.7.0 through v1.9.0), Langflow treats `WEBHOOK_AUTH_ENABLE` as `False`, meaning all webhook endpoints are public"](https://github.com/langflow-ai/langflow/security/advisories/GHSA-cf6m-vc3m-7cgm) — the setting was introduced in v1.7.0 with that default, leaving the only barrier the secrecy of a flow's UUID, which the advisory itself calls security by obscurity. The consequence is that ["This allows a remote attacker who knows a flow's UUID to execute it as if they were the owner, potentially leading to Remote Code Execution (RCE) or Denial of Service (DoS)"](https://github.com/langflow-ai/langflow/security/advisories/GHSA-cf6m-vc3m-7cgm), because Langflow flows can contain components that run arbitrary Python. The affected range is `>= 1.7.0, <= 1.9.0`, and v1.9.1 changes the default to true.

**The credential-encryption key is reproducible from the secret file.** Langflow derived the Fernet key protecting all stored user credentials — provider API keys, database passwords — from the `SECRET_KEY` in one of two ways, and both are recoverable: when the secret is shorter than 32 characters it seeds Python's `random` module, a Mersenne Twister and not a cryptographic generator, and when it is 32 characters or longer the raw key material is used directly as the Fernet key. Langflow rates this Critical at CVSS 9.1 and states that ["An attacker who obtains the `SECRET_KEY` (e.g., via the MCP path traversal in this repo) can reconstruct the exact Fernet key offline and decrypt every credential stored in the database with no brute force required"](https://github.com/langflow-ai/langflow/security/advisories/GHSA-jxw3-mjmx-3pqm) — and names a path-traversal flaw in the same product as a way to read that file. Everything at or below v1.10.0 is affected; v1.10.1 derives the key with SHA-256 instead, keeping backward-compatible decryption of old ciphertext through a multi-key construction so migration works, and the vendor notes that deployments whose secret was under 32 characters must re-enter stored credentials afterwards.

**The third is the same sink as the already-exploited flaw, reached a different way.** The `/api/v1/validate/code` endpoint compiled and executed submitted function definitions to surface syntax errors, and while executing a definition does not run the function body, Python evaluates decorators at definition time — so a submitted function carrying a malicious decorator executes immediately during what the product calls validation. Langflow records that this endpoint had no authentication at all before v1.7.2, that from v1.7.2 through v1.10.0 it required a session but the execution sink was untouched, and that under `AUTO_LOGIN` any caller reaches it regardless; the fix in v1.10.1 compiles without executing, which also resolves a duplicate advisory reporting the same sink reached through default-argument evaluation ([Langflow GHSA-w584-2h2r-2hvf, 2026-08-12](https://github.com/langflow-ai/langflow/security/advisories/GHSA-w584-2h2r-2hvf)).

**Detection.** All three converge on one observable: the Langflow API worker process executing something. In process-creation telemetry with parent lineage, a child process spawned by the Langflow server process — a shell, an interpreter, a network utility — is the durable signal across the webhook path, the decorator path and the already-exploited auto-login path alike, because in normal operation the API worker serves HTTP and does not fork. In egress telemetry, outbound connections originating from the Langflow host to destinations outside its configured model providers are the second hook, and the credential-decryption flaw makes those provider credentials the thing worth watching for abuse elsewhere: unexpected usage or billing on an LLM provider account whose key was only ever stored in Langflow is evidence the key store was read, and that evidence surfaces at the provider, not on the host. **Triage:** legitimate Langflow flows do execute code by design, so process descent from the worker is not by itself malicious — the discriminators are whether the execution correlates with an authenticated, attributable flow run in the application's own logs, and whether the invoking request arrived at a webhook endpoint without an API key. A flow execution with no corresponding authenticated session is the case to run down.
