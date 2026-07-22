**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-22T06:08:10Z · ended_at=2026-07-22T06:17:52Z · duration_seconds=582

## Verification report — 2026-07-22T0409Z-intel (iteration 8, confirmation pass)

Cold read of all 7 new entries, the run record, and the 5 registry records this run added/edited. Iteration 7 (Opus) returned CLEAN; this pass does not anchor on that verdict — every URL below was independently `WebFetch`ed / bridge-fetched in this iteration. Three defensible defects surfaced, so iteration 7's CLEAN is **not** confirmed.

### Unsupported / hallucinated facts

**F4-1** — `entities/registry.yaml` `actor:oilrig` (aliases list): the record lists `Lyceum` as a flat alias of OilRig:
```
aliases:
- APT34
- Helix Kitten
- Evasive Serpens
- Hazel Sandstorm
- Lyceum
```
This is not supported by the canonical taxonomy. MITRE ATT&CK's OilRig group page (G0049) lists its associated names as "COBALT GYPSY, IRN2, APT34, Helix Kitten, Evasive Serpens, Hazel Sandstorm, EUROPIUM, ITG13, Earth Simnavaz, Crambus, TA452" — **no Lyceum** (confirmed via direct fetch of `attack.mitre.org/groups/G0049/`). Lyceum is MITRE's own separately-tracked group (Hexane / Spirlin, G0078). Even the run's own cited corroborating source for the Cavern entry — Check Point Research, "Cavern Manticore: Exposing Iran-Linked Modular C2 Framework" (fetched this iteration) — frames the relationship as a **subgroup** claim, not identity: `"links to the OilRig subgroup named Lyceum"`. Flattening a subgroup/overlap claim into a straight alias risks merging Lyceum-specific future reporting under the OilRig canonical key, corrupting the registry's entity-linking integrity that PD-driven dedup depends on. Recommend dropping `Lyceum` from `aliases:` (or, if kept, moving the relationship to a typed `relations[]` edge — e.g. `part-of`/`overlaps-with` sourced to Check Point — rather than an identity alias).

**F4-2** — `2026-07-22/langflow-cve-2026-0770-exploited-ncsc-nl-15-cve-batch` body, closing sentence of paragraph 2: `"This is the third distinct Langflow CVE CISA has KEV-listed in roughly two weeks (after CVE-2026-33017 and CVE-2026-55255 on 2026-07-07)"`. This sentence carries no inline citation and is factually wrong for one of its two named CVEs. CISA's own KEV catalog (bridge-fetched `fetch_source.py cisa-kev` this iteration) gives:
```
CVE-2026-55255  dateAdded 2026-07-07  Langflow Authorization Bypass Through User-Controlled Key Vulnerability
CVE-2026-33017  dateAdded 2026-03-25  Langflow Code Injection Vulnerability
```
CVE-2026-33017 was KEV-listed on **2026-03-25**, roughly four months before this run, not "on 2026-07-07" alongside CVE-2026-55255. The sentence's "third distinct Langflow CVE … in roughly two weeks" framing is therefore overstated — CVE-2026-0770 (07-21) and CVE-2026-55255 (07-07) are indeed two weeks apart, but CVE-2026-33017 does not belong in that "roughly two weeks" cadence. Recommend correcting to something like "the second Langflow CVE CISA has KEV-listed inside two weeks (after CVE-2026-55255 on 2026-07-07), and the third overall following CVE-2026-33017 (KEV-listed 2026-03-25)."

### Citation does not support the claim

**F3-1** — `2026-07-22/cve-2026-50522-sharepoint-machine-key-theft-exploited` body, paragraph 2: `"A PowerShell PoC (attributed to researcher "Janggggg") went public on 2026-07-20; watchTowr's Attacker Eye honeypots captured successful compromises within hours ([Security Affairs, 2026-07-21](https://securityaffairs.com/195760/security/public-poc-triggers-active-exploitation-of-critical-sharepoint-rce-vulnerability-cve-2026-50522.html))."` I fetched the Security Affairs article (via jina reader, since the direct/bridge routes returned a truncated page) in full this iteration: it names **watchTowr** as the party that "identified proof-of-concept exploit code" on July 20th, and separately credits "Cybersecurity firm Defused Cyber" for spotting exploitation — it never names a researcher "Janggggg" and never uses the word "PowerShell". The "Janggggg" attribution IS supported, but by a different source already cited earlier in the very same paragraph: BleepingComputer's article (`"Security researcher **Janggggg** published the demonstrative exploit on GitHub"`, confirmed via `WebFetch` this iteration). The specific researcher-attribution clause is attached to the wrong citation. Recommend re-citing that clause to BleepingComputer (already in `sources[]`) rather than Security Affairs.

### Strengthen primary source

**F6-1** — `2026-07-22/zimbra-10-1-20-snmp-command-injection-rce-plus-stored-xss`: the entry's `sourcing_note` and body state "the issue mapping for the other two IDs is not stated in any cited source and is left unattributed" (re: CVE-2026-10631 and CVE-2026-50054). That is accurate for the three sources actually cited (BSI CERT-Bund, Zimbra blog, The Hacker News — I re-confirmed BSI's rendered advisory page carries only bare CVE IDs with no visible per-CVE descriptions, and The Hacker News names only CVE-2026-50055). However, SecurityWeek's article "Zimbra Update Patches Critical Vulnerabilities" (fetched this iteration, not currently in the entry's `sources[]`) explicitly resolves the gap: `"CVE-2026-10631: an access control vulnerability in the EWS extension"` and `"CVE-2026-50054: an authorization issue in mailbox delegation"`. Recommend adding this URL as a corroborating source and restoring the specific CVE↔issue mapping (the `type` fields for these two CVEs were downgraded to generic `logic-flaw` in iteration 5's fix pending this exact confirmation — this closes that gap).

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: entities/registry.yaml
  item: "actor:oilrig"
  url_or_quote: "aliases: [..., Lyceum]"
  summary: "MITRE ATT&CK G0049 (OilRig) lists no 'Lyceum' alias; Lyceum is MITRE's separately-tracked G0078 (Hexane/Spirlin). The run's own cited Check Point source frames it as a subgroup claim, not an identity alias."
- code: F4
  category: hallucinated-fact
  section: 2026-07-22/langflow-cve-2026-0770-exploited-ncsc-nl-15-cve-batch
  item: "body para 2"
  url_or_quote: "This is the third distinct Langflow CVE CISA has KEV-listed in roughly two weeks (after CVE-2026-33017 and CVE-2026-55255 on 2026-07-07)"
  summary: "CISA KEV catalog shows CVE-2026-33017 dateAdded 2026-03-25 (not 2026-07-07); only CVE-2026-55255 (07-07) and CVE-2026-0770 (07-21) fall inside 'roughly two weeks'."
- code: F3
  category: claim-not-supported
  section: 2026-07-22/cve-2026-50522-sharepoint-machine-key-theft-exploited
  item: "body para 2, PowerShell PoC / Janggggg clause"
  url_or_quote: "https://securityaffairs.com/195760/security/public-poc-triggers-active-exploitation-of-critical-sharepoint-rce-vulnerability-cve-2026-50522.html"
  summary: "Security Affairs names watchTowr and Defused Cyber, never 'Janggggg' or 'PowerShell'; the Janggggg attribution is instead supported by the already-cited BleepingComputer article."
- code: F6
  category: strengthen-primary-source
  section: 2026-07-22/zimbra-10-1-20-snmp-command-injection-rce-plus-stored-xss
  item: "CVE-2026-10631 / CVE-2026-50054 issue mapping"
  url_or_quote: "https://www.securityweek.com/zimbra-update-patches-critical-vulnerabilities/"
  summary: "SecurityWeek explicitly maps CVE-2026-10631=EWS access control and CVE-2026-50054=mailbox delegation authorization; entry currently leaves both unattributed for lack of a cited source that states this."
```
