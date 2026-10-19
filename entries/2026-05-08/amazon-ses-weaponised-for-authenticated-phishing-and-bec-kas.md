---
schema: 1
kind: research
title: "Phishing and BEC through hijacked Amazon SES accounts: leaked IAM keys let attackers send mail that passes SPF, DKIM and DMARC"
headline: "Kaspersky: attackers use leaked AWS IAM keys to send phishing and fabricated-thread BEC through legitimate Amazon SES accounts"
summary: >
  Kaspersky reports an uptick since January 2026 in phishing sent through legitimate Amazon Simple Email
  Service (SES) accounts, accessed with leaked AWS IAM keys harvested from public repositories, ENV files,
  Docker images, configuration backups and open S3 buckets. The mail passes SPF, DKIM and DMARC and comes
  from sender IPs reputation blocklists will not block; lures include fake e-signature notices leading to
  sign-in forms on amazonaws.com and a fabricated invoice thread sent to a finance department.
discovered_at: "2026-05-08T05:00:13Z"
event_date: "2026-05-04"
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - phishing
  - cloud
regions:
  - global
sectors: []
entities: []
cves: []
sources:
  - url: "https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/"
    publisher: "Kaspersky Securelist"
    date: "2026-05-04"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/researchers-report-amazon-ses-abused-in-phishing-to-evade-detection/"
    publisher: "BleepingComputer"
    date: "2026-05-04"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
techniques: [T1552.001, T1078.004, T1566.002, T1684.001]
classification:
  reliability: B
  credibility: 2
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-10-11T14:15:47Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The cited Kaspersky URL did not exist; the report is 'Phishing campaigns and BEC attacks through Amazon SES' of 2026-05-04, now cited with BleepingComputer's coverage. The claim that Kaspersky saw finance departments at European manufacturing firms targeted is in no source and is removed, the credential source is described as leaked IAM keys as the report says, and the entry gains its rating, ATT&CK mapping and labelled guidance from the report.
    fields: [title, headline, summary, event_date, regions, techniques, sources, verification, classification, body]
---

Kaspersky reports that phishing sent through Amazon Simple Email Service (SES) rose in January 2026 and stayed steady through the first quarter ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). Attackers mostly reach SES through leaked AWS IAM access keys that developers leave in public GitHub repositories, ENV files, Docker images, configuration backups or publicly accessible S3 buckets; bots built on the open-source secret scanner TruffleHog find the keys, and the attackers then check each key's permissions and sending limits ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). Because the mail is sent from legitimate infrastructure, it passes SPF, DKIM and DMARC, almost always carries `.amazonses.com` in its Message-ID header, and comes from sender IPs that reputation blocklists cannot block without blocking all SES mail ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)).

A common early-2026 lure was a fake electronic-signature notification whose link led to a sign-in form hosted on `amazonaws.com` ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). In a business-email-compromise case Kaspersky investigated, an email posing as an employee went to the company's finance department with a fabricated thread about an outstanding invoice and PDF attachments holding only payment details and supporting documentation, with no malicious link or QR code ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). BleepingComputer reported the research the same day ([BleepingComputer, 2026-05-04](https://www.bleepingcomputer.com/news/security/researchers-report-amazon-ses-abused-in-phishing-to-evade-detection/)).

**Exposure:** any AWS account whose IAM access keys have leaked into a public repository, container image, backup or bucket can be turned into a phishing sender; an organization is exposed both as the owner of such keys and as a recipient of SES-sent mail ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)).

**Detection:** in mail-gateway telemetry, SES-sent messages almost always carry `.amazonses.com` in the Message-ID header; a message from an unfamiliar SES sender whose link resolves to a sign-in form on `amazonaws.com`, or an invoice thread to finance with PDFs holding only payment details and supporting documentation, is the pattern Kaspersky describes ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). On the AWS side, in analyst judgement, SES sending activity by an IAM key that has no history of sending mail is the signal for a hijacked key.

**Defender takeaway:** authentication results do not separate this mail from legitimate SES mail, so payment-change and invoice requests need out-of-band verification regardless of a passing DMARC result. For your own AWS accounts, Kaspersky advises least-privilege IAM keys, roles instead of long-lived keys, MFA, IP restrictions and automated key rotation with regular audits ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)).

## Correction — 2026-10-11T14:15:47Z

Kaspersky's report names no sector, country or manufacturing victim; its business-email-compromise case is a single fabricated invoice thread sent to a company's finance department ([Kaspersky Securelist, 2026-05-04](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)). The earlier text said Kaspersky observed finance departments at European manufacturing firms being targeted, which no source supports, and cited a Securelist address that does not exist. In most cases attackers use leaked IAM access keys.
