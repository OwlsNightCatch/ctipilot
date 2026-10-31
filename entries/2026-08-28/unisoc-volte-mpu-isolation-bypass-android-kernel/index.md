---
schema: 1
kind: vulnerability
title: "Unisoc T612 modem (and other devices on shared Unisoc modem firmware): a single answered video call can escalate from modem-level RCE to full Android kernel access via an ARM Memory Protection Unit isolation bypass; no CVE, no patch, vendor unresponsive"
headline: "Answering a video call is the only user action needed to hand an attacker root-level access on affected Android devices"
summary: >
  Independent researcher 0x50594d, via SSD Secure Disclosure, chained a March-2026 VoLTE
  SIP/SDP memory-corruption bug in shared Unisoc modem firmware with a new
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
affected_products: ["Unisoc T612"]
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
  post URLs) were unreachable on every transport tried, most recently on 2026-08-30: an anti-bot HTTP 202 shell with no
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
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: correction
    summary: >
      The chipset scope was overstated. This entry named Unisoc T606, T612 and T7250 as affected
      and mapped the three test devices one to one onto them (Motorola E13 to T606, Xiaomi Redmi
      A5 to T7250). Neither reachable source contains the strings T606 or T7250 anywhere: Dark
      Reading and Infosecurity name only the T612, and only the Realme C33 is tied to a chipset
      at all. The SSD Secure Disclosure primary remains behind an anti-bot challenge on every
      transport, so the wider chipset list cannot be traced to any readable source and has been
      removed from the title, summary, affected products and body.
    fields: [title, summary, affected_products, sourcing_note, body]
migrated_from: null
---

Independent researcher 0x50594d, via SSD Secure Disclosure, chained two flaws in Unisoc modem firmware. The only chipset either reachable source names is the T612, demonstrated on a Realme C33; SSD also confirmed the vulnerability on a Xiaomi Redmi A5 and a Motorola E13, without either source stating which chipset those two carry. Treat the affected estate as devices on the shared Unisoc modem firmware line rather than as a closed list of three parts. Stage one, disclosed earlier in March 2026, is a memory-corruption bug in the modem's handling of SIP/SDP messages during VoLTE call setup, giving remote code execution inside the modem processor. Stage two, the new SSD finding, is an uncontrolled-recursion flaw (CWE-674) that lets code already running in the modem write a full-access configuration to the ARM Memory Protection Unit via coprocessor registers: "the new flaw that SSD Security discovered is a memory-isolation weakness in Unisoc's T612 modem's memory protection unit. The firmware flaw allows an attacker who already has access to the modem to escalate privileges and gain kernel level privileges on an affected Android device" ([Dark Reading, citing SSD Secure Disclosure, 2026-08-17](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)).

The MPU is the only hardware boundary separating modem memory from the application processor's memory, including memory used by the Android kernel; Unisoc's design shares that physical memory space between the two processors with no independent hardware enforcement beyond it. The overall attack requires an attacker-controlled position on the 4G/VoLTE network able to deliver the malformed SIP/SDP payload during call setup, and the victim simply answering an incoming video call — no other user interaction. CWE-1189 (Improper Isolation of Shared Resources on a System-on-a-Chip) is the classification given for the combined chain. No CVE identifier has been assigned, and no firmware update or mitigation is available: "the disclosure does not identify a vendor firmware update addressing the flaw" ([Infosecurity Magazine, citing SSD Secure Disclosure, 2026-08-17](https://www.infosecurity-magazine.com/news/unisoc-modem-flaw-rce-calls/)). Unisoc did not respond to SSD's disclosure attempts, and device owners have no interim control beyond watching for a manufacturer firmware update.

Unisoc chips are concentrated in budget-tier Android devices, a segment with weaker patch cadence and longer field life; this is relevant to any BYOD or public-sector device fleet that includes low-cost handsets. No vendor fix or interim mitigation exists; the only defender-facing lever — device-fleet composition — is a standing inventory question. The transferable lesson for a device-procurement or BYOD policy is that chipset-level isolation defects can sit below any control the device's own OS vendor can patch, since the flaw is in modem firmware Unisoc alone controls, not in Android itself.

## Correction — 2026-08-30T13:12:06Z

This entry named Unisoc T606, T612 and T7250 as the affected chipsets and paired each with one of the three test devices. That pairing is not in any source this entry can cite. Dark Reading and Infosecurity Magazine both name only the T612, and only for the Realme C33: "Researchers at SSD Secure Disclosure... demonstrated the attack chain in a controlled setting against a Realme C33 smartphone... SSD confirmed the vulnerability on a Xiaomi Redmi A5 running the January 2026 Android security patch and a Motorola E13 running the February 2025 patch" ([Dark Reading, 2026-08-17](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)) — with no chipset given for the latter two. The SSD Secure Disclosure write-up itself is still unreachable, so nothing wider can be confirmed. Operationally the exposure is unchanged and if anything less bounded: the flaw sits in modem firmware shared across a product line, and an asset owner should scope by device model against the vendor's own advisory rather than by the three part numbers this entry previously listed.
