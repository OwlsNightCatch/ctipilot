---
schema: 1
kind: threat
title: "\"ted backdoor\" and curlRAT — a DPRK-nexus actor recompiles a victim's own HAProxy source tree to hide C2 inside the load balancer's self-reported connection statistics"
headline: "Rapid7 finds a DPRK-nexus implant that falsifies HAProxy's own traffic counters so its command-and-control never appears in the load balancer's own logs"
summary: >
  Rapid7 Labs documents a previously undocumented Linux espionage toolkit against two South Korean
  media and automotive-sector organizations: a custom HAProxy filter ("ted backdoor") compiled
  directly into a recompiled HAProxy 2.8.12 binary that decrements the proxy's own live connection
  counters after every command-and-control exchange, paired with a companion RAT (curlRAT) built
  into trojanized replacements of crond, agetty, atd and polkitd. Attributed with medium confidence
  to a DPRK-nexus cluster via C2-infrastructure overlap with APT37.
discovered_at: "2026-09-07T04:37:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-07T0411Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - infostealer
  - identity
regions:
  - apac
sectors:
  - media
  - manufacturing
entities:
  - "actor:scarcruft"
  - "malware:ted-backdoor"
  - "tool:curlrat"
techniques:
  - T1190
  - T1059.004
  - T1106
  - T1574.006
  - T1543
  - T1548
  - T1036.005
  - T1685.006
  - T1070.006
  - T1685
  - T1027
  - T1497.001
  - T1480
  - T1556.003
  - T1539
  - T1082
  - T1057
  - T1185
  - T1119
  - T1071.001
  - T1132.001
  - T1102
  - T1572
  - T1568
  - T1041
  - T1560
affected_products:
  - "HAProxy"
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/"
    publisher: "Rapid7 Labs"
    date: "2026-09-03"
    role: primary
  - url: "https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html"
    publisher: "The Hacker News"
    date: "2026-09-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The toolkit is attributed with medium confidence to DPRK APTs, given that the attacks Rapid7 observed were targeting South Korean media and automotive sectors, likely aiming at long-term espionage, the usage of simple xor-based encryption, custom substitution cipher, and the list of C2s hardcoded is associated to APT37 by ThreatFox and maltrail."
    publisher: "Rapid7 Labs"
  - quote: "First, it reaches into HAProxy's internal counters to decrement active connection stats, referencing fields from the proxy struct via hardcoded 2.8.12 offsets to clear any trace left: the per-backend beconn/feconn and the global actconn, then 64-bit fields within be_counters (cum_conn, cum_req, bytes_in, bytes_out) guarded against underflow, and 32-bit peak metrics (sps_max, conn_max, cps_max) decremented only when exactly 1."
    publisher: "Rapid7 Labs"
  - quote: "It is not a HAProxy vulnerability, and installing it requires code execution on the host and the ability to replace the running binary."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: >
  Attribution rests on three separate, only partially reconciled evidentiary threads rather than a
  single confirmed cluster: the hardcoded C2 domain list is tagged to APT37 by ThreatFox and
  maltrail; the watering-hole delivery model otherwise overlaps Kaspersky's Operation SyncHole,
  which Kaspersky attributed to Lazarus; and Rapid7 notes both victims ran an exposed groupware
  login portal consistent with documented Kimsuky tradecraft. Rapid7 itself flags that APT37 and
  Lazarus are organizationally distinct DPRK clusters operating under different agencies per
  Mandiant's 2023 structure assessment, so the medium-confidence attribution is to "DPRK APTs"
  generically, not to a single named actor; this entry links only the registry's APT37 alias
  (actor:scarcruft) as the specific evidentiary thread the C2 infrastructure supports.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Rapid7 Labs documents a previously undocumented Linux espionage toolkit deployed against two South Korean automotive- and media-sector organizations, active since at least early 2025. Rather than exploiting a HAProxy vulnerability, the operators obtained code execution on the host by some other route and recompiled the victim's own HAProxy 2.8.12 source tree to embed a custom filter plugin — internally named `ted_plugin`, left in debug strings as "ted backdoor" — that hooks HAProxy's native HTTP parser, memory-pool allocator and event scheduler ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). Because it is compiled into the load balancer's own binary rather than exploiting a flaw in it, the technique defeats vulnerability scanning and version-string checks outright: a recompiled binary still reports the same version string as a clean build ([The Hacker News, 2026-09-04](https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html)).

The filter's defining trick is anti-forensic self-falsification. After every command-and-control exchange, it reaches into HAProxy's own internal counters — using hardcoded struct offsets specific to build 2.8.12 — and decrements the per-backend connection counts (`beconn`/`feconn`), the global active-connection count (`actconn`), and cumulative traffic fields (`cum_conn`, `cum_req`, `bytes_in`, `bytes_out`), so the C2 traffic that passed through the load balancer never appears in its own self-reported statistics or logs ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). A request to one hardcoded static-asset-style path switches the filter into C2 mode — beacon, file upload/download, shell command execution, configuration update — while outside that mode it can passively capture session cookies and selected HTTP headers, or, when several conditions match (a specific User-Agent pattern, a payload-path selector byte, a URL/referer regex, and either IP allow/deny-list membership or an operator key smuggled in the Accept-Language header that overrides IP filtering), substitute or append attacker content into the HTTP response body via HAProxy's own body-editing callbacks while rewriting `Content-Type`/`Content-Length` and stripping `Accept-Ranges` so the size change goes unnoticed by the client.

A companion RAT, curlRAT (named for its libcurl-based networking — distinct from the unrelated CurlBack RAT attributed to the Pakistan-linked SideCopy group), is compiled into trojanized replacements of `crond`, `agetty`, `atd` and `polkitd` ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). It polls a hardcoded C2 over HTTPS (with an HTTP fallback) every 12 hours by default — or every 30 seconds in an operator-set fast-poll mode — decoding tasking through a Base64-plus-rolling-XOR pipeline, and offers command execution, file transfer, an interactive PTY/reverse shell that escalates to full root privilege before handoff, and a watchdog thread that first checks for the presence of a specific virtualization-driver file before activating — sleeping and aborting if the host does not look virtualized, an anti-analysis check against sandboxed detonation — before reporting HAProxy's running/stopped/restarted state back to the operator every hour ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). If its primary C2 host fails configuration validation, curlRAT falls back to a second hardcoded server, and it derives a per-victim tracking identifier from a hash of host-specific values — hostname, IP address, hardware UUID and a cron-version string — letting the operator distinguish individual infected hosts across a botnet-style deployment rather than relying on a random or sequential ID ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). A stager component deploys only when HAProxy or cron are already present, verifies root, overwrites the legitimate `crond` binary in place, timestomps the replacement to match another system binary's own creation time, and scrubs the keywords `tmp`/`wget`/`cron`/`crond` from root's bash history and six system logs including `auth.log` and `audit/audit.log`, staged through a file named to resemble a JSP engine artifact ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). A separately trojanized `sshd` intercepts plaintext credentials into an encrypted log file for later retrieval ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)).

Rapid7 could not establish the initial-access vector with certainty, but notes both victims ran an exposed groupware login portal and mail server on the same edge host — a plausible entry point Rapid7 says is consistent with documented Kimsuky tradecraft against Korean groupware vendors ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)). The watering-hole delivery model otherwise overlaps Kaspersky's Operation SyncHole (November 2024–February 2025), which Kaspersky attributed to Lazarus; Rapid7 explicitly notes APT37 and Lazarus are organizationally distinct DPRK clusters operating under different agencies, so the toolkit's attribution rests on three only partially reconciled threads (APT37 via C2 infrastructure, Lazarus via the delivery model, Kimsuky via the initial-access hypothesis) rather than a single confirmed cluster ([Rapid7 Labs, 2026-09-03](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/)).

**Defender takeaway:** an internet-facing HAProxy (or comparable load-balancer/reverse-proxy) deployment's own logs and connection statistics cannot be trusted as a complete audit trail once an attacker has host-level code execution — verify binary integrity for edge daemons (`haproxy`, `crond`, `agetty`, `atd`, `polkitd`, `sshd`) against package-manager-recorded checksums from an out-of-band process, and correlate independently captured network telemetry (NetFlow, a downstream device's own access log) against the load balancer's self-reported counters: a gap where externally observed traffic volume exceeds what the proxy itself records is the core discriminator this technique defeats internally. Cross-check system-daemon binary modification times against the package manager's own install/update transaction history rather than against each other, since the technique deliberately timestomps the replacement to match a different system binary. A near-total absence of routine keywords (`cron`, `crond`, `wget`, `tmp`) across bash history and system logs on a host where such activity is normally routine is itself the anomaly this toolkit's log-scrubbing produces.

**Triage:** a legitimate in-house HAProxy Lua or filter module can also hook the HTTP parser and modify response bodies, so that alone is not the signal. The discriminating feature this mechanism supports is that no operationally normal filter module needs to actively decrement or zero HAProxy's own connection or traffic counters — any module observed doing so, rather than only reading them, warrants immediate investigation.
