**Model:** Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-07-04T06:47:09Z · ended_at=2026-07-04T06:51:07Z · duration_seconds=238
**Self-telemetry:** webfetch_calls=4 · websearch_calls=0 · bridge_fetches=0 · urls_checked=4

## Verification report — 2026-07-04T0609Z-intel (iteration 3)

Cold read of 2 new entries + run record. All 4 cited URLs fetched (2 primaries, 2 corroborating THN
rewrites). Dedup: prior_coverage.json grepped for avalon/pamstealer/crownx/maccy/jamf/blackpoint — no match;
both entities registered correctly (tool:avalon-malware-framework aliases [CrownX]; tool:pamstealer). No IOCs
in either entry body (Blackpoint's C2 domain, BTC address and SHA-256 set, and Jamf's avenger-sync[.]live /
maccyapp[.]com correctly kept out). No hallucinated CVE — THN Avalon's CVE-2025-3248 / JADEPUFFER are
related-article cruft and are correctly absent from the entry.

Verified verbatim:
- Avalon evidence[0] "Avalon is operationally significant because it consolidates credential theft,
  persistence, and ransom functionality under one recovered payload rather than distributing them across
  discrete malware families." — EXACT substring of the Blackpoint primary.
- Avalon evidence[1] "The framework bears the hallmarks of AI assisted development, assembled rapidly from
  functional components with little regard for tradecraft refinement or operational security" — verbatim
  substring (primary appends a trailing ellipsis only).
- PamStealer evidence[1] "The result is a quieter routine that keeps only a verified password, and one fewer
  process chain for defenders to detect on." — EXACT substring of the Jamf primary.
- PamStealer evidence[0] opening "Rather than relying on shell commands such as curl or zsh, the AppleScript
  executes a self-contained JavaScript for Automation..." — confirmed verbatim against Jamf.

Body/frontmatter claims confirmed against sources: Avalon — MSBuild inline C# via CodeTaskFactory (T1127.001),
ETW/AMSI patching (T1562.001), CrownX AES-GCM (ChainingModeGCM), VSS/WinRE/System Restore inhibition (T1490),
admin-share lateral movement (T1021.002), scheduled tasks (T1053.005), SSH/RDP/Credential Manager theft
(T1555/T1552.001), HalosGate/TartarusGate, named EDR checks (Defender/SentinelOne/CrowdStrike/Sophos/Elastic/
FortiEDR/ESET/McAfee/Bitdefender), AI-assisted assessment. PamStealer — PAM API validation (pam_start/
pam_authenticate/pam_end), arm64 Rust Mach-O masquerading as Finder, JXA downloader, pbpaste clipboard,
ServiceManagement (SMAppService) persistence, RU/BY/KZ locale exclusion, Full Disk Access social engineering.

Single-source framing correct for both: THN Avalon names Blackpoint researchers and outbound-links to the
Blackpoint primary; THN PamStealer credits Jamf Threat Labs and outbound-links to the Jamf primary — both are
non-independent rewrites, so verification: single-source + sourcing_note is right. Priority notable is
correctly calibrated (detection-relevant research, not actively-exploited/immediate-action). Org-relevance
holds for a Swiss federal SOC (Windows LOLBin abuse; macOS PAM-abuse detection on managed fleets). Volume/
coverage shape fine (2 research entries, 0 CVEs, no deep dive, both net-new — correct new-not-update calls).

### Citation does not support the claim

F3 — Avalon entry, body paragraph 2:
"Secondary reporting frames the framework as bundling into a single implant the capability an actor would
previously have assembled from several discrete malware families ([The Hacker News, 2026-07-03])."
WebFetch of https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html: THN frames Avalon only
as bringing "diverse functions under one umbrella" and, asked directly, does NOT reference capability
previously spread across several discrete malware families. That "discrete malware families" phrasing is
Blackpoint's (primary evidence[0]: "rather than distributing them across discrete malware families"), so the
sentence attributes Blackpoint's framing to THN. LOW SEVERITY: the underlying claim is true and fully sourced.
Cleanest non-regressive fix — re-cite the Blackpoint Cyber primary (already cited in the same entry) for this
sentence, or reword to THN's actual "diverse functions under one umbrella".

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Avalon framework chains a signed-binary MSBuild loader, ETW/AMSI patching and the CrownX ransomware payload in one implant"
  url_or_quote: "Body para 2: 'Secondary reporting frames the framework as bundling into a single implant the capability an actor would previously have assembled from several discrete malware families ([The Hacker News, 2026-07-03]).'"
  summary: "THN frames Avalon only as 'diverse functions under one umbrella' and does not state the 'several discrete malware families' consolidation attributed to it; that phrasing is Blackpoint's. Low severity — claim is true and fully sourced; fix by re-citing the Blackpoint primary (already cited elsewhere in the entry)."
```
