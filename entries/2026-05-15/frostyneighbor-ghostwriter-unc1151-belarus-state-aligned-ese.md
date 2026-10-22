---
schema: 1
kind: threat
title: "FrostyNeighbor (Ghostwriter, UNC1151): since March 2026, geofenced PDF lures deliver a JavaScript PicassoLoader and Cobalt Strike to Ukrainian government organisations"
headline: "Belarus-aligned FrostyNeighbor hits Ukrainian government bodies with geofenced PDF lures and Cobalt Strike"
summary: "ESET reported on 2026-05-14 new activity since March 2026 by FrostyNeighbor (Ghostwriter, UNC1151), a cyberespionage group apparently aligned with Belarus, against governmental organisations in Ukraine: spearphishing PDFs impersonating Ukrtelecom link to a server that returns a benign PDF outside Ukraine and a RAR archive with a JavaScript dropper to Ukrainian IP addresses. The JavaScript PicassoLoader it installs reports a host fingerprint every 10 minutes, and the operators very likely decide manually whether to send a dropper that runs a Cobalt Strike beacon through a renamed copy of rundll32 with Run-key persistence."
discovered_at: "2026-05-15T05:00:02Z"
event_date: 2026-05-14
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - phishing
regions:
  - europe
sectors:
  - public-sector
entities:
  - "campaign:frostyneighbor-2026-05-campaign"
  - "actor:frostyneighbor"
techniques: [T1566.001, T1204.002, T1059.007, T1027, T1140, T1053.005, T1082, T1057, T1071.001, T1105, T1036.003, T1218.011, T1547.001]
affected_products: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
    publisher: "ESET"
    date: "2026-05-14"
    role: primary
  - url: "https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html"
    publisher: "The Hacker News"
    date: "2026-05-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Since March 2026, we have detected new activities that we attributed to FrostyNeighbor, using links in malicious PDFs sent via spearphishing attachments to target governmental organizations in Ukraine."
    publisher: ESET
    source_url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
  - quote: "The decision whether or not to deliver a payload is very likely manually performed by the operators, based on the collected information to decide if the victim is of interest."
    publisher: ESET
    source_url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
  - quote: "The payload is only delivered after server-side victim validation, combining automated checks of the requesting user agent and IP address with the manual validation by the operators."
    publisher: ESET
    source_url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
verification: multi-source
sourcing_note: "ESET's research from its own telemetry is the only analysis; The Hacker News reports it."
confidence: high
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
migrated_from: briefs/2026-05-15.md
updated_at: null
updates:
  - at: "2026-10-21T20:36:01Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      ESET's new FrostyNeighbor activity since March 2026 targets governmental organisations in Ukraine;
      the industrial, healthcare, pharmaceutical and logistics victims in Poland and Lithuania are ESET's
      description of the group's broader historical victimology, not targets of this campaign wave. The
      chain also includes scheduled-task persistence for the JavaScript PicassoLoader and a Cobalt Strike
      beacon run by a renamed copy of rundll32 from an HKCU Run-key LNK.
    fields: [affected_products, body, classification, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title, entities]
---

ESET attributes new activity since March 2026 to FrostyNeighbor, also known as Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA or Storm-0257, a long-running cyberespionage group apparently aligned with the interests of Belarus, using links in spearphishing PDFs to target governmental organisations in Ukraine ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)). In ESET's telemetry the group's Ukrainian targeting focuses on military, defence and government, while its victimology in Poland and Lithuania is broader, spanning industry and manufacturing, healthcare and pharmaceuticals, logistics and many governmental organisations ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)).

The lure is a blurred PDF impersonating Ukrtelecom whose download button leads to the group's delivery server; visitors outside Ukraine receive a benign PDF of the same name, while Ukrainian IP addresses receive a RAR archive holding a JavaScript first stage that shows a decoy, re-runs itself, drops a base64-embedded JavaScript PicassoLoader and builds a scheduled task from an XML template the C2 serves as a fake JPG ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)). PicassoLoader collects the username, computer name, OS version, boot time, current time and running processes, posts them over HTTPS every 10 minutes and evaluates any response longer than 100 bytes ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)). Operators very likely decide by hand whether the victim is of interest; if so, the C2 returns a third-stage dropper that copies `rundll32.exe` into `%ProgramData%` under another name, writes the base64-decoded Cobalt Strike beacon DLL beside it, and registers in the HKCU Run key a LNK that starts the copied `rundll32` with the DLL's export ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)).

**Exposure:** governmental organisations in Ukraine are the targets of this chain; the payload is delivered only after server-side checks of the user agent and IP address and a manual operator decision, so a request from outside Ukraine sees only the benign PDF ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)).

**Detection:** in process telemetry, a JavaScript file from a RAR archive that relaunches itself, followed by scheduled-task creation from a downloaded XML template; in network telemetry, a script process posting to the same HTTPS endpoint every 10 minutes; in persistence telemetry, an HKCU Run entry pointing at a LNK in `%ProgramData%` that starts a renamed copy of `rundll32.exe` loading a DLL from the same directory ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)).

**Triage:** `rundll32.exe` is a normal Windows binary when it runs from the system directory; a copy of it under a different name in `%ProgramData%`, which ESET says is very likely meant to bypass detection rules, is the signal ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)).

**Defender takeaway:** because delivery is geofenced and operator-gated, a clean verdict on an Ukrtelecom-themed lure link from a sandbox outside Ukraine proves nothing; hunt on the host artefacts above instead ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)). The Hacker News reports the same chain ([The Hacker News, 2026-05-14](https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html)).

## Correction — 2026-10-21T20:36:01Z

The activity ESET documents since March 2026 targets governmental organisations in Ukraine ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)); the industrial, healthcare and pharmaceutical, logistics and governmental victims in Poland and Lithuania come from ESET's introduction to the group's broader victimology, not from this campaign wave. The chain also persists: the first stage builds a scheduled task from a downloaded XML template to run PicassoLoader, and the Cobalt Strike stage copies `rundll32.exe` into `%ProgramData%` under another name and starts it from a LNK registered in the HKCU Run key ([ESET, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)), which gives defenders host artefacts to hunt where geofencing hides the network side.
