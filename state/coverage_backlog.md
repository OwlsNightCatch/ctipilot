# Coverage backlog — verified, relevant, not yet published

**What this is.** A short, hand-maintained queue of items the pipeline has already *researched and verified* but never published, because the fire that surfaced them could not publish (a `duplicate-week` stand-down, an abandoned sub-agent whose findings survived, a watchdog cut). Without this file such items are unreachable: the next intel run's window is 24–26 h and the next weekly's is the following ISO week, so both recency gates put a verified item from last week permanently out of scope. The 2026-08-03 weekly stand-down listed nine of them in its run-record body and **not one was ever published** — that is the hole this file closes.

**Who writes it.** Any run that verifies a relevant item it cannot publish: the weekly's stand-down procedure (`prompts/weekly-summary.md` Phases 5→7), and any fire whose watchdog or sub-agent abandonment leaves verified findings on the floor. Narrate the items in the run record *and* append them here — the record is prose nothing consumes, this file is the queue.

**Who reads it.** Every intel run, in Phase 0. Backlog items are **exempt from the recency gate** — they carry their own `event_date` and were verified in-window by the fire that surfaced them; the reason they are unpublished is a pipeline race, not staleness. Everything else applies unchanged: they go through the relevance gate (PD-11) on today's facts, dedup, composition discipline, the mechanical gate and the verifier loop, exactly like any other candidate.

**Working it down.** A run publishes what still clears the gate today and strikes those rows (`~~struck~~` with the publishing entry id). A run that judges an item no longer worth publishing strikes it with a one-clause reason. Do not silently drop a row, and do not let the file grow without bound — an item still open after ~30 days is either published or struck with a reason.

## Open

| Surfaced | By run | Item | Why it clears the gate | Primary source | Event date |
|---|---|---|---|---|---|
| 2026-08-10 | 2026-08-10T0411Z-intel | **1Password Off-by-1 Labs "FLAWED" study** — 54% of 6,080 LLM-generated patches across six CVEs failed to fully remediate or introduced new bugs | PD-11(d), marginal. Judged a borderline drop by this run: the finding is a study statistic about AI-assisted patching rather than tradecraft a Tier 2/3 responder acts on, and the pipeline has already published a concrete instance of the same lesson (an assurance review that missed a five-year key-generation defect). Retained here rather than discarded because a future fire covering AI-assisted remediation practice may want it as supporting material. Strike it if it is still unpublished after ~30 days. | 1password.com/blog/why-ai-generated-patches-still-require-human-review | 2026-08-06 |

## Struck

_All fifteen rows open before this run were resolved by `2026-08-10T0411Z-intel`, which drained the backlog: fourteen published, one struck on relevance. The Retelit row was opened and closed inside the same run — see the last row._

| Surfaced | Item | Resolution |
|---|---|---|
| 2026-08-10 | **Retelit (Italy)** — Qilin extortion against an Italian telco/cloud operator serving 193 public administrations | ~~published~~ as `2026-08-10/retelit-qilin-italian-telco-cloud-operator-public-sector` — opened as a backlog row by this run, then published within the same run after the verifier flagged the deferral as inconsistent with the three recovered coverage gaps this run did publish |
| 2026-08-03 | CERT Intrinsec two-part DFIR artefact map for autonomous coding agents | ~~published~~ as `2026-08-10/coding-agent-forensic-artefacts-opencode-codex-credentials` |
| 2026-08-03 | Intrinsec Enterprise LLM Threat Atlas | ~~struck~~ — does not clear the relevance bar: a methodology and reference document restating widely known LLM threat categories, whose own risk ranking is unquantified in the reachable text; no change to what a highly skilled responder detects, hunts or hardens |
| 2026-08-03 | Group-IB PAM-as-anti-forensics intrusion (`pam_rootok`) | ~~published~~ as `2026-08-10/pam-rootok-identity-shuffle-as-anti-forensics-xmrig` |
| 2026-08-09 | Wazuh 4.14.6 ten-flaw cluster | ~~published~~ as `2026-08-10/wazuh-4-14-6-cluster-root-rce-preauth-authd-overflow` — the CVE-to-GHSA pairing that blocked the surfacing audit was resolved by reading each id off its own advisory record and cross-checking BSI's independent list |
| 2026-08-09 | GOLD EMBRACE / Interlock weaponise Volatility3 and WinPmem | ~~published~~ as `2026-08-10/interlock-volatility3-winpmem-credential-theft` |
| 2026-08-09 | CrowdStrike: command obfuscation in VMware ESXi's BusyBox `ash` | ~~published~~ as `2026-08-10/esxi-busybox-ash-command-obfuscation-21-techniques` |
| 2026-08-09 | Rapid7 on CVE-2026-66066 (Rails ActiveStorage) | ~~published~~ as `2026-08-10/cve-2026-66066-rapid7-metasploit-module-weaponisation` — **with a correction to this row's own framing**: Rapid7 claims no in-the-wild exploitation; the delta is its public Metasploit module and reproduction, i.e. weaponisation, not an exploitation-status change |
| 2026-08-09 | Zscaler ThreatLabz TELESHIM Part 2 (BINDCLOAK) | ~~published~~ as `2026-08-10/bindcloak-rtlqueueworkitem-reflective-loading`, as an update on the Part 1 entry already in the store |
| 2026-08-09 | Żabka (Poland) supplier-account intrusion | ~~published~~ as `2026-08-10/zabka-supplier-account-jira-access-confirmed` — composed strictly on Żabka's confirmed facts, with the Jira→GitLab→production pivot attributed to the forum seller and the outlet's own stated guess |
| 2026-08-09 | FreeBSD CTL HA pre-auth remote kernel RCE trio | ~~published~~ as `2026-08-10/freebsd-ctl-ha-three-preauth-kernel-rce-primitives-port-999` (this run's deep dive); FreeBSD's own commit was located, making it multi-source, and confirms documentation rather than a code fix |
| 2026-08-09 | wp2root | ~~published~~ as `2026-08-10/wp2root-php-uaf-copy-fail-kev-kernel-lpe-to-native-root` — CVE-2026-31431 resolves on NVD and MITRE and is additionally CISA KEV-listed since 2026-05-01 with EPSS 0.999, a fact no prior fire had surfaced |
| 2026-08-10 | XSS2Shell (CVE-2026-64638), WordPress Core | ~~published~~ as `2026-08-10/wordpress-core-xss2shell-cve-2026-64638-preauth-xss-to-rce`; confirmed technically distinct from the tracked WP2Shell chain |
| 2026-08-10 | CVE-2026-33824 root cause (`ikeext.dll`) | ~~published~~ as `2026-08-10/cve-2026-33824-ikeext-double-free-root-cause-published`, single-source for the root cause with Microsoft's own record corroborating the CVE, CWE and affected range |
| 2026-08-10 | Connor Moucka / UNC5537 guilty plea | ~~published~~ as `2026-08-10/unc5537-moucka-guilty-plea-saas-tenant-extortion-template`, with the DOJ-versus-Krebs attribution split verified directly and preserved per fact |
| 2026-08-10 | Forescout water-sector controller census | ~~published~~ as `2026-08-10/forescout-rockwell-plc-exposure-census-cellular-carrier-path` — both primaries were reached directly this run, so the relay caveat no longer applies |
