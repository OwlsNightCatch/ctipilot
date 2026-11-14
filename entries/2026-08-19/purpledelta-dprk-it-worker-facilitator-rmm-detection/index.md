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
updated_at: "2026-08-31T05:45:00Z"
event_date: "2026-08-18"
run_id: 2026-08-19T0410Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, insider-threat, identity, ai-abuse, north-korea-nexus]
regions: [global, us, europe]
sectors: [technology, public-sector, healthcare, finance]
entities: [actor:purpledelta]
techniques: [T1585.001, T1684.001, T1199, T1219, T1219.002, T1078, T1200]
affected_products: []
cves: []
sources:
  - url: "https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations"
    publisher: "Recorded Future / Insikt Group"
    date: "2026-08-18"
    role: primary
  - url: "https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation"
    publisher: "Huntress"
    date: "2026-08-26"
    role: corroborating
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
  - quote: "Defenders can alert on Windows Security Event ID 6416 when`device_description` contains PiKVM or Guermok, and hunt the Windows registry path`HKLM\\SYSTEM\\CurrentControlSet\\Enum\\USB` , especially FriendlyName values such as PiKVM Composite Device and Guermok USB3 Video."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation"
verification: single-source
sourcing_note: >
  Insikt Group is the sole assessor; no independent second read of this research has been located, so it
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
updates:
  - at: "2026-08-31T05:45:00Z"
    run_id: 2026-08-31T0411Z-intel
    type: update
    summary: >
      Huntress published forensic detail from five individuals across three 2026 investigations
      against the same cluster (which it names Famous Chollima, an alias this entry already
      carries) with reusable methodology: detecting PiKVM and Guermok USB hardware via Windows
      Security Event ID 6416 and the USB registry enumeration path, a laptop-farm network-transition
      timeline, and identity-document metadata forensics (camera model, device time offset,
      near-identical issue dates, and a reverse-image/mugshot match) across separate cases.
    fields: [techniques, actions, sourcing_note, sources, evidence, body]
migrated_from: null
---

Insikt Group published its PurpleDelta analysis on 2026-08-18, covering what it describes as a state-directed network of covert North Korean technology workers operating across freelancing platforms and corporate hiring pipelines. On naming, Insikt is unhedged: "The group overlaps with threat actor designations used by other vendors, including Jasper Sleet, UNC5267, Wagemole, and Famous Chollima" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)) — these are presented as different vendors' labels for the same phenomenon rather than as a graded attribution claim. The quantified dataset covers one cluster: "Between late 2024 and early 2025, one cluster applied to jobs at over 1,100 companies, primarily in the software and technology, staffing and consulting, and healthcare and biotechnology sectors" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), sometimes at a rate of at least 60 positions a day, with at least 22 fabricated personas maintained across clusters and operators "highly likely to be actively employed by at least ten organizations" — Insikt's own hedge, kept as one here.

The geography is the reason this is not a North American story. Roughly four in five target companies were North American, "but the operators applied to companies in every region of the world" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), and the sector concentration — software and technology, then staffing and consulting, then healthcare and biotechnology — describes the supplier tier that public-sector and critical-infrastructure organisations in this constituency buy remote technical labour through. This store already carries a Flemish Government agency confirming a North Korean compromise that reached it through a contractor's workstation, which is the same structural exposure arriving by a different route: the organisation's own hiring controls are not the only ones that matter.

What makes the report useful rather than merely alarming is that the fraud leaves endpoint artifacts, and Insikt separates its technical recommendations from its hiring-process advice. The operating model is that a facilitator physically holds the employer-issued laptop while the operator works it remotely over commercial remote-desktop software, with a commercial VPN marketed for circumventing China's national firewall used consistently for connectivity, and Insikt places many of the operators' nexus in Shenyang on the basis of professional profiles, social-media presence and artifacts on their systems. That arrangement cannot be run without leaving two things on a managed device: a remote-access agent the employer did not install, and a persistent mismatch between where the hardware is and where the person claims to be. Insikt's own controls address exactly those — "If you run remote monitoring and management (RMM) software in your organization, ensure that no other RMM software is installed, and deny-list other RMM software on your networks" and "Regularly geolocate company laptops to verify that their locations match employee login locations" ([Insikt Group, 2026-08-18](https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations)), alongside regular port-checking to detect remote access via desktop sharing or VPNs, insider-threat monitoring on company devices, and a requirement that company hardware never be shipped to an anonymised post box or to anyone other than the named individual.

The persona-construction tradecraft is worth knowing mainly because it explains why interview-stage scrutiny fails. Profile photographs come from a face-swapping service and are kept locally on the operator's machine in a dedicated directory; identity documents come from a paid document-generation service; identities and accounts are bought, with Insikt directly observing the purchase of US and Ukrainian identities, while its separate observation of the operators across infostealer-log channels is recorded only as suggesting they may also be buying stolen credentials; contribution histories on code-hosting platforms are fabricated; and multi-account browsers with separate browser profiles and calendars keep the personas apart. Insikt also lists Android emulation software among the operators' tooling without stating what it is used for, and no purpose is inferred here. During live interviews the operators record and transcribe the call and feed questions to purpose-configured chatbot assistants, reading the answers back — Insikt notes the answers were sometimes visibly wrong, which indicates limited subject-matter command rather than genuine skill. One operator was observed running two personas in parallel, one already employed and one interviewing elsewhere, and interview and meeting times for different personas were seen to collide.

**Defender takeaway:** treat this as an endpoint and identity-telemetry problem that a hiring process alone will not close, because the interview defences are the ones the operators have specifically tooled against. The durable signals live in software inventory and authentication geography: a remote-desktop or RMM agent on a corporate device that the estate did not deploy, outbound remote-access sessions from a device whose network egress does not match the employee's stated country, and authentications for one identity arriving from a location that never coincides with where the issued hardware reports itself. **Triage:** legitimate remote workers, contractors and support teams produce remote sessions and foreign egress routinely, so neither is suspicious alone — the discriminators are a *second*, uninventoried remote-access agent alongside the sanctioned one, and a mismatch that is systematic rather than occasional, where the hardware's location and the account's authentication origin never converge over time rather than diverging during travel.

## Update — 2026-08-31T05:45:00Z

Huntress published forensic detail from five individuals identified as likely DPRK workers across three separate 2026 investigations against the same cluster, which it names Famous Chollima — an alias this entry already carries for PurpleDelta ([Huntress, 2026-08-26](https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation)). In one of those investigations (a financial-services employer), Huntress found a PiKVM — an open-source Raspberry Pi-based KVM-over-IP device giving remote control of a host at the hardware level before the operating system even boots — together with a Guermok USB capture card that registers as a webcam and lets streamed video substitute for the operator's own camera in video calls, both connected to the same host. Huntress gives a concrete detection path for both device classes generally, based on the pattern across the incidents it has investigated this year: "Defenders can alert on Windows Security Event ID 6416 when `device_description` contains PiKVM or Guermok, and hunt the Windows registry path `HKLM\SYSTEM\CurrentControlSet\Enum\USB`, especially FriendlyName values such as PiKVM Composite Device and Guermok USB3 Video" ([Huntress, 2026-08-26](https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation)). In that same case, forensic timeline reconstruction from router connection and Windows event logs showed the laptop moving from an MSP's guest network to a residential wireless network to a fixed ethernet connection — consistent with the device becoming a rack asset in a laptop farm — with the serial console adapter and then the PiKVM connected just hours after the laptop first appeared on the residential wireless network, and the switch to a fixed ethernet connection — its last network change — following roughly 15 minutes after the PiKVM.

Huntress also adds identity-document forensics as a distinct evidence class, drawn from two further, separate cases. In the February 2026 healthcare-sector investigation (three individuals), two of the fabricated identity submissions shared the same photography angle, the same issuing police station and passport office, validity periods that matched exactly, the same recorded camera model (an iPhone 15 Pro Max), and photo-metadata timestamps within minutes of each other and a consistent device time offset — indicating one production pipeline behind both. In the same financial-services case as the PiKVM/Guermok finding, an employee's photo used on a messaging tool proved to be a stolen and face-altered image traced by reverse image search to an unrelated GitHub profile. In a third, separate case surfaced by a subsequent proactive hunt for the same hardware pattern, submitted identity documents shared a name, date of birth and driver's-license location with an unrelated individual whose mugshot had previously been published by law enforcement after an arrest — the underlying identification numbers validated as genuine, but the photograph had been swapped. That third case also used Toffeeshare (peer-to-peer file transfer), Codeshare (posting recurring Zoom meeting links with embedded passwords) and VDO Ninja (browser-based screen-capture streaming) — a cluster of consumer web tools Huntress flags as a corroborating, if individually weak, behavioural signal alongside the hardware and document indicators.

