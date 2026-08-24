---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — NCSC UK names the fallback controls for endpoints that cannot take a BitLocker PIN, and states the YellowKey WinRE bypass was patched"
headline: "The pre-boot PIN is the control that survives the next WinRE bug — and for devices that cannot take one, three alternatives plus conditional access"
summary: >
  NCSC UK published guidance on 2026-08-13 responding to the YellowKey BitLocker bypass (CVE-2026-45585), which used
  the Windows Recovery Environment to decrypt drives that should have been protected. Its argument is architectural
  rather than incident-driven: BitLocker deliberately leaves WinRE unencrypted so that data can be recovered when
  BitLocker itself fails, that gap has been used to bypass BitLocker for years — Microsoft found and patched four
  similar bugs in 2025 — and it will be used again. The delta for an estate that already has the PIN recommendation is
  the fallback matrix for devices where mandatory PIN entry is impractical: a shared PIN with Windows Hello, BitLocker
  Network Unlock, or a USB Startup Key configured to require the TPM as well — and, where none of those is possible,
  conditional-access policies to keep those devices away from sensitive resources. NCSC UK also states the YellowKey issue
  was quickly patched.
discovered_at: "2026-08-14T05:09:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: routine
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - patch-available
regions:
  - global
  - europe
sectors:
  - public-sector
  - defense
entities:
  - actor:nightmare-eclipse
  - campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac
techniques:
  - T1006
affected_products:
  - "Microsoft Windows BitLocker"
  - "Microsoft Windows Recovery Environment"
cves:
  - id: CVE-2026-45585
    cvss: "6.8"
    epss: null
    type: auth-bypass
    vector: physical
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: "Windows endpoints using BitLocker without pre-boot authentication (TPM-only)"
    fixed: "NCSC UK states the issue was quickly patched; it names no build"
sources:
  - url: "https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices"
    publisher: "NCSC UK"
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "By using the Windows Recovery Environment (WinRE), YellowKey was able to bypass certain BitLocker configurations, potentially decrypting drives that should have been protected."
    publisher: "NCSC UK"
  - quote: "BitLocker deliberately does not encrypt the files associated with WinRE (because an issue with BitLocker might be the reason you need to recover data)."
    publisher: "NCSC UK"
verification: single-source-national-cert
sourcing_note: "NCSC UK publishing its own hardening guidance for its own jurisdiction is the national-CERT carve-out. Its statement that the YellowKey issue was quickly patched is reported as NCSC UK's characterisation — it names no build and this run did not verify it against a Microsoft record, which matters because this pipeline's 2026-05-20 entry recorded Microsoft as offering a workaround only."
confidence: medium
update_of: 2026-05-20/cve-2026-45585-yellowkey-microsoft-formally-assigns-cve-and
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-05-20):** NCSC UK published guidance on 2026-08-13 on why BitLocker should require a PIN, written in response to the YellowKey disclosure this pipeline tracked through the spring. The recommendation itself is not new — this pipeline's 2026-05-20 entry already argued that adding a PIN or password protector is the durable control and that Microsoft's per-endpoint WinRE registry edit is fragile — so the delta is threefold: a national authority stating the design reason the class recurs, its assertion about patch status, and, for the first time in this store, what to do on devices that genuinely cannot take a PIN.

**The design tension, stated plainly.** NCSC UK records that ["By using the Windows Recovery Environment (WinRE), YellowKey was able to bypass certain BitLocker configurations, potentially decrypting drives that should have been protected"](https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices), and then makes the point that matters for planning: this is not a new bug class. ["BitLocker deliberately does not encrypt the files associated with WinRE (because an issue with BitLocker might be the reason you need to recover data)"](https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices) — the recovery environment exists to retrieve data when BitLocker has failed, so it cannot itself be behind BitLocker, and that unencrypted surface is what successive bypasses have used. NCSC UK notes Microsoft found and patched four very similar bugs in 2025 and presented them publicly, pushes back on the characterisation of YellowKey as a backdoor, and states the issue was quickly patched. Its conclusion is that requiring authentication before WinRE can run is what protects an element of Windows that is uniquely exploitable, and that using BitLocker without a PIN will always be a half measure.

**The fallback matrix is the operational addition.** NCSC UK accepts that a mandatory PIN is impractical in real deployments — it names shared devices with multiple users and devices used in time-critical emergencies, where the seconds spent typing a PIN cannot be spared — and gives three alternatives with different trust models rather than leaving those endpoints uncovered. Using the *same PIN for Windows Hello and BitLocker* removes the memorisation burden and is explicitly not suitable for shared devices, but is described as considerably more protection than no PIN. *Network Unlock* reads the key from a trusted corporate network and skips the prompt while the device is on it, reverting to a PIN prompt when the device is disconnected — which is the condition that matters if a device is stolen — and NCSC UK calls it often the best option for desktops. A *Startup Key* on a USB stick provides a different kind of pre-boot authentication, with the caveat that a physical key can be lost or stolen and that it must be configured to require the TPM **and** the key together, not the key alone. And for the devices where none of those three works, NCSC UK names a fourth control that is not a BitLocker setting at all: ["Finally, if there is no way to add pre-boot authentication to your device, consider how you are going to manage that additional risk. For example, you may wish to use conditional access policies to prevent these high-risk devices from accessing sensitive resources."](https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices) That is the one an estate with a long exception list should read first, because it is the only option that does not require the endpoint to change — it moves the risk decision to what the device is allowed to reach. The closing instruction is blunt: whatever you choose, do not do nothing.

**Why this still matters after the patch.** The reason to act on guidance about a flaw the authority says is fixed is that the fix is for one bug in a surface that structurally cannot be closed — NCSC UK's own framing is that YellowKey was not the first WinRE-based BitLocker bypass and will not be the last. For a public-administration laptop estate, the practical consequence is that the exception list is the risk register: every device still running TPM-only BitLocker is one that the next disclosure in this class will reach, and the four fallbacks above convert that list into something better than nothing without a fleet-wide PIN rollout. This is a hardening programme rather than an incident response, which is why this entry ships no action item — the body carries the decision, and the timeline is the organisation's own.
