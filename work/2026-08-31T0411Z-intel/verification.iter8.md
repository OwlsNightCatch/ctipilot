**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-31T07:39:50Z · ended_at=2026-08-31T07:53:26Z · duration_seconds=816

## Verification report — 2026-08-31T0411Z-intel (iteration 8)

Prior-iteration deltas walked first: iteration 7's sole finding (CVE-2026-49869 `status[]` missing `patch-available`) is correctly remediated — `status: [exploited, patch-available]` now present on `ai-infrastructure-litellm-ragflow-kestra-intrusions.md` cves[2], and the other two `cves[]` records (CVE-2026-42271, CVE-2026-48710) both correctly carry `patch-available` alongside `exploited`, confirming the internal consistency the finding asked for. No new defect introduced by this specific remediation.

Full independent cold read follows below. All 6 new entries, all 3 updated entries (body + frontmatter + `git diff HEAD`), and the run record were read end to end; every inline URL across all 9 entries was fetched this iteration.

### Unsupported / hallucinated facts

**#1 (high confidence) — `manchester-airports-group-data-breach-8-7-million.md`: main-analysis body contradicts the entry's own new Update section.** `git diff HEAD` confirms paragraphs 2–3 of the main body (predating this run) were NOT touched by this run's edit — only a new `## Update — 2026-08-31T05:35:00Z` section was appended. Those untouched paragraphs still read: "No extortion group or actor has claimed the incident publicly at time of writing, and neither MAG nor any outlet has named an access vector, an exploited product, or a CVE" (paragraph 2) and "No source states an access vector, exploited product or CVE, and no extortion actor has claimed responsibility" (paragraph 3, opening the "transferable point is scale rather than mechanism" argument). Both are now false: the same file's own `## Update — 2026-08-31T05:35:00Z` section states "The extortion group FulcrumSec claimed responsibility on 2026-08-30... naming an access vector for the first time: airport-specific Iterable (marketing-platform) API credentials exposed in client-side JavaScript," and the frontmatter title/headline were correctly rewritten to reflect this. This is exactly the check-4c(e) case ("an update that made the CVE exploited while the analysis still says 'no exploitation observed' ... is F4") — the main analysis needs a rewrite (or at minimum a "before this update" qualifier) to stop asserting facts the entry's own newest section refutes two paragraphs later. Fix: reword the "No extortion group..." and "No source states an access vector..." sentences to something like "At the time of MAG's disclosure, no actor had claimed the incident and no access vector had been named — see the 2026-08-31 update below," and reconsider whether "the transferable point is scale rather than mechanism" still holds now that a mechanism (client-side API-key exposure) is on the record.

**#2 (moderate confidence) — `ai-infrastructure-litellm-ragflow-kestra-intrusions.md`: "Kestra's cluster-wide XMRig deployment" is not supported by the cited source.** Body, "The pattern that matters more than any single product" section: "resource monetisation converged in two of the three (LiteLLM's cryptomining, **Kestra's cluster-wide XMRig deployment**)". Fetched `https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/` in full this iteration — the Kestra case study's Stage 3 ("Cryptominer deployment") describes a single compromised worker: "Telemetry showed miner retrieval from a public release source, archive extraction, binary renaming, background execution, and mining-pool communication." The Defender-coverage table likewise says "XMRig v6.26.0 launched with RandomX MSR tuning toward a Monero mining pool, consuming **host** CPU for attacker profit" (singular host). No sentence in the source uses "cluster," "cluster-wide," or describes the miner spreading to more than the one compromised worker node — the Docker-socket enumeration in Stage 2 only reads OTHER containers' *environment variables* (credential exposure), it does not describe miner deployment to those containers. "Cluster-wide" overstates scope beyond what the source documents.

**#3 (low–moderate confidence) — `ai-infrastructure-litellm-ragflow-kestra-intrusions.md`: CVE-2026-48710's `status: [exploited, patch-available]` may overstate what Microsoft's own telemetry confirms.** Frontmatter `cves[1]` (CVE-2026-48710) carries `exploited`. The primary source's own language, verified verbatim this iteration: "Microsoft assesses with high confidence that initial access likely occurred through exploitation of the exposed LiteLLM gateway surface. Relevant public vulnerability paths include CVE-2026-42271... and **the route described in public research** that chains this flaw with CVE-2026-48710... to achieve unauthenticated remote code execution" and "CVE-2026-48710 **can weaken** the authentication boundary in affected configurations, **potentially making** that capability reachable without valid credentials." Microsoft's "high confidence" assessment is explicitly scoped to "the exposed LiteLLM gateway surface" and to CVE-2026-42271 by name; the CVE-2026-42271+CVE-2026-48710 chain itself is attributed to third-party "public research" (the blog's own References section cites Horizon3.ai's write-up) with hedged verbs ("can," "potentially"), not confirmed by Microsoft's own telemetry the way CVE-2026-42271 alone and CVE-2026-49869 are. Marking CVE-2026-48710 `exploited` with the same confidence level as the other two CVEs arguably overstates the source. This is a nuanced hedge-strength reading, not a clean hallucination — flagging for the main agent to weigh (e.g., soften body language around the CVE-2026-48710 clause, or add a qualifier distinguishing Microsoft's own confirmed finding from the third-party chain it cites).

### Citation does not support the claim

**#4 (moderate confidence) — `france-sdis-fire-rescue-data-leak-campaign.md`: July-wave per-unit figures cited to the wrong co-cited article.** Body paragraph 2: "The July wave's cumulative claims — spanning the Landes, **Marne (2,167 people)**, **Alpes-Maritimes (2,325 people)**, Alpes-de-Haute-Provence and Aisne SDIS, plus separate claims against **SDIS d'Indre-et-Loire (2,637 public-service agents plus 54 individuals linked to private structures)**... — totalled at least 166,376 exposed individuals, with a potential total exceeding 932,376... ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/))." The single citation ending this sentence points to the **2026-08-30** ZATAZ article, which only restates the aggregate totals (166,376 / 932,376) — it does NOT contain the Marne, Alpes-Maritimes or Indre-et-Loire per-unit figures. Fetched both ZATAZ articles this iteration: those specific figures (2,167; 2,325; 2,637+54) appear only in the **2026-07-26** ZATAZ article ("Le SDIS de la Marne apparaît ensuite. 2 167 personnes seraient concernées"; "Pour les Alpes-Maritimes, ChimeraZ revendique 2 325 personnes"; "annonce 2 637 agents issus de services publics, auxquels s'ajoutent 54 personnes rattachées à des structures privées"), which is also a listed source on this entry but is not the one cited at the end of this specific clause-chain. Per check 2(d) adjacency: the sentence chains facts from two different articles but names only one. Fix: split the citation so the per-unit figures point to the 2026-07-26 article and the aggregate totals to the 2026-08-30 (or either — both state the totals).

**#5 (low confidence) — `purpledelta-dprk-it-worker-facilitator-rmm-detection.md` update section: "router and VPN connection logs" — no VPN log source is named in the cited case.** New body text: "In that same case, forensic timeline reconstruction from **router and VPN connection logs** showed the laptop moving from an MSP's guest network to a residential wireless network to a fixed ethernet connection..." Fetched the Huntress source this iteration (`https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation`): the August-2026 financial-services timeline (the case being described here) is built from router connections (GL.iNet travel router, BGW320-500 residential router, fixed ethernet), Windows Registry / Security Event ID 6416 (USB device installs), Entra self-service password reset, and browser history — no VPN log source appears anywhere in that case's narrative. VPN evidence (Astrill VPN authentication) appears only in the separate February-2026 healthcare case, which this specific sentence is not about. "VPN connection logs" looks like a cross-case splice.

### Claims missing inline citation

**#6 (high confidence) — `ai-infrastructure-litellm-ragflow-kestra-intrusions.md`: the entire "The pattern that matters more than any single product" section carries zero inline citations.** Confirmed by direct inspection of the file: the whole paragraph — "Initial access differed... but credential collection and durable access converged in all three; resource monetisation converged in two of the three (LiteLLM's cryptomining, Kestra's cluster-wide XMRig deployment)... Microsoft's own framing is the operational takeaway... Correlating an unexpected shell or interpreter spawned from an AI-workload process with subsequent secret access, application-file modification, Docker-socket use, outbound callbacks and resource-hijacking activity exposes this class of attack earlier than any single product-specific indicator." — has no markdown link anywhere. This is a synthesis paragraph making several specific, checkable claims (including the disputed "cluster-wide" claim at #2 above), unlike the entry's Defender-takeaway paragraph (uncited by house style across this run's other entries) — this is a distinct analytical H2 section, not a takeaway, and per check 3 needs its own citation(s) back to the Microsoft blog.

**#7 (moderate confidence) — `zero-logement-vacant-metabase-breach-zerobytes.md`: platform-takedown claim uncited.** Body, end of paragraph 3: "No government confirmation of scope was located, but **the platform's takedown after the intrusion was discovered is a de facto acknowledgment an incident occurred.**" No citation attached to this clause. Fetched Clubic this iteration — it explicitly supports the underlying fact ("La plateforme a été mise hors ligne après la découverte de l'intrusion"; "Le service Zéro Logement Vacant est toujours hors ligne depuis la découverte de l'intrusion"), and Clubic is already a listed source on this entry, but the sentence carries no link. Fix: attach the Clubic citation to this clause.

### Generic / oversight URLs (replace with specific article)

**#8 (moderate confidence) — `watchguard-fireware-ike-vpn-preauth-rce-epm-overflow.md`: BSI CERT-Bund portal URL uses the wrong advisory-id format.** Cited URL: `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-W-2026-3068`. Fetched the CSAF machine-readable document this iteration via `python3 tools/fetch_source.py bsi-csaf WID-SEC-2026-3068` (the bridge tool itself rejects the "W" form: "invalid BSI advisory id ... expected WID-SEC-YYYY-NNNN"). The CSAF document's own `references[]` list distinguishes two URLs explicitly: `{"category": "self", "summary": "WID-SEC-W-2026-3068 - CSAF Version", "url": "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-3068.json"}` and `{"category": "self", "summary": "WID-SEC-2026-3068 - Portal Version", "url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068"}` — BSI's own document labels the **non-"W"** id as the correct portal-page URL; the "W" id is the machine-readable CSAF-file's own tracking id, not a portal query parameter. BSI's own RSS feed (`bsi-rss`) independently confirms this, linking `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068` (no W) for this same WatchGuard advisory. This finding was raised in iteration 1 in a different form ("URL renders as SPA shell to plain fetch") and declined as matching store convention with content confirmed via the structured API — that decline addressed reachability, not this specific new evidence that the ID format itself is wrong per BSI's own document. Both the "W" and non-"W" portal URLs return an identical client-rendered Angular shell to a plain fetch, so I cannot directly confirm the "W" URL 404s in-browser, but BSI's own CSAF file is unambiguous about which format the portal query expects. Replacement URL: `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068`.

### Editorial / less-is-more flags (advisory)

**#9 (advisory, low confidence)** — `purpledelta-dprk-it-worker-facilitator-rmm-detection.md`: the 2026-08-31 update record's declared `fields: [techniques, actions, sourcing_note, sources, evidence, body]` includes `actions`, but `git diff HEAD` shows the `actions:` array is byte-identical before and after this run (both bullets appear as unchanged context lines) — net zero change. This is consistent with iteration 4's history (an action item was added then removed within this same run's remediation cycle, netting back to the original two bullets), so it is very likely a stale/leftover field-list entry from that add-then-revert rather than a current inaccuracy — nothing ships differently to the reader. Worth a one-line cleanup (drop `actions` from `fields`) but not a truth or reader-facing defect.

**#10 (advisory, low confidence)** — Cross-entry inconsistency, out of this run's scope: `ai-infrastructure-litellm-ragflow-kestra-intrusions.md` correctly carries `cvss: "8.7"` / `vector: zero-click` for CVE-2026-42271 (confirmed against BerriAI's own GHSA-v4p8-mg3p-g94g: CVSS v4.0 8.7, vector `AV:N/AC:L/AT:P/PR:L/UI:N/...`), and declares `references: ["2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti", ...]`. That older, un-touched 2026-06-09 entry still carries `cvss: n/a` and `vector: user-interaction` for the same CVE — a real cross-entry inconsistency for a triage agent cross-referencing this CVE, but the older entry is not in this run's scope (not among the 3 updated entries) and correcting it would need its own changelog record on that entry. Flagging for the quality audit, not requesting action from this run.

**#11 (advisory, low confidence)** — `zero-logement-vacant-metabase-breach-zerobytes.md`: body says "and several thousand unique emails and phone numbers"; ZATAZ's own precise figures (fetched this iteration) are "10 729 adresses électroniques uniques, 6 847 numéros de téléphone distincts" — 10,729 unique emails is arguably "over ten thousand" rather than "several thousand." Minor undersell of a number the source states precisely; not incorrect, just imprecise.

### Verdict

`NEEDS_FIXES (truth: 6, editorial: 2, advisory: 3)`

Truth (#1–#5, #8): the Manchester Airports contradiction (#1) is the standout — a clean, high-confidence check-4c(e) violation (stale main-body claims directly refuted by the entry's own newest update section) that survived 7 prior iterations because those iterations' remediations to this entry (iteration 5) touched only the frontmatter title/headline and the new section, never the pre-existing body paragraphs the new section now contradicts. The AI-infrastructure deep dive — despite already carrying the heaviest remediation load of this run (iterations 1, 2, 3, 4, 6, 7 all touched it) — still has two residual truth-class issues (#2, #3) plus one editorial gap (#6), all newly surfaced this pass; this entry has been the recurring source of residual findings across the loop and would benefit from one more targeted read focused specifically on its synthesis paragraph and CVE-2026-48710's confidence framing. #4 and #5 are citation-adjacency splices of the type the org profile calls out as the pipeline's dominant residual defect class. #8 is a genuinely new catch (BSI's own CSAF document contradicts the cited portal-URL format) not raised in any prior iteration.

Editorial (#6, #7): both are missing-citation gaps on claims the entry's own listed sources do support — low remediation cost (add the link), not sourcing problems.

Coverage-completeness check (11/13): re-read the run record's coverage notes, `fetch_failures`, and `bridge_uses` against the dedup context (`prior_coverage.json`, `entities/registry.yaml`) — no additional in-window gap identified this pass beyond what iteration 5's F10 (Swiss wealth-manager/Transparency-Register lead) already surfaced and logged to `coverage_backlog.md`; the inside-it-ch persistent block and the ash_ai borderline-drop are both reasonably documented and argued. No new missed-angle finding this iteration.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "manchester-airports-group-data-breach-8-7-million.md (updated entry)"
  url_or_quote: "No extortion group or actor has claimed the incident publicly at time of writing, and neither MAG nor any outlet has named an access vector, an exploited product, or a CVE."
  summary: "Main-analysis body (untouched by this run's diff) directly contradicted by the entry's own new 2026-08-31 Update section, which states FulcrumSec claimed responsibility and named an access vector (Iterable API credentials in client-side JS)."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "ai-infrastructure-litellm-ragflow-kestra-intrusions.md"
  url_or_quote: "Kestra's cluster-wide XMRig deployment"
  summary: "Microsoft's blog documents XMRig deployed on the single compromised worker only ('consuming host CPU'); no source text supports 'cluster-wide' scope."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "ai-infrastructure-litellm-ragflow-kestra-intrusions.md"
  url_or_quote: "cves[1] CVE-2026-48710 status: [exploited, patch-available]"
  summary: "(low-moderate confidence) Microsoft attributes the specific CVE-2026-42271+CVE-2026-48710 chain to 'the route described in public research' with hedged language ('can weaken', 'potentially making reachable'), distinct from its own directly-confirmed high-confidence assessment for CVE-2026-42271 alone and CVE-2026-49869; marking CVE-2026-48710 exploited at the same confidence level may overstate the source."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "france-sdis-fire-rescue-data-leak-campaign.md"
  url_or_quote: "Marne (2,167 people), Alpes-Maritimes (2,325 people) ... SDIS d'Indre-et-Loire (2,637 public-service agents plus 54 individuals linked to private structures) ... ([ZATAZ.COM, 2026-08-30])"
  summary: "Per-unit figures belong to the 2026-07-26 ZATAZ article (also a listed source); the cited 2026-08-30 article only carries the aggregate totals, not these per-unit numbers."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "purpledelta-dprk-it-worker-facilitator-rmm-detection.md (updated entry)"
  url_or_quote: "forensic timeline reconstruction from router and VPN connection logs"
  summary: "(low confidence) The cited August-2026 financial-services case's timeline is built from router/USB/Windows-Event-Log/Entra evidence per the Huntress source; no VPN log source appears in that case's narrative (VPN evidence belongs to the separate February 2026 case)."
- code: F2
  category: generic-url
  section: new-entries
  item: "watchguard-fireware-ike-vpn-preauth-rce-epm-overflow.md"
  url_or_quote: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-W-2026-3068"
  summary: "(moderate confidence) BSI's own CSAF document labels this 'W' id as the CSAF-file's own tracking id, not the portal query; its own references[] list gives the portal URL as https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068 (no W), independently confirmed via BSI's RSS feed."
- code: F5
  category: missing-citation
  section: new-entries
  item: "ai-infrastructure-litellm-ragflow-kestra-intrusions.md"
  url_or_quote: "## The pattern that matters more than any single product (entire section)"
  summary: "Whole analytical section paraphrasing multiple specific Microsoft-blog claims carries zero inline citations."
- code: F5
  category: missing-citation
  section: new-entries
  item: "zero-logement-vacant-metabase-breach-zerobytes.md"
  url_or_quote: "the platform's takedown after the intrusion was discovered is a de facto acknowledgment an incident occurred"
  summary: "Uncited; Clubic (a listed source) explicitly supports the claim ('La plateforme a été mise hors ligne...') but is not linked at this clause."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "purpledelta-dprk-it-worker-facilitator-rmm-detection.md (updated entry)"
  url_or_quote: "fields: [techniques, actions, sourcing_note, sources, evidence, body]"
  summary: "(low confidence) actions[] shows no net diff vs HEAD (likely a stale field-list entry left from an add-then-revert during this run's earlier remediation); no reader-facing impact."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "ai-infrastructure-litellm-ragflow-kestra-intrusions.md / 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti"
  url_or_quote: "cvss: n/a / vector: user-interaction (older entry) vs cvss: 8.7 / vector: zero-click (this entry, correct)"
  summary: "(low confidence) Pre-existing cross-entry inconsistency for the same CVE; older entry out of this run's scope, flagged for the quality audit."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "zero-logement-vacant-metabase-breach-zerobytes.md"
  url_or_quote: "several thousand unique emails and phone numbers"
  summary: "(low confidence) ZATAZ's own figures are 10,729 emails / 6,847 phones — 'several thousand' undersells the precise number the source states."
```
