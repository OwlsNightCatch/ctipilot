**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-10T04:49:20Z · ended_at=2026-07-10T04:59:52Z · duration_seconds=632
**Self-telemetry:** webfetch_calls=11 · websearch_calls=0 · bridge_fetches=7 · urls_checked=15

## Verification report — 2026-07-10T0409Z-intel (iteration 1)

Cold read of all 6 new entries + run record. Every inline source URL fetched (WebFetch, escalated to jina/bridge where a host 403'd/404'd to the routine UA). All evidence[] quotes checked as contiguous verbatim substrings against the actual pages; frontmatter⇔body agreement, techniques mapping, priority/classification calibration, dedup/update decisions, and the out-of-nexus inclusion all reviewed.

### Citation does not support the claim
None. (One candidate — the CitrixBleed Sophos QEMU cross-reference — checked out: the Sophos post DOES name STAC3725 exploiting CitrixBleed2/CVE-2025-5777 alongside NetScaler/ScreenConnect/Netbird/Impacket. The e-gov "SentinelLabs attributes ... to Bitter (Remcos/PlugX/ShadowPad/Cobalt Strike)" clause carries an Express Tribune anchor, but the prose explicitly credits SentinelLabs and the SentinelLabs primary — cited on the entry — fully supports every named entity; Express Tribune corroborates the broad framing. Not a defect.)

### Unsupported / hallucinated facts
**F4 — nextcloud-gmbh-elasticsearch-exposure-msb-nrw — evidence quote mis-attributed (relabel, not fabrication).**
Frontmatter evidence[] record: quote "The issue was caused by a misconfiguration of our hosting infrastructure and is not related to the Nextcloud solution. No other Nextcloud servers belonging to our customers, partners or other users have been affected by this issue." — publisher: "heise online".
The heise page does NOT contain this string. heise's actual wording (fetched via jina): "Other Nextcloud servers of our customers, partners, or other users are not affected by this problem." The quoted string is verbatim in **Cybernews** (Nextcloud-spokesperson statement: "...have been affected by this issue," the company's spokesperson said.). The quote is genuine and contiguous — only the `publisher` label is wrong. Fix: set publisher to "Cybernews".

### Claims missing inline citation
**F5 — citrixbleed-2-dragonforce-iab-kill-chain-stac3725 — fixed-build version strings unsourced.**
`cves[].fixed` = "14.1-47.46, 13.1-59.19, 13.1-FIPS/NDcPP 13.1-37.236, 12.1-FIPS 12.1-55.328", repeated in action #1 as an explicit patch target. None of the three cited sources carry these builds: Huntress (primary) says only "Patch Citrix NetScaler appliances to the latest software version" (confirmed via jina full text); IT Security Guru and the Sophos QEMU post give no build numbers. The builds are accurate/canonical, but a specific patch target handed to a SOC needs a source. Fix: add the Citrix/NetScaler PSIRT bulletin for CVE-2025-5777 as a corroborating source.

### Editorial / less-is-more flags (advisory)
**F11 — odido-shinyhunters-vishing-dutch-police-attribution — update_of target is a different incident.**
`update_of: 2026-06-26/shinyhunters-used-a-single-vishing-call-into-the-company-s-i` points to the Madison Square Garden ShinyHunters vishing entry — a distinct victim/incident. Odido is a never-previously-covered NL-telco incident. Store precedent ships each new ShinyHunters victim (MSG, Carnival, 7-Eleven, Medtronic, NAIC) as a standalone new incident, and rule 4b wants an update_of target to be "genuinely the same story." The body is a clean delta and the registry linkage (incident:odido -> actor:shinyhunters) is correct, so this is defensible — but consider a standalone new incident entry instead, or confirm the framing. Not publish-blocking.

### What was verified clean
- **CitrixBleed 2 (threat/deep_dive/high):** Both Huntress evidence quotes verbatim ✓; IT Security Guru IAB quote verbatim ✓; 127-byte over-read, 13:07→13:28 (21-min) token replay, RdpBus GUID, gpupdate→AppMgmt→SYSTEM→net user/localgroup chain, WIN- printer-mapping fingerprint, MetaFrameEvents/LocalSessionManager pivot, ScreenConnect/Zoho/Netbird/Atera/PsExec/Impacket/Mimikatz, DragonForce single-host encryption — all supported by Huntress. STAC3725↔Sophos cross-ref confirmed. CVE status [exploited, patch-available] correct. No IOCs (device-class GUID and generic WIN- prefix are OS constants, not indicators). 11 ATT&CK IDs all woven at the behavior they name. Priority `high` (not critical) correctly calibrated — the novelty is a productised IAB runbook on a 2025 CVE, not a fresh 0-day. Classification B2 apt.
- **M365 CA gaps (research/high):** all three evidence quotes verbatim ✓ (2 Huntress, 1 The Hacker News); Railway March 2026 / 344 orgs / device-code / 90-day token / EvilTokens / three IPs ~84% / construction-RFP lures / triple-wrapped SafeLinks; LSHIY 81M+ / ROPC / Azure CLI / 78 accounts / 64 orgs / 55 with active CA MFA / "Block Azure CLI" policy / report-only / userStrongAuthClientAuthNRequired — all supported. Classification B2 apt.
- **CERT.LV LVM/Olpha (incident/notable):** 44 GB, passwords+hashes, certs/keys, code repos, Olpha log-wiping, financially-motivated foreign actor, NATO/EU targeting assessment, ongoing probing, credential-rotation guidance all verbatim-confirmed on CERT.LV primary; 11-June access / 22-23 June detonation sourced to BNN (verified via jina — URL live; WebFetch 404 was a transport artifact); ~2yr-unpatched sourced to The Record (verbatim ✓); Sliver/Proton VPN/C2/Cloudflare-Dev-Tunnels-ngrok on CERT.LV recommendations page ✓. National-CERT-own-jurisdiction carve-out correctly applied; single-authority NATO/EU claim honestly flagged in sourcing_note. Classification A2 apt. No IOCs.
- **Nextcloud (incident/notable):** 367K records, ~8GB, hardcoded DB creds, IONOS/STRATO/MSB NRW, 18–25/27 May window (~9 days) all verbatim/confirmed on Cybernews; heise misconfiguration/no-customer-servers corroboration confirmed. (Only defect: F4 publisher label.) DACH/EU public-sector nexus (Nextcloud as EU sovereign-cloud alternative + German ministry exposed) is solid.
- **Odido (incident/notable/update):** Politie Dutch-national quote verbatim ✓; NOS human-vs-synthetic assessment ✓; older NOS vishing quote verbatim ✓; ShinyHunters attribution explicit in NOS (not an analytical link); 6.2M records / blocked-within-hour / Ben brand / CEO van Lammeren / data fields all supported. (Only issue: F11 update target.)
- **E-gov watering hole (research/notable):** both SentinelLabs evidence quotes verbatim ✓; "Update Complete! Please refresh the page", Smart Police Station EU-supported, Rust stager + .NET/AsyncRAT reflective load, Bitter/TAG-179/Mysterious Elephant/APT-C-08, PlugX/ShadowPad/Cobalt Strike/Remcos all supported. Out-of-nexus-by-victim inclusion earns its place on grounds (b) transferable TTP + (c) plausible EU-gov targeting, framed on the technique not the victim, and says which (sourcing_note). Classification B3 apt. No IOCs (C2 addresses explicitly omitted).
- **Whole-run:** No F16 (no org-triage scheme / no watchlist configured; all entries org_triage:null, watchlist_hit:false, no watchlist tags — compliant). No F17 (all six are non-triage kinds carrying valid classification; none is `vulnerability`-kind so none wrongly carries/omits a block). No F6 (every primary is a research-lab/national-CERT-carve-out/discoverer/law-enforcement source; no NVD/MITRE-only). No F1/F2 (all URLs resolve to specific articles/advisories; BNN 404 and Cybernews/heise/IT-Security-Guru/Express-Tribune 403 to WebFetch all reachable via jina/bridge with matching content). No F10 missed-angle identified: S1's 0-item vuln window is consistent with KEV (no new since 2026.07.07) and NCSC-CH sweep; Gitea CVE-2026-20896 (out-of-window) and Hermes CVE-2026-58122 (no exploitation/PoC/exposure) correctly dropped; Sonatype Q2 correctly dropped as vanity-metric single-source. Entries carry zero IOCs and zero vanity metrics. Run-record notes use standard telemetry vocabulary (S1–S4 / Phase N) as the operator forensic surface — not flagged as a reader-facing leak; entries themselves are style-clean.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 1)

F4 (publisher relabel to Cybernews) and F5 (add Citrix PSIRT for the fixed-build claim) are the substantive fixes; F11 (Odido update_of) is advisory and defensible as-is. Coverage looks both sound and complete for the window.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: nextcloud-gmbh-elasticsearch-exposure-msb-nrw
  item: "Nextcloud GmbH Elasticsearch exposure"
  url_or_quote: "evidence quote attributed to 'heise online'"
  summary: "Verbatim quote mis-attributed to heise; string is actually a Cybernews-published Nextcloud spokesperson statement. Relabel publisher to Cybernews."
- code: F5
  category: missing-citation
  section: citrixbleed-2-dragonforce-iab-kill-chain-stac3725
  item: "CitrixBleed 2 STAC3725 kill chain"
  url_or_quote: "cves[].fixed / action #1 build strings 14.1-47.46, 13.1-59.19, 13.1-FIPS 13.1-37.236, 12.1-FIPS 12.1-55.328"
  summary: "Specific fixed builds in no cited source (Huntress says only 'patch to latest'). Add Citrix/NetScaler PSIRT bulletin for CVE-2025-5777."
- code: F11
  category: editorial-advisory
  section: odido-shinyhunters-vishing-dutch-police-attribution
  item: "Odido update"
  url_or_quote: "update_of: 2026-06-26/shinyhunters-used-a-single-vishing-call-into-the-company-s-i"
  summary: "update_of target is a different incident (MSG). Store precedent ships new ShinyHunters victims standalone. Consider standalone new incident; defensible either way, not blocking."
```
