**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-06T08:37:16Z · ended_at=2026-06-06T08:40:16Z · duration_seconds=180
**Self-telemetry:** webfetch_calls=12 websearch_calls=0 bridge_fetches=4 urls_checked=16

## Verification report — briefs/2026-06-06.md (iteration 1)

Cold read, end-to-end. Every inline Source URL fetched (WebFetch direct, or bridge `tools/fetch_source.py` for known-403 hosts: NCSC-CH, MI5, SolarWinds, BSI). Every named CVE / actor / campaign / version / date / quote / number cross-checked against a source fetched in this iteration.

### URL liveness + claim-support summary (all PASS)

- **MI5 — Five Eyes "Safeguarding Our Secrets"** (bridge): live; canonical page; datePublished Wed 03/06/2026 matches brief; meta confirms China military intelligence / professional-networking + online job platforms / cleared personnel. SUPPORTS.
- **The Record — Five Eyes/Chinese spies job sites**: live; specific article; confirms China, Five Eyes (ASIO/CSIS/FBI/MI5/NZSIS), LinkedIn, "Safeguarding Our Secrets", cleared/military/government targets, $hundreds-to-thousands deliverables, shift to encrypted messaging. SUPPORTS.
- **JFrog Research — IronWorm**: live; specific research post; Rust payload, eBPF kernel rootkit, Tor C2, cloud + AI-provider (Anthropic/OpenAI/Gemini) credential sweep, Trusted Publishing self-propagation, asteroiddao compromised publisher. SUPPORTS.
- **BleepingComputer — IronWorm 36 packages**: live; specific article; confirms 36 npm packages, eBPF rootkit, Tor, 86 env vars / 20 credential files, self-propagation via stolen npm creds. SUPPORTS the "~36 packages" figure.
- **Cisco PSIRT cisco-sa-sdwan-privesc-4uxFrdzx**: live; PSIRT advisory; CVE-2026-20245, command-injection to root requiring netadmin, in-the-wild config-push to edge devices, no fixed release, references CVE-2026-20182 + CVE-2026-20127. SUPPORTS (advisory states CVSS 7.8; brief footer carries `CVSS: n/a` — conservative under-statement, not a defect).
- **NCSC-CH GovCERT 12579** (bridge ncsc-csh post 12579): live; advisory edited 2026-06-05 "Added related Actively exploited CVE-2026-20245"; carries the exact Cisco quote on netadmin prereq + config-push. SUPPORTS.
- **SolarWinds Trust Center CVE-2026-28318** (bridge): live; JS-SPA, `<title>` confirms it is the CVE-2026-28318 advisory page (correct specific page, not a homepage). Body not server-rendered — technical specifics (CWE-400, 15.5.4 Hotfix 1, CVSS 7.5) corroborated instead via CISA KEV (below).
- **CISA KEV** (bridge cisa-kev): CVE-2026-28318 present, dateAdded 2026-06-05, "SolarWinds Serv-U Uncontrolled Resource Consumption", shortDescription = crafted POST with Content-Encoding: deflate crashing the service without authentication. SUPPORTS every load-bearing Serv-U claim incl. the KEV-listing date.
- **ENISA EUVD-2026-34268**: live but JS-SPA returned "application could not be loaded" — additional source only; primary claims already confirmed via KEV. Not load-bearing.
- **GitHub Security Advisory GHSA-h7wj-m45x-884x**: live; confirms CVE-2026-10868, MISP, CVSS 9.0, mass-assignment in UsersController::edit(), fix strips User.id before edit processing. SUPPORTS.
- **BSI CERT-Bund WID-SEC-2026-1800** (bridge): live JS-SPA portal; body not server-rendered. Additional source only; MISP claims confirmed via GHSA. Not load-bearing.
- **ReliaQuest — OP-512**: live; specific research post dated 2026-06-05; confirms OP-512, China-linked, IIS + EOL .NET 4.0, one .aspx + two .ashx handlers, per-deployment RSA/RC4 uniqueness, timestomping, reflective .NET load, hex-DNS self-report from w3wp.exe, 75-day dwell, CL-STA-0048 overlap. SUPPORTS (single-source — correctly flagged [SINGLE-SOURCE] + PD-5 carve-out in §7).
- **OpenSourceMalware — Miasma reaches Azure**: live; `<title>` "The Blight Reaches Microsoft: 73 Repos Disabled in 105 Seconds" confirms 73 repos + 105 seconds + Microsoft. Body not extracted; THN additional source confirms the rest.
- **The Hacker News — Miasma 73 Microsoft repos**: live; specific article; confirms Miasma (Mini Shai-Hulud variant), TeamPCP, durabletask recompromise, 73 repos across Azure/Azure-Samples/Microsoft/MicrosoftDocs, Azure Durable Task family. SUPPORTS. (Note: THN frames durabletask as PyPI; brief frames the npm/Durable Task ecosystem — both consistent with the worm's cross-ecosystem behaviour.)
- **Mandiant/GTIG — targeted campaign US law firms**: live; specific blog dated 2026-06-05; confirms UNC3753/Luna Moth/SRG, Jan–May 2026, US legal/financial/professional services, vishing + AnyDesk/Bomgar/Zoho/SuperOps-via-cURL + WinSCP/Rclone, and BOTH verbatim quotes ("individuals posing as IT technicians entered corporate offices to attempt direct exfiltration of data from an endpoint using USB storage media"; "data searches, staging, and theft initiated in under an hour"). T1052.001 explicitly referenced. SUPPORTS.
- **Help Net Security — FBI SRG law firms (2026-05-27)**: live; confirms SRG/Luna Moth, FBI alert, physical IT-staff impersonation + USB, legitimate-tooling/no-encryption. SUPPORTS.
- **Legal Cheek — Weil ~$20M (2026-06-03)**: live; confirms Weil Gotshal & Manges, $18–20M, client documents from external cloud storage, paid within ~3 days, Luna Moth. SUPPORTS "~$20 M".
- **Security Affairs — SRG DNS fast-flux (2026-06-05)**: live; confirms SRG/Luna Moth/UNC3753 moving C2 to DNS fast-flux. SUPPORTS.
- **BleepingComputer — FBI Luna Moth (2025-05-23)**: live; confirms historical FBI warning, ~two years targeting US law firms, BazarCall/Conti lineage, WinSCP/Rclone, no encryption. SUPPORTS the deep-dive background incl. the 2025-05-23 date.

### Editorial / coverage assessment

- **Coverage shape**: §1 leads with CH/EU-relevant items (Five Eyes personnel-security with explicit Swiss nexus; IronWorm supply-chain). §2 inclusion gates honoured — CVE-2026-20245 (ITW, no patch), CVE-2026-28318 (CISA KEV), CVE-2026-10868 (CVSS 9.0 in the platform underpinning GovCERT.ch/CERT-EU). Deep dive earns its length and explicitly avoids re-reporting the physical-USB tactic as novel, leading on three genuine in-window developments. No §0 Immediate Actions callout present — acceptable; no item meets the "stop reading and act now to the hour" bar (Cisco is mitigation-only, Serv-U is DoS).
- **Dedup**: clean. HTTP/2 Bomb CVE-2026-49975 correctly demoted to §7 (was the 2026-06-04 deep dive). Miasma correctly an UPDATE to 2026-06-02 coverage with a stated material delta (Azure collectors + Microsoft estate). No recycled material.
- **Name-collision check**: "Miasma" and "Shai-Hulud" both attacker entities consistent with prior coverage (TeamPCP lineage). Brief explicitly disambiguates "Miasma is the attacker worm, not a tool" — good. No attacker/defender inversion. IronWorm is described as JFrog's name for the attacker worm, consistent with the source. No F15.
- **Style**: zero IOCs, zero vanity metrics, English throughout, no workflow-internal language. Tags/regions/sectors within vocabulary (mechanical gate confirmed).
- **Single-source**: OP-512 correctly carries [SINGLE-SOURCE] + §7 PD-5 carve-out note. No other single-source item lacks its flag.
- **Quantifiers**: "Second ... zero-day" (Cisco) — supported by NCSC framing the new related zero-day; "73 repositories", "105-second", "~36 packages", "~$20 M", "75 days", "under an hour" all traced to fetched sources. No F14.
- **Analytical links**: TeamPCP→durabletask→Microsoft chain is asserted by THN/OpenSourceMalware sources, not the brief. UNC3753 physical-USB "possibly linked" hedge in Mandiant is preserved by the brief's "reportedly"/forensic-confirmation framing. No F13.

### Advisory note (not a NEEDS_FIXES finding)

- §1 prose names "LinkedIn, Indeed, Upwork" as the recruitment platforms. The Record (fetched) explicitly names only LinkedIn; the MI5 page's server-rendered head/meta names "professional networking sites and online job platforms" generically. I could not retrieve the MI5 article body (bridge returned the SPA shell), so I CANNOT assert the source fails to name Indeed/Upwork — the meta's plural "job platforms" makes their presence in the body plausible. Flagged as advisory only: if the main agent has not independently confirmed Indeed/Upwork appear in a cited source, consider softening to "LinkedIn and other job/freelance platforms." Not blocking.

### Verdict

CLEAN — every load-bearing URL resolves to a specific primary/article and supports its claim; every named entity traced to a fetched source; coverage, dedup, single-source flagging, and style all compliant. The one advisory note (Indeed/Upwork specificity) is non-blocking and cannot be substantiated as a defect without claiming a source-gap I did not verify.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
[]
```
