---
schema: 1
kind: threat
title: "MythicRatatoskr: ESET documents a Go backdoor that hides its command server inside the Yggdrasil mesh network, and a UAC-0099 to Sandworm access handoff that ended in a Group Policy wiper attack on a Ukrainian grain logistics firm"
headline: "ESET: a backdoor reaches its C2 through the Yggdrasil mesh; Sandworm wiped the victim two months after UAC-0099 got in"
summary: >
  ESET reports that UAC-0099 gained access to a Ukrainian grain logistics company on 2025-07-16 with a spearphishing attachment and a day
  later deployed MythicRatatoskr, a Go backdoor whose command server sits inside the Yggdrasil mesh network, reached through public
  peers; on 2025-09-17 the SDelete utility was deployed through Group Policy, which ESET assesses with high confidence as Sandworm
  after UAC-0099 handed off the access. ESET names blocking the public peer addresses as a viable mitigation.
discovered_at: "2026-10-23T03:40:00Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, wiper, russia-nexus]
regions: [russia-cis]
sectors: [transport]
entities: ["actor:uac-0099", "actor:sandworm", "malware:mythicratatoskr"]
techniques: [T1566.001, T1053.005, T1059.001, T1543.003, T1071.001, T1090.001, T1090.003, T1105, T1573, T1570, T1113, T1678, T1484.001, T1485, T1041]
affected_products: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/"
    publisher: "ESET Research (WeLiveSecurity)"
    date: "2026-10-22"
    role: primary
closed_sources: []
evidence:
  - quote: "The data-wiping attack was executed by deploying the SDelete utility via Active Directory Group Policy"
    publisher: "ESET Research (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/"
  - quote: "blocking the public peer addresses is a viable mitigation"
    publisher: "ESET Research (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/"
verification: single-source
sourcing_note: >
  ESET is the only source; the intrusion dates and the handoff assessment come from its telemetry. ESET could not determine which of
  the two groups operated the backdoor, and the intrusion is from 2025 with a Ukrainian victim.
confidence: medium
references: ["2026-10-09/talos-ai-analysis-evasion-instructions-aimed-at-llm-triage"]
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
ESET reports that on 2025-07-16 UAC-0099 gained access to a Ukrainian grain logistics company through a spearphishing attachment: a scheduled task ran a PowerShell payload, the MATCHBOIL downloader deployed the MATCHWOK backdoor, and the next day a previously undocumented Go backdoor, MythicRatatoskr, arrived, which ESET ties to that chain with high confidence because of the timing ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)). Further copies reached other machines through an OpenSSH SFTP server, and a SOCKS5 server appeared on some of them ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)). About two months later, on 2025-09-17, the SDelete utility was deployed through Active Directory Group Policy, which ESET calls standard Sandworm tradecraft and assesses with high confidence as Sandworm after UAC-0099 handed off the access; ESET could not say which group operated MythicRatatoskr, and it sets the pair beside the earlier Gamaredon and Turla collaboration ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).

The backdoor is built on the user-space yggstack, so it needs no tunnel interface or privileges to join the Yggdrasil mesh, an encrypted IPv6 overlay in the 200::/7 range: it picks three peers at random from an embedded list of public peers and then speaks JSON over HTTPS on port 443 to a command server that has an address only inside the mesh, and some samples wait ten minutes before connecting ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)). It runs as a Windows service with an updater-style name, and it exfiltrates files and screenshots over the mesh without staging them ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)). ESET notes that hosting the command server in the mesh may prevent network security tools from detecting the outbound connections to it and that blocking the public peer addresses is a viable mitigation ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).

**Exposure:** Windows estates whose users can open email attachments from outside and whose egress to arbitrary internet peers is not filtered; there is no product vulnerability, and ESET has not seen the backdoor anywhere else ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).

**Detection:** in egress and DNS logs, connections to the public Yggdrasil peer addresses, since the mesh traffic looks like ordinary outbound connections and the peer list is the handle; in service-creation and process telemetry, a new Windows service with an updater-style name that runs a Go binary from a system or user folder, a scheduled task that runs a PowerShell payload from a temporary folder after an attachment is opened, and an OpenSSH SFTP server appearing on a workstation; and for the destructive stage, Group Policy objects that deploy SDelete or a similar wiper and mass file overwriting after a long quiet period ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).

**Triage:** ESET notes that legitimate users adopt Yggdrasil for resilient connectivity, research and hobby networking, so a single mesh connection needs a business-owner check, while a mesh peer connection together with a service named like an updater is the stronger combination ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).

**Defender takeaway:** where the mesh has no business use, block egress to the public Yggdrasil peers and alert on Group Policy changes that deploy wiper-class tools; the observed victim is Ukrainian and ESET describes UAC-0099 as targeting Ukrainian governmental, financial and media organizations, so the lesson transfers as tradecraft, in particular that initial-access activity by one group preceded a destructive stage by another two months later ([ESET Research, 2026-10-22](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/)).
