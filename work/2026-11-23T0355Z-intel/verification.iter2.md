**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-23T04:58:52Z · ended_at=2026-11-23T05:14:21Z · duration_seconds=929

## Verification report — 2026-11-23T0355Z-intel (iteration 2)

Scope: 3 new entries, 1 updated entry (nginx2root, improvement record 2026-11-23T04:35:59Z; `git diff HEAD` shows only the five added `cves[]` records, the `updates[]` record and the section, `updated_at` untouched), run record, registry tail. Post-fix pass: all 84 ledger claims walked (84/84 rows in verification.iter2.claims.yaml; `claim_ledger.py --coverage 2`: 84/84, 0 missing), including every changed claim (23) and every other claim of all four remediated entries. Pages read this iteration with `extract`: GL.iNet notice, BleepingComputer, RemoteToHome repo, pwn.ai, The Hacker News (Ghostscript), VulnCheck, Debian tracker, Kaspersky part 1 and part 2, Sophos, nginx.org advisories, NCSC-NL NCSC-2026-0506, Fortinet FG-IR-26-279, CERT-EU 2026-022, Rapid7, Wiz, Xint, Rapid7 PoC repo, CERT.at; NCSC.ch hub post 13203 via `ncsc-csh post`; CVE record JSON for CVE-2026-125396 (assigner VulnCheck); `cisa-kev` (catalog 2026.11.20, no addition); Artifex release page (dated 2026-09-08).

### Prior-iteration deltas (all 16 checked against the pages)

1. GL.iNet summary and first clause (F3): fixed. The notice reads "a vulnerability in its cloud remote management services" and never names GoodCloud; BleepingComputer: "Its GoodCloud platform allows customers to remotely manage supported devices". Summary now says "(GoodCloud, per BleepingComputer)" and the body attributes the name to BleepingComputer.
2. ShadowCloud takeaway citation (F3): fixed. It now cites part 1, which carries "The exact entry point that let the attackers install the agent is unknown".
3. "signed" (F4): fixed. grep finds no "signed" in the entry; the CEF helper is gone from Detection.
4. "active since early 2026" (F4): fixed. Summary says "identified in early 2026"; part 1: "In early 2026, we identified a new, active intrusion campaign".
5. Title "entering through" (F4): fixed. Title says "delivered through"; part 1 shows the operators using the agent "to drop three additional items".
6. nginx added CVE records (F4, low): type is null for the three classes no source names (118899, 123640, 120993). Vector `zero-click` and auth `pre-auth` remain the entry's inference; `site/taxonomy.yaml` says content_model refuses records that omit vector or auth, so the main agent's reason for keeping a value holds, and the values are plausible for request and connection handling flaws. Accepted, no finding.
7. GL.iNet Exposure token and condition (F5): fixed. The condition is RemoteToHome's ("If your router or KVM had GL.iNet's cloud service switched on, check it now") and cited. See advisory #5 on the wording "any".
8. nginx CVSS (F8): fixed and verified. NCSC-NL: 118899 8.7, 120967 6.3, 120993 6.9, 123640 6.9, 125283 6.9, all "CVSS (v4)"; entry and section match.
9. GL.iNet older backdoor and December 2025 timestamps (F8): fixed and verified. RemoteToHome: "A separate, older backdoor ... GL.iNet's check does not find it"; BleepingComputer: "Some of the malicious files recovered from GL.iNet devices had timestamps dating to December 2025".
10. Ghostscript USN-8949-1 (F9): fixed and verified. pwn.ai: "The notice predates the CVE assignment, so it labels this finding 'No CVE number.'"
11. GL.iNet credibility (F17): now 2; consistent with the vendor-versus-RemoteToHome disagreement and the unconfirmed root cause.
12. GL.iNet actions (F18): reduced to one task, but see finding #1 below.
13. GL.iNet Detection indicators (F11): state file and firewall chain are behavioural now; the vendor's process-string check remains (advisory #2).
14. sourcing_note length and KVM citation (F11): GL.iNet and Ghostscript notes are two sentences each; the KVM build numbers now cite RemoteToHome, which lists them ("KVMs: RM1, RM1V2, RM10, RM10RC, RM1PE, RM4PE: 1.10.3. RMQ1: 1.8.7."). The ShadowCloud note is three sentences, all provenance; no finding.
15. ShadowCloud entities, `actor:famoussparrow` (F11): decline accepted. Part 2 states overlap only ("While this does not prove a direct link"); the registry edge exists; keying would feed ShadowCloud techniques into the actor's TTP profile.
16. nginx closing sentence (F11): fixed. "Updating to 1.31.9 or 1.30.7 covers all ten" cites nginx.org, which lists 1.30.7+ and 1.31.9+ as not vulnerable for nine and 1.31.9+ alone for CVE-2026-120993 (vulnerable 1.31.4 to 1.31.8, so the 1.30 branch was never affected); the section says so in the same paragraph.

Remediations introduced no new truth defect. Quote-literal: spot-checked all GL.iNet, Ghostscript and ShadowCloud evidence quotes against the pages (verbatim); nginx.org dateline caveat is already in the entry's sourcing_note.

### Dedup and coverage

No overlap of the three new entries or the five added nginx CVE ids with the prior-coverage index, `state/cves_seen.json` (before this run) or existing entries; registry additions match the run record (six entities, eleven products; all keys resolve). The run record's claims about earlier fires dropping ShadowCloud (2026-11-18, -20, -21, -22 records) hold. KEV: `cisa-kev` live catalog 2026.11.20, `kev_window_diff` zero additions in window. Missed angles: none evidenced. A search for exploited zero-days and Swiss federal incidents surfaced only items dated 2026-11-16 or earlier (covered by earlier fires) and nothing in the 2026-11-22/23 window; coverage looks complete for a quiet window.

### Action-item discipline

- **#1 (F18, low confidence) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix — actions[0]**
  - Quote: "Inventory every GL.iNet router and Comet KVM your organisation or its remote and branch users run and install the security firmware for its exact model, because GL.iNet confirms exploitation and its cloud fix does not clean devices that are already infected."
  - RemoteToHome (https://github.com/RemoteToHome-io/gl-security-incident-2026): "If your router or KVM had GL.iNet's cloud service switched on, check it now, before you reboot or upgrade it. Some traces only exist until the next restart." and, for KVMs, "It keeps no copy, so upgrading an infected KVM removes the evidence." The vendor says to install the firmware "even if the checks below find no signs of infection". The action, shown alone in the aggregated Action Items, upgrades first with no check-and-capture step, and the Defender takeaway lists "install the security firmware" before "capture the process list, connections and firewall rules before any restart". Fix: word the action as a check of each device with evidence capture before the firmware install restarts it, and state in the takeaway that the vendor and RemoteToHome differ on sequence.

### Editorial / less-is-more flags (advisory)

- **#2 (F11) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix — Detection:** literal process string and path indicator `crond -i /tmp/.log` stays (house rule: no file-name indicators). Raised in iteration 1 and kept deliberately as the vendor's published check; may leave.
- **#3 (F11, low confidence) ghostscript-cve-2026-125396-upload2shell-sandbox-escape — cves[].vector: local.** docs/pipeline.md: `vector` encodes the victim-interaction requirement ("zero-click = attacker-initiated, no victim interaction"). `local` copies CVSS AV:L (VulnCheck: CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P), while pwn.ai shows anonymous CUPS and public WordPress form paths with no interaction and a Roundcube path that needs only a message view. A triage agent reads `local` beside `auth: pre-auth`. Consider `zero-click`.
- **#4 (F11) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2:** the Exposure line has no inline citation (derived claim 24de50cd66; consistent with Kaspersky). The sentence "Sophos, which tracks the Sandboxie sideloading as BRONZE SANDCASTLE, saw victims ..." cites Sophos only; Kaspersky's statement that links it to this campaign ("In a recent brief, Sophos touched on a fragment of this campaign") is in the summary and sourcing_note but not in the body prose.
- **#5 (F11, low confidence) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix — Exposure:** "any GL.iNet router or Comet KVM" is wider than the cited sources (a model-specific list plus "An unlisted model is not necessarily unaffected"; RemoteToHome's reading is GoodCloud-enabled devices).

### Verdict

NEEDS_FIXES (truth: 0, editorial: 1, advisory: 4)

The only numbered defect is finding #1, low confidence and a one-line rewording. Every truth claim in scope (84 of 84) was confirmed against pages fetched this iteration, and none of the prior-iteration remediations introduced a truth defect. If the main agent judges finding #1 a matter of taste, it is the only thing between this output and CLEAN.

### Findings summary (machine-readable)

See work/2026-11-23T0355Z-intel/verification.iter2.findings.yaml (5 records: one F18, four F11).
