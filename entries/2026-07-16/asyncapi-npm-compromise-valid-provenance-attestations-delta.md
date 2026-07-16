---
schema: 1
kind: incident
horizon: operational
title: "AsyncAPI npm compromise — the trojanized packages shipped valid npm/OIDC provenance attestations (Microsoft forensic timeline)"
headline: "AsyncAPI npm compromise: Microsoft finds the malicious versions carried valid npm/OIDC provenance attestations, with an import-time (not install-hook) trigger"
summary: >
  Microsoft Threat Intelligence's forensic timeline of the 2026-07-14 AsyncAPI npm compromise adds
  a load-bearing detail: because the attacker pushed to a branch that triggered AsyncAPI's own
  legitimate release workflow, the five trojanized versions were published via npm trusted
  publishing over GitHub OIDC and carry cryptographically valid provenance attestations that
  correctly name the real repo, commit and workflow — even though the triggering commit was
  unauthorized. The payload also executes at import time, not through an install lifecycle hook,
  so `--ignore-scripts` does not stop it. Provenance verification confirms which pipeline built an
  artifact, not that the triggering commit was authorized.
discovered_at: "2026-07-16T04:44:00Z"
event_date: "2026-07-15"
run_id: 2026-07-16T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [technology, public-sector, finance]
entities: [incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07, tool:m-red-team-malware-framework]
techniques: [T1195.002, T1059.007, T1105, T1027]
affected_products: ["@asyncapi/generator", "@asyncapi/generator-helpers", "@asyncapi/generator-components", "@asyncapi/specs"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-15"
    role: primary
  - url: "https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "All five malicious versions were published through npm trusted publishing using GitHub OIDC and carried valid provenance attestations. The attestations accurately identified the legitimate repositories, commits, and workflows that created the packages, even though the triggering commits were unauthorized."
    publisher: "Microsoft Threat Intelligence"
  - quote: "Do not rely on npm install –ignore-scripts as a mitigation; this campaign executes when the module is imported, not through a lifecycle hook."
    publisher: "Microsoft Threat Intelligence"
verification: multi-source
sourcing_note: "Microsoft Threat Intelligence's forensic write-up is the primary; Unit 42's npm-threat tracker independently corroborates the timeline and Miasma lineage."
confidence: high
update_of: 2026-07-14/asyncapi-npm-supply-chain-compromise-github-actions
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Extend branch-protection and required reviews to every branch that can trigger a publish/release workflow — not just the default branch — since a valid npm/OIDC provenance attestation confirms which pipeline built an artifact but not that the triggering commit was authorized."
migrated_from: null
---

**UPDATE (originally covered 2026-07-14):** Microsoft Threat Intelligence published a forensic timeline of the AsyncAPI npm compromise that adds a detail with broad supply-chain-defence implications ([Microsoft Threat Intelligence, 2026-07-15](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)). Once the attacker held push access as the AsyncAPI service account (via the `pull_request_target` misconfiguration covered in the original entry), no npm-token theft was needed: a direct push to a release-triggering branch ran the project's **own legitimate** `release-with-changesets` workflow, which published the packages via npm trusted publishing over GitHub OIDC. As a result the five trojanized versions carry cryptographically valid provenance attestations that correctly identify the real repository, commit and workflow — even though the triggering commit was unauthorized ([Microsoft Threat Intelligence, 2026-07-15](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)).

Two further deltas: the payload triggers at **import time** (embedded in one file per package — `index.js` for the specs package, `validator.js`/`utils.js`/`ErrorHandling.js` for the generator family) and unwraps an IPFS-fetched bundle through three static-key crypto layers to an `eval()`, so `npm install --ignore-scripts` provides no protection; and Microsoft recovered all three self-identifying strings — `M-RED-TEAM v6.4`, `miasma-train-p1` and `miasma-test-org` — from one binary, resolving the identifier ambiguity across the original reporting. Unit 42 independently corroborates the timeline and identifies the payload as a descendant of the same Miasma RAT deployed in the June 2026 Red Hat supply-chain operation ([Unit 42, 2026-07-15](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)).

**Defender takeaway:** the load-bearing lesson for CI/CD and supply-chain-security reviewers is that SLSA / npm-OIDC provenance attests **which pipeline** built an artifact, not whether the commit that triggered the pipeline was authorized — so provenance verification alone would not have flagged these packages. The control gap is branch-protection coverage on every branch capable of triggering a publish workflow, not only the default branch. Because delivery is import-time, detection belongs at runtime (a build/CI or developer host resolving IPFS gateways or performing a multi-stage decrypt-then-`eval` on module import), not at the install-hook layer.
