# Retrospective truth pass, shared brief (cleanup wave 04, run 2026-10-21T1148Z-audit)

You are a fact-checker for a defensive threat-intelligence knowledge base. The entries you check are already published. They carry no IOCs and no exploit code by policy. Your job: assume nothing, fetch ground truth, and say for every entry whether it is true as it stands today. This is a **retrospective audit pass** (`prompts/quality-audit.md` Phase 1), not a Phase 5.7 iteration: there is no publish verdict and no double-CLEAN chain. Read-only: never edit entries, state, registry or sources.

Today is **2026-10-21** (UTC, clock verified against the network). The entries were filed 2026-05-10 to 2026-05-22.

## What these entries are

Every entry in your batch was migrated from the v2 daily briefs (May 2026) before claim verification, inline citations and the current entry contract existed. No audit has ever checked them. Earlier audits that did check entries of this vintage found a state attribution the cited authority never made, victims placed in the wrong exploitation wave, CVEs marked exploited where the vendor reported one, invented package versions, a regulator review that never opened, and statistics absent from the cited report. Treat every claim as unverified until you read it on a fetched primary (vendor PSIRT or advisory, national CERT, the discloser, the victim, the regulator, the court). An `evidence[]` item quoting "ctipilot v2 brief (migrated)" is the pipeline quoting itself and proves nothing.

The entries also lack what the current contract requires, and a repair worker will add it after you. Your pass supplies the verified material it builds on (the `upgrade` block below), so the worker composes from what you read instead of fetching everything a second time.

## Scope

Every entry file named in your spawn message, read **whole**: frontmatter, main analysis, every `## <Type> — <at>` changelog section and every `updates[]` record.

## What to check, per entry (fetch the primaries; the entry's own citations are not ground truth on their own)

1. Every `cves[]` id and CVSS against the **per-CVE authority** (vendor PSIRT, per-CVE advisory, the discloser's per-vulnerability page). A multi-CVE roundup, even the same publisher's, is never sufficient. Check which flaw each id names (no positional pairing), `affected` / `fixed` against the vendor's structured table, and `status` (exploited / KEV) against the current CISA KEV record (`python3 tools/fetch_source.py cisa-kev` works in this container) and the vendor's own exploitation statement. A CVE id or score that only the CVE record carries (CVE Services API, cve.org, NVD) can be read to check a fact but is never citable. ENISA EUVD per-vulnerability pages are citable and carry the numbering authority's score (`python3 tools/fetch_source.py enisa-euvd advisory <EUVD-id>`). Also flag CVE ids the body names that `cves[]` lacks.
2. Exploitation claims, version boundaries, affected and patched products, victim statements, attribution, counts, dates, durations, and every `evidence[]` quote **verbatim** against its cited URL (a contiguous passage, no splicing). A "no patch" or "no exploitation" claim is checked against the vendor's own channel and written as of its date.
3. **Citation binding.** Each inline citation must sit on a clause its page actually carries. Earlier cleanup passes kept finding a clause cited to a page that holds only part of it, or a paraphrase looser than the source. Flag the clause, name the page that does carry it (when you found one), or say no page you read carries it.
4. Every `techniques[]` id already present is **active** in the pinned dataset `attack/enterprise-attack.json` (ATT&CK v20). Check mechanically, never from memory:
   `python3 -c "import json,sys;d=json.load(open('attack/enterprise-attack.json'))['techniques'];[print(t, d.get(t,{}).get('name'), 'REVOKED' if d.get(t,{}).get('revoked') else '', 'DEPRECATED' if d.get(t,{}).get('deprecated') else '', 'UNKNOWN' if t not in d else '') for t in sys.argv[1:]]" T1190 T1059.001`
5. No IOCs (hashes, IPs, attacker domains, defanged indicators, rule code). Frontmatter agrees with the body. A four-part version number written bare (`5.3.2.0`) reads as an IPv4 address to the IOC scan: note it so the worker writes "version 5.3.2.0".
6. Pipeline self-reference in reader text ("first coverage in this brief series", "tracked here", "~96 h" latency tags in a headline, "(migrated)") is an imprecision to remove. Priority only as context: these entries were judged against the bar on the day they were filed, so flag a `high` or `critical` only when it plainly failed its bar on the facts known then (an unexploited flaw in a non-default configuration, an out-of-nexus incident with no vector or actor).

## The `upgrade` block (every entry, clean ones too)

For each entry, record what its fetched sources support, each item with the URL you read it on:

- `techniques`: every ATT&CK technique the sources describe, as `{id, behavior, url}`, active ids only (check them with the command above). The access or exploitation vector is always mappable on a `threat`, `incident` or `vulnerability` entry when the source states it (an RCE on an exposed service is T1190, a phishing lure T1566, a local privilege escalation T1068). When the sources do not say how access was obtained, map only what they do describe and say so: never bolt on an access vector the sources do not state.
- `rating`: a NATO Admiralty `{reliability: A-F, credibility: 1-6, basis}`. Reliability follows the reporting source's nature (a national CERT for its own jurisdiction or a vendor PSIRT for its own product is A; original research labs and large outlets B; re-reporters C or lower). Credibility follows independent corroboration ("who looked?", not "how many pages say it"): two independent assessors agreeing is 1; one reliable assessor uncorroborated is 2; a vendor advisory plus CERT restatements of it is one assessor, so 2.
- `exposure`, `detection`, `triage`, `takeaway`: short verbatim passages (at most about 300 characters each) from the fetched sources that support each labelled line: who is affected and how to tell (version, feature state, configuration, sector), the telemetry where the activity shows up and any post-patch compromise check, an honest benign-lookalike discriminator (leave `triage` empty when the source gives none, never invent one), and what decision changes. Quote, do not compose.
- `bodies`: for each page you read, the path where you saved its text (below).

## Duplicates

If two entries in your batch report the same finding (same flaw, same disclosure, or a legacy "UPDATE" item and its original), list them as a group at the end of your YAML with a proposed survivor and why. An entry that looks like a twin of an entry outside your batch: name both ids in a `possible_twin_outside_batch` note on the entry, nothing more.

## Inputs

- Your **claim ledger**: `work/2026-10-21T1148Z-audit/truth-<BATCH>.ledger.yaml` (one row per claim, every entry of your batch whole). Write one verdict row per claim to `work/2026-10-21T1148Z-audit/truth-<BATCH>.claims.yaml` as you go: `- {claim_id: <id>, verdict: ok|F3|F4|F5|F13|F14|unreadable, source_url: <url or null>, passage: "<at most 200 chars>"}`. A claim no transport can read is `unreadable`, never `ok`. Every ledger row gets a verdict row.
- Dedup context if you need it: `entities/registry.yaml`, `state/cves_seen.json`.
- **Fetch ladder:** `python3 tools/fetch_source.py extract <URL>` first (clean article body), `url <URL>` for raw HTML, `pdf <URL>` for PDFs, structured recipes (`cisa-kev`, `cisa csaf <id>`, `cert-fr ...`, `msrc ...`, `osv vuln <id>`, `enisa-euvd advisory <id>`, `sec-edgar ...`, `ico-uk ...`), then `WebFetch` with the outbound-links template from your definition (verbatim quotes only, never read "not affected" into an absence) for hosts the container is walled out of (cisa.gov pages without a recipe), `jina <URL>` last. A page that has moved: search for its current URL and say so. Append each fetch to `work/2026-10-21T1148Z-audit/url-liveness.tsv` as `<url>\t<status>\t<UTC timestamp>`.
- **Your own directory:** `work/2026-10-21T1148Z-audit/truth-<BATCH>/`. Save every page body you read there as `bodies/<short-slug>.txt` with the URL on the first line (the repair worker re-reads these), and keep any helper or scratch file there. Never write to another batch's directory.

## Outputs (write order matters)

1. First action: `mkdir -p work/2026-10-21T1148Z-audit/truth-<BATCH>/bodies && date -u +"%Y-%m-%dT%H:%M:%SZ" | tee work/2026-10-21T1148Z-audit/truth-<BATCH>.started_at`
2. After each entry: append `<UTC timestamp> <entry-id> <verdict>` to `work/2026-10-21T1148Z-audit/truth-<BATCH>.progress`, and checkpoint the findings YAML (a cut-off then costs the tail, not the batch).
3. `work/2026-10-21T1148Z-audit/truth-<BATCH>.yaml`, a top-level `entries:` list, one record per entry in your batch, clean ones included, then `duplicate_groups:` (empty list when none):
   ```yaml
   entries:
     - entry: 2026-05-13/example-slug
       verdict: clean            # clean | imprecision | factual-error
       defects:                  # empty list when clean
         - where: "summary"      # field, body paragraph N, labelled line, cves[CVE-...], evidence[N], section <at>
           claim: "<verbatim from the entry>"
           defect: "<what is wrong, one sentence>"
           ground_truth: "<what the source actually says, verbatim where possible>"
           ground_truth_url: "<the page you read it on>"
           fix: "<the narrowest correct statement or field value>"
           class: factual-error  # factual-error | imprecision
       upgrade:
         techniques: [{id: T1190, behavior: "...", url: "..."}]
         rating: {reliability: A, credibility: 2, basis: "..."}
         exposure: [{quote: "...", url: "..."}]
         detection: [{quote: "...", url: "..."}]
         triage: []
         takeaway: [{quote: "...", url: "..."}]
         bodies: [work/2026-10-21T1148Z-audit/truth-<BATCH>/bodies/....txt]
       possible_twin_outside_batch: null
   duplicate_groups: []
   ```
   `factual-error`: the entry asserts something its sources or the authority contradict or do not support, a wrong id, version, date, score or status, an invented quote or statistic. `imprecision`: true but imprecise or missing a material qualifier, an uncited clause, a citation bound to a page that does not carry the clause for a true fact, pipeline self-reference. Mark a defect you cannot fully confirm `(low confidence)` at the start of `ground_truth`.
4. `work/2026-10-21T1148Z-audit/truth-<BATCH>.md`: the Model and Timestamps lines, then per entry with a defect: entry id, quoted claim, ground truth with URL, fix. No commentary on what was fine.
5. Last: `date -u +"%Y-%m-%dT%H:%M:%SZ" | tee work/2026-10-21T1148Z-audit/truth-<BATCH>.ended_at`

## Return exactly these lines

```
**Model:** <friendly name> (`<model-id>`)
**Timestamps:** started_at=... · ended_at=... · duration_seconds=...
**Entries:** N checked · clean N · imprecision N · factual-error N
**Claims:** in_scope=N checked=N
**Duplicate groups:** N
**Findings:** work/2026-10-21T1148Z-audit/truth-<BATCH>.yaml
**Self-telemetry:** webfetch_calls=NN websearch_calls=NN bridge_fetches=NN urls_checked=NN
```

Take the model name from the model line in your own system prompt (fallback: env vars with the marker ` — container default, env fallback`). No time limit: check every claim, not a sample. Nobody answers questions mid-pass: the spawn message and this brief are the whole task. Your findings carry evidence, not reasoning narration.
