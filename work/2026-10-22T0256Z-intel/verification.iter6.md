**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T06:08:12Z · ended_at=2026-10-22T06:25:29Z · duration_seconds=1037

## Verification report — 2026-10-22T0256Z-intel (iteration 6)

Scope walked (post-fix pass): all 11 claims of `claims.changed.iter6.yaml`, every claim of the three entries remediated this round (LiteLLM 18, Publica 26, Cisco 21), and in practice every remaining claim of the other seven entries as well: 257 rows in `verification.iter6.claims.yaml` (256 ok, 1 F3, 0 unreadable). Pages read live this iteration or from the saved bodies of this run: LiteLLM post, issue, Socket, Wiz, Aikido; four Cisco advisories; admin.ch, PK Softech (raw HTML for the Reinach address), watson, Publica DE, Netzwoche, Tages-Anzeiger (lead via reader), Inside IT, PKZH, Pensionskasse Post x2, Cybercrimepolice, NZZ, BPK PDF, BLVK PDF (origin returns 503, read through the Wayback copy); Palo Alto CVE-2026-109618 (live, still TBD) and CVE-2026-0257, Unit 42, php.net, both GHSA pages, CERT-EU, ENISA, BACS, Sansec, Cloudflare, watchTowr, VulnCheck, Security.nl, PHP Foundation, Wordfence, nau.ch x2, RTS, Publica EN; GitLab patch notes and both detections; Group-IB, FG-IR-25-910, FG-IR-19-007, the KEV catalogue; Microsoft, Expel, CrowdStrike (publishDate 07 Oct), Recorded Future, Huntress, Todyl, Sophos, SpecterOps, BleepingComputer, heise, the ConnectWise advisory (Wayback copy, 403 on every live transport), OVH advisory, issue and X post, OpenSourceMalware.

### Prior-iteration deltas (checked first)

- LiteLLM Defender takeaway: every clause now sits on the page that carries it. "rotate every credential the host could reach" is the maintainers' step 5 ("Rotate everything listed above that the host could reach"); "removing the package does not remove the startup files" is Socket; "stolen cloud credentials were in use within hours" is Wiz ("starting approximately 4.5 hours post-exfiltration"); "rebuild from a reviewed release and pin container digests" is Socket ("Use a reviewed release and pin container digests during recovery"); "move to 1.106.2 or an explicit earlier version as the maintainers advise" is the maintainers' "pin your version to 1.106.2 or any explicit version published prior to now". Fix correct.
- Publica main analysis: now "Tamedia's Tages-Anzeiger reports that the Akira ransomware group holds about 100 GB ... and demands ransom, which Inside IT relays without the volume". Tages-Anzeiger lead: "Die Hackergruppe Akira stahl rund hundert Gigabyte komprimierte Pensionskassendaten"; Inside IT carries Akira, the demand, "weit über 100'000" and security-authority staff but no volume; Publica EN/DE: "We still have no indication that data have been published on the dark web". Fix correct.
- Cisco Exposure and Detection: "the affected component is the database service" matches Cisco ("A vulnerability in the database service feature of Cisco Expressway Series"). Fix correct.

### Citation does not support the claim

- **F3 #1 (low confidence)** `publica-pk-softech-supplier-malware-intrusion-data-outflow`, Update 2026-10-22T03:47:53Z: "relaying the paywalled article that Tamedia's Tages-Anzeiger published on 2026-10-20: ..." cited to the Netzwoche page. That page says "Update vom 21.10.2026: ... wie der \"Tages-Anzeiger\" (Paywall) berichtet" and carries no date for the Tages-Anzeiger article. The date is true (dateline 20.10.2026 10:26 on the Tages-Anzeiger page) but is not on the cited page. Fix: cite the Tages-Anzeiger link on that clause or drop the date.

### Needs more research

- **F8 #1 (low confidence)** `k0t-fortiweb-fortigate-globalprotect-edge-device-campaign`, Exposure and actions[0]: "which Fortinet warns can cause install errors and split-brain on FortiManager-managed or HA FortiGates". FG-IR-19-007 continues: "This issue is fixed in FortiManager versions 6.2.7 and above and in FortiGate versions 6.2.6, 6.4.4, 6.6.0 and above." The entry drops the fixed-in versions, so the caveat reads as a live risk on every FortiGate and may deter enabling the control the entry urges. Add the fixed-in versions.
- **F8 #2 (low confidence)** `connectwise-cloud-backup-skykick-m365-app-credential-abuse`, main analysis and Update 2026-10-22T03:46:23Z: the entry keeps ConnectWise's 2026-10-19 01:15 UTC snapshot and takes the restoration start from heise. The Wayback copy of the Trust Center (read by iteration 5 as well) carries updates through 2026-10-22 00:45 UTC: restoration "in controlled phases" from 2026-10-21 12:45 UTC, and on 2026-10-21 22:00 UTC "Based on the evidence available to ConnectWise, including threat intelligence shared by Microsoft, it appears that a China state-aligned group was responsible". The vendor's own acknowledgement of the attribution and its restoration status belong in the update section; the run record's "rests on heise" understates what was readable.

### Editorial / less-is-more flags (advisory)

- **F11 #1 (low confidence)** `litellm-1-107-0-pypi-docker-credential-stealer-lookalike`, Detection: "an encrypted archive posted to a look-alike health-check endpoint" cited to Socket only. Socket says "Despite the URL's health-check wording" and does not call the domain a look-alike; Wiz ("attacker controlled, impersonating LiteLLM infrastructure") and Aikido ("not affiliated with the legitimate LiteLLM project") do. The phrase reads either way; add the Wiz or Aikido citation if the impersonation is meant.
- **F11 #2 (low confidence)** `publica-pk-softech-supplier-malware-intrusion-data-outflow`, summary: "the Pensionskasse Post and the Bernische Pensionskasse say personal data left". BPK told the NZZ "davon ausgegangen werden muss, dass Personendaten abgeflossen sind" (it must be assumed); the body states this correctly, the summary flattens it.

### Checks with no finding

- Priority calibration: PHP `critical` clears the bar (newly disclosed in window; attack traffic by Cloudflare, watchTowr and VulnCheck; public PoCs per CERT-EU and VulnCheck; time-critical; no confirmed compromise written as such). GitLab, Cisco, PAN-OS, k0t, ARTEX and LiteLLM at `notable`, ConnectWise and Publica at `high`: defensible on the cited facts; GitLab at `notable` is borderline (CVSS 10.0, unauthenticated, but unexploited, no PoC and a public-project precondition).
- Dedup: no new entry shares CVEs or a finding with an existing one; PAN-OS, k0t and GitLab declare their earlier entries in `references[]`; LiteLLM's earlier entries concern other incidents.
- Style: no em dash outside `## <Type> — <at>` headings, no workflow vocabulary, no IOC hashes, IPs or attacker domains in any of the ten entries (vendor signature IDs, app client IDs and the look-alike repository name are detection content).
- Missed angles: none found. Searches for in-window Swiss public-sector incidents and emergency patches surfaced only items already covered (Patch Tuesday CVE-2026-96951, FortiMail CVE-2026-104286, FortiClient EMS CVE-2026-35616 are in the store) or the declared borderline drop (FortiSIEM CVE-2026-106173: third-party sources describe it as disclosed 2026-10-13 and not exploited). Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 2, advisory: 2). All findings are low confidence and small; the three iteration-5 remediations are correct and introduced no new defect.

### Findings summary (machine-readable)

See `work/2026-10-22T0256Z-intel/verification.iter6.findings.yaml`.
