# Iteration 5 findings and remediation applied (verify each before the cold pass)

- F3 Barracuda main analysis (2026-11-04/...): "marks both for forensic triage" is now cited to the CISA KEV JSON feed (the alert page does not carry it); the listing date keeps the alert citation.
- F4 Adobe Connect (2026-11-11/adobe-connect-...): every "on-premises" statement and the "bulletin does not cover the hosted service" statement removed (title, headline, summary, actions[0], body, Exposure); the entry now says Adobe Connect on Windows 12.12 and earlier, as the bulletin lists; entities now links product:adobe-connect.
- F11 kernel sourcing_note: stray "; The" fixed.
- F11 Fortinet 2026-11-11 section: states that FG-IR-26-275 lists lower minimum FortiManager builds (8.0.1, 7.6.8, 7.4.6, 7.2.9) beside the October builds.
- Declined (advisory): linking registry keys on the Vates and Chrome entries; product:xen-orchestra-appliance and product:google-chrome would overlap other entries of the 14-day window and raise the dedup entity-overlap warning, and the zero-warning rule takes precedence; the affected_products[] still name the products. Implant/registry/file names in GhostFrame, CopperDragon and Turla prose remain the declared exception.
