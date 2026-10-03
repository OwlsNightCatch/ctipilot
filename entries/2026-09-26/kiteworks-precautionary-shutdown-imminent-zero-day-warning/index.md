---
schema: 1
kind: threat
title: "Kiteworks (formerly Accellion) tells customers worldwide to shut down after 'credible' law-enforcement intelligence of an imminent attack, then publishes fixes including an unauthenticated chain to root in its Email Protection Gateway (CVE-2026-54154, CVSS 10.0)"
headline: "Kiteworks warned of an imminent attack; its 2026-09-30 advisories now include an unauthenticated root-level code-execution chain in the mail gateway"
summary: >
  Kiteworks, a secure managed-file-transfer and confidential-communications
  platform rebranded from Accellion and marketed to government agencies and
  financial institutions, emailed customers worldwide on 2026-09-25 urging a
  precautionary shutdown of every Kiteworks system over the weekend
  of 2026-09-26 (six hours in press coverage, nine on Kiteworks' own page) after receiving "credible threat intelligence from law
  enforcement" of a possible imminent attack. No CVE was known for the
  threat behind the warning and Kiteworks says it is not aware of any actual compromise; the Central
  European shutdown window falls in the timezone Switzerland shares.
  Kiteworks later said its engineering and security work during the shutdown
  led to the discovery and fix of a previously unknown critical vulnerability
  in a capability enabled for under 1% of its customers, with no indication
  it was exploited.
  On 2026-09-30 Kiteworks published advisories for Email Protection Gateway, Core and Secure Data Forms, including
  CVE-2026-54154, a maximum-severity unauthenticated code-execution chain to root in all Email Protection Gateway
  versions before 9.4.1, with further critical fixes in 9.5.0 and 9.5.1, three of them CVSS 9.8 account takeovers; none is stated to be exploited.
discovered_at: "2026-09-26T04:04:42Z"
updated_at: "2026-10-02T04:58:16Z"
event_date: "2026-09-25"
run_id: 2026-09-26T0404Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, zero-day, rce, pre-auth, patch-available]
regions: [global, europe, switzerland]
sectors: [public-sector, finance]
entities: ["product:kiteworks", "product:kiteworks-core", "product:kiteworks-email-protection-gateway", "product:kiteworks-secure-data-forms"]
techniques: [T1190, T1068]
affected_products: ["Kiteworks", "Kiteworks Advanced Forms", "Kiteworks Email Protection Gateway", "Kiteworks Core", "Kiteworks Secure Data Forms"]
cves:
  - id: CVE-2026-54154
    cvss: "10.0 (maximum severity per BleepingComputer; vector AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Email Protection Gateway versions before 9.4.1"
    fixed: "Email Protection Gateway 9.4.1 or later"
  - id: CVE-2026-85065
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Email Protection Gateway versions before 9.5.0"
    fixed: "9.5.0 or later"
  - id: CVE-2026-85066
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Email Protection Gateway versions before 9.5.0"
    fixed: "9.5.0 or later"
  - id: CVE-2026-102115
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Core versions before 9.5.0"
    fixed: "9.5.0 or later"
  - id: CVE-2026-102149
    cvss: "9.4"
    epss: 0.00332
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Email Protection Gateway versions before 9.5.1"
    fixed: "9.5.1 or later"
  - id: CVE-2026-102147
    cvss: "9.3"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "All Kiteworks Core versions before 9.5.1"
    fixed: "9.5.1 or later"
  - id: CVE-2026-102142
    cvss: "7.2"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "All Kiteworks Core versions before 9.5.1"
    fixed: "9.5.1 or later"
  - id: CVE-2026-102150
    cvss: "7.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Kiteworks Secure Data Forms 9.3.0 up to before 9.5.1 (versions before 9.3.0 are not affected)"
    fixed: "9.5.1 or later"
sources:
  - url: "https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html"
    publisher: "Heise Online"
    date: "2026-09-25"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
    publisher: "BleepingComputer"
    date: "2026-09-25"
    role: primary
  - url: "https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-25"
    role: corroborating
  - url: "https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/"
    publisher: "TechCrunch"
    date: "2026-09-25"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12985"
    publisher: "NCSC Switzerland, Cyber Security Hub"
    date: "2026-09-25"
    role: corroborating
  - url: "https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/"
    publisher: "Kiteworks"
    date: "2026-09-27"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3602"
    publisher: "BSI CERT-Bund (WID-SEC-2026-3602)"
    date: "2026-09-27"
    role: corroborating
  - url: "https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/"
    publisher: "Kiteworks"
    date: "2026-09-28"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-5xhq-9wq3-rvj6"
    publisher: "Kiteworks (security advisory, Email Protection Gateway)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-h669-jj53-h764"
    publisher: "Kiteworks (security advisory, Email Protection Gateway)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-rwpq-5xfv-54pv"
    publisher: "Kiteworks (security advisory, Email Protection Gateway)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-q76w-qv9j-q639"
    publisher: "Kiteworks (security advisory, Core)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-c9w5-4frw-7wqq"
    publisher: "Kiteworks (security advisory, Email Protection Gateway)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-xgh2-fgj6-w93r"
    publisher: "Kiteworks (security advisory, Core)"
    date: "2026-09-30"
    role: primary
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-vwvw-rp3m-rm37"
    publisher: "Kiteworks (security advisory, Secure Data Forms)"
    date: "2026-09-30"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/"
    publisher: "BleepingComputer"
    date: "2026-10-01"
    role: corroborating
  - url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-gmgg-7xhc-75f9"
    publisher: "Kiteworks (security advisory, Core)"
    date: "2026-09-30"
    role: primary
closed_sources: []
evidence:
  - quote: "We have received credible threat intelligence from law enforcement indicating an attack on Kiteworks systems may be imminent this weekend. We strongly recommend you shut down your Kiteworks system for six hours"
    publisher: "Kiteworks CISO Frank Balonis, via Heise Online"
    source_url: "https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html"
  - quote: "We are not aware of any compromise of Kiteworks systems, and this advisory is preventative rather than a response to a confirmed breach"
    publisher: "Kiteworks, statement to BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
  - quote: "All known vulnerabilities are addressed in our current release, 9.5.1, and we continue to recommend customers run the latest version."
    publisher: "Kiteworks, statement to BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
  - quote: "There is no known CVE, patch, or additional technical details available – but nobody requests that their entire customer base unplug production systems over the weekend because of a hunch."
    publisher: "Jake Knott, watchTowr, via The Record (Recorded Future News)"
    source_url: "https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident"
  - quote: "As of September 27th, the shutdown recommendation is now lifted for all customers. If you have not already restarted, you may bring your Kiteworks system back online."
    publisher: "Kiteworks"
    source_url: "https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/"
  - quote: "We have no indication that Kiteworks or our customers' systems have been compromised, so this advisory is preventative rather than a response to a confirmed breach."
    publisher: "Frank Balonis, CISO, Kiteworks"
    source_url: "https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/"
  - quote: "An attacker can exploit a vulnerability in Kiteworks Advanced Forms to carry out an unspecified attack." # translated from German
    publisher: "BSI CERT-Bund (WID-SEC-2026-3602)"
    source_url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3602"
    original: "Ein Angreifer kann eine Schwachstelle in Kiteworks Advanced Forms ausnutzen, um einen nicht näher spezifizierten Angriff durchzuführen."
  - quote: "During the shutdown, this activity led to the discovery of a previously unknown critical vulnerability confined to a capability that is enabled for less than 1% of the customer base."
    publisher: "Kiteworks"
    source_url: "https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/"
  - quote: "Kiteworks developed and deployed a fix during the window, applied an additional protective layer across all environments, and has no indication the vulnerability was ever exploited."
    publisher: "Kiteworks"
    source_url: "https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/"
  - quote: "A remote attacker may be able to execute arbitrary code with root privileges."
    publisher: "Kiteworks (security advisory, Email Protection Gateway)"
    source_url: "https://github.com/kiteworks/security-advisories/security/advisories/GHSA-5xhq-9wq3-rvj6"
  - quote: "The flaw affects all Kiteworks Email Protection Gateway releases before 9.4.1 and is now patched in versions 9.4.1 or later."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/"
  - quote: "Kiteworks has yet to share additional details on the fixed vulnerability and has not yet assigned a CVE ID for easy tracking."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/"
verification: single-source
sourcing_note: >
  Every outlet's reporting traces to Kiteworks' own customer notification and CISO statements, and the underlying
  threat remains the vendor's own unconfirmed, precautionary characterization. BSI's WID-SEC-2026-3602 advisory names
  Kiteworks' own press release as its source, so it is the same assessor with a second publisher.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Kiteworks deployment to 9.5.1 or later (the Email Protection Gateway needs at least 9.4.1 for CVE-2026-54154), and ask Kiteworks Support in writing whether the flaw it found during the shutdown needs customer-side action on self-hosted instances."
updates:
  - at: "2026-09-29T04:50:00Z"
    run_id: 2026-09-29T0405Z-intel
    type: update
    summary: >
      Kiteworks lifted the shutdown recommendation for all customers on 2026-09-27, stating it found no
      indication of compromise. Germany's BSI (WID-SEC-2026-3602) and NCSC Switzerland now name the
      specific vulnerable component for the first time: Kiteworks Advanced Forms below version 9.5.1,
      fixed in 9.5.1; no CVE has been assigned. Priority moves from high to notable now that the acute
      threat has resolved without confirmed compromise.
    fields: [priority, tags, affected_products, sources, evidence, sourcing_note, actions, body]
  - at: "2026-09-30T05:21:00Z"
    run_id: 2026-09-30T0404Z-intel
    type: update
    summary: >
      Kiteworks's own release of 2026-09-28 says its engineering and security work during the customer-wide shutdown
      led to the discovery of a previously unknown critical vulnerability in a capability enabled for under 1% of its customers, that it deployed a fix during the
      window and an extra protective layer across all environments, and that it has no indication the vulnerability
      was exploited. The release names no component or CVE.
    fields: [summary, sources, evidence, actions, body]
  - at: "2026-10-02T04:58:16Z"
    run_id: 2026-10-02T0404Z-intel
    type: update
    summary: >
      Kiteworks published GitHub advisories on 2026-09-30 naming CVE-2026-54154, a maximum-severity unauthenticated
      code-execution chain to root in all Email Protection Gateway versions before 9.4.1, three CVSS 9.8 account
      takeovers fixed in 9.5.0 (CVE-2026-85065, CVE-2026-85066, CVE-2026-102115), and further account takeover,
      security-bypass and command-execution flaws in Email Protection Gateway, Core and Secure Data Forms fixed in
      9.5.1. None is stated as exploited and no source ties them to the flaw found during the shutdown. Priority moves
      from notable to high because the chain is unauthenticated and reaches root. The earlier text now gives the
      nine-hour shutdown window from Kiteworks' own page next to the six hours in press coverage, and the sourcing
      rests on the vendor alone.
    fields: [title, headline, summary, priority, tags, techniques, affected_products, cves, sources, evidence, actions, verification, entities, sourcing_note, body]
migrated_from: null
---

Kiteworks, a secure managed-file-transfer and confidential-communications platform rebranded from Accellion in 2021 and marketed to government agencies, financial institutions and enterprises, emailed customers worldwide on 2026-09-25 urging a precautionary shutdown of every Kiteworks system, staggered by timezone; press coverage put it at six hours, and the Central European window falls 04:00–10:00 CEST on Saturday 2026-09-26, a timezone Switzerland shares ([Heise Online, 2026-09-25](https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html); [TechCrunch, 2026-09-25](https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/)). Kiteworks' own page gives the recommended window as nine hours ([Kiteworks, 2026-09-27](https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/)). CISO Frank Balonis wrote to customers, in an email obtained by Heise Online, that the company "received credible threat intelligence from law enforcement indicating an attack on Kiteworks systems may be imminent this weekend" ([Heise Online, 2026-09-25](https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html)), and recommended shutting systems down even where they are not directly internet-facing, since the possible access route is unconfirmed. No CVE was known for the threat behind the warning ([The Record, 2026-09-25](https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident)), and Kiteworks stated plainly it was "not aware of any compromise of Kiteworks systems" and that "all known vulnerabilities are addressed in our current release, 9.5.1" ([BleepingComputer, 2026-09-25](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)); the advisory is preventative, not a confirmed-breach response. Researcher Kevin Beaumont's Shodan search found at least a thousand internet-facing Kiteworks instances, though TechCrunch notes the count is likely an overcount of actually-affected customer systems ([TechCrunch, 2026-09-25](https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/)), and watchTowr's Jake Knott called the request itself unusual: "nobody requests that their entire customer base unplug production systems over the weekend because of a hunch" ([The Record, 2026-09-25](https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident)).

The precedent class is exactly the one that matters for public-sector defenders: BleepingComputer notes that the Clop extortion gang "has a long history of targeting enterprise platforms in data-theft attacks," naming Accellion FTA, GoAnywhere MFT, SolarWinds Serv-U FTP, Cleo, and MOVEit Transfer as past victims of that pattern ([BleepingComputer, 2026-09-25](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)); no actor has been named or confirmed for this specific warning by Kiteworks, the FBI, or CISA. Kiteworks itself was formerly Accellion, whose FTA product was the subject of exactly this kind of zero-day mass exploitation in December 2020, when a Clop-linked group stole data from dozens of high-profile organizations ([The Record, 2026-09-25](https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident)).

**Defender takeaway:** the shutdown ended without a claimed compromise, but Kiteworks has since published a maximum-severity unauthenticated code-execution chain to root in the Email Protection Gateway and further critical fixes. Run 9.5.1 or later on every deployment (Email Protection Gateway at least 9.4.1), and put the open question to Kiteworks Support in writing: the vendor has not said whether the critical flaw it found during the shutdown needs customer-side action beyond its notice to customers with self-hosted Advanced Forms to contact Customer Support ([Kiteworks, 2026-09-27](https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/)).

## Update — 2026-09-29T04:50:00Z

Kiteworks' own press release states the recommended shutdown window was nine hours, while press coverage of the initial advisory reported six; the vendor's own page is the more authoritative figure, and neither the press coverage nor Kiteworks' later statement explains the difference. Kiteworks updated its own press release on 2026-09-27 to state the shutdown recommendation is
lifted: "As of September 27th, the shutdown recommendation is now lifted for all customers. If you have not
already restarted, you may bring your Kiteworks system back online"
([Kiteworks, 2026-09-27](https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/)).
CISO Frank Balonis reiterated the company found no evidence of compromise: "We have no indication that
Kiteworks or our customers' systems have been compromised, so this advisory is preventative rather than a
response to a confirmed breach"
([Kiteworks, 2026-09-27](https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/)).
Germany's BSI published advisory WID-SEC-2026-3602 on 2026-09-27, citing the Kiteworks press release as its
source and naming the vulnerable component for the first time: "An attacker can exploit a vulnerability in
Kiteworks Advanced Forms to carry out an unspecified attack" (translated from German)
([BSI CERT-Bund, 2026-09-27](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3602)),
listing Advanced Forms versions below 9.5.1 as affected and fixed in 9.5.1; NCSC Switzerland's Cyber Security
Hub advisory was updated the same day with the lifted-shutdown status. No CVE has been assigned to date, and
the BSI record carries no vulnerability-class (CWE) description beyond "unspecified attack": genuinely thin technical detail from the vendor side even now.


## Update — 2026-09-30T05:21:00Z

Kiteworks's own release, dated 2026-09-28, reports the outcome of the shutdown: the threat window "passed without incident", and the company has no indication that any Kiteworks or customer system was compromised ([Kiteworks, 2026-09-28](https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/)). It adds that its engineering and security activity during the shutdown led to the discovery of "a previously unknown critical vulnerability confined to a capability that is enabled for less than 1% of the customer base", that Kiteworks developed and deployed a fix during the window and applied an additional protective layer across all environments, and that it has no indication the vulnerability was ever exploited; all other Kiteworks products were unaffected ([Kiteworks, 2026-09-28](https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/)). The release names no component and no CVE; whether it is the Advanced Forms flaw that BSI listed on 2026-09-27 is not stated. The vendor's own statements are the only source for the discovery, the fix and the absence of exploitation, and customers with questions are pointed to Kiteworks Technical Support ([Kiteworks, 2026-09-28](https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/)).

## Update — 2026-10-02T04:58:16Z

On 2026-09-30 Kiteworks published GitHub security advisories for Email Protection Gateway, Core and Secure Data Forms. The most severe, CVE-2026-54154, affects all Email Protection Gateway versions before 9.4.1: a remote attacker may be able to execute arbitrary code with root privileges, with a CVSS 3.1 vector of network, low complexity, no privileges and no user interaction, and Kiteworks credits three researchers who reported it through its YesWeHack bug-bounty programme ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-5xhq-9wq3-rvj6)). BleepingComputer, quoting the advisory, describes input-handling flaws in publicly reachable endpoints that potentially allowed unauthenticated code execution and, by chaining local weaknesses, escalation to root, and lists path traversal, code injection and missing authentication as the chain ([BleepingComputer, 2026-10-01](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)). Three further advisories rated CVSS 9.8 describe network-reachable account takeovers that need no privileges or user interaction and are fixed in 9.5.0: two in Email Protection Gateway, CVE-2026-85065 ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-h669-jj53-h764)) and CVE-2026-85066 ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-rwpq-5xfv-54pv)), and one in Core, CVE-2026-102115 ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-q76w-qv9j-q639)). BleepingComputer counts 11 critical fixes in Core and Email Protection Gateway beyond the root chain ([BleepingComputer, 2026-10-01](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)). Further fixes in 9.5.1 include an Email Protection Gateway account takeover, CVE-2026-102149, reachable over the network without authentication ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-c9w5-4frw-7wqq)); a Core account takeover to administrative access through an injection flaw, CVE-2026-102147, that needs user interaction ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-xgh2-fgj6-w93r)); a Core command execution flaw for administrators, CVE-2026-102142 ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-gmgg-7xhc-75f9)); and a Secure Data Forms security bypass, CVE-2026-102150, in versions 9.3.0 up to before 9.5.1 ([Kiteworks, 2026-09-30](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-vwvw-rp3m-rm37)).

BleepingComputer reports Kiteworks fixed 126 vulnerabilities in the same cycle and that Shadowserver tracks nearly 400 internet-exposed Kiteworks instances, with no patch-state information ([BleepingComputer, 2026-10-01](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)). No advisory states exploitation, and no source ties any of these flaws to the one Kiteworks found during the shutdown, which BleepingComputer says Kiteworks still has not detailed or assigned a CVE ([BleepingComputer, 2026-10-01](https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/)).
