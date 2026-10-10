---
schema: 1
kind: vulnerability
title: "Elementor Pro (WordPress): unauthenticated arbitrary file upload to RCE via a validator/mover desynchronization in the Forms File Upload field (CVE-2026-32475, CVSS 9.0)"
headline: "Two loops in the same file disagree about what an empty upload field means, and the disagreement is remote code execution"
summary: >
  CVE-2026-32475 (CVSS 9.0) affects Elementor Pro ≤4.2.1, fixed in 4.2.2. A validator/mover
  desynchronization in the Forms module's File Upload field lets an unauthenticated visitor upload
  a .php payload to any published page carrying a Form widget with a File Upload field — an
  everyday configuration such as a job-application or support-ticket form — with no session or
  nonce required, and the stored filename is recoverable from the server's own Date header.
discovered_at: "2026-08-28T05:45:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, T1505.003]
affected_products: ["Elementor Pro (WordPress plugin)"]
cves:
  - id: CVE-2026-32475
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Elementor Pro ≤4.2.1"
    fixed: "4.2.2"
sources:
  - url: "https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/"
    publisher: "Patchstack"
    date: "2026-08-19"
    role: primary
  - url: "https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html"
    publisher: "The Hacker News"
    date: "2026-08-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An empty first entry makes validation() return before it ever type-checks the .php entry that follows it. process_field(), meanwhile, only continues past that empty entry and moves the .php one anyway. The validator reports a clean submission because it stopped reading; the mover proceeds because it did not."
    publisher: "Patchstack"
  - quote: "The .php file lands in wp-content/uploads/elementor/forms/, a public, web-accessible directory, letting a fully unauthenticated visitor place executable PHP on the server and, by requesting the file directly, achieve remote code execution."
    publisher: "Patchstack"
verification: multi-source
sourcing_note: >
  Patchstack is the discloser's own disclosure venue (Tin Pham/TF1T reported to Patchstack), read
  and reviewed by Patchstack as the reproducing party who confirmed the patch effective; The Hacker
  News corroborates independently. Wordfence's own blog post naming the flaw was unreachable on
  every transport this run (persistent anti-bot response, jina reader credit-exhausted); this
  entry is composed entirely from Patchstack's own technical account, not attributed to Wordfence.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade Elementor Pro to 4.2.2 or later on every WordPress site now, and audit wp-content/uploads/elementor/forms/ for any .php file as a compromise check regardless of current patch level — any published page with a Form widget carrying a File Upload field (Required toggle off by default) has been exposed since before this disclosure."
updates: []
migrated_from: null
---

CVE-2026-32475 (CVSS 9.0) affects Elementor Pro ≤4.2.1, fixed in 4.2.2 (patched 19 August, patch reviewed and confirmed effective by Patchstack). The Forms module's File Upload field (`modules/forms/fields/upload.php`) validates an upload's extension in one loop (`validation()`) and moves accepted files to a public directory in a separate loop (`process_field()`) — and the two loops disagree about what an empty file entry (`UPLOAD_ERR_NO_FILE`) means. `validation()` does `if (!required && UPLOAD_ERR_NO_FILE) return;` — an empty first entry makes it abandon checking the entire field, including every later entry. `process_field()` instead does `if (UPLOAD_ERR_NO_FILE) continue;` — it skips only the empty entry and still moves everything after it: "an empty first entry makes validation() return before it ever type-checks the .php entry that follows it. process_field(), meanwhile, only continues past that empty entry and moves the .php one anyway. The validator reports a clean submission because it stopped reading; the mover proceeds because it did not" ([Patchstack, 2026-08-19](https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/)).

Submitting two file parts for one File Upload field — an empty first part, then a `.php` payload as the second — makes the validator report a clean submission (it stopped reading before reaching the `.php` entry) while the mover still processes and moves that `.php` file. The blocklist check (`is_file_type_valid()`, which does correctly reject php/phtml/asp/etc.) never runs against the payload at all: "the .php file lands in wp-content/uploads/elementor/forms/, a public, web-accessible directory, letting a fully unauthenticated visitor place executable PHP on the server and, by requesting the file directly, achieve remote code execution" ([Patchstack, 2026-08-19](https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/)).

The only prerequisite is any published Elementor page containing a Form widget with a File Upload field (Required toggle off by default) — an everyday configuration such as a job-application, support-ticket, or "attach a document" form. Every value the exploit needs (`post_id`, `form_id`, the field's `form_fields[ID]` name) is visible in the page's public HTML, and the request goes through the `elementor_pro_forms_send_form` AJAX action with no cookie or nonce required. Recovering the stored filename — always `uniqid().extension`, discarding the submitted name — is cheap: the 8 hex "seconds" digits come straight from the server's own `Date:` response header, leaving only 5 hex microsecond digits to brute-force, or, on forms with an autoresponder email action enabled (common on the same job-application/support-ticket forms), Elementor's own default notification template discloses the exact upload URL to the attacker-controlled email address with zero brute-forcing. The fix in 4.2.2 synchronizes the two loops' empty-entry handling and additionally re-checks the extension inside `process_field()` itself, immediately before the move, so the blocklist now guards the sink directly.

**Triage:** any `.php` (or other server-executable) file under `wp-content/uploads/elementor/forms/` is a compromise indicator regardless of current patch level. On the request side, form submissions to `elementor_pro_forms_send_form` carrying multiple file parts for a single File Upload field — one empty, one non-empty — are the delivery shape; a legitimate single-file upload never needs a leading empty part, so its presence has no benign explanation.
