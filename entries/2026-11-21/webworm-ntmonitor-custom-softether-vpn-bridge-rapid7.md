---
schema: 1
kind: threat
title: "Webworm's NtMonitor: Rapid7 finds a custom rebuild of the SoftEther VPN Bridge that removes the open-source tool's detection fingerprints (rebranded metadata, renamed handshake endpoints, a custom handshake watermark, an embedded resource archive and an encrypted configuration), attributed with moderate confidence to the China-aligned actor that targets European governments"
headline: "Rapid7: Webworm hides SoftEther VPN Bridge behind NtMonitor branding, new endpoints and an encrypted config"
summary: >
  Rapid7 describes NtMonitor, a Windows build of SoftEther VPN Bridge 4.44 that it attributes with moderate confidence to Webworm, the China-aligned actor that ESET documented moving to European government targets in May 2026. The rebuild keeps SoftEther's function of bridging a remote network into the victim's LAN and strips its fingerprints: branding, handshake paths, the handshake watermark, the separate resource archive and the plain-text configuration are all changed, and Rapid7 found no backdoor or other added capability. Only one antivirus vendor detected the sample on VirusTotal although it has been public since January.
discovered_at: "2026-11-21T04:49:00Z"
updated_at: null
event_date: "2026-11-19"
run_id: 2026-11-21T0355Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage]
regions: [europe]
sectors: [public-sector]
entities: ["actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu", "malware:ntmonitor"]
techniques: [T1587.001, T1027.005, T1027.013, T1140, T1036.005, T1686.003, T1599, T1090.001, T1071]
affected_products: []
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge"
    publisher: "Rapid7"
    date: "2026-11-19"
    role: primary
  - url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
    publisher: "ESET Research"
    date: "2026-05-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "NtMonitor changes the upstream GIF watermark with a custom byte pattern (a truncated PNG file showing the Windows logo), so that stock SoftEther clients and servers cannot handshake with this build"
    publisher: "Rapid7"
    source_url: "https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge"
  - quote: "which we attribute to Webworm with moderate confidence"
    publisher: "Rapid7"
    source_url: "https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge"
verification: single-source
sourcing_note: >
  Rapid7 is the only analyst of the tool and works from the one public sample plus decrypted configurations its own intelligence holds; the attribution is Rapid7's, at moderate confidence, resting on matching TTPs reported by ESET and on infrastructure in configurations that Rapid7 says it has seen tied to Webworm before. ESET is cited for the earlier shift of the actor, not for this tool.
confidence: medium
references: ["2026-05-21/webworm-china-aligned-shifts-to-eu-government-targets-echocr"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Rapid7 analysed what it believes is a so-far unknown custom tool, a modified build of SoftEther VPN Bridge version 4.44 (build 9807) that it attributes to Webworm with moderate confidence ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)). Webworm is the China-aligned actor that ESET reported in May 2026 moving to European government targets and to dual-use tools such as SoftEther ([ESET Research, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). The rebuild keeps the bridge function, which cascades a remote network into the victim's local network, and removes the fingerprints: the PE metadata and internal strings are rebranded as a network-monitoring product (inconsistently, since the service name and many registry paths still say SoftEther), the HTTP handshake endpoints get update-style names, the handshake watermark becomes a truncated PNG header so stock SoftEther peers cannot connect and the stock watermark cannot fingerprint the build, the resource archive that normally sits beside the executable is embedded in it as a PE resource, and the configuration is stored under a new name in a custom-encrypted format ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)). Rapid7 found no backdoor or other added capability, concludes the actor puts stealth above capability, and says only one antivirus vendor detected the sample although it has been public since January ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)).

**Exposure:** Windows hosts in government networks that Webworm has already compromised; Rapid7 says that in every configuration it holds the VPN is set to bridge a remote network into the local one ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)).

**Detection:** Rapid7's most reliable network detection, where TLS traffic can be inspected, is a POST request to an update-themed CGI path with a JPEG content type whose body starts with a PNG file header; on hosts, look for a SoftEther VPN Bridge service that was not installed by the organisation, in particular one whose binary carries its resource archive inside itself, and for firewall rules added by such a service ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)). Rapid7 calls the branding the easiest change for the actor to make next and says the endpoints and watermark can be swapped out trivially, so behaviour that is intrinsic to SoftEther matters more than any one string ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)).

**Defender takeaway:** government networks in Europe should treat any unmanaged SoftEther VPN Bridge, however it is named, as a persistence mechanism that bridges an outside network into theirs, and learn the tool's intrinsic behaviour, as Rapid7 recommends for the government sector ([Rapid7, 2026-11-19](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge)).
