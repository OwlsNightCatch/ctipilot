---
schema: 1
kind: research
title: "DDRop: a $159 DDR5 hardware interposer silently drops targeted memory writes, defeating Intel TDX/SGX and AMD SEV-SNP integrity guarantees — no CVE, no vendor fix"
headline: "Researchers show a cheap hardware add-on can forge Intel TDX attestation reports by tampering with memory writes at the DRAM bus"
summary: >
  Researchers from KU Leuven, ETH Zurich, Durham University and Google disclosed DDRop, an
  open-source DDR5 hardware interposer costing about $159 that abuses the memory bus's own
  error-handling path to silently drop targeted writes, defeating the confidentiality and
  integrity guarantees of Intel TDX, Intel Scalable SGX and AMD SEV-SNP confidential computing —
  including forging Intel TDX remote-attestation reports. Intel and AMD confirmed the findings
  but both declare physical DRAM-bus attacks out of scope for their current threat models; neither
  is assigning a CVE or shipping a mitigation. The prerequisite is brief physical access to the
  hardware, not a software bug.
discovered_at: "2026-09-17T04:44:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-17T0409Z-intel
priority: notable
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
updates: []
migrated_from: null
---

Researchers from KU Leuven, ETH Zurich, Durham University and Google disclosed DDRop, an open-source DDR5 hardware interposer that costs roughly $159 in parts and installs in minutes ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). Unlike earlier passive bus-snooping attacks (Membuster, WireTap, TEE.fail), DDRop actively abuses the DDR5 bus's error-handling path: it forges a parity error on a targeted write and suppresses the resulting alert, so the memory module silently discards the command while the processor believes the write completed, leaving stale, attacker-chosen ciphertext in place. Unlike earlier passive interposers, which had to slow the memory bus to work with second-hand lab equipment — making the tampering easier to notice — DDRop runs at native DDR5 speed ([DDRop research team, 2026-09-14](https://ddropattack.eu/)). Against Intel TDX, the team used this to corrupt the TDX module's initialization writes to Secure Extended Page Tables, letting an attacker-controlled Trust Domain remap its own memory onto any physical RAM address; under TDX's default Logical Integrity mode this also lets an attacker corrupt a target Trust Domain's own debug-mode-attribute bit, giving roughly a 50% chance per attempt of forcing the hypervisor's debug API to dump that victim's plaintext memory before the original ciphertext is restored. Even under TDX's stronger Cryptographic Integrity mode, an attacker can still forge their own Trust Domain's launch-measurement attestation, so a backdoored VM passes remote attestation as trusted ([DDRop research team, 2026-09-14](https://ddropattack.eu/)).

The only prerequisite is brief physical access to install the interposer, on top of the standard confidential-computing threat model of a compromised hypervisor or BIOS; the researchers list malicious data-center technicians, hardware supply-chain tampering and law-enforcement or state seizure as realistic access vectors. Intel and AMD confirmed the findings under coordinated disclosure but both declared physical DRAM-bus attacks out of scope for their current products' threat model, and neither is assigning a CVE or shipping a mitigation ([Intel PSIRT, 2026-09-14](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html); [AMD Product Security, 2026-09-15](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html)). Intel says it is evaluating "Platform Owner Endorsements" — a mechanism to let remote parties verify who physically holds sensitive hardware ([Intel PSIRT, 2026-09-14](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-08-11-001.html)) — and, per heise's reporting, next-generation memory-encryption schemes with stronger hardware protection ([heise Security, 2026-09-16](https://www.heise.de/news/DDROP-Adapterstecker-hebelt-Confidential-Computing-aus-11454579.html)). Research code, hardware schematics and firmware are published publicly; no in-the-wild exploitation is claimed or plausible given the physical-access requirement.

**Defender takeaway:** DDRop undercuts the specific assurance that makes confidential computing attractive for hosting sensitive workloads on infrastructure an organization does not physically control — that a compromised host operator cannot read or tamper with a workload's memory, and that remote attestation can prove it. Any procurement or risk decision that treats Intel TDX/SGX or AMD SEV-SNP attestation as a hard trust boundary against a malicious data-center operator or seized hardware should now account for a low-cost, publicly documented physical bypass with no vendor fix; the only available lever is procedural — restricting and monitoring physical access to hardware and vetting supply-chain handling — not a patch.
