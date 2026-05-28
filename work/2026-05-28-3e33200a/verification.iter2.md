**Model:** Anthropic Claude (claude-sonnet-4-6)
**Timestamps:** started_at=2026-05-28T04:58:08Z · ended_at=2026-05-28T05:02:56Z · duration_seconds=288
**Self-telemetry:** webfetch_calls=15 bridge_fetches=3 urls_checked=18

## Verification report — briefs/2026-05-28.md (iteration 2)

Even-iteration Sonnet rotation (v2.47). Prior-iteration deltas block received; walked all 11 remediations before cold-read pass. Full brief read end-to-end.

### Iter-1 remediation walkthrough

**F4 — TanStack scope (§ 5):** Post-remediation text reads "malicious versions across approximately 42 `@tanstack/*` npm packages were published with a credential-stealing payload... The Nx postmortem specifically names `@tanstack/zod-adapter@1.166.15` as the resolved malicious dependency." GHSA-g7cv-rxg3-hmpx fetched: title is "Malware in 42 @tanstack/* packages exfiltrates cloud credentials, GitHub tokens, and SSH keys"; advisory lists zod-adapter among the 42 affected packages. Nx postmortem fetched: explicitly names "@tanstack/zod-adapter@1.166.15". Both claims are now supported. **Remediation: CORRECT.**

**F4 — Roundcube `_user` / `preg_replace` (§ 2):** Post-remediation § 2 text reads "an unauthenticated network attacker can inject arbitrary SQL through the plugin's login-time virtual-user lookup when the plugin is enabled" — no `_user` or `preg_replace()` detail present. NCSC-CH 12596 (bridge-fetched) confirms: "CVE-2026-48842 (HIGH) - Pre-authentication SQL injection in the virtuser_query plugin" with no parameter naming. Roundcube vendor page fetched: no `_user` or `preg_replace` language. **Remediation: CORRECT in § 2 body — but see new finding F4 below (§ 6 action item retains the `_user` parameter claim).**

**F4 — LACMTA exfil figure (§ 1):** Post-remediation text reads "exfiltrated a large volume of emails, backups and other files from LACMTA." Gambit Security page fetched: no exfiltration quantity given. TechCrunch and The Record also carry no specific GB figure. **Remediation: CORRECT.**

**F3 — Ajax citation chain (§ 1):** Post-remediation text: "BleepingComputer and The Record report the underlying API flaw exposed more than 300,000 fan accounts and 42,000+ season-ticket holders" with explicit dual-citation of BleepingComputer and The Record; Ajax victim statement attached separately to "the attacker 'granted himself access...'" quote. BleepingComputer article fetched: confirms "42,000 season tickets affected" and "300,000+ accounts viewable". Ajax victim statement fetched: confirms it does NOT carry the large figures; carries "few hundred people... fewer than 20 stadium bans". **Remediation: CORRECT.**

**F4 — Germany BDI / netzpolitik.org (§ 1):** Post-remediation text: "The Bundesverband der Deutschen Industrie (BDI) and civil-society voices warned of collateral-damage risk." Onvista/dpa fetched: names BDI and quotes Holger Lösch (BDI Vice Executive Director). No netzpolitik.org mention in any cited source — the phrase has been successfully removed. **Remediation: CORRECT.**

**F12 — Germany staffing contradiction (§ 7):** Post-remediation § 7 reads: "Germany Cybersicherheitsstärkungsgesetz staffing figure — onvista (dpa) reports 'more than 350 new positions' across BKA / BSI / Bundespolizei plus ~€50 million per year; t-online reports a notably smaller initial figure (37 additional employees). The brief carries the dpa-sourced ~350 framing because the onvista/dpa wire is more likely to reflect the cabinet's published bill text; the t-online figure may refer to one specific agency or a phased intake." Onvista fetched: confirms 350+ positions and €50M. Body text softened to "order of 350" with parenthetical note "t-online reports a smaller initial figure — see § 7". **Remediation: CORRECT.**

**F4 — FBI SRG alias cluster (§ 1):** Post-remediation text: "tracked variously across cited sources as Luna Moth, Chatty Spider and UNC3753, with the Storm-0252 designation specifically referenced by CyberScoop." All three sources fetched: CyberScoop lists "Chatty Spider, UNC3753, Storm-0252" (no Luna Moth); The Record lists "Luna Moth, Chatty Spider, UNC3753" (no Storm-0252); Help Net Security lists "Luna Moth, Chatty Spider, UNC3753" (no Storm-0252). Post-remediation phrasing correctly attributes Luna Moth to The Record and Help Net Security (via "cited sources"), and Storm-0252 specifically to CyberScoop. **Remediation: CORRECT.**

**F4 — DAEMON Tools footer date (§ 5):** Post-remediation text: "Disc Soft Limited, 2026-05-06" in both inline citations and footer. Disc Soft page fetched: publication date confirmed as "May 6, 2026". **Remediation: CORRECT.**

**F11 — GlassWorm TL;DR takedown time:** Advisory only — no change made. Not escalating. ✓

**F11 — MuddyWater / Industrial Cyber + Symantec dates:** Post-remediation footer reads "Symantec / Broadcom Threat Intelligence (2026-05-12)" and "Industrial Cyber (2026-05-13)" and "The Hacker News (2026-05-26)". Symantec (security.com) fetched: confirmed 12 May 2026. Industrial Cyber fetched: confirmed "May 13, 2026". The Hacker News fetched: confirmed May 26, 2026. § 7 note updated accordingly. **Remediation: CORRECT.**

**F11 — Cybersicherheitsstärkungsgesetz formal name:** Advisory only — defensible compression; no escalation needed. ✓

### New finding from fresh cold-read pass

### Claims missing inline citation / unsupported technical detail retained after remediation

**F4** — § 6 Action Items, second bullet point (Roundcube action item).

Brief claim (line 168): "**Roundcube — upgrade to 1.6.16 LTS or 1.7.1, today if `virtuser_query` is enabled.** Pre-auth SQLi via the login `_user` parameter (CVE-2026-48842, CVSS 8.1) plus three high-severity companion bugs — see § 2."

The `_user` parameter detail is not present in any of the three cited sources. Roundcube vendor page (fetched): describes the vulnerability in terms of the `virtuser_query` plugin but does not name the `_user` login parameter. NCSC-CH 12596 (bridge-fetched): "CVE-2026-48842 (HIGH) - Pre-authentication SQL injection in the virtuser_query plugin" — no parameter name given. Heise Security: confirms CVE IDs without parameter naming.

The iter-1 F4 remediation removed `_user` from the § 2 body paragraph but left it in the § 6 action item, where it now reads as a sourced technical claim. This is the same unsourced technical detail that iter-1 flagged.

Suggested fix: change "Pre-auth SQLi via the login `_user` parameter (CVE-2026-48842, CVSS 8.1)" to "Pre-auth SQLi in the `virtuser_query` plugin (CVE-2026-48842, CVSS 8.1)".

### Quantifier without source

**F14** — § 5 Deep Dive, background paragraph (line 134).

Brief claim: "GitHub's CISO Alexis Wales publicly confirmed that the resulting credential-harvest reached approximately 3,800 internal repositories — **the first time** a primary developer platform has been named as a downstream victim of this campaign class."

The Help Net Security article (fetched) reports the GitHub breach and Alexis Wales's statement without using "first time" language. The Nx postmortem (fetched) does not use "first time" language. No cited source supports the quantifier "the first time." This is an analytical claim the brief adds as emphasis with no sourcing.

Suggested fix: remove "the first time a primary developer platform has been named as a downstream victim of this campaign class" or replace with "the first documented instance of this campaign class reaching a primary developer platform's internal repositories, per GitHub's public disclosure" if the CISO's statement actually uses that framing (none of the cited sources do).

### Missed angles

**F10** — The brief covers TeamPCP / Mini Shai-Hulud via Help Net Security referencing the Aikido.dev research. The Aikido.dev blog (linked in Help Net Security outbound) published the primary reverse-engineering of Mini Shai-Hulud including the TanStack compromise mechanism (`https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised`). This is an unlinked primary research source that provides the deepest technical account of the attack mechanism cited in § 5. The brief's citation chain does not include it. Not a truth defect (the facts are supported by the cited sources), but the detection engineer readership would benefit from the Aikido primary.

Suggested search: `site:aikido.dev "mini shai-hulud" tanstack 2026`

### Verdict

**NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)**

- Truth: F4 ×1 (`_user` parameter claim surviving in § 6 action item — unsourced technical detail not in any cited Roundcube source); F14 ×1 ("the first time" quantifier in § 5 deep dive with no source support).
- Editorial: 0.
- Advisory: F10 ×1 (missed Aikido.dev primary research link for TeamPCP / Mini Shai-Hulud deep dive).

The remaining F11 advisories from iter-1 (GlassWorm TL;DR takedown time; formal Cybersicherheitsstärkungsgesetz name) were correctly left as no-change per iter-1's advisory-only disposition. The § 7 notes are accurate. All other iter-1 remediations are confirmed correct. The brief is otherwise substantively clean.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: action-items
  item: "Roundcube — upgrade to 1.6.16 LTS or 1.7.1 (§ 6 second action item)"
  url_or_quote: "Pre-auth SQLi via the login `_user` parameter (CVE-2026-48842, CVSS 8.1)"
  summary: "`_user` parameter not mentioned in Roundcube vendor page, NCSC-CH 12596 (bridge-fetched), or Heise Security. Iter-1 F4 remediation dropped `_user` from § 2 body but left it in § 6 action item. Fix: replace with 'Pre-auth SQLi in the `virtuser_query` plugin (CVE-2026-48842, CVSS 8.1)'"

- code: F14
  category: quantifier-without-source
  section: deep-dive
  item: "§ 5 Deep Dive — Nx Console / TanStack / DAEMON Tools background paragraph"
  url_or_quote: "the first time a primary developer platform has been named as a downstream victim of this campaign class"
  summary: "Help Net Security (fetched), Nx postmortem (fetched) do not use 'first time' language. Analytical emphasis added by the brief without source support. Fix: remove or recast as analyst inference."

- code: F10
  category: missed-angle
  section: deep-dive
  item: "§ 5 Deep Dive — TeamPCP / Mini Shai-Hulud attack mechanism"
  url_or_quote: "https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised"
  summary: "Aikido.dev published the primary reverse-engineering of the TanStack Mini Shai-Hulud attack mechanism; linked from Help Net Security outbound links but not cited in the brief. Advisory only — not a truth defect."
```
