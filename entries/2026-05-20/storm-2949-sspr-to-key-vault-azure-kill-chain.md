---
schema: 1
kind: threat
title: "Storm-2949: SSPR abuse of four privileged users turned into a data-theft sweep across Microsoft 365, Key Vault, SQL, Storage and Azure VMs"
headline: "Storm-2949 hijacked privileged Entra ID accounts through SSPR abuse, then mined Azure management features for data"
summary: >
  Microsoft Threat Intelligence reported on 2026-05-18 that Storm-2949 abused Microsoft's Self-Service
  Password Reset to take over four privileged Entra ID accounts at one organization, re-enrolled MFA on
  its own devices, and used their Azure RBAC roles to pull App Service publishing profiles, Key Vault
  secrets, SQL and Storage data and VM access through Run Command and VMAccess. The actor relied mostly on
  legitimate cloud management features, installed ScreenConnect on VMs, aimed at mass data exfiltration
  and, per Microsoft, did not extort and shows no link to ShinyHunters.
discovered_at: "2026-05-20T05:00:14Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: high
immediate_action: null
tags:
  - identity
  - cloud
  - phishing
  - data-breach
regions:
  - global
sectors: []
entities:
  - "campaign:storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain"
  - "actor:storm-2949"
techniques: [T1621, T1078.004, T1556.006, T1098.005, T1087.004, T1098.001, T1530, T1213.002, T1555.006, T1686.001, T1651, T1136.001, T1552.005, T1685, T1219, T1036.004, T1685.005, T1070.003, T1070.004, T1082, T1087.002, T1069.002, T1552.001, T1552.004]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-05-18"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/"
    publisher: "BleepingComputer"
    date: "2026-05-19"
    role: corroborating
  - url: "https://learn.microsoft.com/en-us/entra/identity/authentication/howto-sspr-reporting"
    publisher: "Microsoft Learn"
    date: "2025-03-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We assess with high confidence that Storm-2949 leveraged a social engineering technique consistent with known abuses of Microsoft’s Self-Service Password Reset (SSPR) process."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/"
  - quote: "Over the span of four minutes, the threat actor successfully manipulated Key Vault access configurations and accessed dozens of secrets within the said Key Vault."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/"
  - quote: "The script then installed the ScreenConnect remote monitoring and management (RMM) tool obtained from threat actor-controlled infrastructure."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/"
  - quote: "Tanmay Ganacharya, VP of Microsoft Security Research, told BleepingComputer that current Storm-2949 activity does not indicate a connection to ShinyHunters or an affiliate of the group."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/"
verification: single-source
sourcing_note: >
  Microsoft Threat Intelligence is the only assessor, describing its own incident response to an unnamed
  victim; BleepingComputer restates it and adds Microsoft's statements on extortion and ShinyHunters.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-10-21T20:22:14Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Microsoft does not call Storm-2949 financially motivated: its objective was mass data exfiltration,
      Storm is a temporary designation, no extortion was seen and there is no ShinyHunters link, and the
      intrusion was not binary-free, since ScreenConnect was installed on VMs, Defender weakened and event
      logs cleared. SSPR abuse took over four privileged accounts on a hedged phishing assessment,
      unsourced hunting operation names and sector claims are dropped, and the analysis is rebuilt from
      Microsoft's write-up with exposure, detection and takeaway guidance.
    fields: [body, classification, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification]
---

Microsoft Threat Intelligence published its account of an intrusion by Storm-2949 on 2026-05-18: a campaign whose singular focus was to exfiltrate as much sensitive data as possible from one target organization's high-value assets, across Microsoft 365, file hosting and the Azure production environment ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). The actor did not rely on traditional malware but on legitimate cloud and Azure management features that blend into administrative behavior ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). Storm is Microsoft's temporary designation for activity not yet classified, and Microsoft saw no follow-on extortion and no link to ShinyHunters ([BleepingComputer, 2026-05-19](https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/)).

**Identity takeover.** Microsoft assesses with high confidence that Storm-2949 abused Self-Service Password Reset (SSPR): the actor starts a reset on a targeted user's behalf and persuades the user to approve the resulting MFA prompts, likely through an organized and convincing phishing scheme, for example by posing as IT support ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). It then reset the password, removed the user's phone, e-mail and Authenticator methods and enrolled Microsoft Authenticator on its own device, locking the user out; the victims included IT personnel and senior leadership, and the actor repeated the process until it held four accounts ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

**Directory discovery and Microsoft 365 theft.** A custom Python script enumerated users and applications through Microsoft Graph to find privileged identities, and an attempt to add credentials to a service principal failed for lack of permissions ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). The actor searched OneDrive and SharePoint for VPN configuration and remote-access documents and in one instance downloaded thousands of files from the OneDrive web interface in a single action ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

**Azure control plane.** With privileged custom RBAC roles on several subscriptions, the actor called `microsoft.Web/sites/publishxml/action` to retrieve the publishing profiles of secondary App Service apps, which often hold FTP, Web Deploy and Kudu credentials; with an Owner role over one Key Vault it changed the vault's access configuration and read dozens of secrets within four minutes, then used them to take over the primary production web app and change its password ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). It opened SQL server firewall rules with `microsoft.sql/servers/firewallrules/write` and deleted them after taking data, opened storage account network access to its own addresses with `microsoft.storage/storageaccounts/write`, and retrieved account keys and SAS tokens with `microsoft.Storage/storageAccounts/listkeys/action` to download blobs over several days with an Azure SDK script ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

**Virtual machines and endpoints.** Through the VMAccess extension the actor created a local administrator on a VM, and through Run Command it tried to use the VM's managed-identity token from the Instance Metadata Service against Key Vault, which failed on permissions ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). A Run Command PowerShell script then disabled Defender Antivirus protections, installed ScreenConnect from actor infrastructure under names resembling Windows components, and cleared event logs, command history and temporary files; over ScreenConnect the actor ran host and domain discovery, exfiltrated .pfx certificate files and scanned file shares for password strings ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

**Exposure:** Entra ID tenants where users with privileged Azure RBAC roles over Key Vault, App Service, SQL, Storage or VMs can reset their password through SSPR; Microsoft names no sector, country or victim ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

**Detection:** identity audit logs first: Entra ID records reset and registration activity in the Self-Service Password Management audit category ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-sspr-reporting)), and the pattern here is a reset followed by removal of every existing method and a new Authenticator registration ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). Then the Azure activity log for the operations above from one principal (publishing-profile retrieval, Key Vault access changes, SQL firewall and storage network rule writes, key listing, VMAccess and Run Command), and on VMs the disabling of Defender protections, a new remote-access service and cleared event logs ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). Evicting the accounts is not enough: the actor's Authenticator registrations, the web app password it changed, the Key Vault secrets it read and the storage keys it listed all stay usable until they are removed or rotated.

**Defender takeaway:** require phishing-resistant MFA for administrators and privileged users and make sure every privileged user already has a registered MFA method, which blocks the malicious registration step; limit publishing-profile access, Run Command and VMAccess through RBAC, and prefer Azure RBAC over Key Vault access policies ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

## Correction — 2026-10-21T20:22:14Z

Storm-2949 is not described as financially motivated: Microsoft's stated objective for the campaign is mass data exfiltration ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)), Storm is its temporary designation for unclassified activity, and it observed no extortion and sees no link to ShinyHunters ([BleepingComputer, 2026-05-19](https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/)). The intrusion did not stay free of binaries: on VMs the actor installed ScreenConnect, weakened Defender Antivirus and cleared event logs ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)). SSPR abuse took over four privileged accounts, not one, and Microsoft hedges the social engineering as consistent with SSPR abuse and likely a phishing scheme, giving an IT-support call only as an example ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)).

At Key Vault the actor changed the vault's access configuration and read dozens of secrets, connection strings and identity credentials among them ([Microsoft, 2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)); the Key Vault operation names given earlier for hunting are not in Microsoft's write-up, and Entra ID records SSPR activity in the Self-Service Password Management audit category ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-sspr-reporting)). Microsoft names no victim sector or country.
