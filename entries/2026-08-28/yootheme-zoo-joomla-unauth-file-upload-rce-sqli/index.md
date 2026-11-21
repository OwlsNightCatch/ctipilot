---
schema: 1
kind: vulnerability
title: "YOOtheme ZOO for Joomla: unauthenticated file-upload RCE (CVSS 10.0) plus a precondition-free SQL injection reachable with no submission form at all — three releases in three days, and the 3.x line has no fix"
headline: "A Joomla content extension trusts the client's own Content-Type header to decide what an anonymous visitor can upload"
summary: >
  mySites.guru found three unauthenticated flaws in YOOtheme ZOO (com_zoo) for Joomla, affecting
  every version 1.0.0–4.1.63: CVE-2026-74803 (CVSS 10.0) is an arbitrary-file-upload-to-RCE via
  a Content-Type-only validation bypass in the front-end submission form; CVE-2026-74804 (CVSS
  9.3) is a precondition-free unauthenticated SQL injection reachable even with no submission form
  configured. Fixed in ZOO 4.1.66 after two follow-up releases; no fix exists for the 3.x line.
discovered_at: "2026-08-28T05:30:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, sqli, pre-auth, patch-available, no-patch]
regions: [global, europe]
sectors: [public-sector, technology]
entities: [trend:joomla-extension-file-upload-rce-wave]
techniques: [T1190, T1505.003]
affected_products: ["YOOtheme ZOO (com_zoo)", "YOOtheme Pro for Joomla"]
cves:
  - id: CVE-2026-74803
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "YOOtheme ZOO 1.0.0–4.1.63"
    fixed: "4.1.64 (superseded by 4.1.66)"
  - id: CVE-2026-74804
    cvss: "9.3"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "YOOtheme ZOO 1.0.0–4.1.63 — reachable on any installation, not only sites with a submission form enabled"
    fixed: "4.1.64 (superseded by 4.1.66)"
  - id: CVE-2026-76612
    cvss: "8.6"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "YOOtheme ZOO — missed or introduced by the 4.1.64 fix"
    fixed: "4.1.66"
  - id: CVE-2026-76613
    cvss: "8.6"
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "YOOtheme Pro for Joomla and WordPress — CVSS corrected 23 August from 9.2 with a PR:N vector YOOtheme told the CNA was wrong, to 8.6 with PR:H; the record's own description still says 'any contributor-level user', a mismatch mySites.guru flags as unresolved"
    fixed: "5.0.41 (WordPress); 4.5.34 with a regression fix in 4.5.35 (Joomla-3-only line)"
  - id: CVE-2026-75114
    cvss: "5.1"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "YOOtheme ZOO — Twitter comment callback"
    fixed: "4.1.64 (superseded by 4.1.66)"
sources:
  - url: "https://mysites.guru/blog/zoo-unauthenticated-file-upload-rce/"
    publisher: "mySites.guru"
    date: "2026-08-25"
    role: primary
closed_sources: []
evidence:
  - quote: "ZOO lets visitors submit content through a front-end submission form"
    publisher: "mySites.guru"
  - quote: "The Image element validates that attachment. It builds a validator configured with a MIME type group of image and a maximum size"
    publisher: "mySites.guru"
  - quote: "The problem is which value that validator inspects. It reads the Content-Type header the client attached to the upload."
    publisher: "mySites.guru"
  - quote: "A site with no submission form at all is still fully exposed to this one."
    publisher: "mySites.guru (on CVE-2026-74804)"
verification: single-source
sourcing_note: >
  mySites.guru is the discoverer and sole publisher for the ZOO findings; its own CVE records,
  filed through the Joomla CNA, are the underlying authority for the identifiers themselves, which
  makes this closer to a first-party disclosure than a media report despite the single-source
  label. Reliability reflects mySites.guru's standing as an original Joomla-security research
  outlet rather than an aggregator.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every YOOtheme ZOO (com_zoo) installation to 4.1.66 or later now, regardless of whether the front-end submission form is enabled — CVE-2026-74804 (unauthenticated SQL injection) is reachable on any site running ZOO at all. There is no fix for the 3.x line; treat any ZOO 3.x installation as permanently exposed and plan migration or removal."
  - "Audit images/zoo/uploads/ on every ZOO installation for any non-image file, especially .php, as a compromise check regardless of current patch level — the file-upload flaw (CVE-2026-74803) predates this week's disclosure across the entire 1.0.0–4.1.63 range."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): the first evidence quote spliced three
      non-contiguous source fragments with ellipses; split into three separate verbatim
      records (a residual flagged by the publishing fire's own final verification pass).
      No factual claim changed.
    fields: [evidence]
migrated_from: null
---

mySites.guru (Phil Taylor) found and reported three unauthenticated flaws in YOOtheme ZOO (`com_zoo`), a Joomla content-construction extension, affecting every version 1.0.0 through 4.1.63. CVE-2026-74803 (CVSS 10.0, CWE-434) is an arbitrary-file-upload-to-RCE: the front-end submission form's Image element validates an upload solely by trusting the client-supplied `Content-Type` header — "the Image element validates that attachment. It builds a validator configured with a MIME type group of image and a maximum size", and, as the discloser puts it, "the problem is which value that validator inspects. It reads the Content-Type header the client attached to the upload" ([mySites.guru, 2026-08-25](https://mysites.guru/blog/zoo-unauthenticated-file-upload-rce/)) — never inspecting file bytes or enforcing an extension allow-list. An anonymous visitor uploads a `.php` file declared `image/jpeg`; Joomla's `File::makeSafe()` preserves the `.php` extension, and the file lands executable inside `images/zoo/uploads/`, a directory the web server executes PHP from.

CVE-2026-74804 (CVSS 9.3, CWE-89) is a precondition-free unauthenticated SQL injection in `ItemController::element()` — two unescaped request values pasted into the query's string-comparison condition — reachable on any site running ZOO at all: "a site with no submission form at all is still fully exposed to this one" ([mySites.guru, 2026-08-25](https://mysites.guru/blog/zoo-unauthenticated-file-upload-rce/)). mySites.guru proved it bypasses access filters and extracts the database name and version via UNION-based extraction. CVE-2026-75114 (CVSS 5.1) is a lower-severity open redirect in the Twitter comment callback.

All three were fixed in ZOO 4.1.64 (2026-08-19), but two follow-up releases inside three days closed five further issues that 4.1.64 had missed or introduced, including CVE-2026-76612 (CVSS 8.6, unauthenticated stored XSS via comments/field elements) — current guidance is 4.1.66 or later. No fix exists for the ZOO 3.x line at all, since the affected range starts at 1.0.0. The same week, YOOtheme Pro for Joomla shipped its own fix for CVE-2026-76613 (SQL injection); the CVSS score was corrected on 23 August from 9.2 with a `PR:N` (no privileges required) vector to 8.6 with `PR:H`, after YOOtheme told the CNA the original vector was wrong — though mySites.guru flags one mismatch the correction did not resolve: the record's own description still reads "any contributor-level user", a role most sites treat as barely privileged, while `PR:H` denotes privileges giving significant control over the component; mySites.guru states it has not audited YOOtheme Pro itself and cannot settle which reading is right, and this entry carries that same open question rather than treating `PR:H` as settled — and the fix was backported to the Joomla-3-only 4.5.x line in 4.5.34 (24 Aug) with a regression fix in 4.5.35 (25 Aug) after that first backport introduced a new problem.

**Triage:** any non-image file under `images/zoo/uploads/` — especially `.php`, `.phtml` or any server-executable extension — is a compromise indicator regardless of current patch level, since the flaw has existed since ZOO 1.0.0. For the SQL injection, unusual UNION-shaped query patterns or boolean-timing probes against ZOO's item-listing endpoints from unauthenticated sessions are the discriminator; ZOO's normal front-end traffic issues parameterised, predictable queries.
