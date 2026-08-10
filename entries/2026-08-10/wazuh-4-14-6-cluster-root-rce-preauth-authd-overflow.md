---
schema: 1
kind: vulnerability
horizon: operational
title: "Wazuh 4.14.6 — two cluster-protocol paths to root that bypass the CVE-2026-25770 fix, a DAPI deserialization RCE, and a pre-auth stack overflow on the enrollment port"
headline: "Wazuh patches root-RCE chains in the cluster protocol and a pre-auth overflow reachable on TCP/1515 under stock defaults"
summary: >
  Wazuh 4.14.6 fixes a ten-CVE cluster disclosed as individual GitHub Security Advisories and
  independently cross-listed by BSI. Two critical flaws (CVE-2026-49441, CVE-2026-48024) let a
  cluster peer holding the shared Fernet key overwrite arbitrary files on the master — including
  ossec.conf, reaching root — through two sibling code paths that both defeat the _ALLOWED_PREFIXES
  hardening added for CVE-2026-25770; CVE-2026-44901 reaches root code execution when a REST request
  fans out across two or more nodes; and CVE-2026-45798 is a pre-authentication stack overflow in
  wazuh-authd on TCP/1515, reachable with no credential under the shipped anonymous-SSL default.
  Affected ranges differ per flaw — from 4.0.0, 4.3.0 or 4.5.0 respectively through 4.14.5 — and all are fixed in 4.14.6, with no exploitation reported.
discovered_at: "2026-08-10T04:40:00Z"
event_date: "2026-08-06"
run_id: 2026-08-10T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, priv-esc, patch-available, default-config]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1210, T1190, T1068]
affected_products: ["Wazuh", "Wazuh manager"]
cves:
  - id: CVE-2026-49441
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: ">= 4.3.0, <= 4.14.5"
    fixed: "4.14.6"
  - id: CVE-2026-48024
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: ">= 4.0.0, <= 4.14.5"
    fixed: "4.14.6"
  - id: CVE-2026-44901
    cvss: "8.4"
    epss: null
    type: deserialization
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: ">= 4.0.0, <= 4.14.5"
    fixed: "4.14.6"
  - id: CVE-2026-45798
    cvss: "7.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 4.5.0, <= 4.14.5"
    fixed: "4.14.6"
sources:
  - url: "https://github.com/wazuh/wazuh/security/advisories/GHSA-3v57-hgvj-3vj2"
    publisher: "Wazuh (GitHub Security Advisory)"
    date: "2026-08-07"
    role: primary
  - url: "https://github.com/wazuh/wazuh/security/advisories/GHSA-gh4h-fx78-q8xc"
    publisher: "Wazuh (GitHub Security Advisory)"
    date: "2026-08-06"
    role: primary
  - url: "https://github.com/wazuh/wazuh/security/advisories/GHSA-8c6v-7g3w-prrq"
    publisher: "Wazuh (GitHub Security Advisory)"
    date: "2026-08-06"
    role: primary
  - url: "https://github.com/wazuh/wazuh/security/advisories/GHSA-4fvp-jfc3-qr6r"
    publisher: "Wazuh (GitHub Security Advisory)"
    date: "2026-08-06"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2699"
    publisher: "BSI CERT-Bund"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A cluster peer holding the shared Fernet key can write arbitrary files anywhere the wazuh user has write access on the master, including /var/ossec/etc/ossec.conf."
    publisher: "Wazuh (GitHub Security Advisory)"
  - quote: "The function is reachable pre-authentication via the V: field of an enrollment message sent to wazuh-authd on TCP/1515 over anonymous SSL (default configuration: use_password=no, ssl_verify_host=no)."
    publisher: "Wazuh (GitHub Security Advisory)"
  - quote: "A compromised worker can set sort_casting=[\"exec\"] and embed a Python payload inside affected_items. When the master merges responses from two or more nodes, it calls : exec(<payload>) as root."
    publisher: "Wazuh (GitHub Security Advisory)"
verification: multi-source
sourcing_note: >
  Each CVE identifier was read directly off its own GitHub Security Advisory record rather than
  paired by position against a multi-flaw list, then cross-checked against BSI's independently
  published WID-SEC-2026-2699, which names the identical identifiers for the same release. None of
  the four had propagated to NVD or MITRE when this entry was composed, so the vendor's per-advisory
  record plus the national-CERT cross-listing is the strongest available provenance. Credibility is
  assessed at 2 rather than 1 because BSI restates the vendor's own advisory data — one assessor
  with two publishers, not two independent assessments. The pre-authentication overflow's advisory
  is narrower than the others in two respects carried here: its affected range begins at 4.5.0, and
  it records the flaw as verified against a 5.0.0 beta with the reachability path not separately
  verified for the 4.x line in that submission.
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
  - "Upgrade every Wazuh manager to 4.14.6 — the pre-auth overflow in wazuh-authd needs no credential and no cluster membership, so an internet-reachable or untrusted-segment enrollment port on TCP/1515 is exposed under the shipped anonymous-SSL default."
migrated_from: null
---

Wazuh — the open-source SIEM and XDR platform many public-sector SOCs run themselves — shipped 4.14.6 on 2026-08-06 and 2026-08-07 with ten CVEs, each disclosed as its own advisory, and BSI CERT-Bund independently cross-listed the same identifiers for the same release ([BSI CERT-Bund, 2026-08-06](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2699)). Four carry the operational weight, and two of them matter beyond their scores because they defeat a fix the project already shipped.

CVE-2026-49441 and CVE-2026-48024 are both arbitrary-file-write-to-root primitives in the cluster protocol's master-side file-receive path, and both reach it through sibling code paths that the `_ALLOWED_PREFIXES` hardening added for CVE-2026-25770 in 4.14.3 does not cover — one through the non-merged branch's unchecked mapping of a peer-supplied key to a destination path, the other through peer-controlled path traversal in the merged-file header line ([Wazuh, 2026-08-07](https://github.com/wazuh/wazuh/security/advisories/GHSA-3v57-hgvj-3vj2), [Wazuh, 2026-08-06](https://github.com/wazuh/wazuh/security/advisories/GHSA-gh4h-fx78-q8xc)). Either lets a peer holding the shared Fernet key overwrite `ossec.conf` and reach root by way of the next `wazuh-logcollector` reload. CVE-2026-44901 is a deserialization flaw in the distributed API's response-merging function: a compromised worker sets `sort_casting` to a builtin name that is never allowlisted, and the master resolves and calls it as root — but only when a REST request fans out across two or more nodes, which is the precondition worth remembering during triage ([Wazuh, 2026-08-06](https://github.com/wazuh/wazuh/security/advisories/GHSA-8c6v-7g3w-prrq)).

CVE-2026-45798 is the one reachable by anyone. A fixed-size copy in the version-comparison helper never NUL-terminates a maximum-length input, and the out-of-bounds scans that follow crash the daemon; the function sits behind the `V:` field of an enrollment message to `wazuh-authd` on TCP/1515, and Wazuh states plainly that the shipped defaults require no credential to get there ([Wazuh, 2026-08-06](https://github.com/wazuh/wazuh/security/advisories/GHSA-4fvp-jfc3-qr6r)). Every flaw here is researcher-reported with no exploitation claimed by any party.

Detection, telemetry class first. The cluster wire protocol is rarely visible to conventional network inspection, so the durable anchor for the file-write pair is file-integrity state on `ossec.conf` — an unexpected content or timestamp change followed by a `wazuh-logcollector` restart is the sequence, not either event alone. For the distributed-API flaw, process-creation telemetry showing the manager's own API or cluster daemon as the parent of a shell or interpreter is anomalous on a healthy cluster, and the necessary condition is a REST request naming more than one node. For the enrollment overflow, repeated short-lived connections to the enrollment port followed by daemon restarts is the crash signature. **Triage:** legitimate cluster synchronisation writes constantly into each peer's own queue subtree, so file writes by the manager are normal — the discriminator is a write landing *outside* that subtree, in the configuration directory. **Defender takeaway:** none of the file-write or deserialization paths is reachable without holding or spoofing the cluster key, so key hygiene and putting cluster traffic on a segment no untrusted host can reach contains three of the four; the enrollment overflow is the one that does not care, and it is the reason the upgrade is not schedulable around.
