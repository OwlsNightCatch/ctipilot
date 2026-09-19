---
schema: 1
kind: threat
title: "CISA replaces the KEV 14-day rule: BOD 26-04 introduces risk-tiered remediation with a 3-day class for the worst exposures"
headline: "CISA replaces the KEV 14-day rule: BOD 26-04 introduces risk-tiered remediation with a 3-day class for the worst exposures"
summary: "CISA issued Binding Operational Directive 26-04 (\"Prioritizing Security Updates Based on Risk\") on 10 June, superseding and revoking BOD 19-02 and BOD 22-01 — the directive that created the flat KEV remediation deadlines (CISA, 2026-06-10)."
discovered_at: "2026-06-12T05:00:03Z"
event_date: 2026-06-10
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - us-nexus
regions:
  - us
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk"
    publisher: CISA BOD 26-04
    role: primary
  - url: "https://www.cisa.gov/news-events/news/patch-smarter-not-harder"
    publisher: "CISA — Patch smarter, not harder"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cisa-tells-govt-agencies-to-patch-critical-exploited-flaws-in-3-days/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-12.md
---

CISA issued Binding Operational Directive 26-04 ("Prioritizing Security Updates Based on Risk") on 10 June, superseding and revoking BOD 19-02 and BOD 22-01 — the directive that created the flat KEV remediation deadlines ([CISA, 2026-06-10](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk)). US federal civilian agencies must now tier remediation by four criteria: internet exposure of the asset, KEV listing, exploit automatability, and total-versus-partial technical impact. Vulnerabilities meeting all four require remediation within **three calendar days plus a forensic triage before patching** to determine whether the system was already compromised; low-risk findings may defer to the next upgrade cycle. CISA's companion post cites AI-accelerated exploitation as a driver and notes that "only 26% of vulnerabilities on CISA's Known Exploited Vulnerabilities (KEV) Catalog were fully remediated by organizations in 2025," with median time-to-remediation rising to 43 days ([CISA, 2026-06-10](https://www.cisa.gov/news-events/news/patch-smarter-not-harder)). The directive binds only US FCEB agencies — it carries no jurisdictional weight in Switzerland or the EU — but the four-criterion model is a transferable benchmark for patch-governance SLAs under NIS2 Art. 21 vulnerability-handling obligations.

**Why it matters to us:** if your patch SLA still treats every KEV entry identically, the four-criterion test (exposed + KEV + automatable + total control) is a defensible way to concentrate emergency-change effort; CISA's pilot data suggests only ~1 % of findings land in the 3-day class.
