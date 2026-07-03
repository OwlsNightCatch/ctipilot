---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Akira ransomware on Groupe 3R — 20 Swiss medical-imaging centres across seven cantons; second cyberattack on the same operator within twelve months"
headline: "Akira ransomware on Groupe 3R — 20 Swiss medical-imaging centres across seven cantons; second cyberattack on the same operator within twelve months"
summary: "Groupe 3R (Réseau Radiologique Romand) — Akira leak-site listing claims 48 GB; ~20 imaging centres across seven Swiss cantons (Vaud, Valais, Fribourg, Genève, Neuchâtel, Berne, and Zürich) — six in Romandie plus Zürich; second cyberattack on the same Swiss operator within twelve months. Victim disclosed publicly 2026-04-30, notified BACS/OFCS, filed criminal complaint, will not pay ransom; legacy examination data still inaccessible. (Groupe 3R victim statement · ICTjournal.ch · daily 2026-05-10)"
discovered_at: "2026-05-04T05:00:05Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
regions:
  - switzerland
sectors:
  - healthcare
entities:
  - "incident:groupe-3r-akira-2026"
  - "actor:akira"
cves: []
sources:
  - url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
    publisher: Groupe 3R victim statement
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes"
    publisher: ICTjournal.ch
    role: corroborating
  - url: "https://www.blick.ch/fr/suisse/romande/cyberattaque-le-groupe-romand-3r-de-radiologie-cible-id21930477.html"
    publisher: Blick.ch
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

**If you did nothing this week:** Swiss and DACH healthcare operators with internet-exposed Cisco ASA / FTD, Fortinet SSL-VPN, or VMware ESXi management interfaces — Akira's documented edge-device initial-access targets — face the same playbook used here. Groupe 3R confirmed the attack on its own website 2026-04-30, filed a criminal complaint, notified the Federal Office for Cybersecurity (BACS/OFCS), and explicitly stated it will not pay ransom; Akira's leak-site listing on approximately 2026-05-08 claims 48 GB exfiltrated including employee identity documents, patient records, payment information, and signed NDAs ([Groupe 3R victim statement, 2026-04-30](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/) · [ICTjournal.ch, 2026-05-06](https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes) · [Blick.ch, 2026-05-07](https://www.blick.ch/fr/suisse/romande/cyberattaque-le-groupe-romand-3r-de-radiologie-cible-id21930477.html) · [daily 2026-05-10](/briefs/2026-05-10/)).

Groupe 3R (Réseau Radiologique Romand) operates ~20 medical-imaging centres across seven Swiss cantons listed in the operator statement (Vaud, Valais, Fribourg, Genève, Neuchâtel, Berne — six in Romandie — plus Zürich in German-speaking Switzerland) — a direct Swiss critical-health-infrastructure incident, and the operator's second cyberattack within twelve months (the prior April 2025 incident is acknowledged in the operator's own statement as having involved different attackers and methodology). Legacy examination data remains inaccessible at week-end; new examination data security has been restored on rebuilt infrastructure. Data-exfiltration was not confirmed by the victim; Akira's leak-site post asserts 48 GB exfiltrated. Akira's documented playbook against European healthcare and SME targets emphasises edge-device initial access (Cisco ASA/FTD CVEs, Fortinet SSL-VPN CVEs, VMware ESXi authenticated RCE) and intermittent file-encryption to evade EDR file-IO heuristics — observed ATT&CK techniques include [T1190](https://attack.mitre.org/techniques/T1190/), [T1133 External Remote Services](https://attack.mitre.org/techniques/T1133/), [T1486 Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/), and [T1567 Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/). Defenders should re-validate patch state on the edge devices in Akira's standard target list, confirm EDR rules trigger on intermittent-encryption write-skip-write file-IO patterns, and verify radiology-modality VLAN segmentation from corporate Active Directory — PACS/RIS environments tend to co-tenant with Windows file shares, providing trivial east-west reach once an attacker lands. The Akira-as-actor attribution comes from `ransomware.live` (aggregator), not from the victim or an independent primary; logged with confidence HIGH on incident, MEDIUM on actor.
