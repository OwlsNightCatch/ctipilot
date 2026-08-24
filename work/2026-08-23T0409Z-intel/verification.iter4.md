**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-23T06:22:15Z · ended_at=2026-08-23T06:23:54Z · duration_seconds=99

## Verification report — 2026-08-23T0409Z-intel (iteration 4, alt/delta-focused, time-boxed)

Per the spawn instructions this iteration verified the thirteen prior-iteration (iteration 3, Opus) deltas against current entry text and, where time allowed, against saved source text/spot-checked facts. No new findings were raised.

### Delta verification (all thirteen, iteration 3 → this iteration)

- **F1 (blockchain-dead-drop, mis-credited naming/dating):** RESOLVED and source-confirmed. Body now reads "which Red Canary calls EtherHiding and dates to first reporting in 2023," which is a verbatim match to `body.redcanary.txt` line 380: "First reported in 2023, EtherHiding uses blockchain infrastructure…" — no organisation is credited with coining the name, matching the fix. Further cross-check: the source's "EtherHiding" section lists three top-10 users (ClearFake, Phexia, EtherRAT) separately from its "dead drop resolution" section's three users (Phexia, CastleRAT, EtherRAT); the entry's claim "three of four new entrants… two of those three read it from a public blockchain" (Phexia + EtherRAT, with CastleRAT resolving via steamcommunity.com/domains) and the closing sentence "three of its top ten using it this month, two of them new arrivals" both reconcile exactly against the source's two distinct three-item lists. No regression.
- **F2 (payload-zurich, "eight" vs "seven other" customers):** RESOLVED. Title now reads "…names seven other Swiss customers alongside it"; body states "the school's among them, alongside seven other organisations" and "The affected customer set is seven organisations plus one higher-education institution" — internally consistent.
- **F3 (payload-zurich, unsupported "Zurich area" location):** RESOLVED. Provider is now referred to only as "a Swiss data-centre operator" / "Swiss customers"; no remaining geographic qualifier finer than country for the provider (the "Zurich business school" reference is to HWZ itself, which is correctly named as a Zurich institution, not the provider).
- **F4 (spectre-uat-10147, wrong CVSS-score provenance in sourcing_note):** RESOLVED. Sourcing note now reads: "Neither score comes from Cisco Talos… the two have different provenance: the Dell flaw's score is its own CNA record's, while the MSI flaw's CNA record carries no metrics at all, so its score is the national vulnerability database's analyst assessment."
- **F5 (gtig-russia, "silently" overstatement):** RESOLVED. Summary now reads "…a fake voice call on the same page captures microphone and camera through the browser under cover of the call" (no "silently" claim), consistent with the body's existing "the call is presented as having failed" framing.
- **F6 (uat-10147-agentic, "update" vs "start" routine):** RESOLVED and source-confirmed. Body now reads "…a deceptive scheduled task named after a browser start routine." `talos-agentic-text.txt` states the actor creates "deceptive scheduled tasks named 'Google Chrome Start'" — exact match.
- **F7 (run record, backfill sweep count 3 vs 4):** RESOLVED. Run record now states "four of this run's eleven entries came from that sweep, including the deep dive" (S3 telemetry note and § "The wide gap changed how the research was tasked" both say four, deep dive named).
- **F8 (payload-zurich, unsupported sector list):** RESOLVED. Body now reads "The listing gives only domain names; no cited source describes what those other customers do, and this entry does not guess."
- **F9 (gtig-russia headline, "satisfied rather than bypassed" contradiction):** RESOLVED. Headline now reads "No exploit and no payload — the victim approves the attacker's session, or issues a credential the second factor never sees," which covers both the device-code/WhatsApp "satisfied" cases and the app-password "bypassed entirely" case, consistent with the action item on disabling application-specific passwords.
- **F10 (trueconf, unnamed malware keys + unsupported name-to-implant mapping):** RESOLVED. Body now names both PhantomHook and PhantomReact explicitly and states "no source states which name belongs to which implant, so this entry does not assert the mapping."
- **F11 (uat-10147-agentic, missing scheduled-task technique id):** RESOLVED. `techniques:` now includes T1053.005 (Scheduled Task/Job: Scheduled Task), matching the body's described behaviour.
- **F12 (trueconf, systemd-persistence id with no body clause):** RESOLVED. Body now states artefacts "show both persisting as systemd units under attacker-chosen service names, which is the *nix counterpart to the Windows service persistence above," giving T1543.002 a body basis.
- **F13 (martigny-combe, "notified" vs "in progress" police complaint):** RESOLVED. Summary and body both now read "a criminal complaint with the cantonal police in progress" / "was recorded as in progress rather than filed," distinct from the federal/cantonal notifications, matching the commune's own communiqué distinction.

### Spot checks performed (time-boxed, beyond the thirteen deltas)

- Run record calibration line "Five entries at high, six at notable, none critical" — counted directly from all 11 entry frontmatter `priority:` fields: 5× high (btr-sys, gtig-russia, rust-crates, spectre-uat-10147, trueconf), 6× notable (blockchain-dead-drop, cve-2026-69836, martigny-combe, misp-stix, payload-zurich, uat-10147-agentic), 0× critical. Matches exactly.
- Run record "Twelve actions ship across nine entries; two carry none, both incident items" — counted `actions[]` list items per entry: totals to 12 across 9 non-empty entries; the two empty (`martigny-combe`, `payload-zurich`) are both `kind: incident`. Matches exactly.

No regressions were introduced by any of the thirteen remediations, and no new truth or editorial defects were identified in the scope reviewed under this iteration's time box.

### Verdict

CLEAN

### Findings summary (machine-readable)

```yaml
[]
```
