---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "npm / developer-ecosystem supply-chain wave status: AsyncAPI was the week's marquee compromise, and DPRK's Contagious Interview broadened the developer-as-target vector from package poisoning to CI/CD pipelines and job-interview repos"
headline: "Supply-chain update — AsyncAPI's CI/CD compromise shipped versions with valid provenance attestations; Contagious Interview hides its payload in SVG comments"
summary: >
  Update to the prior weekly's npm supply-chain wave. This week the wave's front edge moved from poisoning published packages to abusing the trust machinery around them. The AsyncAPI compromise reached over-three-million-weekly-download packages by riding the org's own legitimate CI/CD release workflow, so the five trojanized versions carried cryptographically valid npm/OIDC provenance attestations and executed at import time (defeating --ignore-scripts). In parallel, the DPRK-aligned Contagious Interview campaign broadened the developer-targeting vector: a fake job posting delivered a trojanized Next.js repo hiding its payload as Base64 fragments across HTML comments in every SVG flag image, reassembled and run with eval() to evade scanners that do not parse SVG comment bodies. Both extend the tracked pattern the same way — the initial-access target is the developer and the build/trust pipeline, not just the registry — and both defeat a control defenders assumed held (provenance attestation; install-hook scanning). No change to the previously-tracked jscrambler/injectivelabs strains beyond this new front.
discovered_at: "2026-07-19T23:38:00Z"
event_date: 2026-07-18
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07
  - tool:m-red-team-malware-framework
  - campaign:contagious-interview
cves: []
techniques:
  - T1195.002
  - T1027
  - T1204
affected_products: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-15"
    role: primary
  - url: "https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography"
    publisher: "Elastic Security Labs"
    date: "2026-07-18"
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "AsyncAPI is multi-source (Wiz + Microsoft, covered operationally); Contagious Interview is single-source Elastic primary. Both first-party research; reliability B, credibility 2 (the Contagious Interview strand is single-lab). Framed as the fresh front of the tracked wave, not a re-summary of prior strains."
confidence: high
update_of: 2026-07-12/weekly-w28-npm-supply-chain-wave
references:
  - 2026-07-14/asyncapi-npm-supply-chain-compromise-github-actions
  - 2026-07-16/asyncapi-npm-compromise-valid-provenance-attestations-delta
  - 2026-07-18/contagious-interview-ottercookie-svg-steganography
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-12):** The prior weekly tracked the npm supply-chain wave through the jscrambler and injectivelabs compromises, whose signature was moving the dropper out of the install hook to evade scanners. This week the wave's front edge moved again — from poisoning packages to abusing the trust machinery around them, and the developer is now squarely the target. The marquee event was AsyncAPI: the attacker rode the org's own legitimate CI/CD release workflow, so the trojanized versions carried cryptographically valid npm/OIDC provenance attestations and executed at import time "even though the triggering commits were unauthorized," defeating `--ignore-scripts` ([Microsoft, 2026-07-15](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)) — the detailed provenance-vs-authorization lesson is in this week's incidents recap. In parallel, the DPRK-aligned Contagious Interview campaign broadened the developer-targeting vector beyond the registry entirely: Elastic documented a fake job posting delivering a trojanized Next.js repo that hides its payload as Base64 fragments inside HTML comments across every SVG flag image in an assets directory, reassembled alphabetically and run with `eval()` to evade scanners that do not parse SVG comment bodies, then running an OtterCookie-aligned credential/wallet stealer on project startup ([Elastic, 2026-07-18](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)). The consolidated status: the wave the pipeline tracks now spans package poisoning, CI/CD-pipeline compromise and job-interview repos, and its through-line is that the developer's build environment and the trust signals around it (attestations, install hooks, static scanners) are the surface — so branch-protection and workflow-trigger review, import-time dependency monitoring, and treating any candidate/contractor take-home repo as untrusted code are the current counters.
