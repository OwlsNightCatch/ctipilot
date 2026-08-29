---
schema: 1
kind: research
title: "Git commit-signature malleability mints a second \"Verified\" GitHub commit with a different hash — defeating hash-based blocklists"
headline: "Research: signature malleability lets anyone forge a second \"Verified\" GitHub commit under a new hash, bypassing SHA-based supply-chain controls"
summary: >
  Jacob Ginesin (CMU / Cure53) showed that Git/GitHub's "Verified" commit badge is not a
  unique identifier: given any signed commit, an attacker without the signing key can mint
  a second, distinct commit with the same tree, author and date and a still-valid signature —
  differing only in its hash. The cause is signature malleability (ECDSA (r,s)→(r,n−s);
  ignorable OpenPGP subpackets; S/MIME encoding), not a hash collision. Hash-based
  incident-response blocklists and push-protection rules can be trivially bypassed. A public
  PoC tool exists; no CVE and no Git/GitHub fix as of disclosure.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-08"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, poc-public, no-patch]
regions: [global]
sectors: [technology, public-sector, finance, telco]
entities: []
cves: []
sources:
  - url: "https://thehackernews.com/2026/07/github-verified-commits-can-be.html"
    publisher: "The Hacker News"
    date: "2026-07-08"
    role: primary
  - url: "https://arxiv.org/abs/2607.02820"
    publisher: "Jacob Ginesin (CMU / Cure53) — arXiv preprint"
    date: "2026-07-02"
    role: primary
  - url: "https://github.com/JakeGinesin/git-chain-malleator"
    publisher: "Jacob Ginesin — public PoC tool (git-chain-malleator)"
    date: "2026-07-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Given any signed commit, someone without the signing key can mint a second commit with the same files, author, and date, and a valid signature, GitHub still stamps 'Verified.'"
    publisher: "The Hacker News, summarising Jacob Ginesin's research"
  - quote: "GitHub does not normalize a signature before checking it. No strict encoding on S/MIME, no stripping of those OpenPGP fields, and non-canonical ECDSA values accepted as-is."
    publisher: "The Hacker News, summarising Jacob Ginesin's research"
verification: multi-source
sourcing_note: null
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
  - "Do not rely on commit-hash (SHA) allow/deny-listing alone for supply-chain integrity — after a known-bad-commit takedown, hunt for repeat pushes of content-identical trees under new commit hashes."
  - "Pair 'Verified' status with content-level diffing/allowlisting; treat the badge as authorship provenance only, not commit-identity uniqueness."
migrated_from: null
---

Jacob Ginesin (Carnegie Mellon PhD student, Cure53 auditor) published research on 2 July, amplified by The Hacker News on 8 July, showing that Git/GitHub's **"Verified" commit badge is not a unique identifier**: given any signed commit, an attacker without the signing key can mint a second, distinct commit with an identical tree, identical author/date metadata, and a valid signature that still shows "Verified" — differing only in its resulting hash ([The Hacker News, 2026-07-08](https://thehackernews.com/2026/07/github-verified-commits-can-be.html); [Ginesin, arXiv, 2026-07-02](https://arxiv.org/abs/2607.02820)). The root cause is **signature malleability**, not a hash collision. A commit's SHA is computed over everything inside it, including the raw signature bytes in its header, and many signatures can be rewritten into a different-but-valid form.

Three malleation routes are demonstrated: (1) for ECDSA, the classical algebraic symmetry that turns a valid pair `(r,s)` into `(r, n−s)` using only public curve parameters, producing a second equally-valid signature over the same payload with different bytes and therefore a different commit hash; (2) for RSA and EdDSA under OpenPGP, appending an ignorable experimental subpacket in the unhashed subpacket region defined in RFC 4880 §5.2.3; (3) an analogous X.509/S-MIME path. GitHub does not normalize or canonicalize a signature before verifying it — no strict encoding enforcement on S/MIME, no stripping of the manipulable OpenPGP fields, and non-canonical ECDSA values accepted as-is ([The Hacker News, 2026-07-08](https://thehackernews.com/2026/07/github-verified-commits-can-be.html)). A public exploitation tool implementing all three attacks, plus demo repos where the malleated commits still show "Verified", is released ([Ginesin, git-chain-malleator](https://github.com/JakeGinesin/git-chain-malleator)). Ginesin reported to GNU/Git in January and GitHub in March 2026; neither had shipped a fix at publication, and no CVE is assigned. Maps to `T1195.002 Compromise Software Supply Chain` as a control-bypass primitive.

**Defender takeaway:** any organisation — including government CI/CD pipelines — that keys incident-response or push-protection controls off a specific commit SHA should treat those controls as bypassable. After taking down a known-malicious commit, an operator can re-push a content-identical "ghost twin" under a fresh, equally-"Verified" hash that is not on the blocklist. Move integrity decisions to tree hash + author + content diff, allowlist content rather than commit identity, and read "Verified" as provenance rather than uniqueness until Git/GitHub canonicalize signatures.
