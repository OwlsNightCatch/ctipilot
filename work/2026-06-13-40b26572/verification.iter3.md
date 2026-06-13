**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-13T12:20:16Z · ended_at=2026-06-13T12:23:42Z · duration_seconds=206
**Self-telemetry:** webfetch_calls=14 · websearch_calls=0 · bridge_fetches=2 · urls_checked=15

## Verification report — briefs/2026-06-13.md (iteration 3)

Cold hostile read on both axes. Env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID were unset at spawn,
so the Model line is derived from runtime context per the fallback rule.

Every cited URL fetched (Oracle PSIRT via tools/fetch_source.py bridge after a WebFetch 403; Sygnia
Operation Highland confirmed UA-blocked as §7 discloses). Named entities cross-checked against the
sources fetched this iteration. One truth defect found; all other prior-iteration concerns
re-derived clean.

### Unsupported / hallucinated facts

**F4 — §3 LangGraph item: `langgraph-checkpoint` 4.0.1 is not in either cited source.**
Brief (§3, line 61): "the fixes shipped in `langgraph-checkpoint-sqlite` 3.0.1 (CVE-2025-67644),
`langgraph-checkpoint` 4.0.1 (CVE-2026-28277) and `langgraph-checkpoint-redis` 1.0.2
(CVE-2026-27022)." Repeated in §6 Action Items (line 118): "pin `langgraph-checkpoint-sqlite`
>=3.0.1 / `langgraph-checkpoint` >=4.0.1 / `langgraph-checkpoint-redis` >=1.0.2".

- Check Point Research (cited primary, fetched this iteration) states the fix for CVE-2026-28277
  is `langgraph 1.0.10+` — package name `langgraph`, version 1.0.10, NOT `langgraph-checkpoint 4.0.1`.
  Verbatim: "Users should update to `langgraph-checkpoint-sqlite 3.0.1+`, `langgraph 1.0.10+`, and
  `langgraph-checkpoint-redis 1.0.2+`."
- The Hacker News (cited Additional source, fetched this iteration) states the same versions and
  explicitly: "The article does not mention a 'langgraph-checkpoint 4.0.1' version."

Both the package name and the version for the CVE-2026-28277 fix are wrong. Correct to
`langgraph` 1.0.10 in §3 and §6. (The sqlite 3.0.1 and redis 1.0.2 strings match the cited
primary and are fine; THN gives redis 1.0.1 but Check Point — the authoritative primary — says
1.0.2, so leave it.) Truth-class: the brief asserts a remediation version a reader would pin
that no cited source supports.

### Re-derived clean (prior-iteration concerns and own truth pass — no finding)

- §0 / §4 PeopleSoft: CVE-2026-35273, CVSS 9.8, UNC6240/ShinyHunters, PeopleTools 8.61/8.62,
  Environment Management / PSEMHUB, 27 May–9 June window, 100+ victims / 68% higher-ed, MeshCentral-
  as-Azure, SSH fan-out, KEV 12 June — all supported by Mandiant/GTIG + Rapid7. Oracle PSIRT (bridge)
  confirms 8.61/8.62 + CVSS 9.8 + Updated-Date 2026-06-10 (the "OOB patch 2026-06-10" claim).
  Nottingham 454,600 records + passport numbers: NOT on the Nottingham page itself, but fully
  carried by BleepingComputer (cited Additional source on the §4 item). Supported.
- §1 Novo Nordisk: the Novo Nordisk press-release HTML surfaces only "personal data copied" +
  "systems offline"; the full pseudonymised clinical-trial field list and the HCP
  name/phone/WhatsApp list are carried verbatim by BleepingComputer (cited Additional source) and
  The Register (cited Additional source, HTTP 200 — the trailing /5254812 article-ID is benign).
  Supported.
- §1 Atomic Arch: ~400 AUR packages, atomic-lockfile, Rust stealer, eBPF rootkit, PKGBUILD,
  Sonatype-2026-003775, CVSS 8.7, ~1,500 estimate, second-wave js-digest/lockfile-js + Bun —
  all in the Sonatype primary; BPF map paths /sys/fs/bpf/hidden_{pids,names,inodes},
  CAP_BPF/CAP_SYS_ADMIN in ioctl.fail. (Minor: the inline cite on the second-wave/CVSS/~1,500
  clause points to BleepingComputer, which does not carry those specifics — but the Sonatype
  primary cited on the same item does, so every fact is sourced. Advisory-only, not flagged.)
- §1 Coupang: ₩624.7 bn record fine, former engineer / signing key / forged tokens / seven months /
  "deficiencies in basic safety management" / ~6 months log deletion — all in The Record;
  corroborated by BleepingComputer. §7 aggregator-only reduced-confidence note present and honest.
- §2 SimpleHelp CVE-2026-48558: OIDC signature-not-verified auth bypass, Technician session,
  MFA bypass, fixed 5.5.16 / 6.0 RC2, affected 5.5.15-and-earlier, Security Notice 2026-05, CVSS
  n/a — Horizon3 + SimpleHelp advisory both support; neither states a CVSS, so n/a is correct.
- §3 Agentjacking: Tenet Security, Sentry DSN, markdown-injected error events, developer-privilege
  execution, EDR/WAF/IAM/VPN bypass, Sentry declined root-cause fix / content-filter only, no CVE —
  all in THN relay. Tenet originator UA-blocked exactly as §7 discloses.
- §3 Google/Outsider: "Outsider Enterprise", China-based, Telegram, credential capture, AI-generated
  HTML imported into the kit — Google blog confirms the org/China/Telegram; THN secondary confirms
  the AI-code-into-kit technique verbatim. The brief's "postal/parcel/tax lures" is a soft
  analytical mapping onto Swiss/EU themes (sources say 290+ templates impersonating trusted
  institutions + brokerage/carrier lures); within analytical-framing latitude, not flagged.
- §4 Maine AG: specific press release, hoax confirmation + portal-offline all supported.
- §5 Velvet Ant: Operation Highland, China-nexus, air-gapped ~decade/since 2016, nine pam_unix.so
  variants, magic password, credential-logging sshd — all in THN relay; T-IDs (T1556.003, T1554,
  T1078, T1021.004, T1036.005) map correctly to the described behaviour and link to live ATT&CK pages.
- Style: zero IOCs, zero vanity metrics, English throughout, no workflow-internal language in prose
  (grep hits are the AI-content notice, the `**Sub-agents:**` footer, the §7 S1/S2 provenance note,
  and legitimate detection content). Single-source: §7 "none" is correct — every item >=2 sources.
  Quantifiers all sourced. No name-collision inversion (Atomic Arch / Shai-Hulud lineage is
  consistent across coverage). No analytical-link-as-fact. Dedup: PeopleSoft + Maine AG correctly
  carried as UPDATEs of 2026-06-12; MariaDB CVE-2026-49261 correctly dropped; all other items net-new.

### Missed angles

None material. The §7 coverage-gap log (databreaches-net, sec-disclosures-edgar, group-ib,
sophos-xops, inside-it-ch, cert-fr-actu) is honest and consistent with the run_log. Suggested
optional probe for a future run if SimpleHelp gains traction: search
"SimpleHelp CVE-2026-48558 exploited OR KEV" to catch any ITW pivot, since this item is currently
research-PoC only.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One truth defect: F4 (LangGraph fix version `langgraph-checkpoint` 4.0.1 -> `langgraph` 1.0.10,
in §3 and §6). Everything else verified clean against sources fetched this iteration. Fixing F4
should clear the brief to CLEAN.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: research-investigative
  item: "Check Point chains SQL injection to RCE in LangGraph's checkpointer (CVE-2025-67644 + CVE-2026-28277)"
  url_or_quote: "the fixes shipped in `langgraph-checkpoint-sqlite` 3.0.1 (CVE-2025-67644), `langgraph-checkpoint` 4.0.1 (CVE-2026-28277) and `langgraph-checkpoint-redis` 1.0.2 (CVE-2026-27022)"
  summary: >-
    The package+version `langgraph-checkpoint` 4.0.1 for CVE-2026-28277 is supported by
    neither cited source. Check Point Research (cited primary) states the fix is
    `langgraph 1.0.10+`; The Hacker News (cited secondary) states the same and explicitly
    notes it 'does not mention a langgraph-checkpoint 4.0.1 version'. Correct to
    `langgraph` 1.0.10 (the package name AND the version are both wrong). Defect
    propagates to the §6 Action Items line ('pin ... `langgraph-checkpoint` >=4.0.1').
```
