**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-12T23:51:31Z · ended_at=2026-07-13T00:00:15Z

## Verification report — 2026-07-12T2309Z-weekly (iteration 1)

Cold read of 15 new W28 strategic entries + run record. Weekly dedup polarity applied
(strategic entries synthesise this week's operational entries; the-gentlemen-status →
update_of W26, netherlands-nis2-in-force → update_of W27, both confirmed present in prior
coverage). check_run.py exited 0 pre-verify. jina-402 outage noted; not verifier-relevant.

Evidence-quote verification: all load-bearing evidence[] quotes fetched and confirmed
VERBATIM against their sources — Huntress Conditional-Access (2 quotes), Huntress CitrixBleed,
Unit 42 The Gentlemen (2), Socket jscrambler (2), Group-IB Scattered Spider (2), FINMA (2
German), Rijksoverheid (Dutch), BleepingComputer/KEVIntel ColdFusion, THN Joomla endpoint,
mySites.guru SP Page Builder, NCSC-CH Gitea (via bridge recipe — 'Actively Exploited, Proof of
Concept Available' + 'via a single custom HTTP header' both confirmed), Mandiant ADFS
('bypassing MFA, conditional access, and all identity-based controls'). Also fetched and
confirmed content: AI Now 'Friendly Fire', THN GitHub verified-commit malleability, Groupe 3R
SwissCybersecurity (July-7 forensic-update content confirmed under the May-slug URL).

Single-source items correctly flagged: threat-actor (Scattered Spider reframing = single Group-IB
primary, verification: single-source, sourcing_note names it) and the-gentlemen (Unit 42,
single-source) — no F12. No watchlist usage anywhere (all watchlist_hit: false); org_triage null
everywhere — correct for this deployment (no F16). Every entry carries a valid Admiralty
classification within vocabulary; FINMA/NIS2 reliability A appropriate for national-authority
primaries (no F17). Actions on Joomla/exploited-edge/npm are all concrete, do-now and
finding-derived; the sector/research/policy/roll-up entries correctly carry actions: [] (no F18).
W-PD-1: every entry answers on-fire / cross-day / strategic-shift or is a valid update/outlook —
no bare re-lists. Priority: the four highs (Joomla, exploited-edge, M365, gov-targeting) are
defensible; no critical is the right call. Coverage looks complete — run-record telemetry shows
W1 actively checked and excluded ShinyHunters/UNC6240, FortiBleed, DragonForce/CitrixBleed,
Operation Endgame; no in-window story I can name a source for is missing.

### Unsupported / hallucinated facts

**F4 — weekly-w28-government-public-admin-targeting — 'EU-facing' mischaracterisation of a
Pakistani victim.** Body asserts: "three of the five strands carry a direct home-region or
EU-critical-operator nexus (a Swiss cantonal authority, a Latvian state operator, an EU-facing
espionage watering-hole)". The watering-hole strand's cited source
(https://www.sentinelone.com/labs/one-target-china-india-espionage-converge-on-pakistani-law-enforcement/)
describes a PAKISTANI law-enforcement Complaint Management System — part of an EU-*supported*
(funded) 'Smart Police Station' programme in Balochistan, not an EU-facing target. The referenced
operational entry (2026-07-10/e-government-portal-watering-hole-cms-implant-espionage) states
verbatim "the victim class carries no direct European nexus" and its sourcing_note reads
"Out-of-nexus by victim (Pakistani law enforcement) — surfaced for the transferable technique
class". So the strand belongs on transferable-technique grounds, not EU nexus; the "three … direct
… nexus" count is really two (Swiss PDAG + Latvian LVM). Fix: recharacterise the strand as
EU-supported-programme / transferable-technique and correct the count. Entry itself is sound and
stays high.

**F4 — weekly-w28-vuln-status-rollup — summary lists a non-exploited CVE under 'Confirmed
exploited / KEV'.** Summary frontmatter: "Confirmed exploited / KEV this week: … and the Joomla
extension file-upload wave (CVE-2026-48908/56290/56291/48939/57827)". CVE-2026-57827 (RSFiles!) is
listed inside the confirmed-exploited wave, but the same entry's body says "CVE-2026-57827/57828
patched without confirmed exploitation yet" and the Joomla top-story confirms "no confirmed
exploitation of that pair yet". Summary overstates body/source. Fix: remove 57827 from the
confirmed-exploited parenthetical (retain 48908/56290/56291/48939).

### Observations (non-blocking, no finding raised)

- Citation date labels in several entries trail the source page date by 1–3 days (e.g.
  "[BleepingComputer, 2026-07-08]" vs a July-6 page; "[Mandiant, 2026-07-09]" vs July-7;
  "[Huntress, 2026-07-10]" vs July-9; "[AI Now Institute, 2026-07-11]" vs July-8; "[The Hacker
  News, 2026-07-09]" for the GitHub item vs July-8). These consistently match the operational
  entries' event dates (dating the development, not the article) and every cited claim is fully
  supported, so this is a deliberate/defensible convention, not raised as a defect. WebFetch date
  extraction is itself unreliable; flagged only for awareness.
- healthcare entry credibility: 1 aggregates a single-source-victim Groupe 3R strand (rated
  credibility 2 operationally); acceptable for a multi-strand synthesis of first-party/authoritative
  disclosures — not raised.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

Both findings are content-correctness fixes on otherwise-sound entries; neither warrants a drop.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: weekly-sector-patterns
  item: "weekly-w28-government-public-admin-targeting"
  url_or_quote: "three of the five strands carry a direct home-region or EU-critical-operator nexus (a Swiss cantonal authority, a Latvian state operator, an EU-facing espionage watering-hole)"
  summary: "e-gov watering-hole is a Pakistani victim in an EU-supported programme, not 'EU-facing'; source and referenced operational entry both state no European nexus. Recharacterise as transferable-technique; correct 'three' to two direct-nexus strands."
- code: F4
  category: hallucinated-fact
  section: weekly-vuln-rollup
  item: "weekly-w28-vuln-status-rollup"
  url_or_quote: "Confirmed exploited / KEV this week: ... and the Joomla extension file-upload wave (CVE-2026-48908/56290/56291/48939/57827)"
  summary: "Summary lists CVE-2026-57827 under confirmed-exploited/KEV; body and Joomla top-story state 57827/57828 patched without confirmed exploitation. Drop 57827 from that parenthetical."
```
