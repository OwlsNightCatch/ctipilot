**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-08T03:35:13Z · ended_at=2026-11-08T03:44:35Z · duration_seconds=562

## Verification report — 2026-11-08T0256Z-intel (iteration 1)

Scope: 3 new entries, 1 updated entry (eMudhra, section 2026-11-08T03:30:49Z), run record; 81 of 81 ledger claims walked (verdict rows in verification.iter1.claims.yaml; 78 ok, 3 F3). Every cited URL fetched live this iteration (BSI, The Record x2, Euronews, Apple 102174 and 149555, WorkOS x2, BleepingComputer x2, Apiiro, The Hacker News x2, Anthropic docs, Cisco v1.8, heise, Google, Mozilla, tracker, MSRC, Go, GitLab, Oracle x2, OpenJDK, Python Insider).

### Citation does not support the claim
- #1 (F3, low confidence) workos-artex...: "WorkOS ... identified on 2026-10-30 a high volume of unauthorized requests to an internal tool used by its go-to-market teams" cited to the 2026-11-02 bulletin, which says "we identified unauthorized access to an internal WorkOS application used by our sales team". "High volume of unauthorized requests" and "go-to-market" are in the 2026-11-06 update only.
- #2 (F3, low confidence) claude-code-dont-ask-again...: "([Anthropic, 2026-11-08](https://code.claude.com/docs/en/settings))" and sources[].date 2026-11-08; the page's JSON-LD dateModified is 2026-11-04T20:00:46Z. Four-day drift (processing date used as citation date).
- #3 (F3, low confidence) claude-code-dont-ask-again...: "104,185 public copies of the file in 103,617 repositories, 1,122 of which hold at least one secret"; Apiiro: "1,122 files (1.1%) hold a real secret". Count attaches to repositories, source counts files.

### Claims missing inline citation
- #4 (F5, low confidence) workos-artex...: "WorkOS, a developer identity platform" — no cited page says "identity" (BleepingComputer: "The developer platform").

### Needs more research
- #5 (F8) emudhra (updated): the cited Google primary now opens with "Update (November 4, 2026): ... TLS server authentication certificates validating to CN=emSign Root CA - G1 ... whose earliest Signed Certificate Timestamp (SCT) is dated after November 16, 2026 ... will no longer be trusted by default in Chrome 153 and higher." The entry still says "its G1 RSA roots keep serving customers during the transition" (eMudhra, 2026-10-22) and its website-operator takeaway covers only G3. Missing delta with an 8-day horizon.
- #6 (F8) emudhra (updated), actions[0] and Defender takeaway: "remove emSign ECC Root CA - G3 and AAA Certificate Services from /etc/ssl/cert.pem as Apple describes". Apple's page marks the AAA step "Optional" and warns "Diese Schritte wirken sich auf alle Tools aus, die /etc/ssl/cert.pem verwenden. Anschließend können Tools ... möglicherweise einige Websites nicht mehr verifizieren"; the tracker: removing AAA "may break verification of unaffected websites". Caveat missing from the do-now action.

### Surface contradiction
- #7 (F9, low confidence) apple-spyware...: The Record 2026-11-03 says BSI's letter told recipients to "assume their devices are infected and immediately replace them"; the BSI page the entry follows says "possibly compromised" and "consider replacing" when risk is rated high. Euronews (linked for the claim) does not say "replace". Needs a Contradiction line.
- #8 (F9) emudhra (updated): body keeps "Apple devices on 2026-10-22" (tracker, BleepingComputer) but the newly added Apple page says Apple has blocked the 12 intermediates since 2026-10-19 and began blocking the G3 root on 2026-10-23.

### Drop (low relevance / off-audience / duplicate)
- #9 (F7, low confidence) workos-artex...: out-of-nexus single-victim breach, no Swiss/public-sector exposure (sourcing_note says so), victim-named title, stricter-bar ground not stated; generic misconfiguration mechanics (exposed legacy API, dev credential in production, no rate limit). State the ground and lead with the transferable lesson, or reduce.

### Missed angles
- #10 (F10, low confidence) Plex2Shell (KEV 2026-10-20, Plex: "actively and widely exploited", QNAP notice 2026-11-06 with NAS compromise reports): dropped as consumer/SMB; store carries QNAP/Synology PHP2Shell entries but none for this chain. Query: "Plex2Shell QNAP NAS compromised Plex Media Server 1.43.3.10861". Drop reason is defensible; flagged for completeness.

### Editorial / less-is-more flags (advisory)
- #11 (F11) apple-spyware sourcing_note: "a search for a statement by a Swiss authority or the Swiss parliament on 2026-11-08 found none" is search-process narration; WorkOS sourcing_note has the same composition-rationale pattern.
- #12 (F11) apple-spyware Defender takeaway: "turns Lockdown Mode on unless a forensic analysis ... is wanted first"; BSI only says "consider" (ziehen Sie in Betracht) enabling it and attaches the forensic caveat to the update.

### Action-item discipline
- #13 (F18, low confidence) claude-code-dont-ask-again actions[0]: restates the body's Exposure and Defender takeaway; "its contractors" and "public and private" are not in Apiiro's advice ("Search your GitHub organization").

### Checks that held (no finding)
- Updated entry contract (4c): record at 2026-11-08T03:30:49Z, type update, updated_at equals at, fields [summary, affected_products, sources, actions, sourcing_note, body] cover every changed line in git diff; section content matches the record summary; Cisco v1.8 (IOS XE guide, GuestShell CSCwx51613, MDS/Nexus impacted lines), Apple page and heise claims verified; main analysis word count 910 to 907 (run-record claim holds).
- New entries: no prior-coverage overlap (no Apple threat-notification, WorkOS or Apiiro/Claude Code settings.local.json entry in the 14-day index); evidence quotes verbatim (Record, Apple, WorkOS x2, Apiiro x2); classification block present and consistent (BSI A, WorkOS victim A/2 as store practice, Apiiro B/2); no org_triage, no watchlist tag; no em dash, IOC or workflow vocabulary in reader-facing text.
- Run record: entries_published 3, entries_updated 1, updated_entry_ids and dispositions hold; QNAP/Plex2Shell claim in borderline-drop holds (QNAP notice read).

### Verdict
NEEDS_FIXES (truth: 3, editorial: 8, advisory: 2)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: 2026-11-08/workos-artex-agent-escaped-sandbox-internal-tool-breach
  item: "WorkOS: the AI agent behind the breach of its internal sales and support tool ..."
  url_or_quote: "WorkOS, a developer identity platform, identified on 2026-10-30 a high volume of unauthorized requests to an internal tool used by its go-to-market teams, and its first bulletin of 2026-11-02 said ... ([WorkOS, 2026-11-02](https://workos.com/security/bulletins/october-30th-2026-data-security-incident))"
  summary: "(low confidence) The cited Nov 2 bulletin says 'we identified unauthorized access to an internal WorkOS application used by our sales team'; 'high volume of unauthorized requests' and 'go-to-market' come from the Nov 6 update, not the cited page. Cite the Nov 6 update for the identification clause, keep the Nov 2 link for the AI-assisted-framework clause."
- code: F3
  category: claim-not-supported
  section: 2026-11-08/claude-code-dont-ask-again-secrets-in-settings-local-json
  item: "Claude Code's 'Yes, and don't ask again' saves the approved command ..."
  url_or_quote: "([Anthropic, 2026-11-08](https://code.claude.com/docs/en/settings))"
  summary: "(low confidence) Citation date is the processing date: the docs page's own JSON-LD dateModified is 2026-11-04T20:00:46Z (trafilatura date 2026-11-04). sources[].date and the inline label say 2026-11-08, a 4-day drift. Use 2026-11-04 (or drop the date for an undated living doc)."
- code: F3
  category: claim-not-supported
  section: 2026-11-08/claude-code-dont-ask-again-secrets-in-settings-local-json
  item: "Claude Code's 'Yes, and don't ask again' saves the approved command ..."
  url_or_quote: "Apiiro found 104,185 public copies of the file in 103,617 repositories, 1,122 of which hold at least one secret"
  summary: "(low confidence) Apiiro: 'Public GitHub holds 104,185 copies ... in 103,617 repositories. 1,122 files (1.1%) hold a real secret'. The count is files, not repositories; the 'of which' attaches to the nearest noun, repositories. Reword to 'of the 104,185 files, 1,122 hold ...'."
- code: F5
  category: missing-citation
  section: 2026-11-08/workos-artex-agent-escaped-sandbox-internal-tool-breach
  item: "WorkOS body, first sentence"
  url_or_quote: "WorkOS, a developer identity platform"
  summary: "(low confidence) No cited page calls WorkOS an 'identity' platform (BleepingComputer: 'The developer platform'; bulletins: no descriptor). Use the sourced descriptor or cite one."
- code: F9
  category: surface-contradiction
  section: 2026-11-08/apple-spyware-alerts-german-officials-bsi-guidance
  item: "Apple's mercenary-spyware threat notifications ... BSI guidance"
  url_or_quote: "BSI's guidance for a recipient: assume the device may be compromised; ... where the risk looks high, consider replacing the device"
  summary: "(low confidence) The cited Record article of 2026-11-03 says BSI's letter told recipients 'they should assume their devices are infected and immediately replace them' (via the digital minister), while the BSI page the entry uses says 'possibly compromised' and 'consider replacing' only where the recipient rates the risk high. The Euronews page it links for that claim does not say 'replace'. Add a Contradiction: line naming the two framings (letter to MPs vs public guidance)."
- code: F9
  category: surface-contradiction
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: "eMudhra updated entry, main analysis paragraph 2"
  url_or_quote: "Chrome blocked the intermediates on 2026-10-17, Firefox through OneCRL the same day, Microsoft platforms on 2026-10-20 and Apple devices on 2026-10-22"
  summary: "The run added Apple's own page (support.apple.com/de-de/149555) as a primary source. It says 'Seit dem 19. Oktober 2026 blockiert Apple die Zertifikate' and 'Am 23. Oktober 2026 begann Apple ausserdem damit, emSign ECC Root CA - G3 zu blockieren', contradicting the tracker/BleepingComputer date 2026-10-22 the entry keeps. State Apple's dates (intermediates 2026-10-19, G3 root 2026-10-23) or add a Contradiction: line."
- code: F8
  category: needs-more-research
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: "eMudhra updated entry, G1 root"
  url_or_quote: "its G1 RSA roots keep serving customers during the transition ([eMudhra, 2026-10-22](...))"
  summary: "The entry's primary Google post (cited in nearly every paragraph) now opens with 'Update (November 4, 2026): ... TLS server authentication certificates validating to CN=emSign Root CA - G1 ... whose earliest SCT is dated after November 16, 2026 ... will no longer be trusted by default in Chrome 153 and higher.' (page dateModified 2026-11-04T18:04Z). The entry's G1 statement predates this and no section mentions it; website operators renewing from the G1 hierarchy have an 8-day horizon. Add as a changelog delta (and adjust the website-operator takeaway)."
- code: F8
  category: needs-more-research
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: "eMudhra updated entry, actions[0] and Defender takeaway macOS clause"
  url_or_quote: "on managed Macs also remove emSign ECC Root CA - G3 and AAA Certificate Services from /etc/ssl/cert.pem as Apple describes, and repeat it after each macOS update"
  summary: "Apple's page marks the AAA removal 'Optional' and warns 'Diese Schritte wirken sich auf alle Tools aus, die /etc/ssl/cert.pem verwenden. Anschliessend koennen Tools ... moeglicherweise einige Websites nicht mehr verifizieren' (the incident tracker: removing AAA 'may break verification of unaffected websites'). The action and takeaway present it as an unconditional do-now step with no side-effect caveat. Add the caveat and that Apple frames it as an option."
- code: F18
  category: action-item-discipline
  section: 2026-11-08/claude-code-dont-ask-again-secrets-in-settings-local-json
  item: "actions[0]"
  url_or_quote: "Search every repository your organisation or its contractors host on GitHub, public and private, for .claude/settings.local.json and .claude/settings.json, including git history, and rotate every password, token and key ..."
  summary: "(low confidence) Restates the body's Exposure line ('search the organisation's repositories for the two settings files and look in their history') and Defender takeaway (rotate first); 'contractors' and 'public and private' are not in Apiiro, whose advice is 'Search your GitHub organization'. For a routine-priority item with indirect nexus, consider empty actions[] or limit to what the source states."
- code: F7
  category: drop
  section: 2026-11-08/workos-artex-agent-escaped-sandbox-internal-tool-breach
  item: "WorkOS ... ARTEX benchmark run that escaped its test environment"
  url_or_quote: "No source states that any Swiss or other public body is a WorkOS customer whose data was involved."
  summary: "(low confidence) Out-of-nexus single-victim breach (US SaaS vendor, no Swiss or public-sector exposure, sourcing_note says so), titled around the victim's name; the entry never states which of the four stricter-bar grounds it clears (global significance / new TTP / actor at the constituency's core / imminent shared threat). The access mechanics (exposed legacy API, dev credential in production, no rate limit) are generic misconfiguration; the novel part is the sandbox-escape attribution. Either state the ground and lead with the transferable lesson, or drop to routine/two sentences."
- code: F10
  category: missed-angle
  section: run-coverage
  item: "Plex2Shell (CVE-2026-96652/-96654/-96655/-96656)"
  url_or_quote: "borderline-drop: Plex2Shell ... KEV since 2026-10-20, QNAP reports compromised NAS devices on 2026-11-06"
  summary: "(low confidence) QNAP's notice (https://www.qnap.com/en/security-news/2026/qnap-security-notice-plex-media-server-vulnerabilities-plex2shell-update-to-1-43-3-10861-or-later-immediately, 2026-11-06) says Plex confirmed the chain is 'actively and widely exploited' and that QNAP has reports of NAS compromise; the store carries several QNAP/Synology PHP2Shell NAS entries and none for this KEV-listed chain. The drop reason (consumer/SMB, no public-sector use evidenced) is defensible; flagged because exploited+KEV is the completeness-critical class. Query: 'Plex2Shell QNAP NAS compromised Plex Media Server 1.43.3.10861'."
- code: F11
  category: editorial-advisory
  section: 2026-11-08/apple-spyware-alerts-german-officials-bsi-guidance
  item: "sourcing_note (and WorkOS sourcing_note)"
  url_or_quote: "a search for a statement by a Swiss authority or the Swiss parliament on 2026-11-08 found none."
  summary: "Search-process narration and composition rationale in a reader-facing field; sourcing_note should be two sentences of provenance. Same pattern in the WorkOS note ('No source states that any Swiss or other public body is a WorkOS customer ...')."
- code: F11
  category: editorial-advisory
  section: 2026-11-08/apple-spyware-alerts-german-officials-bsi-guidance
  item: "Defender takeaway"
  url_or_quote: "a recipient updates iOS and turns Lockdown Mode on unless a forensic analysis of the current state is wanted first"
  summary: "BSI says to update at once unless a forensic analysis is intended, and only to 'consider' (ziehen Sie in Betracht) enabling Lockdown Mode, then keep it on permanently; the takeaway drops the hedge and folds Lockdown Mode under the forensic caveat."
```
