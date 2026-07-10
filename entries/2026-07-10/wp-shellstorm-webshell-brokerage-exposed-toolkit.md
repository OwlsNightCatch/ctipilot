---
schema: 1
kind: threat
horizon: operational
title: "WP-SHELLSTORM: an exposed webshell-brokerage toolkit reveals 27 weaponized CVEs fired at 1.4M WordPress/Joomla sites plus a parallel Nacos/Spring Boot credential-theft track"
headline: "SOCRadar finds a webshell-brokerage crew's own open staging server — 5,700+ live shells, 27 weaponized CVEs, and a parallel Nacos/Spring Boot credential heist"
summary: >
  SOCRadar found a webshell access-brokerage operation's own Python SimpleHTTPServer left open for 22 days,
  exposing its full toolkit, target lists and logs. The crew (tracked as WP-SHELLSTORM, assessed as
  financially-motivated and Chinese-speaking) fired 27 weaponized CVEs at ~1.4M WordPress/Joomla domains,
  confirming 5,700+ active webshells, with a WordPress caching-plugin flaw the single highest-yield exploit.
  A separate, earlier track abused an Apache Nacos auth bypass with JDumpSpider to steal cloud credentials
  and DB connection strings from Java heap dumps. The breadth-first, FOFA-driven targeting puts any exposed
  Swiss/European CMS or Nacos/Spring Boot estate in scope.
discovered_at: "2026-07-10T20:34:32Z"
event_date: "2026-07-09"
run_id: 2026-07-10T2009Z-intel
priority: notable
immediate_action: null
tags: [actively-exploited, botnet, organized-crime, rce, china-nexus]
regions: [global]
sectors: [public-sector, finance, technology]
entities: [actor:wp-shellstorm]
techniques: [T1190, T1505.003, T1036.004, T1552.001, T1071.001]
affected_products: ["WordPress", "Joomla", "Apache Nacos", "XXL-Job", "Spring Boot"]
cves: []
sources:
  - url: "https://socradar.io/blog/wp-shellstorm-expose-1-4m-wordpress-sites/"
    publisher: "SOCRadar"
    date: "2026-07-09"
    role: primary
  - url: "https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html"
    publisher: "The Hacker News"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "a Python SimpleHTTPServer instance, left open for 22 days, exposed the full toolkit, logs, and target lists"
    publisher: "SOCRadar"
  - quote: "The most productive single exploit was a Breeze Cache Cleaner flaw (45,000+ targets, 17,000+ confirmed shells), followed by a ThemeREX Addons vulnerability (3,378 shells from 46,600 targets)."
    publisher: "SOCRadar"
  - quote: "Ctrl-Alt-Intel's deduplicated count found 25,195 sites with confirmed or validated compromise evidence, while SOCRadar, counting active webshells, put the live figure at 5,700-plus."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: "SOCRadar's Threat Intelligence Team conducted the primary passive-OSINT investigation of the exposed directory; The Hacker News independently cites a second research group (Ctrl-Alt-Intel) whose deduplicated analysis of the same directory reached a higher compromise count. Attribution to a Chinese-speaking, financially-motivated crew is SOCRadar's assessment from language and tooling artifacts, reported as assessed."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "Update or disable the directly-targeted plugins now if you run them: Breeze Cache (CVE-2026-3844) and ThemeREX Addons (CVE-2026-1969); scan WordPress/Joomla web-writable directories (uploads, plugin dirs) for unexpected PHP files and treat any as a web shell until cleared."
  - "If you run Apache Nacos, upgrade to ≥ 2.2.1 with nacos.core.auth.enabled=true and rotate every credential that lived in an exposed instance; test exposure by confirming a 'Nacos-Server' User-Agent request against the cluster-nodes endpoint (CVE-2021-29441) returns no data without auth."
  - "Disable /actuator/heapdump in production and lock all Spring Boot Actuator endpoints behind authentication; close and segment unauthenticated XXL-Job executor endpoints from the internet."
migrated_from: null
---

SOCRadar's Threat Intelligence Team spotted an unauthenticated open directory — a Python SimpleHTTPServer left running for 22 days on a US-based VPS — that exposed the complete toolkit, target lists, bash history and C2 configuration of a webshell access-brokerage operation it names WP-SHELLSTORM ([SOCRadar, 2026-07-09](https://socradar.io/blog/wp-shellstorm-expose-1-4m-wordpress-sites/)). The operation weaponized 27 CVEs (14 critical, 9 high) against roughly 1.4 million WordPress and Joomla domains sourced via FOFA, confirming more than 5,700 live webshells; the single highest-yield exploit was a Breeze Cache Cleaner flaw (CVE-2026-3844) at 45,000+ targets and 17,000+ confirmed shells, followed by a ThemeREX Addons vulnerability (CVE-2026-1969), while a Joomla JCE flaw fired at 560,000+ targets yielded only 77 shells — a reminder that raw target count and success rate diverge with how patched an ecosystem is. The Hacker News independently cites a second team, Ctrl-Alt-Intel, whose deduplicated count reached 25,195 compromised sites; SOCRadar reads the crew as financially motivated rather than state-directed ([The Hacker News, 2026-07-10](https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html)). A parallel, earlier track abused the Apache Nacos authentication bypass (CVE-2021-29441 — a request with a "Nacos-Server" User-Agent header skips auth entirely) to exfiltrate hundreds of Nacos configuration files, yielding cloud credentials, database connection strings and API keys; a separate technique scanned Spring Boot for exposed heap dumps and used the open-source JDumpSpider to pull credentials from those Java memory dumps. Because Nacos config routinely holds XXL-Job admin tokens, one Nacos bypass chains to RCE across connected executor nodes ([SOCRadar, 2026-07-09](https://socradar.io/blog/wp-shellstorm-expose-1-4m-wordpress-sites/)).

The webshell payloads include a multi-layer-obfuscated BestShell-derived `down.php`, a Godzilla-framework variant, and a shell that returns HTTP 404 to normal visitors and blocks crawler user-agents; remote access uses a WebSocket-delivered dropper (SNOWLIGHT) fetching an architecture-matched VShell implant that renames its own process to mimic a Linux kernel worker thread ([SOCRadar, 2026-07-09](https://socradar.io/blog/wp-shellstorm-expose-1-4m-wordpress-sites/)).

**Defender takeaway:** the breadth-first FOFA targeting means exposure is a function of unpatched plugins and internet-reachable Java-stack management interfaces, not of being individually targeted — any Swiss or European public-sector, SME or fintech estate running the named CMS plugins or an exposed Nacos/XXL-Job/Spring Boot instance is a candidate. The durable, vendor-neutral detections are file-integrity monitoring flagging unexpected PHP files under CMS upload/plugin directories, and web-server logs showing scanner-pattern requests at volume against plugin endpoints. **Triage:** the VShell implant masquerades as a kernel worker by renaming its process to a `[kworker/X:Y]` form — the discriminator is that a genuine kernel thread has no backing executable, so a process presenting that name whose `/proc/<pid>/exe` resolves to a real on-disk binary (rather than a kernel path) is the implant, not a kernel worker; a `ps aux` name match alone is not the signal. On the Java side, an unauthenticated request bearing a `Nacos-Server` User-Agent that returns cluster data, or an out-of-band `/actuator/heapdump` generation, is the exposure to hunt.
