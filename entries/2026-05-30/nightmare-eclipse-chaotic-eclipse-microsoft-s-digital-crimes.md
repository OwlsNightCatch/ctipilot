---
schema: 1
kind: vulnerability
title: "Microsoft calls Nightmare Eclipse's six uncoordinated Windows zero-day releases \"never justifiable\"; the three May drops were fixed in June 2026"
headline: "Microsoft says its Digital Crimes Unit will keep bringing cases after six leaked Windows zero-days; three fixed in June"
summary: >
  On 2026-05-27 Microsoft's Security Response Center called the uncoordinated release of six Windows
  zero-days by the researcher Nightmare Eclipse "never justifiable" and said its Digital Crimes Unit
  will keep bringing cases against attackers and those who enable them; the researcher threatened a
  further release for 14 July 2026. BlueHammer, UnDefend and RedSun had already been exploited, and
  Microsoft fixed YellowKey, GreenPlasma and MiniPlasma in the June 2026 Windows updates.
discovered_at: "2026-05-30T05:00:11Z"
event_date: 2026-05-27
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - poc-public
  - patch-available
  - actively-exploited
regions:
  - global
sectors: []
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
techniques: [T1068, T1685]
affected_products:
  - "Microsoft Windows 11"
  - "Microsoft Windows 10"
  - "Microsoft Windows Server"
  - "Microsoft Defender"
cves:
  - id: CVE-2026-45585
    cvss: "6.8"
    epss: null
    type: null
    vector: physical
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: "Windows 11 24H2, 25H2 and 26H1 and Windows Server 2025 before the June 2026 updates"
    fixed: "Windows 11 24H2 build 10.0.26100.8655, 25H2 build 10.0.26200.8655, 26H1 build 10.0.28000.2269; Windows Server 2025 build 10.0.26100.32995"
sources:
  - url: "https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more"
    publisher: The Record
    date: "2026-05-29"
    role: primary
  - url: "https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html"
    publisher: heise Security
    date: "2026-05-29"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585"
    publisher: Microsoft MSRC
    date: "2026-05-19"
    role: corroborating
  - url: "https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure"
    publisher: "Microsoft MSRC blog"
    date: "2026-05-27"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
    publisher: "BleepingComputer (MiniPlasma)"
    date: "2026-05-17"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586"
    publisher: "MSRC CVE-2026-45586"
    date: "2026-06-09"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103"
    publisher: "MSRC CVE-2020-17103"
    date: "2026-06-09"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/"
    publisher: "BleepingComputer (June 2026 fixes)"
    date: "2026-06-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Our Digital Crimes Unit will continue bringing cases against these actors and those that enable their criminal activity"
    publisher: "Microsoft MSRC blog"
    source_url: "https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure"
  - quote: "The company stopped short of directly threatening legal action"
    publisher: The Record
    source_url: "https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more"
  - quote: "The researcher threatened a further release on July 14"
    publisher: The Record
    source_url: "https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more"
  - quote: "The company is threatening lawsuits and the police."
    publisher: heise Security
    source_url: "https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html"
  - quote: "This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2020-17103"
    publisher: "MSRC CVE-2020-17103"
    source_url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references:
  - 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-30.md
updated_at: "2026-10-21T15:40:42Z"
updates:
  - at: "2026-10-21T15:40:42Z"
    run_id: 2026-10-21T1149Z-audit
    type: update
    summary: >
      Microsoft fixed YellowKey, GreenPlasma (now CVE-2026-45586) and MiniPlasma (through a re-release of
      CVE-2020-17103) in the June 2026 updates and, according to BleepingComputer, stepped back from its
      initial legal threats. Microsoft's statement is now dated to its 2026-05-27 blog post, the headline
      no longer says criminal action was threatened and the differing readings by The Record and heise are
      shown, the 14 July release is placed on the July Patch Tuesday, and YellowKey's CVE is described as
      a physical-access BitLocker bypass rather than a local privilege escalation; uncited detection
      advice is removed.
    fields: [affected_products, body, classification, cves, event_date, evidence, headline, references, sources, sourcing_note, summary, tags, techniques, title]
---

In a blog post on 2026-05-27, the Microsoft Security Response Center said the vulnerabilities known as RedSun, UnDefend, BlueHammer, YellowKey, GreenPlasma and MiniPlasma "were not responsibly disclosed" and that uncoordinated disclosures putting proof-of-concept code for unpatched flaws "into the hands of bad actors are never justifiable"; it added that its Digital Crimes Unit "will continue bringing cases against these actors and those that enable their criminal activity" ([Microsoft MSRC blog, 2026-05-27](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure)). The Record reported the post on 2026-05-29 as Microsoft's first response to the release campaign, noted that the researcher's GitHub account had since been removed, and reported that the researcher threatened a further release on 14 July 2026, the date of Microsoft's July Patch Tuesday ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)).

**Contradiction:** the outlets read the statement differently. The Record says Microsoft "stopped short of directly threatening legal action" ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)), while heise writes that the company "is threatening lawsuits and the police" ([heise Security, 2026-05-29](https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html)).

The first three drops, BlueHammer (CVE-2026-33825), UnDefend (CVE-2026-45498) and RedSun (CVE-2026-41091), all disclosed in April, have been exploited in live intrusions and appear on CISA's Known Exploited Vulnerabilities catalogue ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)); UnDefend lets a standard user block Microsoft Defender definition updates ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)). The three May drops had no patch and no confirmed exploitation when The Record reported ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)). YellowKey, tracked as CVE-2026-45585, is a BitLocker security feature bypass that needs physical access ([Microsoft MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585)). The researcher says MiniPlasma abuses the `HsmOsBlockPlaceholderAccess` routine of the Cloud Filter driver `cldflt.sys`, and that it is the flaw Google Project Zero reported in 2020 as CVE-2020-17103, "still present, unpatched"; BleepingComputer's test on a fully patched Windows 11 Pro system with the May 2026 updates opened a SYSTEM command prompt from a standard user account ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).

Microsoft fixed the three May drops on 2026-06-09: GreenPlasma as CVE-2026-45586, a CTFMON elevation of privilege that can give SYSTEM ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)), MiniPlasma by re-releasing CVE-2020-17103 with the June 2026 updates ([MSRC CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)), and YellowKey in the same Patch Tuesday ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)).

**Exposure:** Windows systems without the June 2026 updates: GreenPlasma and MiniPlasma are local privilege escalations open to any logged-on user ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)) ([MSRC CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)), and YellowKey needs physical access to a BitLocker device not protected by TPM+PIN ([Microsoft MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585)).

**Detection:** for MiniPlasma, ThreatLocker advised watching registry-modification telemetry from the EDR for changes under the user hive's `Software\Policies\Microsoft\CloudFiles\BlockedApps` key and the `.DEFAULT\Volatile Environment` key ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).

**Defender takeaway:** the decision is patch level, not the dispute: three of the researcher's six drops were exploited after release ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)), and the other three are closed by the June 2026 Windows updates ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)).

## Update — 2026-10-21T15:40:42Z

Microsoft fixed the three May drops in the June 2026 Patch Tuesday updates of 2026-06-09: YellowKey (CVE-2026-45585) and GreenPlasma, now tracked as CVE-2026-45586 ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)), and MiniPlasma through CVE-2020-17103, which Microsoft re-released "to comprehensively address the vulnerability identified by CVE-2020-17103" ([MSRC CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)). BleepingComputer also reports that Microsoft backtracked on its initial threats of legal action after blowback on social media, saying it would work with law enforcement when a security researcher "breaks the law and engages in malicious activity causing real harm to our customers" ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)).
