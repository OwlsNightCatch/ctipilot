---
schema: 1
kind: threat
title: "Gambling Goblin (Earth Berberoka overlap): a Chinese-speaking cluster compiles malicious Apache modules on compromised Brazilian .gov.br servers, borrowing their search-engine trust for a global gambling-SEO fraud network"
headline: "The victim domain never changes in the browser bar — a hooked Apache module quietly reverse-proxies matching requests to attacker infrastructure"
summary: >
  Check Point Research documents Gambling Goblin, a Chinese-speaking cluster it assesses with medium-to-high
  confidence overlaps Earth Berberoka (tracked since 2022), compromising Brazilian government web servers at every
  administrative tier — federal, state and municipal — since mid-2025 to compile and install custom Apache modules
  that silently reverse-proxy visitors into phishing pages impersonating Google Play, Microsoft Store and Amazon.
  A purpose-built toolset supports the operation, including a reconnaissance agent, a downloader, a credential
  stealer, and two backdoors (oRAT, AlphaAgent) whose codebase and infrastructure Check Point ties to Earth
  Berberoka.
discovered_at: "2026-09-03T05:15:00Z"
updated_at: null
event_date: "2026-09-02"
run_id: 2026-09-03T0410Z-intel
priority: notable
immediate_action: null
tags: [nation-state, organized-crime, ai-abuse, phishing]
regions: [global, latam]
sectors: [public-sector]
entities:
  - actor:earth-berberoka
  - tool:orat
  - tool:alphaagent
  - tool:downpro
techniques: [T1584.004, T1090.002, T1071.001, T1071.004, T1572, T1036.005, T1070.006, T1552.004, T1110, T1595.002, T1497.001, T1614, T1685, T1543.002, T1027, T1105, T1046]
affected_products: ["Apache HTTP Server"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/"
    publisher: "Check Point Research"
    date: "2026-09-02"
    role: primary
  - url: "https://blog.checkpoint.com/research/gambling-goblin-a-chinese-speaking-actor-hijacks-brazilian-government-sites-to-fuel-a-global-seo-fraud-machine/"
    publisher: "Check Point Blog"
    date: "2026-09-02"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/gambling-goblin-brazilian/"
    publisher: "Infosecurity Magazine"
    date: "2026-09-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The group compromises legitimate Brazilian government web servers, many of them .gov.br sites spanning federal, state, and municipal institutions, and installs malicious modules that silently turn them into reverse proxies for phishing content, invisible to the visitor"
    publisher: "Check Point Blog"
  - quote: "We assess with medium-to-high confidence that Gambling Goblin is tied to Earth Berberoka"
    publisher: "Check Point Research"
  - quote: "Audit Apache configurations and installed modules. Look for unexpected .so files, especially any timestamped to match legitimate modules like mod_ssl or mod_suexec."
    publisher: "Check Point Blog"
  - quote: "oRAT was tied to Earth Berberoka in 2022, and the variant we analyzed shares the same orat/cmd/agent codebase and REST-style operator routes"
    publisher: "Check Point Research"
  - quote: "one of the AlphaAgent samples we recovered was uploaded in the same archive as other tools previously attributed to Earth Berberoka, placing AlphaAgent directly alongside the group's known toolset"
    publisher: "Check Point Research"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Check Point Research documents Gambling Goblin, a Chinese-speaking cluster it assesses with medium-to-high
confidence overlaps Earth Berberoka — first documented by Trend Micro in 2022 targeting gambling platforms serving
Chinese-speaking users. Active against Brazilian organisations since mid-2025, primarily government and educational
institutions, the operation's distinguishing move is weaponising the search-engine trust of compromised `.gov.br`
domains: navigation tiles on the resulting fraud pages point to dozens of real domains spanning a federal ministry, a
national public agency, a state legislative assembly, state courts of accounts, a state utility, and numerous
municipal administrations
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
The technique — compromising a government web server to graft attacker content onto its own trusted domain — is
directly transferable to any public-sector web-hosting estate, at any administrative tier, regardless of region.

On an already-compromised Linux host, a Bash installer confirms root, fingerprints the distribution, patches a
missing macro, and compiles a custom Apache module (`opsproxy.c`) via `apxs`, then deletes the build artefacts and
timestomps the resulting `.so` and its load configuration to match legitimate modules such as `mod_ssl` or
`mod_suexec`
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
The module registers at Apache's name-translation stage and inspects every incoming request for a small set of
hardcoded URL prefixes (`/wps`, `/bmw`, `/card` in the analysed samples); a match rewrites the request into a
reverse proxy to a hardcoded upstream, so the visitor is silently relayed to attacker infrastructure while the
request still appears, from the outside, to originate from the legitimate compromised domain
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
The module also strips the site's own Content-Security-Policy header and replaces it with a permissive one allowing
inline/`eval`'d scripts and third-party assets, so the injected phishing content renders unrestricted. A second,
separate Apache module disguises itself as a basic filter, decrypts an RC4-protected ruleset keyed on
path/referrer/User-Agent/client-IP, locates the page body via a compiled-in `<body.*?>` regex, and injects
fetched remote content via `ap_rwrite` — classic SEO-cloaking and content-injection behaviour, distinct from the
reverse-proxy module
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
The upstream phishing pages impersonate Google Play, Microsoft Store and Amazon with fabricated ratings and
`schema.org` metadata, pushing gambling and sports-betting content.

Beyond the Apache modules, the group runs an internet-facing reconnaissance agent (a Go ELF binary wrapping
dirprobe, httpx, naabu, nuclei v3, subfinder and whatweb over gRPC C2) to map attack surface, plus a downloader
(DownPro) that stages the rest of the toolkit, blending its drop paths into names mimicking legitimate system
binaries. Two backdoors carry Check Point's own attribution basis: **oRAT**, a Go RAT with an embedded SSH/SFTP
server that persists as a systemd service disguised as the legitimate `xtables-addons` netfilter package, disables
SELinux enforcement (`setenforce 0`) as part of its setup routine, and masquerades its process as `sshd:
root@pts/0`, sharing the same `orat/cmd/agent` codebase and REST-style operator routes Check Point tied to Earth
Berberoka in 2022
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
**AlphaAgent**, a modular Go backdoor using gRPC-over-HTTPS with browser-fingerprint mimicry (or a DNS covert
channel) and bundling a SOCKS5 proxy and Ligolo-style relay for pivoting, was recovered from the same archive as
tools already attributed to Earth Berberoka, placing it directly alongside the group's known toolset
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
A third attribution point is infrastructure: the group's command-and-control shares Earth Berberoka's historical
Amazon ASN (AS16509)
([Check Point Research, 2026-09-02](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/)).
A credential stealer built on the open-source 3snake project intercepts `sshd`/`sudo`/`su`/`ssh`/`passwd`/`kinit`/
`login` executions via netlink process-event monitoring and `ptrace`, masquerading as one of roughly 29 fake
kernel-thread process names. Check Point states the model is already exported beyond Brazil: parallel phishing
templates localised for Vietnamese, Spanish and English audiences, with daily domain generation.

No source describes how the group obtains its initial foothold on a target web server — the reporting begins from
already-established root access. Defenders should read this as post-compromise infrastructure abuse, not an
exploitation narrative to patch against.

**Triage and hunting:** a sudden absence of Content-Security-Policy headers on specific URL paths of a public-sector
web server is a strong signal of injected reverse-proxy behaviour
([Check Point Blog, 2026-09-02](https://blog.checkpoint.com/research/gambling-goblin-a-chinese-speaking-actor-hijacks-brazilian-government-sites-to-fuel-a-global-seo-fraud-machine/)).
Audit installed Apache modules for `.so` files timestamped to match legitimate modules such as `mod_ssl` or
`mod_suexec` — a mismatch between a module's claimed identity and its actual behaviour is the core detection
concept, not any single file name
([Check Point Blog, 2026-09-02](https://blog.checkpoint.com/research/gambling-goblin-a-chinese-speaking-actor-hijacks-brazilian-government-sites-to-fuel-a-global-seo-fraud-machine/)).
Further behavioural artefacts a defender can hunt for without treating them as fixed indicators: a systemd service
claiming to be `xtables-addons` that does not match the real package's binary; a process presenting as `sshd` but
running from an unexpected path; unexplained `apxs`/module-compilation activity on a production web server outside
a maintenance window; and process names drawn from common kernel-worker naming conventions (`kworker`, `ksoftirqd`,
`watchdog`, `journald`) that do not correspond to genuine kernel threads when inspected further.

**Defender takeaway:** the transferable lesson is architectural, not this specific campaign — any organisation
running public-facing Apache on government or institutional domains should treat unexpected Apache module changes,
timestomped `.so` files, and stripped security headers on specific paths as high-priority investigation triggers,
since the value an attacker extracts here is entirely the domain's own search-engine and user trust, not data theft
from the server itself.
