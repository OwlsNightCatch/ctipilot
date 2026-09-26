---
schema: 1
kind: incident
title: "Coder's Cloudflare-fronted Terraform module registry was compromised for 14 hours, serving trojanized modules that harvested cloud, CI/CD and AI-tooling credentials"
headline: "An attacker who never touched Coder's source code hijacked its CDN routing to serve credential-stealing Terraform modules for half a day"
summary: >
  Coder, a self-hosted cloud-development-environment platform, disclosed that an unidentified actor
  gained access to the Cloudflare infrastructure fronting its Terraform module registry and added
  unauthorized origin servers, causing a roughly 14-hour window (2026-08-31, 07:35-21:45 UTC) in
  which some registry requests were served trojanized, credential-stealing modules. Fixed in
  2.37.0, 2.36.4, 2.35.7 and 2.34.9; Coder cannot conclusively enumerate every affected deployment.
discovered_at: "2026-09-04T06:00:00Z"
updated_at: null
event_date: "2026-08-31"
run_id: 2026-09-04T0410Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cloud, identity]
regions: [global]
sectors: [public-sector, defense, technology]
entities:
  - "incident:coder-registry-cloudflare-compromise-2026-08"
techniques: [T1195.002, T1552.001, T1071.001]
affected_products: ["Coder", "Coder module registry (registry.coder.com)"]
cves: []
sources:
  - url: "https://github.com/coder/coder/security/advisories/GHSA-vx42-ghc9-gw65"
    publisher: "Coder (GitHub Security Advisory)"
    date: "2026-09-01"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/"
    publisher: "BleepingComputer"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unidentified malicious actor gained access to Coder's Cloudflare infrastructure and added unauthorized IP addresses to the pool used for Coder's module registry. These unauthorized IP addresses hosted a version of Coder's registry that contained artifacts which included malicious code."
    publisher: "Coder (GitHub Security Advisory)"
  - quote: "the delivery window for the malicious artifacts was between 07:35 UTC and 21:45 UTC on Monday, August 31"
    publisher: "Coder / BleepingComputer"
  - quote: "because the attacker's infrastructure is outside the project's control, Coder does not have access to crucial logs and cannot conclusively identify every compromised deployment"
    publisher: "BleepingComputer, reporting Coder's advisory"
verification: single-source-victim
sourcing_note: >
  Single-source under the victim's-own-disclosure carve-out: Coder is the affected organization
  disclosing its own incident via a formal GitHub Security Advisory. BleepingComputer restates the
  same advisory rather than independently assessing the compromise.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "For any Coder deployment that created or updated a workspace template, ran a template-build dry run, or built a workspace without module caching disabled (module caching is on by default) between 2026-08-31 07:35 and 21:45 UTC: rotate every credential a provisioner job in that window could have accessed — cloud/AI-tooling API keys, CI/CD credentials, OIDC tokens, configured SSH keys, and, where the provisioner ran inside coderd itself, the Coder deployment's own database password."
updates: []
migrated_from: null
---

Coder — a self-hosted cloud-development-environment platform whose customers include, per BleepingComputer, Dropbox, Palantir, Square, Mercedes-Benz, KKR, EnBW, and US government agencies and defense contractors — disclosed that an unidentified actor gained access to the Cloudflare infrastructure fronting registry.coder.com, its Terraform-module package registry, and added unauthorized origin IP addresses to the CDN's server pool ([Coder, GitHub Security Advisory GHSA-vx42-ghc9-gw65, 2026-09-01](https://github.com/coder/coder/security/advisories/GHSA-vx42-ghc9-gw65)). For roughly 14 hours on 2026-08-31 (07:35-21:45 UTC), Cloudflare routed a subset of registry requests to the attacker's servers instead of Coder's own, serving modified Terraform modules containing credential-stealing code. The malicious modules searched for and exfiltrated provisioner environment variables and secrets, cloud-infrastructure and AI-tooling API keys, CI/CD credentials, configuration-file secrets, terminal history, user OIDC tokens, configured SSH keys, one-time external-auth tokens, and — when the provisioner ran inside coderd itself — the Coder deployment's own database password and other configuration secrets, sent to a lookalike domain registered 2026-08-28 that impersonates Coder's own infrastructure naming convention.

Exposure requires only that a deployment created or updated a workspace template, ran a template-build dry run, or built a workspace without module caching during the exposure window; module caching is on by default, so a deployment relying on the default configuration was still exposed on any fresh template build. Coder states it "does not have access to crucial logs and cannot conclusively identify every compromised deployment," because the credential-theft traffic went to infrastructure entirely outside its own control ([BleepingComputer, reporting Coder's advisory, 2026-09-03](https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/)). No refresh tokens were exposed, and Coder reports no evidence of impact to data it directly maintains. Fixed in 2.37.0, 2.36.4, 2.35.7 and 2.34.9, released 2026-09-01; the currently-served registry content has been reviewed and confirmed clean.

**Defender takeaway:** this is a CDN/edge-infrastructure compromise, not a code-repository or maintainer-account compromise — the attacker never touched Coder's source code or release pipeline, only the routing layer in front of the registry. Any organisation self-hosting a package or module registry behind a third-party CDN should treat origin-pool integrity — who can add an origin IP to your own CDN pool — as a supply-chain trust boundary equal in importance to registry authentication itself. Detection concept: query provisioner job logs for the Terraform `data.external.telemetry` block name the malicious modules used to invoke their exfiltration script, and check firewall/proxy/DNS/VPC flow logs for outbound connections coinciding with template builds or workspace creation during the exposure window.
