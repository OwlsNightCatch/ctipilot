**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-22T05:55:47Z · ended_at=2026-07-22T06:06:20Z · duration_seconds=633
**Self-telemetry:** webfetch_calls=11 · websearch_calls=2 · bridge_fetches=9 · urls_checked=20

## Verification report — 2026-07-22T0409Z-intel (iteration 7)

Cold, independent read of all 7 new entries, the run record, and the 5 added/edited
registry records. Every cited URL fetched this iteration (CISA/NCSC.ch/NCSC-NL/BSI via
the bridge; ZDI/Zimbra/BSI/THN/swissinfo/itmagazine/Halcyon/BleepingComputer/SecurityAffairs/
Kaspersky x2/CheckPoint/KoreaHerald/DailySecu/SeoulShinmun via WebFetch/jina). Every
evidence[] quote checked for verbatim/contiguity; every cves[] id+CVSS checked against a
per-CVE authority; dedup and update_of targets checked against prior_coverage.json and the
entry store; registry↔entry↔run-record consistency checked end to end.

### What was verified clean

- **Langflow (CVE-2026-0770 + 15-CVE batch):** CISA KEV alert lists the four CVEs incl.
  CVE-2026-0770 (verbatim CISA evidence quote). ZDI-26-036 confirms exec_globals/validate
  endpoint/root/CVSS 9.8 (verbatim evidence quote; reported 2025-07-18, disclosed 2026-01-09
  ≈ six months). NCSC-NL CSAF confirms exactly 15 CVEs with matching CVSS (9202=9.8, 8859=9.9,
  9135=9.9, 7754/7755/8476 present). The three specific CVE→behavior mappings (9202 = unauth
  account creation via NEW_USER_IS_ACTIVE; 8859 = APIRequest path-traversal via Content-Disposition;
  9135 = ToolGuard code injection via dynamic CodeInput) independently confirmed. All four CVEs
  absent from prior coverage → new entry correct. Classification A/1 (multi-source confirmed) sound.
- **Zimbra 10.1.20:** NCSC-CH post 12782 + BSI CSAF (exactly CVE-2026-50055/-10631/-50054, no
  per-CVE descriptions/CVSS) + Zimbra blog (9 issues; both evidence quotes verbatim) + THN
  (CVE-2026-50055 = mail-forwarding bypass only). CVE-2026-50055 confirmed RESERVED on NVD.
  The iter-5 CVE-mapping fix holds: the two unmapped IDs are left explicitly unattributed.
- **Everest/Stadler:** swissinfo (both German evidence quotes verbatim) + itmagazine + Halcyon
  (every background claim confirmed). Investigated the aviation-date framing: Halcyon's
  "Current Status: Active as of October 2025 ... aviation systems" line and "Everest claimed on
  their leak site in October to have compromised aviation systems" both support the entry's
  "claimed, in October 2025" wording — not a defect. Registry summary (iter-6 Halcyon-attribution
  fix) is consistent.
- **SharePoint CVE-2026-50522:** NCSC-NL 0237 rev 1.0.2/2026-07-21 UPDATE section — Dutch evidence
  quote is a verbatim contiguous substring (double space and all); CVSS 9.80 confirmed.
  BleepingComputer (both evidence quotes verbatim; Janggggg PoC 2026-07-20; chain) + SecurityAffairs
  (specific article). update_of target 2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup
  exists and prior_coverage maps CVE-2026-50522 to it → update correct.
- **XEntry Team:** Kaspersky Securelist confirms two-incident cluster, "Hacked by XEntry Team"
  (Mexico only), the "may confirm a link"/"do not reveal a clear connection" hedge (verbatim).
  Single-source correctly flagged (verification: single-source + sourcing_note + run-record line);
  credibility 2 correct for uncorroborated single source. iter-4 F13 fix holds.
- **Project CAV3RN/Cavern:** Kaspersky (both evidence quotes verbatim; low-confidence OilRig
  association, no code reuse/infra overlap) + Check Point (Cavern Manticore tracking).
  update_of target 2026-07-21/hollowgraph-... exists. Registry oilrig→cavern-c2-framework is a
  single related-to (low-confidence note), no overlaps-with — matches iter-1/iter-4 fixes.
- **KNDA breach:** Korea Herald (both evidence quotes verbatim) + DailySecu + Seoul Shinmun all
  confirm "up to ~10,000 records" and the exposed/not-exposed data fields. The iter-3 F14 fix
  holds: the fabricated "2,500 / 350" breakdown is gone; no source carries a role breakdown.
  Out-of-region breach clears the gate on scale + transferable exposure-class lesson; lesson-framed.

### Cross-cutting

- No org_triage blocks, no watchlist tags — correct for this deployment (none configured).
- Every entry carries a valid Admiralty classification block; calibration sound.
- Priorities defensible (2× high on actively-exploited RCE, 5× notable); no false criticals,
  no under-alerting.
- actions[] disciplined: two concrete single-task actions (Langflow, Zimbra), five correctly empty
  (incidents/updates/behavioural — hardening left in body, not restated).
- All attacker-behavior entries carry non-empty techniques[]; ids are active ATT&CK.
- No IOCs; English throughout (Dutch/German only inside verbatim evidence quotes); no reader-facing
  workflow jargon.
- Coverage complete: the four-CVE CISA KEV batch fully triaged (Langflow published; DD-WRT and the
  two WordPress WP2Shell CVEs correctly dedup-dropped as already-covered). No unaddressed home-region
  or actively-exploited-edge omission identified.

### Verdict

CLEAN — no truth, editorial, or advisory findings. Six prior iterations drove out the real defects
(OilRig overstatement, unsourced Everest/Langflow claims, KNDA quantifier, Zimbra CVE mapping,
Everest registry propagation); this independent cold read confirms each fix landed and finds no
new defect. Publishable.

### Findings summary (machine-readable)

```yaml
[]
```
