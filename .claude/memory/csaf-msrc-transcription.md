---
name: CSAF / MSRC structured-field transcription
description: When composing ICS or Microsoft vulnerability entries, read affected/fixed status from the structured product_status / remediations / revision fields, not the human-readable summary
type: feedback
---

# CSAF / MSRC vulnerability-field transcription

**2026-07-15 (run 2026-07-15T0409Z-intel):** three of the seven verifier findings on a
data-heavy CISA-ICS + Microsoft-Patch-Tuesday run were the *same* root-cause defect —
reading vulnerability facts from the human-readable summary instead of the structured
machine fields. The cold-reader loop caught all three (over iterations 1, 2 and 4);
none is subtle, all are avoidable at compose time.

## The failures and the fix

1. **Affected vs fixed versions live in `product_status`, not the product-name list.**
   The CISA CSAF JSON (`tools/fetch_source.py cisa csaf <icsa-id>`) product tree lists
   *both* affected and fixed product versions. A naïve walk that collects every
   `product.name` conflates them. **ABB T-MAC Plus:** `known_affected` = 4.0-24,
   `fixed` = 4.0-25 — I listed both as affected. Always read
   `vulnerabilities[].product_status.{known_affected, fixed, first_fixed, known_not_affected}`
   and map each product_id back to its name.

2. **The vendor fix lives in `remediations`, not the "Recommended Practices" notes.**
   For **Rockwell CVE-2026-10577** I read only the generic network-isolation guidance in
   the `notes` block and wrote "no fix — network isolation only." The actual fix
   (firmware **3.011**) was in `vulnerabilities[].remediations[]` with
   `category: vendor_fix`. A CISA ICS advisory's "Recommended Practices" is boilerplate
   mitigation; the real remediation is the `remediations` array. Never conclude "no fix"
   without checking it.

3. **MSRC fix timing can predate the CVE's July release — read the revision history.**
   **CVE-2026-58644** (SharePoint) was documented on 2026-07-14 but its
   `revisions` note said "The Patch for this issue was released but the CVE was
   inadvertently left out of the Patch Tuesday June 2026 release" — the patch shipped
   with the **June** cumulative update. A July-dated CVE record does not guarantee a July
   patch. Check `msrc cve <id>` -> `revisions[]` before stating a `fixed:` release.

## Rule of thumb

When composing an entry from CSAF or MSRC OData, the `affected` / `fixed` / patch-timing
facts come from the **structured** fields:
- CSAF: `product_status`, `remediations[].category == vendor_fix`, plus per-CVE `scores`.
- MSRC OData (`msrc cve <id>`): `vectorString`, `exploited`, `latestSoftwareRelease`
  (exploitability), and `revisions[]` for late/moved patches.
The prose summary and "Recommended Practices" are for readability, not ground truth.
Extract-and-drop still applies, but extract from the right key.
