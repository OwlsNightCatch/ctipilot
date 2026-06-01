**Model:** Anthropic Claude (specific model not determined — env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset; runtime self-id: Opus 4.8 `claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-01T04:36:42Z · ended_at=2026-06-01T04:39:28Z · duration_seconds=166

## Verification report — briefs/2026-06-01.md (iteration 1)

Cold read, all four cited primaries plus three secondary/MITRE pages fetched this iteration. Mechanical gate already PASS (only run-log placeholder + 2 benign name-collision WARNs outstanding). Focus: URL truth + entity cross-check + editorial.

URLs fetched & live this pass (all resolve to specific articles, support most attached claims):
- posthogstatus.com/incidents/01KSV6HJYKG5QJAP8HVTSQVSM1 — live, supports PostHog claims (timeline, AWS-cred rotation, no customer data, vector undisclosed).
- microsoft.com/.../33-malicious-npm-packages... — live, BUT body documents 45 packages not 33 (see F3).
- sonatype.com/blog/inside-a-176-package-npm-campaign... — live, fully supports (176 pkgs, Sonatype-2026-003429, 99.99.99, Russian comments, shared infra, 2026-05-28).
- isc.sans.edu/diary/rss/33034 (via bridge) — live, fully supports § 3 (2026-05-27 infection, processor.vbs 109B → token.bat 8262B → setup.cab 17,275,805B, UpdateInstaller path, self-delete, Brad Duncan, encoded-not-TLS TCP/443 since April). No IOCs leaked into brief — confirmed clean.
- news.risky.biz/...sorm... — live, supports PostHog secondary.
- edri.org/our-work/inside-italys-low-cost-spyware-economy — live, supports MOST deep-dive claims BUT NOT the 16-June-2026 EP debate / Commission-of-Inquiry / export-controls-unenforced claims (see F4, F3).
- osservatorionessuno.org/.../morpheus... (via bridge; direct WebFetch 403) — live, fully supports Morpheus technical claims incl. AV-kill list (Bitdefender/Sophos/Avast/AVG/Malwarebytes + Google SafetyCore), 2025.3.0, IPS Intelligence, device_config indicator suppression, WhatsApp pairing.

MITRE IDs verified real & sensibly applied: T1626 Abuse Elevation Control Mechanism (Android) ✓; T1516 Input Injection (Android) ✓; T1070.004 Indicator Removal: File Deletion ✓; T1059.005 Visual Basic ✓ (VBScript reasonable); T1219 — see F11 (MITRE renamed to "Remote Access Tools"; brief says "Remote Access Software"). T1190/T1195.002/T1082/T1083/T1614 are analyst-applied mappings consistent with described behaviour — acceptable.

### Citation does not support the claim
- **F3a — npm package count.** TL;DR + § 1 state "Microsoft (33 packages, 9 organisational scopes)" / "detailed 33 malicious packages pushed in two bursts" / "All 33 packages were removed within hours." The cited Microsoft blog body documents **45** packages (per-maintainer breakdown mr.4nd3r50n 26 + ce-rwb 7 + t-in-one 12 = 45); "33" is only the stale URL-slug/headline count from before the 29 May t-in-one wave. The brief presents 33 as the documented total, which the cited source body contradicts. Fix: change to 45 (or "33 initially, 45 after the 29 May wave") to match the cited body. The "9 organisational scopes" figure IS supported.
- **F3b — npm removal timing.** "All 33 packages were removed within hours" — the Microsoft source says only that the "repos and users were taken down" and gives **no removal timing**. "within hours" is unsupported. Fix: drop "within hours" or attribute to a source that states it.
- **F3c — EDRi export-controls claim.** § 5 states "export controls are largely unenforced ([EDRi, 2026-05-28])." The EDRi page does not characterise export controls as unenforced (it says internal-market rules let vendors operate freely across member states). Fix: reword to what EDRi actually says (free cross-border operation under internal-market rules) or drop the export-controls phrasing.

### Unsupported / hallucinated facts
- **F4 — 16-June-2026 EP debate + Commission of Inquiry (deep dive, § 5).** Brief: "The European Parliament is scheduled to debate the combined Paragon-and-domestic-vendor spyware question on **16 June 2026**, with EDRi and civil-society groups pushing for a **Commission of Inquiry** and EU-wide proportionality rules ([EDRi, 2026-05-28])." Fetched the EDRi page twice — **neither the 16-June-2026 date, nor "Commission of Inquiry", nor "EU-wide proportionality rules" appear on the cited page** (it calls for an EU-wide spyware ban with binding transparency obligations). Worse: a web search shows the "16 June" EP Paragon debate + Commission-of-Inquiry calls map to the **2025** Paragon scandal timeline (Citizen Lab 12-June report, Cancellato/Fanpage, Greens-EFA request) — i.e. this looks like a past event mis-stated as an upcoming 16-June-**2026** scheduled debate, and it is attached to a source that does not contain it. This is the most serious finding: a forward-looking factual claim with a wrong-looking date and no supporting cited source. Fix: remove the sentence, or replace with a correctly-dated, correctly-cited source if one exists; do not present it as a scheduled future debate on EDRi's authority.

### Editorial / less-is-more flags (advisory)
- **F11a — T1219 name.** § 3 writes "T1219 Remote Access Software"; MITRE has renamed T1219 to "Remote Access Tools". ID is correct, concept correct, platform (Win/Lin/mac) correct for NetSupport. Cosmetic — update label if convenient.
- **F11b — Risky Biz negative attribution (§ 1).** The sentence ending "...has not disclosed the vector, the research team, or whether a CVE was assigned ([Risky Biz News])" attributes negative/absence facts to Risky Biz; Risky Biz simply doesn't mention those details. Both PostHog status and Risky Biz are silent on vector/CVE, so the negative is true-by-absence and acceptable, but the citation placement implies Risky Biz affirmatively reported the non-disclosure. Minor — leave or soften.

### Confirmed-benign (no finding)
- name-collision WARN "Shai-Hulud": npm item explicitly says "distinct from the Mini Shai-Hulud / TrapDoor activity covered last week" — explicit disambiguation, same attacker-tooling referent, no defender/attacker inversion. Benign.
- name-collision WARN "ClickFix": generic recurring attacker technique, same referent as prior coverage, no inversion. Benign.
- Dedup: npm/PostHog/SmartApeSG/Italy-spyware are all genuinely new vs prior_coverage.json (TrapDoor/TeamPCP/Mini-Shai-Hulud 2026-05-26 & W22 are distinct). No recycled content.
- No IOCs leaked despite IP/hash/domain-rich SANS + Osservatorio sources — confirmed clean.
- Coverage shape: § 1 leads CH/EU/tech, § 2 empty with justification, deep dive earns length, no emergency-action overclaim. Style discipline clean (English, no vanity metrics, no workflow leakage).

### Verdict
NEEDS_FIXES (truth: 4, editorial: 0, advisory: 2)

Truth = F3a, F3b, F3c, F4. Advisory = F11a, F11b. F4 is the load-bearing one — fix it before publish.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: tldr-and-active-threats
  item: "Two concurrent npm dependency-confusion campaigns — Microsoft"
  url_or_quote: "Microsoft (33 packages, 9 organisational scopes) / All 33 packages were removed within hours"
  summary: "Cited Microsoft blog body documents 45 packages (26+7+12), not 33; 33 is the stale headline/slug count. Change to 45 (or '33 initially, 45 after the 29 May wave')."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "npm dependency-confusion — removal timing"
  url_or_quote: "All 33 packages were removed within hours"
  summary: "Microsoft source says repos/users 'were taken down' with no timing; 'within hours' unsupported. Drop the timing claim."
- code: F3
  category: claim-not-supported
  section: deep-dive
  item: "Italy spyware — export controls"
  url_or_quote: "export controls are largely unenforced ([EDRi, 2026-05-28])"
  summary: "EDRi page does not say export controls are unenforced; it says internal-market rules let vendors operate freely across member states. Reword to source or drop."
- code: F4
  category: hallucinated-fact
  section: deep-dive
  item: "Italy spyware — EP 16 June 2026 debate"
  url_or_quote: "The European Parliament is scheduled to debate ... on 16 June 2026, with EDRi and civil-society groups pushing for a Commission of Inquiry and EU-wide proportionality rules ([EDRi, 2026-05-28])"
  summary: "None of '16 June 2026', 'Commission of Inquiry', or 'EU-wide proportionality rules' appear on the cited EDRi page (fetched twice). Public record ties a '16 June' Paragon EP debate + Commission-of-Inquiry to the 2025 timeline, suggesting a wrong-date future-event claim on an unsupporting source. Remove or re-cite with a correctly-dated source."
- code: F11
  category: editorial-advisory
  section: research
  item: "SmartApeSG — T1219 label"
  url_or_quote: "T1219 Remote Access Software"
  summary: "MITRE renamed T1219 to 'Remote Access Tools'; ID/concept/platform correct. Cosmetic relabel."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "PostHog — Risky Biz negative attribution"
  url_or_quote: "has not disclosed the vector, the research team, or whether a CVE was assigned ([Risky Biz News])"
  summary: "Negative/absence facts attributed to Risky Biz which is simply silent; true-by-absence and acceptable but citation placement implies affirmative reporting. Soften or leave."
```
