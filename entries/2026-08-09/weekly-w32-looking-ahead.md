---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: "2026-W32 looking ahead — items already in motion: a NIS2 law in force in six days, a PAM appliance whose full exploitation detail is due in September, five products that will never be patched, and a federal ISMS deadline five months out"
headline: "W32 outlook — the 15 August Dutch NIS2 clock, WALLIX details due in September, and five products with no fix coming"
summary: >
  A watch list of items already in motion at the close of ISO week 2026-W32, each with a source and a date —
  not predictions. The Dutch Cyberbeveiligingswet enters into force on 15 August 2026. The researchers who
  reported the WALLIX Bastion CVSS 10.0 authentication bypass intend to publish full technical details in
  September 2026, which dates the window for patching quietly. The EU AI Act's high-risk obligations have
  moved to 2 December 2027 and 2 August 2028, and two new prohibited practices apply from 2 December 2026.
  The Cyber Resilience Act's reporting obligations begin on 11 September 2026, two days before ENISA's
  managed-security-services certification consultation closes. Swiss federal administrative units have until
  1 January 2027 to have built their own ISMS. And five products carry flaws that no vendor will fix.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-09"
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, supply-chain]
regions: [europe, switzerland, global]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities:
  - policy:netherlands-nis2-cyberbeveiligingswet-2026
  - policy:eu-ai-act-digital-omnibus-2026
  - policy:switzerland-isv-federal-isms-deadline-2026
  - policy:eu-cyber-resilience-act
  - actor:clop
  - campaign:clop-windchill-flexplm-extortion-2026
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht"
    publisher: "Rijksoverheid (Ministerie van Justitie en Veiligheid)"
    date: "2026-07-07"
    role: primary
  - url: "https://www.wallix.com/support-services/alerts/"
    publisher: "WALLIX"
    date: "2026-07-20"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-08-06"
    role: corroborating
  - url: "https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng/xhtml"
    publisher: "EUR-Lex / Official Journal of the European Union"
    date: "2026-07-24"
    role: primary
  - url: "https://www.fedlex.admin.ch/eli/cc/2023/735/de"
    publisher: "Fedlex — Informationssicherheitsverordnung (ISV), SR 128.1"
    date: "2023-11-08"
    role: primary
  - url: "https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/"
    publisher: "InfoGuard Labs"
    date: "2026-08-07"
    role: corroborating
  - url: "https://www.ncsc.gov.uk/blogs/making-forensic-observability-the-norm-for-network-devices"
    publisher: "NCSC UK"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  Every item names a source that states the date or the pending status; nothing here is a forecast. The
  Swiss ISV deadline is derived from the ordinance's own text — Article 51(4) requires the administrative
  units under Article 2(1)(c) to build their ISMS within three years of entry into force, and Article 52
  sets that entry into force at 1 January 2024 — and its addressee is the federal administration itself,
  not critical-infrastructure operators generally, which is narrower than some practitioner commentary
  implies.
confidence: high
update_of: null
references:
  - 2026-08-09/wallix-bastion-rest-api-unauth-admin-cvss10
  - 2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach
  - 2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming
  - 2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor
  - 2026-08-08/cpdlc-atn-b1-five-protocol-flaws-no-mitigation-available
  - 2026-08-05/check-point-cve-2026-18574-management-auth-bypass
  - 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Items already in motion at the close of ISO week 2026-W32, each with a source and a date. None of these is a prediction.

**Dated obligations.**

- **15 August 2026 — the Netherlands' Cyberbeveiligingswet enters into force**, together with the companion critical-entities resilience law, imposing registration, duty-of-care, incident-notification and board-accountability duties on more than 8,000 organisations across 18 sectors, with registration in NCSC-NL's national entity register mandatory from that date ([Rijksoverheid, 2026-07-07](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht)). Relevant to anyone with Dutch entities, suppliers or public-sector counterparts, whose notification behaviour changes on that date.
- **11 September 2026 — the Cyber Resilience Act's reporting obligations begin**, ahead of the regulation's principal obligations in December 2027. **13 September 2026 —** ENISA's consultation on the draft EU Managed Security Services certification scheme closes, two days later; providers delivering services under the EU Cybersecurity Reserve would need that certification within two years of the scheme's entry into force, which makes it a procurement gate rather than a voluntary mark. Both were established in prior weekly coverage and neither date has moved.
- **2 December 2026 — two new prohibited AI practices apply** under the AI Act as amended, and **2 December 2027 / 2 August 2028** are the new application dates for high-risk obligations under Annex III and Annex I respectively, following Regulation (EU) 2026/1744 ([EUR-Lex, 2026-07-24](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng/xhtml)). Any readiness plan written against 2 August 2026 for Annex III systems is now diarised to the wrong date.
- **1 January 2027 — Swiss federal administrative units must have built their ISMS.** The Informationssicherheitsverordnung requires the administrative units under its Article 2(1)(c) to build their information-security management system within three years of the ordinance's entry into force, and the ordinance entered into force on 1 January 2024 ([Fedlex, ISV SR 128.1](https://www.fedlex.admin.ch/eli/cc/2023/735/de)). Roughly five months remain. The addressee is the federal administration itself; commentary that presents this as a general critical-infrastructure obligation is reading it more broadly than the text supports.

**Disclosure and exploitation clocks.**

- **September 2026 — full technical details of the WALLIX Bastion authentication bypass are due.** WALLIX states that the reporting researchers intend to publish the complete write-up of the CVSS 4.0 base 10.0 flaw that gives an unauthenticated caller full product-administrator control of the appliance — its credential vault and session recordings included — in September ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). Bastion 12.3.7 and 12.4.1 and later are patched, per the CERT-FR advisory that relayed the bulletin ([CERT-FR, 2026-08-06](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/)). This is a dated window for remediating quietly, not a current threat.
- **Cl0p's Windchill and FlexPLM listings have still not begun.** Research re-checked this week found no leak-site listing for that campaign, leaving affected organisations in the interval between exfiltration and publication — the status a prior weekly recorded, unchanged.

**Flaws with no fix coming.** Five items from this week's coverage will not be resolved by waiting for a vendor, and each therefore converts into an architecture or lifecycle decision:

- **Tobit TeamDavid** — 22 CVEs bounded at "Rollout 524" with no fixed release named, against roughly 12,000 internet-facing instances, and researchers reporting that both they and the coordinating national cyber security centre were left without a vendor response ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)).
- **Flowise** — three CVEs assigned days after the vendor announced it is winding down; self-hosted operators own the compensating controls.
- **Zbtlink routers (ENDLESSDOORS)** — a factory-shipped root backdoor on twenty models, where the discloser's remediation is device replacement.
- **CPDLC over ATN-B1** — five flaws that are properties of the standard, with CISA recording the remediation category as none-available.
- **Check Point's end-of-support management trains** — R80 through R81.10 are listed as affected by this week's unauthenticated management-authentication bypass with no fix on offer.

**In development, no date.** NCSC UK confirms it is working with international partners on a reference architecture for forensic observability in network appliances, intended to give vendors something concrete to build to ([NCSC UK, 2026-07-29](https://www.ncsc.gov.uk/blogs/making-forensic-observability-the-norm-for-network-devices)). It is not published, and no publication date is stated. Separately, the Metabase SQL-injection zero-day exploited this week still has no CVE identifier assigned, so it will not reach any process that waits for one.
