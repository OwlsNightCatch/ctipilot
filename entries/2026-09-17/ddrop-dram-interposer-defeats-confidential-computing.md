---
schema: 1
kind: research
title: "DDRop: a $159 DDR5 hardware interposer silently drops targeted memory writes, defeating Intel TDX/SGX and AMD SEV-SNP integrity guarantees, with no vendor fix"
headline: "Researchers show a cheap hardware add-on can forge Intel TDX attestation reports by tampering with memory writes at the DRAM bus"
summary: >
  Researchers from KU Leuven, ETH Zurich, Durham University and Google disclosed DDRop, an
  open-source DDR5 hardware interposer costing about $159 that abuses the memory bus's own
  error-handling path to silently drop targeted writes. They show it undermining the protection of
  Intel TDX, Intel Scalable SGX and AMD SEV-SNP confidential computing, and on Intel TDX forging
  remote-attestation reports. Intel and AMD acknowledged the findings but place physical attacks on
  the memory bus outside their threat models. AMD does not plan to assign a CVE or release mitigations, and
  Intel is evaluating further hardening. The prerequisite is brief physical access to install the
  interposer, which takes minutes, not a software bug.
discovered_at: "2026-09-17T04:44:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-17T0409Z-intel
priority: routine
immediate_action: null
tags: [cloud]
regions: [global]
sectors: [public-sector, technology]
entities: ["tool:ddrop-hardware-interposer"]
techniques: [T1200, T1553]
affected_products: ["Intel TDX", "Intel Scalable SGX", "AMD SEV-SNP"]
cves: []
sources:
  - url: "https://ddropattack.eu/"
    publisher: "DDRop research team (KU Leuven / ETH Zurich / Durham University / Google)"
    date: "2026-09-14"
    role: primary
  - url: "https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html"
    publisher: "Intel PSIRT"
    date: "2026-09-14"
    role: corroborating
  - url: "https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html"
    publisher: "AMD Product Security (AMD-SB-3048)"
    date: "2026-09-15"
    role: corroborating
  - url: "https://www.heise.de/news/DDROP-Adapterstecker-hebelt-Confidential-Computing-aus-11454579.html"
    publisher: "heise Security"
    date: "2026-09-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "DDRop is a small, low-cost hardware interposer device that can make writes to a server's memory disappear, causing the computer to read old data as if it were newly written."
    publisher: "DDRop research team"
  - quote: "This primitive is 100% deterministic and lets an attacker-controlled TD remap its own memory onto any physical address in RAM."
    publisher: "DDRop research team"
  - quote: "Intel's analysis confirms that the described scenarios fall outside Intel's standard threat model for confidential computing deployments."
    publisher: "Intel PSIRT"
  - quote: "AMD has assessed this report and has determined that the described technique relies on a physical attack against the memory bus, which falls outside the scope of the published threat model for SEV-SNP. AMD does not plan to assign a CVE or release mitigations in response to this report."
    publisher: "AMD Product Security (AMD-SB-3048)"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:08Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: hardware research needing physical access, with
      no near-term decision for Swiss public bodies. The body is shortened to suit that priority, and
      the vendor positions are narrowed to what Intel and AMD published: AMD does not plan to assign a CVE
      or release mitigations, and Intel is evaluating further hardening. The title no longer says
      neither vendor assigns a CVE, since only AMD says so.
    fields: [priority, body, summary, title]
migrated_from: null
---

Researchers from KU Leuven, ETH Zurich, Durham University and Google disclosed DDRop, an open-source DDR5 hardware interposer that costs about $159 in parts and, unlike earlier passive interposers, runs at native bus speed ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). It forges a parity error on a targeted write and suppresses the alert, so the memory module silently drops the write and stale, attacker-chosen ciphertext stays in place. Against Intel TDX this corrupts the TDX module's initialization of Secure Extended Page Tables, so an attacker-controlled Trust Domain can remap its memory onto other physical memory. Under TDX's default logical integrity mode that lets the attacker flip a victim Trust Domain's debug attribute and read its memory through the hypervisor's debug API, and even under cryptographic integrity mode the attacker can forge the launch measurement of a rogue VM of their own so that it passes remote attestation ([DDRop research team, 2026-09-14](https://ddropattack.eu/)).

The attack needs a brief, one-time visit to install the interposer, which takes minutes, on top of the standard confidential-computing threat model in which the adversary controls the hypervisor and BIOS. The researchers name data-center insiders, supply-chain tampering and hardware access compelled by law enforcement or governments as ways to get that access ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). Intel and AMD both place physical attacks on the memory bus outside their threat models; AMD does not plan to assign a CVE, and Intel is evaluating further hardening and detection options ([Intel PSIRT, 2026-09-14](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html); [AMD Product Security, 2026-09-15](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html)). Schematics, board files, firmware and proof-of-concept code are public ([DDRop research team, 2026-09-14](https://ddropattack.eu/)), and no in-the-wild use is claimed.

**Defender takeaway:** Confidential computing on Intel TDX, Intel Scalable SGX or AMD SEV-SNP is no longer a hard trust boundary against whoever physically holds the hardware, including the cloud provider it is meant to exclude, and on Intel TDX even remote attestation can be forged ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). A risk decision that relies on it for that case must account for a cheap, public physical bypass with no vendor fix. Restricting and monitoring physical access to servers, as Intel advises, is the remaining lever ([Intel PSIRT, 2026-09-14](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html)).

## Correction — 2026-09-30T06:56:08Z

Intel and AMD acknowledged the findings and place physical attacks on the memory bus outside their threat models ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). Only AMD says it does not plan to assign a CVE or release mitigations ([AMD Product Security, 2026-09-15](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html)). Intel's announcement does not mention a CVE and says Intel is evaluating additional architectural hardening options and detection mechanisms ([Intel PSIRT, 2026-09-14](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html)). The earlier statement that both vendors confirmed the findings and that neither is assigning a CVE went beyond what they published.
