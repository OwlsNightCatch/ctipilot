---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: Looking ahead — 2026-W22
headline: Looking ahead — 2026-W22
summary: "Windows \"Chaotic Eclipse\" zero-day cluster — June 2026 Patch Tuesday (~2026-06-10) is the expected first fix, with a researcher drop announced for July 14."
discovered_at: "2026-05-25T05:00:31Z"
event_date: 2026-05-30
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - zero-day
  - cloud
  - rce
  - phishing
  - wiper
regions:
  - global
sectors: []
entities: []
cves: []
sources:
  - url: "https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more"
    publisher: The Record
    role: primary
  - url: "https://www.rapid7.com/blog/post/ve-authenticated-rce-via-argument-injection-gogs-unfixed/"
    publisher: Rapid7
    role: corroborating
  - url: "https://www.ic3.gov/PSA/2026/PSA260527"
    publisher: FBI IC3 PSA260527
    role: corroborating
  - url: "https://www.tenable.com/security/research/tra-2026-44"
    publisher: Tenable TRA-2026-44
    role: corroborating
  - url: "https://isc.sans.edu/diary/33016"
    publisher: SANS ISC diary 33016
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
migrated_from: briefs/weekly/2026-W22.md
---

Items already in motion at the close of 2026-W22. Not predictions — each links to the in-motion reporting underneath.

- **Windows "Chaotic Eclipse" zero-day cluster — June 2026 Patch Tuesday (~2026-06-10) is the expected first fix, with a researcher drop announced for July 14.** Microsoft's Digital Crimes Unit has threatened criminal action over the serial zero-day releases, but the cluster's escalation paths remain unpatched with public PoCs — **YellowKey** (CVE-2026-45585), **GreenPlasma**, and **MiniPlasma** (CVE-2020-17103, the `cldflt.sys` Cloud Filter driver, whose 2020 patch the researcher claims is incomplete) — and the researcher has announced more for **July 14**. Until a fix ships, BitLocker PIN / Network-Unlock GPOs and `ctfmon.exe`-injection WDAC rules are the available controls. ([The Record](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more); [Daily 2026-05-30](/briefs/2026-05-30/))
- **Gogs argument-injection RCE remains unpatched with a public Metasploit module and a non-responsive maintainer.** Rapid7 published the unfixed authenticated-RCE-via-argument-injection with exploit code; with no vendor fix in sight, the only mitigation is keeping Gogs off the public internet behind authenticated access and watching for the maintainer's response. ([Rapid7](https://www.rapid7.com/blog/post/ve-authenticated-rce-via-argument-injection-gogs-unfixed/); [Daily 2026-05-29](/briefs/2026-05-29/))
- **FIFA World Cup phishing ramps toward the June 11 kickoff — "Ghost Stadium" PhaaS.** 300+ FIFA domain clones with multi-language fake SSO are already harvesting UK / Germany / Portugal / Spain fan credentials; the FBI IC3 PSA flags continued growth as the tournament approaches. Expect a volume spike in the next fortnight; brief staff and monitor for lookalike-domain credential-harvest landing pages. ([FBI IC3 PSA260527](https://www.ic3.gov/PSA/2026/PSA260527); [Daily 2026-05-30](/briefs/2026-05-30/))
- **Delta Electronics DIAView SCADA CVE-2026-9642 has no patch — incomplete fix for prior unauthenticated remote database access.** Tenable's disclosure shows the earlier CVE-2025-62582 fix was incomplete; watch for a complete vendor patch and keep DIAView off internet-reachable networks in the interim. ([Tenable TRA-2026-44](https://www.tenable.com/security/research/tra-2026-44); [Daily 2026-05-27](/briefs/2026-05-27/))
- **Shai-Hulud wave-6 candidate registries — Cargo (Rust) and Maven (Java) remain the un-hit major ecosystems.** With the worm framework now open-sourced and a wiper stage added (§ 2), the registry-agnostic OIDC-token-reuse primitive makes Cargo and Maven the next logical targets; pre-stage Sigstore / provenance-anomaly hunts in Rust and Java pipelines. ([SANS ISC diary 33016](https://isc.sans.edu/diary/33016); [Daily 2026-05-26](/briefs/2026-05-26/))
