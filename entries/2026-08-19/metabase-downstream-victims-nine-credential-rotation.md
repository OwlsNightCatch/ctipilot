---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — the Metabase SQL injection has produced nine publicly confirmed downstream breaches, and the reason the list keeps growing is that patching the BI tool does not invalidate the database credentials it already handed over"
headline: "A business-intelligence layer holds the keys to every warehouse behind it, and the patch does not take them back"
summary: >
  A tracker maintained by VenariX, updated 2026-08-17, now counts nine publicly confirmed organisations
  whose compromised Metabase environments were used to reach connected data warehouses — n8n, Framework,
  Tally and Kilo Code, joined on 2026-08-17 by Stocksy United Co-op, ShipMonk, Checkly, Cypress.io and Bits
  of Gold. This pipeline covered CVE-2026-72898 on 2026-08-09 and 2026-08-12 as an exploited CVSS 10.0
  unauthenticated SQL injection in the password-reset endpoint; the delta is the downstream pattern. Because
  Metabase stores the credentials for every database it connects to, administrative access to the
  application yields those credentials, and Metabase's own guidance is that patching does not invalidate
  credentials already exposed. Metabase also published a two-request log pattern that indicates a given
  instance was compromised.
discovered_at: "2026-08-19T05:02:00Z"
event_date: "2026-08-17"
run_id: 2026-08-19T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, sqli, pre-auth, actively-exploited, cisa-kev, data-breach, supply-chain, patch-available]
regions: [global, europe]
sectors: [technology, retail, finance]
entities: [incident:metabase-sqli-zeroday-2026-08]
techniques: [T1190, T1552.001, T1213, T1078]
affected_products: ["Metabase", "Metabase Cloud"]
cves:
  - id: CVE-2026-72898
    cvss: "10.0"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Metabase Cloud and self-hosted releases in the 58 through 63 branches"
    fixed: "latest patched release for each affected self-hosted branch; Metabase Cloud patched by the vendor"
sources:
  - url: "https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments"
    publisher: "VenariX"
    date: "2026-08-17"
    role: primary
  - url: "https://databreaches.net/2026/08/17/israels-largest-crypto-broker-bits-of-gold-hit-by-data-breach-affecting-200000-customers/"
    publisher: "DataBreaches.net"
    date: "2026-08-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This brings the number of publicly confirmed downstream organizations tracked by VenariX to nine."
    publisher: "VenariX"
  - quote: "Credential rotation is especially important if exploitation is suspected, because patching the application does not invalidate credentials that may already have been exposed."
    publisher: "VenariX"
  - quote: "Metabase states that this pattern in application or ingress logs indicates that the instance was likely compromised."
    publisher: "VenariX"
verification: multi-source
sourcing_note: >
  VenariX is an incident-tracking service rather than an original research lab or a primary disclosing
  party, which is why its reliability is rated C: it aggregates victim disclosures and vendor guidance
  rather than producing first-hand telemetry. Its tracker is nonetheless the only party publishing the
  consolidated downstream list, and it is cited as the source of the count and of the association between
  each named organisation and the Metabase compromise — that association is VenariX's assessment, not a
  statement by the named organisations. The detection pattern and the remediation guidance in this entry
  are Metabase's own, relayed by VenariX and attributed to Metabase accordingly rather than to the tracker.
  That relay is the reason credibility is 2 rather than 1: the operational guidance and the detection pattern
  are second-hand here. Metabase's own advisory and the GitHub advisory record VenariX names were both
  attempted this run to cite the vendor at first hand — the advisory database returned no record for that
  identifier and the advisory host is unreachable from this environment — so the guidance is carried as
  relayed rather than dropped, and the reader is told which party originated it.
  DataBreaches.net independently carries the Bits of Gold disclosure, in which the company describes access
  through a third-party data analytics network without naming Metabase; the identification of that platform
  as Metabase is VenariX's. One transport caveat on that citation, stated rather than smoothed over: the
  Bits of Gold item was read from DataBreaches.net's own syndication feed, whose entry for 2026-08-17T13:19Z
  carries the substance quoted here and links to the article URL cited below. The article page itself refused
  a direct fetch (HTTP 403) both to the research pass and to the pre-commit link check, and the reader proxy
  that would normally hydrate it is credit-exhausted, so the page was never rendered in this run — the
  publisher's feed is what was actually read. The per-victim data-exposure details are each drawn from the
  victim's own disclosure as VenariX reproduces it.
confidence: high
update_of: 2026-08-12/cve-2026-72898-metabase-sqli-cve-assigned-kev
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "For any Metabase instance that was reachable and unpatched during the exploitation window, rotate the credentials for every database and warehouse it was configured to connect to — not just the Metabase admin credentials — and revoke active sessions and API keys, because the upgrade does not invalidate what was already retrieved."
  - "Search Metabase application or ingress logs for a POST to /api/session/reset_password returning HTTP 400 immediately followed by a GET to /api/user/current returning HTTP 200; Metabase states that sequence indicates the instance was likely compromised."
migrated_from: null
---

**UPDATE (originally covered 2026-08-12):** the count of downstream victims is now the story. A tracker maintained by VenariX, first published 2026-08-10 and updated 2026-08-17, states that "This brings the number of publicly confirmed downstream organizations tracked by VenariX to nine" ([VenariX, 2026-08-17](https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments)) — n8n, Framework, Tally and Kilo Code from the first wave, with Stocksy United Co-op, ShipMonk, Checkly, Cypress.io and Bits of Gold added on 2026-08-17. The earlier entries covered the flaw itself: an unauthenticated SQL injection reachable at the password-reset endpoint, CVSS 10.0, exploited, catalogued as such on 2026-08-11.

The mechanism behind the growing list is a property of business-intelligence tooling rather than of this bug. Metabase stores the connection configuration, including credentials, for every external database and warehouse it queries; an attacker who reaches administrative context in the application can therefore read those stored credentials and query or export whatever they reach ([VenariX, 2026-08-17](https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments)). The blast radius of any given instance is set entirely by what it was wired to — VenariX's own framing is that a deployment connected only to a restricted reporting database is a materially different incident from one connected to a production warehouse, which is the assessment question a defender should be answering first.

The victim disclosures show the range. n8n's investigation found the attacker queried 136 records containing names and email addresses, five of which also carried bcrypt password hashes tied to n8n Cloud accounts, and reported that the queries returned a variable set of rows, which prevented it from determining exactly which individual records were returned. Framework confirmed customer data was stolen including names, email addresses, phone numbers, login IP addresses and billing and shipping addresses, with payment information not included. Tally's exposure covered email addresses and password hashes while form content was stored separately and unaffected, and Kilo Code's included names, email addresses, billing addresses, location data and, for a subset of users, partial or full prompts ([VenariX, 2026-08-17](https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments)). Of the newly added names, Bits of Gold separately disclosed on 2026-08-17 that an attacker gained unauthorized access to a third-party data analytics network and obtained names, national ID numbers and emails for roughly 200,000 customers ([DataBreaches.net, 2026-08-17](https://databreaches.net/2026/08/17/israels-largest-crypto-broker-bits-of-gold-hit-by-data-breach-affecting-200000-customers/)) — the company describes the platform class, not the product, and it is VenariX that places the incident in this campaign.

The operational point is the one most likely to be got wrong in a remediation ticket. Metabase's own guidance, as VenariX relays it, is that "Credential rotation is especially important if exploitation is suspected, because patching the application does not invalidate credentials that may already have been exposed" ([VenariX, 2026-08-17](https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments)). An estate that upgraded Metabase and closed the ticket has fixed the injection and left the attacker holding working warehouse credentials. Metabase's fuller recommendation set for potentially exposed instances is to revoke active sessions, review administrator accounts and API keys, rotate credentials for connected databases, and review both Metabase and warehouse logs; where an immediate upgrade is impossible it recommends temporarily blocking access to the reset-password endpoint.

Detection has an unusually crisp anchor for a SQL-injection flaw, because the vendor published one. Metabase identified a recurring two-request pattern associated with exploitation — a POST to `/api/session/reset_password` returning HTTP 400, immediately followed by a GET to `/api/user/current` returning HTTP 200 — and "Metabase states that this pattern in application or ingress logs indicates that the instance was likely compromised" ([VenariX, 2026-08-17](https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments)). Beyond that, the investigative surface is Metabase's own query history, database and warehouse audit logs, administrator accounts, API keys, and any unexpected use of the stored connection credentials — the last being where a compromise that started in the BI tier becomes visible in the warehouse tier.

**Triage:** a failed password reset followed by a session check is not by itself unusual in a web application's logs, which is exactly why the ordered pair matters rather than either request alone — a genuine failed reset does not produce an authenticated `/api/user/current` success on the same session immediately afterwards. Downstream, the discriminator for warehouse activity is whether queries arriving under the Metabase service credential match the dashboards and questions that credential is actually used for: bulk selects against tables no saved question references, or access at hours the reporting schedule does not run, are the signal, while high query volume under that identity is normal by design.
