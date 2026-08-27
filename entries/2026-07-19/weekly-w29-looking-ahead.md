---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: "2026-W29 looking ahead — items already in motion: WordPress WP2Shell and Firefox public exploit code, a SharePoint Pwn2Own chain half-patched until August, a withheld ShareFile CVE, and two EU regulatory clocks running"
headline: "W29 outlook — public PoCs (WP2Shell, Firefox), a SharePoint chain half-patched until August, a withheld ShareFile CVE, and the CRA/CER clocks already ticking"
summary: >
  A justified watch list of items already in motion at the close of 2026-W29 — not predictions. WordPress "WP2Shell" (CVE-2026-63030/-60137) has public PoC on GitHub with NCSC-NL expecting short-term exploitation; Firefox 152.0.6's two critical flaws (CVE-2026-15718/-15719) carry public exploit code with no confirmed in-the-wild abuse yet. Rapid7 is holding the SharePoint JWT auth-bypass CVE-2026-55040 PoC under a 30-day embargo and its chained RCE half is not scheduled for patch until August, so the July fix is the only current break in that chain. Progress has reserved but withheld a ShareFile Storage Zone Controller CVE, due to publish in roughly two weeks. And two EU regulatory clocks are running: the CRA Article 14 reporting obligation from 11 September 2026 and Germany's KRITIS-Dachgesetz registration window opened 17 July. Each is a concrete, sourced development a Swiss/European defender can act on now.
discovered_at: "2026-07-19T23:59:00Z"
event_date: 2026-07-18
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
cves: []
techniques: []
affected_products: []
sources:
  - url: "https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core"
    publisher: "Searchlight Cyber"
    date: "2026-07-17"
    role: primary
  - url: "https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed"
    publisher: "Rapid7 Labs"
    date: "2026-07-14"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/"
    publisher: "BleepingComputer"
    date: "2026-07-14"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0242"
    publisher: "NCSC-NL"
    date: "2026-07-16"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/"
    publisher: "Help Net Security (citing Defused)"
    date: "2026-06-30"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Every item is a sourced, already-in-motion development (public PoC, scheduled disclosure/patch, reserved CVE, statutory deadline) — not a forecast. Reliability B / credibility 2: the timing claims (August RCE patch, ~2-week CVE publication) are vendor/researcher statements of intent, not settled events."
confidence: medium
update_of: null
references:
  - 2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030
  - 2026-07-17/firefox-152-0-6-wasm-site-isolation-public-exploit
  - 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
  - 2026-07-13/progress-sharefile-storage-zone-controller-shutdown
  - 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed
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

Items already in motion at the close of the week — each sourced, none a prediction:

- **WordPress "WP2Shell" pre-auth RCE (CVE-2026-63030 + CVE-2026-60137)** — Searchlight Cyber withheld exploit details but published a public checker, public proof-of-concept code is already on GitHub, and NCSC-NL assesses short-term exploitation is expected; no confirmed in-the-wild abuse as of 2026-07-18 ([Searchlight Cyber, 2026-07-17](https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core)). Any stock WordPress not on 7.0.2 / 6.9.5 / 6.8.6 is the exposure to close first.
- **SharePoint JWT auth-bypass CVE-2026-55040 (Pwn2Own chain)** — Rapid7 is holding full technical detail and the PoC under a 30-day disclosure embargo, and the chained RCE half is not scheduled for patch until August, so applying the July fix now is the only current break in the chain ([Rapid7, 2026-07-14](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed)). Watch for the embargo lift (~mid-August) and the August RCE patch.
- **Firefox 152.0.6 (CVE-2026-15718 WebAssembly, CVE-2026-15719 site-isolation)** — public exploit code exists; Mozilla states no in-the-wild attacks, contrary to some aggregator "zero-day" framing ([NCSC-NL, 2026-07-16](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0242)). A browser code-execution chain with public code on managed/ESR fleets is the watch item.
- **Progress ShareFile Storage Zone Controller CVE** — Progress named a path-traversal root cause and shipped 5.12.5 / 6.0.2 but reserved and withheld the CVE identifier, due to publish in roughly two weeks ([BleepingComputer, 2026-07-14](https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/)); patch and post-exposure review should not wait for the identifier.
- **Oracle E-Business Suite Payments (CVE-2026-46817)** — confirmed exploited from late June before any public PoC ([Help Net Security, 2026-06-30](https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)); any instance exposed after 2026-05-28 is inside a live post-exposure compromise-assessment window, not merely a patch task.
- **EU regulatory clocks running** — the CRA Article 14 24-hour vulnerability-reporting obligation begins 11 September 2026, and Germany's KRITIS-Dachgesetz operator-registration window opened 17 July 2026 (three-month registration deadline); both are covered in this week's policy entry and are obligations the constituency's supplier and cross-border tail is already inside.
