---
schema: 1
kind: threat
horizon: operational
title: "\"Miasma\" worm backdoors 32 Red Hat Cloud Services npm packages via OIDC trusted-publishing abuse"
headline: "\"Miasma\" worm backdoors 32 Red Hat Cloud Services npm packages via OIDC trusted-publishing abuse"
summary: "\"Miasma\" supply-chain worm compromised 32 @redhat-cloud-services npm packages via a hijacked maintainer GitHub account and OIDC trusted-publishing abuse, adding new GCP and Azure cloud-identity collectors (Wiz, 2026-06-01)."
discovered_at: "2026-06-02T05:00:02Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: high
immediate_action: null
tags:
  - supply-chain
  - cloud
  - identity
  - infostealer
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
  - "campaign:miasma-redhat-npm-supply-chain"
cves: []
sources:
  - url: "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages"
    publisher: Wiz Research
    role: primary
  - url: "https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm"
    publisher: Aikido Security
    role: corroborating
  - url: "https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages"
    publisher: Socket
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-02.md
---

Threat actor cluster TeamPCP used a compromised Red Hat maintainer GitHub account to inject malicious CI/CD workflows into 32 packages in the `@redhat-cloud-services` npm namespace, poisoning 96 releases across high-traffic packages — Wiz puts the combined weekly downloads at roughly 80,000, while Aikido counts closer to 117,000 ([Wiz, 2026-06-01](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages) · [Aikido Security, 2026-06-01](https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm)). Rather than compromising developer machines directly, the attack abused GitHub Actions OIDC trusted publishing so the CI/CD pipeline itself republished backdoored packages carrying obfuscated `preinstall` hooks. The "Miasma" payload — a new variant in the Mini Shai-Hulud / Shai-Hulud lineage — sweeps for GitHub Actions secrets, npm tokens, AWS keys, SSH keys, HashiCorp Vault and Kubernetes credentials, and now adds dedicated collectors for **GCP service-account and Azure managed-identity tokens**, signalling a pivot from developer-host theft toward cloud-account takeover ([Socket, 2026-06-01](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages)). Wiz notes the new variant's cloud-identity focus explicitly.

**Why it matters to us:** Red Hat tooling has a broad EU public-sector DevOps footprint (OpenShift/OpenStack estates). Inventory installed `@redhat-cloud-services/*` versions across build agents and developer endpoints, alert on `preinstall` scripts spawning obfuscated `node -e` chains from `npm`/`npx` parent trees, and rotate any CI/CD cloud-identity tokens reachable from affected pipelines.
