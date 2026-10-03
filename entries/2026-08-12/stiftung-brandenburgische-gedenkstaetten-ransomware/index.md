---
schema: 1
kind: incident
title: "A German federal- and state-funded memorial foundation is rebuilding its entire IT from scratch after ransomware — all seven sites offline, data assumed exfiltrated, no actor named"
headline: "Stiftung Brandenburgische Gedenkstätten confirms encryption across every site and chooses full reconstruction over restoring from backup"
summary: >
  The Stiftung Brandenburgische Gedenkstätten, the German public-law foundation operating seven
  memorial sites including Sachsenhausen and Ravensbrück, disclosed on 2026-08-11 that ransomware
  detected on 5 August encrypted parts of its IT systems and data, and that it must currently assume
  attackers downloaded data first. All seven locations and the central office are affected. The
  foundation cut all internet and network connections and is rebuilding its IT from scratch rather
  than restoring from backups, working with a BSI-recommended incident-response provider. No actor,
  ransomware family, leak-site listing or initial-access vector has been disclosed by any party.
discovered_at: "2026-08-12T04:49:00Z"
event_date: "2026-08-05"
run_id: 2026-08-12T0411Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [dach, europe]
sectors: [public-sector, education]
entities:
  - incident:stiftung-brandenburgische-gedenkstaetten-ransomware-2026-08
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.stiftung-bg.de/presse/presseinformationen/42-26-die-stiftung-wurde-opfer-eines-ransomware-angriffs/"
    publisher: "Stiftung Brandenburgische Gedenkstätten"
    date: "2026-08-11"
    role: primary
  - url: "https://www.heise.de/news/Brandenburg-Cyberangriff-legt-IT-System-der-Gedenkstaetten-lahm-11410695.html"
    publisher: "heise online"
    date: "2026-08-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Die Stiftung Brandenburgische Gedenkstätten ist Opfer eines sogenannten Ransomware-Angriffs geworden."
    publisher: "Stiftung Brandenburgische Gedenkstätten"
  - quote: "Nach aktuellem Stand muss davon ausgegangen werden, dass Daten von den Angreifern heruntergeladen wurden."
    publisher: "Stiftung Brandenburgische Gedenkstätten"
verification: multi-source
sourcing_note: >
  The victim's own press release (Nr. 42/2026) is the primary; heise online corroborates
  independently. Both are German-language and are quoted here in the original with an English gloss
  in the body. No source names an actor, a ransomware family or an initial-access vector, and no
  leak-site listing had appeared as of this run.
confidence: high
update_of: null
references: []
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

The Stiftung Brandenburgische Gedenkstätten — a public-law foundation funded by the Brandenburg state ministry for science and culture and by the federal government's commissioner for culture and media, operating seven memorial sites including the former Sachsenhausen and Ravensbrück concentration camps — published press release Nr. 42/2026 on 2026-08-11 stating that it "ist Opfer eines sogenannten Ransomware-Angriffs geworden" ("has become the victim of a so-called ransomware attack") ([Stiftung Brandenburgische Gedenkstätten, 2026-08-11](https://www.stiftung-bg.de/presse/presseinformationen/42-26-die-stiftung-wurde-opfer-eines-ransomware-angriffs/)). The attack was detected on 5 August; attackers reached the internal IT systems, encrypted parts of the systems and data with dedicated software, and left a ransom note demanding payment for decryption. The foundation states that "Nach aktuellem Stand muss davon ausgegangen werden, dass Daten von den Angreifern heruntergeladen wurden" — on current assessment it must be assumed that data was downloaded by the attackers before encryption. Its director describes the entire IT system as currently non-functional. heise online corroborates the disclosure independently ([heise online, 2026-08-11](https://www.heise.de/news/Brandenburg-Cyberangriff-legt-IT-System-der-Gedenkstaetten-lahm-11410695.html)).

All seven memorial-site locations and the central business office are affected. The foundation's IT department disconnected every internet and network connection immediately, and the foundation reported the incident to the Zentrale Ansprechstelle Cybercrime at the Brandenburg state police and filed a breach notification with the Brandenburg data-protection authority within the statutory window. Physical visits to the memorials continue; booking delays for educational programmes are expected. No source names a threat actor or ransomware family, no leak-site listing had surfaced as of this run, and neither the foundation nor heise states how the attackers got in.

The transferable part is the recovery decision, not the victim. The foundation is rebuilding its IT systems from scratch rather than restoring from backups, explicitly to deny the attacker a route back in, and is doing so with an external incident-response provider recommended by the BSI ([Stiftung Brandenburgische Gedenkstätten, 2026-08-11](https://www.stiftung-bg.de/presse/presseinformationen/42-26-die-stiftung-wurde-opfer-eines-ransomware-angriffs/)). The foundation expects the systems to be available again in a few days ("in einigen Tagen"), with delays to educational-programme bookings until then. For a small public body the rebuild is still the more expensive of the two options — it trades a longer outage for the certainty that restored infrastructure is not carrying the intruder's persistence — and it is the correct default when data theft is assumed and the dwell time is unknown, because a backup taken during an undetected intrusion restores the foothold along with the files.

**Defender takeaway:** this is the fourth European public-sector body in nine days to disclose a compromise of its own operating infrastructure rather than a customer dataset, and the pattern for small, federated cultural and educational institutions is consistent: a lean IT function, one shared estate spanning many physically separate sites, and no capacity to run a parallel forensic and restoration effort. Where an organisation of that shape is in scope for a SOC, the useful preparation is the decision itself — knowing in advance whether the answer to a domain-wide encryption event is restore-and-monitor or rebuild-and-reissue, and having the identity infrastructure documented well enough that the second option is achievable inside an acceptable outage.

**Triage:** with no actor, family or vector disclosed, there is nothing here to match an alert against — the entry is a sector-pattern and recovery-posture record, and any attempt to bind it to a specific intrusion set would be invention.
