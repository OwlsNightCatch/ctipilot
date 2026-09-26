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
  regulatory data requests. Threat-intelligence firm Hudson Rock later reported the mailbox was
  an infostealer-compromised account on Italy's Ministry of the Interior's own domain, though the
  attacker's own account of how remains only partly corroborated. A group calling itself
  "Imnotavillain" now claims sole authorship and has pivoted to individually extorting roughly 680
  named customers directly.
discovered_at: "2026-09-13T04:37:32Z"
updated_at: "2026-09-26T04:04:42Z"
event_date: "2026-09-12"
run_id: 2026-09-13T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity]
regions: [global, uk]
sectors: [finance]
entities: ["incident:revolut-fake-government-request-breach-2026-09", "actor:imnotavillain"]
techniques: [T1598, T1684.001, T1657, T1586.002, T1070.008]
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
  - url: "https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering"
    publisher: "Hudson Rock"
    date: "2026-09-15"
    role: primary
  - url: "https://cyberinsider.com/revolut-hackers-used-infostealer-to-hijack-italian-government-emails/"
    publisher: "CyberInsider"
    date: "2026-09-16"
    role: corroborating
  - url: "https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/"
    publisher: "The Irish Times"
    date: "2026-09-17"
    role: corroborating
  - url: "https://www.heise.de/news/Neobank-Revolut-Cybergang-Imnotavillain-behauptet-Datendiebstahl-11465363.html"
    publisher: "Heise Online"
    date: "2026-09-25"
    role: primary
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
  - quote: "The hacker gained access to government employee accounts using an infostealer. After gaining entry to an employee's email, they would log in, add a recovery email under their control, begin logging activities, and silently monitor communications."
    publisher: "The Duel Investigations Team, via Hudson Rock"
    source_url: "https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering"
  - quote: "By checking Hudson Rock's extensive cybercrime database, we identified approximately 300 compromised pec.interno.it webmail logins stemming from already infected machines. Based on this intelligence, we assess that it is highly unlikely the hacker actively infected these specific employees themselves."
    publisher: "Hudson Rock"
    source_url: "https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering"
  - quote: "Upon receiving a reply to their fraudulent emails, they would immediately download it as a .eml file and delete it before the actual account owner noticed."
    publisher: "The Duel Investigations Team, via Hudson Rock"
    source_url: "https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering"
  - quote: "The data breach is understood to have affected at least 680 customer accounts."
    publisher: "The Irish Times"
    source_url: "https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/"
  - quote: "one of their former accomplices took only part of the obtained data. He is posing as the actual perpetrator. He is, however, a fraud." # (translated from German)
    original: "einer ihrer ehemaligen Mittäter lediglich einen Teil der ergatterten Daten mitgenommen habe. Er gebe sich als der eigentliche Täter aus. Dieser sei jedoch ein Betrüger."
    publisher: "Heise Online"
    source_url: "https://www.heise.de/news/Neobank-Revolut-Cybergang-Imnotavillain-behauptet-Datendiebstahl-11465363.html"
  - quote: "'Imnotavillain' is now offering the data sets of 680 high-ranking individuals for sale. As a special twist, the perpetrators are also luring the individual data subjects — they could buy the removal of their own record before the data is sold as a whole to interested parties in the future." # (translated from German)
    original: "„Imnotavillain“ bietet nun Datensätze von 680 hochrangigen Persönlichkeiten zum Verkauf an. Als Besonderheit ködern die Täter auch die einzelnen Betroffenen – sie könnten die Entfernung ihres Datensatzes erkaufen, bevor die Daten künftig als Ganzes an Interessenten veräußert würden."
    publisher: "Heise Online"
    source_url: "https://www.heise.de/news/Neobank-Revolut-Cybergang-Imnotavillain-behauptet-Datendiebstahl-11465363.html"
verification: single-source-victim
sourcing_note: >
  All reporting on the original disclosure traces to Revolut's own customer notification and
  spokesperson statement; no independent forensic or regulatory confirmation of the incident's
  scope or mechanism has been published, and Revolut declines to name the government agency,
  country, or number of customers affected. The 2026-09-16 extortion-escalation development is
  sourced to DataBreaches.net's relay of Computing.co.uk reporting, unconfirmed by Revolut or a
  second source. The access-vector detail (infostealer-compromised pec.interno.it mailboxes)
  traces to Hudson Rock's own independent finding of roughly 300 already-compromised credentials
  in its cybercrime database, genuine independent corroboration, but the surrounding attacker
  narrative (the five-month timeline, the anti-forensic .eml-deletion technique, the
  forged-court-orders pivot) originates from the attacker's own account to a third outlet, Duel,
  relayed via Hudson Rock and CyberInsider rather than independently verified; the attacker's own
  claimed initial-access method was itself inconsistent (first a RAT, then an infostealer), a
  reliability signal Hudson Rock itself flags. The actor-identity claim and its extortion-tactic
  pivot are the actor's own darknet statements, sourced to Heise ("Imnotavillain") and The Irish
  Times ("iamnotavillain") separately — no cited source explicitly states the two spellings name the
  same actor, though both describe the same Revolut breach and neither is independently verified by
  Revolut, a researcher, or law enforcement; a rival claimant disputes authorship, and neither
  party's identity is established.
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
  - at: "2026-09-18T05:08:00Z"
    run_id: 2026-09-18T0410Z-intel
    type: update
    summary: >
      Hudson Rock reports the access vector: infostealer-compromised webmail accounts on
      pec.interno.it, Italy's Ministry of the Interior's certified-email domain, monitored for
      roughly five months with an anti-forensic technique of deleting fraudulent outgoing mail
      and downloading-then-deleting replies. Hudson Rock's own database independently found
      approximately 300 already-compromised pec.interno.it credentials, though the attacker's own
      inconsistent account of infecting the officials directly is not independently confirmed.
    fields: [techniques, sources, evidence, summary, sourcing_note, body]
  - at: "2026-09-26T04:04:42Z"
    run_id: 2026-09-26T0404Z-intel
    type: update
    summary: >
      A group calling itself "Imnotavillain" now claims sole authorship of the breach on its own
      darknet site, disputing a rival claimant it calls a fraud, and has pivoted from its earlier
      bulk ransom demand to individually extorting roughly 680 named customers, offering each
      removal from a future bulk publication in exchange for payment. The Irish Times independently
      confirms the customer count previously unverifiable in this entry.
    fields: [entities, sources, evidence, summary, sourcing_note, body]
migrated_from: null
---

Revolut confirmed to TechCrunch on 2026-09-12 that it disclosed sensitive customer data after receiving a fraudulent information request sent from "an unauthorised email account sent directly using the official government agency's email domain" ([Revolut, via Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)); Security Affairs assesses the attacker either registered a rogue mailbox within that domain or compromised an existing one. Because the message carried valid domain-authentication credentials, Revolut's compliance and KYC-response process treated it as authentic and fulfilled it: exposed data included full name, date of birth, occupation, postal and email address, phone number, passport or driver's-licence copies, verification selfies, IBAN and account statements, withdrawal records and full transaction history including Bitcoin ([Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)). "No systems were compromised, no malware was used"; the entire incident was a social-engineering compromise of the legal and regulatory data-request channel rather than a technical intrusion ([Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)). Revolut confirmed to TechCrunch that a "limited" number of customers were affected, declining to disclose the exact count, the government agency involved, or whether the incident was confined to one market ([TechCrunch, 2026-09-12](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/)). Revolut discovered the fraud only after independently contacting the government agency to verify the request, at which point the agency confirmed it had not made it ([Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)); it has since blocked the sending mailbox and notified the agency, law enforcement and financial regulators ([TechCrunch, 2026-09-12](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/)).

The same weakness applies to any organization whose legal or regulatory data-request process trusts that a request's sending domain is proof of the sender's authority: an attacker who obtains or spoofs access to a single mailbox on that domain can submit an urgent, seemingly authentic request that bypasses the normal verification a company would otherwise apply. Here that pattern reached a major fintech's KYC/AML compliance channel, and the entire compromise happened at the request-verification step: no phishing link was clicked and no credential was stolen, only an email that domain-authenticated correctly and asked for the right kind of data in a plausible way.

For any organization that operates a legal or regulatory data-request intake process, the transferable lesson is that domain-level email authentication (the same trust SPF, DKIM and DMARC exist to establish) is not proof of institutional authority: an adversary who controls, or convincingly spoofs, a single mailbox on a trusted government or law-enforcement domain can defraud any recipient who verifies a request only by checking that it came from the right domain. This cuts both ways for a public-sector authority: any authority that itself issues legal data requests to third parties (banks, telcos, cloud providers, ISPs) as part of investigations should assume that a compromise of its own mail infrastructure could be used to defraud those third parties in its name, and should expect the recipients of its own legitimate requests to apply out-of-band verification rather than treat that as an insult to its authority.

**Defender takeaway:** any legal or regulatory data-request intake process should require out-of-band verification, a callback to a directory-listed number rather than a reply to the same email thread, before releasing sensitive customer data, regardless of how authentic the sending domain looks; log and periodically audit which staff can approve bulk or sensitive data releases against the legal-request queue, since that approval step is exactly the chokepoint this attacker targeted.

## Correction — 2026-09-13T14:05:00Z

The quotation from Revolut's customer notification in the opening paragraph was rendered with an inserted ellipsis. Revolut's sentence reads in full: "The request came from an unauthorised email account sent directly using the official government agency's email domain" ([Revolut, via Security Affairs, 2026-09-12](https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html)). The two elided words are the operative ones for a defender reading this as a control failure: the request was **sent directly** from the agency's own domain rather than from a lookalike, which is why domain authentication passed and why the sending domain told Revolut's reviewer nothing about the sender's authority.

## Update — 2026-09-16T05:30:00Z

Parties claiming responsibility for the breach have posted samples of the allegedly stolen data across several Telegram groups, reported to include details belonging to "prominent individuals, including business leaders, sports professionals and performing artists," and are demanding Revolut pay a ransom of 10,000 Bitcoin, worth more than 782 million US dollars at the time of reporting, threatening to publish further data "every day" if unpaid ([DataBreaches.net, relaying Computing.co.uk, 2026-09-15](https://databreaches.net/2026/09/15/hackers-demand-10000-bitcoin-from-revolut-following-data-breach/)). This is the first extortion dimension reported on an incident this entry previously described only as a disclosed process-abuse breach with no stated attacker demand. Computing.co.uk, the outlet that originated this reporting, remains unreachable on every transport tried as of 2026-09-16; neither Revolut nor a second independent outlet has confirmed the ransom figure, the Telegram posting, or the claimed victim identities, so these remain attacker-stated claims rather than established fact.

## Update — 2026-09-18T05:08:00Z

Hudson Rock, relaying the attacker's own account to the Duel Investigations Team, reports the access vector claimed behind the fraudulent request: infostealer-compromised webmail accounts on pec.interno.it, the certified-email domain of Italy's Ministry of the Interior. Per that account, the hacker gained access to government employee accounts using an infostealer, and after gaining entry to an employee's email, would log in, add a recovery email under their control, begin logging activities, and silently monitor communications ([The Duel Investigations Team, via Hudson Rock, 2026-09-15](https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering)). Upon receiving a reply to their fraudulent emails, the operator would immediately download it as a .eml file and delete it before the actual account owner noticed, an anti-forensic technique the account says let the campaign run for roughly five months, beginning with forged court orders before pivoting to Revolut Bank UAB, Revolut's Lithuania-licensed EU subsidiary obligated to respond to European Investigation Orders ([The Duel Investigations Team, via Hudson Rock, 2026-09-15](https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering)). Hudson Rock's own cybercrime database independently identified approximately 300 compromised pec.interno.it webmail logins from already-infected machines, and on that basis assesses it is highly unlikely the hacker actively infected these specific employees themselves ([Hudson Rock, 2026-09-15](https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering)) — the attacker's own account of the initial-access method was itself inconsistent, first describing a remote-access trojan and later an infostealer. This resolves the access-vector question the original disclosure left open; CyberInsider reports Revolut told it only that the fraudulent request "appeared authentic based on the technical indicators available to its staff" ([CyberInsider, 2026-09-16](https://cyberinsider.com/revolut-hackers-used-infostealer-to-hijack-italian-government-emails/)), and Revolut itself has not confirmed the five-month timeline, the pec.interno.it detail, or the anti-forensic technique. CyberInsider separately references unnamed "separate reporting" giving a customer count of around 680, a figure this entry cannot independently verify.

## Update — 2026-09-26T04:04:42Z

The Irish Times independently confirms the customer count this entry previously could not verify: "The data breach is understood to have affected at least 680 customer accounts" ([The Irish Times, 2026-09-17](https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/)), reporting on a group spelling its name "iamnotavillain." A group whose name Heise Online spells "Imnotavillain" now claims sole responsibility for the breach on its own darknet site, disputing a rival claimant it says "took only part of the obtained data" and "is posing as the actual perpetrator" while calling that rival "a fraud" ([Heise Online, 2026-09-25](https://www.heise.de/news/Neobank-Revolut-Cybergang-Imnotavillain-behauptet-Datendiebstahl-11465363.html), translated from German) — no cited source explicitly states the two spellings name the same actor, and neither claimant's identity is independently established. Having already issued a 6,000 XMR ($3 million) ransom ultimatum to Revolut itself with a 24-hour deadline, published on its own website with a countdown clock ([The Irish Times, 2026-09-17](https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/)) — no cited source states what happened when that deadline passed — a separate, larger 10,000 Bitcoin demand this entry's 2026-09-16 update recorded came from a single, since-unreachable relay and is not corroborated by this Irish Times reporting or any other cited source, and the two figures are not reconciled here — a group under this name has now pivoted to individually extorting the roughly 680 named customers directly: it is "offering the data sets of 680 high-ranking individuals for sale" and letting each "buy the removal of their own record before the data is sold as a whole to interested parties in the future," publishing sample records including full name, email, phone number, address, account IDs, crypto withdrawal and balance data, bank transactions, and KYC documents and selfies as proof ([Heise Online, 2026-09-25](https://www.heise.de/news/Neobank-Revolut-Cybergang-Imnotavillain-behauptet-Datendiebstahl-11465363.html), translated from German). Revolut itself told the Irish Times at the time of the original ultimatum that it "has not received any direct contact or demand from the individuals or group making these claims" ([The Irish Times, 2026-09-17](https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/)); neither Revolut nor an independent researcher has confirmed either claimant's identity or the completeness of the data set.
