**Model:** Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-26T04:45:31Z · ended_at=2026-06-26T04:47:46Z · duration_seconds=135

## Verification report — briefs/2026-06-26.md (iteration 2)

Read cold from disk. Prior-iteration deltas block received and walked first. URLs fetched in this iteration: 404 Media, The Next Web, Abnormal Security, Mandiant/GTIG, Cisco PSIRT (cisco-sa-sdwan-privesc-4uxFrdzx), SentinelLABS (macOS.Gaslight), Infosecurity Magazine, ESET WeLiveSecurity (Gamaredon), Sekoia (redirected to sekoia.com), The Record (Ukrposhta), New Voice of Ukraine, MITRE T1566.004, MITRE T1078.004. Total: 13 URLs fetched.

---

## Prior-iteration delta walkthrough

### Delta 1 — F1 remediation (Entra attribution)

**Iter-1 finding:** The original brief asserted "Microsoft Entra, the platform MSG uses for identity and network access" attributed to 404 Media's review. No cited source supports this.

**Remediation claimed:** Rewrote the item — "identity and network-access platform" in body; Entra/Okta specificity framed as Abnormal's generic documentation; TL;DR softened.

**Verification:**
- TL;DR bullet (line 11): now reads "the company's identity and network-access platform" — CORRECTLY HEDGED.
- Body text (line 26): reads "places the foothold at the company's identity and network-access platform" — CORRECTLY HEDGED.
- Body (line 26): "the vishing → identity-platform (Entra/Okta) → MFA-enrollment → SSO-pivot chain that Abnormal Security documents generically" — CORRECTLY attributed to Abnormal as a generic pattern.
- **Section heading (line 24): "ShinyHunters used a single vishing call into Microsoft Entra to breach Madison Square Garden."** This still asserts "into Microsoft Entra" as a specific fact about the MSG incident.

Fetched 404 Media (404media.co/how-hackers-broke-into-madison-square-garden/): confirms vishing, low-level employee granted "system access," 45GB. Does NOT name Microsoft Entra. Does NOT attribute to ShinyHunters.

Fetched The Next Web (thenextweb.com/news/shinyhunters-madison-square-garden-45gb-data-leak-facial-recognition): names ShinyHunters, 45GB, 26M records, June 15 deadline, June 16 publication. Does NOT mention vishing or Entra.

Fetched Abnormal Security (abnormal.ai/blog/shinyhunters-sso-social-engineering-mfa-identity-compromise): lists "Okta, Microsoft Entra, Google Identity" as GENERIC example platforms in the SSO attack class. Not MSG-specific. Page dated 2026-02-06.

The heading "into Microsoft Entra" is unsupported by any cited source as a MSG-incident-specific fact. The body and TL;DR remediation is correct, but the heading was not updated to remove the unsupported Entra specificity. This is a residual F13 (analytical-link-as-fact) finding.

**Is ShinyHunters still correctly the attacker?** Yes — The Next Web names ShinyHunters as the attacker; MSG as victim. No inversion.

### Delta 2 — F2 remediation (citation date drift)

**Remediation claimed:** Corrected to [Abnormal Security, 2026-02-06] and [Sekoia, 2026-06-04].

**Verification:**
- Line 26: `[Abnormal Security, 2026-02-06]` — confirmed, matches actual page date.
- Line 48: `[Sekoia, 2026-06-04]` — confirmed, Sekoia page (now at sekoia.com/blog/...) metadata shows June 4, 2026.
- Line 52 (footer): `· Additional source: [Sekoia](https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/)` — no inline date in the footer (per brief template: footer has no date, the inline inline citation carries the date). The citation in the body at line 48 correctly reads [Sekoia, 2026-06-04].

Both date corrections are correctly applied. F2 fully resolved.

---

## Fresh truth pass

### Cisco SD-WAN Manager CVE-2026-20245 (deep dive priority check)

Fetched Mandiant/GTIG (cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager): CONFIRMS all major claims — CVE-2026-20245, zero-day exploitation at communications service provider from late 2025 through March 2026 before patch, peering-bypass via CVE-2026-20127/CVE-2026-20182, SSH as vmanage-admin, tenant-upload CSV injection, troot UID-0 account creation, anti-forensic admin-password-revert-then-restore, command history deletion. "Threat actor" described without name — NO named attribution. Fixed trains listed: 20.9.9.2, 20.12.7.2, 20.15.4.5, 20.15.5.3, 20.18.3.1, 26.1.1.2 — ALL confirmed.

Fetched Cisco PSIRT (cisco-sa-sdwan-privesc-4uxFrdzx): CONFIRMS advisory ID `cisco-sa-sdwan-privesc-4uxFrdzx`, CVSS 7.8, CWE-116, same fixed version list, post-auth with netadmin privileges. No workaround confirmed.

Brief's claim "Mandiant names no threat actor" — CONFIRMED. Brief's fixed-version list — CONFIRMED against both sources. Advisory ID — CONFIRMED.

### macOS.Gaslight

Fetched SentinelLABS (sentinelone.com/labs/macos-gaslight-rust-backdoor-...): CONFIRMS Rust implant, DPRK high confidence, XProtect MACOS_BONZAI_COBUCH, AIRPIPE rule, 3.5 KB blob, 38 fabricated system messages, Telegram Bot-API C2 with AES-GCM payloads, cert-pinned TLS, LaunchAgent `com.apple.system.services.activity`, CPython 3.10.18 staged at runtime, login.keychain-db. ALL confirmed.

Fetched Infosecurity Magazine (infosecurity-magazine.com/news/macos-gaslight-rust-backdoor/): corroborates North Korea attribution, 38 fabricated system messages, Telegram Bot API C2, same technical details. CONFIRMED as corroborating secondary.

### ESET Gamaredon "exclusively Ukrainian targeting"

Fetched ESET WeLiveSecurity (welivesecurity.com/en/eset-research/gamaredon-2025-...): page explicitly states "Throughout 2025, Gamaredon exclusively targeted governmental and military institutions in Ukraine." No EU or non-Ukrainian targets mentioned. Brief's framing "targeting stayed exclusively Ukrainian government and military — the report names no EU targets" — CONFIRMED verbatim.

Six PowerShell tools named (PteroDee, PteroCache, PteroDum, PteroOdd, PteroEffigy, PteroPaste) plus PteroSetup VBScript: CONFIRMED. Cloudflare tunnels, Workers, Microsoft DevTunnels, Loophole, No-IP DDNS, Clever Cloud, Supabase: CONFIRMED. rclone to Wasabi, Tebi, Intercolo (primary by December): CONFIRMED. Dead-drop resolvers on Telegram, Telegra.ph, Dropbox, GoFile, Mastodon, paste services: CONFIRMED. Turla collaboration (early 2025): CONFIRMED.

Sekoia citation date [Sekoia, 2026-06-04]: CONFIRMED (see delta-2 above).

### Ukrposhta

Fetched The Record (therecord.media/ukraine-state-postal-operator-reports-disruption): CONFIRMS Ukrposhta cyberattack June 25 2026, mobile app and digital services disrupted, IT Army of Russia claiming prior breach and data exfiltration, Recorded Future News could not independently verify. Brief's framing "Recorded Future News states it could not independently verify" — CONFIRMED.

Fetched New Voice of Ukraine (english.nv.ua/business/cyberattack-disrupts-ukrposhta-app-and-digital-services-50619276.html): CONFIRMS "due to an overnight hostile cyberattack on IT systems, the Ukrposhta mobile application is temporarily experiencing disruptions." Both sources resolve correctly.

### Name-collision WARN (ShinyHunters — check_brief.py flag)

ShinyHunters appears in prior coverage across multiple dates, always referring to the same threat actor (UNC6240 in W-25 context). Prior coverage: Kodak breach (2026-06-20), One Medical pressure (2026-06-21), Council of Europe / weekly multi-day item (2026-W25). All instances refer to the same criminal extortion brand. Today's brief adds the MSG breach by the same actor. This is the same entity — not a name-collision with a different actor or a defender/attacker inversion. The check_brief.py WARN is benign; no F15 finding warranted.

### Editorial quality

Coverage shape: §1 leads with Ukrposhta (Ukraine, European-postal pattern, CH/EU relevance via defender takeaway) then ShinyHunters/MSG (US victim, kill chain transferable to EU public sector). §2 intentionally empty with specific justification. §3 macOS.Gaslight and Gamaredon are research/annual-report items with transferable defensive value. §4 UPDATE for CVE-2026-20245. §5 deep dive earns length — documented kill chain, hunt/detection, hardening. §6 Action Items are specific and actionable. §7 Verification Notes includes item drops with specific rationale and source-health notes.

No IOCs, no vanity metrics, English throughout. No workflow-internal language leaked. Source variety is appropriate (primary research vendors, secondary reporters).

---

### Analytical-link-as-fact (residual from F1)

**F1 (residual — section heading, analytical-link-as-fact / F13 class).** §1 ShinyHunters/MSG, section heading (line 24):

> "ShinyHunters used a single vishing call **into Microsoft Entra** to breach Madison Square Garden"

Fetched all three cited sources in this iteration:
- 404 Media: says "granted system access," no mention of Microsoft Entra, no named platform.
- The Next Web: names ShinyHunters as attacker, no mention of Entra or vishing.
- Abnormal Security: lists "Okta, Microsoft Entra, Google Identity" only as generic example SSO platforms in a kill-chain description not specific to MSG.

The heading asserts "into Microsoft Entra" as a specific fact about the MSG breach — what platform MSG's identity system runs on, and what the attackers targeted. No cited source supports this as an MSG-specific fact. The body text and TL;DR were correctly remediated in iteration 1 (they now say "the company's identity and network-access platform" without asserting Entra). The heading was not remediated. This is a narrow, targeted fix: change the heading's "into Microsoft Entra" to "into the company's identity platform" or equivalent non-assertive language.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One residual truth finding: the section heading "into Microsoft Entra" asserts Entra as the specific MSG-incident platform. No cited source supports this. The body and TL;DR are correctly hedged. Fix is localized to the heading only.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F13
  category: analytical-link-as-fact
  section: active-threats
  item: "ShinyHunters used a single vishing call into Microsoft Entra to breach Madison Square Garden"
  url_or_quote: "Section heading line 24: 'ShinyHunters used a single vishing call into Microsoft Entra to breach Madison Square Garden'"
  summary: "Heading asserts 'into Microsoft Entra' as a specific MSG-incident fact. Fetched 404 Media (says 'system access', no Entra, no ShinyHunters named), The Next Web (names ShinyHunters, no Entra or vishing), Abnormal Security (lists Entra only as a generic SSO example, not MSG-specific). No cited source confirms MSG uses Microsoft Entra or that the vishing call targeted Entra specifically. Body and TL;DR correctly hedged in iter-1 remediation; heading was not updated. Fix: change heading to 'into the company's identity platform' or equivalent."
```
