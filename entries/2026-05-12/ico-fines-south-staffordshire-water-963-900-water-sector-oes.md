---
schema: 1
kind: incident
title: "ICO fines South Staffordshire Water £963,900 under UK GDPR for the 2020 to 2022 intrusion: phishing foothold, ZeroLogon on two unpatched domain controllers, 5% of IT monitored"
headline: "ICO fines South Staffordshire £963,900: a 20-month phishing foothold, ZeroLogon on two DCs and only 5% of IT monitored"
summary: "The UK ICO fined South Staffordshire Plc and South Staffordshire Water Plc £963,900 under UK GDPR on 2026-05-11 for an attack in which a phishing attachment opened in September 2020 gave an attacker a foothold that went undetected for 20 months, followed by domain-admin compromise from May 2022 with ZeroLogon (CVE-2020-1472) exploited on two unpatched domain controllers; the personal data of 633,887 people was published on the dark web. The ICO found that only 5% of the IT environment was monitored, Windows Server 2003 was still in use and no regular vulnerability scans were run."
discovered_at: "2026-05-12T05:00:00Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - law-enforcement
regions:
  - uk
  - europe
sectors:
  - water
  - public-sector
entities:
  - "incident:south-staffordshire-water-ico-2026"
  - "actor:clop"
techniques: [T1566.001, T1204.002, T1068, T1078.002]
affected_products: ["Microsoft Windows Server"]
cves:
  - id: CVE-2020-1472
    cvss: "5.5 (CVSS 3.1, MSRC's current record; its vector AV:L/PR:L disagrees with MSRC's own description of an unauthenticated network attack)"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "Windows domain controllers without the August 2020 Netlogon security updates"
    fixed: "August 2020 security updates, the first of Microsoft's two-phase rollout"
sources:
  - url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/"
    publisher: "UK ICO (press release)"
    date: "2026-05-11"
    role: primary
  - url: "https://therecord.media/uk-water-company-had-hackers-lurking-for-years"
    publisher: "The Record"
    date: "2026-05-11"
    role: corroborating
  - url: "https://www.theregister.com/cyber-crime/2026/05/11/ico-fines-south-staffordshire-963k-over-2022-breach/5237875"
    publisher: "The Register"
    date: "2026-05-11"
    role: corroborating
  - url: "https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf"
    publisher: "UK ICO (monetary penalty notice)"
    date: "2026-05-07"
    role: primary
  - url: "https://ico.org.uk/action-weve-taken/enforcement/2026/05/south-staffordshire-plc-and-south-staffordshire-water-plc/"
    publisher: "UK ICO (enforcement action)"
    date: "2026-05-07"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472"
    publisher: "Microsoft Security Response Center (CVE-2020-1472)"
    date: "2020-08-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In this case, the recipient opened an attachment which enabled the attacker to install malicious software which remained undetected within the organisation's systems for 20 months."
    publisher: "UK ICO (press release)"
    source_url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/"
  - quote: "Inadequate monitoring and logging — only 5% of the IT environment was being monitored, meaning malicious activity was not detected."
    publisher: "UK ICO (press release)"
    source_url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/"
  - quote: "Endpoint telemetry and logging were not integrated into South Staffordshire’s security incident and event monitoring platform."
    publisher: "UK ICO (monetary penalty notice)"
    source_url: "https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf"
  - quote: "Two domain controllers also remained unpatched against a critical vulnerability known as ZeroLogon which allows rapid escalation of privileges and was first published in August 2020. The attacker successfully exploited this vulnerability during the incident."
    publisher: "The Record"
    source_url: "https://therecord.media/uk-water-company-had-hackers-lurking-for-years"
  - quote: "The penalty notice makes no reference to any compromise of operational or water treatment systems."
    publisher: "The Record"
    source_url: "https://therecord.media/uk-water-company-had-hackers-lurking-for-years"
verification: multi-source
sourcing_note: >
  The findings are the ICO's own, from its press release, enforcement notice and penalty notice; The Record and The Register restate
  them and add the Cl0p attribution, which the ICO does not make.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
updates:
  - at: "2026-10-21T20:43:46Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The ICO's own penalty notice names ZeroLogon (CVE-2020-1472), unpatched on two domain controllers
      and exploited during the incident though not the way in; only the Cl0p attribution comes from the
      press. The phishing foothold of September 2020 stayed dormant for 20 months before lateral movement
      and domain-admin compromise from May 2022, detection came on 15 July 2022, only 5% of the IT
      environment was monitored, and the fine is a UK GDPR penalty.
    fields: [affected_products, body, classification, cves, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title]
---

The UK Information Commissioner's Office fined South Staffordshire Plc and South Staffordshire Water Plc £963,900 for infringing Articles 5(1)(f) and 32(1) of the UK GDPR ([ICO enforcement action](https://ico.org.uk/action-weve-taken/enforcement/2026/05/south-staffordshire-plc-and-south-staffordshire-water-plc/)), after a 40% reduction for the company's early admission, which it accepted without appeal ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)). The attack began in September 2020 with a phishing email whose attachment, once opened, let the attacker install malicious software that stayed undetected for 20 months; in May 2022 the attacker moved through the network and compromised domain administrator privileges, and the breach was found only when IT performance problems started an internal investigation on 15 July 2022, followed by a ransom note on 26 July ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)). Two domain controllers were unpatched against ZeroLogon (CVE-2020-1472) in May 2022, and while the incident did not start through it, the attacker exploited it during the incident ([ICO penalty notice](https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf)). The company held data on about 1.85 million customers, around 750,000 current and 1.1 million former, and on its staff; the personal data of 633,887 people was published on the dark web, part of over 4.1 TB of data, including online-service usernames and passwords, bank account numbers and sort codes, employees' National Insurance numbers and information from which disabilities of Priority Services Register customers could be inferred ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)). The ICO does not name the attacker; The Record and The Register attribute the attack to Cl0p, which claimed it, and the penalty notice makes no reference to any compromise of operational or water-treatment systems ([The Record, 2026-05-11](https://therecord.media/uk-water-company-had-hackers-lurking-for-years); [The Register, 2026-05-11](https://www.theregister.com/cyber-crime/2026/05/11/ico-fines-south-staffordshire-963k-over-2022-breach/5237875)).

**Exposure:** the failures the ICO found: limited controls that let the attacker escalate to administrator after the first foothold, monitoring of only 5% of the IT environment, Windows Server 2003 still in use, unpatched critical systems and no regular internal or external security scans ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)). ZeroLogon lets an unauthenticated attacker who connects to a domain controller over the Netlogon Remote Protocol obtain domain administrator access ([Microsoft, CVE-2020-1472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472)).

**Detection:** coverage of endpoint telemetry in the SIEM is the gap the notice names: in December 2021 a third-party security operations centre monitored only 5% of the IT environment, and endpoint telemetry and logging were not integrated into the security monitoring platform ([ICO penalty notice](https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf)).

**Defender takeaway:** for UK data controllers, the ICO treats missing monitoring coverage, unsupported software and unpatched domain controllers as a breach of the UK GDPR security duty, and asks whether logging and monitoring cover the IT environment and alerts are acted on ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)); domain controllers still without Microsoft's Netlogon updates of August 2020 remain exposed to the same escalation ([Microsoft, CVE-2020-1472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472)).

## Correction — 2026-10-21T20:43:46Z

The ICO itself names the vulnerability: two domain controllers were unpatched against ZeroLogon (CVE-2020-1472) in May 2022, and the attacker exploited it during the incident, although the incident did not start through it ([ICO penalty notice](https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf)); it is the Cl0p attribution that comes from The Record and The Register ([The Record, 2026-05-11](https://therecord.media/uk-water-company-had-hackers-lurking-for-years)). The sequence was a phishing attachment opened in September 2020, malicious software undetected for 20 months, then movement through the network and domain-admin compromise from May 2022, with the breach found on 15 July 2022 ([ICO, 2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/)). The monitoring gap was concrete: a third-party security operations centre covered 5% of the IT environment and endpoint telemetry was not in the SIEM ([ICO penalty notice](https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf)). The fine is a UK GDPR penalty under Articles 5(1)(f) and 32(1) ([ICO enforcement action](https://ico.org.uk/action-weve-taken/enforcement/2026/05/south-staffordshire-plc-and-south-staffordshire-water-plc/)); the Cyber Security and Resilience Bill was still expected to be introduced to Parliament ([The Record, 2026-05-11](https://therecord.media/uk-water-company-had-hackers-lurking-for-years)).
