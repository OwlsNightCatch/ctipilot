---
schema: 1
kind: threat
horizon: operational
title: "Gunra ransomware-as-a-service: a joint six-agency advisory documents FortiOS edge exploitation, a persistent MFA backdoor built from one fixed OTP value, and a Linux encryptor whose keys can be reconstructed"
headline: "Six agencies publish the Gunra RaaS playbook — edge exploitation, an OTP-value MFA backdoor, and a recoverable Linux key"
summary: >
  The FBI, CISA, DC3, NSA, the US Secret Service and South Korea's National Police Agency published joint advisory
  AA26-222A on 2026-08-10 on Gunra, a Conti-derived double-extortion ransomware-as-a-service that opened an affiliate
  programme in January 2026 and lists victims across Europe, the Americas, the Middle East, Africa and Asia-Pacific in
  government services, utilities, healthcare, financial services, transport and critical manufacturing. Initial access
  is exploitation of the known FortiOS and FortiProxy authentication-bypass flaws CVE-2024-55591 and CVE-2025-24472 on
  internet-facing firewall and VPN appliances, after which the actors abuse scheduled tasks to create a persistent
  super-user account, and — in one case — edited the authentication-processing files on a victim's VDI authentication
  portal so that one attacker-chosen one-time-password value always validated, giving a durable MFA bypass that survives
  password resets. The advisory also records a defender-usable weakness: the Linux encryptor seeds its key generator
  with the system clock, so responders may reconstruct keys from file timestamps and recover data without paying.
discovered_at: "2026-08-11T04:36:00Z"
event_date: "2026-08-10"
run_id: 2026-08-11T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, organized-crime, actively-exploited, auth-bypass, identity, vulnerabilities]
regions: [global, europe]
sectors: [public-sector, healthcare, finance, energy, transport, manufacturing]
entities: [actor:gunra]
techniques: [T1190, T1133, T1078.001, T1078.002, T1098, T1021.001, T1021.002, T1003, T1003.003, T1550.002, T1550.003, T1040, T1539, T1556.006, T1555, T1685, T1070.003, T1678, T1622, T1679, T1049, T1083, T1106, T1005, T1114, T1530, T1560, T1567, T1048, T1486, T1490, T1047, T1059.003, T1105, T1572, T1657]
affected_products: ["Fortinet FortiOS", "Fortinet FortiProxy"]
cves:
  - id: CVE-2024-55591
    cvss: "n/a"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "specific FortiOS and FortiProxy versions — see the CVE record; the advisory does not restate the range"
    fixed: "not stated in this advisory"
  - id: CVE-2025-24472
    cvss: "n/a"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "specific FortiOS and FortiProxy versions — see the CVE record; the advisory does not restate the range"
    fixed: "not stated in this advisory"
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a"
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
    date: "2026-08-10"
    role: primary
  - url: "https://intel.breakglass.tech/post/gunra-ransomware-s-linux-variant-has-a-fatal-flaw-time-seeded-rand-makes-encrypted-files-recoverable-without-paying"
    publisher: "Breakglass Intelligence"
    date: "2026-03-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "primarily through the exploitation of known vulnerabilities in internet-facing devices"
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
  - quote: "create a new, malicious persistent user forticloud-sync with super user privileges and a hard-coded password"
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
  - quote: "the Gunra actors modified authentication processing files on the corporate VDI authentication portal server to allow successful authentication when a specific, Gunra-designated one time password (OTP) value was entered, thereby enabling the continuous bypass of multi-factor authentication (MFA)"
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
  - quote: "Defenders may leverage this to mathematically reconstruct the keys using file timestamps and recover files without paying the ransom."
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
  - quote: "Gunra ransomware appears to be based on, or significantly influenced by, the Conti ransomware source code leaked in 2022."
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
verification: multi-source
sourcing_note: "Primary is the joint advisory of six national authorities, which is also the disclosing party for the FBI and KNPA case material it describes; the Linux key-recovery weakness is corroborated by the independent research the advisory itself cites."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Search authentication-server change history on every VDI, SSL-VPN and SSO portal for edits to authentication-processing files, and re-validate that a repeated OTP value cannot authenticate — a password reset and an MFA re-enrolment do not remove this backdoor."
  - "If a Linux host has been encrypted with the .GNRA extension, preserve the encrypted files, their timestamps and the system logs before any rebuild: the advisory states the keys can be reconstructed from file timestamps, and reimaging destroys the recovery path."
migrated_from: null
---

Six authorities — the FBI, CISA, the Department of Defense Cyber Crime Center, the NSA, the US Secret Service and the Republic of Korea's National Police Agency — published a joint #StopRansomware advisory on Gunra on 2026-08-10 ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). Gunra first appeared in April 2025 and is, in the authoring agencies' assessment, based on or significantly influenced by the Conti source code leaked in 2022; as of January 2026 it runs a structured affiliate programme advertised on criminal forums, supplying a management panel, a configurable builder, cross-platform lockers and affiliate documentation, and the FBI records the group also operating under the name Golden Community and recruiting penetration testers as initial-access brokers ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). The victim set on the group's leak site spans the Americas, Europe, the Middle East, Africa and Asia-Pacific, and the advisory names government services and facilities, utilities, healthcare, financial services, critical manufacturing and transport among the affected sectors — which is why this reads directly onto the European public-sector and critical-infrastructure estate, not only onto its Korean and American case studies.

**Initial access is the edge appliance.** The FBI observed Gunra obtaining access primarily by exploiting known vulnerabilities in internet-facing firewall and VPN appliances, specifically the FortiOS and FortiProxy authentication-bypass flaws CVE-2024-55591 and CVE-2025-24472, both CWE-288 ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). The advisory points at the CVE records rather than restating affected versions, and it is explicit about what the exploitation buys: those two flaws let an actor abuse scheduled tasks on a vulnerable FortiOS firewall to create a new persistent super-user account named `forticloud-sync` carrying a hard-coded password ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). That account name is the cheapest hunt in this advisory: an appliance administrator enumeration that finds it has found an intrusion, and finding it after patching means the patch did not evict anyone. Separately, KNPA observed initial access through credential-exposure and SSH access-control weaknesses on internet-facing VPN gateways, and in one case through an SSL-VPN administrator account reachable with default credentials because no account-lockout control was configured.

**The identity plane is where the intrusion becomes durable.** After taking a network administrator's workstation and the SSL-VPN administrative console, the actors located an unused account with reach into both the internet-facing and internal networks and modified its configuration to bypass the mandatory password-change requirement, then used it ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). Against one victim they manipulated the traffic-control functionality of the SSL-VPN appliance itself to collect the credentials and session material users were sending to a corporate VDI authentication portal, then replayed the captured session cookies to impersonate legitimate users. Against the same victim they went one step further and edited the authentication-processing files on that VDI authentication portal server so that a specific attacker-chosen one-time-password value would always authenticate successfully — a standing MFA bypass rather than a stolen token. Credential access elsewhere is conventional but thorough: `secretsdump.py` against domain controllers to pull hashes out of NTDS for pass-the-hash and pass-the-ticket movement, `psexec.py` and `smbclient.py` over SMB for lateral movement, RDP into the VDI estate, and in one case theft of a symmetric key from a system access-control server that decrypted the stored passwords for every enterprise server account.

**Behavioural shape, in telemetry terms.** The operators work deliberately unsociable hours — the advisory records reconnaissance and internal activity concentrated between 22:00 and 06:00 to avoid administrator attention — and clear system and network access logs and shell command history behind them ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). Collection and exfiltration precede encryption: business documents, databases, personal data and internal mail are staged, a purpose-built executable pulls data out of Microsoft OneDrive and SharePoint, and for at least one victim compressed archives running to tens of terabytes went to a consumer file-sharing service, with 7-Zip, RClone and FileZilla among the tools observed on the group's own infrastructure. Recovery is attacked directly: volume shadow copies are deleted through WMI from a command shell before encryption, and against one victim backup and archive data was deleted at both the primary data centre *and* the disaster-recovery site, before and after deployment. The encryptor itself enumerates every drive letter through the native file-enumeration APIs, skips system directories and system-critical file extensions so the host stays bootable and the ransom note stays readable, checks for a debugger, and encrypts the surviving user data multi-threaded with ChaCha20 and RSA-4096, appending `.ENCRT`. Ransom notes land per directory and route victims to a Tor negotiation portal and an encrypted messenger with a five-to-seven-day clock.

**The one piece of genuinely good news is a cryptographic mistake.** The advisory records that as of March 2026 researchers identified a weakness in the Linux ELF variants, which append `.GNRA`: the encryption keys come from a weak pseudo-random generator seeded with the predictable `srand(time(NULL))`, and defenders may use that to mathematically reconstruct the keys from file timestamps and recover files without paying ([CISA et al., 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a); original research at [Breakglass Intelligence, 2026-03-12](https://intel.breakglass.tech/post/gunra-ransomware-s-linux-variant-has-a-fatal-flaw-time-seeded-rand-makes-encrypted-files-recoverable-without-paying)). This has an operational consequence that cuts against normal incident-response reflex: the advisory's own instruction, for a Gunra Linux incident where encryption has happened, is to preserve the encrypted files, their timestamps, the ransom notes and the system logs — because a rebuild-from-backup-and-move-on response throws away the timestamps the key reconstruction depends on. No such weakness is recorded for the Windows encryptor.

**Detection concepts.** Three of this actor's behaviours produce durable, vendor-neutral signal. In edge-appliance administrative logs and configuration audit trails, surface any newly created administrative or super-user account and any change that clears a mandatory-password-change flag on a dormant account — both are the advisory's stated persistence steps, and both are visible in configuration state rather than in transient telemetry. In authentication-server change control, file-integrity monitoring over the authentication-processing components of VDI, SSL-VPN and SSO portals is the only control that sees the OTP backdoor at all; it produces no failed logins, no impossible travel and no anomalous token, because from the portal's point of view the authentication genuinely succeeded. In endpoint process telemetry with parent lineage, the shadow-copy deletion is a command shell invoking the WMI command-line utility with a shadowcopy delete operation, and the credential-dumping and lateral-movement steps present as the Impacket family's characteristic service-creation-over-SMB and NTDS access patterns on domain controllers.

**Triage:** the tooling here is deliberately dual-use — remote-access and archiving utilities that administrators run legitimately every day — so presence alone is not the signal and the advisory says as much. The discriminators are contextual: the same remote-access agent installed on a host that has no help-desk ticket behind it, an archiving utility writing multi-gigabyte archives on a file server at 03:00, an account whose password-change requirement was cleared without a change record, and — the sharpest one — a successful multi-factor authentication in which the presented one-time-password value is identical across sessions or across users. Legitimate one-time codes never repeat; that is the whole property they exist for.

**Defender takeaway:** two of Gunra's steps outlive the obvious remediation. Patching the FortiOS or FortiProxy appliance does not delete an administrative account the actor already created on it, and resetting user passwords or re-enrolling second factors does not remove an authentication-portal file that has been edited to accept a fixed code. Any organisation that ran an unpatched FortiOS or FortiProxy appliance internet-facing through the exploitation window for these two flaws owes itself an appliance-configuration review and an integrity check of its authentication portals, not merely a version check. Where a Linux host has already been encrypted, preserve the evidence before rebuilding — the recovery path documented here depends on file timestamps that a reimage destroys.
