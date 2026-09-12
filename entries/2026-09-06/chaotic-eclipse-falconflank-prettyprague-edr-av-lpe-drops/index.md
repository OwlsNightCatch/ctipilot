---
schema: 1
kind: vulnerability
title: "Chaotic Eclipse turns its zero-day drops on third-party security products: local privilege escalation in CrowdStrike Falcon and Avast, with working proof-of-concept code public — all three vendors have since remediated"
headline: "CrowdStrike, Gen Digital and Kaspersky have all now remediated one researcher's four security-product PrivEsc PoCs, per LevelBlue's follow-up analysis"
summary: >
  The pseudonymous researcher tracked as Chaotic Eclipse / Nightmare Eclipse published working
  local-privilege-escalation proof-of-concept code against three security products in early September
  2026, without vendor notice. FalconFlank abused CrowdStrike Falcon Sensor's Office malicious-macro
  remediation to reach SYSTEM; PrettyPrague dumped the SAM database and spawned a SYSTEM shell through
  the Avast Sandbox component; Kaspersky's HardBreacher was fixed first, on 2026-08-31. LevelBlue's
  2026-09-09 independent analysis states both FalconFlank and PrettyPrague have since received vendor
  remediation as well; The Hacker News names a specific fixed version for Avast (26.7.11086 fix
  992 / 26.8.11125 fix 993, released 2026-09-04) but no CrowdStrike source names a specific
  Falcon build or date. No CVEs are
  assigned to any of the four PoCs analysed.
discovered_at: "2026-09-06T14:00:00Z"
updated_at: "2026-09-10T05:10:00Z"
event_date: "2026-09-03"
run_id: 2026-09-06T1308Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, priv-esc, lpe, poc-public, patch-available]
regions: [global, europe]
sectors: [public-sector, technology]
entities: ["actor:nightmare-eclipse", "tool:hardbreacher", "tool:prettyprague", "tool:falconflank", "tool:greensection"]
techniques: [T1068, "T1003.002", T1134.004, T1548.002, T1574.001, T1211]
affected_products: ["CrowdStrike Falcon", "Avast Antivirus", "Kaspersky Endpoint Security for Windows"]
cves: []
sources:
  - url: "https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html"
    publisher: "The Hacker News"
    date: "2026-09-03"
    role: primary
  - url: "https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike"
    publisher: "Truesec"
    date: "2026-09-04"
    role: corroborating
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/expanding-the-attack-surface-analyzing-nightmare-eclipses-latest-pocs"
    publisher: "LevelBlue (Trustwave) SpiderLabs"
    date: "2026-09-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We are actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting"
    publisher: "The Hacker News (quoting a CrowdStrike spokesperson)"
  - quote: "As of now the PoC works in a fully updated windows 11 25H2 / Windows Server 2025 with Crowdstrike Falcon – Phase 3 Optimal Protection with “Microsoft Office file malicious macro removal” setting."
    publisher: "Truesec"
  - quote: "Gen was recently made aware of a security vulnerability affecting a subset of Gen products, including Avast Antivirus, that could allow an attacker to elevate their system privileges. We immediately initiated our security response procedures and are actively developing a patch."
    publisher: "The Hacker News (quoting a Gen Digital spokesperson)"
  - quote: "Every Windows logon session has a private object directory inside the kernel's namespace – \\Sessions\\0\\DosDevices\\{AuthId}\\, and any standard user process can place symbolic links inside their own session's directory without any special privilege."
    publisher: "LevelBlue (Trustwave) SpiderLabs"
  - quote: "The vulnerability is that a standard user process can send IOCTL 0x82AC0054 directly to the aswSnx driver to request that a chosen executable be run inside the sandbox."
    publisher: "LevelBlue (Trustwave) SpiderLabs"
  - quote: "For CrowdStrike clients to be susceptible to this local privilege escalation vulnerability, an endpoint must be assigned to a Prevention Policy with the \"Microsoft Office file malicious macro removal\" setting enabled. This vulnerability does not impact CrowdStrike Falcon Government clients."
    publisher: "LevelBlue (Trustwave) SpiderLabs"
  - quote: "As of September 4, 2026, Gen has released a patch for the following versions of Avast Antivirus for Windows"
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: "The Hacker News carries first-party statements it obtained directly from CrowdStrike, Gen Digital and Kaspersky, which is what establishes the patch status of each product; Truesec independently describes the FalconFlank preconditions and the mitigation from its own reading. LevelBlue SpiderLabs has since independently reproduced and analysed all four PoCs, supplying the mechanism-level detail (session-namespace symlink hijacking, aswSnx IOCTL abuse, reparse-point/oplock redirection) the original vendor statements did not carry, and confirming FalconFlank, PrettyPrague and HardBreacher against its own testing. Reliability held at B: no vendor has published a formal advisory of its own (CrowdStrike points customers to an unread support-portal Tech Alert; Gen Digital has issued only the quoted statement), and LevelBlue is an original-research lab rather than a first-party authority. Credibility raised to 1 now that an independent second party (LevelBlue) has reproduced and confirmed the core findings across all four PoCs, rather than only relaying the vendors' own statements."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Confirm every CrowdStrike Falcon sensor and Gen Digital Avast install (including on unmanaged or contractor endpoints) is on the current release now that both vendors are reported to have remediated FalconFlank and PrettyPrague; until that is confirmed, treat any endpoint on an older build as still exposed and keep the \"Microsoft Office File Suspicious Macro Removal Windows\" Falcon prevention setting disabled as an interim control on unconfirmed hosts."
updates:
  - at: "2026-09-10T05:10:00Z"
    run_id: 2026-09-10T0410Z-intel
    type: update
    summary: >
      LevelBlue SpiderLabs independently reproduced and analysed all four PoCs, supplying
      mechanism-level detail the original vendor statements lacked: HardBreacher's session-namespace
      symlink DLL-load-path hijack with parent-PID spoofing, PrettyPrague's aswSnx IOCTL abuse to
      dump and offline-decrypt the SAM database via a CMSTPLUA UAC bypass, and a reparse-point/oplock
      mechanism for FalconFlank — which LevelBlue's own lab testing found CrowdStrike's cloud ML
      detection caught and quarantined, preventing the final step in that test run. LevelBlue also
      independently characterises GreenSection as a
      shared-memory-section trust-boundary finding with no demonstrated privilege escalation, a
      narrower claim than the original report's "memory-corruption bug" framing. Credibility moves
      from 2 to 1 on this independent confirmation. LevelBlue's own Key Takeaways further state that
      both FalconFlank and PrettyPrague have since received vendor remediation, though it names no
      specific patch version or date for either — superseding this entry's original "no fix"/"still
      developing a patch" framing for both, which the title, headline, summary, tags, actions and
      body are corrected to reflect.
    fields: [title, headline, summary, tags, actions, entities, techniques, sources, evidence, sourcing_note, classification, body]
migrated_from: null
---

The pseudonymous researcher tracked here as Nightmare Eclipse, and by The Hacker News under the further aliases Chaotic Eclipse, INFINITE NIGHTMARE and MSNightmare, spent 2026 publishing working proof-of-concept exploits for Windows and Microsoft Defender privilege escalations without giving the vendor advance notice. In early September the target set changed: three of the four latest drops are against third-party endpoint security products rather than Microsoft's, and at disclosure two of them had no fix ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)) — both are now reported remediated (see the update below). That shift is what makes this an operational matter for estates that never had Defender in scope.

FalconFlank abuses CrowdStrike Falcon Sensor's Office malicious-macro remediation path. The remediation routine runs at high privilege in order to clean an infected document in place, and the exploit turns that cleanup into a low-privileged account's route to SYSTEM. Truesec, reading the release independently, records the preconditions precisely: the proof-of-concept "works in a fully updated windows 11 25H2 / Windows Server 2025 with Crowdstrike Falcon – Phase 3 Optimal Protection with 'Microsoft Office file malicious macro removal' setting" ([Truesec, 2026-09-04](https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike)). A CrowdStrike spokesperson told The Hacker News the company is "actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting", adding that customers "remain protected through the Cloud Anti-malware for Microsoft Office Files settings" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). At disclosure there was no patch and no CVE, and the only control on offer was turning a prevention feature off, which Truesec notes means malicious macros will no longer be replaced in place while cloud-side blocking continues ([Truesec, 2026-09-04](https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike)); CrowdStrike is now reported to have remediated the flaw (see the update below).

PrettyPrague is the same shape against a different vendor. The researcher describes it as dumping the SAM database "by abusing a vulnerability in Avast Sandbox" and spawning a full SYSTEM shell against fully patched Avast Antivirus on a patched Windows 11 25H2 host, and states a belief that other Gen Digital products including AVG and Norton are affected ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). Gen Digital confirmed a vulnerability "affecting a subset of Gen products, including Avast Antivirus, that could allow an attacker to elevate their system privileges" and said at the time it was "actively developing a patch", without naming which further products are in scope ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)); Gen Digital is now reported to have shipped that fix (see the update below). The third drop, HardBreacher against Kaspersky Endpoint Security for Windows 14.0.0.504, is the one that is resolved: Kaspersky told the same outlet the fix ships through an automatic database update or a manually triggered one ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). A fourth release, GreenSection, is described only as an NVIDIA memory-corruption bug that crashes any application using Vulkan or OpenGL, rather than a privilege escalation ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)).

The releases are unco-ordinated by the researcher's own account, and the reason they give matters for timeline planning rather than attribution. The Hacker News reports the researcher claiming that Microsoft continues to ignore them and refuses to engage in "any sort of communication", and quotes them saying they "can't even report the bugs I find to their respective vendors because of the restrictions by Microsoft" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). The same reporting quotes them planning the timing of future drops: "Think I will start publishing bugs for third-parties in that window where Patch Tuesday isn't released yet" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). For a defender that means there is no embargo to wait out and no co-ordinated patch date, the gap between publication and a vendor fix is open-ended, and by the researcher's own stated intent the next drop is likelier to land in the days before a Patch Tuesday than after one.

**Defender takeaway:** an endpoint agent's own remediation logic runs at SYSTEM on every managed host, which makes a flaw in it a full-estate local privilege escalation rather than a single-host bug, and it sits precisely where a defender is least likely to be watching. Both CrowdStrike and Gen Digital are now reported to have remediated their respective flaws (see the update below): confirm every Avast Antivirus install is on 26.7.11086 fix 992, 26.8.11125 fix 993, or later, and confirm every CrowdStrike Falcon sensor is on the current release, since no CrowdStrike source names a specific fixed build to check against.

**Triage:** these exploits ride a security agent's legitimate high-privilege routines, so the signal is not the agent acting with privilege, which it always does. What separates abuse is what the privileged action produces: a remediation or sandbox operation followed by a process spawning from an unexpected parent under a low-privileged user's session, a write into a system directory that the agent's normal cleanup does not target, or SAM access originating from the antivirus process tree rather than from a backup or credential-management workflow. Because the code is public and the researcher notes detections may already exist, an endpoint alert naming the agent's own remediation component is worth treating as an exploitation attempt rather than a product fault.

## Update — 2026-09-10T05:10:00Z

LevelBlue SpiderLabs independently reproduced and analysed all four PoCs, adding mechanism-level detail none of the original vendor statements carried. HardBreacher: "every Windows logon session has a private object directory inside the kernel's namespace – \Sessions\0\DosDevices\{AuthId}\, and any standard user process can place symbolic links inside their own session's directory without any special privilege" ([LevelBlue SpiderLabs, 2026-09-09](https://www.levelblue.com/blogs/spiderlabs-blog/expanding-the-attack-surface-analyzing-nightmare-eclipses-latest-pocs)); the exploit builds a fake filesystem tree redirecting Kaspersky's `avpuimain.dll` load path to an attacker DLL, then spawns `avpui.exe` suspended with the redirect live and resumes it so the OS loader loads the malicious DLL, additionally using `NtCreateUserProcess` with the parent-process attribute set to `explorer.exe` so EDR process-tree telemetry records Explorer, not the real caller, as the parent — the payload then hides and terminates the product's user-facing notification process from inside. PrettyPrague: "the vulnerability is that a standard user process can send IOCTL 0x82AC0054 directly to the aswSnx driver to request that a chosen executable be run inside the sandbox" ([LevelBlue SpiderLabs, 2026-09-09](https://www.levelblue.com/blogs/spiderlabs-blog/expanding-the-attack-surface-analyzing-nightmare-eclipses-latest-pocs)), where the sandbox's virtualized SAM-hive copy carries none of the real SAM's ACLs; the exploit races the sandbox's own cleanup to copy the hive out via a rolled-back Kernel Transaction Manager transaction, decrypts NTLM hashes offline using the LSA boot key, and reaches a SYSTEM context through a CMSTPLUA COM-interface UAC bypass to log in as every local admin, reverting the passwords afterward. FalconFlank's precondition is narrower than the original report suggested: "for CrowdStrike clients to be susceptible to this local privilege escalation vulnerability, an endpoint must be assigned to a Prevention Policy with the 'Microsoft Office file malicious macro removal' setting enabled. This vulnerability does not impact CrowdStrike Falcon Government clients" ([LevelBlue SpiderLabs, 2026-09-09](https://www.levelblue.com/blogs/spiderlabs-blog/expanding-the-attack-surface-analyzing-nightmare-eclipses-latest-pocs)), and in LevelBlue's own lab testing, CrowdStrike's cloud-based ML engine (detection logic `OnWriteOfficeMacroMLMedium`) identified and quarantined the malicious DLL the exploit stages, preventing the final privilege-escalation step in that test run — a detection outcome that limits, without eliminating, the real-world exploitability the initial disclosure implied. LevelBlue independently characterises GreenSection differently from the original report's "memory-corruption bug that crashes any application using Vulkan or OpenGL": its own analysis describes a standard user opening, mapping, modifying and restoring an NVIDIA global shared-memory section, with no privilege-escalation or code-execution primitive demonstrated — a narrower, trust-boundary-design finding rather than a crash bug, though LevelBlue did not claim to have tested for a crash condition either.

**Defender takeaway:** LevelBlue's detection table is directly reusable for EDR/SIEM engineering: flag process-lineage anomalies on `avpui.exe` (a real caller other than the expected Kaspersky parent, or `explorer.exe` reported as parent for a process that was not user-launched), any non-Avast caller of `\\.\aswSnx`, and unexpected `CMSTPLUA`/`ICMLuaUtil` COM instantiation outside a normal UAC-elevation flow — all three are host-visible regardless of whether the specific PoC binaries are the ones seen.

LevelBlue's closing assessment also updates the patch picture this entry originally carried: "PrettyPrague demonstrated the most significant security impact prior to remediation, while HardBreacher highlighted opportunities for security-product abuse and evasion. GreenSection is primarily a security design concern, and FalconFlank's operational relevance was limited both by its configuration-dependent exposure and by rapid vendor remediation" ([LevelBlue SpiderLabs, 2026-09-09](https://www.levelblue.com/blogs/spiderlabs-blog/expanding-the-attack-surface-analyzing-nightmare-eclipses-latest-pocs)) — both FalconFlank and PrettyPrague are now reported remediated, which supersedes the "no fix"/"still developing a patch" status this entry carried at disclosure. The Hacker News's own update to its original report names a specific fix: "as of September 4, 2026, Gen has released a patch for the following versions of Avast Antivirus for Windows - 26.7.11086, fix version 992 [and] 26.8.11125, fix version 993" ([The Hacker News, 2026-09-03](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)). No source reached for this entry names a specific fixed CrowdStrike Falcon build or date for FalconFlank; confirm current release status directly with CrowdStrike rather than treating this as a version-checkable patch.
