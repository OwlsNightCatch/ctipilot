# W1 Research Notes — 2026-W20 (Long-horizon ongoing + Annual/Periodic Reports)

**Run id:** 2026-W20-71c96b25
**Domain:** W1
**Window:** 192 hours (Mon 2026-05-11 → Sun 2026-05-17)
**Researcher model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Started:** 2026-05-17T22:12:01Z

---

## Summary

11 items returned: 7 status-updates on "Looking Ahead" items from W19, 2 campaign-status updates on items already in the W20 daily coverage, 2 annual/periodic reports.

---

## § 1 — LOOKING AHEAD STATUS UPDATES

### UPDATE: PAN-OS CVE-2026-0300 — Wave 2 delay confirmed 2026-05-28

The Palo Alto Networks PSIRT advisory was updated on 2026-05-16, confirming the two-wave patch schedule. Wave 1 shipped on 2026-05-13 for the majority of actively-exploited branch hotfixes. Wave 2 (ETA 2026-05-28) still outstanding for PAN-OS 12.1.7, 11.2.4-h17, 11.2.12, 11.1.7-h6, 11.1.15, 10.2.7-h34, 10.2.13-h21, and 10.2.16-h7.

**Workaround status (unchanged):** Restrict User-ID Authentication Portal to trusted zones; disable Response Pages on external-facing L3 interface management profiles; Threat Prevention subscribers can block via Threat ID 510019 (content >= 9097-10022, requires PAN-OS >= 11.1).

**Source:** [Palo Alto Networks PSIRT CVE-2026-0300](https://security.paloaltonetworks.com/CVE-2026-0300) — updated 2026-05-16

---

### UPDATE: Canvas/Instructure — Ransom paid, Congressional investigation launched

Instructure confirmed payment to ShinyHunters (ransom amount undisclosed; ~$10M unconfirmed). Agreement terms: data return + digital confirmation of destruction + no customer extortion. Despite this, ShinyHunters subsequently defaced ~330 Canvas institutional login pages by exploiting the same Free-For-Teacher account vulnerability. House Homeland Security Committee Chairman Garbarino requested CEO briefing by 2026-05-21 — outcome expected this coming week.

**Sources:**
- [The Record — Instructure pays ransom, Congress investigation](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation) (2026-05-12)
- [House Homeland Security Committee letter](https://homeland.house.gov/2026/05/11/chairman-garbarino-seeks-information-from-canvas-developer-after-cyberattacks-impact-schools-and-universities-nationwide/) (2026-05-11)

---

### UPDATE: "The Gentlemen" RaaS — Operations continue; decryptor published; Fortinet/Cisco CVEs confirmed as initial access

Administrator zeta88/hastalamuerte responded to the May 4 Rocket DB leak (hosting provider 4VPS breach) by announcing a full comms-infrastructure overhaul — NOT cessation of operations. The nine-person core structure remains intact. ~332 victims in H1 2026.

**New in window:** Bedrock Safeguard (Canada) published a decryptor on ~2026-05-14 exploiting Go's failure to zero XChaCha20/X25519 ephemeral private key material from goroutine stacks — 35/35 files decrypted. Operator claims to have patched the binary.

**Confirmed initial access CVEs:** CVE-2024-55591 (FortiOS mgmt interface auth bypass), CVE-2025-32433 (Erlang SSH). Post-access: RelayKing NTLM relay (CVE-2025-33073), AD enumeration, EDR disable, GPO locker deployment.

**Sources:**
- [Check Point Research — Thus Spoke The Gentlemen](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/) (2026-05-14)
- [Bedrock Safeguard decryptor](https://github.com/Bedrock-Safeguard/gentlemen-decryptor)

---

### UPDATE: Dirty Frag CVE-2026-43284/43500 — Major distros patched; CVE-2026-43500 (RxRPC) patch still lagging

AlmaLinux 8/9/10 patched. AlmaLinux 8 not affected by CVE-2026-43500 (rxrpc module not built). RHEL errata rolling; Ubuntu, Debian, Fedora, openSUSE acknowledged. KernelCare livepatches available for CVE-2026-43284. CVE-2026-43500 patches slower — only affects systems with kernel-modules-partner installed.

**Sources:**
- [AlmaLinux blog](https://almalinux.org/blog/2026-05-07-dirty-frag/) (2026-05-07)
- [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/08/active-attack-dirty-frag-linux-vulnerability-expands-post-compromise-risk/) (2026-05-08)

---

### UPDATE: CVE-2026-31431 "Copy Fail" — Patched in major distros as of 2026-05-01; RHEL outstanding at publication; CISA KEV deadline 2026-05-15

Patches in Ubuntu, Debian, AlmaLinux, SUSE, Fedora, CloudLinux (KernelCare K20260501_02). RHEL errata were outstanding at time of daily coverage. No new exploitation developments in this window.

---

### UPDATE: MOVEit Automation CVE-2026-4670 — No ITW exploitation confirmed

As of 2026-05-17 no confirmed in-the-wild exploitation. Patches available (2025.1.5, 2025.0.9, 2024.1.8). 1,400+ internet-exposed instances. Risk remains elevated given MFT historical exploitation patterns.

---

### UPDATE: SEPPmail CVE-2026-44128 — CIRCL advisory confirms CVSS 9.3 unauthenticated Perl eval RCE; no third-party write-up in window

CIRCL (Luxembourg national CERT operator) hosts the canonical advisory. Affected: < 15.0.2.1. CWE-95 eval injection in GINA UI. Patch to >= 15.0.2.1. No independent PoC or root-cause analysis published in window.

**Source:** [CIRCL vulnerability.circl.lu](https://vulnerability.circl.lu/vuln/cve-2026-44128) (2026-05-08)

---

## § 2 — CAMPAIGN STATUS UPDATES (from W20 daily context)

### UPDATE: Secret Blizzard / Turla Kazuar — Corroborated; Europe confirmed in scope

Two independent sources (Microsoft 2026-05-14 deep-dive + The Record) corroborate the modular P2P botnet architecture (Kernel/Bridge/Worker modules, leadership election, multi-channel C2: HTTP/WebSocket/EWS). European government, diplomatic, and defense sectors explicitly in scope. No named European victims disclosed publicly.

Detection focus:
- Anomalous Windows Mailslot/Messaging IPC to system processes
- EWS protocol access from non-mail-client processes
- Exchange Web Services enumeration events

**Sources:**
- [Microsoft Security Blog — Kazuar anatomy](https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/) (2026-05-14)
- [The Record — Turla/Ukraine](https://therecord.media/turla-secret-blizzard-russia-espionage-ukraine-cybercrime-tools) (2026-05-14)

---

### UPDATE: FrostyNeighbor / Ghostwriter (UNC1151) — ESET corroborated by THN; EU scope (Poland, Lithuania)

ESET's primary research (2026-05-14) corroborated by The Hacker News. Attack chain since March 2026: spearphish Ukrtelecom PDF → RAR → JS PicassoLoader → server-side geo-validation → Cobalt Strike. Persistence: scheduled tasks + registry. Polish targeting via CVE-2024-42009 Roundcube XSS (CERT.pl confirmed). EU victim scope: Poland, Ukraine, Lithuania governments and industrial/healthcare/logistics sectors.

---

### UPDATE: Mini Shai-Hulud / TeamPCP — Source code leaked; IDE persistence hooks newly documented

Shai-Hulud source code (TypeScript/Bun) briefly published on GitHub 2026-05-12. Datadog Security Labs analysis (2026-05-13) surfaces new IDE persistence vectors via `.claude/settings.json` and `.vscode/tasks.json` hooks — allowing arbitrary command execution on developer workspace events. GitHub Actions OIDC token extraction from `/proc/<pid>/mem` allows provenance forgery (Sigstore attestation bypass). 172 packages / 403 malicious versions compromised in wave 4.

Detection filesystem indicators:
- Repos named "Shai-Hulud: Here We Go Again"
- `gh-token-monitor` daemon process
- `.claude/settings.json` with unexpected hook entries
- Commits from `claude@users.noreply.github.com` in unexpected repositories

---

### UPDATE: Qilin — April 2026 data: leading RaaS operator (15% of global attacks); Germany 5% of victims

Check Point April 2026 report confirms Qilin leads. Germany third-most targeted country globally. Die Linke (German political party) confirmed March 2026 Qilin victim. Europe at 27% of global ransomware victims. Sophos Active Adversary Report 2026 (Feb 2026) places Qilin at 11.06% of IR cases (second behind Akira at 22.58%).

---

## § 3 — ANNUAL / PERIODIC REPORTS

### Sophos State of Identity Security 2026 — Published 2026-05-15

**Coverage window:** Q1 2026 survey, 5,000 IT/security leaders, 17 countries, 14 industries, orgs 100–5,000 employees.

Key operational findings for defenders:
- **71%** of organisations experienced identity breach in past year (avg 3 incidents)
- **67%** of ransomware victims: incident directly tied to identity attack
- **41%** of successful identity breaches root-caused to weak non-human identity (NHI) management
- **34%** of organisations regularly audit NHI accounts (service accounts, API keys, AI agents)
- **$1.64M** average breach remediation cost
- NHI/human identity ratio up to **100:1** in surveyed organisations

Corroborates Sophos Active Adversary Report 2026 (Feb 2026): identity-rooted initial access in 67% of 661 IR/MDR cases; Impacket tool usage surged 83% YoY; Akira (Gold Sahara) 22.58% ransomware share, Qilin (Gold Feather) 11.06%.

**Sources:**
- [Sophos State of Identity Security 2026](https://www.sophos.com/en-us/blog/sophos-state-of-identity-security-2026) (2026-05-15)
- [Sophos press release — 71%](https://www.sophos.com/en-us/press/press-releases/2026/05/71-percent-organizations-suffered-identity-breach-state-of-identity-security-2026)

---

### Verizon DBIR 2026 (19th annual) — Page live, PDF pending (webinar 2026-05-19)

The 2026 DBIR page is live on Verizon's site (updated within 2 weeks of 2026-05-17). Full PDF not yet publicly downloadable. Webinar scheduled 2026-05-19, 11 AM ET.

Confirmed headline figures (from DBIR page FAQ and pre-release coverage):
- **Third-party involvement:** 30% of breaches (doubled from ~15% in prior edition)
- **Ransomware:** 44% of breaches
- **Stolen credentials:** 22% — single most common initial access vector
- **Vulnerability exploitation:** 20% — approaching credentials as top initial access
- **Human element:** 60%+ of breaches
- Dataset: incidents Nov 2024 – Oct 2025 (largest DBIR dataset)

**Key relevance for CH/EU public sector:** The third-party doubling to 30% directly maps to NIS2 Article 21/21 third-party risk management obligations and DORA supply-chain requirements for EU-licensed financial entities. Swiss FINMA expects equivalent third-party governance.

**Source:** [Verizon DBIR 2026](https://www.verizon.com/business/resources/reports/dbir/) — Note: full report PDF not yet available; update after 2026-05-19 webinar.

---

## Campaigns checked — no new developments in window

- **Sandworm/GRU Unit 74455 Bauman pipeline:** No new sanctions announcements or follow-up analysis found in window beyond the original May 2026 investigative consortium publication. The 2,000-document cache is still being digested by analysts — vsquare.org and theins.press had follow-up pieces but all pre-dated the W20 window.
- **APT28 / CVE-2026-32202 PatchDiff-AI incomplete patch:** Exploitation confirmed active as of 2026-04-27 (CISA KEV); no new exploitation reporting in this week's window beyond what was already in dailies.
- **CVE-2024-55591 (Fortinet long-running):** No new exploitation campaign reporting in window; already documented as The Gentlemen initial access above.
- **UAT-8302 (edge-device/SD-WAN):** No new movement found.
- **MuddyWaterChaos false-flag:** No corroboration found in window.
- **Akira Swiss-healthcare:** No new Swiss victim named in window beyond Groupe 3R (2026-05-10 daily).
- **ENISA Threat Landscape 2026:** Not published; most recent is ETL 2025 (Oct 2025, published Jan 2026). No 2026 edition announced.
- **CrowdStrike Global Threat Report 2026:** Published 2026-02-24 — outside the 192-hour window and already covered in W19 context. No new analysis pieces in window.

---

## Fetch failures (none qualifying under v2.55 criteria)

No sources returned a real unrecovered failure. The brighttalk.com webinar page for Verizon DBIR returned HTTP 403 — but coverage was obtained via the Verizon DBIR page directly. The Verizon DBIR full PDF is not yet released (not a fetch failure — it simply hasn't been published).
