---
schema: 1
kind: threat
horizon: operational
title: "Correction — Unit 42's autonomous-agent campaign confirmed command execution on 11 Marimo notebook endpoints as well as three NetScaler exfiltrations"
headline: "The confirmed-impact count in the 2026-07-31 entry came from a quote Unit 42 never wrote — Marimo Notebook CVE-2026-39987 belongs on the exposure list"
summary: >
  This pipeline's 2026-07-31 entry on Unit 42's autonomous-AI intrusion campaign framed the operation
  as landing three confirmed compromises, all from the operator's manual NetScaler work, and supported
  it with an evidence quote attributed to Unit 42 that does not appear in Unit 42's post. The real
  sentence records data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) AND command
  execution on 11 Marimo notebook endpoints (CVE-2026-39987), and Unit 42's own CVE table lists
  CVE-2026-39987 with command execution confirmed. Two further CVEs
  carry confirmed attempts: reverse shells against nine Apache Tomcat servers (CVE-2026-34486) and
  callbacks from three IKE VPN endpoints (CVE-2026-33824). The operational consequence is an exposure
  list four CVEs long rather than one, with Marimo Notebook the addition most likely to be missing
  from an asset inventory.
discovered_at: "2026-08-02T14:05:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T1309Z-audit
priority: high
immediate_action: null
tags: [ai-abuse, vulnerabilities, actively-exploited, rce, pre-auth]
regions: [global, europe]
sectors: [public-sector, technology]
entities: [actor:knaithe-knyuan, tool:hermes-ai-agent]
techniques: [T1190, T1059]
affected_products: ["Marimo Notebook", "Citrix NetScaler ADC", "Apache Tomcat"]
cves:
  - id: CVE-2026-39987
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "marimo prior to 0.23.0 — the terminal WebSocket endpoint /terminal/ws performs no authentication validation, so an unauthenticated attacker obtains a full PTY shell (CWE-306), per the CVE record that owns the identifier. Unit 42 states no version boundary in its post; the boundary and the CVSS 4.0 vector AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H come from the owning record, not from Unit 42's table."
    fixed: "marimo 0.23.0. The flaw was published 2026-04-09 and is CISA KEV-listed; this pipeline covered it on 2026-05-30. The patch has been available for months, which is what makes the exposure question here a compromise-assessment question rather than a discovery of something new to install."
sources:
  - url: "https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/"
    publisher: "Unit 42"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "Across all the exploitation attempts, both autonomous and manual, Unit 42 confirmed data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) and command execution on 11 Marimo notebook endpoints (CVE-2026-39987)."
    publisher: "Unit 42"
verification: single-source
sourcing_note: "Single-source and deliberately so: the correction is a re-reading of the same Unit 42 post the original entry cited, re-fetched in full by this audit, so Unit 42 is the authority for its own confirmed-impact counts and for its own CVE table. Both evidence quotes were confirmed as contiguous substrings of the fetched page. Only CVE-2026-39987 enters cves[] — the NetScaler CVE is already carried by the original entry, and the Tomcat and IKE VPN ids are recorded by Unit 42 as attempts rather than confirmed compromises, so they are named in the body without a cves[] record. Credibility 2: one assessing party."
confidence: high
update_of: 2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Confirm every marimo notebook instance is on 0.23.0 or later and that none answers from outside the development network — then, separately, compromise-assess any instance that was exposed while below 0.23.0, because Unit 42 records command execution as confirmed on 11 endpoints in this campaign rather than merely attempted, and the patch does not evict an attacker who already had a PTY shell."
migrated_from: null
---

**UPDATE (originally covered 2026-07-31):** the original entry understated the campaign's confirmed impact, and it did so on the strength of a quotation Unit 42 did not write. This pipeline's own weekly quality audit caught it by checking the entry's `evidence[]` against the fetched page.

The original entry carried, inside quotation marks and attributed to Unit 42, a sentence reading "Across all the exploitation attempts, both autonomous and manual, Unit 42 was only able to confirm three targets were successfully exploited." Unit 42's actual sentence, at the same point in the post, is "Across all the exploitation attempts, both autonomous and manual, Unit 42 confirmed data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) and command execution on 11 Marimo notebook endpoints (CVE-2026-39987)" ([Unit 42, 2026-07-30](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)). The fabricated version dropped the second half of the finding and added a limiting phrase — "was only able to confirm" — that carries an editorial judgement the source does not make.

Unit 42's own CVE table is unambiguous on the omitted half: its row for CVE-2026-39987 gives the product as Marimo Notebook, the score as 9.8, the exploitation method as manual, and the status as active exploitation with command execution confirmed. The post's confirmed-impact list runs to four entries rather than one: data exfiltration from three organisations via the Citrix NetScaler flaw, command execution on 11 Marimo notebook instances, Java deserialization reverse-shell attempts against nine Apache Tomcat servers (CVE-2026-34486), and reverse-shell callbacks targeting three IKE VPN endpoints (CVE-2026-33824). Unit 42 also notes it "reviewed evidence of batch exploitation against an unknown number of hosts that were listed in a file deleted by the actor prior to our analysis", so even the enumerated figures are a floor rather than a total.

What survives from the original entry is its central reading of the autonomy question: Unit 42 attributes the confirmed compromises to the operator's manual work, and its table records the manual method against each of the four CVEs above, so the autonomous scanning component still did not itself produce the confirmed intrusions. What does not survive is the impact framing. A reader who took "three confirmed compromises, all NetScaler" from the original entry built the wrong exposure list, and the missing item is the awkward one: Marimo is an open-source reactive Python notebook that data-science and research teams install themselves, so it is far more likely to be absent from a central asset inventory than a NetScaler appliance is.

**Defender takeaway:** re-run the exposure question against four products rather than one. NetScaler and Tomcat will be in the asset register; Marimo Notebook and self-managed IKE VPN endpoints frequently will not, and a notebook server is exactly the class of asset a research or analytics group stands up outside the change process. For marimo specifically the patch is old news — 0.23.0 shipped in April, the flaw is CISA KEV-listed, and this pipeline covered it on 2026-05-30 — so the actionable half is not "patch it" but "find it, then check it": an instance still below 0.23.0 four months on is likely one nobody owns, and command execution confirmed on 11 endpoints means an exposed one should be treated as a compromise-assessment target, worked from the notebook host's process ancestry and outbound connections rather than from a version number.

**Triage:** the discriminator for a notebook server is lineage rather than the process itself. A Marimo host legitimately spawns Python child processes constantly — that is what a notebook does — so process creation under the notebook service is noise. What is not noise is a child process that is not the interpreter: a shell, a download utility, or a scheduling command spawned by the notebook service account, especially on a host where no interactive session was open at that timestamp. Outbound connections from a notebook server to destinations outside the package-registry and data-source set it normally reaches are the second signal, and the two together — a non-interpreter child plus an unfamiliar egress destination within the same minute — are worth an alert on a host that was internet-reachable during the campaign window.
