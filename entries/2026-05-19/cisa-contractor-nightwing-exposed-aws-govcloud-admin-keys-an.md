---
schema: 1
kind: incident
title: "CISA contractor's public GitHub repository exposed AWS GovCloud admin keys and plaintext passwords for internal CISA systems for up to six months"
headline: "CISA contractor's public GitHub repo exposed AWS GovCloud admin keys and plaintext passwords for internal systems"
summary: "A Nightwing employee working for CISA kept a public GitHub repository named Private-CISA, created on 2025-11-13 and taken offline after GitGuardian, KrebsOnSecurity and Seralys raised it in mid-May 2026, that held cloud keys, tokens, plaintext passwords and files on how CISA builds software, including administrative credentials for three AWS GovCloud accounts and passwords for dozens of internal systems (Krebs on Security, 2026-05-18). The contractor had disabled GitHub's default block on publishing secrets, the AWS keys stayed valid for 48 hours after the takedown, and CISA said there was no indication that sensitive data was compromised."
discovered_at: "2026-05-19T05:00:02Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
  - cloud
regions:
  - us
sectors:
  - public-sector
entities:
  - "incident:cisa-nightwing-contractor-aws-govcloud-keys-exposed-github"
techniques: [T1593.003, T1552.001, T1078.004]
affected_products: []
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
    publisher: Krebs on Security
    date: "2026-05-18"
    role: primary
  - url: "https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330"
    publisher: Gizmodo
    date: "2026-05-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Valadon said the exposed CISA credentials represent a textbook example of poor security hygiene, noting that the commit logs in the offending GitHub account show that the CISA administrator disabled the default setting in GitHub that blocks users from publishing SSH keys or other secrets in public code repositories."
    publisher: Krebs on Security
    source_url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
  - quote: "Caturegli said he validated that the exposed credentials could authenticate to three AWS GovCloud accounts at a high privilege level."
    publisher: Krebs on Security
    source_url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
  - quote: "But Caturegli said the exposed AWS keys inexplicably continued to remain valid for another 48 hours."
    publisher: Krebs on Security
    source_url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
verification: multi-source
sourcing_note: >
  Krebs on Security reports from the two researchers who examined the repository (Valadon of GitGuardian and Caturegli of Seralys) and carries CISA's
  statement; Gizmodo reports from Krebs, so the account rests on one investigation.
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
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:38:37Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      LZ-DSO, the Landing Zone DevSecOps secure code development environment, was one of the internal
      systems whose passwords were exposed, and the Artifactory package repository credentials were a
      separate item in the archive. CISA said there was no indication that sensitive data was compromised
      and that it was adding safeguards; the staffing loss of nearly a third of its workforce is Krebs's
      context, not a CISA statement about contractor oversight. The work-to-home synchronization is
      Caturegli's suspicion, and his backdoor scenario for the Artifactory credentials is a risk
      assessment, not a finding of write access.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, techniques, title]
---

GitGuardian researcher Guillaume Valadon alerted KrebsOnSecurity on 2026-05-15 to a public GitHub repository named Private-CISA, kept by an employee of the government contractor Nightwing, that held cloud keys, tokens, plaintext passwords, logs and files describing how CISA builds, tests and deploys software ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). One file held administrative credentials to three AWS GovCloud servers, which Philippe Caturegli of Seralys validated as authenticating to three GovCloud accounts at a high privilege level; a CSV of browser-saved passwords listed plaintext credentials for dozens of internal CISA systems, among them LZ-DSO (Landing Zone DevSecOps), the agency's secure code development environment; and the archive also held plaintext credentials to CISA's internal Artifactory package repository ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). The commit logs show the administrator had disabled GitHub's default setting that blocks publishing SSH keys or other secrets, and many passwords were each platform's name followed by the current year ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)).

The repository was created on 2025-11-13 and taken offline shortly after KrebsOnSecurity and Seralys notified CISA, but the AWS keys stayed valid for another 48 hours ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)); Gizmodo puts the exposure at about six months, possibly much shorter depending on when each item was added ([Gizmodo, 2026-05-19](https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330)). Caturegli suspects the contractor used the repository to synchronize files between a work laptop and a home computer, and calls the Artifactory credentials a prime place to move laterally and backdoor software packages ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). CISA said it was investigating, that there was no indication any sensitive data was compromised, and that it was adding safeguards ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). For public bodies the case is a transferable pattern: a contractor's own repository holding an agency's privileged cloud and build-system credentials.

**Exposure:** organizations whose staff or contractors can push agency material to public code repositories and can switch off the platform's secret-blocking setting, as this administrator did ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)).

**Detection:** in code-hosting and secret-scanning telemetry, alerts on public repositories outside the organization's own namespace that contain its credentials, the kind of finding GitGuardian raised here; in cloud control-plane audit logs, use of long-lived access keys after the material they leaked from has been taken down, since these keys kept working for 48 hours ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)).

**Defender takeaway:** when a secret leaks through a public repository, revoke the keys and passwords at once rather than relying on the takedown, and check that administrators cannot disable the code platform's secret blocking for repositories that hold agency material ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)).

## Correction — 2026-10-21T20:38:37Z

LZ-DSO, which appears to stand for Landing Zone DevSecOps, the agency's secure code development environment, was one of the dozens of internal systems whose passwords sat in the exposed CSV; the plaintext credentials to CISA's internal Artifactory package repository were a separate item in the archive ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). CISA did not link the exposure to staffing: it said there was no indication that any sensitive data was compromised and that it was working to add safeguards, while the loss of nearly a third of its workforce is Krebs's own context ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). That the repository synchronized files between a work laptop and a home computer is Caturegli's suspicion, and his point about the Artifactory credentials is a risk he describes, a prime place to move laterally and backdoor software packages, rather than an established write access ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)). The exposure ran from the repository's creation on 2025-11-13 until it was taken offline in mid-May 2026, up to about six months ([Gizmodo, 2026-05-19](https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330)).
