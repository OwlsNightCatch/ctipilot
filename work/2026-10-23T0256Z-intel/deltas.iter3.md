# Prior-iteration (2) findings and the remediation applied — verify each in iteration 3

| # | code | entry | remediation_applied |
|---|---|---|---|
| 1 | F3 | publica-pk-softech… body paragraph 1 | "of Reinach (BL)" removed |
| 2 | F14 | publica-pk-softech… 2026-10-23 section | "the first reported statement by an authority" → "a reported confirmation of the actor by an authority" |
| 3 | F3 | pan-os-panorama-php2shell… body and Detection | three conditions as the advisory lists them (dataplane routing, replaced inbound-management certificate, threat prevention enabled); the "decrypted" clause and "four conditions" removed |
| 4 | F3 | fortinet-fortisandbox-fortisiem… takeaway, actions[0] | only the FortiSIEM tcp 27918 workaround is attributed to Fortinet; the FortiSandbox GUI precaution is labelled as the usual precaution, not a Fortinet instruction; the action says "as Fortinet's workaround says" |
| 5 | F4 | blackx… cves[CVE-2023-24932] | status is now [patch-available] (no `exploited`) |
| 6 | F4 | run record | entries_dropped_by_verification is 1; `completed` re-stamped at 04:55:04Z, after the FortiSandbox entry's discovered_at; it is re-stamped again at the end of the run |
| 7 | F9 | publica-pk-softech… main analysis | sentences dated ("as of 2026-10-20 … had not confirmed", "as of 2026-10-21 no authority had confirmed"); summary reads "As of 2026-10-22 neither the Confederation nor Publica has itself named the actor or the demand" |
| 8 | F9 | cve-2026-114625-arista… | body now says the CSAF describes the flaw as "VeloCloud Orchestrator Remote Code Execution (VCO RCE)" while the advisory page names an SQL injection, and that Arista does not relate the two |
| 9 | F8 | emudhra… cves[].fixed and Update section | the tracker's fixed Java builds added to cves[].fixed and to the section, with the note that the tracker's 8u511 as fixed sits against Oracle's 8u511 as affected, unreconciled |
| 10 | F11 | fortinet-hardening…, fortinet-fortisandbox-fortisiem… | "the store covers in the earlier entry linked from this one" removed; the FortiSandbox overlap now cites Help Net Security (three June CVEs exploited) and Fortinet PSIRT FG-IR-26-141 (CVE-2026-25089 fixed in 5.0.6 / 4.4.9, now in sources[]) |
| 11 | F11 | emudhra… Update section | trimmed to the delta (Java affected/fixed builds, Web Start note, NCSC.ch status); the duplicated alternatives paragraph removed |
| 12 | F11 | publica-pk-softech… | "available to cite" replaced in summary, sourcing_note, section and record summary; headline now "apparently kept" |
| 13 | F11 | pan-os-panorama-php2shell… headline | "hits" → "affects" |
