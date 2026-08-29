---
schema: 1
kind: threat
title: "PurpleDelta: Insikt Group gets inside a North Korean IT-worker operation and finds the detectable half is on the endpoint — a second remote-management tool on the company laptop, and a device whose location never matches the login"
headline: "The fraud is a hiring problem; the evidence sits in RMM inventory and laptop geolocation"
summary: >
  Recorded Future's Insikt Group published an analysis on 2026-08-18 of PurpleDelta, its designation for the
  North Korean IT-worker cluster that overlaps with the vendor names Jasper Sleet, UNC5267, Wagemole and
  Famous Chollima. Between late 2024 and early 2025 one cluster applied to over 1,100 companies, sometimes 60
  positions a day, running at least 22 fabricated personas, some of them supported by AI-generated photos, illicit identity
  documents and purpose-configured chatbot assistants used to answer interview questions in real time; Insikt
  assesses the operators are highly likely to have been employed by at least ten organisations. Roughly 80% of
  the target companies were North American, but Insikt states operators applied in every region of the world.
  The transferable value for defenders is Insikt's own technical control set: the employer-issued laptop is
  held by a facilitator and reached over commercial remote-desktop tooling, which makes a second RMM agent and
  a location mismatch the observable evidence.
discovered_at: "2026-08-19T05:40:00Z"
event_date: "2026-08-18"
run_id: 2026-08-19T0410Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, insider-threat, identity, ai-abuse, north-korea-nexus]
regions: [global, us, europe]
sectors: [technology, public-sector, healthcare, finance]
entities: [actor:purpledelta]
techniques: [T1585.001, T1684.001, T1199, T1219, T1219.002, T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations"
    publisher: "Recorded Future / Insikt Group"
    date: "2026-08-18"
    role: primary
closed_sources: []
evidence:
  - quote: "The group overlaps with threat actor designations used by other vendors, including Jasper Sleet, UNC5267, Wagemole, and Famous Chollima."
    publisher: "Recorded Future / Insikt Group"
  - quote: "Between late 2024 and early 2025, one cluster applied to jobs at over 1,100 companies, primarily in the software and technology, staffing and consulting, and healthcare and biotechnology sectors."
    publisher: "Recorded Future / Insikt Group"
  - quote: "Roughly 80% of the companies are based in North America, but the operators applied to companies in every region of the world."
    publisher: "Recorded Future / Insikt Group"
  - quote: "If you run remote monitoring and management (RMM) software in your organization, ensure that no other RMM software is installed, and deny-list other RMM software on your networks."
    publisher: "Recorded Future / Insikt Group"
  - quote: "Regularly geolocate company laptops to verify that their locations match employee login locations."
    publisher: "Recorded Future / Insikt Group"
verification: single-source
sourcing_note: >
  Insikt Group is the sole assessor; no independent second read of this research was located this run, so it
  ships single-source at credibility 2. Two different kinds of claim in the report are carried differently
  here, matching how Insikt itself states them: the overlap with Jasper Sleet, UNC5267, Wagemole and Famous
  Chollima is stated by Insikt as fact — it presents these as other vendors' names for the same phenomenon
  rather than a confidence-qualified attribution — while its reported "signs of overlap" with a separate,
  malware-deploying cluster it tracks is explicitly hedged and is therefore not carried as a connection here.
  The employment count is Insikt's own hedge ("highly likely to be actively employed by at least ten
  organizations") and is reproduced as a hedge rather than converted into a confirmed figure. Insikt does not
  disclose its collection methodology beyond naming the artifact classes it reviewed — recorded video
  sessions, calendar and spreadsheet tracking artifacts, workspace content, and device forensics from what it
  assesses was an operator's own accidental self-infection. The observation window for the quantified cluster
  is late 2024 to early 2025; the report states the tempo continues, and that distinction is kept explicit.
  One further hedge is preserved rather than flattened: Insikt directly observed the operators buying
  identities and accounts, but records their presence across infostealer-log channels only as suggesting
  they may also be purchasing stolen credentials, and this entry carries that as the inference it is.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory remote-monitoring-and-management agents across corporate endpoints and alert on any second RMM or remote-desktop agent appearing on a device that already carries the sanctioned one — Insikt names this as its own primary technical control, and it is the artifact a facilitator-held laptop necessarily produces."
  - "Compare the geolocation of company-issued laptops against the claimed work location and the source of that employee's authentications, starting with remote contractor devices shipped rather than handed over in person."
migrated_from: null
---

Insikt Group published its PurpleDelta analysis on 2026-08-18, covering what it describes as a state-directed network of covert North Korean technology workers operating across freelancing platforms and corporate hiring pipelines. On naming, Insikt is unhedged: "The group overlaps with threat actor designations used by other vendors, including Jasper Sleet, UNC5267, Wagemole, and Famous Chollima" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)) — these are presented as different vendors' labels for the same phenomenon rather than as a graded attribution claim. The quantified dataset covers one cluster: "Between late 2024 and early 2025, one cluster applied to jobs at over 1,100 companies, primarily in the software and technology, staffing and consulting, and healthcare and biotechnology sectors" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), sometimes at a rate of at least 60 positions a day, with at least 22 fabricated personas maintained across clusters and operators "highly likely to be actively employed by at least ten organizations" — Insikt's own hedge, kept as one here.

The geography is the reason this is not a North American story. Roughly four in five target companies were North American, "but the operators applied to companies in every region of the world" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), and the sector concentration — software and technology, then staffing and consulting, then healthcare and biotechnology — describes the supplier tier that public-sector and critical-infrastructure organisations in this constituency buy remote technical labour through. This store already carries a Flemish Government agency confirming a North Korean compromise that reached it through a contractor's workstation, which is the same structural exposure arriving by a different route: the organisation's own hiring controls are not the only ones that matter.

What makes the report useful rather than merely alarming is that the fraud leaves endpoint artifacts, and Insikt separates its technical recommendations from its hiring-process advice. The operating model is that a facilitator physically holds the employer-issued laptop while the operator works it remotely over commercial remote-desktop software, with a commercial VPN marketed for circumventing China's national firewall used consistently for connectivity, and Insikt places many of the operators' nexus in Shenyang on the basis of professional profiles, social-media presence and artifacts on their systems. That arrangement cannot be run without leaving two things on a managed device: a remote-access agent the employer did not install, and a persistent mismatch between where the hardware is and where the person claims to be. Insikt's own controls address exactly those — "If you run remote monitoring and management (RMM) software in your organization, ensure that no other RMM software is installed, and deny-list other RMM software on your networks" and "Regularly geolocate company laptops to verify that their locations match employee login locations" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), alongside regular port-checking to detect remote access via desktop sharing or VPNs, insider-threat monitoring on company devices, and a requirement that company hardware never be shipped to an anonymised post box or to anyone other than the named individual.

The persona-construction tradecraft is worth knowing mainly because it explains why interview-stage scrutiny fails. Profile photographs come from a face-swapping service and are kept locally on the operator's machine in a dedicated directory; identity documents come from a paid document-generation service; identities and accounts are bought, with Insikt directly observing the purchase of US and Ukrainian identities, while its separate observation of the operators across infostealer-log channels is recorded only as suggesting they may also be buying stolen credentials; contribution histories on code-hosting platforms are fabricated; and multi-account browsers with separate browser profiles and calendars keep the personas apart. Insikt also lists Android emulation software among the operators' tooling without stating what it is used for, and no purpose is inferred here. During live interviews the operators record and transcribe the call and feed questions to purpose-configured chatbot assistants, reading the answers back — Insikt notes the answers were sometimes visibly wrong, which indicates limited subject-matter command rather than genuine skill. One operator was observed running two personas in parallel, one already employed and one interviewing elsewhere, and interview and meeting times for different personas were seen to collide.

**Defender takeaway:** treat this as an endpoint and identity-telemetry problem that a hiring process alone will not close, because the interview defences are the ones the operators have specifically tooled against. The durable signals live in software inventory and authentication geography: a remote-desktop or RMM agent on a corporate device that the estate did not deploy, outbound remote-access sessions from a device whose network egress does not match the employee's stated country, and authentications for one identity arriving from a location that never coincides with where the issued hardware reports itself. **Triage:** legitimate remote workers, contractors and support teams produce remote sessions and foreign egress routinely, so neither is suspicious alone — the discriminators are a *second*, uninventoried remote-access agent alongside the sanctioned one, and a mismatch that is systematic rather than occasional, where the hardware's location and the account's authentication origin never converge over time rather than diverging during travel.
