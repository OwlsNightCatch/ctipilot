---
schema: 1
kind: vulnerability
title: "Chaotic Eclipse turns its zero-day drops on third-party security products: unpatched local privilege escalation in CrowdStrike Falcon and Avast, with working proof-of-concept code public"
headline: "Unpatched SYSTEM escalations in CrowdStrike Falcon and Avast, with public exploit code and no fix: the only Falcon control is switching a prevention feature off"
summary: >
  The pseudonymous researcher tracked as Chaotic Eclipse / Nightmare Eclipse published working
  local-privilege-escalation proof-of-concept code against three security products in early September
  2026, without vendor notice. FalconFlank abuses CrowdStrike Falcon Sensor's Office malicious-macro
  remediation to reach SYSTEM on fully patched Windows 11 25H2 and Windows Server 2025; CrowdStrike
  has no fix and advises disabling the "Microsoft Office File Suspicious Macro Removal Windows"
  policy setting. PrettyPrague dumps the SAM database and spawns a SYSTEM shell through the Avast
  Sandbox component, with Gen Digital still developing a patch. Kaspersky's HardBreacher is fixed.
  No CVEs are assigned to any of the three.
discovered_at: "2026-09-06T14:00:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-06T1308Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, priv-esc, lpe, poc-public, no-patch]
regions: [global, europe]
sectors: [public-sector, technology]
entities: ["actor:nightmare-eclipse"]
techniques: [T1068, "T1003.002"]
affected_products: ["CrowdStrike Falcon", "Avast Antivirus", "Kaspersky Endpoint Security for Windows"]
cves: []
sources:
  - url: "https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html"
    publisher: "The Hacker News"
    date: "2026-09-03"
    role: primary
  - url: "https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike"
    publisher: "Truesec"
    date: "2026-09-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We are actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting"
    publisher: "The Hacker News (quoting a CrowdStrike spokesperson)"
  - quote: "As of now the PoC works in a fully updated windows 11 25H2 / Windows Server 2025 with Crowdstrike Falcon – Phase 3 Optimal Protection with “Microsoft Office file malicious macro removal” setting."
    publisher: "Truesec"
  - quote: "Gen was recently made aware of a security vulnerability affecting a subset of Gen products, including Avast Antivirus, that could allow an attacker to elevate their system privileges. We immediately initiated our security response procedures and are actively developing a patch."
    publisher: "The Hacker News (quoting a Gen Digital spokesperson)"
verification: multi-source
sourcing_note: "The Hacker News carries first-party statements it obtained directly from CrowdStrike, Gen Digital and Kaspersky, which is what establishes the patch status of each product; Truesec independently describes the FalconFlank preconditions and the mitigation from its own reading. Reliability B rather than A because no vendor has published an advisory of its own: CrowdStrike points customers to a support-portal Tech Alert this entry cannot read, and Gen Digital has issued only the statement quoted here. Credibility 2 for the entry as a whole: only the FalconFlank portion has two parties describing it consistently, while PrettyPrague, HardBreacher and GreenSection rest on The Hacker News alone, and the rating covers the weakest of the four rather than the strongest. The proof-of-concept repositories are deliberately not linked."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Disable the \"Microsoft Office File Suspicious Macro Removal Windows\" prevention setting in CrowdStrike Falcon next-gen antivirus policy (under Clean infected Microsoft Office files) on every managed endpoint until CrowdStrike ships a fix; Cloud Anti-malware for Microsoft Office Files continues to block malicious macros with that setting off."
  - "Confirm which Gen Digital antivirus products are deployed anywhere in the estate, including on unmanaged or contractor endpoints: Avast is confirmed affected with no patch yet, and the researcher states AVG and Norton may share the flaw."
updates: []
migrated_from: null
---

The pseudonymous researcher tracked here as Nightmare Eclipse, and by The Hacker News under the further aliases Chaotic Eclipse, INFINITE NIGHTMARE and MSNightmare, spent 2026 publishing working proof-of-concept exploits for Windows and Microsoft Defender privilege escalations without giving the vendor advance notice. In early September the target set changed: three of the four latest drops are against third-party endpoint security products rather than Microsoft's, and two of them have no fix ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). That shift is what makes this an operational matter for estates that never had Defender in scope.

FalconFlank abuses CrowdStrike Falcon Sensor's Office malicious-macro remediation path. The remediation routine runs at high privilege in order to clean an infected document in place, and the exploit turns that cleanup into a low-privileged account's route to SYSTEM. Truesec, reading the release independently, records the preconditions precisely: the proof-of-concept "works in a fully updated windows 11 25H2 / Windows Server 2025 with Crowdstrike Falcon – Phase 3 Optimal Protection with 'Microsoft Office file malicious macro removal' setting" ([Truesec, 2026-09-04](https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike)). A CrowdStrike spokesperson told The Hacker News the company is "actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting", adding that customers "remain protected through the Cloud Anti-malware for Microsoft Office Files settings" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). There is no patch and no CVE; the control on offer is turning a prevention feature off, which Truesec notes means malicious macros will no longer be replaced in place while cloud-side blocking continues ([Truesec, 2026-09-04](https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike)).

PrettyPrague is the same shape against a different vendor. The researcher describes it as dumping the SAM database "by abusing a vulnerability in Avast Sandbox" and spawning a full SYSTEM shell against fully patched Avast Antivirus on a patched Windows 11 25H2 host, and states a belief that other Gen Digital products including AVG and Norton are affected ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). Gen Digital confirmed a vulnerability "affecting a subset of Gen products, including Avast Antivirus, that could allow an attacker to elevate their system privileges" and said it is "actively developing a patch", without naming which further products are in scope ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). The third drop, HardBreacher against Kaspersky Endpoint Security for Windows 14.0.0.504, is the one that is resolved: Kaspersky told the same outlet the fix ships through an automatic database update or a manually triggered one ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). A fourth release, GreenSection, is described only as an NVIDIA memory-corruption bug that crashes any application using Vulkan or OpenGL, rather than a privilege escalation ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)).

The releases are unco-ordinated by the researcher's own account, and the reason they give matters for timeline planning rather than attribution. The Hacker News reports the researcher claiming that Microsoft continues to ignore them and refuses to engage in "any sort of communication", and quotes them saying they "can't even report the bugs I find to their respective vendors because of the restrictions by Microsoft" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). The same reporting quotes them planning the timing of future drops: "Think I will start publishing bugs for third-parties in that window where Patch Tuesday isn't released yet" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). For a defender that means there is no embargo to wait out and no co-ordinated patch date, the gap between publication and a vendor fix is open-ended, and by the researcher's own stated intent the next drop is likelier to land in the days before a Patch Tuesday than after one.

**Defender takeaway:** an endpoint agent's own remediation logic runs at SYSTEM on every managed host, which makes a flaw in it a full-estate local privilege escalation rather than a single-host bug, and it sits precisely where a defender is least likely to be watching. For Falcon, apply CrowdStrike's own guidance now and record the change as a temporary reduction in on-host macro remediation to be reversed when a fix ships. For Avast and its Gen Digital siblings there is no vendor control yet, so the practical step is inventory: establish where those products run, particularly on endpoints outside central management, and weigh whether an unpatched SYSTEM escalation there is acceptable.

**Triage:** these exploits ride a security agent's legitimate high-privilege routines, so the signal is not the agent acting with privilege, which it always does. What separates abuse is what the privileged action produces: a remediation or sandbox operation followed by a process spawning from an unexpected parent under a low-privileged user's session, a write into a system directory that the agent's normal cleanup does not target, or SAM access originating from the antivirus process tree rather than from a backup or credential-management workflow. Because the code is public and the researcher notes detections may already exist, an endpoint alert naming the agent's own remediation component is worth treating as an exploitation attempt rather than a product fault.
