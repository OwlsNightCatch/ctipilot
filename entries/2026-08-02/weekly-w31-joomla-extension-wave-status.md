---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Joomla third-party-extension wave status: the wave crossed from disclosed to evidenced this week — server access logs showing exploitation requests, and 92 planted administrator accounts on one live site"
headline: "The tracked Joomla extension wave reached logged, evidenced exploitation — 92 planted admin accounts"
summary: >
  Status update on the Joomla third-party-extension vulnerability wave prior weeklies tracked from a
  file-upload-to-RCE cluster through a cookie-as-identity auth bypass. The delta this week is evidentiary
  rather than technical: a vendor-commissioned follow-on audit of Balbooa Gridbox found 22 further
  vulnerabilities in the single component, and a 23rd surfaced not from the audit but alongside the live
  exploitation — the anonymous-registration privilege escalation now tracked as CVE-2026-65884. The
  researcher reports server
  access logs showing exploitation requests arriving plus 92 planted administrator accounts on one connected
  site — the wave's first member with logged in-the-wild abuse rather than disclosure-only status. The Joomla
  CNA marks both Gridbox CVEs as attacked. Cadence continued at the same rate: an unauthenticated PHP object
  injection in Aimy Captcha-Less Form Guard and a five-CVE batch in JoomShaper SP Page Builder including an
  effectively pre-authentication SQL injection that returns the whole Joomla database.
discovered_at: "2026-08-02T23:58:30Z"
event_date: "2026-07-29"
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags: [vulnerabilities, actively-exploited, pre-auth, priv-esc, rce, sqli, auth-bypass, patch-available]
regions: [global, europe]
sectors: [public-sector, technology, education]
entities:
  - trend:joomla-extension-file-upload-rce-wave
techniques: [T1190, T1136.001, T1505.003]
affected_products: ["Balbooa Gridbox for Joomla", "Aimy Captcha-Less Form Guard for Joomla", "JoomShaper SP Page Builder"]
cves: []
sources:
  - url: "https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/"
    publisher: "mySites.guru"
    date: "2026-07-29"
    role: primary
  - url: "https://mysites.guru/blog/sp-page-builder-sql-injection-mail-relay-disclosure/"
    publisher: "mySites.guru"
    date: "2026-07-27"
    role: primary
  - url: "https://www.vulncheck.com/blog/aimy-captcha-less-form-guard-object-injection"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release"
    publisher: "Balbooa"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now"
    publisher: "mySites.guru"
  - quote: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group."
    publisher: "mySites.guru"
  - quote: "Both list the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix. And both set the exploit maturity to Attacked with an urgency of Red, which is the CVE record's own way of recording that this is being used against real sites rather than sitting as a theoretical risk."
    publisher: "mySites.guru"
verification: multi-source
sourcing_note: >
  The Gridbox mechanics, exploitation evidence and affected range are cited to mySites.guru's audit, with
  Balbooa's own release notice corroborating the fixed version; the SP Page Builder and Aimy Captcha strands
  to their respective disclosers. The 92-account figure and the server-log claim are the researcher's own
  observations on sites it monitors, quoted verbatim rather than restated, and are presented as the
  researcher's finding rather than as an independently verified count. CVSS figures for the Gridbox and SP
  Page Builder identifiers are the Joomla CNA's CVSS 4.0 scores. Per-product detail lives in the referenced
  operational entries, one per disclosure, so a defender running only one of the three extensions has an entry
  scoped to it.
confidence: high
update_of: 2026-07-26/weekly-w30-joomla-extension-wave-status
references:
  - 2026-07-31/balbooa-gridbox-cve-2026-65884-anon-admin-registration-rce
  - 2026-08-01/aimy-captcha-joomla-cve-2026-65883-object-injection-rce
  - 2026-08-02/sp-page-builder-cve-2026-65766-preauth-sqli-mail-relay
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

**UPDATE (originally covered 2026-07-26):** the prior weekly recorded this wave broadening beyond file-upload RCE into a cookie-trusted-as-identity auth bypass, with no member yet confirmed exploited in the wild. That changed this week.

A follow-on source-code audit of Balbooa Gridbox, commissioned by the vendor after its earlier authentication-bypass disclosure, found 22 further vulnerabilities in that one component — and the researcher is explicit that the flaw this entry leads on was not among them: "Number 23 is not from the audit. It surfaced alongside the active exploitation" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Its mechanism is a single line of logic: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group." ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Chained with an authenticated arbitrary file upload, that becomes end-to-end unauthenticated remote code execution. The affected range is total — the researcher notes that both CNA records "list the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix. And both set the exploit maturity to Attacked with an urgency of Red, which is the CVE record's own way of recording that this is being used against real sites rather than sitting as a theoretical risk." ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)), with the complete fix in Gridbox 2.20.2 ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)). Note that 2.20.1 was itself the fix for the prior weekly's cookie-forgery flaw, so a site that patched in response to that disclosure is still exposed to these.

What moves the wave's status is the evidence class rather than the severity. Previous members were disclosed, sometimes with a public proof-of-concept, occasionally KEV-listed later. This one arrives with logs: "we have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Ninety-two planted administrator accounts on a single site is not opportunistic scanning; it is an automated campaign that has already run.

Cadence did not slow. VulnCheck disclosed an unauthenticated PHP object injection in Aimy Captcha-Less Form Guard, where the anti-spam token is deserialized with no signature and the XOR keystream needed to forge it ships in the same page ([VulnCheck, 2026-07-30](https://www.vulncheck.com/blog/aimy-captcha-less-form-guard-object-injection)). And mySites.guru reported four vulnerabilities in JoomShaper SP Page Builder — 6.7.1 closes five in total, the fifth being one the discloser states it neither reported nor tested — the sharpest of them being an `ORDER BY` injection whose only guard is a Joomla anti-CSRF token that Joomla issues to every anonymous visitor — making it effectively pre-authentication SQL injection returning the entire Joomla database, password hashes included ([mySites.guru, 2026-07-27](https://mysites.guru/blog/sp-page-builder-sql-injection-mail-relay-disclosure/)).

**Defender takeaway:** for the Swiss and European municipal, cantonal and public-sector Joomla estates this wave targets, the operative point is that these components are not discoverable from outside. An internet-wide scan does not enumerate which commercial extensions a site has installed, and one of this week's three only renders on the specific forms an administrator attached it to. The inventory has to come from the Joomla extension manager on each site, which makes a central register of installed extensions across the estate the prerequisite for responding to this wave at all — and the wave has now produced three disclosures in one week from one researcher, so the register is going to be needed again. Where a site ran an affected version while reachable, the Gridbox case gives a concrete artifact to hunt rather than a general suspicion: administrator-group members whose account creation and group assignment happened in the same transaction.
