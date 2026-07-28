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

## A displayed CVSS score may be the temporal one — check the vector before calling it a discrepancy

**2026-07-28 (run 2026-07-28T0409Z-intel), FortiOS CVE-2025-68686.** The FortiGuard advisory
page displays "CVSSv3 Score 5.3" while the CNA record Fortinet submitted carries 5.9. Composition
wrote this up as an inconsistency *inside Fortinet's own records* and picked the vendor page's
figure. It is not a discrepancy at all: the 5.3 on the page **hyperlinks to the vector**
`AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N/E:P/RL:O/RC:C` — the same base vector with **temporal
metrics appended**. 5.9 base × 0.94 (E:P) × 0.95 (RL:O) × 1.0 (RC:C) = 5.269 → 5.3. Three
verifier iterations re-derived the arithmetic independently before it was settled.

Two rules from this:

1. **Before reporting two scores as contradictory, look at the vector each one is attached to.**
   A vendor page that renders a bare number often links the calculator URL; `E:`, `RL:` and `RC:`
   in that vector mean you are looking at a temporal score, not a competing base score.
2. **`cves[].cvss` carries the BASE score.** Every other record in the store does, so a temporal
   figure silently corrupts cross-entry comparison, the `/cve/` pages and any automated consumer.
   Put the temporal figure in `sourcing_note` so a reader who sees it on the vendor page can
   reconcile the two, and say which is which.
