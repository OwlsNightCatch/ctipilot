---
schema: 1
kind: vulnerability
horizon: operational
title: "Bouncy Castle for Java 1.85 — 32 CVEs published three weeks after the silent fix: three certificate-validation bypasses and a static Diffie-Hellman key-recovery flaw rated critical"
headline: "Bouncy Castle publishes 32 CVE write-ups for a July release — three break certificate validation, one leaks a static DH key"
summary: >
  The Legion of the Bouncy Castle published CVE records and per-flaw technical write-ups for 32
  vulnerabilities on 2026-08-03, three weeks after the fixed binaries shipped in Bouncy Castle for
  Java 1.85 / 1.85.1 on 2026-07-12. Four are rated critical. Three of them independently defeat a
  distinct certificate-validation guarantee — a stapled OCSP response accepted without being bound
  to the certificate under test, a JSSE hostname CN-fallback that ships enabled despite documenting
  the opposite, and a name-constraint bypass via a trailing dot — while the fourth is a different
  class entirely: an MTI/A0 Diffie-Hellman agreement that exponentiates an unvalidated peer value,
  leaking the static private key. No exploitation is reported, but the fix commits
  and full root-cause detail are now public while unpatched estates are not — inventory
  org.bouncycastle artifacts below 1.85 (BC-LTS 2.73.12, per-module FIPS builds) and upgrade.
discovered_at: "2026-08-03T05:10:00Z"
event_date: "2026-08-03"
run_id: 2026-08-03T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, dos, patch-available]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1557, T1499.004]
affected_products: ["Bouncy Castle for Java", "Bouncy Castle for Java LTS", "Bouncy Castle FIPS Java API"]
cves:
  - id: CVE-2026-8763
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "Name Constraints bypass via trailing dot in rfc822Name and URI"
  - id: CVE-2026-12185
    cvss: "7.1"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "BKS/UBER keystore allocates from untrusted lengths before integrity check"
  - id: CVE-2026-12802
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "CMS AuthEnvelopedData fails to enforce tag-length on decryption"
  - id: CVE-2026-12803
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "KCCMBlockCipher MAC does not bind nonce when AAD is absent (cross-nonce AEAD forgery)"
  - id: CVE-2026-12816
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "IESEngine stream-mode MAC forgery via length-dependent KDF split"
  - id: CVE-2026-12817
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "OpenPGP AEAD decryption skips final tag on chunk-aligned data"
  - id: CVE-2026-12852
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (from 1.73)"
    fixed: "1.85"
    note: "MLS wire decoder allocates attacker-declared opaque length before bounds check — does not affect BC-LTS"
  - id: CVE-2026-12860
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "RSA PKCS#1 verification skips last two hash bytes in NULL-omitted path"
  - id: CVE-2026-13506
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "Lazy ASN.1 sequence forcing resets nesting-depth guard"
  - id: CVE-2026-13586
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "PKCS#12 MAC and bag-decryption KDF iteration-count bound (DoS)"
  - id: CVE-2026-14682
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "Possible OOM from unbounded up-front allocation on a definite-length read"
  - id: CVE-2026-15055
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "PKCS#8 / PBES2 decryptors honour unbounded KDF cost from input"
  - id: CVE-2026-58059
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "Quadratic-time escaping when stringifying X.500 distinguished names"
  - id: CVE-2026-58060
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "HSS public-key level count unbounded, enabling huge allocation on verify"
  - id: CVE-2026-58061
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "CCM-family modes write plaintext to caller buffer before tag check"
  - id: CVE-2026-58062
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "Stapled OCSP response accepted without binding to the checked certificate"
  - id: CVE-2026-58063
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "BCFKS keystore load honours unbounded KDF cost from untrusted file"
  - id: CVE-2026-59638
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "JSSE hostname verifier CN-fallback enabled by default despite documented opt-in"
  - id: CVE-2026-59639
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "CMS verifySignatures returns true for SignedData with zero signers"
  - id: CVE-2026-59640
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "OpenPGP CFB quick-check oracle active on symmetric/session-key paths"
  - id: CVE-2026-59641
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "S/MIME validator trusts signer-asserted signingTime for path validation"
  - id: CVE-2026-59642
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "CMS AuthenticatedData content not bound to MAC when authAttrs present"
  - id: CVE-2026-59643
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (from 1.81); BC-FJA bcpg-fips < 2.0.13"
    fixed: "1.85 (BC-FJA bcpg-fips 2.0.13)"
    note: "OpenPGP inline-signature policy failures silently ignored; does not affect BC-LTS"
  - id: CVE-2026-59644
    cvss: "8.7"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (from 1.73)"
    fixed: "1.85"
    note: "MLS hash-ratchet honours arbitrary 32-bit generation counter from sender — does not affect BC-LTS"
  - id: CVE-2026-59645
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "OER parser recurses without depth limit on self-referential IEEE 1609.2 schema"
  - id: CVE-2026-59646
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "DTLS handshake reassembler allocates buffer from unchecked 24-bit length"
  - id: CVE-2026-59647
    cvss: "6.9"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "CRMF/CMP password-MAC honours unbounded iteration count"
  - id: CVE-2026-59648
    cvss: "6.9"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "OpenPGP Argon2 S2K honours attacker-chosen memory and passes"
  - id: CVE-2026-59649
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "OpenPGP user-attribute subpacket length bounded only by JVM max memory"
  - id: CVE-2026-59650
    cvss: "9.3"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "MTI/A0 DH agreement exponentiates unvalidated peer value"
  - id: CVE-2026-59651
    cvss: "7.1"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85 (BC-LTS < 2.73.12)"
    fixed: "1.85 (BC-LTS 2.73.12)"
    note: "BKS keystore accepts legacy version with 16-bit integrity MAC key"
  - id: CVE-2026-59652
    cvss: "6.9"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Bouncy Castle for Java < 1.85"
    fixed: "1.85"
    note: "LDAP filter injection in legacy jdk1.4 LDAPStoreHelper — does not affect BC-LTS"
sources:
  - url: "https://raw.githubusercontent.com/bcgit/bc-java/main/docs/releasenotes.html"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9058062"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059638"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%908763"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059643"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059650"
    publisher: "Legion of the Bouncy Castle"
    date: "2026-08-03"
    role: primary
closed_sources: []
evidence:
  - quote: "CVE-2026-58062 - Stapled OCSP response accepted without binding to the checked certificate."
    publisher: "Legion of the Bouncy Castle"
  - quote: "The javadoc for the property says the unset default must DISABLE the fallback, but the code ships with it active in every deployment that doesn't explicitly set the property to false."
    publisher: "Legion of the Bouncy Castle"
  - quote: "An attacker who controls a name-constrained intermediate CA can issue certificates for email/URI hosts that the constraints were meant to exclude."
    publisher: "Legion of the Bouncy Castle"
verification: single-source
sourcing_note: >
  All substantive detail originates with the Legion of the Bouncy Castle, which is both the
  maintainer and the CVE numbering authority for this batch. NVD and ENISA EUVD carry the same CNA
  records rather than an independent assessment, so this is one assessor with several publishers;
  the scores and affected ranges quoted here are read from the per-CVE NVD records and the official
  release notes rather than from any roundup. The published fix commits are independently
  inspectable code, which corroborates that the fixes exist but is not a second assessment.
  The CVSS 4.0 base scores in this entry's CVE metadata are the numbering authority's own,
  read from its published records; neither the release notes nor the per-flaw pages carry a
  score, which is why severity appears in the metadata rather than as a cited claim in the body.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory org.bouncycastle artifacts (bcprov, bcpkix, bctls, bcpg, bcmail and the bc-fips family) across build manifests, container images and mobile packages for versions below 1.85 / BC-LTS 2.73.12 / the per-module FIPS fixed builds, and upgrade — Bouncy Castle is usually a transitive dependency, so an application inventory will miss it where a dependency tree will not."
  - "Where an upgrade cannot land this week on a JSSE client that terminates TLS against untrusted or partner networks, set the Bouncy Castle JSSE hostname CN-fallback property explicitly to false — it is the documented mitigation for CVE-2026-59638 and the code has shipped with the fallback on since 1.61 in every deployment that never set it."
migrated_from: null
---

Bouncy Castle for Java 1.85 and 1.85.1 shipped on 2026-07-12, and the write-ups describing what those releases fixed only became public on 2026-08-03, when the maintainer published a per-flaw page for each of the 32 identifiers ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059638)). The project's official release notes carry the authoritative id-to-flaw list, and its own one-line summaries are the safest binding to work from ([Legion of the Bouncy Castle, 2026-08-03](https://raw.githubusercontent.com/bcgit/bc-java/main/docs/releasenotes.html)). Nothing in the batch is reported exploited and no proof-of-concept is public, but the disclosure clears the out-of-band bar on its own mechanics rather than on exploitation: the fixed binaries have been available for three weeks, the fix commits are linked from each write-up, and the root-cause detail is now specific enough — class, method and the exact comparison that goes wrong — that reconstruction is a reading exercise for anyone who wants one, while any estate still on an older release remains exactly as exposed as it was.

Four flaws carry the batch's highest severity rating — the per-CVE scores are in this entry's CVE metadata — and they are not variations on one bug. Three attack certificate-chain validation, each removing a different guarantee; the fourth is not a certificate flaw at all but a key-recovery bug in a Diffie-Hellman agreement, and it is grouped here only by severity. In CVE-2026-58062 the JCA revocation checker accepts a stapled OCSP response that was never bound to the certificate being checked, so a validly-signed "good" response covering some other certificate is treated as proof the end-entity is unrevoked instead of being rejected in favour of a CRL fallback ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9058062)). CVE-2026-59638 is a default-configuration inversion: `HostnameUtil` gates the legacy 'match CN when no dNSName SAN exists' fallback (the maintainer's own phrasing) on a two-argument property lookup that returns the caller-supplied default of `true` when the property is unset, and as the maintainer puts it, "The javadoc for the property says the unset default must DISABLE the fallback, but the code ships with it active in every deployment that doesn't explicitly set the property to false" — an issue present since 1.61 ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059638)). Because RFC 5280 name constraints only bind SAN entries of the constrained type, a leaf certificate carrying no dNSName SAN passes a dNSName-constrained chain and is then matched on its attacker-chosen CN. The odd one out is CVE-2026-59650, which involves no certificate, chain or PKIX code path: it is a missing peer-value check in the MTI/A0 two-pass Diffie-Hellman agreement, which exponentiates the raw wire value with no range or subgroup-membership test: the write-up states that "each exchange leaks x mod r for some small prime r; combining these via CRT recovers the full static private key" — the classical small-subgroup confinement attack, against a static key ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059650)). CVE-2026-8763 is an inconsistency in `PKIXNameConstraintValidator`, which strips trailing dots before comparing dNSName constraints but compares rfc822Name and URI hosts with a bare case-insensitive equality, so a trailing dot slips an excluded name past the check and "An attacker who controls a name-constrained intermediate CA can issue certificates for email/URI hosts that the constraints were meant to exclude" ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%908763)).

The rest of the batch matters less individually and more as patch-scope. Around fourteen more are integrity and authenticity bypasses in the CMS, S/MIME, OpenPGP and AEAD code paths — among them a CMS signature check that returns success for signed data carrying no signers at all (CVE-2026-59639), an RSA PKCS#1 verification path that skips the last two hash bytes when the DigestInfo NULL is omitted (CVE-2026-12860), an S/MIME validator that trusts a signer-asserted signing time for path validation (CVE-2026-59641), and CCM-family modes that write plaintext into the caller's buffer before the tag is checked (CVE-2026-58061). The remainder are resource-exhaustion defects where an attacker-supplied file or message dictates allocation or work factor: unbounded KDF cost when loading BCFKS, PKCS#12 and PKCS#8 material, quadratic-time X.500 name stringification, an unbounded HSS public-key level count, and a DTLS reassembler sizing a buffer from an unchecked 24-bit length. All 32 are fixed in 1.85, and most — though not all — also in BC-LTS 2.73.12; four of the batch never affected BC-LTS, which this entry's CVE metadata records per identifier. The FIPS modules carry their own per-module fixed builds, and there are at least three families rather than one: bc-fips 1.0.2.7, 2.0.2 and 2.1.3 for the provider flaws ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%908763)), bctls-fips 1.0.24, 2.0.24 and 2.1.24 for the JSSE hostname issue ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059638)), and bcpg-fips 2.0.13 for at least one of the OpenPGP flaws ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059643)). A FIPS estate has to resolve its exposure per module, not per product.

Detection here is an inventory problem before it is a telemetry one, because Bouncy Castle is overwhelmingly a transitive dependency: the first sweep is software-composition analysis over build manifests, container images and mobile packages for org.bouncycastle artifacts below the fixed versions, not a search for an application named "Bouncy Castle". Where a runtime check is warranted, the observable classes follow the mechanics — in OCSP responder logs, a response whose subject or serial does not correspond to the certificate that was actually being validated, where a CRL fallback should have fired instead; in TLS session telemetry from JSSE clients, peers accepted against a certificate with no dNSName SAN whose CN merely matches the target hostname. Discriminating the benign case is largely a matter of where the client terminates: a Bouncy Castle JSSE client talking to a pinned internal endpoint on a trusted segment produces the same telemetry with none of the risk, while the same client terminating against partner networks, VPN concentrators or any on-path-capable segment is where a forged chain would actually be presented. Two interim levers exist before a full upgrade: setting the JSSE hostname CN-fallback property explicitly to `false`, which is the control the maintainer names for CVE-2026-59638 ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059638)), and the strict-DigestInfo property the release notes expose as `org.bouncycastle.pkcs1.strict_digestinfo` for CVE-2026-12860 ([Legion of the Bouncy Castle, 2026-08-03](https://raw.githubusercontent.com/bcgit/bc-java/main/docs/releasenotes.html)). The OCSP-binding, Diffie-Hellman and name-constraint flaws have no configuration toggle and require the version bump.

One note on reading the maintainer's own advisory index, because it moved during the course of this reporting: the page filed under the CVE-2026-58062 slug initially displayed the write-up for CVE-2026-58063, the unrelated and much less severe keystore issue, rather than the OCSP-binding flaw. The maintainer has since corrected it, and both pages now show their own content — checked again immediately before publication ([Legion of the Bouncy Castle, 2026-08-03](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9058062)). It is recorded here only because anyone who triaged this batch from that index in its first hours would have read the most serious flaw in it as a denial-of-service bug, and may want to re-check what they concluded.

**Defender takeaway:** the operative question is not whether you run Bouncy Castle but whether you can answer where it is embedded — as a JSSE provider, a PKIX validator, or a CMS/OpenPGP implementation inside an application or appliance you did not build. Anyone who took the 1.85 release on 12 July already closed all 32 issues before today's detail existed; anyone who did not is now three weeks behind a public root-cause description of three independent ways to make a certificate chain validate when it should not, and of a fourth flaw that recovers a static Diffie-Hellman private key outright.
