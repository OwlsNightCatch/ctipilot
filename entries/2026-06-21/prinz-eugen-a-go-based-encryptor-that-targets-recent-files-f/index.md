---
schema: 1
kind: threat
title: "Prinz Eugen: a Go-based encryptor that targets recent files first and leaves no ransom note"
headline: "Prinz Eugen: a Go-based encryptor that targets recent files first and leaves no ransom note"
summary: "A new Go-based ransomware family, Prinz Eugen, encrypts most-recently-modified files first and drops no ransom note — confirmed against a French public-sector workforce agency. Initial access is stolen RDP credentials, followed by backdoor admin-account creation and RemotePC RMM abuse for lateral movement (Malwarebytes ThreatDown, 2026-06-17). The no-note, out-of-band-extortion model defeats ransom-note-based detection — hunt on RDP-logon-then-admin-account-creation and .prinzeugen write fan-out instead."
discovered_at: "2026-06-21T04:55:04Z"
event_date: 2026-06-20
run_id: 2026-06-21-2b75e32c
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - europe
  - global
sectors:
  - finance
  - public-sector
  - education
entities:
  - "campaign:prinz-eugen-ransomware"
cves: []
sources:
  - url: "https://www.threatdown.com/blog/prinz-eugen-ransomware-a-deep-dive-into-a-new-go-based-encryptor/"
    publisher: Malwarebytes ThreatDown
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-prinz-eugen-ransomware-prioritizes-recent-files-for-encryption/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: The Go-based malware prioritizes the encryption of the most recently modified files.
    publisher: Malwarebytes ThreatDown
  - quote: "A new ransomware operation named 'Prinz Eugen' prioritizes recently modified files for encryption and leaves no ransom note on the system."
    publisher: BleepingComputer
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-21.md
---

Malwarebytes ThreatDown published a technical deep dive into Prinz Eugen, a Go-based ransomware operation active since at least April 2026 and operating as a standalone crew rather than a ransomware-as-a-service affiliate ([Malwarebytes ThreatDown, 2026-06-17](https://www.threatdown.com/blog/prinz-eugen-ransomware-a-deep-dive-into-a-new-go-based-encryptor/)). A confirmed European victim — Transitions Pro Centre Val de Loire, a French state-funded workforce-transition agency — puts it squarely in scope for a Swiss/EU public-sector SOC, alongside victims reported in finance and US automotive services. Two design choices make it worth a defender's attention: it leaves **no ransom note on disk**, and it **encrypts the most-recently-modified files first** ([BleepingComputer, 2026-06-20](https://www.bleepingcomputer.com/news/security/new-prinz-eugen-ransomware-prioritizes-recent-files-for-encryption/)).

**Kill chain.** Initial access is via stolen RDP credentials ([T1133 External Remote Services](https://attack.mitre.org/techniques/T1133/), [T1021.001 Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/)). Post-access is hands-on-keyboard: the operator creates a backdoor local admin account (the documented command line is `net user admin germania /add`, [T1136.001 Create Account: Local Account](https://attack.mitre.org/techniques/T1136/001/)), stages the encryptor as `servertool.exe` (downloaded via Chrome into the user's Music folder, [T1105 Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)), and abuses the legitimate RemotePC (IDrive) RMM tool plus enterprise platforms (SharePoint, OneDrive, Citrix) for lateral movement and to blend with normal activity. Encryption is [T1486 Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/); extortion is conducted entirely out-of-band (no on-host note), defeating the common detection heuristic of alerting on dropped ransom-note files.

**Encryption internals.** The Go binary encrypts with ChaCha20-Poly1305 (AEAD) using a 32-byte master key and per-file random IVs, with a three-stage key-derivation chain — Argon2id → SHA-256 → HKDF-SHA256. Encrypted files carry a `CHV1` magic header and the `.prinzeugen` extension. After encryption the binary zeroes its hardcoded key material and forces garbage collection before self-deleting, frustrating post-incident key recovery from memory. The "recent files first" ordering is the operationally significant detail: it maximises impact on active business data while shortening the encryption window before detection.

**Hunt and detection concepts (no IOCs).** The highest-fidelity signal is the access-to-persistence transition: an RDP logon from an unusual ASN or geography followed within minutes by local-admin-account creation (Windows Security Event ID `4624` logon → `4720` account created → `4732` added to Administrators). Watch for `net user … /add` on command lines (Event ID `4688` process creation with command-line auditing), `servertool.exe` executing with directory-path arguments, and RemotePC installed on endpoints outside the managed-software inventory — a standalone high-signal hunt. Finally, monitor for `.prinzeugen` extension fan-out across file shares.

**Hardening / recovery.** Restrict RDP to VPN or jump-host access and enforce MFA on all remote-access sessions — this closes the documented initial-access vector. Inventory and revoke dormant RMM licences and add network detection for RemotePC traffic originating from endpoints that should never be remote-administered. The "recent files first" behaviour has a recovery corollary worth planning around: file-share snapshots taken within the last 24–48 h before an encryption event will have the highest recovery fidelity, so frequent short-interval, access-controlled backups or snapshots are disproportionately valuable against this family.
