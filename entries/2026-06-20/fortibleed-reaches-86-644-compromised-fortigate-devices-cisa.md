---
schema: 1
kind: incident
horizon: operational
title: "FortiBleed reaches 86,644 compromised FortiGate devices; CISA issues emergency hardening guidance"
headline: "FortiBleed reaches 86,644 compromised FortiGate devices; CISA issues emergency hardening guidance"
summary: "FortiBleed escalates to 86,644 compromised FortiGate devices; CISA issues emergency hardening guidance. Up from 73,932 (covered 2026-06-18); attackers are cracking SSL VPN password hashes and pivoting into Active Directory (§ 4)."
discovered_at: "2026-06-20T05:12:18Z"
event_date: 2026-06-19
run_id: 2026-06-20-4cfd00ef
priority: high
immediate_action: null
tags:
  - actively-exploited
  - data-breach
  - identity
  - russia-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
  - telco
entities:
  - "incident:fortibleed-fortigate-credential-exposure"
cves: []
sources:
  - url: "https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure"
    publisher: CISA alert
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-20.md
---

**UPDATE (originally covered 2026-06-18):** The FortiBleed SSL VPN credential-harvesting campaign has grown from the 73,932 internet-facing FortiGate devices reported on 2026-06-18 to 86,644 confirmed compromised credentials across 194 countries, and CISA has published an emergency hardening advisory ([SecurityWeek, 2026-06-19](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/); [CISA, 2026-06-18](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure)).

The new detail is methodology and impact: a Russian-speaking actor cracked SSL VPN password hashes with a 45-GPU Hashtopolis cluster, after which the actors pivot into internal Active Directory using harvested service and admin accounts ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/)). CISA's guidance mandates immediate SSL VPN session termination, full credential resets, enforcement of PBKDF2 (replacing the older MD5-crypt admin-hash scheme), and phishing-resistant MFA on all remote access. Defenders should cross-reference SSL VPN session logs against the Shadowserver notification feed and hunt for sequential VPN authentication failures from rotating residential IP ranges followed by a success and immediate internal RDP/SMB/LDAP reconnaissance.
