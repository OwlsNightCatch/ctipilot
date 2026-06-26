**Model:** Anthropic Claude (specific model not determined; runtime env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset — harness reports Opus 4.8 (1M context), `claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-26T04:39:30Z · ended_at=2026-06-26T04:53:00Z · duration_seconds=810

## Verification report — briefs/2026-06-26.md (iteration 1)

Read cold from disk. Every cited URL fetched in this iteration (10 distinct URLs: Mandiant/GTIG, SentinelLABS, 404 Media, The Next Web, Abnormal Security, ESET WeLiveSecurity, Sekoia, The Record, Cisco PSIRT, Infosecurity Magazine). New Voice of Ukraine not separately fetched (corroborating secondary, content mirrored by The Record which was fetched). MITRE ATT&CK technique URLs not individually fetched (canonical attack.mitre.org/techniques/<ID> pattern, low risk; technique-to-label mapping spot-checked against descriptions and consistent).

Truth-pass result: the four high-attention items the spawn flagged all check out on their primaries —
- (a) Cisco SD-WAN CVE-2026-20245: advisory ID `cisco-sa-sdwan-privesc-4uxFrdzx`, CVSS 7.8, post-auth (netadmin), fixed trains 20.9.9.2/20.12.7.2/20.15.4.5/20.15.5.3/20.18.3.1/26.1.1.2, no workaround, `troot` UID-0 account, `request tenant-upload` path, peering-bypass CVE-2026-20127/-20182, anti-forensic admin-password-revert — ALL confirmed against both Mandiant/GTIG and Cisco PSIRT. "Mandiant names no threat actor" — CONFIRMED (page refers only to "threat actor").
- (b) macOS.Gaslight: Rust, DPRK high-confidence, XProtect `MACOS_BONZAI_COBUCH`, AIRPIPE rule, 3.5 KB blob, 38 fabricated system messages, `{{DATA}}` token, Telegram Bot-API getUpdates C2, AES-GCM, cert-pinned TLS, LaunchAgent `com.apple.system.services.activity`, CPython staging, login.keychain-db — ALL confirmed against SentinelLABS primary.
- (c) ShinyHunters/MSG: attacker = ShinyHunters, victim = MSG — NO INVERSION (mechanical name-collision WARN is benign). But citation mapping is defective — see F1.
- (d) Gamaredon "exclusively Ukrainian targeting" — CONFIRMED verbatim in ESET paper ("Throughout 2025, Gamaredon exclusively targeted governmental and military institutions in Ukraine"). Six PteroXxx tools, PteroSetup, tunnel/worker/devtunnel C2, rclone→Wasabi/Tebi/Intercolo (Intercolo primary by December), dead-drops, Turla collaboration — all confirmed.

### Citation does not support the claim

**F1 (truth, analytical-link-as-fact / F13 class).** §1 ShinyHunters/MSG item, opening sentence (line 26):
> "404 Media's review of the stolen Madison Square Garden data and the attackers' own account confirm ShinyHunters gained their foothold by phoning a low-level employee and talking them into granting access to **Microsoft Entra, the platform MSG uses for identity and network access**"

Verified each cited source:
- **404 Media** (https://www.404media.co/how-hackers-broke-into-madison-square-garden/): confirms vishing, low-level employee talked into "granting system access", 45GB, MSG victim. Does NOT name ShinyHunters; does NOT mention Microsoft Entra; says "system access," not Entra specifically.
- **The Next Web** (https://thenextweb.com/news/shinyhunters-madison-square-garden-45gb-data-leak-facial-recognition): names ShinyHunters, 45GB, 26M+ records, missed 15 June deadline. Does NOT mention vishing or Entra.
- **Abnormal Security** (https://abnormal.ai/blog/shinyhunters-sso-social-engineering-mfa-identity-compromise): describes the GENERIC ShinyHunters kill chain and lists "Okta, Microsoft Entra, Google Identity" only as EXAMPLE platforms — it is not a review of the MSG breach and does not state MSG used Entra.

The composite sentence attaches "talking them into granting access to **Microsoft Entra, the platform MSG uses for identity**" to "404 Media's review … confirm." No cited source confirms that the MSG vishing call targeted Microsoft Entra specifically, nor that MSG uses Entra. The Entra specificity is imported from Abnormal's generic example list and asserted as an MSG-incident fact. The vishing-into-identity-platform pattern is real and well-sourced; the **MSG-uses-Entra / call-targeted-Entra** specificity is not. Remediation: either (i) attribute the Entra detail correctly as the generic Abnormal-documented pattern ("the platform class — Entra/Okta/Google — that the ShinyHunters playbook targets") rather than an MSG-specific fact, or (ii) downgrade "Microsoft Entra, the platform MSG uses" to "the company's identity platform" with the kill-chain Entra detail moved into the Abnormal-sourced clause where it belongs. The "Why it matters" paragraph and §6 action item already correctly frame Entra as the generic hunt surface, so the fix is localized to the lead sentence.

### Strengthen primary source / minor source-metadata

**F2 (editorial, low severity — date drift on Additional sources).** Two cited dates do not match the fetched pages:
- Abnormal Security is cited as `[Abnormal Security, 2026-06-24]` (line 26). The page is dated **Feb 6, 2026**. As an Additional source for a generic kill-chain analysis this is fine to keep, but the date should read 2026-02-06.
- Sekoia is cited as `[Sekoia, 2026-06-25]` (lines 48, 52). The fetched Sekoia "FSB's Matryoshka #3/3: GammaSteel" article is dated **June 4, 2026** (updated). Content claim (S3-compatible exfil to Tebi, dead-drops, Supabase payload hosting, tunnel C2) is supported, but the date and the framing "Sekoia independently documented the same 2025 shift … 2026-06-25" should read 2026-06-04. The "independently documented … in its parallel series" claim is accurate; only the date is wrong.

Neither changes the substance; both are verifiable date corrections to keep the citations honest.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

F1 is the load-bearing finding: a specific factual claim (MSG uses Microsoft Entra / the vishing call targeted Entra) attributed to "404 Media's review … confirm" that no cited source supports as an MSG-incident fact. F2 is two minor Additional-source date corrections. Everything else in the brief — all primary-source technical detail, attribution, CVE/version/advisory-ID facts, Gamaredon victimology, the ShinyHunters attacker/victim direction, §2-empty justification, deep-dive kill chain, action items — verified clean against sources fetched this iteration. Coverage shape is sound: §1 leads CH/EU-relevant (Ukrposhta European-postal pattern, then identity-platform kill chain transferable to EU public sector); §2-empty is justified and the §7 drop log is specific and well-reasoned; deep dive earns its length; no IOCs, no vanity metrics, English throughout, no workflow language leaked.

Missed-angle note (not a finding): the §7 catch-up note on PixelSmash/CVE-2026-8461 (FFmpeg MagicYUV, Nextcloud/Jellyfin server-side preview) is the right thing to watch for CH/EU public-sector; no action needed this run.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: analytical-link-as-fact
  section: active-threats
  item: "ShinyHunters used a single vishing call into Microsoft Entra to breach Madison Square Garden"
  url_or_quote: "404 Media's review of the stolen Madison Square Garden data and the attackers' own account confirm ShinyHunters gained their foothold by phoning a low-level employee and talking them into granting access to Microsoft Entra, the platform MSG uses for identity and network access"
  summary: "No cited source supports MSG-uses-Entra / call-targeted-Entra as an MSG-incident fact. 404 Media says 'system access' (no Entra, no ShinyHunters); The Next Web names ShinyHunters but no vishing/Entra; Abnormal lists Entra only as a generic example platform, not MSG-specific. Entra specificity imported from generic kill-chain and asserted as incident fact. Reattribute Entra to the generic Abnormal-documented pattern or downgrade to 'the company's identity platform'."
- code: F2
  category: strengthen-primary-source
  section: active-threats
  item: "ShinyHunters/MSG (Abnormal cite) and Gamaredon (Sekoia cite) date drift"
  url_or_quote: "[Abnormal Security, 2026-06-24] (actual page date 2026-02-06); [Sekoia, 2026-06-25] (actual page date 2026-06-04)"
  summary: "Two Additional-source citation dates do not match the fetched pages. Abnormal blog is dated 2026-02-06 not 2026-06-24; Sekoia FSB's-Matryoshka-3/3 GammaSteel article is dated 2026-06-04 not 2026-06-25. Content claims on both are supported; correct the dates only."
```
