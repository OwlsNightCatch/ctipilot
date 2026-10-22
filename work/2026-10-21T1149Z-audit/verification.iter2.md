**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T20:43:25Z · ended_at=2026-10-21T21:02:49Z · duration_seconds=1164

## Verification report — 2026-10-21T1149Z-audit (iteration 2)

Scope (post-fix pass, 155 of 276 ledger claims, every one with a row in `verification.iter2.claims.yaml`: 153 ok, 2 F3): all 28 claims in `claims.changed.iter2.yaml`; every claim of the nine entries remediated after iteration 1 (Japan GSS, nginx, YellowKey, Dirty Frag, DEVCORE Exchange, DENIC, Cisco SD-WAN CVE-2026-20245, FortiClient EMS, Adobe APSB26-120: 115 claims including the changed ones); and a random quarter of the other 161 claims (40, seeded; drawn from CERT-FR, GLPI, LiteLLM, Spring Cloud Config, Copy Fail, the Pwn2Own roundup, Exchange OWA, Ghost CMS, Nightmare Eclipse, Cisco CVE-2026-20262, SimpleHelp and Oracle EBS). The nine remediated entries were read whole with `git diff HEAD`; the SimpleHelp, Oracle EBS, Copy Fail, Exchange OWA, Ghost, Nightmare Eclipse, Pwn2Own and n8n diffs and entries were read for the sampled claims, and the Unified CM claims were checked beyond the sample. Every cited page was fetched this pass (MSRC through `msrc cve` and the CVRF for 2026-May, -Jun and -Aug; NCSC-CH through `ncsc-csh`; CISA KEV through the bridge; EUVD through its API; the rest through `extract`/`url`). The gate was re-run: `check_run.py` 58 pass, 0 warn, 0 fail. Unreadable in this pass: CCB Belgium (403 maintenance page on `extract`, `url` and `WebFetch`); no claim in scope rests on it alone.

### Prior-iteration deltas (all re-checked against fetched sources)

- F1 Japan: the Digital Agency notice is `sources[0]`; the nippon.com URL is gone from sources, body and evidence (curl 404 confirmed); `sourcing_note` reads two outlets, no rating vocabulary; the record summary says the source is dropped. Confirmed. Residual dangling references: see F11 #7.
- F3 nginx: re-cited to EUVD, which carries "leading to a restart", but the wording "the reliable impact" is not on the page: see F3 #2.
- F3 YellowKey (GreenPlasma inference): dropped; only The Register's UAC clause remains and is on the page ("in its current state it triggers a UAC consent prompt in default Windows configurations"). Confirmed.
- F3 YellowKey ("closes both flaws"): the takeaway now cites MSRC CVE-2026-45586 (Released Jun 9, 2026; CVRF 2026-Jun lists its fixed builds for Windows 10, 11 and Server 2012 to 2025). Confirmed.
- F4 wave report: priority reads "high to notable" and the entry is `priority: notable`; base `29364cd` equals `base.sha`. F4 run record: repair-4 stamps 11:56:07Z to 12:09:56Z give 829 s. All durations, the 23/2/6/15 record split and `updated_at` mirrors hold.
- F5 YellowKey 2026-05-20 section: the MSRC link now follows the "consider implementing" quotation, which is on the page ("Microsoft recommends that you consider implementing these mitigations if you are concerned your devices and data are at risk of being compromised or stolen"); "TPM-only" is gone; nothing after 2026-05-20 is reported (the script described there appeared on 2026-05-21 but the steps match the earlier manual ones; the 2026-10-21 section dates the replacement correctly).
- F8 Dirty Frag: "Copy Fail is the earlier CVE-2026-31431" is on the Microsoft blog ("previously disclosed CopyFail vulnerability (CVE-2026-31431)"); `references[]` carries the Copy Fail entry; the record summary declares the nickname drop and the link.
- F9 YellowKey summary: attributed; but see F9 #5 on the takeaway. F9 nginx: the Contradiction line states NCSC-CH #12575 ("Achieving RCE additionally requires the host system to have ... ASLR disabled") against F5's updated description. Confirmed. F9 DEVCORE: Franky's Web says "The attacker does not need valid credentials"; MSRC says "an authorized attacker" (CVSS 8.0); both now stated. Residual: F9 #4. F9 DENIC: "more than three hours" matches the entry's own timeline (21:57 to 01:15 local, 19:57 to 23:15 UTC, 3 h 18 min); DENIC's final report says "approximately three hours", which is not contradicted.
- F18 Cisco 20245: the action now ends with the edge-device configuration check (Cisco: "verify the configuration of the edge devices"); the auth.log hunt lives in Detection; the record summary declares the dropped UID-0 check. F18 nginx: action removed, `actions` in the record's `fields`. Confirmed.
- F11 FortiClient: payload and log names replaced by behaviour; no attacker file name remains (`fortitray.exe` and `ipsec.exe` are the Fortinet binaries Arctic Wolf names as the process parents). F11 Adobe: "run record" and "this window" removed from the sourcing note.
- Declined items (F16 SimpleHelp and Dirty Frag, Pwn2Own ledger, CERT-FR/Exchange duplication, Nightmare Eclipse `cves[]`, ZDI announcement date, GLPI range, CCB Belgium): not re-raised. Note for the SimpleHelp priority: Horizon3 says the group-login setting "is found to be enabled in practice with the clients we assessed" and 7.2% of ~14,000 exposed servers use OIDC, which supports leaving it `critical`.

### Citation does not support the claim

- **F3 #1** — 2026-06-30 SimpleHelp, Exposure: "SimpleHelp servers on 5.5.15 or earlier, or on an affected 6.0 beta or release-candidate build, with OIDC group-authenticated technician logins enabled ([Horizon3.ai, 2026-06-12](...))". The Horizon3 page (read in full) gives the three conditions but no SimpleHelp version at all. The ranges are on SimpleHelp's guide ("Servers on 5.5.15 and earlier, and early 6.0 pre-release builds (beta and release candidates) are vulnerable if all of the following are true"). HEAD cited both SimpleHelp and Horizon3 on this clause; this fire's rewrite kept only Horizon3 on it. Cite the guide on the version clause.
- **F3 #2** (low confidence) — 2026-05-15 nginx: "F5 describes the reliable impact as a heap buffer overflow in the NGINX worker process leading to a restart ([ENISA EUVD, 2026-09-10])". EUVD (assigner f5): "This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with ... ASLR ... disabled or when the attacker can bypass ASLR." "Reliable" is not on the page and the text is hedged ("may cause").

### Unsupported / hallucinated facts

- **F4 #3** — run record `entities_added: []`. `git diff HEAD -- entities/registry.yaml` adds `product:chroma`, `product:lm-studio`, `product:nvidia-container-toolkit`, `product:nvidia-megatron-bridge`, `product:red-hat-enterprise-linux-for-workstations` (first_seen 2026-05-17), and the wave report says `tools/sync_products.py` "added five product records". docs/pipeline.md: `entities_added` = "registry keys added this run"; the 2026-10-11T1307Z-audit record lists its product keys and its verifier raised the same omission. List the five keys.

### Surface contradiction

- **F9 #4** (low confidence) — DEVCORE Exchange, Contradiction line: the remediation sets Microsoft ("authorized attacker") against Franky's Web ("does not need valid credentials") but leaves out MB VRED, cited in the takeaway and the 2026-10-21 section, whose page is titled "Analysis of Exchange Server Pre-Auth RCE (CVE-2026-62911)" and calls it a "PreAuth RCE vuln demo at p2o 2026" (its text also shows a `low_priv_attacker`, so its reading is ambiguous). Add it to the line or say so.
- **F9 #5** (low confidence) — YellowKey takeaway: "For devices that leave the premises, TPM+PIN removes YellowKey's precondition ([MSRC CVE-2026-45585])" states Microsoft's side flat although the entry's Contradiction line records the researcher's unpublished TPM+PIN variant; the MSRC sentence is "No, if you are using TPM+PIN the vulnerability is not exploitable" and does not say "precondition". Attribute it, as the summary now does.

### Editorial / less-is-more flags (advisory)

- **F11 #6** — 2026-05-25 Ghost CMS: "While the page silently downloads `update.zip`, ... starts `update.bat` minimized; ... starts its exported `Begin` function through `rundll32`" (and `update.zip` again in the 2026-10-21 section). Attacker-chosen file names added by this fire (neither HEAD survivor nor twin carries them); XLab lists them among its IOCs. Same class as the FortiClient names removed in iteration 1. Describe the behaviour without the names.
- **F11 #7** (low confidence) — 2026-09-12 Japan GSS: the 2026-09-13 section still lists Jiji Press among the three outlets that "each report that announcement" though Jiji is dropped and 404; the 2026-10-21 section says "An earlier note here called it undisclosed whether the flaw was known", but this fire deleted that clause from the 2026-09-13 section, so there is no earlier note to find. State only that the minister said the agency knew of the flaw beforehand, and acknowledge Jiji's removal.
- **F11 #8** (pre-existing) — 2026-08-07 Adobe APSB26-120: em dashes in title, headline, summary and body.
- **F11 #9** (low confidence) — nginx: "2026-09-10" labels the EUVD record's `dateUpdated` (published "May 13, 2026"); right where the text says "updated on 2026-09-10", but the restart clause and `sources[].date` carry it without saying so.
- **F11 #10** (low confidence) — run record `bridge_uses: []` although repair-3 used `fetch_source.py bsi-csaf` and iteration 1 reports 120 bridge fetches; the previous audit record lists such uses.
- **F11 #11** — run record body is still "(skeleton)"; it must be written before the commit.

### Checks with no finding

Update-vs-new decisions hold (the Ghost fold is the same finding and carries the twin's verified facts; Adobe, YellowKey, Nightmare Eclipse and DEVCORE links are correct `references[]`). All sampled evidence quotes are verbatim on their pages (the two Proofpoint quotes match once the extract's markdown link is stripped). Priority: YellowKey `notable` (patched, not exploited), Nightmare Eclipse `notable`, nginx `high` (PoC public, VulnCheck honeypot attempts), Cisco 20245 `high` (exploited, KEV) are defensible. No IOC strings (hashes, IPs, attacker domains) in the 23 bodies; no workflow vocabulary in reader-facing fields. KEV dates verified against the catalogue (CVE-2026-20245 2026-06-09, 35616 2026-04-06, 42208 2026-05-08, 20262 2026-06-15, 48558 2026-06-29, 46817 2026-07-15). Missed angles: none; this wave published no new entries and its sources were the entries' own.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 2, advisory: 6)

### Findings summary (machine-readable)

See `work/2026-10-21T1149Z-audit/verification.iter2.findings.yaml` (11 records).
