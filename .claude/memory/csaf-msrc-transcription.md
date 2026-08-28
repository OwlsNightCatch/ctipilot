---
name: CSAF / MSRC / CVE-record transcription
description: Read affected/fixed/score facts from structured fields, not prose; the verdict field is the claim, membership in a list is not
type: feedback
---

# Vulnerability-record transcription rules

Read `affected`/`fixed`/patch-timing from **structured** fields, never the human-readable summary (3 of 7 verifier findings on 2026-07-15 were this one root cause):

- **CSAF:** `vulnerabilities[].product_status.{known_affected, fixed, known_not_affected, under_investigation}` (a naïve product-tree walk conflates affected and fixed) and `remediations[].category == vendor_fix` (the real patch — "Recommended Practices" is boilerplate; never conclude "no fix" without checking `remediations`).
- **MSRC** (`msrc cve <id>`): `vectorString`, `exploited`, `revisions[]` — a July-dated CVE can carry a June patch ("inadvertently left out of Patch Tuesday").
- **Red Hat hydra** (`securitydata/cve/<id>.json`): `package_state[]` lists every product ASSESSED; the row's `fix_state` is the verdict (`Affected` / `Not affected` / `Will not fix` / …). Reading membership without the verdict inverts the finding (2026-08-19 Keycloak: "Not affected" shipped as "Affected with no fix"). **In every format the enumeration is the scope of assessment and a sibling field is the verdict — transcribe the verdict.**
- **CVE record** (`url https://cveawg.mitre.org/api/cve/<id>`): `containers.cna.metrics` is the CNA's own scoring; `containers.adp[].metrics` is downstream (usually CISA-ADP); NVD's "Primary" nvd@nist.gov score is a third party. `cna.metrics: null` + ADP score present = the CNA never scored it. A discloser's "CNA score" column may not be the CNA's — spot-check outliers.

## CVSS score rules

- `cves[].cvss` carries the **BASE** score. A displayed vendor score may be the TEMPORAL one — check the linked vector for `E:`/`RL:`/`RC:` before calling two scores contradictory.
- A CNA publishing CVSS 4.0 AND 3.1 side by side is parallel metrics, not a self-correction — read every element of `cna.metrics`.
- Never rank scores across CVSS versions. When multiple legitimate figures exist, the number goes in `cves[].cvss` and the reconciliation (which body, which scale) in `sourcing_note`.
- OSV 404s on ecosystem-less products (Joomla extensions, firmware) are not unreachability — the CVE API has no ecosystem requirement.
