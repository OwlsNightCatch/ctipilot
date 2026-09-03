# Deep-read verification report — run 2026-09-03T0410Z-intel

Scope: Phase 4 deep-read/verification pass over the 11-item will-publish set. All primaries
re-fetched this run via `tools/fetch_source.py extract` (trafilatura, rung 2) with `jina`
(rung 4) used only where extract/direct returned a JS-only shell. Saved bodies live at
`work/2026-09-03T0410Z-intel/src-*.txt`. All fetches logged to `url-liveness.tsv`.

General note on literal-check methodology: every "FAIL" below was re-inspected by hand
against the saved body. Where noted "FAIL — formatting artifact only", the underlying words
match the source exactly and the grep -F miss is caused solely by markdown emphasis markers
(`**`/`*`/backticks) trafilatura inserts around inline code/entity names, a markdown-escaped
underscore (`\_`), or a Unicode smart-quote apostrophe (U+2019 ’) in the source vs. a straight
ASCII apostrophe in the draft quote — never a wording or substance difference. These are
flagged per instructions (never silently fixed) so the composer can either adjust the quote's
punctuation/formatting to match the literal source string, or drop the surrounding markdown
when lifting the quote for the entry's `evidence[]`.

---

## 1. LiteLLM CVE-2026-59822

**Primary re-fetched:** https://osv.dev/vulnerability/GHSA-7488-6r32-c95q (trafilatura-direct)
**Also fetched for cross-check:** https://github.com/advisories/GHSA-7488-6r32-c95q (jina;
GitHub's own GHSA page, which OSV mirrors) — used because OSV's rendered page dropped the
"Aliases" field content during extraction (see note below).

**Quote verification:**
- Q1 "LiteLLM's MCP Streamable HTTP endpoint could allow an unauthenticated attacker to
  establish an authenticated MCP session using an arbitrary Bearer token..." — **PASS**,
  verbatim on both osv.dev and the GitHub GHSA page.
- Q2 "If upgrading is not immediately possible, disable MCP routes or block access to
  `/mcp/`..." — **PASS**, verbatim on both pages (full sentence: "...disable MCP routes or
  block access to `/mcp/` and related MCP endpoints at your reverse proxy or API gateway.").

**Fact confirmation:**
- CVSS 4.0 8.8 — **CONFIRMED** (OSV.dev severity block: "8.8 (High) CVSS_V4 -
  CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:L/VA:N/SC:N/SI:N/SA:N").
- Fixed version 1.84.0 — **CONFIRMED** ("The issue is fixed in `1.84.0`. We recommend
  upgrading to `1.84.0` or later." — both pages; OSV's affected-versions table also shows
  `Fixed 1.84.0`).

**Additional material:**
- The CVE-2026-59822 identifier is legitimate and correctly tied to this GHSA — worth noting
  only because OSV.dev's own "Aliases" field rendered **empty** in my extraction (a page-
  rendering/JS quirk on OSV's side, reproduced consistently), which could look like a mismatch.
  Cross-check on GitHub's advisory page confirms the CVE ID explicitly ("### CVE ID
  CVE-2026-59822"), as does the page title itself ("CVE-2026-59822 - GitHub Advisory
  Database") and an NVD outbound link (https://nvd.nist.gov/vuln/detail/CVE-2026-59822). No
  action needed — the CVE id in the draft is correct; just don't cite OSV's "Aliases" section
  as evidence of the CVE link if re-fetched again from a fresh session, since it may render
  blank.
- CWE-287 (Improper Authentication). EPSS at 42nd percentile per GitHub's advisory page (not
  requested for confirmation but may be useful context).
- Root cause detail beyond the given quote: "The MCP auth handler supported OAuth2 passthrough
  for upstream MCP servers, but the fallback path could replace failed LiteLLM key validation
  with an empty `UserAPIKeyAuth()` object. This allowed requests with a fabricated
  `Authorization` header to reach MCP tooling without a valid LiteLLM key." — useful if the
  entry wants one more sentence of mechanism detail.
- Fix commit: BerriAI/litellm@73869f0 (PR #26463); reported by GitHub user @yaaras; published
  by @jaydns to BerriAI/litellm Jun 30, 2026; NVD published Jul 8, 2026; reviewed into the
  GitHub Advisory Database Jul 22, 2026 (matches OSV's own Published/Modified timestamps of
  2026-07-22/23).

---

## 2. SonicWall SMA1000 CVE-2026-83548 / CVE-2026-83549

**Primary re-fetched:** https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016 — direct
extract/`url` returned only a JS-app shell (SPA); escalated to `jina` (rung 4), which returned
the full advisory text reliably across two separate fetches this run.
**Corroborating re-fetched:** https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/ (trafilatura-direct)
**Additional corroborating fetched:** https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/ (trafilatura-direct) — used to resolve the hotfix/version detail the vendor advisory itself omits from its short-form text.

**Quote verification (all PASS, verbatim):**
- Q1 "SonicWall PSIRT has investigated a case indicating the active exploitation of the
  vulnerabilities described in this advisory..." — **PASS** (SonicWall PSIRT page, also
  quoted identically inside the BleepingComputer article).
- Q2 "A Pre-authentication SSRF vulnerability exists in the SMA1000 Appliance Work Place
  interface due to an unintended alternate access path..." — **PASS**, verbatim on the PSIRT
  page.
- Q3 "Internet security watchdog Shadowserver currently tracks over 400 SMA1000 appliances
  exposed online..." — **PASS**, verbatim on BleepingComputer (full sentence: "...exposed
  online, although some may already have been patched against this exploit chain.").

**Fact confirmation:**
- CVE-2026-83548 CVSS 3.0 10.0 — **CONFIRMED** (PSIRT page: "CVSS Score: 10.0", vector
  `CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`).
- CVE-2026-83549 CVSS 3.0 7.8 — **CONFIRMED** (PSIRT page: "CVSS Score: 7.8", vector
  `CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H`).
- Affected models 6210/7210/8200v — **CONFIRMED** via BleepingComputer ("The two security
  flaws affect SMA1000 6210, 7210, and 8200v models") and independently via SecurityWeek
  ("SMA1000 models 6210, 7210, and 8200v are affected by the zero-days").
- Fixed hotfix 12.4.3-03526 / 12.5.0-02952 — **CONFIRMED** via SecurityWeek ("Hotfixes
  12.4.3-03526, 12.5.0-02952, and higher versions patch the vulnerabilities.") — note the
  vendor PSIRT page's own text (as rendered via jina) does **not** state hotfix version
  numbers or affected-model names at all; that detail lives only in the press coverage
  (SecurityWeek, and consistent with a WebSearch synthesis giving vulnerable versions as
  "12.4.3-03453 (platform-hotfix) and older, and 12.5.0-02835 (platform-hotfix) and older").
  Recommend citing SecurityWeek or BleepingComputer for the hotfix-version fact rather than
  the vendor advisory page directly, since the advisory page's own body doesn't carry it.

**Additional material:** SSL-VPN on SonicWall firewalls and the SMA 100 Series product line
are explicitly **not** affected (BleepingComputer, SecurityWeek). Prior related incidents this
year: CVE-2026-15409/CVE-2026-15410 (SMA1000, zero-day for weeks, later abused by ransomware
gangs per CISA) and CVE-2025-40602 (December, root-privilege chain) — useful "prior campaign"
context if the entry wants a pattern-of-repeated-targeting note.

---

## 3. Sangoma Switchvox CVE-2026-9586

**Primary re-fetched:** https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/ (trafilatura-direct)
**Corroborating re-fetched:** https://www.helpnetsecurity.com/2026/09/02/exploitation-of-sangoma-switchvox-flaw-underway-cve-2026-9586/ (trafilatura-direct)
**Additional fetched for CVSS confirmation:** NVD REST API directly
(`https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-9586`) and
https://securityonline.info/sangoma-switchvox-cve-2026-9586-rce/ (trafilatura-direct).

**Quote verification:**
- Q1 "The PhoneIP field extracted directly from the XML message and directly concatenated
  into an unparameterized SQL query." — **FAIL — formatting artifact only.** Horizon3's actual
  text wraps the field name in markdown emphasis: "The ***PhoneIP*** field extracted directly
  from the XML message and directly concatenated into an unparameterized SQL query." Word
  content identical.
- Q2 "Given the quick succession of exploit attempts across multiple honeypots from the same
  source IP, we believe that it is likely that most internet exposed Switchvox instances will
  be or have already been targeted." — **PASS**, verbatim.
- Help Net Security cryptominer / "dozens of additional source IPs" content — **CONFIRMED,
  found verbatim** in the 2026-09-02 2:45pm ET update appended to the Help Net Security piece:
  "...since the initial observations, the same threat actor has been observed downloading
  second-stage malware onto the system, which on a cursory look appeared to be a cryptominer,
  he shared." and "Also, since his post was published, dozens of additional source IPs have
  been observed exploiting the honeypots to include simple scanning payloads and also more
  second stage malware installation."

**Fact confirmation:**
- CVSS 4.0 9.3 — **CONFIRMED authoritatively.** Horizon3's own post does not state a CVSS
  score. Queried NVD's REST API directly for CVE-2026-9586: returns CVSS v4.0 vector
  `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`, baseScore **9.3** — exact
  match. (NVD also carries a CVSS 3.1 score of 9.8 on the same record — a different scoring
  system's number, not a contradiction; don't conflate the two if quoting a single CVSS figure.)
  securityonline.info independently states "CVSS: 9.3 (Critical · CVSSv4)" as corroboration.
- Patched version 8.4.0.2 — **CONFIRMED** ("patched in Switchvox 8.4.0.2" — Horizon3; "CVE-2026-9586 was patched in Switchvox version 8.4.0.2, released on July 14, 2026" — Help Net
  Security).
- Exploitation start date 2026-08-30 — **CONFIRMED** (Horizon3 timeline: "30 August 2026 –
  Defused Cyber honeypots trip with valid exploitation attempt"; Help Net Security: "On August
  30, the honeypots started seeing exploitation attempts against CVE-2026-9586.").

**Additional material:** Horizon3 reported 12 distinct Switchvox vulnerabilities in total;
this post covers only CVE-2026-9586. Independently co-discovered by Security Risk Advisors
(SRA), who published their own advisory 17 July 2026. Attack surface: unauthenticated endpoint
`/pa` handled by `PhoneAppsHandler.pm`; full data-flow chain documented line-by-line
(`pre_cmd()` → `tel_notify()` → `XML::Simple::XMLin()` → string-concatenated SQL →
`$db->query()` running as PostgreSQL superuser, enabling `COPY (...) TO PROGRAM` command
execution). Forensic artifact: `/var/log/switchvox/db-quirks.log` records the injected SQL
payload. Shodan shows ~4,000 internet-exposed instances, mostly in the US. New color from
Horizon3's researcher (quoted in the Help Net Security update, not in the original post):
"The Switchvox appliance is likely most valuable as a pivot point into organizations from
external into internal networks. It is possible some appliances hold integration secrets that
may allow them to pivot with stolen credentials."

---

## 4. GitSpawn (AI coding-agent git-config RCE class)

**Primary re-fetched:** https://www.manifold.security/blog/ai-coding-agents-git-hijack
(trafilatura-direct)
**Corroborating re-fetched:** https://www.heise.de/news/KI-Agenten-fuehren-git-Schadcode-beim-Starten-automatisch-aus-11437165.html (trafilatura-direct, German) and
https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html (trafilatura-direct)

**Quote verification:**
- Q1 "Open a folder with Claude Code and it runs git status before you type anything. Before
  the workspace-trust prompt. On some agents, before you have even authenticated." — **FAIL —
  formatting artifact only.** Source wraps the command in backticks: "...it runs `git status`
  before you type anything..." Word content identical.
- Q2 "Delivery is worth being precise about, because git never carries this. Cloning a
  hostile URL does nothing, and neither does fetch or pull. The repository has to arrive as
  files with its .git directory already inside" — **FAIL — formatting artifact only.** Source:
  "...with its `.git` directory already inside, so the vector is anything that moves a
  directory instead of cloning it: a shared `.zip`, a shared drive, a sync folder, a USB
  stick." Word content identical (backticks around `.git`).

**Patched/unpatched matrix, confirmed as of the primary's current state (page metadata date
still 2026-09-01 — not updated further as of this fetch on 2026-09-03):**

| Agent / finding | Status | Version detail |
|---|---|---|
| Claude Code — `core.fsmonitor` sink | **Patched** | Confirmed vulnerable on 2.1.193, fixed by **2.1.196** (reported 26 June 2026, closed as duplicate of a same-day report) |
| Claude Code — `ultrareview` sink (second, different config-key sink) | **Unpatched** | Reported 15 July 2026 on 2.1.210; **confirmed still unpatched on 2.1.252 as of 1 September 2026** |
| Qwen Code | **Unpatched** | Confirmed 0.19.6 (7 July), confirmed again unpatched on 0.22.3 (1 Sept) |
| Goose | **Patched** | Fixed in 1.44.0; CVE-2026-72718 assigned |
| Grok Build | **Unpatched** | Confirmed 0.2.93 (14 July), confirmed again unpatched on 1.0.13 (1 Sept) |
| Hermes Agent | **Unpatched** | Confirmed 0.18.2/0.21.0; CVE-2026-71963 (VulnCheck-assigned); no vendor triage after six contact attempts across five channels |
| OpenAI Codex | **Patched** | Closed as duplicate of an earlier report; patched |
| Cursor | **Patched** | Closed as duplicate of an earlier report; patched |

This is 4 patched / 4 unpatched, matching the article's own framing: "Four of the eight
findings are still live."

**Second-sink confirmation (task's specific ask):** the `claude ultrareview` sink is **real
and distinct from `core.fsmonitor`** — Manifold's own text: "This one is not `core.fsmonitor`.
It is a different git setting of the same kind, one the review path does not strip." — and is
**confirmed still unpatched** as of the article's most recent recheck (2.1.252, 1 September
2026). Manifold deliberately withholds the specific config-key name "while it remains
unpatched," so the exact sink name cannot be extracted from any source fetched this run.

**Cross-check against Hacker News (per task instruction, confirming it still says the same
thing — not re-litigating):** confirmed unchanged. "GitHub assigned CVE-2026-72718 a CVSS 4.0
base score of 7.0 in an advisory crediting Francisco Rosales, the only score any of these
findings carries" and "VulnCheck assigned CVE-2026-71963, according to Manifold. The Hacker
News found no published record for that identifier in MITRE's CVE List on September 2, where
the identifiers either side of it are published VulnCheck records." Both facts confirmed
verbatim on today's re-fetch of the Hacker News article.

**heise.de corroboration — one naming discrepancy worth flagging:** heise's German summary
refers to the second, still-unpatched Claude Code sink as "**claude ultraview**" (missing the
"re" — Manifold's own term is `ultrareview`). This looks like a typo in heise's own copy, not a
different finding — heise is otherwise consistent with Manifold ("Anthropic hat die
fsmonitor-Lücke beseitigt, nicht aber eine ähnliche mit `claude ultraview`" = "Anthropic fixed
the fsmonitor gap, but not a similar one in `claude ultraview`"). heise also reports it
contacted Manifold directly and got a response not in the blog post itself: "Wir können sagen,
das Muster ist nicht auf die genannten Agenten begrenzt, und die Liste der betroffenen
Hersteller enthält beide großen KI-Labore und große Softwarefirmen" ("the pattern is not
limited to the named agents, and the list of affected vendors includes both major AI labs and
major software companies") and that Codex and Cursor have since been added to the list but are
patched — consistent with Manifold's own "Update, 1 September 2026" note.

---

## 5. Gambling Goblin / Earth Berberoka (deep dive)

**Primary re-fetched (full technical report):** https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/ (trafilatura-direct, 457 lines captured, read in full)
**Also re-fetched (shorter defender-facing companion post):** https://blog.checkpoint.com/research/gambling-goblin-a-chinese-speaking-actor-hijacks-brazilian-government-sites-to-fuel-a-global-seo-fraud-machine/ (trafilatura-direct, read in full)

**Quote verification — IMPORTANT SOURCE CORRECTION:** two of the five quotes belong to the
**blog.checkpoint.com** companion post, not research.checkpoint.com as listed in the task.

- Q1 "The group compromises legitimate Brazilian government web servers, many of them .gov.br
  sites spanning federal, state, and municipal institutions, and installs malicious modules
  that silently turn them into reverse proxies for phishing content, invisible to the visitor"
  — **PASS, verbatim — but only on blog.checkpoint.com** (it is a bullet in that post's "Key
  Findings" list). This exact sentence does **not** appear anywhere in research.checkpoint.com;
  attribute this quote to blog.checkpoint.com in the entry's `evidence[]`.
- Q2 "We assess with medium-to-high confidence that Gambling Goblin is tied to Earth Berberoka"
  — **FAIL — formatting artifact only** (research.checkpoint.com wraps both entity names in
  markdown bold: "We assess with medium-to-high confidence that **Gambling Goblin** is tied to
  **Earth Berberoka –** a Chinese-speaking threat cluster first documented by Trend Micro in
  2022..."). Word content identical.
- Q3 "Audit Apache configurations and installed modules. Look for unexpected .so files,
  especially any timestamped to match legitimate modules like mod_ssl or mod_suexec." — **FAIL
  — formatting artifact only, and also only on blog.checkpoint.com** (research.checkpoint.com
  does not carry a "What Defenders Should Do" section at all — that's unique to the companion
  post). blog.checkpoint.com's actual text: "**Audit Apache configurations and installed
  modules.** Look for unexpected .so files, especially any timestamped to match legitimate
  modules like mod_ssl or mod_suexec." (bold markdown around the lead sentence). Word content
  identical; attribute to blog.checkpoint.com.
- Q4 "oRAT was tied to Earth Berberoka in 2022, and the variant we analyzed shares the same
  orat/cmd/agent codebase and REST-style operator routes" — **FAIL — formatting artifact
  only** (research.checkpoint.com wraps the path in backticks: "...shares the same
  `orat/cmd/agent` codebase..."). Word content identical.
- Q5 "one of the AlphaAgent samples we recovered was uploaded in the same archive as other
  tools previously attributed to Earth Berberoka, placing AlphaAgent directly alongside the
  group's known toolset" — **FAIL — formatting artifact only.** research.checkpoint.com uses a
  Unicode right-single-quote (U+2019 ’) in "group’s", not the ASCII apostrophe used in the
  draft quote. Confirmed at the byte level (0xE2 0x80 0x99). Word content identical.

**Apache module hooking mechanism (name-translation stage) — full detail extracted:**
"The source file, `opsproxy.c`, reveals a purpose-built reverse proxy that quietly grafts
attacker-controlled content onto a compromised web server. The module registers itself at
Apache's name-translation stage and inspects every incoming request for one of a small set of
hardcoded URL prefixes which in our samples, `/wps`, `/bmw`, and `/card`. When a request
matches, the module rewrites it into a reverse-proxy request to a corresponding upstream server
hardcoded into the source, silently relaying the visitor to attacker infrastructure while the
request still appears, to the outside world, to come from the legitimate compromised domain."
It also strips the upstream's Content-Security-Policy headers and replaces them with a
permissive policy allowing inline/`eval`'d scripts, third-party assets, and `data:`/`blob:`
sources, and forwards the original `Host` header plus standard proxy headers.

A **second, separate Apache module** (distinct from `opsproxy.c`) exists and is not covered in
the draft's summary at all: it "disguises itself as a basic filter module while registering
request and response hooks that examine visitor headers, URI paths, referrers, and client
IPs. It carries a static configuration, decrypts it with RC4, and parses it into two rule
types: **rule1** (path/referrer/User-Agent matched to a proxy URL) and **rule3** (an optional
response-filtering/injection configuration). Using a compiled-in regex for `<body.*?>` to
locate its injection point, the module expands placeholders (`{host}`, `{hip}`, `{url}`,
`{name}`), fetches remote content with libcurl, and writes that content into Apache responses
via `ap_rwrite` and bucket manipulation." Check Point calls this "consistent with SEO cloaking
and content-injection malware."

**Full list of named implants and roles (11 distinct tools — more complete than a short
summary would carry):**
1. **cam-agent / `cluster-asset-mapping`** — Go ELF recon/asset-mapping agent found on an
   exposed open directory; bundles known pentest tools as modules (dirprobe, httpx, naabu,
   nuclei v3, subfinder, whatweb); gRPC C2 over mTLS-style embedded certs; logs to
   `/tmp/asset-scan/payload-run.log`.
2. **opsproxy.c Apache module** — reverse-proxy grafting module (detailed above).
3. **Second Apache module (unnamed)** — RC4-config content-injection/cloaking module (detailed
   above).
4. **DownPro** — Go downloader; drops the main backdoor, ChUser, and PasswordHarvester
   (`unix_updates`); AES-GCM+Base64 encrypted URLs passed via CLI flags; blends destination
   path into legitimate-looking system binary names when root, PHP-session/temp-file names
   when non-root.
5. **ChUser** (`/usr/bin/chuser`) — simple backdoor, dual activation gate (HTTP response-value
   check or local MD5-salted secret match); timestomped to match `/bin/ls`; setuid.
6. **`unix_updates` / PasswordHarvester** — 3snake-based (github.com/blendin/3snake) credential
   stealer; monitors `sshd`/`sudo`/`su`/`doas`/`ssh`/`ssh-add`/`passwd`/`kinit`/`login` via
   netlink process-event subscription; `ptrace`-attaches to intercept credential buffers;
   exfiltrates RC4+Base64; masquerades as one of ~29 fake kernel-thread/daemon process names.
7. **AlphaAgent** — modular Go backdoor; gRPC-over-HTTPS (with uTLS Chrome-fingerprint mimicry,
   Google/Cloudflare traffic camouflage, AES-GCM payload-in-TLS encryption) or DNS-tunneled or
   plain-HTTP C2; SOCKS5/yamux/Ligolo-style tunneling; dormant/placeholder-only rootkit loader
   via Go `embed.FS`; geofence exit if host country = China; newest build adds an "AI plugin"
   execution path (`ai_plugin_%s.sh` scripts) — capability confirmed present via log strings,
   contents unknown.
8. **oRAT** — Go RAT; tcp/stcp(TLS)/sudp(QUIC) transport with multiplexed HTTP-over-session;
   REST-style operator routes (`/agent/info`, `/exec`, `/upload`, `/download`, `/screenshot`,
   `/zip`, `/portscan`, `/proxy`, `/net`, `/ssh`, `/upgrade`, `/kill-self`); embedded SSH+SFTP
   server with hardcoded RSA host key; persistence as systemd service `xtables-addons`
   (masquerading as the real netfilter package) at `/usr/local/bin/xtables-addons`; GUID hidden
   as a comment appended to `/etc/protocols`; lock file `/tmp/.lock`; process masquerades as
   `sshd: root@pts/0`.
9. **SSH brute-forcer** — reads target IP/user/pass lists, concurrent SSH login attempts,
   writes results to plaintext `res.txt`; no C2 or persistence of its own.
10. **`info.sh`** — Bash recon script; login-history profiling, `.ssh`/`.bash_history`
    harvesting across all home directories (incl. root), remote-mount/Docker-volume discovery
    (NFS/CIFS/WebDAV/cloud FUSE, filtered to exclude container noise), `/etc/hosts`/listening
    ports/ARP-table collection.
11. **`findweb.sh`** — Bash recon script; enumerates all web servers/vhosts on a host
    (Nginx/Apache/httpd, incl. Docker-hosted), parses configs for `server_name`/`DocumentRoot`/
    `ServerAlias`/`proxy_pass`, producing a domain-to-webroot-to-existing-proxy-rule inventory
    — explicitly the reconnaissance step that feeds target selection for weaponizing a
    newly-compromised server.

**Additional MITRE ATT&CK-mappable behavior beyond the task's given list**
(T1584.004/T1090.002/T1071.001/T1071.004/T1572/T1036.005/T1070.006/T1552.004/T1110/T1595.002,
all independently confirmed present in the fetched text): **T1497.001/T1497.003**
(Virtualization/Sandbox Evasion — AlphaAgent's randomized outlast-sandbox sleep and its
"virtualization role" host-inventory field); **T1614** (System Location Discovery — country
geofence check, exits if host is in China); **T1014** (Rootkit — kernel-module component
embedded via Go `embed.FS`, described as present only as a placeholder in analyzed samples,
not observed live); **T1562.001** (Impair Defenses: Disable or Modify Tools — oRAT's
`setenforce 0` SELinux-disable during its prep routine); **T1543.002** (Create or Modify System
Process: Systemd Service — oRAT's `xtables-addons` service registration); **T1053.003**
(Scheduled Task/Job: Cron — oRAT's per-user persistence fallback); **T1027/T1027.002**
(Obfuscated/Packed Files — AES-GCM/RC4-encrypted configs; one AlphaAgent variant wrapped in an
anti-analysis protector that unpacks only in memory); **T1622** (Debugger Evasion — that same
protector "watches for a debugger, popping a decoy error and exiting the moment it detects
one"); **T1105** (Ingress Tool Transfer — DownPro's payload fetch); **T1046/T1595.001**
(Network Service Discovery / Scanning IP Blocks — cam-agent's naabu/httpx/nuclei/subfinder
modules and oRAT's `/agent/portscan` route); **T1564** (Hide Artifacts — bind-mounting over a
process's own `/proc/<pid>` entry to hide it from process-table inspection, used by both
AlphaAgent and oRAT).

**Additional concrete detection/hunting guidance beyond the Apache-module-audit quote:**
From blog.checkpoint.com's "What Defenders Should Do": "**Watch for stripped security
headers.** A sudden absence of Content-Security-Policy headers on specific URL paths is a
strong signal of injected reverse-proxy behavior." From the technical body (research.
checkpoint.com), concrete behavioral/file-path artifacts a defender could hunt for (paths and
process-naming patterns, not raw IOCs): cam-agent log file `/tmp/asset-scan/payload-run.log`;
oRAT persistence at `/usr/local/bin/xtables-addons` + systemd unit `xtables-addons` + a
`# GUID: <uuid>` comment line appended to `/etc/protocols` + lock file `/tmp/.lock`; DownPro's
blend-in destination names (root: `/usr/local/bin/{systemd-udevd,rsync-tsl,tcp-tsl,snapd-ext,
fsck-disk,nftables-init}`; non-root: `/tmp/php_sess_<32-hex>` or `/tmp/private-tmp-<5-alnum>`);
ChUser at `/usr/bin/chuser` timestomped to match `/bin/ls`'s timestamp with the setuid bit set;
the 3snake-based stealer's process-masquerade pool of ~29 fake kernel-thread names (e.g.
`[kworker/1:2]`, `[ksoftirqd/0]`, `[watchdog/0]`, `[systemd]`, `[dbus-daemon]`, `[journald]`,
`[migration/0]`, `[ksmd]`); AlphaAgent's process-disguise-by-profile (aws/google/aliyun/general)
and its network camouflage tells (SNI `api.google.com`, decoy `NID`/`SID` cookies, Cloudflare-
style `_cf_auth_ts`/`_cf_auth_nonce`/`_cf_auth_method` parameters, handler paths
`/agent/heartbeat` and `/notifications/v1/push`).

---

## 6. MoiClient

**Primary re-fetched:** https://asec.ahnlab.com/en/95211/ — fetched twice via two different
transports (trafilatura-direct and jina) to isolate whether an unusual capitalization pattern
was a fetch artifact or a source characteristic.

**Quote verification — all three quotes FAIL literal grep, but purely due to a genuine,
source-side capitalization quirk (confirmed identical across both independent transports, so
it is NOT a fetch/extraction artifact — it is how ASEC's own published page renders these
strings):**
- Q1 "MoiClient uses the ncalrpc protocol sequence to connect to the RPC interface of the
  AppInfo Service, then executes winver.exe as a debug target and acquires the debug object
  handle." — **FAIL, source-casing artifact.** ASEC's page reads: "...then executes
  **winver.Exe** as a debug target..." (capital E in "Exe"). Word content otherwise identical.
- Q2 "version 2.5.30.11281 of BootRepair.Sys—a vulnerable driver in Lenovo PC Manager—was
  exploited. MoiClient creates this driver in the %Public% path under the name moimoi.sys" —
  **FAIL, source-casing artifact.** ASEC's page reads: "...version 2.5.30.11281 **Of**
  BootRepair.Sys...MoiClient creates this driver in the %Public% **Path** under the name
  **moimoi.Sys**..." (capitalized "Of", "Path", and "Sys"). Word content otherwise identical.
- Q3 "The registered task runs every 30 minutes. At that time, SumatraPDF—named "demo.exe"—is
  launched, and "uxtheme.dll," which is located in the same path and is actually MoiClient, is
  reloaded." — **FAIL, source-casing artifact.** ASEC's page reads: "...named **"demo.Exe"**—
  is launched, and **"uxtheme.Dll,"** which is located in the same **Path**..." Word content
  otherwise identical.

Recommend the composer either (a) quote these with ASEC's actual casing verbatim in the
entry's `evidence[]` (technically correct, if visually odd), or (b) paraphrase instead of
quoting directly, rather than using the cleaner-cased versions as literal quotes.

**Fact confirmation — all CONFIRMED:** driver version 2.5.30.11281 of BootRepair.Sys (Lenovo
PC Manager); dropped to `%Public%\moimoi.sys`; RPC technique via `ncalrpc` to the AppInfo
Service, using `winver.exe` as a debug target to acquire a debug-object handle, then
`ComputerDefaults.exe` to obtain and clone an elevated process handle (parent-spoofed onto
`sc.exe` and PowerShell to inherit privilege and bypass UAC); Task Scheduler job named
`MicrosoftWindowsUpdateTask<4-digit-number>` (or with a trailing period appended if a name
collision exists), re-running every 30 minutes, at which point `demo.exe` (renamed SumatraPDF)
re-triggers DLL side-loading of `uxtheme.dll` (actually MoiClient).

**Additional material:** BYOVD kill-list of targeted security products named explicitly —
Windows Defender family, Malwarebytes, Bitdefender, Kaspersky, Avast, AVG, McAfee (terminated
via PID hand-off to the `\\.\BootRepair` device). A separate, dedicated method specifically
targets Windows Defender: downloads `defendnot.dll` + `defendnot-loader.exe` from C2 and runs
them via PowerShell using the UAC-bypassed privileges. Final payload is "MoiXD Stealer" (`c.txt`,
in-memory-executed via `CreateThread()`), which uses ChromeElevator to steal browser-stored
passwords. ASEC provides an explicit reader checklist: check for unintended `explorer.exe`
processes, check Task Scheduler for the naming pattern, and check for the presence of
`%Public%\moimoi.sys`, `%LOCALAPPDATA%\uxtheme.dll`, `%LOCALAPPDATA%\data.dat`,
`%LOCALAPPDATA%\defendnot-loader.exe`, `%LOCALAPPDATA%\defendnot.dll`.

---

## 7. Kimsuky Backblaze B2 LNK campaign

**Primary re-fetched:** https://asec.ahnlab.com/en/95217/ (trafilatura-direct)

**Quote verification:**
- Q1 "In this attack, Backblaze B2 was used not merely as a file storage space but as a C2
  infrastructure to exfiltrate information from infected PCs and relay follow-up commands." —
  **PASS**, exact verbatim match.
- Q2 "Based on such similarities in code and behavior, AhnLab determined that this malicious
  LNK is also linked to the Kim Sukki group." — **PASS**, exact verbatim match.
- Q3 "it is configured to execute ping_<FIRST 4 digits of UUID>.Js approximately every 14
  minutes via wscript.Exe." — **FAIL — formatting artifact only.** ASEC's page uses a
  markdown-escaped underscore: "...configured to execute ping**\_**<FIRST 4 digits of
  UUID>.Js approximately every 14 minutes via wscript.Exe." (note: unlike item 6, this source
  page actually does use "wscript.Exe"/".Js" with the odd capitalization consistently, and the
  draft's quote already matches that casing correctly — the only mismatch is the escaped
  underscore character.)

**Fact confirmation:** all confirmed. Malicious LNK named "[Royal Hotel Seoul] Request for
Review of Seafood Ingredient Purchases.LNK"; drops a legitimate decoy .hwp + XOR-encrypted ZIP
to `C:\ProgramData\systmp\sunshine`; extracts `termsvc.ps1` + `poc.js` to `C:\ProgramData\
video`, plus a copy saved as `C:\ProgramData\systmp\ping_<first-4-UUID-digits>.js`; Task
Scheduler job named `MicrosoftOffice2016_<first-4-UUID-digits>` re-executes the JS every ~14
minutes via `wscript.exe`; `termsvc.ps1` collects OS/arch, timezone, public IP (queried via
`api.ipify.org`), username/domain, running-process list (`tasklist`), computer name; uploads
via Backblaze B2 API to a path keyed by the victim's BIOS serial number; downloads a follow-up
command file named `aaa` from the same B2 path, saved as a randomly-named `.cmd` in `%TEMP%`,
run hidden via `cmd.exe /c`, then deleted after a ~120-second wait.

**Additional material — naming inconsistency worth flagging:** the article's own **title**
calls the actor "**Kim Sooki**," while the **body text** consistently calls it "**Kim Sukki**"
— neither matches the canonical registry spelling "Kimsuky." This is AhnLab's own internal
translation inconsistency (confirmed present in the fetched page itself, not a transcription
error on my part), not a different actor. The composer/entity-linker should map this to the
`Kimsuky` registry entity regardless of which of ASEC's two spellings gets quoted.
AhnLab's stated attribution basis: "Similarities to previous cases included not only the
PowerShell execution syntax but also the method of identifying the original LNK based on file
size, the structure for extracting data from within the LNK using a fixed offset, and the
method of registering the Task Scheduler to repeatedly execute malicious scripts."

---

## 8. Langflow CVE-2026-0768 renewed exploitation

**Primary re-fetched:** https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/ (trafilatura-direct)
**Corroborating re-fetched:** https://www.heise.de/news/Jetzt-patchen-Angreifer-attackieren-Langflow-Instanzen-mit-Schadcode-11437701.html (trafilatura-direct, German)
**Also fetched to resolve the version discrepancy:** https://github.com/langflow-ai/langflow/releases (jina) and the GitHub Releases API directly for both tags (`v1.12.0`, `v1.11.6`).

**Quote verification:**
- Q1 (environment-variable querying quote) — **PASS**, exact verbatim match on
  BleepingComputer: "Among other things, attacker requests are querying environment variables
  (LANGFLOW_SUPERUSER, OPENAI_API*, AWS_ACCESS*, AWS_SECRET*), reading
  /root/.cache/langflow/secret_key, and checking .ssh access and .bash_history size."
  (attributed to VulnCheck's Caitlin Condon).
- heise's "mehr als 350 Angriffsversuche" quote — **PASS**, exact verbatim match: "Die
  Sicherheitsforscher geben an, mittlerweile mehr als 350 Angriffsversuche beobachtet zu haben
  – Tendenz steigend." ("The security researchers state they have now observed more than 350
  attack attempts – and rising.")

**Exploitation-attempt count — CONFIRMED exact.** BleepingComputer states both numbers the
draft cites: "at least 50 exploitation attempts over the weekend" (VulnCheck honeypots, UK,
attack traffic primarily from Russia), rising to "the total number of observed attacks
increased to 360 as of today" (per VulnCheck's Caitlin Condon, as of the article's 2026-09-01
publication). heise's "more than 350" one day later (2026-09-02) is consistent with a still-
climbing count from a different snapshot in time, not a contradiction.

**Patched-version discrepancy — RESOLVED, not a real error by either outlet.** Confirmed via
the GitHub Releases API directly:
- `v1.11.6` — `published_at: 2026-09-01T02:21:38Z`
- `v1.12.0` — `published_at: 2026-09-01T21:16:20Z` (~19 hours later, same calendar day)

BleepingComputer's article (dated 2026-09-01) states "the latest available version, 1.11.6" —
this was accurate at the time BleepingComputer's reporting was compiled, since v1.12.0 had not
yet shipped. heise's article (dated 2026-09-02) states "Aktuell ist die Ausgabe 1.12.0"
("current version is 1.12.0") — correct, since v1.12.0 shipped later on 2026-09-01, before
heise wrote its piece. **Neither source is wrong; they observed two different points on the
same day.** The operative current-patched-version guidance for this run's publication date
(2026-09-03) is: **Langflow 1.12.0** is the current release and supersedes 1.11.6; the
underlying CVE-2026-0768 fix itself applies to any version after 1.4.2 (both outlets agree on
that baseline), so 1.12.0 is simply the latest of many fixed releases, not a version where the
fix was newly introduced.

**Minor additional note:** heise's article states "Verwundbar ist Langflow bis inklusive
Version **1.42**" — almost certainly a rendering/typo of "1.4.2" (matches BleepingComputer's
"affects Langflow versions 1.4.2 and earlier" exactly); flagging so the composer doesn't
mistake this for a genuinely different affected-version boundary.

**Reminder carried forward per task instruction (not re-litigated):** CVE-2026-0768 (this
item, CWE-94, `code` parameter in the custom-component validate endpoint, CVSS 9.8, ZDI-26-034,
disclosed January 2026, not KEV-listed) is confirmed by BleepingComputer's own text to be
distinct from CVE-2026-0770 (CWE-829, `exec_globals` parameter, KEV-listed 2026-07-21, already
covered by this store) — BleepingComputer explicitly lists both as separate items in its "prior
Langflow vulnerabilities this year" recap.

---

## 9. EtherRAT Teams-helpdesk campaign (Microsoft)

**Primary re-fetched:** https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/ (trafilatura-direct, full 312-line body captured cleanly, including the ATT&CK table, IOC tables, and all KQL queries).

**Quote verification — all three PASS, exact verbatim:**
- Q1 "Microsoft Threat Intelligence has observed a human-operated intrusion campaign that
  abuses Microsoft Teams external collaboration to impersonate IT or helpdesk personnel and
  socially engineer users into granting an interactive remote session." — **PASS**.
- Q2 "The analyzed implants also contained dormant logic capable of querying an Ethereum smart
  contract for an updated C2 URL. This functionality was disabled in the recovered builds,
  which instead used a hard-coded fallback server." — **PASS**.
- Q3 "operator-issued tasking executed through the Node.js backdoor initiated internal
  remote-management connections over WinRM on TCP port 5985 to a large set of domain-joined
  systems" — **PASS**.

**IMPORTANT NAMING CORRECTION — "EtherRAT" does not appear anywhere in Microsoft's article.**
Searched the full fetched body for "EtherRAT" (and variants) — zero hits. The only related
string Microsoft uses is inside its Defender Antivirus detection-name table: **`Trojan:JS/
EtherRatz.A!MTB`** and **`Trojan:JS/EtherRatz.B!MTB`** (note: **"EtherRatz,"** not "EtherRAT")
for the Node.js implant stage, alongside `Trojan:JS/SynkLoader.SA` / `Trojan:Win32/
SynkLoader.SA` for the MSI/loader stage. Microsoft does not give the campaign or the implant a
proper name anywhere in the body text — its own companion Threat Analytics report is titled
generically: "Teams-based helpdesk impersonation delivers MSI loader and Node.js implant for
hands-on-keyboard intrusion." **If the entry's title/naming uses "EtherRAT" as though it were
Microsoft's coined name, it should be corrected to reference the actual detection-signature
family "EtherRatz,"** or reworded to make clear the campaign itself is unnamed by Microsoft and
"EtherRatz" is only a Defender AV-signature label, not a malware-family name Microsoft uses in
prose.

**KQL hunting queries — captured verbatim (all short enough to quote in full; six total):**

1. External Teams-chat first-contact detection (`CloudAppEvents`, filters `Application ==
   "Microsoft Teams"`, `ActionType == "ChatCreated"`, `IsExternalUser == true`, extends
   thread-creator/recipient UPN/DisplayName/OrganizationId fields).
2. Cross-referencing a known thread ID against `MessageEvents`, `CallActivityEvents`,
   `MessageUrlInfo` via a `union` query.
3. PowerShell writing an MSI to a user-writable path (`DeviceFileEvents`, parent `explorer.exe`
   → `powershell.exe`, `FileName endswith ".msi"`, path contains `\Downloads\`/`\AppData\`/
   `\Temp\`).
4. `node.exe` executing a staged payload from a user-writable path launched by `wscript.exe`
   (`DeviceProcessEvents`, checks `ProcessCommandLine` contains `\AppData\Local\` but not
   `.js`, initiating process `wscript.exe`).
5. Screen capture via hidden PowerShell writing Base64 to a temp file (`DeviceProcessEvents`,
   initiating process `node.exe`, command line containing `CopyFromScreen`, `ToBase64String`,
   `System.Drawing.Bitmap`, `WriteAllText`).
6. WinRM lateral movement from a non-administrative process (`DeviceNetworkEvents`, initiating
   `powershell.exe` with `-NoLogo -NoProfile -ExecutionPolicy Bypass`, `RemoteUrl endswith
   ":5985/wsman"`).

Full text of each is in the saved body (`src-microsoft-etherrat.txt`, lines 165–246) if the
composer wants to quote them verbatim in the entry.

**Full MITRE ATT&CK table (Microsoft's own mapping, 14 rows) confirmed present, more granular
than needed for the composer's `techniques[]` list:** T1566.003, T1059.001, T1059.007,
T1218.007, T1218.011, T1036, T1497.001, T1082, T1016, T1087.002, T1018, T1518.001, T1113,
T1071.001, T1105, T1021.006 (note the table itself lists 16 rows but two tactic/technique pairs
repeat T1082/T1113-style groupings — recount from the raw table if the composer wants an exact
row-for-row count).

**Note on the IOC section:** Microsoft's article includes a file-hash table (6 SHA-256 values)
and a domain table (5 Azure Blob Storage staging domains + 3 C2 domains). Per this store's
no-IOC policy these should **not** be carried into the published entry — flagging only so the
composer doesn't accidentally lift them while pulling the ATT&CK table from the same page.

---

## 10. PaperCut NG/MF update (existing entry: entries/2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce.md)

**Existing entry read first** (frontmatter + full body) to establish baseline: it currently
describes Emergency Patch **Release 2** as the fix, with fixed versions "v24.1.9, v25.0.12,
v26.0.4 and later" for both CVEs, and states there is no fix for v23 and earlier.

**Primary re-fetched:** https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/ (trafilatura-direct; bulletin now shows "Last updated September 2, 2026")

**Quote verification:**
- Q1 "Emergency Patch (Release 3) has been released by our emergency response team and
  supersedes Release 2. You do not need to install previous patches, this patch is an
  accumulation of all emergency releases. This release addresses two known regressions and
  adds additional hardening and mitigation against potential attack chains." — **PASS**, exact
  verbatim match.
- Q2 "Regressions include: Addresses broken SAML login flows; Restored support for using
  legacy Microsoft SQL Server drivers for external card lookup" — **FAIL as a single
  contiguous string** (the page renders this as a lead-in line followed by a two-item bullet
  list, not one flowing sentence: "Regressions include:" / "- Addresses broken SAML login
  flows" / "- Restored support for using legacy Microsoft SQL Server drivers for external card
  lookup"). **Each individual clause is independently verbatim** on the page. Recommend
  quoting the three fragments separately, or rendering as a list, rather than as one merged
  quote with semicolons.

**MATERIAL UPDATE requiring correction (not just addition) to the existing entry:**

1. **Emergency Patch Release 3**, published **1 September 2026, 6:22pm (AEST)**, **supersedes
   Release 2** and is cumulative — "You do not need to install previous patches." It fixes two
   regressions that Release 2 itself had introduced (broken SAML login flows; broken legacy
   Microsoft SQL Server driver support for external card lookup) and adds further, undisclosed
   "hardening and mitigation against potential attack chains." **The existing entry's `fixed:`
   field, which currently only names "Emergency Patch Release 2," should be updated to name
   Release 3 as the current recommended patch**, since Release 2 is now known-superseded and
   carries the two named regressions. The version strings themselves are unchanged — Release 3
   ships as the same v24.1.9/v25.0.12/v26.0.4 line — but distinguished by new build numbers:
   MF v26.0.4 build 76531, v25.0.12 build 76532, v24.1.9 build 76534; NG v26.0.4 build 76530,
   v25.0.12 build 76533, v24.1.9 build 76535 (checksums also given on the bulletin page if the
   composer wants to note "install strictly via the official upgrade procedure, verify
   checksums" as a hardening line — no need to reproduce the actual hash values, which would be
   an IOC-adjacent artifact best left uncited).

2. **NEW: a second wave of attacks is now confirmed**, per the bulletin's "Updates from the
   field" entry (2 September 2026, 4:38pm AEST): "As anticipated there is a second wave of
   attack on servers that are not fully patched and are publicly available. We note that the
   majority of customers have their server behind firewalls or have applied the patch, thank
   you... This second wave appears to involve **more sophisticated post-compromise behaviour**
   than what was observed in the first days of this incident." This is new, materially
   significant information not in the existing entry and should be added via a changelog
   record (dated update, non-internal, since it changes the reader-facing "current status" and
   the entry's severity framing for the still-unpatched population).

3. **NEW concrete post-compromise attacker TTP chain** (first-wave activity, timestamped from
   first command, PaperCut's own bulletin): initial discovery (`whoami & ver` → `tasklist` →
   `nltest /dclist:` → `quser & dir c:\users`), then a PowerShell-delivered download of a
   renamed executable via a public file-sharing service, silent execution (`/S` switch),
   installation of a **Windows service literally named "Remote Access Service"** running
   `SimpleService.exe` (identified by PaperCut as a **SimpleHelp** remote-access agent) as
   `LocalSystem` with auto-start, followed by a further `tasklist` and a PowerShell-delivered
   download of **AnyDesk**. PaperCut's own guidance: "We recommend checking for the presence of
   a Windows service named 'Remote Access Service' running `SimpleService.exe`... and for
   unexpected AnyDesk installations, as potential indicators of post-compromise remote access
   tooling." This is genuinely new detection/hunt-relevant detail (abuse of legitimate RMM
   tooling for durable post-compromise access) not present in the existing entry, and is stated
   as vendor-neutral behavioral guidance (service name + process name), not a raw IOC, so it
   fits the store's no-IOC-but-behavioral-detection convention.

4. **NEW additional artifact strings** (30 August update, some already partially reflected in
   the existing entry, some not): `server.log` strings `DB URL: jdbc:derby:memory:pwn;
   create=true`, two `Database error looking up cardID: VALUES CAST(...)` variants, and `DB
   URL: jdbc:no:x DB Driver: <5-char random name>`; disk artifacts `<install>\server\lib\
   <5-char-name>.class`, `<install>\server\data\content\<5-char-name>.cmd`, `<install>\server\
   data\content\<5-char-name>.out` — the bulletin explicitly notes these files "may be cleaned
   up by the attacker as activity progresses, so their absence does not rule out compromise,"
   consistent with the existing entry's framing but with more artifact specificity than
   currently captured.

5. **Scoping clarifications confirmed by the FAQ** (useful if the entry wants a precision
   note): PaperCut Hive and PaperCut Pocket are **not** affected by this bulletin; Mobility
   Print and Print Deploy server components are **not** affected; the User Client, Print
   Deploy client, and Mobility Print installer client software are **not** affected and do not
   need updating; Site Servers and secondary/print servers **do** need updating to a patched
   version (not just the primary Application Server).

6. Confirms unchanged: v23-and-earlier guidance remains "upgrade to the latest version" (no
   patch for that line), matching the existing entry exactly.

---

## 11. EU CRA reporting-platform update (existing entry: entries/2026-08-29/eu-cra-reporting-obligation-ncsc-fi-checklist.md)

**Existing entry read first.** It currently sources the 24h/72h/14-day/1-month reporting clock
solely to NCSC-FI, with an explicit `sourcing_note` stating: "the specific 24h/72h/14-day/1-
month notification-clock detail is NCSC-FI's alone and not independently corroborated by ENISA
or any other source" and credibility rated `2` (probably true) on that basis. It also states
"until then, only the two named Assigned Representatives per manufacturer can file."

**Primary re-fetched:** https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions (trafilatura-direct; page states "Updated: 31 August
2026")
**Corroborating (legal analysis) re-fetched:** https://www.hlc.com/en/publications/eu-cyber-resilience-act-preparing-for-vulnerability-and-incident-reporting (trafilatura-direct; article
itself dated 2026-06-10, used per task instruction as durable background legal citation, not
as a fresh news item)

**Quote verification:**
- Q1 "The platform is scheduled to be operational by 11 September 2026." — **FAIL —
  formatting artifact only.** ENISA's page wraps the date in markdown bold: "The platform is
  scheduled to be operational by **11 September 2026** ." (also has a stray extra space before
  the final period). Word content identical.
- Q2 "however no Application Programming Interfaces will be provided at this stage" — **PASS**,
  exact verbatim match.
- Q3 "Non-validated ARs will be able to submit up to 20 notifications for one manufacturer
  before validation becomes mandatory." — **PASS**, exact verbatim match.
- Hogan Lovells Cadwalader Art. 69(3) quote — **FOUND and confirmed**: "Notably, the reporting
  obligations apply from 11 September 2026 to all products with digital elements within the
  CRA's scope that have been made available on the EU market before full CRA application (Art.
  69(3) CRA)."

**MATERIAL CORRECTIONS needed to the existing entry (this is the most consequential finding of
this deep-read pass):**

1. **The existing entry's sourcing_note claim that ENISA does not independently corroborate the
   24h/72h/14-day/1-month clock is now FALSE.** ENISA's own FAQ (updated 31 August 2026, Q7,
   "What are the deadlines for reporting?") states, essentially verbatim to NCSC-FI's own
   checklist: "**Early Warning:** Without undue delay and in any case within **24 hours** of
   becoming aware of the vulnerability or incident; **Vulnerability/Incident Notification:**
   Without undue delay and in any case within **72 hours** of becoming aware...; **Final
   Report:** For **vulnerabilities**: No later than **14 days** after a corrective measure
   (e.g., patch) is available. For **severe incidents**: Within **1 month** after the initial
   notification." This is a direct, independent EU-institutional corroboration of the exact
   clock NCSC-FI published — the entry's sourcing_note should be corrected (the numbers are now
   confirmed by two independent authorities, ENISA and NCSC-FI, not NCSC-FI alone), and its
   `classification.credibility` could reasonably move from `2` (probably true) toward `1`
   (confirmed) on that basis, per this deployment's Admiralty scheme (independent corroboration
   is what drives credibility toward 1).

2. **The existing entry's "only the two named Assigned Representatives per manufacturer can
   file" claim appears to UNDERSTATE the actual limit and should be corrected.** ENISA's FAQ
   Q9 states: "There can be only **one Primary AR** per manufacturer, while there can be **up
   to 20 Secondary ARs**." The accurate cap is 1 Primary + up to 20 Secondary = **up to 21**
   Assigned Representatives per manufacturer, not "two." (NCSC-FI's own framing of "a primary
   and backup" may have described a minimum recommended setup rather than the platform's actual
   ceiling — either way, ENISA's FAQ is the more precise and more authoritative source on this
   specific point and should supersede the "two" figure in the entry.)

3. **NEW, not yet in the existing entry:** non-validated ARs can submit up to 20 notifications
   for one manufacturer before validation becomes mandatory — i.e., an AR does not have to wait
   for their AR-manufacturer association to be validated by the coordinating CSIRT before they
   can start filing; validation happens in parallel with reporting. This is a materially useful
   operational detail for any organization's incident-response runbook planning.

4. **NEW, minor:** at launch the SRP will be available in **English only**; ENISA states it
   will "progressively translate the Factsheet and other available material into all EU
   languages" later — worth a one-line note given the constituency's German/French/Italian
   working languages.

5. **Confirmed unchanged / still NCSC-FI-only:** the existing entry's specific claim that
   API-based submission is "expected... from spring 2027" is **not** independently corroborated
   by this ENISA fetch — ENISA's FAQ only states "no Application Programming Interfaces will be
   provided **at this stage**" without giving a specific target date. That "spring 2027" figure
   should continue to be attributed to NCSC-FI alone unless a further ENISA source states it
   explicitly.

6. Confirmed unchanged: SRP go-live date 11 September 2026 (both ENISA's FAQ and the Hogan
   Lovells legal analysis agree); the reporting obligation itself binding on products already
   placed on the EU market before full CRA application, i.e. covering legacy/EOL products too
   (Art. 69(3) CRA per Hogan Lovells — consistent with, and now with a specific legal-article
   citation for, the existing entry's NCSC-FI-sourced note that "products past end-of-life and
   no longer receiving updates remain subject to the reporting obligation").

---

## Fetch failures

None. All 11 primaries (plus every corroborating/cross-check source pursued) were reachable
this run — the only escalations needed were rung 2→4 (jina) for the SonicWall PSIRT SPA shell
and one GitHub advisory/API lookup, both of which succeeded on the jina rung. No source on the
ladder failed outright.
