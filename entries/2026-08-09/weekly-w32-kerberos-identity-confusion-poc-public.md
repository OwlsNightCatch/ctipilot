---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Two Active Directory identity-confusion flaws patched in spring got their full mechanics and a working proof-of-concept published this week — one takes a low-privileged user to Domain Admin by putting the target's name in their own UPN"
headline: "KerberLoss and ResetNightmare go fully public — spring's Important-rated AD fixes are now a runnable exploit"
summary: >
  At Black Hat USA 2026, Semperis published the full technical detail and a proof-of-concept for two logical
  Active Directory privilege-escalation flaws. KerberLoss (CVE-2026-25177) uses unfilterable Unicode
  characters to defeat Service Principal Name uniqueness checks, causing Kerberos tickets to be encrypted
  under the wrong key and forcing a fallback to NTLM. ResetNightmare (CVE-2026-27912) abuses the Kerberos
  password-change protocol: a low-privileged user sets their own user principal name to a target
  administrator's account name, requests a ticket with the enterprise name type, and resets their password
  while carrying the target's identity — because the password-change flow needs only a ticket-granting
  ticket and never passes through the request where the requester's identity is validated. Microsoft patched
  them in March and April 2026; the exploitation mechanics are public now.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-05"
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags: [identity, vulnerabilities, priv-esc, poc-public, patch-available]
regions: [global, europe]
sectors: [public-sector, technology, finance]
entities: []
techniques: [T1558, T1078.002, T1098]
affected_products: ["Microsoft Active Directory Domain Services", "Microsoft Windows Server"]
cves:
  - id: CVE-2026-25177
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "Active Directory Domain Services — improper restriction of names for files and other resources, allowing an authorized attacker to elevate privileges over a network"
    fixed: "Microsoft patched it in March 2026; the CVE record was published 2026-03-10"
  - id: CVE-2026-27912
    cvss: "8.0"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "Windows Kerberos — improper authorization allowing an authorized attacker to elevate privileges over an adjacent network"
    fixed: "Microsoft patched it in April 2026; the CVE record was published 2026-04-14"
sources:
  - url: "https://www.semperis.com/blog/identity-crisis-novel-vulnerabilities-leading-to-kerberos-downgrade-dos-and-full-domain-takeover/"
    publisher: "Semperis"
    date: "2026-08-05"
    role: primary
  - url: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-25177"
    publisher: "NIST National Vulnerability Database"
    date: "2026-03-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Each vulnerability takes a unique approach to causing identity confusion on DCs, resulting in various impacts. The second (and more severe vulnerability) enables a low-privileged user to instantly gain Domain Admin privileges."
    publisher: "Semperis"
  - quote: "Microsoft patched KerberLoss (CVE-2026-25177) in March 2026 and ResetNightmare (CVE-2026-27912) in April 2026."
    publisher: "Semperis"
verification: single-source
sourcing_note: >
  Semperis is both the discovering lab and the Black Hat presenter, so the technical account is
  single-source. Both identifiers were independently verified against the National Vulnerability Database in
  this run: CVE-2026-25177 (CVSS 3.1 base 8.8, "improper restriction of names for files and other resources
  in Active Directory Domain Services", published 2026-03-10) and CVE-2026-27912 (CVSS 3.1 base 8.0,
  "improper authorization in Windows Kerberos", published 2026-04-14) — both dates matching the vendor patch
  months Semperis states. No in-the-wild exploitation is reported by any party.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Both of the week's Active Directory findings were fixed months ago, which is exactly why they belong in a strategic read rather than an operational one: what changed in 2026-W32 is not the exposure but the cost of exploiting it. At Black Hat USA 2026 Semperis published the full mechanics and a runnable proof-of-concept for two logical flaws it describes as taking "a unique approach to causing identity confusion on DCs, resulting in various impacts," adding that "the second (and more severe vulnerability) enables a low-privileged user to instantly gain Domain Admin privileges" ([Semperis, 2026-08-05](https://www.semperis.com/blog/identity-crisis-novel-vulnerabilities-leading-to-kerberos-downgrade-dos-and-full-domain-takeover/)).

KerberLoss turns on name uniqueness. Active Directory enforces that a Service Principal Name is unique, but the check runs over a directory layer that cannot filter certain Unicode characters — so an attacker holding only the ability to write an SPN on any computer or user object can plant a duplicate the uniqueness check does not catch. The consequence is that Kerberos tickets get encrypted under the wrong account's key, producing authentication failures for the legitimate service, and — the part that matters operationally — pushing clients into an NTLM fallback, or enabling SPN hijacking as a stepping stone toward delegation abuse. The National Vulnerability Database records the flaw as "improper restriction of names for files and other resources in Active Directory Domain Services allows an authorized attacker to elevate privileges over a network," at CVSS 3.1 base 8.8 ([NVD, 2026-03-10](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-25177)).

ResetNightmare is the more serious of the two and turns on where identity is checked. A low-privileged user sets their own user principal name to a target administrator's account name, then requests a ticket-granting ticket using the enterprise name type, so the ticket carries the target's name. They then drive the Kerberos password-change flow — which requires only a ticket-granting ticket — to reset a password while holding that borrowed identity, and authenticate as the administrator afterwards. Semperis locates the root cause precisely: the validation that would have caught the mismatch lives in a later request the password-change flow never makes, noting that "the TGS-REQ is where the PAC_REQUESTOR_SID validation occurs." NVD records it as "improper authorization in Windows Kerberos allows an authorized attacker to elevate privileges over an adjacent network," CVSS 3.1 base 8.0.

**Defender takeaway:** the action is confirmation rather than remediation — Semperis states that "Microsoft patched KerberLoss (CVE-2026-25177) in March 2026 and ResetNightmare (CVE-2026-27912) in April 2026," and both NVD publication dates match those patch cycles. For an estate that tracks domain-controller patching by exception rather than by assertion, this is the week to convert that into an explicit check across every DC, because the exploitation detail and a proof-of-concept are now public against a bug class whose prerequisite is only a low-privileged domain account. Beyond patching, the standing hardening lever both flaws share is write access to identity attributes: `WriteSPN` on computer or user objects, and the ability to modify a user principal name, are non-default permissions that accumulate through delegation and rarely get reviewed.

**Triage:** neither technique produces a failed authentication, so the signal is in directory-object modification rather than in logon telemetry. For ResetNightmare, the discriminator is a user principal name being set to a value that matches another account's logon name — a collision that has no legitimate cause — followed shortly by a password-reset event for the modifying account; either alone is unremarkable, the pair is not. For KerberLoss, audit for Service Principal Name values containing non-printing or unexpected Unicode characters, and for duplicate SPNs that the directory nonetheless accepted. The benign lookalikes are account renames and service-account migrations, both of which are change-managed and none of which produce an SPN with characters no administrator would type.
