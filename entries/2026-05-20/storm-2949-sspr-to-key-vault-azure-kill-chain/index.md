---
schema: 1
kind: threat
title: Storm-2949 SSPR-to-Key-Vault Azure kill chain
headline: Storm-2949 SSPR-to-Key-Vault Azure kill chain
summary: "Storm-2949 turns one SSPR-abused identity into a cloud-wide breach across Entra ID → M365 → App Service → Key Vault → SQL → Storage → Azure VMs — no malware required. Microsoft Threat Intelligence published the full incident analysis on 2026-05-18;."
discovered_at: "2026-05-20T05:00:14Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: high
immediate_action: null
tags:
  - identity
  - cloud
  - phishing
  - organized-crime
regions:
  - global
  - europe
sectors:
  - public-sector
  - healthcare
  - finance
  - telco
entities:
  - "campaign:storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain"
  - "actor:storm-2949"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/"
    publisher: "Microsoft Threat Intelligence — Storm-2949, 2026-05-18"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/"
    publisher: "BleepingComputer, 2026-05-19"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
---

Microsoft Threat Intelligence published the full Storm-2949 incident analysis on [2026-05-18](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/), with [BleepingComputer corroboration on 2026-05-19](https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/). The actor is financially motivated, currently unattributed to a nation-state nexus, and the engagement notable for what it does **not** contain: no traditional malware, no exploits, no zero-days — only end-to-end abuse of legitimate Azure / M365 management features. The incident is operationally relevant to every Swiss / EU organisation running production workloads on commercial Azure or Azure Government, which now spans much of federal admin, cantonal IT, healthcare, finance, telco, and education.

**Background.** SSPR (Self-Service Password Reset) social-engineering as an initial-access vector has been documented in passing by several vendors since 2024 — the technique typically pairs a legitimate SSPR initiation by the attacker with a phone call posing as IT support, getting the victim to approve an MFA prompt the attacker triggered. What Microsoft's 2026-05-18 write-up adds is the **post-identity cloud kill chain**: the same engagement walks from SSPR abuse through Entra ID, Microsoft Graph reconnaissance, OneDrive / SharePoint exfiltration, App Service Kudu console pivoting, Key Vault secret theft, SQL firewall mutation, Storage SAS-token theft, and finally on to Azure VM credential harvesting and on-prem reconnaissance — a single chain crossing five Azure resource providers without dropping a binary.

**Phase 1 — Identity (SSPR + voice phishing).** Storm-2949 initiated the Microsoft SSPR flow for selected target users (IT personnel and senior leadership), then contacted those users posing as internal IT support to walk them through approving the resulting MFA prompts. With four accounts compromised, the actor: reset passwords, removed existing MFA methods (phone, email, Authenticator registrations), enrolled Microsoft Authenticator on attacker-controlled devices, and locked the legitimate users out. Maps to [T1078.004 (Valid Accounts: Cloud Accounts)](https://attack.mitre.org/techniques/T1078/004/), [T1556.006 (Modify Authentication Process: Multi-Factor Authentication)](https://attack.mitre.org/techniques/T1556/006/), and [T1098.005 (Account Manipulation: Device Registration)](https://attack.mitre.org/techniques/T1098/005/). Microsoft notes: ["Storm-2949 leveraged a social engineering technique consistent with known abuses of Microsoft's Self-Service Password Reset (SSPR) process. In such attacks, a threat actor initiates the SSPR process on behalf of a targeted user and subsequently employs social engineering tactics to persuade the user to complete multifactor authentication (MFA) prompts that appear to be legitimate."](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/)

**Phase 2 — M365 discovery and exfiltration.** With four hijacked identities, the actor authenticated to Microsoft Graph from custom Python tooling, enumerated users, roles, applications, and service principals across the tenant, and exfiltrated thousands of files from OneDrive and SharePoint — selecting VPN configuration documents and remote-access procedures as a lateral-movement springboard. Maps to [T1530 (Data from Cloud Storage)](https://attack.mitre.org/techniques/T1530/) and [T1083 (File and Directory Discovery)](https://attack.mitre.org/techniques/T1083/) via Graph.

**Phase 3 — Azure App Service to Key Vault pivot.** Using a privileged custom Azure RBAC role accessible to one of the compromised principals, Storm-2949 invoked `microsoft.Web/sites/publishxml/action` on secondary App Service instances — auxiliary apps hosting internal authentication and API surfaces — extracting basic-auth FTP / Web Deploy credentials. From there the actor accessed the Kudu management console of those App Services (which expose a shell and file-system inside the App Service container). They then pivoted to **Azure Key Vault** using the **Owner** role (which one of the compromised user's Azure RBAC permissions granted over a specific Key Vault), modified access policies to grant themselves vault data-plane permissions, and exfiltrated dozens of secrets — database credentials, connection strings, third-party API keys. Microsoft: ["The threat actor pivoted to the organization's Azure Key Vault estate — an environment more likely to centralize sensitive secrets and offer indirect access to production systems."](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/) Maps to [T1552.001 (Unsecured Credentials: Credentials In Files)](https://attack.mitre.org/techniques/T1552/001/) and [T1021.007 (Remote Services: Cloud Services)](https://attack.mitre.org/techniques/T1021/007/).

**Phase 4 — Azure SQL and Storage.** The actor mutated **SQL firewall rules** via `microsoft.sql/servers/firewallrules/write` to open access from attacker IPs, queried databases over those rules, then deleted the rules to remove the artefact — defence evasion via the cloud control plane. In parallel, **Storage account network ACLs** were mutated via `microsoft.storage/storageaccounts/write` to allow attacker IPs, **SAS tokens and account keys** were retrieved via `microsoft.Storage/storageAccounts/listkeys/action`, and large-blob downloads were executed over multiple days using a custom Python script against the Azure Storage SDK. Maps to [T1562.007 (Impair Defenses: Disable or Modify Cloud Firewall)](https://attack.mitre.org/techniques/T1562/007/), [T1530 (Data from Cloud Storage)](https://attack.mitre.org/techniques/T1530/), and [T1041 (Exfiltration Over C2 Channel)](https://attack.mitre.org/techniques/T1041/).

**Phase 5 — Azure VM compromise.** Storm-2949 deployed the **VMAccess** Azure VM extension to create new local admin accounts on selected VMs and used **Azure Run Command** to execute payloads for in-VM credential harvesting and on-prem Active Directory reconnaissance via the VM's network presence. Maps to [T1078.004](https://attack.mitre.org/techniques/T1078/004/) (cloud-managed admin via VMAccess) and [T1021.007](https://attack.mitre.org/techniques/T1021/007/) (Run Command as cloud remote-services execution).

**Detection concepts.** The kill chain crosses identity, App Service, Key Vault, SQL, Storage, and VM extensions; endpoint-only coverage will miss the entire chain. The detection layers that matter are cloud-side:

- **Entra ID Sign-In + Audit Logs.** Hunt for SSPR flow initiations (`category: SelfServicePasswordReset`) followed within the same session by MFA-method removal, new Authenticator-device enrollment, and sign-in from a new IP / device. Alert on rapid Graph-API user / role / app enumeration (hundreds of `users`, `applications`, `servicePrincipals` reads in a short window).
- **Microsoft Defender for Cloud.** Alerts on Key Vault access-policy modifications, SQL firewall-rule mutations, Storage account network-access-rule changes, App Service `publishxml` extraction, and VM extension deployments. Each is individually noisy; the time-correlation is the signal.
- **Azure Audit Log (Activity Log).** Hunt for the sequence `Add-AzKeyVaultCertificate` / `microsoft.keyvault/vaults/accessPolicies/write` → `microsoft.sql/servers/firewallrules/write` → `microsoft.storage/storageaccounts/write` → `microsoft.Storage/storageAccounts/listkeys/action` from the same principal within a short window.
- **App Service / Kudu access logs.** Unusual SCM (Source Control Manager) authentication events from non-developer IPs and unexpected Kudu shell-command issuance.

**Hardening / mitigation.**

- **Require phishing-resistant MFA (FIDO2 / certificate-based) for all privileged roles** — admin roles, Key Vault Contributor, Storage Account Contributor, SQL Server Contributor, App Service Contributor. SSPR-via-Authenticator-prompt is a number-matching MFA path; phishing-resistant binds eliminate it.
- **Restrict SSPR to pre-registered recovery methods only.** Conditional Access policies that block SSPR registration of new methods without an interactive sign-in from a compliant device close the device-enrollment hijack pattern.
- **Constrain Owner and Key Vault Contributor role assignments** — both grant management-plane modification of access policies. Microsoft notes Storm-2949 exercised the Owner role over a specific Key Vault to mutate access policies and grant itself data-plane access; Key Vault Contributor confers the same management-plane mutation capability. Where Key Vault data access is needed, use the data-plane RBAC model (Key Vault Secrets User / Reader) rather than management-plane Owner / Contributor.
- **Enable Defender for Cloud across Key Vault, App Service, Storage, and SQL** — Storm-2949's chain triggers built-in alerts at every step; absent the per-service Defender plans, those events sink into the Activity Log without alerting.
- **Audit custom Azure RBAC roles** specifically for `microsoft.Web/sites/publishxml/action`, `microsoft.sql/servers/firewallrules/write`, `microsoft.storage/storageaccounts/write`, `microsoft.Compute/virtualMachines/extensions/write`, and `microsoft.Compute/virtualMachines/runCommand/action` — these are the cloud-control-plane verbs the kill chain depends on.

**Why this matters for Swiss / EU public-sector defenders.** Storm-2949 specifically targeted IT personnel and senior leadership — the audience-of-one pattern most likely to clear MFA prompts under social-engineering pressure. The kill chain is generic Azure / M365 abuse; nothing in it is tenant-specific. Any Swiss federal, cantonal, healthcare, or finance organisation running Azure has the resource types Storm-2949 walked through. The mitigations are also generic: phishing-resistant MFA on privileged roles, SSPR Conditional Access, Defender-for-Cloud enablement on the four affected services. None of those require breaking changes — they're configuration work, primarily.
