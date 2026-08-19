---
schema: 1
kind: threat
horizon: operational
title: "StopAndProtect runs its whole operation off other people's WordPress sites — a must-use plugin that never appears in the plugin list, a hidden REST route that accepts PHP, and an installer that deletes itself"
headline: "Roughly 2,000 hijacked sites are the infrastructure, not the victims, and the persistence lives where nobody looks"
summary: >
  Check Point Research published an analysis on 2026-08-18 of StopAndProtect, a criminal toolkit it first saw
  in mid-May 2026 that hosts its payloads, command-and-control and stolen data on compromised WordPress sites
  rather than on dedicated infrastructure. Persistence on each hijacked site is a must-use plugin dropped at
  wp-content/mu-plugins/wp-sec.php — a directory WordPress auto-loads on every request and does not show in
  the standard plugin list — which registers a hidden REST route authenticated by hardcoded credentials that
  will write files, explicitly including PHP, almost anywhere under the site root; the installer then
  deactivates and deletes itself. Delivery is a fake-CAPTCHA paste-and-run lure leading through two .NET
  loader stages to a component set covering encryption, an SMB/USB worm, a credential and screenshot
  collector, a lock screen and an operator chat channel. Check Point states no initial-compromise vector and
  names no actor.
discovered_at: "2026-08-19T05:35:00Z"
event_date: "2026-08-18"
run_id: 2026-08-19T0410Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, infostealer, phishing, supply-chain, data-breach]
regions: [global, europe]
sectors: [public-sector, education, technology, retail]
entities: [campaign:stopandprotect, malware:silentencryptor]
techniques: [T1204.004, T1059.001, T1620, T1505.003, T1105, T1135, T1091, T1047, T1059.005, T1113, T1056.001, T1486, T1657]
affected_products: ["WordPress"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/"
    publisher: "Check Point Research"
    date: "2026-08-18"
    role: primary
closed_sources: []
evidence:
  - quote: "We first noticed a ransomware family called StopAndProtect in the middle of May 2026."
    publisher: "Check Point Research"
  - quote: "It authenticates with hardcoded credentials."
    publisher: "Check Point Research"
  - quote: "It lets anyone who knows valid credentials upload files to almost any path under the WordPress root."
    publisher: "Check Point Research"
  - quote: "They do not appear/manage like normal plugins in the standard Plugins UI."
    publisher: "Check Point Research"
  - quote: "There are many vulnerable WordPress websites simply because their owners do not keep them updated."
    publisher: "Check Point Research"
  - quote: "It also contains a few text files listing close to 2,000 compromised WordPress domains, giving us a hint about the size of the operation."
    publisher: "Check Point Research"
verification: single-source
sourcing_note: >
  Check Point Research is the only party to have analysed this operation; the corroborating hit found this run
  was Check Point's own corporate blog restating the same research, which is the same assessor and therefore
  not corroboration. No editorially independent second publisher was located, so this ships single-source at
  credibility 2 with the mechanism resting on one research lab's direct observations. Check Point provides
  hashes, screenshots and dual-perspective chat captures for each component it names, so the component set is
  its own observation rather than inference — but it states no initial-compromise vector for the WordPress
  sites (no CVE, no credential-stuffing claim, only a general observation that unmaintained sites are
  plentiful), and names no ransomware lineage, actor or overlap with any tracked operation. This entry
  therefore asserts no access vector and no attribution. The victim-distribution figures are described rather
  than quoted where they appear only as a table row, and Check Point itself qualifies its log analysis as
  partial, with sandbox and researcher traffic mixed in. The report's own defender guidance is a single line
  about Check Point's own products; the detection framing below is derived from the mechanics it documents.
confidence: medium
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
  - "On every WordPress site you own, list the contents of wp-content/mu-plugins — files there load on every request and do not appear in the admin plugin list, so a hostile one is invisible to the usual review — and treat any unrecognised file, wp-sec.php in particular, as a live backdoor rather than a stale artifact."
  - "Enumerate the REST routes each WordPress site actually exposes and compare against the routes its installed plugins should register; a route that no known plugin accounts for is the finding."
migrated_from: null
---

Check Point Research published its analysis of StopAndProtect on 2026-08-18, an operation it had been tracking since it "first noticed a ransomware family called StopAndProtect in the middle of May 2026" ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)). The name originally applied only to the encryption component and was extended to the whole operation because encryption is not the universal outcome — many victims are only quietly mined for data. The structural point, and the reason this matters to organisations that are not themselves targets, is where the operation lives: payload hosting, command-and-control and stolen-data collection all run on compromised WordPress sites rather than on infrastructure the operators own.

The persistence mechanism is the part worth acting on, because it is chosen specifically to defeat the review an administrator would actually perform. Check Point recovered an installer from one hijacked server which, on activation, writes a must-use plugin to `wp-content/mu-plugins/wp-sec.php`. Files in that directory load automatically on every request, and — the property that matters — "They do not appear/manage like normal plugins in the standard Plugins UI" ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)). The planted plugin registers a hidden REST route, `wp-sec/v1/upload`; "It authenticates with hardcoded credentials" and "It lets anyone who knows valid credentials upload files to almost any path under the WordPress root", explicitly including `.php` files ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)). The installer then deactivates and deletes itself. What remains is a file in a directory nobody browses, reachable by anyone holding a static credential, that will write executable code anywhere on the site.

Delivery to end users is the now-familiar paste-and-run pattern: a fake verification page on a hijacked site logs the visitor and puts a PowerShell command on the clipboard for the victim to run themselves, and Check Point records that "the infection chain starts with a ClickFix social-engineering technique, which prompts victims to execute a PowerShell command" ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)). Two PowerShell stages lead to a base64-encoded .NET assembly that is decoded and loaded in memory, and each .NET stage reaches the next by reflectively enumerating the loaded assembly's types for a static, parameterless method of a fixed name and invoking it — a generic in-memory hand-off repeated at every stage, so nothing after the first command touches disk as an executable. The final component set covers encryption (with per-file keys derived from a password and machine-name pair the operator embeds in the renamed file), an SMB and removable-media worm, a Visual Basic script spreader that moves laterally by creating processes remotely through Windows management interfaces, a lock screen carrying the ransom note, a collector that keylogs, lists files, harvests messaging contacts through interface automation and screenshots the desktop at half-minute intervals while the victim is active, and a bespoke victim-to-operator chat utility.

The scale estimate comes from the operators' own mistake. Check Point assesses that the operator infected their own machine and uploaded desktop files to the collection server, which yielded the source of a fleet-management tool used to toggle the lure across the estate, and "It also contains a few text files listing close to 2,000 compromised WordPress domains, giving us a hint about the size of the operation" ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)). A separate exposed directory held roughly 700 stolen-data archives and about 31,000 victim screenshots gathered between mid-May and the end of July 2026. Log analysis as of 24 July 2026 indicates more than 6,000 unique victim addresses, distributed most heavily across the United States and then Russia and India in a table Check Point publishes; the lab qualifies this as partial, noting sandbox and researcher traffic in the data and that one server's log had been reset more than once.

On how the WordPress sites themselves were taken, Check Point makes no claim beyond an observation that "There are many vulnerable WordPress websites simply because their owners do not keep them updated" ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)), illustrated by one compromised site found running a five-year-old WordPress core with around forty identifiable issues. No CVE, no credential-theft finding, no actor name and no lineage to any previously tracked operation are offered, and none is asserted here.

**Defender takeaway:** for most organisations in this constituency the exposure is being conscripted rather than encrypted — a public-sector or institutional WordPress site becomes the hosting layer for someone else's extortion operation, which is a reputational and legal problem before it is a security one, and this pipeline has already covered Swiss websites compromised and repurposed to serve paste-and-run lures. The two checks that matter are cheap and specific: enumerate `wp-content/mu-plugins` on every site you own, and reconcile the REST routes each site exposes against the plugins that should be registering them. Detection on the endpoint side rests on process lineage — a script interpreter spawned from a browser or from the clipboard-driven run dialog, followed by a second interpreter stage and then no new executable on disk at all, is the shape this chain leaves. **Triage:** administrators and deployment tooling legitimately place files in plugin directories and legitimately register REST routes, so presence alone is not the signal; the discriminators are that a must-use plugin file corresponds to no installed, inventoried plugin, that the route it serves accepts writes authenticated by a credential no administrator issued, and on the endpoint that the interpreter chain originates from user-initiated paste rather than from a scheduled task or a management agent.
