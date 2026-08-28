---
schema: 1
kind: vulnerability
horizon: operational
title: "Unisoc T606/T612/T7250 modems: a single answered video call can escalate from modem-level RCE to full Android kernel access via an ARM Memory Protection Unit isolation bypass — no CVE, no patch, vendor unresponsive"
headline: "Answering a video call is the only user action needed to hand an attacker root-level access on affected Android devices"
summary: >
  Independent researcher 0x50594d, via SSD Secure Disclosure, chained a March-2026 VoLTE
  SIP/SDP memory-corruption bug in shared Unisoc modem firmware (T606/T612/T7250) with a new
  uncontrolled-recursion flaw that lets modem-level code fully reprogram the ARM Memory Protection
  Unit separating modem memory from the Android application processor. The only user action
  needed is answering an incoming video call. No CVE, no firmware update, and Unisoc has not
  responded to disclosure attempts.
discovered_at: "2026-08-28T05:48:00Z"
updated_at: null
event_date: "2026-08-17"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, priv-esc, no-patch]
regions: [global]
sectors: [public-sector, telco]
entities: []
techniques: [T1210, T1068]
affected_products: ["Unisoc T606", "Unisoc T612", "Unisoc T7250"]
cves: []
sources:
  - url: "https://www.infosecurity-magazine.com/news/unisoc-modem-flaw-rce-calls/"
    publisher: "Infosecurity Magazine"
    date: "2026-08-17"
    role: primary
  - url: "https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems"
    publisher: "Dark Reading"
    date: "2026-08-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The new flaw that SSD Security discovered is a memory-isolation weakness in Unisoc's T612 modem's memory protection unit. The firmware flaw allows an attacker who already has access to the modem to escalate privileges and gain kernel level privileges on an affected Android device."
    publisher: "Dark Reading, citing SSD Secure Disclosure"
  - quote: "The disclosure does not identify a vendor firmware update addressing the flaw."
    publisher: "Infosecurity Magazine, citing SSD Secure Disclosure"
verification: multi-source
sourcing_note: >
  SSD Secure Disclosure's own posts (ssd-disclosure.com, both the landing page and the two named
  post URLs) were unreachable on every transport this run — an anti-bot HTTP 202 shell with no
  extractable body, and the jina reader pool credit-exhausted throughout. Composed entirely from
  two independent B-reliability secondary sources that both directly quote and link the primary;
  confidence is MEDIUM rather than HIGH because the primary itself could not be read and some fine
  technical detail (the exact SDP field/parser involved, the precise coprocessor register
  sequence) may exist in the SSD post that these secondaries do not carry.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Independent researcher 0x50594d, via SSD Secure Disclosure, chained two flaws in Unisoc modem firmware shared across the T606, T612 and T7250 chipsets — confirmed on the Motorola E13 (T606), Realme C33 (T612) and Xiaomi Redmi A5 (T7250), though SSD does not present this as an exhaustive device list. Stage one, disclosed earlier in March 2026, is a memory-corruption bug in the modem's handling of SIP/SDP messages during VoLTE call setup, giving remote code execution inside the modem processor. Stage two, the new SSD finding, is an uncontrolled-recursion flaw (CWE-674) that lets code already running in the modem write a full-access configuration to the ARM Memory Protection Unit via coprocessor registers: "the new flaw that SSD Security discovered is a memory-isolation weakness in Unisoc's T612 modem's memory protection unit. The firmware flaw allows an attacker who already has access to the modem to escalate privileges and gain kernel level privileges on an affected Android device" ([Dark Reading, citing SSD Secure Disclosure, 2026-08-17](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)).

The MPU is the only hardware boundary separating modem memory from the application processor's memory, including memory used by the Android kernel; Unisoc's design shares that physical memory space between the two processors with no independent hardware enforcement beyond it. The overall attack requires an attacker-controlled position on the 4G/VoLTE network able to deliver the malformed SIP/SDP payload during call setup, and the victim simply answering an incoming video call — no other user interaction. CWE-1189 (Improper Isolation of Shared Resources on a System-on-a-Chip) is the classification given for the combined chain. No CVE identifier has been assigned, and no firmware update or mitigation is available: "the disclosure does not identify a vendor firmware update addressing the flaw" ([Infosecurity Magazine, citing SSD Secure Disclosure, 2026-08-17](https://www.infosecurity-magazine.com/news/unisoc-modem-flaw-rce-calls/)). Unisoc did not respond to SSD's disclosure attempts, and device owners have no interim control beyond watching for a manufacturer firmware update.

Unisoc chips are concentrated in budget-tier Android devices, a segment with weaker patch cadence and longer field life; this is relevant to any BYOD or public-sector device fleet that includes low-cost handsets. `actions[]` is left empty deliberately: no vendor fix or interim mitigation exists, and the only defender-facing lever — device-fleet composition — is a standing inventory question rather than a do-now task this specific disclosure changes. The transferable lesson for a device-procurement or BYOD policy is that chipset-level isolation defects can sit below any control the device's own OS vendor can patch, since the flaw is in modem firmware Unisoc alone controls, not in Android itself.
