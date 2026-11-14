---
schema: 1
kind: incident
title: "OPSSHIELD cPGuard: an attacker who registered as a customer reached the vendor's billing and licensing server and shipped a fake update on 2026-11-02 that ran as root on about 2,950 Linux servers, copying root secrets and leaving a root shell and a scheduled task"
headline: "cPGuard update channel pushed a fake root update to about 2,950 servers on 2 Nov; update, then rotate root secrets"
summary: >
  OPSSHIELD's disclosure of 2026-11-03 says an attacker registered as a customer on its billing portal and ran commands on the billing and licensing server, through crafted requests to the portal's callback pages (the vendor's logs do not record the exact request that gave access), took the keys used to publish updates
  and shipped a fake cPGuard update for about 70 minutes on 2026-11-02 (02:08 to 03:20 UTC). The update ran as root on about 2,950 customer servers, copied password hashes, root SSH keys, the MySQL root password and root shell history (cloud storage keys on a few) and left a
  hidden root shell and a scheduled task; about 7,900 billing-portal accounts were exposed as well. The clean update 5.88.26 removes the shell and a follow-up update removes the task, but credentials copied before cleanup may still be usable.
discovered_at: "2026-11-04T03:45:00Z"
updated_at: null
event_date: "2026-11-02"
run_id: 2026-11-04T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [technology]
entities: ["incident:opsshield-cpguard-update-channel-compromise-2026-11", "product:opsshield-cpguard"]
techniques: [T1195.002, T1190, T1078, T1059.004, T1003.008, T1552.001, T1552.003, T1552.004, T1053.003, T1041]
affected_products: ["OpsShield cPGuard"]
cves: []
sources:
  - url: "https://opsshield.com/notice/security-incident-disclosure-servermanage.html"
    publisher: "OPSSHIELD (security incident disclosure)"
    date: "2026-11-03"
    role: primary
  - url: "https://opsshield.com/notice/cpguard-update-channel-compromise.html"
    publisher: "OPSSHIELD (cPGuard security advisory)"
    date: "2026-11-03"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hackers-hijack-cpguard-autoupdate-to-deploy-backdoor-steal-data/"
    publisher: "BleepingComputer"
    date: "2026-11-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attacker signed up as a customer, used that account to break into our billing and licensing server, took the keys we use to publish updates, and shipped a fake cPGuard update for about 70 minutes on 2 November."
    publisher: "OPSSHIELD (security incident disclosure)"
    source_url: "https://opsshield.com/notice/security-incident-disclosure-servermanage.html"
  - quote: "If your server had cPGuard installed and online between 02:08 and 03:20 UTC on 2 November, assume its root-level secrets are known to the attacker."
    publisher: "OPSSHIELD (security incident disclosure)"
    source_url: "https://opsshield.com/notice/security-incident-disclosure-servermanage.html"
  - quote: "A successful update removes the known files, but credentials copied before cleanup may still be usable."
    publisher: "OPSSHIELD (cPGuard security advisory)"
    source_url: "https://opsshield.com/notice/cpguard-update-channel-compromise.html"
verification: single-source-victim
sourcing_note: >
  OPSSHIELD's two documents are the victim vendor's own statements and the only first-hand sources; BleepingComputer restates the earlier advisory and adds a spokesperson's statement that 2,946 servers were affected. The later disclosure supersedes the earlier advisory's preliminary scope (32 retrieved files, which the advisory calls a preliminary count and not the total number of affected servers)
  with about 2,950 servers and about 7,900 billing-portal accounts, and it names 5.88.26 where the advisory named 5.88.25. The earlier advisory attributed the access to compromised credentials for the update distribution infrastructure (CDN), which BleepingComputer repeats; the later disclosure replaces that account with a customer sign-up and an exploit of the billing and licensing server. The vendor says its logs do not record the exact request that gave the attacker access, so the entry point is traced but not fully
  reconstructed. No actor is named.
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
  - "On every Linux server that ran cPGuard on 2026-11-02, update to the latest version (the disclosure names 5.88.26 as the clean update), confirm that the hidden root shell and the scheduled task the fake update left are gone, then reset root and local passwords from a trusted environment and rotate the root SSH keys, the MySQL root password, any cloud storage keys and every secret in root's shell history; rebuild from a clean backup taken before 1 November any server the vendor tells you the attacker logged in to by hand."
updates:
  - at: "2026-11-08T14:07:37Z"
    run_id: 2026-11-08T1309Z-audit
    type: improvement
    internal: true
    summary: >
      Sourcing note now records that the vendor's earlier advisory, repeated by BleepingComputer,
      described stolen CDN credentials as the access path, which its later disclosure replaced.
    fields: [sourcing_note]
migrated_from: null
---

OPSSHIELD says the attacker registered a customer account under a false identity on the vendor's billing portal, studied how the cPGuard agent talks to the licensing system with a trial install, sent crafted requests to the portal's callback pages, gained the ability to run commands on the billing and licensing server, took the keys used to publish updates and shipped a fake update for about 70 minutes on 2026-11-02; the vendor's logs do not record the exact request that gave access ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)). cPGuard agents installed the fake update between 02:08 and 03:20 UTC, and it ran as root ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)). The script copied the local password hashes, root's SSH private keys and authorization files, the MySQL root password and root's shell history back to the attacker, and root's cloud storage keys on a small number of servers; it also left a hidden root shell and a scheduled task ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)). The vendor puts the affected servers at about 2,950 and the exposed billing-portal accounts, with name, company, postal address, e-mail and hashed password, at about 7,900 ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)). A clean update, 5.88.26, removes the hidden root shell and a follow-up update removes the scheduled task ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)), but credentials copied before cleanup may still be usable ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/cpguard-update-channel-compromise.html)). The shared exposure is every operator of a cPGuard server: BleepingComputer says hosting firms and server administrators commonly run it alongside panels such as cPanel, DirectAdmin and Plesk ([BleepingComputer, 2026-11-03](https://www.bleepingcomputer.com/news/security/hackers-hijack-cpguard-autoupdate-to-deploy-backdoor-steal-data/)).

**Exposure:** any Linux server on which cPGuard was installed and online between 02:08 and 03:20 UTC on 2026-11-02; the vendor's earlier advisory framed the exposure as an install of versions 5.88.12 through 5.88.19 shown by "Successfully updated" entries in the product's install log, which proves installation and not that the script ran ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/cpguard-update-channel-compromise.html)), and the later disclosure narrows the fake update to 02:08 to 03:20 UTC without repeating a version range or withdrawing that check ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)). Holders of a billing-portal account are exposed separately.

**Detection:** in the install log, the affected version entries of 2026-11-02; on the host, the hidden root shell and the scheduled task the update left, which the vendor says to confirm are gone after updating; in authentication logs, root logins and use of the copied SSH keys from new sources after 2026-11-02, on this server and on every server that trusted its keys; in egress logs, the update script's collection and outbound copy of root's files.

**Defender takeaway:** treat any server that ran the fake update as compromised for credential purposes even after the update: reset root and all local passwords, from a trusted environment as the earlier advisory says ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/cpguard-update-channel-compromise.html)), create new root SSH keys and remove the old public keys from every server that trusted them, change the MySQL root password and any database passwords it holds, rotate every secret in root's shell history and any cloud storage keys, and treat servers reached with those keys as exposed; rebuild from a clean backup taken before 1 November any server the vendor says the attacker logged in to by hand, and reset the billing-portal password with two-factor login ([OPSSHIELD, 2026-11-03](https://opsshield.com/notice/security-incident-disclosure-servermanage.html)).
