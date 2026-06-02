# Compose plan — 2026-06-02 (run 2026-06-02-8af85d01)

- window_hours=36, developing=72, gap=24h, standard daily
- main: Claude Opus 4.8 (claude-opus-4-8); sub-agents S1-S4: Claude Sonnet 4.6

## §0 TL;DR (5 bullets) + Immediate Action callout
- Immediate Action: CVE-2026-41089 Windows Netlogon pre-auth RCE now actively exploited (CCB Belgium 06-01)

## §1 Active Threats (CH/EU/public-sector first)
1. Spain National Police arrest doxer — INCIBE/AG/Civil Guard (Police-ESP-Doxed) [S4]
2. KS-SOMED Polish healthcare supply-chain — CERT-PL CVE-2026-42251 [S2]
3. Miasma / Red Hat npm supply-chain — TeamPCP, Mini Shai-Hulud [S1+S3 merged]
4. Meta AI support-bot Instagram takeover — pro-Iranian, AI-abuse [S4]

## §2 Trending Vulnerabilities
1. CVE-2026-8732 WP Maps Pro (9.8, actively exploited) [S1]
2. CVE-2026-8931 Disig Web Signer (9.4, eIDAS, Slovak gov) [S2]
3. CVE-2026-44825 Apache Solr (8.1, hardcoded creds, no patch) [S2]
4. CVE-2024-21182 Oracle WebLogic (KEV-added 06-01) [S1]
+ CVE summary table (incl CVE-2026-41089 cross-ref §4)

## §3 Research
1. Gamaredon GammaPhish/GammaWorm — Sekoia [S3] (CVE-2025-8088)
2. WordPress Steam-profile Unicode-steganography C2 — GoDaddy [S3]
3. Anthropic Mythos -> ENISA (Project Glasswing) — Bloomberg [S2] (tight, no vanity metrics)

## §4 Updates
1. UPDATE CVE-2026-41089 Netlogon now actively exploited (orig 2026-05-13)
2. UPDATE ShinyHunters/Charter data published (orig 2026-05-27) [S4]

## §5 Deep Dive — Operation Dragon Weave (apt-campaign, china-nexus) [S1+S3 merged]

## §6 Action Items
## §7 Verification Notes
- DROPS: PHANTOMPULSE (05-22 out-of-window), Check Point AI digest (05-26 out-of-window + dubious CVE claims), CIFSwitch (05-30 out-of-window + no §2 gate), Vodafone/Lapsus$ (event 05-12 out-of-window, reduced-confidence corroboration), Dashlane (single-source, routine credential-stuffing)
- CONTRADICTION: Netlogon vector — S3 MS-NRPC TCP/445/135 vs S2 heise CLDAP UDP/389; BleepingComputer doesn't specify port. Describe component-level, attribute CLDAP detail to heise, note MSRC silent on vector.
- NUANCE: Microsoft had not updated advisory to mark exploited as of 06-01; exploitation per CCB Belgium + 3 outlets.
- single-source: none kept in main brief (Dashlane dropped)
- candidate source: ccb-belgium (1 per run)
- coverage gaps: sec-edgar (HTTP 500), sophos-xops (503), therecord (404), inside-it-ch (not attempted), databreaches-net, cert-fr-actualite (stalled Oct 2025), anssi-fr (out-of-window)
