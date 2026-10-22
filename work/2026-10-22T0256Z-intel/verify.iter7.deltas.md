# Prior-iteration deltas (iteration 6 NEEDS_FIXES → iteration 7 post-fix pass)

| finding | entry | remediation applied | verify in this iteration |
|---|---|---|---|
| F3 Publica update section: "Tages-Anzeiger published on 2026-10-20" cited to Netzwoche only | publica-pk-softech-supplier-malware-intrusion-data-outflow | Tages-Anzeiger citation added to the clause | citation |
| F11 Publica summary flattened BPK's "must be assumed" | same | summary: Pensionskasse Post says data left, Bernische Pensionskasse says it must be assumed so | wording |
| F8 k0t private-data-encryption caveat lacked the fix versions | k0t-fortiweb-fortigate-globalprotect-edge-device-campaign | caveat now ends "until FortiManager 6.2.7 and FortiGate 6.2.6, 6.4.4 or 6.6.0 and later" (FG-IR-19-007); to stay within the word limit the "then opens an OpenConnect VPN session" clause was cut (OpenConnect persistence stays in the next paragraph) | against FG-IR-19-007 |
| F8 ConnectWise: later advisory updates unused | connectwise-cloud-backup-skykick-m365-app-credential-abuse | read the archived copy of the Trust Center page (bodies/cw-wayback.txt); update section now carries ConnectWise's own statement (2026-10-21 22:00 UTC) that it appears a China state-aligned group was responsible using an openly available agentic AI framework, the start of controlled restoration on 2026-10-21 (12:45 UTC), the "several days" and keep-connections-disabled instructions, and the twice-daily updates from 2026-10-22; heise kept as a second source for restoration; record summary, sourcing_note, sources[] date (2026-10-21) and the run-record fetch-failure mitigation line updated; the record's `fields` still equal the diff | each new clause against the archived page; the canonical URL is cited because the live page is walled |
| F11 LiteLLM "look-alike health-check endpoint" | litellm-1-107-0-pypi-docker-credential-stealer-lookalike | now "an encrypted archive posted to a path labelled as a health check" (Socket: "Despite the URL's health-check wording") | wording |

Declined again: OVH envchecker folder and extension name (advisory); GitLab priority (iteration 6 called notable borderline but made no finding).
