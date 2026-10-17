---
schema: 1
kind: threat
title: "Star Blizzard's RedFlick: mass-mailed think-tank event invitations, compromised-website senders and a single-click scheduled-task chain to the CosmicPulse backdoor"
headline: "Microsoft: Star Blizzard adds mass mailings and a one-click scheduled-task chain to its CosmicPulse backdoor delivery"
summary: >
  Microsoft Threat Intelligence reports that the Russian state actor Star Blizzard has moved from purely
  targeted spear-phishing to at least 13 large-scale campaigns since January 2026, sent from accounts on
  compromised WordPress and cPanel websites and lured with closed-door think-tank event invitations. Its new
  RedFlick delivery chain needs one user interaction and installs the CosmicPulse Python backdoor through
  scheduled tasks; Microsoft counts over 100 affected organizations, primarily in the US and UK, and names
  governments and diplomatic and multilateral bodies among the targets.
discovered_at: "2026-09-30T04:42:00Z"
updated_at: null
event_date: "2026-09-29"
run_id: 2026-09-30T0404Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, russia-nexus]
regions: [global, us, uk]
sectors: [public-sector, finance]
entities: ["actor:star-blizzard", "campaign:star-blizzard-redflick-2026", "malware:cosmicpulse"]
techniques: [T1566, T1566.001, T1584.004, T1204.002, T1036.008, T1202, T1059.001, T1059.003, T1059.006, T1053.005, T1036.004, T1218.002, T1105, T1140, T1112, T1027.003]
affected_products: ["Microsoft Windows"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-09-29"
    role: primary
  - url: "https://cyberscoop.com/microsoft-star-blizzard-redflick-phishing-campaigns/"
    publisher: "CyberScoop"
    date: "2026-09-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Since January 2026, Microsoft observed at least 13 distinct large-scale phishing campaigns targeting primarily NGOs, think tanks, and government organizations worldwide."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/"
  - quote: "By contrast, the RedFlick infection flow only requires a single user interaction, reducing friction in the compromise process."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/"
  - quote: "Microsoft Threat Intelligence assesses with high confidence that these websites have been compromised by Star Blizzard for this purpose."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/"
  - quote: "The emails in these RedFlick campaigns are often sent in bulk."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/"
verification: single-source
sourcing_note: >
  Single-sourced to Microsoft Threat Intelligence's own telemetry; CyberScoop restates the report without independent
  observation. The attribution to the FSB, the tooling names and the mass-mailing-platform inference are Microsoft's.
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
updates: []
migrated_from: null
---

Microsoft Threat Intelligence reports that Star Blizzard, which CISA attributes to Russia's FSB Centre 18 ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)) and which CyberScoop lists under the names SEABORGIUM, Callisto Group, TA446 and COLDRIVER ([CyberScoop, 2026-09-29](https://cyberscoop.com/microsoft-star-blizzard-redflick-phishing-campaigns/)), has since January 2026 added large-scale phishing to its targeted spear-phishing: at least 13 distinct campaigns of tens to hundreds of emails each, aimed primarily at NGOs, think tanks and government organizations, with Ukrainian individuals and institutions, diplomatic and multilateral bodies and financial organizations also named ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). Microsoft counts over 100 affected organizations, primarily in the United States and United Kingdom, and infers the actor now uses a mass-mailing platform ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). The lures are invitations to closed-door roundtables that borrow the names of real think tanks, often written to look like internal mail from the target's own organization; the first message is usually without an attachment, and a reply is answered with a password-protected RAR or ZIP archive whose password is shown as an image, although the Ukraine-focused campaigns and a few later ones attached the lure directly ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). Since March the sending accounts sit on WordPress and cPanel websites, replacing free Proton and Microsoft consumer mailboxes, and Microsoft assesses with high confidence that Star Blizzard compromised those sites ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). One March campaign instead gave respondents a link to the DarkSword iOS backdoor installation, which Microsoft says Proofpoint reported, and a mid-August campaign employed steganography to conceal identifiers ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)).

The delivery chain changed three times in 2026 and replaced the ClickFix flow of earlier campaigns with one that needs a single user interaction ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). From mid-January, a virtual hard disk file in the archive held a shortcut disguised as a PDF that started a hidden console window and a batch script; the script opened a decoy PDF and ran the SSH client with PermitLocalCommand enabled to download and run a remote MSI, which created a scheduled task that used control.exe to fetch the CosmicPulse downloader disguised as a Control Panel applet ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). From April the MSI created three scheduled tasks named like network components: one beaconing host and user names to the command server and running a remote DLL through a WebDAV path, one preparing WebDAV support, and one running control.exe against a remote path to execute the next stage ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). From July, a shortcut used conhost.exe and curl to download a PDF, and PowerShell then searched that file for a marker, decoded the Base64 blob that follows it and ran the result to fetch another MSI ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)). The downloader fetches two ZIP archives, stores an encrypted AES key in a registry key under HKCU\Software\Classes, and a Python bootstrapper decrypts and runs the CosmicPulse payload, which is publicly tracked as YESROBOT ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)).

Where each step surfaces: mail-flow logs show bulk initial-contact invitations and a follow-up with a password-protected archive; process-creation telemetry with parent lineage shows a hidden console window spawning a command shell that runs an SSH client, msiexec started from a script, control.exe loading a remote path, and conhost.exe with curl downloading a PDF that PowerShell then parses; scheduled-task creation events show tasks named like network components, one pointing at a WebDAV path; registry telemetry shows a key written under HKCU\Software\Classes. Microsoft's recommended controls include phishing-resistant authentication, Conditional Access, Safe Links and Safe Attachments with zero-hour auto purge, EDR in block mode, and Windows Firewall rules restricting outbound SSH connection attempts to what the business needs ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)).

**Triage:** Microsoft's discriminators for this actor are a sender whose organization name appears only in the local part of the address on an unrelated domain, bulk delivery, an initial message that is usually without an attachment and a follow-up archive after a reply ([Microsoft Threat Intelligence, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)).

**Defender takeaway:** the endpoint chain is the durable detection surface, because sender infrastructure now rotates across compromised websites: an SSH client launched by a script on a workstation, a scheduled task whose action is control.exe or a WebDAV path, and a PDF parsed by PowerShell rather than opened are each worth an alert. Government officials, diplomatic and policy staff are among the target profiles Microsoft names; Microsoft names no Swiss victim.
