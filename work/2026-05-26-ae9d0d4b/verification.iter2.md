**Model:** Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-26T04:53:11Z · ended_at=2026-05-26T04:56:01Z · duration_seconds=170
**Self-telemetry:** urls_checked=12 · webfetch_calls=9 · bridge_fetches=1

## Verification report — briefs/2026-05-26.md (iteration 2)

### Prior-iteration delta verification

**F3 Remediation 1 — CVE-2026-9058 specific institutions (CERT Polska source)**
CERT Polska post at https://cert.pl/en/posts/2026/05/CVE-2026-9058/ was fetched. The page describes the CVE in Szafir SDK developed by KIR (Krajowa Izba Rozliczeniowa) and the general vulnerability — return code 0 even when certificate trust status is `nondetermined`. It names no specific affected institutions such as ZUS, Centrum e-Zdrowia, or e-Gate. The brief now reads "Any application that uses the SDK to accept qualified electronic signatures — the typical Polish e-government use case — is exposed." This is accurate and supported by the source. Remediation verified correct.

**F3 Remediation 2 — THN @antv article date**
The THN article at https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html was fetched. Publication date confirmed as May 19, 2026. The article confirms 639 malicious versions across 323 packages and forged Sigstore attestations. The brief now cites it as "The Hacker News, 2026-05-19." Remediation verified correct.

**F14 Remediation 3 — GTIG PhaaS platform count**
GTIG source at https://cloud.google.com/blog/topics/threat-intelligence/chinese-language-phishing-services/ was fetched. The source uses the phrase "a dozen current PhaaS offerings." The brief now reads "around a dozen current Chinese-language PhaaS offerings." Remediation verified correct. No other unsupported quantifiers found in the PhaaS item.

---

### Citation does not support the claim

**F1-NEW (renumbered F1 for this iteration): § 1 ACR Stealer — JPEG payload concealment**

The brief states: "the loader stages a follow-on payload concealed inside a JPEG before running the commodity infostealer"

The cited source, SANS ISC diary 33018, fetched at https://isc.sans.edu/diary/33018, states verbatim: "This image doesn't appear to be malicious, nor could I find any obvious signs of embedded data, but it's somehow related to this infection chain."

The source explicitly does NOT support the claim that a payload is concealed inside a JPEG. The source analyst found no evidence of payload steganography in the image — merely that the JPEG appears somewhere in the infection chain in an unclear capacity. The brief's claim of "payload concealed inside a JPEG" is a stronger assertion than the source makes and is not supported by the only cited source. This is a truth defect.

**Suggested fix:** Change "stages a follow-on payload concealed inside a JPEG before running the commodity infostealer" to "delivers additional stages via a chain that includes a JPEG whose precise role in the infection chain is unclear from the published analysis."

---

### Missed angles

**F2-NEW: Anti-inversion verification — Datadog Security Labs role (§ 4)**
The brief reads: "Datadog Security Labs' static analysis (reported by ISC) describes a modular TypeScript/Bun toolkit for credential harvesting..."

The SANS ISC 33016 source confirms Datadog Security Labs "published a static analysis of a public GitHub repository containing what appears to be the complete TeamPCP framework." This is an analyst/researcher role — Datadog is analyzing an attacker's open-sourced framework. The brief correctly describes Datadog as producing analysis of the open-sourced attacker framework, NOT releasing a defender tool. Anti-inversion concern is clear: no inversion found. The § 4 text accurately represents Datadog's passive analytical role.

**F3-NEW: Missed angle — supply-chain worm duplication check**
The dedup context confirms the § 4 TeamPCP UPDATE introduces genuine new material vs. 05-21/05-22 coverage: (1) the 05-21 brief covered GitHub internal breach and `durabletask` poisoning at a high level; the 05-25 SANS ISC source provides consolidated technical detail through 05-24, including the wiper extension, the forged Sigstore badge specifics, and the open-source copycat fork proliferation — these are in-window escalations. (2) The 05-22 update covered SLSA Build Level 3 attestation being invalidated via genuine CI compromise; today's § 4 now adds forged Sigstore badges in the npm UI as a distinct attack on trust signals from a different direction. The brief's framing ("package provenance is now under attack from both directions at once") is accurate and non-duplicative. No dedup concern.

---

### Name-collision unflagged

**Advisory: GitHub and WebAuthn name-collision WARNs from mechanical gate**
- "GitHub" in § 1 TrapDoor: used as a common noun referring to GitHub the platform/registry. No prior coverage uses "GitHub" as an attacker or campaign name that could create confusion. This is a false-positive WARN from the mechanical gate. No finding.
- "WebAuthn" in § 3 GTIG PhaaS: WebAuthn is used as a defensive technology standard (FIDO2/WebAuthn as countermeasure). No prior coverage uses "WebAuthn" as an attacker tool or campaign name. False-positive WARN. No finding.

Both name-collision WARNs confirmed as common-noun false positives with no attacker/defender inversion.

---

### Whole-brief checks

**IOC check — RemotePE § 5**
The Fox-IT source contains C2 domains (livedrivefiles[.]com, aes-secure[.]net, azureglobalaccelerator[.]com, etc.) and SHA256 sample hashes. The brief deliberately omits these, noting "(no IOCs)" in the detection section. The THN article also mentions aes-secure[.]net. The brief correctly carries no IOCs. Confirmed clean.

**§ 0 TL;DR / § 2 CVE-2026-9058 consistency**
Both sections now use generalised language without institution names. Consistent.

**§ 2 CVE-2026-5426 — sourcing and claims**
GTIG source confirmed: CVE-2026-5426, shared machineKey, ViewState deserialization RCE, BLUEBEAM/Godzilla web shell, w3wp.exe, Japan-based Digital Knowledge, zero-day pre-2026-02-24. MNDT-2026-0009 GitHub advisory confirmed CVE-2026-5426 and shared machineKey. All claims verified.

**§ 1 TrapDoor — sourcing**
Socket source confirmed: 34+ packages, 384+ versions, earliest activity 2026-05-22 ~20:20 UTC, AWS/GitHub token validation, zero-width Unicode in .cursorrules and CLAUDE.md. THN article confirmed same campaign facts. All key claims verified.

**§ 4 TeamPCP UPDATE sourcing — SANS ISC 33016**
SANS ISC 33016 confirmed: framework open-sourced ~2026-05-22, Datadog Security Labs static analysis, copycat forks, @antv wave with 639 versions across 323 packages, 42 packages with forged Sigstore badges, durabletask 1.4.1-1.4.3 trojanised with Linux disk wiper, echarts-for-react ~1.1M and size-sensor ~4.2M weekly downloads. All claims verified. Article published 2026-05-25, within window.

**§ 3 GTIG PhaaS — sourcing**
GTIG source confirmed: "a dozen current PhaaS offerings," real-time OTP relay, RCS/iMessage delivery, Puppeteer-driven AI page cloning, 119 countries, Europe named as targeted region, UNC5814/Darcula link, YY Lai Yu case study, FIDO2/WebAuthn as countermeasure. All claims verified.

**§ 5 RemotePE deep dive — Telegram social engineering**
The Fox-IT source does not mention Calendly/Picktime or Telegram social engineering. The THN article (which IS cited as "Additional source" in § 5) confirms "approached the victim on Telegram under the guise of an existing employee of a trading company and scheduling a meeting on fake Calendly and Picktime domains." The Telegram/Calendly/Picktime social engineering claim in § 5 is backed by the cited THN additional source. Claim verified.

**§ 7 drops — consistency check**
The five drops noted in § 7 align with the dedup context:
- Glasswing/Claude Mythos: not in dedup context, correctly dropped on fake-news/vanity grounds.
- Packagist dup: covered 2026-05-24 deep dive. Correct.
- Oncology/TriZetto: US nexus, outside 36h window. Correct.
- Charter no-delta: covered 2026-05-25, no new development today. Correct.
- CVE-2026-9256 nginx-poolslip: § 7 notes the valuable detail (patch for 42945 doesn't cover 9256; requires 1.31.1+/1.30.2+). Correctly retained as a § 7 note rather than a § 2 item given medium severity and no ITW exploitation. Correct.

**Coverage shape — § 1 leads appropriately**
CVE-2026-9058 in § 2 carries a CH/EU public-sector primary focus. § 3 GTIG PhaaS explicitly names Europe. § 5 RemotePE notes European financial institutions. Coverage shape is sound.

**Editorial quality — Single-source items**
Both single-source items correctly flagged inline:
- § 1 ACR Stealer: `[SINGLE-SOURCE]` present, SANS ISC is HIGH-reliability for documented malware delivery chains.
- § 3 GTIG PhaaS: `[SINGLE-SOURCE]` present, GTIG is HIGH-reliability primary research.

§ 7 confirms both items with the single-source notice and the "HIGH-reliability primaries" carve-out.

**Style discipline**
No workflow-internal language detected. No IOCs in body. English throughout. No vanity metrics in brief body.

---

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)`

One truth finding (F1): the brief asserts a payload was concealed inside a JPEG; the sole cited source (SANS ISC diary 33018) explicitly states the image "doesn't appear to be malicious, nor could I find any obvious signs of embedded data." The claim is stronger than what the source supports.

All three prior-iteration (iter-1) remediations verified correct. No regressions introduced. The name-collision WARNs (GitHub, WebAuthn) are confirmed false positives. All other Sources resolve, land on specific articles, and support their claims. No IOCs found in published text.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "ACR Stealer distributed through counterfeit Claude AI download pages"
  url_or_quote: "the loader stages a follow-on payload concealed inside a JPEG before running the commodity infostealer"
  summary: "SANS ISC diary 33018 states 'This image doesn't appear to be malicious, nor could I find any obvious signs of embedded data, but it's somehow related to this infection chain.' The source does not support the 'concealed inside a JPEG' claim."
```
