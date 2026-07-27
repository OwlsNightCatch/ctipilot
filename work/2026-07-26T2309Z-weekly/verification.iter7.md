**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-27T01:11:51Z · ended_at=2026-07-27T01:20:51Z · duration_seconds=540
**Self-telemetry:** urls_checked=28 · webfetch_calls=20 · bridge_fetches=15

## Verification report — 2026-07-26T2309Z-weekly (iteration 7)

Cold, independent F1–F18 read of the 11 new strategic entries + run record. Priority focus per spawn: per-fact attribution, quote verbatimness, LAUNDRY BEAR vs TA458 disambiguation, W-PD-1 framing, and the two update_of deltas.

### Sources fetched and verified this iteration
- CISA joint CSA AA26-204A (bridge): confirms "Last 90 days of emails", "Global Address List (GAL)", "Two-factor authentication (2FA) tokens", "Newly-created Application Passcode" — supports the webmail 90d/GAL/2FA clause now cited to AA26-204A. View-based evidence quote verbatim.
- Proofpoint TA488 (WebFetch): "Proofpoint has not observed TA458 using CVE-2025-66376…" verbatim; view/half-click and app-specific-password persistence supported.
- Proofpoint TA458 RoundPress (WebFetch): half-click evidence quote verbatim; "it was patched as CVE-2026-8496 in version 5.12.8" verbatim; GRU assessment supported.
- NCSC-CH post 12778 (bridge): "Current exploitation status: Actively exploited" verbatim.
- BleepingComputer SharePoint (WebFetch): Attacker Eye evidence quote verbatim; machine-key/long-term-access supported.
- Check Point blog (WebFetch): "very specific configuration… without IP restrictions" verbatim; "handful of customers" supported.
- CISA 07-21 four-KEV + 07-22 two-KEV (bridge): confirm CVE-2026-16232 (07-22), CVE-2026-0770/-63030/-60137 (07-21).
- Rapid7 WP2Shell (WebFetch): "Given confirmed exploitation in the wild, Rapid7 strongly recommends investigating for signs of compromise" is a contiguous prefix — verbatim.
- Talos msaRAT (WebFetch): "This RAT never touches the network directly…" verbatim; Twilio TURN relay + Cloudflare Workers signalling supported.
- Zscaler TELESHIM (jina, raw): "TELESHIM abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic." EXACT verbatim (WebFetch had paraphrased; escalation confirmed entry is correct).
- OpenAI (jina): "In one example, the model chained together multiple attack vectors…remote code execution path on the Hugging Face servers." verbatim.
- Hunt.io (WebFetch): "unattended or YOLO mode, bypassing approval prompts…" verbatim; Ministry-not-confirmed hedge correct.
- Sysdig (jina): "In a new development, the operator behind JADEPUFFER has doubled down on that bet, using ransomware to destroy the one thing an organization can't simply restore: a trained AI model." verbatim.
- swissinfo (WebFetch): Everest CHF-10M ransom-not-paid quote verbatim; shared data-exchange platform supported.
- PS News DNSC (WebFetch): 2M-records Romanian quote verbatim; vCenter/ESXi/100-VM/1083-VM/no-AV all confirmed.
- 20min (WebFetch): French bénéficiaires quote verbatim; does NOT name DragonForce (correctly cited to ICTjournal).
- ICTjournal (WebFetch): names DragonForce explicitly.
- Le Temps (jina): BravoX, 220 GB / 100,000+ dossiers, conseiller d'Etat confirmed.
- NCSC-NL 0264 (WebFetch): CVE-2026-62144 CVSS v4 10.0, CVE-2026-62145 CVSS v4 9.4 confirmed.
- NCSC-NL 0252 (bridge): nine CVSS-10.0 unauth Oracle Fusion Middleware flaws; "zeer waarschijnlijk dat grootschalig misbruik op korte termijn" confirmed.
- ENISA EUMSS (WebFetch): baseline-requirements quote verbatim; consultation window, five domains, IR vertical, Reserve two-year rule confirmed.
- ENISA Health (jina): "Contribution Agreement of EUR 6 million…set for three years" verbatim.
- BaFin (jina): "Die Finanzaufsicht Bafin hat am 16. Juli 2026 eine Geldbuße in Höhe von 240.000 Euro gegen die TeamViewer SE festgesetzt." verbatim (ß correct); Article 17(1) confirmed.
- heise (jina): "Ad-hoc-Meldungen müssen über ein elektronisches Informationssystem an Medien und an die Bafin verteilt sowie auf der Unternehmenswebseite veröffentlicht werden" verbatim.
- mySites.guru Gridbox (WebFetch): CVE-2026-61425, unauth cookie-as-identity Super User, fixed 2.20.1, shipped since Oct 2025 confirmed.
- cyberstan nginx (bridge): "defeating ASLR in a single unauthenticated GET request" supported. The hedged "~21 days" withholding figure traces to the referenced operational entry's derivation of the author's stated early-August timeline — consistent, hedged, not a defect.

### Cross-cutting checks
- Disambiguation (F15): LAUNDRY BEAR (Void Blizzard / TA488) and TA458 (RoundPress) held distinct; "not observed TA458 using CVE-2025-66376" quote confirmed on the TA488 page; distinct registry entities. Sound.
- update_of deltas: npm→W29 (SANDWORM_MODE MCP-config poisoning, CrowdStrike-confirmed) and joomla→W28 (Gridbox cookie-as-identity, new technique class) are both genuine deltas.
- Classification (F17): every entry carries a valid Admiralty block; org_triage null throughout (no scheme configured) — correct. joomla single-source correctly credibility 2. No drift.
- F12: joomla (single-source) and eu-procurement (single-source-national-cert, ENISA carve-out) both correctly flagged with sourcing_note.
- techniques[]: non-empty on all threat/incident/vulnerability/synthesis/research kinds; empty only on policy/outlook kinds — correct.
- actions[]: empty on all — correct for weekly strategic entries.
- Priority: two high top-stories justified; none miscalibrated as critical. W-PD-1 framing satisfied by every entry.
- Relevance/completeness: strong CH/EU nexus throughout; Thailand-MoF strand clears the transferable-TTP bar with explicit hedge. W1 abandonment disclosed transparently in run record; no nameable missed in-window story.
- Style: no IOCs, English, no workflow-internal leakage.

### Verdict
CLEAN

No truth or editorial defects found on this cold independent read. The six prior iterations resolved the earlier per-fact-attribution and verbatimness issues; my fetches confirm the current state holds. This CLEAN begins the double-CLEAN publish chain.

### Findings summary (machine-readable)
```yaml
[]
```
