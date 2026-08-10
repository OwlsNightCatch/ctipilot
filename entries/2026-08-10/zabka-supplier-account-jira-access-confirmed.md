---
schema: 1
kind: incident
horizon: operational
title: "Żabka confirms an external service-provider account reached its ticketing system — the claimed pivot from Jira into source control and production is the seller's assertion, not the company's"
headline: "A supplier account reached Jira at a Polish convenience-store chain; the interesting part of the story is the part nobody has confirmed"
summary: >
  Żabka, a Polish convenience-store franchise chain, confirmed in a written statement to
  Polish outlets that it detected unauthorized access to technical resources supporting
  franchisor-franchisee information exchange, that the access came through an external service
  provider's account, that it was blocked immediately, and that to its current knowledge the
  perpetrator reached the ticketing system. It states transaction data, consumer services and loyalty
  app data are unaffected, and has notified its data-protection officer, the Polish regulator and
  law enforcement. A criminal-forum seller separately claims a far larger scope reaching source
  control and production infrastructure — a claim the reporting outlet explicitly frames as the
  attacker's own, with its proposed mechanism labelled a guess.
discovered_at: "2026-08-10T04:52:00Z"
event_date: "2026-07-31"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, identity]
regions: [europe]
sectors: [retail, technology]
entities: [incident:zabka-supplier-account-jira-gitlab-secrets-2026-07]
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/"
    publisher: "Niebezpiecznik"
    date: "2026-08-03"
    role: primary
  - url: "https://sekurak.pl/potencjalny-wyciek-danych-z-zabki/"
    publisher: "Sekurak"
    date: "2026-08-03"
    role: corroborating
  - url: "https://www.rmf.fm/styl-zycia/news,n1012527,zabka-wydala-komunikat-po-ataku-hakerskim-zapewniamy-ze.html"
    publisher: "RMF FM"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Do nieautoryzowanego dostępu doszło przy wykorzystaniu konta zewnętrznego dostawcy usług."
    publisher: "Niebezpiecznik"
  - quote: "Zgodnie z naszą obecną wiedzą sprawca uzyskał dostęp do systemu kolejkowania zgłoszeń."
    publisher: "Niebezpiecznik"
  - quote: "Zgadujemy, że atakujący wykorzystał umieszczone w JIRZE informacje takie jak tokeny/hasła/konta testowe aby dostać się do kolejnych systemów."
    publisher: "Niebezpiecznik"
verification: multi-source
sourcing_note: >
  Żabka issued no reachable corporate press-room statement during this run; the official wording
  traces to a single press-office quote reproduced in near-identical form by the three independent Polish
  outlets cited here, which is why the confirmed facts are treated as corroborated. The scope claims are
  explicitly the attacker's, relayed from a criminal-forum listing, and the mechanism linking Jira to
  downstream systems is the reporting outlet's stated guess — both are attributed as such throughout
  and neither is carried as fact.
confidence: medium
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

Żabka has confirmed a compromise in a written statement its press office gave to Polish outlets, reproduced in near-identical wording by the outlets cited here. The confirmed facts are narrow and worth separating carefully from everything else in circulation. The company detected unauthorized access to selected technical resources supporting information exchange between franchisor and franchisees at the end of the preceding week; the access occurred "przy wykorzystaniu konta zewnętrznego dostawcy usług" — through the use of an external service provider's account — and was detected and immediately blocked under existing security procedures ([Niebezpiecznik, 2026-08-03](https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/)). On scope, Żabka says only that "zgodnie z naszą obecną wiedzą sprawca uzyskał dostęp do systemu kolejkowania zgłoszeń" — to its current knowledge the perpetrator gained access to the ticketing system. It states that transaction data, consumer services and the confidentiality of its loyalty-app data are unaffected, and that it has referred the matter to its own data-protection officer, to the Polish data-protection authority and to specialised law-enforcement bodies, with CERT Polska also notified ([RMF FM, 2026-08-04](https://www.rmf.fm/styl-zycia/news,n1012527,zabka-wydala-komunikat-po-ataku-hakerskim-zapewniamy-ze.html)). It declines to name the supplier or comment on the perpetrator.

Everything beyond that is claim. A seller on a criminal forum listed a data package on 2026-08-02, and Niebezpiecznik's itemised breakdown of that listing is prefaced explicitly as conditional on believing the attacker — hundreds of thousands of Jira issues across dozens of projects, service-desk tickets referencing internal retail and ERP systems, source code and infrastructure-as-code from a large number of repositories, and, claimed separately, live production material including a reused access token, message-broker and database credentials, and cloud infrastructure mapping. The mechanism connecting the two halves is not a forensic finding either: the outlet's own words are "Zgadujemy, że atakujący wykorzystał umieszczone w JIRZE informacje takie jak tokeny/hasła/konta testowe aby dostać się do kolejnych systemów" — *we guess* that the attacker used tokens, passwords or test accounts placed in Jira to reach further systems ([Niebezpiecznik, 2026-08-03](https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/)).

That distinction is the entry's reason for existing, and it cuts in a useful direction rather than a dismissive one. The confirmed half — a third-party account reaching an internal ticketing system — is a shape every public administration running an outsourced service desk shares, and it is confirmed by the victim. The unconfirmed half is a hypothesis about what ticketing systems contain, and it is a hypothesis defenders can test on their own estate today without waiting for anyone's forensics.

**Defender takeaway:** the question this raises for a European public-sector estate is answerable internally and does not depend on how the Żabka investigation resolves. What can a supplier's service-desk account actually reach, and what is sitting in the ticket bodies and attachments it can read? Ticketing systems accumulate credentials because pasting one into a ticket is the fastest way to get help, and the resulting secrets are rarely rotated, rarely scanned for, and rarely in scope when a supplier account is offboarded. Scope a supplier-account compromise as reaching everything that account can authenticate to *and* everything readable in what it can see — not as reaching the tickets alone.
