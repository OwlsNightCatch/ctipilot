---
schema: 1
kind: vulnerability
horizon: operational
title: "22 CVEs in Tobit TeamDavid, a DACH-region self-hosted Microsoft 365 alternative: an unauthenticated heap leak hands over stored mailbox passwords, and the vendor stopped responding"
headline: "One unauthenticated endpoint returns uninitialised heap memory containing user credentials — roughly 12,000 TeamDavid instances are internet-facing"
summary: >
  InfoGuard Labs published 22 CVEs on 2026-08-07 against the Webbox web application of Tobit
  TeamDavid, an enterprise collaboration and unified-messaging suite marketed across the DACH region
  as a self-hosted alternative to Microsoft 365, which the researchers put at roughly 12,000 publicly
  accessible instances. The load-bearing chain needs no authentication: requesting
  /.well-known/mta-sts. with an extension that does not resolve makes the server return up to 4 KB of
  uninitialised heap memory from earlier requests, which leaks the per-user access.ini files whose
  stored passwords are obfuscated with a trivially reversible XOR scheme rather than hashed — giving
  an attacker any user's mailbox. A single unauthenticated request to /internalRestart also takes the
  service down until an administrator restarts it by hand. The CVE records bound every issue at
  TeamDavid through Rollout 524 and name no fixed release; the researchers state they cannot say
  which flaws are fixed, and report that
  the vendor stopped responding to both them and the national cyber security centre that had taken up
  the coordination.
discovered_at: "2026-08-09T04:46:00Z"
event_date: "2026-08-07"
run_id: 2026-08-09T0412Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, pre-auth, info-disclosure, dos, identity]
regions: [dach]
sectors: [public-sector]
entities: []
techniques: [T1190, T1552.001, T1187, T1499, T1005]
affected_products: ["Tobit Laboratories AG TeamDavid"]
cves:
  - id: CVE-2026-54203
    cvss: "9.2"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54218
    cvss: "8.8"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54213
    cvss: "9.2"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54210
    cvss: "9.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54212
    cvss: "9.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54211
    cvss: "9.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54209
    cvss: "8.9"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54208
    cvss: "8.5"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54202
    cvss: "8.5"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54200
    cvss: "8.4"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-12070
    cvss: "8.4"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54204
    cvss: "7.7"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54201
    cvss: "6.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54205
    cvss: "6.3"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54206
    cvss: "6.3"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54207
    cvss: "6.3"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54216
    cvss: "5.3"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54217
    cvss: "5.3"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54215
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54214
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-54199
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
  - id: CVE-2026-12071
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "TeamDavid through Rollout 524"
    fixed: "not stated"
sources:
  - url: "https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/"
    publisher: "InfoGuard Labs"
    date: "2026-08-07"
    role: primary
closed_sources: []
evidence:
  - quote: "Current data from Shodan and Censys indicates approximately 12,000 publicly accessible instances."
    publisher: "InfoGuard Labs"
  - quote: "Successful exploitation primarily leads to the complete compromise of user mail accounts, with the potential for full system compromise."
    publisher: "InfoGuard Labs"
  - quote: "Both the NCSC and our team had been ghosted by the manufacturer despite multiple follow-up emails."
    publisher: "InfoGuard Labs"
  - quote: "Update to newest version, we don’t exactly know which vulnerabilities are fixed and which are not"
    publisher: "InfoGuard Labs"
verification: single-source
sourcing_note: >
  Single-source: InfoGuard Labs is the sole assessor. The published CVE records carry the same
  researchers' findings through the assigning authority, so they corroborate nothing independently —
  they are the same assessment with a second publisher, which is why credibility stays at 2. Those
  records were still read individually to fix provenance: every identifier, CVSS 4.0 base score, the
  per-flaw mapping in `cves[]` and the "TeamDavid through Rollout 524" affected bound come from the
  per-CVE records rather than from the post, which groups several identifiers under a single heading
  without stating which identifier names which flaw — pairing them by position would have been a
  guess. No fixed release is named in either place. One internal discrepancy in the record for
  CVE-2026-54211: its description says an authenticated attacker while its CVSS vector carries PR:N;
  this entry follows the description, which agrees with the discloser. First coverage, and published
  2026-08-07 — just outside this run's 26-hour window. It reaches the brief now because the InfoGuard
  Labs source record carried a listing-extraction defect that hid its publication dates from every
  previous run; that recipe was repaired during this fire, so the disclosure had never been eligible
  for coverage before today. The researchers name the coordinating authority only as "the NCSC"; this
  entry does not assume which one.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Establish whether any TeamDavid Webbox in your estate or your suppliers' is reachable from the internet, and put it behind a VPN or a filtering reverse proxy that blocks /internalRestart and /.well-known/mta-sts. — a single unauthenticated request to the first drops the service, and repeated requests to the second return heap memory containing other users' credentials."
  - "Rotate the passwords of every account on an exposed TeamDavid instance rather than only the ones you can prove were leaked: credentials are stored reversibly on disk, so any prior file-system or heap exposure has already handed over usable plaintext."
  - "Block outbound 445/TCP from the TeamDavid server, which is what turns the UNC-path handling in its search and messaging functions into NetNTLM capture or SMB relay against your own domain."
migrated_from: null
---

InfoGuard Labs published 22 CVEs on 2026-08-07 against the Webbox web application of Tobit TeamDavid, an enterprise collaboration and unified-messaging suite sold across the DACH region as a self-hosted alternative to Microsoft 365 and combining mail, video conferencing and chat with fax, SMS and physical letter mail; the researchers found the flaws during an external penetration test and put current Shodan and Censys data at approximately 12,000 publicly accessible instances ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). Their own summary of the impact is that successful exploitation primarily leads to complete compromise of user mail accounts, with the potential for full system compromise ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)).

The chain that needs no credentials is two flaws deep. The application is largely file-based, and access to each user's mailbox is governed by an `access.ini` file in that user's directory holding the username and a stored password that is obfuscated rather than encrypted — each character XORed against a key derived from 128 plus its index position, which anyone holding the file can reverse, and in some instances the password is stored in plaintext outright without the researchers being able to pin down what triggers that (CVE-2026-54218) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). Reaching those files remotely is what the second flaw provides. The unauthenticated `/.well-known/mta-sts.` handler treats the part of the URL after `mta-sts.` as a file extension and reads the corresponding file from a fixed directory; when that file does not exist it skips the read but continues processing a buffer it allocated and never zeroed, then returns the leftover heap contents as an HTTP 200 body — up to 4 KB of residual memory from earlier requests, which in the researchers' testing spilled `access.ini` contents, email, attachments, configuration files and SQL queries (CVE-2026-54203) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). Poll the endpoint, recover an `access.ini`, decode the password, log in as that user.

Separately, an endpoint named `/internalRestart` does not restart anything — one unauthenticated request shuts the web server down entirely and it stays offline until an administrator brings it back by hand (CVE-2026-54213) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). Four further buffer overflows crash the server, three of them needing no credentials at all: an overlong filename in the file-upload functions (CVE-2026-54210), a request body beginning with a number followed by at least seven characters on an API endpoint (CVE-2026-54212), and the password-change handler, which is triggered by putting the string `(editini)` in the request path and loads the file at that path into a fixed-size stack buffer without checking that it is actually an `Archive.ini`, so an unauthenticated caller can point it at any oversized file (CVE-2026-54209); the fourth, in several form parameters of the `serverClient_close.html` endpoint, requires an authenticated session (CVE-2026-54211) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). The researchers observed these terminate the process with `STATUS_STACK_BUFFER_OVERRUN` and note that the stack cookie blocks a straightforward return-address overwrite, while stating that with a different stack state or a canary leaked through another flaw these could potentially escalate to remote code execution ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)) — that escalation is explicitly hypothetical and has not been demonstrated.

The remaining flaws matter mostly for what they do to the surrounding domain. Four separate functions resolve attacker-supplied UNC paths, so the server can be made to authenticate outbound to an attacker-controlled host and hand over NetNTLM material for capture or relay whenever 445/TCP egress is permitted: the search function's `pathnameroot` parameter takes it without authentication, though a `../` in the URL is needed to get past the authorisation check (CVE-2026-54204), while the link-storing, `@@INCLUDE` messaging and archive-move paths require an authenticated session (CVE-2026-54205, CVE-2026-54206, CVE-2026-54207) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). An authenticated user can attach arbitrary server files to an outgoing message with `@@attach` and download them, bypassing the filter over configuration and user directories through NTFS alternate data streams, which reaches the server's private key and other users' `access.ini` files (CVE-2026-54200); delete any file on the server with `@@COMMENTFILE` (CVE-2026-12070); and create folders anywhere on disk, including system directories and other users' private directories, through the archive-creation path (CVE-2026-54202) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). An unauthenticated arbitrary file write in the password-change function, constrained by the target directory's own `access.ini`, still allows planting a `.htm` file that executes JavaScript when opened (CVE-2026-54208), and error logs are served with no authentication or authorisation check at a predictable URL (CVE-2026-54201) ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). A reflected and a stored cross-site scripting flaw, two open redirects and two HTTP header injections round out the set ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)).

The disclosure history is the reason this is an exposure decision rather than a patching one. The researchers first contacted the vendor on 2025-11-05, submitted 13 findings on 2025-12-27, were told on 2026-01-27 that eight were patched with five scheduled for the next release, retested on 2026-02-06 and found several only partially remediated plus nine new issues, escalated to a national cyber security centre on 2026-02-17, sent CVE drafts on 2026-05-28, and by 2026-08-06 recorded that both they and that centre had been ghosted by the manufacturer despite multiple follow-up emails — publishing the next day ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). Their first recommendation is to update to the newest version while stating plainly that they do not know which vulnerabilities are fixed and which are not ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). The published CVE records bound every one of the 22 issues at TeamDavid through Rollout 524 and name no fixed release, which is why the `cves[]` records on this entry carry none. No in-the-wild exploitation is reported by any party.

**Defender takeaway:** treat this as an exposure-and-credential problem rather than a patching one, while noting the one piece of good news in the same recommendation block — the researchers say the two endpoint flaws this entry leads on, the `/internalRestart` denial of service and the `/.well-known/mta-sts.` heap leak, seem to be fixed in the newest version, even as they state they cannot say which of the 22 are fixed overall ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). The vendor also told them on 2026-05-29 that it was working on a rewrite, without commenting on the CVE drafts ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)) — so remediation work exists, but nothing published lets an operator map a build number to a fixed flaw. The researchers' own guidance is to keep the Webbox off the open internet behind a VPN or a filtering reverse proxy that blocks the non-essential endpoints, restrict outbound SMB, rotate credentials on the basis that reversible storage means any earlier file-system exposure already leaked usable passwords, and consider migrating — their stated reasoning being that the issues are rooted in the file-based architecture rather than isolated coding mistakes, so a comparable security baseline would need substantial re-engineering ([InfoGuard Labs, 2026-08-07](https://labs.infoguard.ch/posts/22-cves-in-david-a-secure-m365-alternative/)). For a Swiss or German public-sector body, the supplier question is the sharper one: this product is chosen precisely by organisations avoiding a hyperscale cloud suite, so it turns up in exactly the estates that assume self-hosting is the conservative option.

**Triage:** requests to `/.well-known/mta-sts.` are not inherently hostile — MTA-STS is a real mail-security mechanism and a policy fetch is ordinary. Two things separate the leak from that traffic in web-server access logs: a legitimate client fetches `mta-sts.txt` at the documented path, whereas exploitation requests a varying stream of extensions that do not exist, and it repeats — the leak returns whatever happens to be in reused heap, so an attacker polls rather than fetching once. A run of 200 responses to distinct non-existent extensions from one source is the signal; a single `mta-sts.txt` fetch is not.
