**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T04:12:09Z · ended_at=2026-11-01T04:31:04Z · duration_seconds=1135

## Verification report — 2026-11-01T0256Z-intel (iteration 2)

Scope: all 147 ledger claims (claims.iter2.yaml; the 48 changed claims plus every other claim of all six entries; no claim sampled out), coverage 147/147 per `tools/claim_ledger.py --coverage 2`. Verdict rows: 138 ok, 7 F3, 2 F4 (verification.iter2.claims.yaml). Pages read this iteration: run bodies for Dream, Unit 42, GTIG, MSRC, Cisco (eMudhra, PHP), GitLab, Python post, tracker, vd.ch, RTS, SRF, Hunt.io, GreyNoise; everything else fetched fresh with `extract`/`url` (php.net archive from raw HTML, Python feed, tracker raw HTML, GreyNoise live page at 04:21 UTC, Wayback copy of Dream 2026-10-28, Le Temps, Oracle 91403 and 114820, OpenJDK advisories, ENISA record, Go announcement, PSIRT page and JSON, NCSC.ch post 13091 via `ncsc-csh`, CISA KEV via `cisa-kev`, CISA alert via WebFetch).

### Iteration-1 remediations (deltas block)

All remediations check out except where a new finding below says otherwise.
- PAN-OS tunnel: text now "on the second of two firewalls ... (the first crashed)"; Dream: first firewall "crashed shortly after ... and never came back online", tunnel on the second. Confirmed.
- eMudhra Python/tracker: Exposure, cves[CVE-2026-115557].fixed and action 1 name 3.15.2, 3.14.10, 3.13.18, 3.12.16, 3.11.18 (Python Insider, feed pubDate Mon, 26 Oct 2026); tracker 28 October update and pending list (Bottlerocket, OpenHarmony/HarmonyOS, certbot, containerd, Godot, LibreOffice) confirmed on the raw tracker HTML. New defect: the CVE's status was not moved (finding 2).
- PHP main text: "all twenty hotfixes" is true on the live PSIRT page and Cisco 26.2.1.9 (Nov 2026) matches v1.10 (2026-OCT-30); the Palo Alto label date is off (finding 5).
- ARTEX summary: now ties extortion and PRC-nexus adoption to ARTEX only; GTIG: "ARTEX has been adopted ... financially motivated extortion groups and suspected cyber espionage operators", "additional suspected PRC-nexus clusters". Confirmed.
- Vaud: whole entry read against vd.ch and RTS; "no context, reason or objective known" is RTS ("On ne connaît ni le contexte, ni les raisons, ni les objectifs de ce vol"); shape matches the incident floor (two sentences plus relevance clause, Detection, Defender takeaway). Le Temps and SRF relay the release only (read both). Confirmed.
- DCTL in action 2/takeaway: DCTL of 2026-10-20 is MSRC's; the out-of-band-update half is finding 6.
- PHP Dream label 2026-10-29 in the main text: confirmed. Detection: PAN-OS "about 900 MB" is Dream's (hedge "likely from" dropped, harmless). Vaud Detection: derivation now marked "would appear". Run-record Hunt.io note: corrected, but a sibling bullet is now stale (finding 4).
- GlobalProtect: the Exposure line states both statements accurately; the record summary overstates (finding 3).
- eMudhra depth restored (P-384, values below 256, both checkRevocation flags, macOS note): confirmed against BleepingComputer, OpenJDK page, tracker. Threat ID 543004 clause: present in the hotfix paragraph, conditions match the advisory.
- FU1 additions: GreyNoise first success 28 Oct 2026 05:14:01 UTC, 1,177 confirmed from 5 attacker IPs (still 1,177 on the live page at 04:21 UTC), Hunt.io dated 2026-10-30 (page timestamp 2026-10-30T14:38Z), evidence quotes verbatim; location and date detail wrong (finding 1).
- Classification credibility 2 (PAN-OS), campaign keys on both entries, T1090 and the other mapped ids: supported by Dream; keys exist in the registry.

### Citation does not support the claim

1. **F3 — PHP main entry, Detection line, Update 2026-11-01T04:10:00Z and its record summary** ("create a .ssh directory under the web root"; "downloads of enumeration and secret-scanning tools that were run over the web root"; https://php.events.greynoise.io/). GreyNoise's rows show `mkdir -p /var/www/.ssh` and `chmod 600 /var/www/.ssh/authorized_keys`: the web user home, beside the document root `/var/www/html` that the scanners are pointed at (`gitleaks dir '/var/www/html'`), not under it. The scanner runs (`gitleaks dir` over /var/www/html, /srv, /home, /opt, /root, /etc) appear only in sessions of 2026-10-31; the 2026-10-29 sessions show reverse shells, metadata queries, the downloads of gitleaks and linpeas and a deep-loot script. The follow-up note FU1 says "under the web user home (/var/www/.ssh)". A hunter told to look under the web root misses the path. Fix the wording and move the scanner runs to 2026-10-31.
2. **F4 — eMudhra cves[CVE-2026-115557]**: `status: ["mitigation-only"]` against `fixed: "Python 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 carry the ssl denylist"`; the Python post lists CVE-2026-115557 in "Security content in all five releases". Set `patch-available`.
3. **F4 — PAN-OS changelog record summary**: "Dream and Palo Alto differ on whether GlobalProtect shares the affected web server." The advisory says only "GlobalProtect portal, gateway and Clientless VPN are not impacted" and "strictly affects the management web interface"; the update section does not mention GlobalProtect. The Exposure line is accurate; reword the record.
4. **F4 — run record notes**: "Dream says ... fronts the GlobalProtect portal ... the entry carries Palo Alto's statement only" contradicts the next bullet ("The PAN-OS entry states both, attributed") and the entry's Exposure line.
5. **F3 (low confidence) — PHP main body paragraph 2**: "with all twenty hotfixes released ... ([Palo Alto Networks, 2026-10-29])". The entry's own 2026-10-29 section says the 10-29 read "lists all PAN-OS hotfixes as released except 11.1.7-h12"; the vendor timeline removes that ETA at 2026-10-29T23:54Z. The URL supports the claim today, but the PHP entry has no 2026-10-30 PSIRT source record; add one and cite it.
6. **F3 (low confidence) — eMudhra actions[1] and Defender takeaway**: "deliver the Disallowed Certificate Trust List of 2026-10-20 and Microsoft's out-of-band update of 2026-10-26 to Windows devices that do not receive automatic certificate-trust updates". MSRC says "the updated Disallowed Certificate Trust List and the upcoming trust-list changes"; it does not name the out-of-band update.
7. **F3 (low confidence) — Fragnesia summary**: "25 Palo Alto Networks PAN-OS ... (Dream Research, 2026-10-27)": the PAN-OS naming and the count of 25 are in Dream's version updated 2026-10-29 (the Wayback copy of 2026-10-28 names no vendor). Relabel.

### Needs more research

8. **F8 (and missed angle) — eMudhra, CVE-2026-114820**: Oracle's alert (https://www.oracle.com/security-alerts/alert-cve-2026-114820.html) carries "2026-October-30 | Rev 2. Added Oracle Autonomous Health Framework, Oracle Database Serve[r], Oracle Global Lifecycle Management OPatch, Oracle Hospitality Cruise Shipboard Property Management (SPMS)": Oracle Database Server RDBMS (Java) 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 (not applicable to client-only installations), Trace File Analyzer 26.3-26.10, OPatch 12.2.0.1.16-12.2.0.1.52 and Hospitality SPMS 23.3.4-23.3.6, each remotely exploitable without authentication, CVSS 3.1 9.1. The entry (cves[].affected, affected_products, the 2026-11-01 section) lists only Java SE, GraalVM and OpenJDK. The tracker's Java row also names fixed Oracle JDK builds 27.0.1.0.3, 25.0.5.0.3, 21.0.13.0.3, 17.0.21.0.3, 11.0.33.0.3, 8u511 b33 and "Pending for OpenJDK", while the entry's fixed field says "build numbers in Oracle's Patch Availability Document" and action 1 says "or the OpenJDK update". Suggested search: `Oracle Security Alert CVE-2026-114820 Rev 2 Oracle Database patch availability`.
9. **F8 (low) — PAN-OS Exposure**: Dream states the attacker's target list was filtered to "the PAN-OS 12.1 and 12.2 branches running PHP 8.0.30" (11.1 on PHP 7.4.33 provisional); one clause gives the compromise check a priority order.

### Action-item discipline

10. **F18 (low confidence)**: PAN-OS action 2 depends on "the web-shell, persistence and outbound-SSH checks" defined only in the Detection line and repeats the Defender takeaway's rotation sentence; eMudhra action 1 bundles seven products plus a verification step and repeats the takeaway's "update trust bundles and toolchains ... rebuild container images".

### Editorial / less-is-more flags (advisory)

11. **F11** — PHP Update 2026-11-01T04:10:00Z, Hunt.io paragraph: Hunt.io's sentence continues "but php2shell has been used to root internet-facing PAN-OS firewalls, the first confirmed production compromises"; the entry drops it and does not say Hunt.io relays Dream and Unit 42 in the section (the sourcing note does).
12. **F11** — record summaries narrate field edits ("the summary, chain description, appliance action and sourcing note now name it"; "Two actions are rewritten ... the Cisco remediation list follows version 1.5").
13. **F11** — PAN-OS record names `classification` in `fields` although A/2 equals HEAD.
14. **F11** — Fragnesia: record typed `improvement` carries a new sourced fact and the 2026-10-29 section still says "does not name the vendor" without a supersession sentence (the PHP entry has one).

### Checked and clean

Relevance and priorities (PAN-OS high, PHP critical, Fragnesia high, eMudhra and ARTEX notable, Vaud routine) hold; Admiralty codes consistent with sourcing (vd-ch-press-releases is reliability A in sources.json); `updated_at` mirrors the `at` of each non-internal update record and is untouched by the improvement; no IOCs, em dashes or workflow vocabulary in entry prose; new Vaud entry is not covered by prior_coverage or the registry; the KEV window sweep agrees (catalogVersion 2026.10.30, newest additions covered, checked with `kev_window_diff.py`); no other missed critical/high item found beyond finding 8.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 3, advisory: 4)

### Findings summary (machine-readable)

See work/2026-11-01T0256Z-intel/verification.iter2.findings.yaml
