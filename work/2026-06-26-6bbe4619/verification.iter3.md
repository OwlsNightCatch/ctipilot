**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-26T04:50:18Z · ended_at=2026-06-26T04:52:17Z · duration_seconds=119

## Verification report — briefs/2026-06-26.md (iteration 3)

Cold read, full end-to-end. Every inline source URL fetched in this iteration:
Mandiant/GTIG, SentinelLABS, ESET WeLiveSecurity, 404 Media, The Next Web,
Abnormal Security, Sekoia (followed 301), Cisco PSIRT (bridge), The Record,
New Voice of Ukraine, Infosecurity Magazine, MITRE T1556.006. All resolve to
specific articles/advisories; none are homepages/listings/NVD-CVE pages.

### Truth pass — claims verified against fetched primaries

- **Cisco SD-WAN CVE-2026-20245 (§4 UPDATE + §5 deep dive):** Cisco PSIRT
  `cisco-sa-sdwan-privesc-4uxFrdzx` confirms exact advisory ID, CVE, CVSS 7.8
  (AV:L/AC:L/PR:L), post-auth, no workaround, and ALL SIX fixed versions
  (20.9.9.2 / 20.12.7.2 / 20.15.4.5 / 20.15.5.3 / 20.18.3.1 / 26.1.1.2) verbatim.
  Mandiant/GTIG (2026-06-24) confirms: zero-day at a comms service provider,
  `request tenant-upload` CSV command-injection, `troot` UID-0 account,
  peering-bypass via CVE-2026-20127/-20182, `vmanage-admin` SSH foothold,
  admin-password change-then-revert anti-forensics. **Mandiant attributes to
  NO named actor — confirmed verbatim** ("Unattributed"); brief's "names no
  threat actor" / "attributes the activity to no named actor" is accurate.
  Publication date 2026-06-24 correct.
- **macOS.Gaslight (§0, §3):** SentinelLABS (2026-06-23) confirms Rust backdoor,
  DPRK high-confidence, XProtect `MACOS_BONZAI_COBUCH`, AIRPIPE rule, 3.5 KB blob
  of 38 fabricated system messages with `{{DATA}}` tokens for analyst-LLM
  prompt injection, Telegram Bot-API `getUpdates` C2, AES-GCM, CPython staging,
  `login.keychain-db` copy, LaunchAgent `com.apple.system.services.activity`.
  All brief details match. Infosecurity Magazine (2026-06-24) corroborates.
- **Gamaredon (§0, §3):** ESET (2026-06-25) confirms FSB attribution (18th
  Center FSB per SSU), all six PowerShell tools named verbatim, PteroSetup
  resurrected VBScript weaponizer, tunnel/worker/devtunnel infra, rclone to
  Wasabi/Tebi/Intercolo (Intercolo primary by December 2025), dead-drop
  resolvers, Turla early-2025 collaboration, and **"exclusively Ukrainian
  governmental and military; no EU targets named" — confirmed verbatim**.
  Brief's "exclusively Ukrainian … report names no EU targets" is accurate and
  the §7 note correctly records the dropped sub-agent "EU secondary targeting"
  claim. Sekoia corroboration confirmed (Matryoshka series, 2025 S3/tunnel
  shift, published 2026-06-04).
- **ShinyHunters / MSG (§0, §1):** Attribution chain is correctly layered.
  404 Media (2026-06-24) supports the vishing-call-into-low-level-employee fact
  (cited for exactly that). The Next Web (ShinyHunters attribution, 45GB/26M
  records, missed 15 June deadline) supports those facts. Abnormal Security
  (2026-02-06) supports the generic Entra/Okta vishing→MFA→SSO kill chain and
  the brief explicitly frames it as "the wider pattern … that Abnormal Security
  documents generically." ShinyHunters is correctly the ATTACKER throughout.
  MITRE T1556.006 verified as MFA manipulation. No truth defect.
- **Ukrposhta (§1):** The Record (2026-06-25) confirms overnight cyberattack,
  app/digital-service disruption, "IT Army of Russia" pro-Russian claim of a
  prior breach + user-DB exfil, Recorded Future News "could not independently
  verify," Ukrposhta not confirming data compromise. Brief's unverified-leak
  framing is correct. New Voice of Ukraine resolves to a specific article.

### Editorial / less-is-more flags (advisory)

- **F11 (advisory):** §1 lead sentence — "Reporting attributes the breach to
  ShinyHunters **and places the foothold at the company's identity and
  network-access platform**" — is cited to The Next Web, but neither The Next
  Web nor 404 Media names an identity/network-access platform as the MSG
  foothold; the Entra/Okta detail is Abnormal's *generic* pattern. The brief
  largely self-mitigates: the immediately following sentences explicitly
  attribute the Entra/Okta chain to Abnormal "generically." Borderline
  analytical-link-as-fact (F13), but the surrounding framing does the
  disambiguation, so logged advisory only. Main agent may optionally soften
  "places the foothold at the company's identity and network-access platform"
  to "places the foothold in identity-platform abuse" or move the clause to the
  Abnormal-attributed sentence. Not blocking.
- **F11 (advisory):** §3 Gamaredon Sekoia URL `https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/`
  issues a permanent 301 to `https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel`.
  Content matches the claim (redirect resolves successfully), so not a broken
  URL (not F1). Main agent may optionally update to the canonical
  `www.sekoia.com` URL to avoid a stale-redirect footer. Not blocking.

### Coverage / style

- §1 leads with EU/public-sector nexus (Ukrposhta — EU postal/public-sector
  pattern) before the US ShinyHunters item. §2 intentionally empty with a clear
  justification and §7 records the GitLab / UniFi assessments. Deep dive earns
  its length (control-plane criticality + host-level detection that the vManage
  dashboard cannot surface). No IOCs in prose (Mandiant's IPs/hashes correctly
  excluded). No vanity metrics. English throughout. No workflow-internal
  language leaked. §7 verification notes are thorough and accurate.

### Verdict

CLEAN — all truth claims verified against fetched primaries; only two
non-blocking F11 advisories (optional ShinyHunters lead-sentence softening,
optional Sekoia canonical-URL update). The brief is genuinely ready to publish.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "ShinyHunters used a single vishing call ... to breach Madison Square Garden"
  url_or_quote: "Reporting attributes the breach to ShinyHunters and places the foothold at the company's identity and network-access platform"
  summary: "Cited The Next Web/404 Media do not name an identity/network-access platform as the MSG foothold; Entra/Okta is Abnormal's generic pattern. Self-mitigated by following sentences. Optional: soften the clause. Non-blocking."
- code: F11
  category: editorial-advisory
  section: research
  item: "ESET's 2025 Gamaredon paper (Sekoia corroboration)"
  url_or_quote: "https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/"
  summary: "301 permanent redirect to https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel ; content matches claim. Optional: update to canonical URL. Non-blocking."
```
