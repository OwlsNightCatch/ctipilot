---
schema: 1
kind: vulnerability
horizon: operational
title: "GitLab CE/EE RCE via the Jupyter-notebook diff renderer and two ~5-year-old Oj Ruby-parser memory-corruption bugs — public PoC, silent patch, no CVE"
headline: "Public PoC chains two Oj Ruby-parser bugs to code execution on self-managed GitLab; the fix shipped as an unlabeled dependency bump"
summary: >
  depthfirst published a working proof-of-concept (2026-07-24) chaining two
  memory-corruption bugs in the native-C Oj Ruby JSON parser into remote code
  execution on default self-managed GitLab CE/EE — reachable by any user with
  push access to a project via a crafted .ipynb file and the notebook-diff
  renderer, no admin or CI access and no victim interaction. GitLab bumped the
  vulnerable Oj dependency in its 10 June 2026 releases (18.10.8 / 18.11.5 /
  19.0.2) without listing it in the security-fix table and with no CVE assigned,
  so operators that gate patching on GitLab's security-advisory feed alone were
  unknowingly exposed for 44 days before the PoC dropped. No in-the-wild
  exploitation is reported.
discovered_at: "2026-07-26T04:25:36Z"
event_date: "2026-07-24"
run_id: 2026-07-26T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, poc-public, patch-available, supply-chain]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["GitLab CE", "GitLab EE"]
cves: []
sources:
  - url: "https://depthfirst.com/research/going-depthfirst-achieving-gitlab-rce-via-two-ruby-memory-corruption-vulnerabilities"
    publisher: "depthfirst"
    date: "2026-07-24"
    role: primary
  - url: "https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html"
    publisher: "The Hacker News"
    date: "2026-07-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The resulting chain affected GitLab CE and EE versions 15.2.0 through 18.10.7, 18.11.0 through 18.11.4, and 19.0.0 through 19.0.1."
    publisher: "depthfirst"
  - quote: "A normal authenticated user able to create or push to a project and view the resulting commit diff could commit an .ipynb file"
    publisher: "depthfirst"
verification: single-source
sourcing_note: >
  Single-origin primary research: depthfirst is the sole discloser; The Hacker
  News re-reports its findings rather than corroborating independently. The claim
  is backed by a published PoC (GitHub wupco/gitlab-rce-demo) and by the
  independently verifiable GitLab fixed releases (18.10.8 / 18.11.5 / 19.0.2,
  bundling Oj 3.17.3). The two chain bugs carry no CVE; a separate set of nine
  Oj advisories came out of the same review and cover other Oj APIs, also fixed
  in Oj 3.17.3.
confidence: medium
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
  - "Confirm every self-managed GitLab CE/EE instance is on 18.10.8 / 18.11.5 / 19.0.2 or later (Oj ≥ 3.17.3) — the fix was not in GitLab's security-fix table, so a version check is the only reliable signal; upgrade any instance in 15.2.0–18.10.7 / 18.11.0–18.11.4 / 19.0.0–19.0.1."
migrated_from: null
---

depthfirst disclosed (2026-07-24) a remote-code-execution chain against default self-managed GitLab CE/EE, reached through GitLab's in-tree `ipynbdiff` gem, which calls `Oj::Parser.usual.parse` — the native-C implementation of the Oj Ruby JSON parser — whenever a commit diff contains a `.ipynb` (Jupyter notebook) file ([depthfirst, 2026-07-24](https://depthfirst.com/research/going-depthfirst-achieving-gitlab-rce-via-two-ruby-memory-corruption-vulnerabilities)). Two Oj memory-safety bugs that had survived in the parser for nearly five years (introduced 2021-08-08, first shipped in Oj 3.13.0, and reachable in GitLab from 15.2.0 once notebook validation switched to Oj in July 2022) are combined: an unchecked 16-bit key-length narrowing truncates an oversized object key and causes GitLab's notebook-diff output to print a live heap pointer (used to defeat ASLR and locate libc/libruby), and an unchecked nesting-stack overflow in `Oj::Parser.usual.parse` supplies a write primitive that redirects a parser callback to `system()`. The whole chain needs no elevated access — in depthfirst's words, "A normal authenticated user able to create or push to a project and view the resulting commit diff could commit an .ipynb file" ([depthfirst, 2026-07-24](https://depthfirst.com/research/going-depthfirst-achieving-gitlab-rce-via-two-ruby-memory-corruption-vulnerabilities)) — no admin rights, no CI/runner access, no victim interaction — by committing two crafted notebooks and requesting the commit diff (`GET /<project>/-/commit/<sha>/diffs_stream`).

The affected range is GitLab CE/EE 15.2.0–18.10.7, 18.11.0–18.11.4 and 19.0.0–19.0.1; GitLab shipped the fixed Oj (3.17.3) in its 10 June 2026 releases 18.10.8, 18.11.5 and 19.0.2 ([The Hacker News, 2026-07-25](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html)). The operationally important detail is that GitLab did not record the fix in its security-fix table and no CVE was assigned to the GitLab chain, so any operator that tracks GitLab patching against the vendor's security-advisory feed missed it for the 44 days between the silent 10 June bump and the 2026-07-24 PoC publication; GitLab.com and Dedicated instances were already patched, but self-managed operators must act. A separate set of nine Oj advisories (covering the dumper, loader, SAJ callback and document APIs, each with its own CVE) came out of the same depthfirst review and are also fixed in Oj 3.17.3. No in-the-wild exploitation is reported; this is a disclosed researcher PoC.

**Detection:** in GitLab web/application-access telemetry (Rails/Workhorse request logs), the exploit's own mechanics surface as `.../-/commit/<sha>/diffs_stream` requests correlated with recently-pushed `.ipynb` files carrying implausible JSON field lengths — object keys near the 65,535-byte boundary that only make sense as a deliberate truncation trigger; the attacker must push two purpose-built notebooks and then request their diff in sequence. In host process telemetry, a shell interpreter forked from the GitLab Puma/Rails worker (parent image `puma` / `bundle exec puma`) would reflect the `system()` redirection this chain achieves. **Triage:** routine data-science notebook review produces `diffs_stream` requests too — the discriminators are the anomalous multi-kilobyte JSON key lengths in the pushed notebook and the parent-of-shell being the Puma worker, neither of which appears in legitimate notebook diffing. Because the chain needs only ordinary push access, tightening project push-access grants is a meaningful interim control for instances that cannot upgrade immediately, but there is no vendor workaround short of the patch.
