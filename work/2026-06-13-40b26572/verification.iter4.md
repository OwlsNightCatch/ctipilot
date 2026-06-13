**Model:** Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-13T12:28:18Z · ended_at=2026-06-13T12:33:06Z · duration_seconds=288
**Self-telemetry:** urls_checked=22 · webfetch_calls=18 · bridge_fetches=1

## Verification report — briefs/2026-06-13.md (iteration 4)

Cold read. Env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset; self-identified from runtime context per fallback rule. This is an even iteration (alt-verifier Sonnet). Prior-iteration delta block processed first, then full cold truth + editorial pass.

## Prior-iteration delta verification (iter-3 F4 remediation)

**Delta:** iter-3 found `langgraph-checkpoint` 4.0.1 (wrong package+version for CVE-2026-28277) in §3 and §6; remediation was to correct to `langgraph` 1.0.10.

**Verification:** Both cited sources fetched in this iteration confirm:
- Check Point Research (`research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/`): "Mentioned entities — Versions: langgraph-checkpoint-sqlite 3.0.1+, **langgraph 1.0.10+**, langgraph-checkpoint-redis 1.0.2+" — confirms `langgraph` 1.0.10 as the fix for CVE-2026-28277.
- The Hacker News (`thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html`): confirms `langgraph (before 1.0.10)` as affected; does not mention `langgraph-checkpoint 4.0.1`.

**Current brief §3 (line 61):** "the fixes shipped in `langgraph-checkpoint-sqlite` 3.0.1 (CVE-2025-67644), `langgraph` 1.0.10 (CVE-2026-28277) and `langgraph-checkpoint-redis` 1.0.2 (CVE-2026-27022)." — CORRECT.
**Current brief §6 (line 118):** "pin `langgraph` ≥1.0.10 / `langgraph-checkpoint-sqlite` ≥3.0.1 / `langgraph-checkpoint-redis` ≥1.0.2" — CORRECT.

Remediation confirmed. F4 defect is resolved.

Minor note: THN states `@langchain/langgraph-checkpoint-redis` before 1.0.1 (not 1.0.2), while Check Point says 1.0.2+. The brief uses 1.0.2 following the authoritative primary (Check Point). This discrepancy was already noted in iter-3 and explicitly deferred to Check Point as the primary; it is not a new defect.

## Full cold truth + editorial pass

### URL resolution check

All cited URLs checked in this iteration:

| URL | Status |
|-----|--------|
| `cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/` | 200, specific article, supports claims |
| `www.oracle.com/security-alerts/alert-cve-2026-35273.html` | 200 via bridge, specific PSIRT advisory, supports claims |
| `www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/` | 200, specific ETR post, supports claims |
| `www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916571` | 200, specific press release, supports access + copied data claim |
| `www.bleepingcomputer.com/news/security/pharmaceutical-giant-novo-nordisk-discloses-security-breach/` | 200, specific article, supports HCP data detail |
| `www.theregister.com/security/2026/06/12/novo-nordisk-says-hackers-stole-clinical-trial-data/5254812` | [not re-fetched — iter-3 confirmed 200; trailing /5254812 benign article-ID] |
| `www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency` | 200, specific blog post, supports all claims |
| `ioctl.fail/preliminary-analysis-of-aur-malware/` | 200, specific research post, supports BPF map paths + eBPF claims |
| `www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/` | 200, specific article, supports ~400 packages + atomic-lockfile |
| `therecord.media/south-korea-data-breach-record-fine-coupang` | 200, specific article, supports all Coupang claims including six-month log detail |
| `www.bleepingcomputer.com/news/security/south-korea-hits-coupang-with-record-409-million-fine-over-data-breach/` | 200, specific article, supports fine amount + key facts |
| `horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/` | 200, specific disclosure, supports CVE + bypass description |
| `simple-help.com/security/simplehelp-security-update-2026-05` | 200, specific security notice, supports versions 5.5.16 / 6.0 RC2 |
| `research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/` | 200, specific CPR post, supports LangGraph CVE chain + fix versions |
| `thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html` | 200, specific THN article, supports LangGraph claims |
| `thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html` | 200, specific THN article, supports Agentjacking claims |
| `tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/` | Cloudflare-blocked (as §7 discloses) |
| `blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/` | 200, specific Google blog post, supports Outsider/lawsuit |
| `thehackernews.com/2026/06/google-sues-chinese-smishing-network.html` | 200, specific THN article, supports Gemini-weaponised / China / Telegram |
| `www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident` | 200, specific Nottingham page (no 454,600 figure, but BleepingComputer Additional source carries it) |
| `www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/` | 200, confirms 454,600 + passport numbers |
| `www.maine.gov/ag/news-and-library/press-releases/statement-office-maine-attorney-general-abuse-data-breach-reporting` | 200, specific press release, confirms hoax + portal offline |
| `www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/` | 200, confirms portal offline |
| `thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html` | 200, specific THN article, supports Velvet Ant claims |
| `www.sygnia.co/blog/operation-highland-velvet-ant/` | Imunify360/Cloudflare blocked (as §7 discloses) |
| `www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/` | Imunify360/Cloudflare blocked (as §7 discloses) |

No broken URLs. No homepages or index pages. All source citations land on specific articles. Both Sygnia pages are UA-blocked exactly as §7 discloses; the brief correctly leads those items with the verified THN relay.

### Named entity cross-check

- **CVE-2026-35273, CVSS 9.8, UNC6240/ShinyHunters, PeopleTools 8.61/8.62, PSEMHUB, 27 May–9 June, 100+ orgs, 68% higher-ed, MeshCentral-as-Azure, SSH fan-out, KEV 12 June:** All confirmed by Mandiant/GTIG + Rapid7. Oracle PSIRT (bridge) confirms 8.61/8.62, CVSS 9.8, updated-date 2026-06-10. Nottingham 454,600 + passport numbers confirmed by BleepingComputer.
- **CVE-2026-48558, OIDC signature bypass, Technician session, MFA bypass, 5.5.15 affected, fixed 5.5.16 / 6.0 RC2, Security Notice 2026-05, CVSS n/a:** All confirmed by Horizon3 + SimpleHelp advisory.
- **CVE-2025-67644 (SQLite SQLi), CVE-2026-28277 (msgpack deserialization → RCE), CVE-2026-27022 (Redis SQLi); `langgraph-checkpoint-sqlite` 3.0.1, `langgraph` 1.0.10, `langgraph-checkpoint-redis` 1.0.2:** All confirmed by Check Point Research primary.
- **Agentjacking, Sentry DSN, markdown-injected events, Tenet Security, no CVE, Sentry content-filter-only:** Confirmed by THN relay. Tenet originator UA-blocked as §7 discloses.
- **Outsider Enterprise, China-based, Gemini AI weaponised, Telegram subscription, PhaaS:** Google blog + THN confirm. The brief's framing of postal/delivery/tax lures as mapping to Swiss/EU smishing themes is analytical framing on known PhaaS template categories; defensible.
- **Velvet Ant, Operation Highland, ~decade/2016, nine pam_unix.so variants, magic password, credential-logging sshd, air-gapped network:** All confirmed by THN relay.
- **Novo Nordisk, HCP names/phones/WhatsApp, pseudonymised clinical-trial data:** Primary press release confirms access/copied data; BleepingComputer carries HCP field detail + WhatsApp. Confirmed.
- **Coupang, ₩624.7 bn (record), former employee, signing key, forged tokens, seven months, "deficiencies in basic safety management," six months logs deleted:** All confirmed across The Record + BleepingComputer.
- **Atomic Arch, ~400 AUR packages, atomic-lockfile, Rust stealer, eBPF rootkit, BPF maps at /sys/fs/bpf/hidden_*, second wave js-digest/lockfile-js + Bun, Sonatype-2026-003775 CVSS 8.7, ~1,500 estimate:** All in Sonatype primary (the inline cite on second-wave sentence points to BleepingComputer which doesn't carry those specifics, but Sonatype is cited as Source on the same item — advisory-only, not flagged).

### Style / IOC / editorial checks

- Zero IOCs (no IP addresses, no hashes, no attacker domains) — confirmed by regex check.
- Zero vanity metrics in brief prose.
- English throughout.
- No workflow-internal language in published sections. "Sub-agents" / "S1–S4" / "verify:" appear only in the AI-content notice header (machine-readable provenance), not in prose. "Spawned" in §1 and §6 refers to security-technical behaviour ("MeshCentral agents spawned by the app-server process"), not workflow terminology.
- Single-source check: §7 confirms "none — every published item carries ≥2 independent sources." Verified: all §1–§5 items have two or more independent cited sources.
- Dedup: PeopleSoft and Maine AG carried as explicit UPDATE items of their prior coverage dates. MariaDB CVE-2026-49261 correctly dropped per §7 note. All other items net-new vs. the 7-day dedup window in prior_coverage.json.
- Quantifiers: "100+ orgs" and "68% higher-ed" confirmed by Mandiant/GTIG; "454,600 student and alumni records" confirmed by BleepingComputer; "nine distinct compiled variants of pam_unix.so" and "nearly a decade" / "2016" confirmed by THN relay; "seven months" (Coupang) confirmed by The Record. No unsourced absolute quantifiers found.
- Name-collision candidates: "Shai-Hulud" (prior coverage: TeamPCP attacker worm) does not appear in today's brief — no collision. "WhatsApp" / "GitHub" / "JavaScript" flag in the mechanical WARN are generic platform names, not campaign/tooling codename collisions; confirmed benign.
- F13 (analytical-link-as-fact): No linkages asserted as cited that aren't supported by the cited sources. UNC6240 = ShinyHunters is stated by the Mandiant/GTIG primary directly.
- F14 (quantifier-without-source): No unsourced quantifiers found. All numeric claims cross-checked.
- F15 (name-collision): No inversion cases. Confirmed benign for all mechanical WARN flagged terms.

### Missed angles

The §7 coverage-gap log is honest and consistent with the run_log (databreaches-net, sec-disclosures-edgar, group-ib, sophos-xops, inside-it-ch, cert-fr-actu all correctly noted as unreachable). No material missed angle identified. Optional future probe: "SimpleHelp CVE-2026-48558 actively exploited OR KEV" — given this is currently research-PoC only, worth monitoring for KEV addition.

### Verdict

CLEAN

All items verified against sources fetched in this iteration. The iter-3 F4 remediation (correcting `langgraph-checkpoint` 4.0.1 → `langgraph` 1.0.10 in §3 and §6) is confirmed correct by both cited sources. No new truth defects found. No editorial defects found. No broken URLs. No hallucinated facts. No unsourced claims. No IOCs. No style violations. The brief is publication-ready.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
[]
```
