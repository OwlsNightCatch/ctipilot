**Model:** Anthropic Claude (Opus 4.8) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-03T05:00:23Z · ended_at=2026-06-03T05:04:10Z · duration_seconds=227
**Self-telemetry:** urls_checked=14 · webfetch_calls=13 · bridge_fetches=2 · websearch_calls=1

## Verification report — briefs/2026-06-03.md (iteration 3)

Cold read, odd iteration (no prior-iteration deltas, by design). Every cited URL fetched in this pass (Record-2023, CISA, Dashlane-vendor, databreaches, inside-it excepted per below). Named entities (CVE / CVSS / version / actor / cluster / date / count) cross-checked against the cited source actually fetched, not against model knowledge or NVD.

### URLs fetched and corroborated (clean)
- THN WebLogic (CVE-2024-21182, CVSS 7.5, T3/IIOP 7001/7002, KEV 2026-06-01) — supports.
- Oracle CPU Jul 2024 — CVE-2024-21182, versions 12.2.1.4.0 / 14.1.1.0.0, CVSS 7.5 — supports.
- Security Affairs WebLogic (2026-06-02) — supports incl. J2EE middleware framing.
- Android Security Bulletin 2026-06-01 — CVE-2025-48595, Framework, "limited, targeted exploitation", versions 14/15/16/16-qpr2, patch levels 2026-06-01 / 2026-06-05 — supports.
- BleepingComputer Android (124 flaws, High, Framework, no-interaction LPE, Android 14+) — supports.
- Help Net Security Android — confirms "integer overflow", High, Framework, 14/15/16/16-qpr2 — supports the integer-overflow claim (the Bulletin summary alone did not surface that word; Help Net carries it).
- CISA KEV catalog (bridge) — CVE-2022-0492 (cgroups v1 release_agent priv-esc) and CVE-2024-21182 (WebLogic T3/IIOP) both present, added in-window — supports.
- Unit 42 CVE-2022-0492 — cgroup_release_agent_write(), missing CAP_SYS_ADMIN in initial userns, release_agent/notify_on_release, unshare unprivileged path, seccomp scoping ("Only containers running without Seccomp can create a new user namespace"), AppArmor/SELinux, v2 unaffected — supports all deep-dive mechanics EXCEPT the "5.17 cycle" fixed-version (see F5).
- NCSC.ch G7 Évian advisory (bridge) — G7, Évian, DDoS, hacktivist, disruptive maneuvers in cyberspace — supports the NCSC half of the attribution split.
- ZENDATA G7 risk map (2026-05-03) — independently published; Bürgenstock 2024, NoName057(16) DDoS, state intel vs hotel/telecom, rogue base stations/IMSI, social engineering vs staff — supports the ZENDATA half. Attribution split in § 1 is correctly drawn.
- TechCrunch Dashlane (Zack Whittaker, 2026-06-02) — ~20 accounts / dozen vaults, TOTP brute-force, new-device-registration, master-password encryption retained, no infra compromise, LastPass 2022 — supports.
- THN Dashlane (2026-06-02) — "fewer than 20 personal plan users", new-device-registration — supports (keyspace specific not carried; see F11-advisory).
- BleepingComputer Dashlane (2026-06-01) — lockout via rate-limiting then restored, no infra compromise — supports.
- Sophos X-Ops "Pointing a Cursor at evading detection" — ~80 modules/70+ techniques, coordinator+role agents, MCP→Git, Cursor, Ludus, 3× WinSrv2022 (Sophos/CrowdStrike/EDR-free), Sliver+Cobalt Strike, Cloudflare Worker, detection fired on payloads from a testing directory — supports. (Russian-language comments confirmed via Help Net additional source.)
- Help Net Security AI-lab — confirms Russian-language comments + all agent roles/tooling — supports.
- Sophos 2026 Active Adversary Report — 661 cases, identity leading root cause, MFA gap in majority (59.46%), compressed time-to-AD, Impacket most frequent, AnyDesk most-abused, firewall logs missing ~half ransomware cases, EOL Windows Servers — supports; vanity %s correctly omitted per PD-4.
- SANS ISC diary 33040 (Xavier Mertens, 2026-06-02) — SVG phishing, Base64+XOR JS, window.location.href, application/ecmascript MIME evasion, native SVG exec, .cfd domain — supports.
- Seqrite XENOFISCAL (2026-05-29) — SideCopy/APT36, 34 Mustoufiats/MoF Afghanistan, Pashto LNK→mshta→HTA from compromised education domain, .NET loaders, XenoRAT, "Edgre" Run-key typosquat, Scheduled Task, AS59711 (HZ Hosting, Bulgaria = EU) — supports.
- THN SideCopy (2026-06-02) — SideCopy/APT36, XenoRAT 1.8.7, mshta/HTA, Afghanistan MoF — supports.
- Sekoia "FSB's matryoshka #1/3" (2026-06-01) — Gamaredon/UAC-0010/ACTINIUM, CVE-2025-8088 "WinRAR versions prior to 7.13", Startup-folder write, GammaSteel, GammaPhish/GammaLoad/GammaWorm chain, S3-compatible exfiltration — supports the UPDATE's primary claims AND resolves the 7.13-vs-7.10 contradiction the brief notes.

### Citation does not support the claim
- **F3** — § 4 Gamaredon UPDATE, line 95. Brief: *"The series also names GammaSteel … and — newly — exfiltrates to attacker-controlled S3-compatible cloud storage in addition to Gamaredon's previously documented HTTP/Telegram channels ([The Record, 2026-06-02](https://therecord.media/russia-backed-hacker-group-gamaredon-attacking-ukraine-with-info-stealing-malware))."* The cited Record URL resolves to an article dated **February 1, 2023** ("Russia-backed hacker group Gamaredon attacking Ukraine with info-stealing malware"). That 2023 article predates CVE-2025-8088 (a 2025 CVE) and contains **no** mention of the WinRAR vector or S3-compatible cloud exfiltration — it only covers GammaLoad/GammaSteel via RAR/LNK at a high level. The brief stamps it with date "2026-06-02," which the page does not bear. The in-window S3-exfil delta IS supported by the Sekoia primary (fetched, confirms GammaSteel → S3-compatible storage), so the *fact* is sound; the *additional-source citation and its date are wrong*. Remediation: replace the Record URL with a correct in-window article on this story (verified live this pass: `https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html` per WebSearch; SC Media `https://www.scworld.com/brief/russian-hackers-exploit-winrar-vulnerability-for-data-theft` and Infosecurity `https://www.infosecurity-magazine.com/news/gamaredon-worm-ntfs-data-streams/` also surfaced), or drop the Record citation and rely on Sekoia, which already supports every claim in the blockquote. The fabricated "2026-06-02" date must not survive.

### Claims missing inline citation / version unsupported by cited source
- **F5** — § 5 Deep Dive, line 103/105/115. Two facts in the deep dive are attributed to the cited sources but are NOT in them as fetched:
  (a) *"earlier mainline kernels shipped without the missing capability check (fixed in the 5.17 cycle) ([Unit 42, 2022-03-07])"* — the Unit 42 page (fetched) describes the missing `CAP_SYS_ADMIN` check and the cgroup-v1 mechanism but does **not** state the fixed kernel version 5.17. The CISA KEV note (fetched) links the torvalds commit but also does not name 5.17. The "5.17 cycle" is correct per NVD/the upstream commit, but neither cited source carries it.
  (b) *"the footer carries the CVSS 7.0 base score"* (line 105) and footer `CVSS: 7.0` (line 115) — neither Unit 42 nor CISA states a CVSS 7.0; CISA KEV does not publish CVSS, and Unit 42 does not give a base score. 7.0 is the NVD value, but NVD is not cited anywhere in this item.
  Remediation: either add a per-CVE primary that carries 5.17 + CVSS 7.0 as an `Additional source:` (e.g. the kernel.org / Red Hat CVE page `https://access.redhat.com/security/cve/cve-2022-0492`, which Unit 42 itself links and which carries the score and fixed-version), or reword to not attribute these specifics to Unit 42/CISA. Low-severity but it is a real source-attribution gap in the brief's flagship deep dive.

### Editorial / less-is-more flags (advisory)
- **F11** — § 1 Dashlane, line 27. The sentence *"The technique abuses the bounded TOTP keyspace — one million six-digit codes per 30-second window — … ([The Hacker News, 2026-06-02])"* attaches the THN citation to the keyspace specific, but the THN Dashlane article (fetched) does not state the one-million-codes / 30-second figure (it refers generically to "2FA protections"). The figure is true-by-definition (six digits = 10^6; RFC 6238 default 30 s step), so this is not a truth defect, but the citation does not add the specific it is attached to. Optional: move the THN citation to the end of the preceding clause (which THN does support) or leave as-is given the figure is definitional. Advisory only.
- **F11** — Android chipset vendors, line 43. *"…also carries chipset fixes from Qualcomm, MediaTek, Imagination and Unisoc ([Help Net Security, 2026-06-02])"* — Help Net (fetched) does NOT name those four vendors (it says "third-party chipset components" generically); the **Android Bulletin** (also cited earlier in the same paragraph) DOES name all four. The entities are in a cited source, just not the one the clause points to. Advisory: re-point the citation to the Android Bulletin for the vendor-name clause. No truth defect.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 2)

- Truth (F3): wrong/stale Record citation with fabricated 2026-06-02 date on the Gamaredon S3-exfil delta; fact is sound via Sekoia, citation is not.
- Editorial (F5): deep-dive "5.17 cycle" fixed-version and CVSS 7.0 not carried by the cited Unit 42 / CISA sources; add a per-CVE primary (Red Hat CVE page, already linked by Unit 42) or reword.
- Advisory (F11 ×2): Dashlane keyspace specific and Android chipset-vendor names each attached to a citation that doesn't carry them, though a different already-cited source does. Main agent may leave or re-point.

Everything else in the brief is corroborated against a source fetched in this pass. Coverage shape is sound: § 1 leads CH/EU/public-sector (G7 Évian, Dashlane EU-relevant); § 2 inclusion gates honoured (all three CVEs are KEV-listed active-exploitation in-window); the deep dive earns its length and traces (with the F5 exception) to Unit 42/CISA; the Gamaredon § 4 UPDATE is a genuine in-window delta (Sekoia 2026-06-01, S3-exfil + WinRAR vector are new vs the 2026-06-02 prior coverage); recency window and dedup drops (Dragon Weave, KnowledgeDeliver, ENISA NIS360) are correctly logged in § 7. No IOCs, no vanity metrics, no workflow-language leakage, English throughout. No § 1 attribution inversion (NCSC vs ZENDATA split is correct). No analytical-link-as-fact (F13), no unsourced quantifier (F14 — the "fewer than 20", "661 cases", "three VMs", "34 Mustoufiats", "70+ techniques" all trace to a fetched source), no name-collision (F15).

### Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: updates-to-prior-coverage
  item: "UPDATE: Gamaredon weaponises WinRAR CVE-2025-8088 and adds the GammaSteel stealer"
  url_or_quote: "https://therecord.media/russia-backed-hacker-group-gamaredon-attacking-ukraine-with-info-stealing-malware"
  summary: "Cited Record URL is a 2023-02-01 article with no WinRAR/S3 content; brief stamps it 2026-06-02 and uses it for the S3-exfil delta. Fact is supported by the Sekoia primary; replace Record URL with an in-window article (e.g. https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html) or drop it. Fabricated date must go."
- code: F5
  category: missing-citation
  section: deep-dive
  item: "Linux cgroups v1 release_agent container escape (CVE-2022-0492)"
  url_or_quote: "fixed in the 5.17 cycle ([Unit 42]) / CVSS 7.0 footer"
  summary: "Unit 42 and CISA (both fetched) do not state the 5.17 fixed-version nor CVSS 7.0; values are correct per NVD/Red Hat but uncited. Add Red Hat CVE page (https://access.redhat.com/security/cve/cve-2022-0492, linked by Unit 42) as Additional source, or reword."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Dashlane discloses TOTP brute-force"
  url_or_quote: "one million six-digit codes per 30-second window ([The Hacker News])"
  summary: "THN Dashlane article does not carry the keyspace figure (definitional/true regardless). Optional: re-point citation or leave."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2025-48595 — Android Framework"
  url_or_quote: "chipset fixes from Qualcomm, MediaTek, Imagination and Unisoc ([Help Net Security])"
  summary: "Help Net does not name the four chipset vendors; the Android Bulletin (also cited in-paragraph) does. Re-point citation to the Bulletin."
