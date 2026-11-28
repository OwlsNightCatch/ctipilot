---
schema: 1
kind: incident
title: "Attackers compromised the .gh, .sl and .as country-code registries, rewrote authoritative DNS and obtained valid HTTPS certificates for Google and YouTube names"
headline: "Registry-level DNS hijacks of .gh, .sl and .as produced valid HTTPS certificates for Google names"
summary: >
  Google's Chrome team reported on 2026-10-06 that attackers compromised the .gh, .sl and .as country-code
  registries, changed authoritative DNS records and obtained unauthorized HTTPS certificates for Google domains and for domains
  of other organizations; Chrome blocked them and Google had the issuing authorities revoke the Google certificates. Google names no attacker or entry
  vector and says it cannot guarantee it found every affected domain; The Hacker News found 12 certificates for Google and
  YouTube names in public logs, 11 issued by Let's Encrypt and one by ZeroSSL, first logged between 2026-09-22 and 2026-09-27.
discovered_at: "2026-10-11T03:36:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-10-11T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [technology]
entities: ["incident:cctld-registry-hijacks-gh-sl-as-2026-09"]
techniques: [T1584.002, T1588.004]
affected_products: []
cves: []
sources:
  - url: "https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/"
    publisher: "Google Chrome Secure Web and Networking Team"
    date: "2026-10-06"
    role: primary
  - url: "https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html"
    publisher: "The Hacker News"
    date: "2026-10-08"
    role: corroborating
  - url: "https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941/2"
    publisher: "Let's Encrypt community forum"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "During these hijacks, attackers modified authoritative DNS records and obtained unauthorized HTTPS certificates covering several Google domains, as well as domains belonging to other organizations."
    publisher: "Google Chrome Secure Web and Networking Team"
    source_url: "https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/"
  - quote: "we cannot guarantee that our analysis identified every affected domain, nor do Chrome interventions reliably protect non-Chrome users."
    publisher: "Google Chrome Secure Web and Networking Team"
    source_url: "https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/"
  - quote: "The 12 certificates are for seven domains. Let's Encrypt issued 11 of them and ZeroSSL issued one."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html"
  - quote: "Yes, certificates for Google and Youtube were issued, and have been revoked."
    publisher: "Let's Encrypt community forum"
    source_url: "https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941/2"
verification: multi-source
sourcing_note: >
  Google, the party whose certificates were abused, discloses the hijacks; The Hacker News reviewed public Certificate
  Transparency data itself and a Let's Encrypt staff member confirmed issuance and revocation on the authority's forum. Google
  gives no hijack dates, so the event date is the first certificate The Hacker News found in the logs.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Google's Chrome Secure Web and Networking Team says attackers compromised the third-party .gh (Ghana), .sl (Sierra Leone) and .as (American Samoa) country-code top-level domains, modified authoritative DNS records and obtained unauthorized HTTPS certificates covering several Google domains and domains of other organizations ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)). A certificate authority issues a domain-validated certificate once the applicant shows control of the domain, for example by adding a record to its DNS, so control of the registry's DNS passes that check; Google has no reason to believe the issuing authorities did anything wrong ([The Hacker News, 2026-10-08](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html); [Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)). Chrome blocked the Google certificates through its CRLSets mechanism and Google had the authorities revoke them; Certificate Transparency data then surfaced further organizations, among them leading global brands, whose certificates Chrome also blocked ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)).

The Hacker News' own review of public logs found 12 certificates for seven Google and YouTube names, 11 issued by Let's Encrypt and one by ZeroSSL, first logged on 2026-09-22 (.gh), 2026-09-25 (.sl) and 2026-09-27 (.as) and revoked between 2026-09-26 and 2026-10-01 ([The Hacker News, 2026-10-08](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)), and a Let's Encrypt staff member confirmed that certificates for Google and YouTube were issued and revoked ([Let's Encrypt community forum, 2026-10-07](https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941/2)). Google's post does not name the attackers, say how the registries were compromised, or say whether any certificate was used to pose as a Google site or read users' data ([The Hacker News, 2026-10-08](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)), and it names only these three registries ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)).

**Exposure:** any organization holding a name under .gh, .sl or .as, including parked or regional variants of a brand name, and in principle any name whose registry or DNS operator an attacker can reach, because domain-validated issuance trusts whoever controls the DNS. Google tells owners of such names to review recent Certificate Transparency entries for unexpected issuance ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)).

**Detection:** Certificate Transparency monitoring of every owned name, parked and foreign registrations included, is the near-real-time signal, because every certificate Chrome trusts by default must be disclosed in public logs ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)); compare each issuing authority and account with the certificate inventory. Because the hijacks worked by changing authoritative DNS records, unexpected changes to a name's delegation or records are the second signal. After DNS control returns, restrictive CAA records bound to specific ACME accounts and validation methods stop an attacker from reusing a cached domain-control check to mint further certificates; CAA cannot prevent issuance while the hijack is live ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)).

**Triage:** a valid, correctly chained certificate is no longer evidence that a site is genuine once registry DNS can be changed. In the logs The Hacker News reviewed, every other certificate for google.com.gh, google.sl and google.as came from Google's own authority, while the 12 unauthorized ones came from Let's Encrypt and ZeroSSL, so an issuing authority or account outside your inventory, especially several certificates for one registry's names logged within hours, is the discriminator ([The Hacker News, 2026-10-08](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)).

**Defender takeaway:** put every domain you hold, including defensive and foreign registrations, under Certificate Transparency monitoring and bind issuance with CAA to your own ACME account and validation methods; Google says browser-side blocking should not be relied on to protect users and does not reliably protect clients other than Chrome ([Google, 2026-10-06](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)).
