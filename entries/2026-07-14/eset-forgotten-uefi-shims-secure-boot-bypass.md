---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-8863, CVE-2026-10797 — forgotten pre-0.9 UEFI shims bypass Secure Boot via a signature-length validation mismatch"
headline: "ESET details 11 Microsoft-signed pre-0.9 UEFI shims that bypass Secure Boot on any machine trusting the third-party UEFI CA"
summary: >
  ESET Research published (2026-07-14) a technical dissection of 11 Microsoft-signed UEFI shim bootloaders
  (all shim version 0.9 or below) that undermine Secure Boot on any machine trusting the "Microsoft
  Corporation UEFI CA 2011" third-party certificate, regardless of installed OS. The core flaw
  (CVE-2026-10797) is a signature-length validation mismatch that lets an attacker evade the shim's
  revocation check while still passing signature verification; companion weaknesses (CVE-2026-8863) cover
  pre-0.9 non-enforcement of the MOK deny-list and pre-15.3 absence of SBAT. Microsoft revoked all 11
  binaries in the 2026-06-09 dbx update; no in-the-wild exploitation has been reported. Fleets that have not
  applied the June dbx revocation carry a persistent Secure-Boot-bypass exposure.
discovered_at: "2026-07-14T12:45:00Z"
event_date: "2026-07-14"
run_id: 2026-07-14T1210Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, auth-bypass, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1542.003, T1553.006]
affected_products: ["Shim (UEFI bootloader, versions ≤ 0.9)", "Red Hat Enterprise Linux / CentOS 7.2", "Oracle Linux", "openSUSE", "ROSA Linux", "Baramundi Management Suite", "Blancco/WhiteCanyon WipeDrive", "PC-Doctor Service Center", "Spyrus WTGCreator", "Abitti"]
cves:
  - id: CVE-2026-10797
    cvss: null
    epss: null
    type: auth-bypass
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "shim bootloader versions ≤ 0.9 (signature-length validation mismatch)"
    fixed: "revoked via Microsoft dbx (Forbidden Signature Database) update, 2026-06-09"
  - id: CVE-2026-8863
    cvss: null
    epss: null
    type: auth-bypass
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "shim bootloader versions ≤ 0.9 (trust-validation weakness in the forgotten shim set)"
    fixed: "revoked via Microsoft dbx (Forbidden Signature Database) update, 2026-06-09"
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/"
    publisher: "ESET Research (WeLiveSecurity)"
    date: "2026-07-14"
    role: primary
  - url: "https://kb.cert.org/vuls/id/616257"
    publisher: "CERT/CC — VU#616257"
    date: "2026-06-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the revocation check used the value from the signature header, while the signature verification function used the value from the PE header"
    publisher: "ESET Research"
  - quote: "An attacker needs no complicated exploitation primitives – only a copy of an old, still-trusted, but unrevoked shim binary and a basic understanding of how UEFI shims work."
    publisher: "ESET Research"
  - quote: "An attacker could exploit these vulnerable shim bootloaders using a Bring Your Own Vulnerable Driver (BYOVD)-style technique to execute arbitrary code during the early boot phase, prior to operating system initialization, thereby bypassing Secure Boot protections."
    publisher: "CERT/CC"
verification: multi-source
sourcing_note: "ESET Research is the primary technical source; CERT/CC's coordinated VU#616257 corroborates the class and carries the complete affected-vendor list. CVSS scores were not stated in ESET's write-up and are left null; the two CVE identifiers resolve on cve.org. ESET deliberately withholds indicators of compromise to avoid mass misidentification of the many legitimate systems that carry these still-trusted binaries."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Confirm Microsoft's 2026-06-09 dbx (Forbidden Signature Database) revocation is enrolled in firmware across the Windows and Linux/dual-boot fleet — dbx enrollment commonly lags OS patching — and audit EFI System Partitions for forked/vendored shim binaries at version ≤ 0.9 or lacking SBAT (the sei-vsarvepalli/uefi-dbx-audit script and Microsoft's secureboot_objects dbx manifest are the concrete artifacts to diff against)."
migrated_from: null
---

ESET Research published (2026-07-14) a full dissection of 11 Microsoft-signed UEFI shim bootloaders — all at shim version 0.9 or below — that undermine Secure Boot on any machine trusting the "Microsoft Corporation UEFI CA 2011" third-party certificate, independent of which OS is installed ([ESET Research, 2026-07-14](https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/)). The primary flaw (CVE-2026-10797) is a signature-length validation mismatch: an Authenticode-signed PE records its signature length in two places, and "the revocation check used the value from the signature header, while the signature verification function used the value from the PE header" ([ESET Research, 2026-07-14](https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/)), so an attacker can tamper the `WIN_CERTIFICATE` structure to make the revocation routine compare the deny-lists against bogus data while verification still succeeds. Two companion weaknesses in the same forgotten binaries (tracked with CVE-2026-8863) compound it: shims below 0.9 never enforce the MOK deny-list (MokListX), so an older still-trusted shim can be substituted to load a binary that was explicitly revoked, and shims before version 15.3 predate SBAT (Secure Boot Advanced Targeting) entirely, reopening old GRUB 2 bugs such as CVE-2015-5281 that SBAT was built to close.

Crucially, exploitation requires no complex exploitation primitive — "only a copy of an old, still-trusted, but unrevoked shim binary" copied to the EFI System Partition alongside a compatible second-stage bootloader ([ESET Research, 2026-07-14](https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/)); writing to the ESP is itself a privileged local operation (consistent with this entry's local, post-auth vector), so the technique is a persistence/defense-evasion primitive for an attacker who already has that access rather than a remote initial-access exploit. CERT/CC frames it as a "Bring Your Own Vulnerable Driver (BYOVD)-style technique to execute arbitrary code during the early boot phase, prior to operating system initialization" ([CERT/CC, 2026-06-17](https://kb.cert.org/vuls/id/616257)). Because the vulnerable binary travels with the boot media rather than the installed OS, any endpoint trusting the third-party UEFI CA is a candidate carrier even when its OS is fully patched. Vendors named in CERT/CC's coordinated disclosure include Red Hat/CentOS, Oracle Linux, openSUSE, ROSA Linux, Baramundi Management Suite, Blancco/WhiteCanyon WipeDrive, PC-Doctor Service Center, Spyrus WTGCreator, and Finland's Abitti exam-kiosk system — a long tail of Linux-distro, PC-diagnostic, disk-wipe and kiosk tooling that forked an old shim and never rebased onto upstream fixes. Microsoft revoked all 11 binaries in its 2026-06-09 Patch Tuesday dbx update; no in-the-wild exploitation has been reported, and ESET deliberately withholds indicators of compromise because the binaries are "present on thousands of systems that have never been compromised via these loaders."

**Defender takeaway.** This is a pre-OS-boot technique class, so runtime endpoint telemetry cannot see the exploitation step — the actionable control is inventory and firmware-state verification, not detection. Confirm the June dbx revocation is actually enrolled in firmware (firmware-level dbx updates frequently lag OS patching, and a machine can show a fully patched OS while its dbx is stale), sequencing the accompanying DB update before the DBX update where the vendor guidance calls for it to avoid bricking dual-boot or recovery partitions, then audit Linux and dual-boot EFI System Partitions for forked shim binaries at version ≤ 0.9. **Triage:** legitimate dual-boot recovery media and vendor diagnostic USB sticks are exactly the artifact class this bug lives in, so a hunt for "old shim present" will surface real, benign, stale tooling — the discriminator is not the shim's presence but whether the dbx revocation has been enrolled in that device's firmware: a revoked-but-present shim is inert, an unrevoked one is the exposure.
