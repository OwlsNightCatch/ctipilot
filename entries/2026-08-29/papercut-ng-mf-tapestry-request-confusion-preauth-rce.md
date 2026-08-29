---
schema: 1
kind: vulnerability
title: "CVE-2026-82078 / CVE-2026-81578 — PaperCut NG/MF: an Apache Tapestry request-routing confusion chains an unauthenticated config rewrite to arbitrary code execution, exploited before a patch existed"
headline: "PaperCut ships an emergency patch for a pre-auth RCE chain already used against live customers — and a second emergency release after the first one was bypassed"
summary: >
  PaperCut NG and PaperCut MF (all versions) carry an unauthenticated remote-code-execution chain — CVE-2026-81578
  (auth bypass, CVSS4.0 8.8) and CVE-2026-82078 (unsafe dynamic class loading, CVSS4.0 9.4) — that PaperCut confirmed
  under active exploitation on 2026-08-27, before any CVE or patch existed. Emergency Patch Release 2 fixes v24/25/26;
  there is no fix for v23 and earlier, and Huntress estimates 47% of the PaperCut installs it tracks run v23 or older.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-29T0409Z-intel
priority: critical
immediate_action:
  title: "Patch PaperCut NG/MF now, or take internet-facing servers offline"
  action: >
    PaperCut NG and MF are under active exploitation via an unauthenticated request-routing chain that reaches
    remote code execution as the PaperCut server process; two confirmed customer incidents occurred before any
    patch existed, one as recently as 27 August against a still-unpatched v24 install. Apply PaperCut's Emergency
    Patch Release 2 immediately on every v24/25/26 Application Server — Release 2 supersedes the original
    emergency patch, which a Home-page variant of the same request defeated. For v23 and earlier there is no fix
    at all: restrict the Application Server to trusted/internal IP addresses right now, and treat any
    internet-facing instance as potentially compromised until proven otherwise.
tags: [vulnerabilities, zero-day, actively-exploited, pre-auth, rce, no-patch, patch-available]
regions: [global]
sectors: [public-sector, education, healthcare, finance, telco]
entities: []
techniques: [T1190, T1059.007, T1082, T1057, T1070.004]
affected_products: ["PaperCut NG", "PaperCut MF"]
cves:
  - id: CVE-2026-81578
    cvss: "8.8 (CVSS4.0)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "All versions of PaperCut NG and PaperCut MF"
    fixed: "Emergency Patch Release 2 (v24.1.9, v25.0.12, v26.0.4 and later); no fix for v23 and earlier — vendor recommends upgrading to a supported version"
  - id: CVE-2026-82078
    cvss: "9.4 (CVSS4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [exploited, patch-available]
    affected: "All versions of PaperCut NG and PaperCut MF"
    fixed: "Emergency Patch Release 2 (v24.1.9, v25.0.12, v26.0.4 and later); no fix for v23 and earlier — vendor recommends upgrading to a supported version"
sources:
  - url: "https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/"
    publisher: "PaperCut Software (vendor security bulletin)"
    date: "2026-08-29"
    role: primary
  - url: "https://www.huntress.com/blog/papercut-actively-exploited"
    publisher: "Huntress"
    date: "2026-08-28"
    role: primary
  - url: "https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/"
    publisher: "Rapid7"
    date: "2026-08-28"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1095/"
    publisher: "CERT-FR (ANSSI) advisory CERTFR-2026-AVI-1095"
    date: "2026-08-28"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0334"
    publisher: "NCSC-NL advisory NCSC-2026-0334"
    date: "2026-08-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "PaperCut Software security response team is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF."
    publisher: "PaperCut Software"
  - quote: "PaperCut's authorization check could trust the rendered page and miss the permissions required by the component behind it."
    publisher: "Huntress"
  - quote: "By selecting either the public Error page or Exception page for display, an attacker can bypass authentication while invoking administrative components belonging to ConfigEditor or UserList."
    publisher: "Rapid7"
  - quote: "47% of the approximately 2,500 PaperCut installations Huntress tracks are running v23 or older, for which no patch is currently available."
    publisher: "Huntress"
  - quote: "PaperCut has been targeted in the past; in 2023, CVE-2023-27350 was broadly exploited in the wild by multiple threat-actor groups, including ransomware operators."
    publisher: "Rapid7"
verification: multi-source
sourcing_note: >
  PaperCut's own bulletin confirms the vulnerability's existence, active exploitation and the two-CVE structure, but
  the deep technical narrative — the Apache Tapestry request-routing confusion mechanism, the specific HTTP request
  chains, the JDBC/Derby/Nashorn exploitation path, and the Huntress incident-response artifacts — traces to Rapid7
  and Huntress, both rated B (original vendor vuln/incident research) in sources.json rather than A. Reliability held
  at B rather than A to reflect that dependency, the same standard this run applied to its ServiceNow entry.
confidence: high
references: []
deep_dive: true
deep_dive_category: web-app-rce
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Apply PaperCut's Emergency Patch Release 2 to every PaperCut NG/MF Application Server now (v24/25/26); for v23 and earlier, immediately restrict the Application Server's web interface to trusted/internal IP addresses only — no patch exists for that line."
  - "Before patching or restarting an internet-facing server, preserve the server/logs directory and the Application Server's process tree; check server.log for the two vendor-documented error strings and for an unexplained gap or truncation, and check derby.log for a Derby boot line naming an in-memory database directory ending in \"pwn\" — either is a high-confidence sign of prior exploitation."
updates: []
migrated_from: null
---

PaperCut has been hit before at this scale: in 2023, CVE-2023-27350 — an unrelated authentication-bypass flaw in the
same PaperCut NG/MF Application Server — was mass-exploited in the wild by multiple ransomware operators before a
patch existed, a precedent Rapid7's own incident-response team cites directly when framing why this new chain
demands the same urgency ([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Three years later, PaperCut disclosed on 27 August 2026 that it was investigating active exploitation of a new,
unrelated flaw in the same product line — again before any CVE, patch, or public technical detail existed, and
again reconstructed from a real victim's own incident-response evidence: a university customer's security and DFIR
team supplied the reproduction data that let PaperCut confirm and patch the bug
([PaperCut Software, 2026-08-29](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).

PaperCut's Application Server runs on the Apache Tapestry web framework, whose "complex direct" request format lets
a single HTTP request name one page to render and a different page's component to actually execute. PaperCut's own
authorization check validates only the page selected for rendering, not the component that runs behind it — so a
request that asks Tapestry to render the public, unauthenticated Error, Exception, or Home page while invoking the
administrative `ConfigEditor` or `UserList` component bypasses authentication entirely
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Through three such POST requests — `/app?service=direct/1/Error/ConfigEditor/quickFindForm`,
`.../ConfigEditor/$Form`, and `.../UserList/$QuickFind.$Form` — an unauthenticated attacker rewrites four external
card/ID lookup settings (`user-lookup.db-driver`, `user-lookup.db-url`, `user-lookup.id-to-username-sql`,
`user-lookup.enabled`) that normally point PaperCut at an administrator-configured external card database
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Redirected instead to an attacker-controlled JDBC target through PaperCut's bundled Apache Derby driver and its
`foreignViews` feature, the connection reaches an attacker-controlled H2 database whose inline `INIT` statement
creates a JavaScript-backed trigger; PaperCut's bundled Nashorn JavaScript engine then executes that trigger to
launch an operating-system process — full remote code execution as the PaperCut server, triggered the moment the
forged `UserList` search runs the malicious lookup
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
This is a two-CVE chain: CVE-2026-81578 (CWE-306, missing authentication) is the pre-auth entry that gains write
access to the server configuration; CVE-2026-82078 (CWE-470, unsafe dynamic class loading) is the flaw that turns a
reconfigured database connection into arbitrary Java bytecode execution once that write access is held
([PaperCut Software, 2026-08-29](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).

PaperCut treats **all versions** of NG and MF as potentially affected. Huntress observed two live customer
exploitations: one on 26 August lasting under two minutes against version 25.0.10.75465, and a second on 27 August
against version 24.1.5.71847 — before Emergency Patch Release 2 extended coverage to the v24 line
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). In both cases the attacker ran
base64-encoded discovery commands (`whoami & ver`, and separately `whoami & ver & tasklist`) via a dropped,
OS-agnostic Java `.class` file that wrote its output to a temporary file and then deleted both that file and the
server's own `server.log`
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). Huntress's own proof-of-concept
reproduced the full chain against a stock PaperCut NG install and observed the code execution surface as an
observable `charmap.exe` process running as SYSTEM, spawned under the PaperCut Application Server's own `pc-app.exe`
process
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). PaperCut released an initial
emergency patch for v25/v26 on 28 August, which a Home-page variant of the same request bypassed
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Emergency Patch Release 2, published later the same day with hardening developed alongside Huntress and watchTowr,
closes that bypass and extends coverage to v24
([PaperCut Software, 2026-08-29](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
There is no fix for v23 and earlier — PaperCut's guidance for that line is to upgrade to a supported version — and
Huntress estimates 47% of the roughly 2,500 PaperCut installations it tracks still run v23 or older
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)).

Detection, telemetry class first: alert on any child process spawned from `pc-app.exe` or the PaperCut Application
Server's Java process — PaperCut never legitimately spawns a shell, `cmd.exe`, or a system-discovery utility such as
`charmap.exe`, `whoami`, or `tasklist` from that lineage. Web-access logs for the PaperCut Application Server should
be checked for POST requests to `/app?service=direct/*/{Error,Exception,Home}/ConfigEditor/*` or
`.../UserList/$QuickFind.$Form` from unauthenticated or external sources — this URL shape is not a pattern ordinary
PaperCut administration produces. Two log artifacts are near-unique indicators: a `server.log` line reading
`DB URL: jdbc:derby:memory:pwn`, and a corresponding `derby.log` entry recording Derby booting an in-memory database
directory whose name ends in the literal string `pwn`
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). Both PaperCut and Huntress
stress that these artifacts' *absence* does not clear a system, since the observed payloads delete their own
`server.log` evidence after running
([PaperCut Software, 2026-08-29](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
**Triage:** an unexpectedly truncated, gapped, or missing `server.log` on a PaperCut Application Server is not
normal application behavior — legitimate log rotation does not delete mid-file — and is itself a high-confidence
signal worth investigating even where no other artifact survives. **Defender takeaway:** any PaperCut NG/MF
Application Server that has ever been reachable from the public internet should be assumed targeted; patch to
Emergency Patch Release 2 immediately, and where v23 or earlier cannot yet be replaced, remove public exposure
entirely rather than relying on detection alone.
