# W1-I: residuals noticed by the wave 02 repair workers

Noticed outside the findings each worker was given and left unfixed (the brief allowed no scope creep). Source: `work/2026-10-21T0800Z-audit/repair-<n>.md` § Residuals. Each item still needs checking against its source before a fix.

## repair-1

- Headlines over 120 characters: Beagle (127), GTIG UNC6671 (158), node-ipc (155).
- Fox Tempest `sources[].publisher` strings carry two em dashes.
- PAN-OS 2026-06-10 section still gives fixed builds as "12.1.7+, 11.2.12+, 11.1.15+, 10.2.18-h6+", omitting the earlier hotfix builds. The main text and CVE record are complete.
- The Aikido citation now redirects to `/blog/dirty-frag-cve-2026-43284`, whose page metadata dates it 2026-04-07, while the Fragnesia entry dates it 2026-09-04. (Verifier iteration 8: the page's JSON-LD also carries datePublished 2026-09-04, so the label may be right.)
- The registry key `tool:beagle-fake-claude-stac4713-2026` embeds the STAC4713 link that the 2026-09-30 correction withdrew (the key is permanent, but its name and aliases may need review).
- The Nx entry's "Hardening:" paragraph (extension allow-list, `--ignore-scripts`, approval for install scripts) is largely uncited.
- The Beagle `sources[]` records have no `date` field (the date sits in the publisher string).

## repair-2

- Kemp: Progress's release notes describe the CVE-2026-8037 fix as command injection "in the cipher set UI and API command", while ZDI and watchTowr place it in `/accessv2` `apiuser` handling (KEV: "multiple command endpoints"); the entry gives only the latter.
- Kemp: the 2026-08-08 section's inline Triage ("small, stable set of management sources") is uncited inference.
- Kemp: no cves[] record for CVE-2026-33691 although the body treats it as the bulletin's second CVE.
- Check Point: still `priority: critical` with an `immediate_action` on a June finding; Help Net Security source carries `role: primary`.
- G7 summary: "Geneva–Vaud corridor" has no source wording behind it (ZENDATA says delegations land at Geneva and stay on the Swiss side).
- FortiSandbox: title em dash remains until the entry next gets a record.
- Tool: `sync_products.py --report` writes `entities/registry.yaml`; its docstring presents it as read-only ("what resolved where").

## repair-3

- `tools/sync_products.py --report` writes the registry despite being described as a report mode (tool defect).
- `update_of: null` (retired key) still present on the LiteLLM, PHP, WinRAR, RoguePlanet and Langflow entries.
- LiteLLM: title and headline are identical; the main analysis keeps a legacy "#### CVE Summary Table".
- PeopleSoft: `priority: critical` with `immediate_action` on a June/September wave (calibration); inline T-ids in prose; a non-canonical "**Detection and hunting concepts (no IOCs).**" label and no main-analysis Exposure or Defender takeaway (legacy pass); "Confidence ... is MEDIUM" pipeline wording in the 2026-06-16 section.
- `state/cves_seen.json` titles are stale: CVE-2026-6722 says "patched in PHP 8.4.8" (entry: 8.4.21 etc.); CVE-2026-7261/7262 say "patched 2026-05-08" (entry: 2026-05-07); CVE-2026-65400 names only CVSS 7.1.
- ServiceNow: the EUVD source URL uses the path `/enisa/EUVD-2026-43520`, unlike the store's `/vulnerability/` and `/enisa/eu_vulnerability_database/` forms; it may not resolve.
- SEPPmail: `sources[]` lists the vendor contact page (https://www.seppmail.com/about-us/contact/) as a corroborating source.
- TeamCity: the 2026-08-06 section's sentence on the KEV deadline having "no operational meaning for Swiss organisations" is profile framing.
- CHAINDROP: the 2026-08-08 section puts `**Defender takeaway:**` and `**Triage:**` in one paragraph.
- macOS CVE-2026-65400: the KEV record now carries `forensicTriage: Yes` and BOD 26-04 required-action text the entry does not mention.
- ox.security blog posts are unreadable from this container by every transport (403), WebFetch included.

## repair-4

- Coding-agent entry (research): no Exposure/Detection lines, and its sourcing note runs about eight sentences.
- Exchange entry: Detection and Defender takeaway are inline in paragraph 2, not separate labelled lines, and there is no Exposure line.
- SonicWall entry: Defender takeaway inline in paragraph 3; no Exposure/Detection lines.
- Pixel entry: no Exposure/Detection lines.
- Check Point: both SKs were last modified 2026-10-13. If the R82.20 Take 10 line was added after 2026-09-30, it was a new fix in the world, not an omission (not determinable; the HFA index is a WebHelp shell).
- JFrog entry: still `priority: critical` with an immediate_action five weeks after exploitation began; a calibration question for the audit.
- SAP August: Onapsis also lists Note 3747367 (CVE-2026-44747, HotNews 9.9 update), not in the entry. SAP's page shows a later "Update to Security Note" for 3771065, whose content was not read.
- MikroTik: em dashes remain in title, summary, sourcing_note, actions[1] and body (18) for its next record.
- Cisco ISE and Pixel: earlier `updates[]` summaries still carry statements later corrections retracted (append-only, audit trail only).

## repair-5

- austria-nisg-2026-bcs-transposition: the 2026-09-30 Correction quotes the German word "strafbar" with an English gloss rather than as a marked translation.
- openai-agent-australia-medicare-portal-breach: sources[] publisher "ABC News (Australia) — exclusive, Cam Wilson" contains an em dash.
- oracle-september-2026-cspu-five-unauthenticated-cvss-10: the sourcing note's "No exploitation reporting or KEV listing exists" is an undated negative claim.
- the-gentlemen-open-directory-vhdx-backup-ntds-theft: the body says the upload went "to Wasabi cloud storage"; Talos writes "cloud storage services such as Wasabi".
- shinyhunters-fbi-peoplesoft-breach-claim: the 2026-09-27 section still ends "no party has confirmed or denied either technical claim" in undated present tense.
- virtualizor-billing-hook-unauth-root-rce: VulnCheck's three advisory descriptions read "before 3.2.9 (Patch 9) and 3.0.0", an odd CNA string the entry does not reflect; the CNA's CVSS 3.1 scores stay unshown because only the CVE record carries them.

## repair-6

- tools/check_run.py page checks: drupal.org's "Client Challenge" wall clears `_MIN_PAGE_SKELETON` because script blocks are kept, so every drupal.org citation gets false quote-literal and citation-cve flags. Either add drupal.org to `_JS_RENDERED_HOSTS` or detect challenge bodies. `fetch_source.py url` also does not treat this challenge as a block, so it does not fall back to jina.
- UNCTAD entry, 2026-10-02 section: it still cites Transluce's request tag beginning with "oai", an attribution marker string. This is borderline for the no-marker-indicator rule; it is not the payload labels of item 4.
- Telerik and UNCTAD entries label their detection paragraph "**Detection and hunting.**" rather than the fixed "**Detection:**" string the site lifts.
- Flink takeaway: "is itself worth watching for as this technique's next evolution" is an unsourced forecast.
- Citrix TechZone blog: the jina read shows Published Time 2026-10-04T01:42Z, which is 2026-10-03 PDT and matches the page's "Last Updated on: October 3, 2026". The cited date is fine; no action.
## wave 02 verifier, pre-existing advisories carried forward

- Kemp CVE-2026-8037: "as root" sits under the watchTowr citation, whose page lacks it; the 2026-07-02 section's "(CVSS 9.6–9.8)" sits under eSentire, which carries only 9.6 (verification.iter4).
- ShieldBreak: the 2026-08-24 section quotes "not expected on supported versions", which is not a substring of LevelBlue's sentence, and names file-level artifacts (phoneinfo.dll, WD_SCAN, the symlink target) that read as file-name indicators (verification.iter4).
- NCSC-CH RoguePlanet 2026-07-09: the "NCSC-CH, 2026-07-09" label sits on a clause about ShieldBreak, which post 12622 added on 2026-08-12 (CVE reference on 2026-08-17) (verification.iter4).
- Check Point IKEv1: `priority: critical` with an immediate action on a June finding (verification.iter1, F16).
- Kemp CVE-2026-8037: the GA and LTSF labels sit under an ENISA EUVD citation whose record carries neither, and "the 9.8 score is ZDI's" ends under an EUVD citation (verification.iter4 part c, verification.iter5, verification.iter7).
- ShieldBreak: this fire's own quotes (the 2026-08-18 sentence, the 2026-10-21 correction, a new evidence quote) name phoneinfo.dll, LevelBlue's published detection artifact; decide with the 2026-08-24 item above (verification.iter5).
- Ninja Forms CVE-2026-92438: ENISA EUVD-2026-84282 carries WPScan's score (8.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H); add it to the alias's cves[] record with that source (verification.iter7).
