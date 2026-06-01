**Model:** Claude Opus 4.8 (`claude-opus-4-8[1m]`) — env vars CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID unset; identified from runtime context
**Timestamps:** started_at=2026-06-01T04:55:59Z · ended_at=2026-06-01T04:58:03Z · duration_seconds=124

## Verification report — briefs/2026-06-01.md (iteration 3)

Read cold. All 8 cited Source/Additional-source URLs WebFetched this iteration (PostHog status, Microsoft npm, Sonatype, SANS ISC, Risky Biz, EDRi, Osservatorio Morpheus, Osservatorio Spyrtacus) plus 2 MITRE technique pages (T1516, T1626). IOC-leak sweep run against brief text.

### Truth pass — all PASS
- **URLs:** all 8 cited URLs resolve and land on specific articles/advisories/status-pages (no homepages, listings, or NVD/MITRE per-CVE pages). PostHog incident page is a specific incident ID; Microsoft/Sonatype are specific blog slugs; SANS is a specific diary id (33034); EDRi + both Osservatorio pages are specific posts.
- **PostHog (§0/§1/§6):** start 01:03 UTC, rotation 01:18, resolved 07:16 UTC, AWS credential rotation, no customer data compromised, vector undisclosed — all confirmed by status page. Risky Biz additional source corroborates "rotated all AWS credentials... researchers demonstrated an exploit... no customer data was compromised." T1190 sensibly applied.
- **npm Microsoft (§0/§1/§6):** 45 packages (26+7+12), nine org scopes, aliases mr.4nd3r50n/ce-rwb/t-in-one, versions 100.100.100 & 3.5.22, kill-switch T_IN_ONE_NO_TELEMETRY, run-once marker ~/.cache/._t-in-one_init/, CI/CD detection, repos taken down — all confirmed. Brief's honest note that the post is titled "33" while the body enumerates 45 is accurate. No attribution asserted (correct; source emails are @yandex.ru / C2 oob.moika[.]tech but brief does not over-attribute).
- **npm Sonatype (§1):** 176 packages, Sonatype-2026-003429, version 99.99.99, Russian-language comments framed as observation not attribution — confirmed. T1195.002 + recon T1082/T1083/T1614 sensibly applied.
- **SANS ISC (§0/§3/§6):** Brad Duncan, diary 2026-06-01, infection 2026-05-27, SmartApeSG ClickFix, processor.vbs (109 bytes), token.bat, setup.cab (17,275,805 B ≈ 17 MB), install path C:\ProgramData\UpdateInstaller\, NetSupport final payload, encoded-not-TLS over TCP/443, staging RAT active since April 2026 — all confirmed. T1204.001/T1059.005/T1070.004/T1219 sensibly applied. [SINGLE-SOURCE] flag present and § 7 single-source line present with HIGH-reliability framing.
- **Deep dive (§5):** EDRi 2026-05-28 confirmed (Morpheus/Spyrtacus, IPS Intelligence, SIO, NSO Pegasus, Paragon Graphite contract terminated, ~5,200 trojan interceptions 2024 exceeding other member states, few-euros/day, no centralised oversight, EU-wide ban call with binding transparency). Osservatorio Morpheus 2026-04-23 confirmed (version 2025.3.0, Accessibility/SYSTEM_ALERT_WINDOW/ADB, self-grant, WhatsApp biometric-overlay device pairing, device_config camera_mic_icons_enabled false via ADB, AV-kill Bitdefender/Sophos/Avast/AVG/Malwarebytes). MITRE T1626 (Abuse Elevation Control Mechanism, Mobile) and T1516 (Input Injection, Mobile) verified real and correctly applied. Osservatorio Spyrtacus confirms SIO development, DexGuard, InMemoryDexClassLoader. PD-7 deep-dive analysis exception fairly invoked; older primaries clearly dated; heise hook correctly excluded (TollBit 402) per § 7.

### IOC discipline — PASS
Brief swept for every IP/hash/domain/C2 present in the underlying SANS, Microsoft, Sonatype, and Osservatorio sources (89.110.110.119, 185.163.47.217, hiddenplanetlab.top, oob.moika[.]tech, @yandex.ru, 109.239.245.172, game-host.org, the four SHA256s, etc.). NONE leaked. No bare IPv4 or SHA256 anywhere in the brief. Knowledge carried, indicators stripped — correct.

### Editorial — PASS
Relevance strong (npm scope-lock applies to CH/EU eGov software factories; PostHog EU Cloud; Android-fleet spyware governance; ClickFix hunt). §1 leads CH/EU/public-sector-relevant. §2 and §4 intentionally empty with honest, gate-citing stubs. Deep dive earns its length and ends on a transferable control-surface argument. No Immediate-Actions over-claim (§6 explicitly says no emergency bar met). Primary sources are vendor/research-lab/regulator/handler-diary — no NVD/CERT-only footers. No vanity metrics, no leak-site-as-fact, no workflow-internal language. English throughout. Dedup distinctions (Mini Shai-Hulud / TrapDoor; PAN-OS deep dive) honestly drawn.

### Editorial / less-is-more flags (advisory)
- **F11 — Spyrtacus citation date.** Line 52 cites the Spyrtacus analysis as `2026-04-01`; the fetched page reports a publication date of **9 April 2026**. The URL slug (`/2026/04/`) carries no day, so it does not disambiguate. Every substantive Spyrtacus claim (SIO, DexGuard, InMemoryDexClassLoader) is fully supported regardless. Surfaced as advisory rather than a hard truth finding because the source date I have is summariser-reported, not a verbatim date string I can quote; main agent may correct `2026-04-01` -> `2026-04-09` if a direct read of the page confirms, otherwise leave. Does not block publication.

### Missed angles
None material. Source-coverage gaps (databreaches-net, inside-it-ch, sophos-xops, heise) are honestly logged in § 7; none point to an obvious missed in-window CH/EU story given the dedup context.

### Verdict
CLEAN — the brief is truth-clean and editorially sound. The single F11 item is advisory (citation-date verification) and does not block publication. No F1–F10, F12–F15 findings.

### Findings summary (machine-readable)
```yaml
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "Italy low-cost spyware deep dive — Spyrtacus citation"
  url_or_quote: "[Osservatorio Nessuno — Spyrtacus, 2026-04-01](https://osservatorionessuno.org/blog/2026/04/italian-spyware-maker-sio-still-developing-and-distributing-spyrtacus/)"
  summary: "Brief dates citation 2026-04-01; fetched page reports 9 April 2026. URL slug carries no day. All substantive claims supported. Advisory: summariser-reported date, moderate confidence. Correct to 2026-04-09 if confirmed, else leave."
```
