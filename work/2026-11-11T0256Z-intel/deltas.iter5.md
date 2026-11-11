# Iteration 4 findings and remediation applied (verify each before the cold pass)

- F3 Fortinet Defender takeaway (2026-10-23/fortinet-...): the FGFM-port advice is now a separate clause cited to FG-IR-26-275; the CISO blog citation covers only "keep FortiManager administration off the internet" and MFA. Detection: "IBE webmail endpoints" (no "administrative endpoints") and "FGFM connections from unexpected sources" (no "device serials").
- F14 N-able Exposure: "a compromised server can reach large numbers of the systems N-central manages" (Field Effect's wording).
- F14 Danfoss 2026-11-11 section: the claim that the BACS warning is its "first" is removed; it now says the warning repeats the earlier Cyber Security Hub advisory.
- F9 kernel sourcing_note: now says Sophos's advisory gives Red Hat's rating as 5.9 against Red Hat's own page (record declares `sourcing_note`).
- F11 CopperDragon: stray "; A second route" fixed. Residual implant/registry/file names in GhostFrame, CopperDragon and Turla prose stay as a conscious exception (vendor-published behaviour descriptors and Triage discriminators; Detection lines and actions describe behaviour).
