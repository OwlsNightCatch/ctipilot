---
schema: 1
kind: incident
title: "Belnet, the Belgian government and research network, confirms a supplier zero-day let attackers copy all incoming mail to Belnet-owned domains and the transfer links its FileSender and FedSender services sent directly for 65 days"
headline: "A national research and government network had its mail copied for 65 days through a zero-day in Fortinet technology"
summary: >
  Belnet, the Belgian research and education network that also serves the Belgian government, says an attacker used a
  zero-day in technology from its supplier Fortinet to copy all incoming mail to Belnet-owned domains between 2026-07-22 and 2026-09-25, plus every download link its FileSender and FedSender transfer services generated and sent directly. Belnet links Fortinet's advisory FG-IR-26-175, the FortiMail path traversal, without naming the product; the actor is not named.
discovered_at: "2026-10-02T04:46:00Z"
updated_at: "2026-10-03T04:55:00Z"
event_date: "2026-09-24"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, zero-day]
regions: [europe]
sectors: [public-sector, education]
entities: []
techniques: [T1114]
affected_products: []
cves: []
sources:
  - url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
    publisher: "Belnet"
    date: "2026-10-02"
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-sanctions-force-cas-to-revoke-tls-certs-in-iran-russia/"
    publisher: "Risky Bulletin"
    date: "2026-09-30"
    role: corroborating
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-175"
    publisher: "Fortinet PSIRT (FG-IR-26-175)"
    date: "2026-10-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On 24 September 2026, Belnet identified a security and privacy incident within its IT infrastructure."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
  - quote: "The incident was caused by the exploitation of a zero-day vulnerability affecting technology provided by our external supplier Fortinet."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
  - quote: "During the affected period, emails were copied by the attackers and transferred to external infrastructure."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
  - quote: "At this stage, no further information is available regarding the identity or affiliation of the threat actor responsible for the incident."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
verification: single-source-victim
sourcing_note: >
  Every fact about the incident comes from Belnet's own notice (updated 2026-10-02); Risky Bulletin repeats it and adds the
  description of Belnet's customers. Belnet names Fortinet as the supplier and links Fortinet's advisory FG-IR-26-175
  without naming the product; that the advisory covers FortiMail is Fortinet's statement. Belnet names no actor.
confidence: high
references:
  - 2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-10-03T04:55:00Z"
    run_id: 2026-10-03T0404Z-intel
    type: update
    summary: >
      Belnet's notice, updated 2026-10-02, now names the supplier as Fortinet and links Fortinet's advisory
      FG-IR-26-175, says the Centre for Cybersecurity Belgium is assisting, and says transfers created in the affected
      period were disabled on 2026-09-29, so senders who still need to share the files must create new transfers.
    fields: [headline, summary, priority, sources, evidence, sourcing_note, references, body]
migrated_from: null
---

Belnet identified the incident on 2026-09-24 and says an attacker exploited a zero-day in technology from its external supplier Fortinet; the vulnerability was remediated on 2026-09-25 at 08:10 ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)). Belnet says Fortinet has published technical information about the vulnerability, including the CVE, and links Fortinet's advisory FG-IR-26-175 without naming the product ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)); that advisory covers a FortiMail path traversal that Fortinet reports exploited in the wild ([Fortinet PSIRT, 2026-10-01](https://www.fortiguard.com/psirt/FG-IR-26-175)). Between 2026-07-22 and the morning of 2026-09-25, a window of 65 days, the attackers copied to external infrastructure all incoming mail to Belnet-owned domains (for example guest-roaming and BNIX addresses) and every download link its FileSender and FedSender services generated and sent directly, which could let them fetch the transferred files; password-protected or authenticated transfers are described as unreadable unless the password was written in the upload comment, and Risky Bulletin adds that mail sent to one of its customers was also stolen ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure); [Risky Bulletin, 2026-09-30](https://news.risky.biz/risky-bulletin-sanctions-force-cas-to-revoke-tls-certs-in-iran-russia/)).

**Exposure:** organizations that sent mail to Belnet-owned addresses or shared files through Belnet's FileSender or FedSender between 2026-07-22 and 2026-09-25, and any organization whose own mail gateway runs a FortiMail build listed in FG-IR-26-175, where the same flaw would let an attacker write files and, as Belnet's loss shows, copy mail in bulk ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure); [Fortinet PSIRT, 2026-10-01](https://www.fortiguard.com/psirt/FG-IR-26-175)).

**Detection:** Belnet publishes no technique or indicator itself and does not name the product; Fortinet's advisory FG-IR-26-175 lists the compromise artifacts and log patterns for FortiMail, and the 65-day window shows the retention needed, since scoping an incident like this one takes mail-flow and transfer-link logs reaching back at least that far ([Fortinet PSIRT, 2026-10-01](https://www.fortiguard.com/psirt/FG-IR-26-175)).

**Defender takeaway:** this is a Belgian incident, relevant here as the shared-service supplier-zero-day pattern, in which one exploited flaw in a mail or transfer service run for many public-sector customers exposes all of them at once; treat download links and unprotected attachments exchanged with Belnet in the window as exposed, and check every FortiMail gateway you run against Fortinet's advisory with a look-back to at least 2026-07-22.

## Update — 2026-10-03T04:55:00Z

Belnet's incident notice, updated on 2026-10-02 at 11:00, now names the external supplier as Fortinet and links Fortinet's advisory FG-IR-26-175 ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)). Belnet also says it engaged the Centre for Cybersecurity Belgium for incident response and forensics, and that on 2026-09-29 it removed download links that were still active and disabled transfers created during the affected period, which generated notifications to senders and recipients ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)). Senders who still need to share the files must create new transfers, because Belnet cannot recreate them, and Belnet still names no actor ([Belnet, 2026-10-02](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)).
