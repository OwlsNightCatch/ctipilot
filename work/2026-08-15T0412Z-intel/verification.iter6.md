**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-15T06:43:39Z · ended_at=2026-08-15T06:48:22Z · duration_seconds=283

## Verification report — 2026-08-15T0412Z-intel (iteration 6)

Scope of this pass, per the spawn instructions: verify the eight iteration-5 fixes (F1–F5, F8–F10 in the run record's `n:5` block) and confirm the two missed-angle dispositions are honestly recorded, rather than opening new research lines. I additionally spot-checked the FortiWeb entry's CVE data against Fortinet's own CSAF JSON (all four advisories, fetched directly this iteration) since that entry has been the subject of four consecutive correction rounds, and swept all 14 new entries for nexus/China-attribution language and workflow-internal wording as a fast completeness check.

**Result: seven of the eight listed fixes verified correct. One (F1, mustang-panda nexus) did not fully land — the claim in its own remediation record ("no nexus claim remains anywhere in the entry or its registry record") is false, and I can quote the surviving instance.**

### Unsupported / hallucinated facts

**F1.** Entry: `entities/registry.yaml`, record `malware:plugx` (added this run — `first_seen: 2026-08-15`, cited only to "Kaspersky Securelist, 2026-08-14" via `entities_added` in the run record and via the `mustang-panda-coolclient-signed-kernel-driver-rootkit` entry's `entities[]`).

The record's `nexus:` field is correctly `null` (verified — line 4843 of registry.yaml), and the `mustang-panda-coolclient-…` entry itself is clean (no China/nexus language anywhere in its frontmatter, body, or sourcing_note — grepped directly). But the registry summary text for `malware:plugx` still reads:

> "Long-running remote-access implant used by multiple China-nexus espionage groups. In the Mustang Panda intrusions Kaspersky documented in August 2026 it serves as the initial post-compromise implant, deployed before the group transitions to its CoolClient secondary backdoor (Kaspersky Securelist, 2026-08-14)."

The first sentence carries no citation of its own — the trailing `(Kaspersky Securelist, 2026-08-14)` attaches to the second sentence only, and Kaspersky's own analysis (which I re-read this iteration) explicitly declines to state a nexus: the entry's own `sourcing_note` says "neither cited source states a national nexus, so none is asserted... Kaspersky describes an espionage group operating across Asia and Russia, notes Chinese-language strings in the developer's build path, and says its own open-source checks could not tie those strings to any known organisation." Nothing in this run's sourcing supports "China-nexus" as a fact about PlugX's user base.

This directly contradicts iteration 5's own remediation claim for F1: `remediation_applied: "removed; no nexus claim now appears in the entry or its registry record"` (run record line 235). The registry record is exactly "its registry record" (added by, and only by, this run's `malware:plugx` addition) and the nexus claim is still there, unsourced. Iteration 3's original F4 finding on this same defect class ("a China nexus was asserted in the summary and tagged, though neither cited source states one") was fixed on the actor and the entry, but the same defect resurfaced one hop over, on the co-added malware record, and the two subsequent verification passes (iterations 4 and 5) did not catch it because neither read the registry.yaml diff, only the entry file.

Fix: strip "used by multiple China-nexus espionage groups" (or attribute it to a source that is actually cited somewhere in this run's sourcing, if one exists) from the `malware:plugx` summary, consistent with how `actor:mustang-panda`, `malware:coolclient`, and `malware:toneshell` were already handled.

### Confirmed correct (no further action)

- **F2** (fortiweb actions[] upgrade targets) — `actions[]` now reads "8.0.3, 7.6.7 or 7.4.12" with the Wildcard-disable config change named as the whole remediation on 7.2/7.0; no reference to the unreleased 7.2.13/7.0.13 remains in the action text. Confirmed against Fortinet's own CSAF (`FG-IR-26-158.json`, fetched directly this iteration): `known_not_affected` lists `FortiWeb-8.0.3`, `FortiWeb-7.6.7`, `FortiWeb-7.4.12` as released and `FortiWeb-upcoming 7.2.13` / `FortiWeb-upcoming 7.0.13` as upcoming — the entry's affected/fixed strings and the action match the structured record exactly.
- **F3** (trivy evidence[] record 2) — now reads "March 19, 2026 (~17:43 UTC): The attacker force-pushed 76 of 77 version tags…" with no inserted "On"; a contiguous quote.
- **F4** (trivy LiteLLM citation date) — frontmatter and inline citation both now read 2026-03-24; fetched `docs.litellm.ai/blog/security-update-march-2026` directly this iteration, `article:published_time` = `2026-03-24T14:00:00.000Z`. Matches. (Also re-checked the CERT-EU and Docker dates in the same entry, which iteration 4 had corrected: Docker `datePublished` = `2026-03-23T16:25:14-07:00`, CERT-EU dateline = "Thursday, April 02, 2026 03:15:00 PM CEST" — both match the entry's frontmatter exactly.)
- **F5** (france-dgfip retained-access clause) — now cited to The Register, not the ministry statement. Fetched the Register article directly this iteration: its own dek is "Government disputes claims of continued access as investigators measure damage" and the article states DGFiP disputed the retained-access claim and separately carries the 2-million-record and MFA-bypass claims — all three now attributed correctly in the entry body.
- **F8** (run record wording) — swept the published run-record notes for "sub-agent", "Phase N", "spawn", "main agent"; the only literal hits are inside the machine-readable `findings:` YAML block (which is expected/normal — that block documents the verification loop's own mechanics and isn't prose the reader parses as pipeline narrative) and one telemetry `error_message` field ("unavailable to every sub-agent for the whole run") which is frontmatter telemetry, not the § Verification & coverage notes prose the finding targeted. The prose notes read in plain operational register throughout.
- **F9** (fortiweb interim mitigation) — body now reads "Fortinet offers an interim virtual patch, FG-VD-10009598.0day, in FortiWeb signature database update FMWP 26.071." Fetched FG-IR-26-157 directly this iteration; the page's own text (buried in a client-rendered section) states verbatim: "Virtual Patch named "FG-VD-10009598.0day." is available in FMWP db update 26.071." Exact match.
- **F10** (netscaler sourcing note) — sourcing_note now states explicitly that the FIPS/NDcPP ranges and both CVSS figures come from the vendor's CVE records rather than either cited page, and that those records aren't citable under the source-pattern rule. Consistent with the entry's own citation list (watchTowr + NCSC-CH only).

### Missed-angle disposition (confirmed honest)

Both iteration-5 F6/F7 missed angles (SharePoint CVE-2026-55040/63520 exploitation-status change; Symantec Jewelbug/XG-Web browser-extension research) are recorded as *not published* in both the run record's `findings:` block and its prose notes are consistent with `state/coverage_backlog.md`, which I read directly: both appear as **Open** rows with matching reasons (wall-clock cutoff for the SharePoint item; source-coverage gap — publisher not in any research slice — for Jewelbug), matching `Surfaced: 2026-08-15` / `By run: 2026-08-15T0412Z-intel`. No silent drop.

### Additional spot-checks (not part of the eight, done for completeness given the FortiWeb entry's correction history)

Re-fetched all four Fortinet CSAF JSON records directly (`FG-IR-26-156/157/158/160`) rather than relying on the rendered advisory tables. Every affected-version range, fixed-version string, and CVSS score/vector currently in `entries/2026-08-15/fortiweb-radius-wildcard-bypass-fortimanager-fgfm.md` matches the structured record exactly — including the FortiWeb 7.0 branch (present, matching the entry) and the two "upcoming" 7.2.13/7.0.13 builds (matching the entry's "not yet released" framing). CVE-2026-70465's CVSS (7.3), CVE-2026-70468's CVSS (7.3, both FortiManager and FortiManager Cloud), and CVE-2026-70466's CVSS (4.8) all match. This entry's version data appears fully settled after four correction rounds.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)`

One truth-class residual: the F1 nexus-descriptor fix did not fully land — it survives, uncited, in the `malware:plugx` registry record added by this run. Everything else checked (the other seven listed fixes, the missed-angle backlog disposition, and the FortiWeb entry's full CVE dataset against primary CSAF records) is confirmed correct.

### Findings summary (machine-readable)

```yaml
- code: F1
  category: hallucinated-fact
  section: intel
  item: "entities/registry.yaml — malware:plugx (added 2026-08-15, via mustang-panda-coolclient-signed-kernel-driver-rootkit)"
  url_or_quote: "Long-running remote-access implant used by multiple China-nexus espionage groups."
  summary: "Uncited nexus claim survives in the registry summary for a malware record added this run, contradicting iteration 5's own remediation claim that 'no nexus claim now appears in the entry or its registry record.' The entry's own sourcing_note states neither cited source asserts a national nexus; the actor and malware:coolclient/toneshell records were correctly scrubbed, but malware:plugx was missed. Fix: remove or re-source the clause."
```
