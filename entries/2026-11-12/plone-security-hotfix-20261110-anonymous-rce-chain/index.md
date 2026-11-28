---
schema: 1
kind: vulnerability
title: "Plone security fix of 2026-11-10: a chain of missing security declarations and opened modules lets an anonymous visitor run code on the server in every supported Plone version and back to 4.3; a working proof of concept exists, no CVE ids yet, no exploitation reported"
headline: "Plone anonymous RCE chain: update or install the 20261110 hotfix, block portal_modifier, check modifier conditions"
summary: >
  The Plone and Zope security team released fixes on 2026-11-10 for a chain of issues that together let an anonymous visitor run code on the server in Plone 6.0, 6.1 and 6.2 and, per the team, back to at least 4.3; the entry point is a CMFEditions flaw rated 9.8 with no privileges required, and its advisory says a working proof of concept exists. The team's fixes are the updated packages or the hotfix package Products.PloneHotfix20261110, a workaround that blocks URLs containing portal_modifier has applied since the 2026-11-02 pre-announcement, CVE ids are requested and no source reports exploitation.
discovered_at: "2026-11-12T04:12:30Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-12T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:plone"]
techniques: [T1190, T1059.006]
affected_products: ["Plone"]
cves: []
sources:
  - url: "https://community.plone.org/t/plone-security-hotfix-20261110/23313"
    publisher: "Plone Security Team"
    date: "2026-11-10"
    role: primary
  - url: "https://github.com/plone/Products.CMFEditions/security/advisories/GHSA-67qm-q795-jh7h"
    publisher: "Plone (GitHub Security Advisory, Products.CMFEditions)"
    date: "2026-11-10"
    role: corroborating
  - url: "https://community.plone.org/t/pre-announcement-plone-security-fix-20261110/23303"
    publisher: "Plone Security Team"
    date: "2026-11-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It is a chain of several issues, which together let an anonymous visitor run code on the server."
    publisher: "Plone Security Team"
    source_url: "https://community.plone.org/t/plone-security-hotfix-20261110/23313"
  - quote: "A working proof of concept exists."
    publisher: "Plone (GitHub Security Advisory, Products.CMFEditions)"
    source_url: "https://github.com/plone/Products.CMFEditions/security/advisories/GHSA-67qm-q795-jh7h"
  - quote: "A changed modifier condition stays in the database, also after you install the fix."
    publisher: "Plone Security Team"
    source_url: "https://community.plone.org/t/plone-security-hotfix-20261110/23313"
verification: single-source
sourcing_note: "A disclosure by the Plone and Zope security team for its own product, with its five GitHub advisories; no independent source corroborates it and no CVE ids are assigned yet (requested). The anonymous step is the CMFEditions advisory (CVSS network, no privileges, 9.8); the CMFPlone, MimetypesRegistry and plone.batching advisories are each 9.1 with high privileges required and plone.restapi is moderate, so the anonymous code execution belongs to the chain, not to each advisory. No source states a Swiss deployment."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every Plone site, update to CMFPlone 6.2.3, 6.1.6 or 6.0.16 with the helper packages the Plone team lists, or install Products.PloneHotfix20261110 on any version from 4.3 to 6.2, restart all Zope instances, keep blocking URLs that contain portal_modifier at the front web server, and then check the modifier conditions with @@check-modifier-conditions or the hotfix's startup warning, because an anonymous request can already have stored a malicious condition that survives the fix."
updates: []
migrated_from: null
---

The Plone and Zope security team says the fixes it released on 2026-11-10 close a chain of several issues that together let an anonymous visitor run code on the server, in all supported Plone versions (6.0, 6.1 and 6.2) and in older ones back to at least 4.3 ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)). The anonymous entry point is Products.CMFEditions: the conditional modifiers in portal_modifier had no security declarations, so an anonymous visitor could change a modifier's TALES condition and then run it, and the condition is also evaluated when an editor saves versioned content ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)). Products.CMFPlone, Products.MimetypesRegistry and plone.batching opened whole modules to restricted code, which let TALES expressions and Python scripts escape the sandbox and reach modules such as os, and plone.restapi opened the json module ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)). The CMFEditions advisory rates its flaw 9.8 with no privileges required and states that a working proof of concept exists; the team says details are public and that with current AI tools it may not take long to turn them into a working exploit, and no source reports exploitation ([Plone, 2026-11-10](https://github.com/plone/Products.CMFEditions/security/advisories/GHSA-67qm-q795-jh7h); [Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)).

The fixed packages are CMFPlone 6.2.3, 6.1.6 and 6.0.16 with the helper package versions the announcement lists, or the hotfix Products.PloneHotfix20261110, which covers Plone 4.3 to 6.2, and all Zope instances must be restarted afterwards ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)). The team's pre-announcement of 2026-11-02 already gave the workaround, to block any URL containing portal_modifier at the web server at any path depth, which only helps if Zope's own port cannot be reached directly; the team advises keeping it after updating ([Plone Security Team, 2026-11-02](https://community.plone.org/t/pre-announcement-plone-security-fix-20261110/23303)). After the fix, restricted code can import only the names Plone itself needs from the closed modules, so custom scripts that import others now get an Unauthorized error ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)).

**Exposure:** any Plone site reachable by anonymous visitors, on a version below the fixed packages; no source states a non-default setting that the anonymous path needs, and Plone 5.2 and older are out of security support, with the fix released as an exception.

**Detection:** web-server access logs for anonymous requests whose path contains portal_modifier; and the stored state, which survives the update: a changed modifier condition stays in the database, so as Manager open @@check-modifier-conditions on the site root, or read the hotfix's startup log line that reports modified versioning conditions, and treat the server as compromised if a condition is not recognised, although defaults have changed over time so a difference alone is not an attack ([Plone Security Team, 2026-11-10](https://community.plone.org/t/plone-security-hotfix-20261110/23313)).

**Defender takeaway:** update or install the hotfix and restart now on every internet-facing Plone site, keep the portal_modifier block in place, and run the modifier-condition check afterwards, because the fix does not remove a condition an anonymous request already stored.
