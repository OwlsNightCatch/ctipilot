---
schema: 1
kind: incident
title: "Revolut discloses a customer KYC data breach after fulfilling a fraudulent request sent from inside a genuine government agency's own email domain"
headline: "Revolut handed over customer identity documents and crypto histories because the request came from an authentic-looking government email address"
summary: >
  Revolut confirmed on 2026-09-12 that it disclosed customer KYC documents, selfies, IBANs and
  Bitcoin transaction histories to an unauthorized third party after an attacker submitted a
  fraudulent information request from an unauthorized mailbox operating inside a genuine
  government agency's own email domain. No Revolut system was breached and no malware was
  involved; the compromise was entirely of the process Revolut uses to verify inbound legal and
  regulatory data requests.
discovered_at: "2026-09-13T04:37:32Z"
updated_at: "2026-09-16T05:30:00Z"
event_date: "2026-09-12"
run_id: 2026-09-13T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity]
regions: [global, uk]
sectors: [finance]
entities: ["incident:revolut-fake-government-request-breach-2026-09"]
techniques: [T1598, T1684.001, T1657]
affected_products: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/"
    publisher: "TechCrunch"
    date: "2026-09-12"
    role: primary
  - url: "https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html"
    publisher: "Security Affairs"
    date: "2026-09-12"
    role: corroborating
  - url: "https://databreaches.net/2026/09/15/hackers-demand-10000-bitcoin-from-revolut-following-data-breach/"
    publisher: "DataBreaches.net (relaying Computing.co.uk)"
    date: "2026-09-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Revolut received a request for customer information that appeared to come from a legitimate government agency. The request came from an unauthorised email account sent directly using the official government agency's email domain."
    publisher: "Revolut (customer notification, via Security Affairs)"
  - quote: "As the communication carried valid domain authentication credentials, it was fulfilled under the reasonable belief that it was an authentic government agency request."
    publisher: "Revolut (customer notification, via Security Affairs)"
  - quote: "Revolut recently identified a sophisticated external impersonation scam where an unauthorised third party utilised a legitimate government agency domain email to submit fraudulent requests for information."
    publisher: "Revolut spokesperson, via TechCrunch"
  - quote: "People claiming responsibility for the incident have posted samples of the allegedly stolen information across several Telegram groups and the material appears to include details belonging to prominent individuals, including business leaders, sports professionals and performing artists."
    publisher: "Dev Kundaliya, via DataBreaches.net (relaying Computing.co.uk)"
  - quote: "The attackers have threatened to publish additional information “every day” unless Revolut pays a ransom of 10,000 Bitcoin – currently worth more than $782m."
    publisher: "Dev Kundaliya, via DataBreaches.net (relaying Computing.co.uk)"
verification: single-source-victim
sourcing_note: >
  All reporting on the original disclosure traces to Revolut's own customer notification and
  spokesperson statement; no independent forensic or regulatory confirmation of the incident's
  scope or mechanism has been published, and Revolut declines to name the government agency,
  country, or number of customers affected. The 2026-09-16 extortion-escalation development is
  sourced to DataBreaches.net's relay of Computing.co.uk reporting; Computing.co.uk itself
  remained unreachable on every transport tried as of 2026-09-16, and neither Revolut nor a second
  outlet has confirmed the ransom demand, the Telegram posting, or the alleged victim identities,
  which are treated as attacker-stated claims, not established fact.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-13T14:05:00Z"
    run_id: 2026-09-13T1307Z-audit
    type: correction
    summary: >
      The body rendered Revolut's notification with an inserted ellipsis that dropped the words
      "sent directly" from the middle of the quoted sentence. The full sentence is restored. The
      elided words carry the operative detail: the fraudulent request was sent directly from the
      government agency's own domain, not merely styled to resemble it.
    fields: [body]
  - at: "2026-09-16T05:30:00Z"
    run_id: 2026-09-16T0409Z-intel
    type: update
    summary: >
      Parties claiming responsibility have posted samples of the allegedly stolen data across
      multiple Telegram groups and are demanding a 10,000 Bitcoin ransom, threatening daily
      further publication if unpaid; sourced to a relay of reporting whose original outlet remains
      unreachable as of 2026-09-16, so the claims are attacker-stated, not confirmed by Revolut or
      a second source.
    fields: [techniques, sources, evidence, sourcing_note, confidence, body]
migrated_from: null
---

Revolut confirmed to TechCrunch on 2026-09-12 that it disclosed sensitive customer data after receiving a fraudulent information request sent from "an unauthorised email account sent directly using the official government agency's email domain" ([Revolut, via Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)); Security Affairs assesses the attacker either registered a rogue mailbox within that domain or compromised an existing one. Because the message carried valid domain-authentication credentials, Revolut's compliance and KYC-response process treated it as authentic and fulfilled it: exposed data included full name, date of birth, occupation, postal and email address, phone number, passport or driver's-licence copies, verification selfies, IBAN and account statements, withdrawal records and full transaction history including Bitcoin ([Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)). No Revolut system was compromised and no malware was involved; the entire incident was a social-engineering compromise of the legal and regulatory data-request channel rather than a technical intrusion. Revolut says a "limited" number of customers were affected and declines to name the government agency, the country, or the customer count. Revolut discovered the fraud only when it independently contacted the agency to verify the request and was told the agency never sent it; it has since blocked the sending mailbox and notified the agency, law enforcement and financial regulators.

The same weakness applies to any organization whose legal or regulatory data-request process trusts that a request's sending domain is proof of the sender's authority: an attacker who obtains or spoofs access to a single mailbox on that domain can submit an urgent, seemingly authentic request that bypasses the normal verification a company would otherwise apply. Here that pattern reached a major fintech's KYC/AML compliance channel, and the entire compromise happened at the request-verification step: no phishing link was clicked and no credential was stolen, only an email that domain-authenticated correctly and asked for the right kind of data in a plausible way.

For any organization that operates a legal or regulatory data-request intake process, the transferable lesson is that domain-level email authentication (the same trust SPF, DKIM and DMARC exist to establish) is not proof of institutional authority: an adversary who controls, or convincingly spoofs, a single mailbox on a trusted government or law-enforcement domain can defraud any recipient who verifies a request only by checking that it came from the right domain. This cuts both ways for a public-sector authority: any authority that itself issues legal data requests to third parties (banks, telcos, cloud providers, ISPs) as part of investigations should assume that a compromise of its own mail infrastructure could be used to defraud those third parties in its name, and should expect the recipients of its own legitimate requests to apply out-of-band verification rather than treat that as an insult to its authority.

**Defender takeaway:** any legal or regulatory data-request intake process should require out-of-band verification, a callback to a directory-listed number rather than a reply to the same email thread, before releasing sensitive customer data, regardless of how authentic the sending domain looks; log and periodically audit which staff can approve bulk or sensitive data releases against the legal-request queue, since that approval step is exactly the chokepoint this attacker targeted.

## Correction — 2026-09-13T14:05:00Z

The quotation from Revolut's customer notification in the opening paragraph was rendered with an inserted ellipsis. Revolut's sentence reads in full: "The request came from an unauthorised email account sent directly using the official government agency's email domain" ([Revolut, via Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)). The two elided words are the operative ones for a defender reading this as a control failure: the request was **sent directly** from the agency's own domain rather than from a lookalike, which is why domain authentication passed and why the sending domain told Revolut's reviewer nothing about the sender's authority.

## Update — 2026-09-16T05:30:00Z

Parties claiming responsibility for the breach have posted samples of the allegedly stolen data across several Telegram groups, reported to include details belonging to "prominent individuals, including business leaders, sports professionals and performing artists," and are demanding Revolut pay a ransom of 10,000 Bitcoin, worth more than 782 million US dollars at the time of reporting, threatening to publish further data "every day" if unpaid ([DataBreaches.net, relaying Computing.co.uk, 2026-09-15](https://databreaches.net/2026/09/15/hackers-demand-10000-bitcoin-from-revolut-following-data-breach/)). This is the first extortion dimension reported on an incident this entry previously described only as a disclosed process-abuse breach with no stated attacker demand. Computing.co.uk, the outlet that originated this reporting, remains unreachable on every transport tried as of 2026-09-16; neither Revolut nor a second independent outlet has confirmed the ransom figure, the Telegram posting, or the claimed victim identities, so these remain attacker-stated claims rather than established fact.
