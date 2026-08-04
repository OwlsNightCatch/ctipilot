**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-04T06:02:08Z · ended_at=2026-08-04T06:10:16Z · duration_seconds=488

## Verification report — 2026-08-04T0411Z-intel (iteration 4)

Scope actually exercised: the seventh, never-verified entry (`inc-ransom-sonicwall-sma1000-patch-rollback-fake-ir-outreach.md`) against all five of its cited sources (The Hacker News, Dark Reading, Resecurity, SecurityWeek, SonicWall product notice, plus Volexity's own post to test the overreach claim) and against the follow-up findings YAML; the CrowdStrike entry's two-source citation split; and the run record's account of both. The other five entries were not re-litigated per the spawn instructions; no new issue was found in them incidentally.

### Unsupported / hallucinated facts

**F1.** `entries/2026-08-04/inc-ransom-sonicwall-sma1000-patch-rollback-fake-ir-outreach.md` — `techniques: [T1601.001, T1539, T1111, T1657, T1486]`. `T1601.001` ("Patch System Image") is flagged in the entry's own composition trail (`work/2026-08-04T0411Z-intel/findings.followup-sonicwall.yaml`, `techniques_rationale.T1601.001`) as the composer's own analytical mapping, with an explicit request that the verifier check it before carrying. The behavior it maps is stated in the entry body: *"We observed the threat actor maintaining persistence and rolling the newly applied patch back to a vulnerable state to maintain access."* (Brett Deroche/Rapid7, via Dark Reading — quote re-verified verbatim on the live page, `Published Time: 2026-07-17T20:01:13.000Z`). Checked against the pinned ATT&CK dataset (`attack/enterprise-attack.json`):

- `T1601.001` "Patch System Image": *"Adversaries may modify the operating system of a network device to introduce new capabilities or weaken existing defenses... Adversaries may change this file in storage, to be loaded in a future boot, or in memory during runtime."* — describes injecting new/backdoored code into the image, not reverting to a prior version.
- `T1601.002` "Downgrade System Image": *"Adversaries may install an older version of the operating system of a network device to weaken security. Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features."* — this is exactly "rolling the newly applied patch back to a vulnerable state": reverting the appliance to an older, less-secure firmware/patch state to retain the exploitable condition.

`T1601.002` is the sub-technique that matches the sourced behavior; `T1601.001` does not. This is a wrong-sub-technique mapping under an otherwise-correct parent technique (`T1601`), not a fabricated behavior — but it corrupts the store's ATT&CK overlap matrix / Navigator-layer exports for this entity and technique, which is exactly the downstream surface `techniques[]` exists to keep evidence-bound. Recommend replacing `T1601.001` with `T1601.002` in the frontmatter (`techniques_rationale` in the source YAML can stay as documentation of the mapping decision, corrected to name `.002`).

### Editorial / less-is-more flags (advisory)

**F2 (advisory).** `entries/2026-08-04/crowdstrike-2026-threat-hunting-report-exploitation-window.md`, body: *"...telemetry from 'the past year' ([CrowdStrike, 2026-08-03](...)) — a window reporting on the release dates as the 12 months to 30 June 2026 ([SiliconANGLE, 2026-08-03](...))."* Both halves are now correctly attributed — CrowdStrike's own blog says only "the past year" (re-verified live), and SiliconANGLE independently states *"tracking more than 290 named adversaries over the 12 months to June 30"* (re-verified live) — so the iteration-3 remediation is factually sound. The clause "a window reporting on the release dates as" reads awkwardly (it's not clear what "release dates" refers to). Not a truth defect; leaving as-is is defensible, a light copy-edit would help a first-time reader.

### Everything checked and confirmed sound

- **All five `evidence[]` quotes and every body-text quoted fragment** in the SonicWall entry are contiguous verbatim substrings of the pages they're attributed to: The Hacker News (McKee's "dominant threat actor"/"strong technical correlation" statements — confirmed via re-fetch), Dark Reading (Deroche's patch-rollback quote and "Two days later, Rapid7 specifically attributed this activity to Inc ransomware" — confirmed via bridge fetch, `Published Time: 2026-07-17T20:01:13.000Z`), Resecurity (persistence-artifact quote, fake-IR-outreach quote, victim-geography quote, credential-rotation list, rebuild guidance — all confirmed via WebFetch and a jina full-text dump), SecurityWeek ("has emerged as the most active one" — confirmed).
- **The INC-Ransom-is-not-new claim (check b) is accurate and the entry never drifts from it.** Dark Reading's 2026-07-17 article states the Rapid7 attribution explicitly and pre-dates this store's 2026-07-18 original entry by ~8.5 hours; the SonicWall entry's framing ("the actor link is seventeen days old and the new element is only the *dominance* characterisation") is arithmetically and factually correct.
- **The "Volexity and Rapid7 have since linked" overreach claim (check d) is real and correctly handled.** A full-text jina fetch of the Resecurity page confirms the sentence *"Volexity and Rapid7 have since linked the exploitation cluster to INC Ransomware, which has become the dominant threat actor actively weaponizing the vulnerability chain"* appears verbatim in the article's lead paragraph (missed by two narrower WebFetch section-searches, found on the full-text dump). A direct re-fetch of Volexity's own post confirms zero occurrences of "INC" or "ransomware" — Volexity names only UTA0533. The entry correctly attributes the INC link to Rapid7 alone and calls out Resecurity's overstatement by name.
- **The Swiss/victim-geography handling (check c) is strict and correctly non-load-bearing.** `regions: [global]`, the headline and title carry no Swiss/geography claim, and the body ("On victim geography, hold the claim loosely...") states the causal gap explicitly (no named org, no confirmation, no stated per-listing link to the exploit chain) exactly as the follow-up agent's `q4_swiss_victim_claim` assessed it.
- **No IOCs.** Re-checked the entry against the follow-up's own `ioc_warning` list (file hashes, fake-negotiator domain/email/phone, caller pseudonym, User-Agent strings, PoC repo URL) — none appear. The WebFetch of the live SonicWall/Resecurity pages surfaced the actual phone number and email address that a careless composer could have copied (`+1 (304) 384-0401`, `info@helprans[.]com`) — confirmed absent from the entry. Malware family names (ROOTRUN, KNUCKLEBALL) and generic artifact classes are present, which is permitted.
- **`cves[]` (check g).** Both CVSS values (10.0 / 7.2) and the full affected/fixed firmware build lists were re-verified byte-for-byte against a live fetch of the SonicWall product notice and cross-checked against the CISA KEV catalog (via `tools/fetch_source.py cisa-kev`) for id/dateAdded/description. Exact match.
- **Registry relation (`actor:inc-ransom` → `actor:uta0533`, `overlaps-with`).** Direction and type are right for a correlation claim: Rapid7's own words ("a single threat actor or coordinated group is responsible") are a correlation, not an identity claim, and Volexity has published no INC link — `overlaps-with` (never a merge or `attributed-to`) is the correct typing, sourced to the new entry as required.
- **Priority/actions/classification.** `priority: high` clears the bar the commissioning note argued (escalation, not a new imminent critical); both `actions[]` items are concrete, self-contained, and derived from this delta's own mechanics (re-verify firmware version; widen rotation scope) — neither is generic advice or a body restatement, and the list is not padded. `classification: {reliability: B, credibility: 2}` is defensible given the source mix (Rapid7/Resecurity first-hand vs. corroborating outlets).
- **Run record.** The verification-notes account of the iteration-3 miss and its remediation (paragraph beginning "The confirmation pass earned its keep") is accurate on every checkable point: the 07-17/07-18 timing, the Swiss-claim characterization, the Volexity non-attribution, and the Rapid7-source last-modified-vs-first-published cosmetic note. It does not overstate what was done.
- **Publish call (check h).** Agree with publishing. The patch-rollback mechanic and widened rotation scope are genuinely new, high-value, actionable defender content that the original 2026-07-18 entry could not have carried, and the entry's own hedging on attribution age and the Swiss claim means it doesn't misrepresent its novelty to get published. This was a close call but a sound one.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)`

Single required fix: correct `techniques: [T1601.001, ...]` to `T1601.002` on `entries/2026-08-04/inc-ransom-sonicwall-sma1000-patch-rollback-fake-ir-outreach.md` (and the corresponding `techniques_rationale` note in the work-directory findings YAML, for provenance — optional, the YAML is not published). No other defect found in either priority item or in the run record's account of them.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-04
  item: "SonicWall SMA 1000 — INC Ransom dominant-actor / patch-rollback / fake-IR-outreach update"
  url_or_quote: "techniques: [T1601.001, T1539, T1111, T1657, T1486]"
  summary: "T1601.001 (Patch System Image) does not match the sourced behavior (Rapid7: actor rolls a newly applied patch back to a vulnerable state). T1601.002 (Downgrade System Image) is the correct sub-technique per the pinned ATT&CK dataset's own definitions."
- code: F11
  category: editorial-advisory
  section: entries/2026-08-04
  item: "CrowdStrike 2026 Threat Hunting Report — exploitation window"
  url_or_quote: "a window reporting on the release dates as the 12 months to 30 June 2026"
  summary: "Attribution split (CrowdStrike: 'the past year'; SiliconANGLE: '12 months to June 30') is now factually correct after iter-3 remediation, but the joining clause reads awkwardly. Advisory only, no fix required."
```
