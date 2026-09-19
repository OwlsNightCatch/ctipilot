---
schema: 1
kind: threat
title: "Medusa's joint advisory update puts a number on the patch race: affiliates weaponise newly announced flaws within 24 hours, and the agencies find no sign the group develops any of them itself"
headline: "A ransomware crew that develops no zero-days still beats the patch window, on exploits it obtains from sources the agencies cannot identify"
summary: >
  CISA, the FBI and — newly — HHS updated the joint #StopRansomware advisory on Medusa on 2026-08-18 with
  FBI investigative data through April 2026, raising the recorded victim count from more than 300 to more
  than 500; the only sector list any cited outlet publishes covers medical, education, legal, insurance and
  manufacturing. The operationally
  useful part is the tempo claim: the agencies state Medusa actors exploit newly announced flaws within 24
  hours and have been seen using exploits up to a week before public disclosure, while explicitly assessing
  that the group develops no zero-day or N-day vulnerabilities of its own, obtaining advanced access to
  exploits from sources the agencies could not identify or else moving fast on public disclosures. Separately
  from that, initial-access brokers who sell entry into victim networks are paid from $100 to $1 million, with
  a premium for exclusivity. The advisory also names the remote-management tooling affiliates use post-compromise. The
  group has added no new leak-site victims since April.
discovered_at: "2026-08-19T05:20:00Z"
event_date: "2026-08-18"
run_id: 2026-08-19T0410Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, data-breach, vulnerabilities]
regions: [global, us, europe]
sectors: [healthcare, education, legal-services, finance, manufacturing]
entities: [malware:medusa]
techniques: [T1190, T1078, T1219, T1021.001, T1486]
affected_products: []
cves: []
sources:
  - url: "https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa"
    publisher: "The Record / Recorded Future News"
    date: "2026-08-18"
    role: primary
  - url: "https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/"
    publisher: "CyberScoop"
    date: "2026-08-18"
    role: corroborating
  - url: "https://healthsystemcio.com/2026/08/18/medusa-ransomware-advisory-hhs/"
    publisher: "healthsystemCIO"
    date: "2026-08-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "been observed to use exploits up to a week before public vulnerability disclosure"
    publisher: "The Record / Recorded Future News"
  - quote: "However, there is no indication Medusa actors develop their own zero-day or N-day vulnerabilities, preferring instead to obtain advanced access to exploits from unknown sources or to quickly leverage newly announced exploits before potential victims can mitigate vulnerabilities through patching"
    publisher: "The Record / Recorded Future News"
  - quote: "The FBI said Medusa actors used remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp and Splashtop."
    publisher: "The Record / Recorded Future News"
  - quote: "the victim tally in the advisory jumped from more than 300 to more than 500"
    publisher: "CyberScoop"
  - quote: "Medusa has not added any new victims to its leak site since April"
    publisher: "The Record / Recorded Future News"
verification: multi-source
sourcing_note: >
  The advisory itself is the primary and could not be read: cisa.gov refused every available transport this
  run (HTTP 403 direct, the reader proxy credit-exhausted, and the archive host unreachable), so this entry
  rests on two editorially independent journalists who each read and quoted the advisory directly — Tim
  Starks at CyberScoop and Jonathan Greig at The Record — checked against each other and confirmed not to
  be cross-citing, with healthsystemCIO independently carrying the HHS co-sealer detail. Every quoted
  passage here is reproduced as the outlet printed it, including where the outlet quotes the advisory
  inside its own sentence; nothing is spliced across the two. Because the primary was unreachable, the
  confidence is high on the substance the two independent reads agree on and no claim is made about advisory
  content neither outlet reported. The two historically exploited products named below are given as the
  outlets name them, without identifiers, because this entry is about the advisory rather than about those
  flaws.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

CISA, the FBI and the Department of Health and Human Services published an update to the joint #StopRansomware advisory on Medusa on 2026-08-18, folding in FBI investigative findings through April 2026. The headline number is cumulative rather than current: CyberScoop records that "the victim tally in the advisory jumped from more than 300 to more than 500" ([CyberScoop, 2026-08-18](https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/)) since the original March 2025 advisory — roughly two hundred additional organisations identified over the intervening year. On sectors, the only list any of the cited outlets publishes is healthsystemCIO's, which records the figure as spanning every sector the agencies track, including medical, education, legal, insurance and manufacturing. HHS joined as a co-sealer specifically to add the healthcare perspective, describing the Healthcare and Public Health Sector as a frequent victim of Medusa activity ([healthsystemCIO, 2026-08-18](https://healthsystemcio.com/2026/08/18/medusa-ransomware-advisory-hhs/)).

The finding worth carrying into planning is about speed, and it is unusual in being paired with an explicit negative. The agencies state the group exploits "newly announced exploits within 24 hours" and has "been observed to use exploits up to a week before public vulnerability disclosure" — and then rule out the obvious inference: "However, there is no indication Medusa actors develop their own zero-day or N-day vulnerabilities, preferring instead to obtain advanced access to exploits from unknown sources or to quickly leverage newly announced exploits before potential victims can mitigate vulnerabilities through patching" ([The Record, 2026-08-18](https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa)). That combination is the planning fact. An organisation cannot out-wait this actor by assuming a research lead time the group has to fund itself: the pre-disclosure window comes from exploit access obtained somewhere the agencies could not identify, and the 24-hour window comes from acting on the same public advisory the defender is reading. A patch cycle measured in weeks is not a control against it, and the compensating control is exposure reduction on internet-facing software rather than faster patching alone.

The economics of *entry* are spelled out separately, and are not the same market as the exploit access above — these payments buy a way into a victim network, not a vulnerability. The gang relies on access brokers, "compensating them anywhere from $100 to $1 million, with higher prices going to those who work exclusively with Medusa", while most brokers work simultaneously for multiple ransomware variants ([CyberScoop, 2026-08-18](https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/)); The Record records the same exclusivity premium, noting Medusa "recruits members on cybercriminal forums and offers up to $1 million to initial access brokers who want to work exclusively for the group" ([The Record, 2026-08-18](https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa)). The practical consequence of brokers serving several operations at once is that an access sold into this ecosystem is not tied to one outcome — the same foothold may surface under a different brand.

Post-compromise, the advisory names the tooling rather than bespoke malware. Affiliates deploy credential-stealing tools first, then move to legitimate remote-management software to evade detection: "The FBI said Medusa actors used remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp and Splashtop" ([The Record, 2026-08-18](https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa)), with Remote Desktop Protocol for lateral movement ([CyberScoop, 2026-08-18](https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/)). Two products from the group's historically exploited list are named, each by a different outlet: CyberScoop records the advisory covering flaws in Fortra's GoAnywhere and BeyondTrust ([CyberScoop, 2026-08-18](https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/)), while healthsystemCIO is the outlet that identifies the February 2026 BeyondTrust disclosure as the advisory's own worked example of how quickly a public disclosure becomes an intrusion ([healthsystemCIO, 2026-08-18](https://healthsystemcio.com/2026/08/18/medusa-ransomware-advisory-hhs/)).

One honest caveat belongs next to the victim count: The Record reports that "Medusa has not added any new victims to its leak site since April", with several experts attributing the pause to law-enforcement attention drawn by an attack on a US medical centre ([The Record, 2026-08-18](https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa)). The 500-plus figure is therefore a record of what happened through April, not evidence of a wave in progress — the advisory's value here is the tradecraft and the tempo, not a current-activity signal.

**Defender takeaway:** treat the remote-management tool list as an inventory question rather than a blocklist. Every product named is legitimate software that some estates run deliberately, so the useful control is knowing which one is sanctioned and alerting on the appearance of any other. **Triage:** a sanctioned remote-support tool generates the same process, service-installation and outbound-session telemetry as an attacker-installed one, so the tool's identity does not discriminate — what does is whether a second, unsanctioned remote-management agent appears on a host that already has the approved one, whether its installation correlates with an administrative logon from an unusual source, and whether its outbound sessions run outside the support team's working pattern. The advisory's extortion detail is worth knowing for incident handling rather than detection: victims are offered a fee to delay leak-site publication by a day, and the FBI records a case in which a second Medusa-affiliated actor approached a victim that had already paid, claiming the original negotiator stole the ransom and demanding half again for the "true decryptor" — which the agencies read as either a triple-extortion scheme or internal dysfunction ([The Record, 2026-08-18](https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa)). Either reading argues against treating payment as a route to a predictable outcome.
