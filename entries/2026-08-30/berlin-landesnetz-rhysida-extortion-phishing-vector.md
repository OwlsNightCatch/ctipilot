---
schema: 1
kind: incident
title: "Berlin's state government confirms an extortion attempt after a phishing click opens the shared Landesnetz; media reporting names Rhysida"
headline: "Berlin confirms extortion after a phishing click reaches the shared state network; media reports name Rhysida"
summary: >
  Germany's Berlin state administration confirmed on 2026-08-28 that it faces an active
  extortion attempt following a compromise of its shared Landesnetz government network first
  disclosed on 2026-08-17; media reporting attributes the attack to the ransomware group
  Rhysida, which separately claimed it on its own leak site. Investigative reporting states
  an employee's phishing-email click opened the network to attackers who exfiltrated 5.7 to
  5.8 terabytes of data, including critical-infrastructure and emergency-planning material,
  before detection; Berlin's government has publicly refused the roughly EUR 2 million ransom
  demand.
discovered_at: "2026-08-30T04:35:00Z"
updated_at: null
event_date: "2026-08-28"
run_id: 2026-08-30T0410Z-intel
priority: high
immediate_action: null
tags: [ransomware, data-breach, phishing, organized-crime]
regions: [dach]
sectors: [public-sector]
entities: ["incident:berlin-landesnetz-compromise-2026-08", "actor:rhysida"]
techniques: [T1566, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html"
    publisher: "Der Tagesspiegel"
    date: "2026-08-28"
    role: primary
  - url: "https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html"
    publisher: "heise online"
    date: "2026-08-29"
    role: primary
  - url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
    publisher: "Security Affairs"
    date: "2026-08-29"
    role: corroborating
  - url: "https://www.berliner-zeitung.de/article/cyberangriff-auf-berliner-senat-wegner-bestaetigt-erpressungsversuch-10337926"
    publisher: "Berliner Zeitung"
    date: "2026-08-28"
    role: corroborating
  - url: "https://www.rbb24.de/politik/beitrag/2026/08/berlin-hackerangriff-landesnetz-loesegeld-forderung-erpresser.html"
    publisher: "rbb24 (Rundfunk Berlin-Brandenburg)"
    date: "2026-08-29"
    role: corroborating
  - url: "https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/"
    publisher: "BornCity"
    date: "2026-08-29"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a"
    publisher: "CISA / FBI / Multi-State ISAC"
    date: "2025-04-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attackers apparently gained access to the Landesnetz through an employee's click on a phishing email."
    original: "Zugang zum Landesnetz verschafften sich die Täter offenbar durch den Klick eines Mitarbeiters auf eine Phishing-Mail."
    publisher: "Der Tagesspiegel"
    source_url: "https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html"
  - quote: "“The state of Berlin will not submit to extortion,” Berlin Mayor Kai Wegner and Berlin's interior senator, Iris Spranger, said in a joint statement on Friday, before the ransomware group claimed the attack on their Tor data leak site."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
  - quote: "The ransomware group Rhysida claimed responsibility on its leak site August 28, posting an entry titled simply “Berlin, Germany” and claiming 5.79 terabytes of data across roughly 1.44 million files, with personal information on 12,076 individuals allegedly included."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
  - quote: "Experts identified the ransomware Rhysida as the tool with which the systems were encrypted and the data stolen."
    original: "Experten identifizierten die Ransomware Rhysida als das Werkzeug, mit dem die Systeme verschlüsselt und die Daten entwendet wurden."
    publisher: "BornCity"
    source_url: "https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/"
verification: multi-source
sourcing_note: >
  The phishing access vector and the Rhysida attribution are both sourced to investigative
  journalism (Der Tagesspiegel, Der Spiegel via heise online), not an official BSI or Senate
  technical disclosure; Berlin's Senate administration has explicitly declined to name the
  attacker, citing investigative-tactical reasons. Whether the affected systems were also
  encrypted, not only exfiltrated, is disputed: BornCity attributes an encryption claim to
  unnamed "experts", while every other cited source describes only data theft and extortion.
  Security Affairs states Berlin first disclosed the compromise on 2026-08-17; Berliner
  Zeitung, Der Tagesspiegel and rbb24 all independently state the compromise became public
  and the affected departments were disconnected on 2026-08-14. This entry follows the
  three-source consensus date.
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
updates: []
migrated_from: null
---

Germany's Berlin state administration is the target of a live extortion attempt following a compromise of its Landesnetz, the shared network serving every Senate department and state agency; the attack became public knowledge on 2026-08-14 (translated from German) ([Berliner Zeitung, 2026-08-28](https://www.berliner-zeitung.de/article/cyberangriff-auf-berliner-senat-wegner-bestaetigt-erpressungsversuch-10337926)), the same day the two affected departments were disconnected from the network as a containment measure ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Investigative reporting, not an official technical disclosure, is the first to name a mechanism: the attackers apparently gained access to the Landesnetz through an employee's click on a phishing email (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Forensic investigators found the actual data exfiltration ran between 2026-08-07 and 2026-08-12 ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)), several days before the two affected departments were disconnected.

Der Spiegel reported, citing security-industry sources, that the ransomware group Rhysida is behind the attack ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), an attribution Berlin's Senate administration has declined to confirm, citing investigative-tactical reasons ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)). Rhysida's own dark-web leak site independently posted an entry titled "Berlin, Germany" on 2026-08-28 claiming 5.79 terabytes of data across roughly 1.44 million files, including personal data on 12,076 individuals, more than 5,000 personnel files, plaintext credentials for internal systems, disciplinary and court records, Bundesrat committee protocols, and vulnerability analyses concerning Berlin's water supply ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Rhysida demanded 30 Bitcoin, about EUR 2 million (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), with a one-week ultimatum running from 2026-08-28 (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)); Berlin's Governing Mayor Kai Wegner and Interior Senator Iris Spranger jointly confirmed the extortion attempt and publicly refused to pay, stating the state of Berlin will not submit to extortion ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Whether the affected systems were also encrypted, not only exfiltrated, is disputed: one outlet attributes to unnamed "experts" the claim that the Rhysida ransomware was the tool used to both encrypt the systems and steal the data (translated from German) ([BornCity, 2026-08-29](https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/)), while every other cited source describes only data theft and extortion without confirming encryption; this entry does not assert that encryption occurred.

CrowdStrike is conducting a forensic investigation across every Senate department and state agency network-wide, an effort Tagesspiegel's sources expect to take several more days ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). The department networks disconnected on 2026-08-14 were reconnected on 2026-08-23, but staff report continuing operational degradation days later, with many now working over private internet connections because the corporate network remains impaired; the same reporting flags that workaround as a new, self-inflicted security exposure ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Rhysida has run this extortion pattern against public-sector targets before, including an earlier 2026 claim against the city of Stuttgart (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)); per the joint CISA/FBI/Multi-State ISAC advisory on the group, current as of its 2025-04-30 update, its initial-access techniques include compromising internal VPN access points using valid credentials at organizations lacking multi-factor authentication, and separately deploying Gootloader malware ([CISA, 2025-04-30](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a)).

**Defender takeaway:** the exposure pattern here, a single employee's phishing click reaching a shared administrative network broad enough to threaten a different department's critical-infrastructure and judiciary holdings, is directly transferable to any DACH shared-network government architecture, including Swiss cantonal and federal administrative networks: segment administrative domains so that one credential or endpoint compromise cannot reach unrelated departments' sensitive holdings, and verify that phishing-resistant multi-factor authentication and out-of-band verification cover every remote-access and VPN path that Rhysida's documented playbook targets.

**Triage:** the confirmed mechanism, a user-driven phishing-email click followed by multi-day bulk data exfiltration, surfaces at the point of delivery in mail-flow and attachment-sandboxing logs, and in network-egress and data-loss-prevention telemetry as a sustained high-volume outbound transfer from a single department's network segment; neither cited source states what executed after the click, so no process-level discriminator is offered here.
