---
schema: 1
kind: threat
title: "Luna Moth / Silent Ransom Group (UNC3753): vishing-to-physical-access data-theft extortion against legal and professional services"
headline: "Luna Moth / Silent Ransom Group (UNC3753): vishing-to-physical-access data-theft extortion against legal and professional services"
summary: "Luna Moth / Silent Ransom Group (UNC3753) escalates to sending operatives into victim offices with USB drives — Mandiant documents a Jan–May 2026 vishing-to-data-theft extortion campaign against legal/financial firms with sub-one-hour exfiltration; one victim reportedly paid ~$20 M (Mandiant, 2026-06-05). Deep dive in § 5."
discovered_at: "2026-06-06T05:00:07Z"
event_date: 2026-06-05
run_id: 2026-06-06-d01b95fe
priority: high
immediate_action: null
tags:
  - organized-crime
  - data-breach
  - phishing
regions:
  - us
  - global
sectors:
  - legal-services
  - finance
entities:
  - "campaign:fbi-flash-csa-260526-silent-ransom-group-physical-usb-attacks-us-law-firms"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms/"
    publisher: Mandiant / Google Cloud GTIG — targeted campaign against US law firms
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/27/fbi-silent-ransom-group-law-firms-social-engineering/"
    publisher: "Help Net Security — FBI Silent Ransom Group alert, 2026-05-27"
    role: corroborating
  - url: "https://www.legalcheek.com/2026/06/weil-reportedly-pays-up-to-20-million-after-hackers-steal-client-data/"
    publisher: "Legal Cheek, 2026-06-03"
    role: corroborating
  - url: "https://securityaffairs.com/193215/cyber-crime/silent-ransom-group-srg-switching-to-dns-fast-flux-infrastructure.html"
    publisher: "Security Affairs, 2026-06-05"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
watchlist_hit: false
actions:
  - "**Harden against Luna Moth helpdesk-impersonation and physical intrusion** (. Block unauthorised RMM agents via application control, require out-of-band verification of \"IT support\" callbacks, restrict VDI/VPN to managed devices, and — given the in-person USB vector — review visitor-credentialing/escort policy and USB-write GPO on sensitive endpoints. Brief cleared/research staff on the LinkedIn/job-platform recruitment tradecraft in § 1."
migrated_from: briefs/2026-06-06.md
---

**Background and why this is a deep dive now.** Luna Moth (also Silent Ransom Group / SRG, Chatty Spider, UNC3753) is a financially-motivated data-theft-and-extortion crew that has operated since 2022, originally tied to the BazarCall callback-phishing ecosystem. Its defining trait is the absence of ransomware: it does not encrypt, it steals and threatens publication. In May 2025 the FBI publicly warned that the group had spent roughly two years targeting US law firms via callback phishing ([BleepingComputer, 2025-05-23](https://www.bleepingcomputer.com/news/security/fbi-warns-of-luna-moth-extortion-attacks-targeting-law-firms/)). This brief covered the group's **physical-intrusion escalation** on 2026-05-28, when the FBI's 2026-05-26 Cyber FLASH (CSA 260526) reported operatives entering law-firm offices to insert USB exfiltration devices when remote social engineering failed. The reason for a fuller treatment now is three genuinely-new in-window developments: (1) Mandiant published a comprehensive primary forensic analysis on 2026-06-05 that supplies the kill-chain and ATT&CK detail the earlier news-only FBI-FLASH coverage lacked; (2) a major law firm reportedly paid ~$20 M in a suppression payment; and (3) the group moved its C2 onto DNS fast-flux infrastructure. The deep dive consolidates these into the actionable picture a defender needs — it does not re-report the physical-USB tactic as novel.

**The 2026 campaign.** Mandiant attributes a January-through-May 2026 data-theft extortion campaign against dozens of US professional-, legal- and financial-services organisations to UNC3753 ([Mandiant, 2026-06-05](https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms/)). The intrusion is entirely social-engineered — there is no exploit in the chain. A benign invoice- or subscription-themed email establishes pretext; a follow-up vishing call impersonating internal IT support walks the target into hosting a screen-share session and installing a remote-access tool. Mandiant observed the actor convincing victims to install AnyDesk, Bomgar or Zoho Assist, and in one engagement to execute a "SuperOps RMM agent" via a cURL command. From there the actor pivots through BYOD or virtual desktops, enumerates file shares and document-management systems, then stages and exfiltrates using portable WinSCP or Rclone. The compression of the timeline is the operational headline: Mandiant notes that in many incidents the full sequence from first contact to data theft occurred within a single business day, and "Recently, Mandiant observed data searches, staging, and theft initiated in under an hour." Extortion follows by unbranded email, typically with a short deadline and a threat to publish on the actor's leak site.

**The physical-access escalation (first flagged 2026-05-28, now forensically confirmed).** The off-network tactic the FBI FLASH warned about is now corroborated in Mandiant's primary reporting: "individuals posing as IT technicians entered corporate offices to attempt direct exfiltration of data from an endpoint using USB storage media" (`T1052.001` Exfiltration over Physical Medium). This bypasses every network-side control — egress filtering, RMM-installer detection, cloud-upload DLP — because the data never crosses the network perimeter. Visitor management and physical-security posture become a detection surface that EDR and log telemetry cannot cover.

**Kill chain and ATT&CK mapping.** Initial access via [`T1566.004` Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004/) and [`T1204.002` User Execution](https://attack.mitre.org/techniques/T1204/002/); remote access established through [`T1219` Remote Access Software](https://attack.mitre.org/techniques/T1219/); discovery via [`T1083` File and Directory Discovery](https://attack.mitre.org/techniques/T1083/) and [`T1135` Network Share Discovery](https://attack.mitre.org/techniques/T1135/); collection and exfiltration via [`T1074` Data Staged](https://attack.mitre.org/techniques/T1074/), [`T1567.002` Exfiltration to Cloud Storage](https://attack.mitre.org/techniques/T1567/002/) and, in the physical variant, [`T1052.001`](https://attack.mitre.org/techniques/T1052/001/). The FBI's 2026-05-26 Cyber FLASH independently corroborates the campaign and underscores that, because no encryption is used and only legitimate remote-access and file-transfer tooling appears, conventional ransomware detections do not fire and few host artefacts remain ([Help Net Security, 2026-05-27](https://www.helpnetsecurity.com/2026/05/27/fbi-silent-ransom-group-law-firms-social-engineering/)).

**Why this run.** Two in-window developments make this current rather than a recap of the 2025 FBI warning. First, a major US law firm, Weil, Gotshal & Manges, reportedly paid an estimated ~$20 M suppression payment after client data was stolen from an external cloud-storage site — an unusually large, fast (reportedly within days) payout that signals how high the leverage is when the stolen material is privileged legal data ([Legal Cheek, 2026-06-03](https://www.legalcheek.com/2026/06/weil-reportedly-pays-up-to-20-million-after-hackers-steal-client-data/)). Second, the group is hardening its operational infrastructure: a 2026-06-05 report documents SRG moving its command-and-control onto **DNS fast-flux** infrastructure, improving resilience against takedown and static-indicator blocking ([Security Affairs, 2026-06-05](https://securityaffairs.com/193215/cyber-crime/silent-ransom-group-srg-switching-to-dns-fast-flux-infrastructure.html)).

**Detection and hardening (no IOCs).** Behavioural pivots: alert on RMM-agent installation (AnyDesk/Bomgar/Zoho/SuperOps) initiated from `cmd.exe`/`powershell.exe` or a cURL one-liner (Sysmon EID 1 with parent-process anomalies); flag portable WinSCP/Rclone execution from user-profile paths and high-volume outbound SSH/cloud-storage transfer sessions; watch document-management systems (e.g. iManage/SharePoint) for sudden keyword-search spikes and bulk downloads from VDI sessions. Hardening: block unauthorised RMM agents via WDAC/application control; restrict VDI/VPN authentication to corporate-managed devices with step-up MFA on BYOD; disable USB mass-storage write via GPO on sensitive endpoints; and — uniquely relevant given the in-person vector — enforce visitor credentialing and escort policies, and have help-desk staff verify any "IT support" callback against an out-of-band internal directory before granting remote or physical access. For Swiss and European legal and professional-services firms the campaign is directly transferable: the IT-helpdesk-impersonation vector is identical to the social-engineering pressure already seen across European corporate intrusions, and the physical-intrusion escalation raises a duty-of-care question that is squarely a physical-security, not just a SOC, problem.
