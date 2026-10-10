---
schema: 1
kind: research
title: "ClickFix now drives 52-67% of monthly browser-based-attack detections, delivered overwhelmingly through search engines rather than email, and rotates across 20+ trusted binaries to outpace endpoint rules"
headline: "Push Security's detection data: ClickFix has become the default browser-borne attack, and most of it never touches an inbox"
summary: >
  Push Security's H2 2026 detection-data review reports ClickFix and its derivatives averaging 52% of its
  monthly browser-based-attack detections through Q2 2026, rising to 67% in August, with four in five 2026
  payloads reached via search engines rather than email. NCSC Switzerland maintains a live public advisory
  on the same fake-CAPTCHA technique, reporting a rise in compromised Swiss websites serving it.
discovered_at: "2026-09-29T05:05:00Z"
updated_at: null
event_date: "2026-09-23"
run_id: 2026-09-29T0405Z-intel
priority: notable
immediate_action: null
tags: [phishing, actively-exploited]
regions: [global, switzerland, europe]
sectors: [public-sector]
entities: []
techniques: [T1204.004, T1059.001, T1218, T1140, T1608]
affected_products: []
cves: []
sources:
  - url: "https://pushsecurity.com/blog/the-state-of-clickfix-by-detection-data"
    publisher: "Push Security"
    date: "2026-09-23"
    role: primary
  - url: "https://www.bacs.admin.ch/en/clickfix-en"
    publisher: "NCSC Switzerland / BACS"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Through Q2, ClickFix made up an average of 52% of Push's detections, surpassing other browser-based attacks (predominantly AiTM and device code phishing) for the first time."
    publisher: "Push Security"
    source_url: "https://pushsecurity.com/blog/the-state-of-clickfix-by-detection-data"
  - quote: "And in August, this figure reached 67%."
    publisher: "Push Security"
    source_url: "https://pushsecurity.com/blog/the-state-of-clickfix-by-detection-data"
verification: multi-source
sourcing_note: >
  Push Security's percentages are its own detection telemetry, a single vendor's population, not an
  independently corroborated industry-wide figure; the NCSC-CH/BACS advisory independently corroborates the
  underlying technique and its rise specifically against Swiss-hosted websites, which is what moves this
  above single-source, not a second measurement of Push's own statistics.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:17Z"
    run_id: 2026-09-30T0639Z-audit
    type: improvement
    summary: >
      Priority recalibrated from high to notable: a detection review that informs hunting but forces
      no decision this week. The takeaway adds NCSC Switzerland's advice to restrict outbound
      connections to blockchain RPC providers.
    fields: [priority, body]
migrated_from: null
---

Push Security's H2 2026 detection-data review reports ClickFix and its derivatives averaging 52% of its monthly browser-based-attack detections through Q2 2026, rising to 67% in August 2026, ahead of adversary-in-the-middle phishing and device-code phishing combined ([Push Security, 2026-09-23](https://pushsecurity.com/blog/the-state-of-clickfix-by-detection-data)). Three phishing kits, ERRTRAFFIC plus two Push-internal-named kits TURNTIP and NOCHAIN, account for 73% of ClickFix detections, with ERRTRAFFIC alone responsible for 34% in August. Four in five 2026 ClickFix payloads were reached through search engines (Google/Bing) rather than email, via compromised sites, malvertising and SEO poisoning, meaning the technique largely bypasses email security controls that assume a phishing message is the entry point. Push observed 84 distinct ClickFix command forms spanning more than 20 trusted system binaries (PowerShell, cmd, bash/zsh, mshta, rundll32, msiexec, pcalua, wmic, certutil, schtasks among others), a deliberate LOLBin-rotation strategy intended to outpace endpoint-detection rules keyed on any single binary; Push reports the main kits now read their configuration from a smart contract on a public blockchain (an "EtherHiding" technique observed across BNB Smart Chain testnet, Polygon, Base and Ethereum Sepolia, with most of the observed traffic on testnets) rather than from the page itself, so payload and lure are fetched at load time, can be rotated with a single blockchain transaction, and leave no hosting infrastructure for defenders to take down or block.

NCSC Switzerland maintains a live public advisory describing the same technique's fake-CAPTCHA delivery mechanism, reporting an increase in compromised websites, predominantly WordPress, that serve the ClickFix lure to visitors ([NCSC Switzerland / BACS](https://www.bacs.admin.ch/en/clickfix-en)): direct confirmation that this is not a theoretical or foreign-only trend but one actively affecting Swiss infrastructure that users in Switzerland may encounter through ordinary browsing.

Push notes that standard EDR guidance of baselining LOLBin activity and alerting on anomalies suffers a high false-positive rate for this technique class, because legitimate IT automation, MDM tooling and administrator scripts generate similar-looking process-execution telemetry to a ClickFix payload's own binary invocation.

**Triage:** the discriminator is not which binary runs but its parent-process lineage and trigger context: a LOLBin (PowerShell, mshta, rundll32, certutil, or any of the 20+ Push documents) launched with a paste-derived command line from `explorer.exe` or a browser process, following a user interaction with a fake CAPTCHA or verification prompt on a webpage, is the ClickFix pattern; the same binary launched from a scheduled task, an MDM agent, or an IT-administration parent process in the course of routine automation is the benign lookalike. Sequence and parentage separate the two; the binary alone does not.

**Defender takeaway:** because delivery is overwhelmingly search-driven rather than email-driven, browser and endpoint telemetry, not mail-gateway controls, are where this technique surfaces; monitor for the clipboard-paste-to-Run/PowerShell pattern specifically, and treat any of the 20+ documented LOLBins launched immediately after a browser session visited an unfamiliar or newly-registered domain as a priority hunt lead, independent of which specific binary appears. NCSC Switzerland also advises organisations outside fintech to restrict outbound connections to blockchain RPC providers, which the payload-retrieval step uses ([NCSC Switzerland / BACS, 2026-08-07](https://www.bacs.admin.ch/en/clickfix-en)).

## Improvement — 2026-09-30T06:56:17Z

NCSC Switzerland advises organisations outside fintech to restrict outbound connections to blockchain RPC providers, which the payload-retrieval step uses ([NCSC Switzerland / BACS, 2026-08-07](https://www.bacs.admin.ch/en/clickfix-en)).
