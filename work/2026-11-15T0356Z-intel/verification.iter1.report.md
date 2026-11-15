**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T04:32:53Z · ended_at=2026-11-15T04:42:26Z · duration_seconds=573

## Verification report — 2026-11-15T0356Z-intel (iteration 1)

Scope: 3 new entries, 1 updated entry (Cursor marketplace), run record. Iteration 1 covers all 71 ledger claims (claims.iter1.yaml); every claim has a row in verification.iter1.claims.yaml (62 ok, 9 non-ok, 0 unreadable). Every cited URL was fetched this iteration (Cursor notice and incident report, Fireworks bulletin, Microsoft, Sophos, heise, Phorion, NCSC Hub post 13121, Apiiro, Sonatype, JFrog, StepSecurity, Huntress, Ransom-ISAC); Apiiro was served by the reader rung inside `extract`. No prior-iteration deltas. Evidence quotes: the 10 quotes checked by the gate were spot-confirmed on the pages (all literal).

Update check (Cursor, 4c): the new section is the same finding, carries a genuine delta (origin of the compromise), every claim in it matches https://cursor.com/blog/security-incident-update and the Fireworks bulletin, the record's fields cover every changed frontmatter line in `git diff HEAD`, `updated_at` equals the record's `at`, the main analysis no longer says the origin is undisclosed and the Open VSX statements are reconciled (NCSC post attributed, Cursor and Microsoft stated). Record summary matches the section. Only wording defects below.

### Citation does not support the claim

1. [F3] 2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (summary): "coding errors made the SSH step fail on most standard-user hosts, so Cursor and Sophos say the attacker could not log in there"
   (low confidence) Sophos (https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace) says only "Due to coding errors, SSH enablement fails on most macOS and Windows hosts"; the 'attacker could not log in' conclusion is Cursor's ("the attacker could not have logged in through the tunnel"). Attribute the conclusion to Cursor and the failure to both.

2. [F3] 2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (summary): "a credential from those traces let the attacker write the extension straight onto the marketplace cache"
   (low confidence) Cursor (https://cursor.com/blog/security-incident-update) says "using a stolen credential from the exposed data from our internal system, the attacker placed malicious, unauthorized copies ... directly on the cache". It does not say the credential came from the traces; step 1 says the traces' credentials let the attacker reach select SaaS tools, and step 3 refers to 'the exposed data from our internal system'. The body's wording ('a credential taken through a key exposed at its vendor Fireworks') is the safer form; align the summary to it.

3. [F3] 2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 2): "1,949 repositories were infected again after being publicly listed because the stolen access still worked"
   (low confidence) Apiiro (https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits) says "1,949 got injection pushes after their listing date" and, separately, "Where owners cleaned up, the stolen access often still worked"; it does not say all 1,949 were cleaned-up repositories or that the cause holds for each. In 553 of 2,849 repos the owner kept working on top of the loader, so many were never cleaned. Say 'often' or split the count from the cause.

4. [F3] 2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 2): "The loader reads the newest transaction of a hard-coded Ethereum wallet ... ([Sonatype, 2026-11-04](...))"
   (low confidence, minor) Sonatype says the loaders "locate a transaction sent by the hard-coded wallet"; 'newest' is stated by Apiiro (code comment 'newest tx') and StepSecurity ('most recent transaction'), not by the Sonatype page the clause cites. Add Apiiro to the citation.

5. [F3] 2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (summary): "which an operator keeps online by revisiting the servers every 151 seconds"
   (low confidence) Huntress: "Across 29 servers with complete connection histories ... the operator revisited the servers every 151 seconds". The summary applies it to all 118 servers; the body is correctly scoped to 29. Add 'on the 29 servers with complete history'.


### Unsupported / hallucinated facts

6. [F4] 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (title, headline, summary): headline: "GPO locker failed on replication"; title: "the GPO locker lost a replication race"; summary: "never reached clients because of a replication race" -- https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/
   Hedge dropped. Ransom-ISAC says "The locker's domain-wide mode most likely failed because of a replication race", "One line in the actor's deployment script most likely lost a race against replication" and "That mismatch is why the full deployment most likely failed on replication lag". Title, headline and summary state the cause as established; the sourcing_note hedges only the Domain Admin step. Summary and title also state the Domain Admin hop "through a dormant local administrator" while the report says "We could not prove how the elevation happened" (body hedges correctly). Add 'likely' / 'most likely' to title, headline and summary.

7. [F4] 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (frontmatter sectors): sectors: [technology]
   (low confidence) The only source never names the victim's sector: it says "a Gentlemen affiliate breached a small company" and "The victim's infrastructure is confidential". 'technology' is unsupported; if the taxonomy has no neutral value, an empty list is more honest than a guessed sector.

8. [F4] 2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers and 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (discovered_at): discovered_at: "2026-11-15T04:36:00Z" (ScreenConnect); discovered_at: "2026-11-15T04:41:00Z" (Gentlemen)
   Both timestamps postdate the files' own last write and the clock when verification started: ScreenConnect file mtime 04:27:47Z, Gentlemen file mtime 04:32:26Z, verifier clock 04:32:53Z at start. The run record's completed: '2026-11-15T04:50:00Z' (written 04:31:19Z) and the duration_seconds 3230 derived from it are likewise ahead of the clock. Low severity (gate slack accepts it) but the values are not true when written; set them to actual write times and set completed at the real end.

9. [F4] runs/2026-11-15/2026-11-15T0356Z-intel.md, Verification & coverage notes, 'Single-source:' line: 2026-11-15/screenconnect-crypto-exchange-bait-guest-sessions-118-servers ... 2026-11-15/gentlemen-affiliate-vpn-no-mfa-domain-admin-gpo-locker-failed
   The two ids do not exist. entries/2026-11-15/ holds screenconnect-crypto-bait-guest-sessions-118-servers.md and gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed.md (ls output). Correct the ids in the note.


### Needs more research

10. [F8] 2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (Defender takeaway): "in Huntress's hypothesis the target is a technician client below 26.6.5"
   (low confidence) Huntress's first recommendation is "MSPs should upgrade ScreenConnect host clients to 26.6.5 or later" and, if upgrades must wait, remove TransferFiles from roles and session groups. The takeaway lists only enrolment-limiting steps and the action list omits the lever (reasonably, as the CVE-2026-84869 entry carries it); one clause stating the upgrade lever in the takeaway would let a reader act without opening the other entry.


### Quantifier without source

11. [F14] 2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 1 and summary): "Three routes share one trait: nothing runs at install time." / summary: "nothing runs at install time"
   No cited source states this generalisation for all three routes. JFrog (https://research.jfrog.com/post/accurasofthire-fake-interview/) says the camera-check route hands the candidate a command that downloads a fake 'driver' installer which runs a bootstrap and the payload ("The code runs in the terminal"), and the entry's own sentence says the command "installs the same loader"; StepSecurity lists 'when the candidate runs the "driver" command' as a separate execution trigger. What the sources support is narrower: no npm install or postinstall hook (Sonatype, JFrog take-home) and no execution on clone (Apiiro). Reword to 'no install-script hook' or drop the sweeping claim; the headline 'at build or folder open' also omits the driver-command trigger.

12. [F14] 2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (body paragraph 1): "so a guest installer is all an operator needs to register guests"
   (low confidence) Huntress says "To register, a guest client needs a ScreenConnect server's relay address, which is embedded in that server's guest installer"; it does not say the installer is all that is needed. Soften to 'carries what an operator needs' or cite.


### Editorial / less-is-more flags (advisory)

13. [F11] 2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (updates[] summary and sourcing_note): record summary: "A second action covers the keys Cursor emailed to team admins."; sourcing_note: "...and the entry follows Cursor."
   Record-keeping narration about the actions[] field in the record summary, and a composition-rationale sentence in sourcing_note ('the entry follows Cursor'); sourcing_note is also five sentences where two of provenance suffice. Drop the actions sentence from the summary and trim sourcing_note to provenance.

14. [F11] 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (techniques[]): techniques: [T1133, T1078, T1135, T1558.003, T1110, T1078.003, T1078.002, T1021.006, T1105, T1003, T1555, T1547.001, T1048, T1484.001, T1685, T1685.005, T1486]
   The body describes EtherRAT as a Node.js implant that reads its command address from an Ethereum smart contract and the report's own ATT&CK table lists T1059.007 (JavaScript), T1059.001 (PowerShell) and T1568 (Dynamic Resolution); none is mapped. techniques[] is meant to be the complete source-supported mapping. T1685 / T1685.005 are correctly the v20 successors of the source's T1562.001 / T1070.001.

15. [F11] 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (relevance framing): notable single-victim incident; no sentence says why it earns its place
   A single unnamed small-company victim with no nexus stated. The strict bar for incident entries expects the entry to say which ground it clears; the store already carries The Gentlemen entries against Swiss public-sector suppliers (entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md, entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md), so the actor-targets-the-constituency ground is available; one clause in the Defender takeaway would state it without pipeline wording. Priority notable is defensible.

16. [F11] 2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (action and Detection line): "guest version 25.3.4.9288"
   (low confidence) A claimed client version string used as a hunting key; Huntress itself lists it as 'context indicator, not unique on its own'. Borderline against the zero-IOC rule; consider describing it as 'a uniform, outdated guest client version' and keeping the literal only if the team judges it detection logic, not an indicator.

17. [F11] 2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (entities): entities: ["campaign:polinrider"]
   (low confidence) The fake-recruiter route is the registry's campaign:contagious-interview playbook (JFrog's post is titled 'Contagious Interview'; the registry already records an overlaps-with edge from this entry), yet the entry lists only campaign:polinrider. Consider adding campaign:contagious-interview so the entity page picks the entry up.


### Missed angles

None to raise. The KEV catalogue read this iteration is version 2026.11.13 (1,781 entries) with no addition after 2026-11-13, NCSC Security Hub newest posts (13178 Red Hat Quay, 13177 SignDrop, 13175 Citrix NetScaler) are already covered by entries/2026-11-14/red-hat-quay-signing-key-takeover-cve-2026-123710.md, entries/2026-11-13/signdrop-windows-clfs-authentication-lpe-public-poc-no-patch.md and the Citrix entry, and a Swiss municipal/cantonal search returned nothing newer than August 2026. The borderline-drop dispositions in the run record read as defensible, including Fortinet FG-IR-26-187 (no fix, 'Known Exploited: No' for Fortinet products per the sub-agent's read), the Quantum Systems QBase update-server item (no Swiss customer stated) and the Saxony pager item (older than the window, already dropped twice). Coverage looks complete for the critical/high signal.

Other checks that passed: classification blocks present and in vocabulary on all four entries (B/2 PolinRider, B/2 ScreenConnect single Huntress source, C/2 Gentlemen single Ransom-ISAC source, B/1 Cursor with three independent analyses); no org_triage, no watchlist, no TLP content; verification values match source counts, both single-source entries carry sourcing_note; no IOCs beyond the borderline version string noted above; no em dash outside the permitted changelog heading and one verbatim quote; no workflow vocabulary in reader-facing text beyond the Cursor items noted; first sources are vendor/research primaries; all inline URLs are specific articles; all citation dates equal the sources' own publication dates (Apiiro 2026-11-09, JFrog 2026-11-09, Sonatype 2026-11-04, StepSecurity 2026-11-13, Huntress 2026-11-14, Ransom-ISAC 2026-11-13, Cursor 2026-11-13, Fireworks 2026-11-09). Registry additions (campaign:polinrider, campaign:screenconnect-crypto-bait-sessions-2026-11, product:github) are sourced and typed correctly; campaign:ghostaction and campaign:contagious-interview relations match what Sonatype and JFrog/StepSecurity state.

### Verdict

NEEDS_FIXES (truth: 11, editorial: 1, advisory: 5)

Highest-weight items: the Gentlemen title/headline/summary state a hedged cause as fact (F4), and the PolinRider "nothing runs at install time" generalisation that the JFrog camera-driver route contradicts (F14). The ScreenConnect and Cursor items are scope and attribution tightening; most carry (low confidence). The two timestamp and run-record-id items are mechanical.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) - iteration 1, run 2026-11-15T0356Z-intel
- code: F4
  category: hallucinated-fact
  section: entry
  item: "2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (title, headline, summary)"
  url_or_quote: "headline: \"GPO locker failed on replication\"; title: \"the GPO locker lost a replication race\"; summary: \"never reached clients because of a replication race\" -- https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/"
  summary: "Hedge dropped. Ransom-ISAC says \"The locker's domain-wide mode most likely failed because of a replication race\", \"One line in the actor's deployment script most likely lost a race against replication\" and \"That mismatch is why the full deployment most likely failed on replication lag\". Title, headline and summary state the cause as established; the sourcing_note hedges only the Domain Admin step. Summary and title also state the Domain Admin hop \"through a dormant local administrator\" while the report says \"We could not prove how the elevation happened\" (body hedges correctly). Add 'likely' / 'most likely' to title, headline and summary."
- code: F4
  category: hallucinated-fact
  section: entry
  item: "2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (frontmatter sectors)"
  url_or_quote: "sectors: [technology]"
  summary: "(low confidence) The only source never names the victim's sector: it says \"a Gentlemen affiliate breached a small company\" and \"The victim's infrastructure is confidential\". 'technology' is unsupported; if the taxonomy has no neutral value, an empty list is more honest than a guessed sector."
- code: F4
  category: hallucinated-fact
  section: entry
  item: "2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers and 2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (discovered_at)"
  url_or_quote: "discovered_at: \"2026-11-15T04:36:00Z\" (ScreenConnect); discovered_at: \"2026-11-15T04:41:00Z\" (Gentlemen)"
  summary: "Both timestamps postdate the files' own last write and the clock when verification started: ScreenConnect file mtime 04:27:47Z, Gentlemen file mtime 04:32:26Z, verifier clock 04:32:53Z at start. The run record's completed: '2026-11-15T04:50:00Z' (written 04:31:19Z) and the duration_seconds 3230 derived from it are likewise ahead of the clock. Low severity (gate slack accepts it) but the values are not true when written; set them to actual write times and set completed at the real end."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-11-15/2026-11-15T0356Z-intel.md, Verification & coverage notes, 'Single-source:' line"
  url_or_quote: "2026-11-15/screenconnect-crypto-exchange-bait-guest-sessions-118-servers ... 2026-11-15/gentlemen-affiliate-vpn-no-mfa-domain-admin-gpo-locker-failed"
  summary: "The two ids do not exist. entries/2026-11-15/ holds screenconnect-crypto-bait-guest-sessions-118-servers.md and gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed.md (ls output). Correct the ids in the note."
- code: F14
  category: quantifier-without-source
  section: entry
  item: "2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 1 and summary)"
  url_or_quote: "\"Three routes share one trait: nothing runs at install time.\" / summary: \"nothing runs at install time\""
  summary: "No cited source states this generalisation for all three routes. JFrog (https://research.jfrog.com/post/accurasofthire-fake-interview/) says the camera-check route hands the candidate a command that downloads a fake 'driver' installer which runs a bootstrap and the payload (\"The code runs in the terminal\"), and the entry's own sentence says the command \"installs the same loader\"; StepSecurity lists 'when the candidate runs the \"driver\" command' as a separate execution trigger. What the sources support is narrower: no npm install or postinstall hook (Sonatype, JFrog take-home) and no execution on clone (Apiiro). Reword to 'no install-script hook' or drop the sweeping claim; the headline 'at build or folder open' also omits the driver-command trigger."
- code: F14
  category: quantifier-without-source
  section: entry
  item: "2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (body paragraph 1)"
  url_or_quote: "\"so a guest installer is all an operator needs to register guests\""
  summary: "(low confidence) Huntress says \"To register, a guest client needs a ScreenConnect server's relay address, which is embedded in that server's guest installer\"; it does not say the installer is all that is needed. Soften to 'carries what an operator needs' or cite."
- code: F3
  category: claim-not-supported
  section: entry
  item: "2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (summary)"
  url_or_quote: "\"coding errors made the SSH step fail on most standard-user hosts, so Cursor and Sophos say the attacker could not log in there\""
  summary: "(low confidence) Sophos (https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace) says only \"Due to coding errors, SSH enablement fails on most macOS and Windows hosts\"; the 'attacker could not log in' conclusion is Cursor's (\"the attacker could not have logged in through the tunnel\"). Attribute the conclusion to Cursor and the failure to both."
- code: F3
  category: claim-not-supported
  section: entry
  item: "2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (summary)"
  url_or_quote: "\"a credential from those traces let the attacker write the extension straight onto the marketplace cache\""
  summary: "(low confidence) Cursor (https://cursor.com/blog/security-incident-update) says \"using a stolen credential from the exposed data from our internal system, the attacker placed malicious, unauthorized copies ... directly on the cache\". It does not say the credential came from the traces; step 1 says the traces' credentials let the attacker reach select SaaS tools, and step 3 refers to 'the exposed data from our internal system'. The body's wording ('a credential taken through a key exposed at its vendor Fireworks') is the safer form; align the summary to it."
- code: F3
  category: claim-not-supported
  section: entry
  item: "2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 2)"
  url_or_quote: "\"1,949 repositories were infected again after being publicly listed because the stolen access still worked\""
  summary: "(low confidence) Apiiro (https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits) says \"1,949 got injection pushes after their listing date\" and, separately, \"Where owners cleaned up, the stolen access often still worked\"; it does not say all 1,949 were cleaned-up repositories or that the cause holds for each. In 553 of 2,849 repos the owner kept working on top of the loader, so many were never cleaned. Say 'often' or split the count from the cause."
- code: F3
  category: claim-not-supported
  section: entry
  item: "2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (body paragraph 2)"
  url_or_quote: "\"The loader reads the newest transaction of a hard-coded Ethereum wallet ... ([Sonatype, 2026-11-04](...))\""
  summary: "(low confidence, minor) Sonatype says the loaders \"locate a transaction sent by the hard-coded wallet\"; 'newest' is stated by Apiiro (code comment 'newest tx') and StepSecurity ('most recent transaction'), not by the Sonatype page the clause cites. Add Apiiro to the citation."
- code: F3
  category: claim-not-supported
  section: entry
  item: "2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (summary)"
  url_or_quote: "\"which an operator keeps online by revisiting the servers every 151 seconds\""
  summary: "(low confidence) Huntress: \"Across 29 servers with complete connection histories ... the operator revisited the servers every 151 seconds\". The summary applies it to all 118 servers; the body is correctly scoped to 29. Add 'on the 29 servers with complete history'."
- code: F8
  category: needs-more-research
  section: entry
  item: "2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (Defender takeaway)"
  url_or_quote: "\"in Huntress's hypothesis the target is a technician client below 26.6.5\""
  summary: "(low confidence) Huntress's first recommendation is \"MSPs should upgrade ScreenConnect host clients to 26.6.5 or later\" and, if upgrades must wait, remove TransferFiles from roles and session groups. The takeaway lists only enrolment-limiting steps and the action list omits the lever (reasonably, as the CVE-2026-84869 entry carries it); one clause stating the upgrade lever in the takeaway would let a reader act without opening the other entry."
- code: F11
  category: editorial-advisory
  section: entry
  item: "2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor (updates[] summary and sourcing_note)"
  url_or_quote: "record summary: \"A second action covers the keys Cursor emailed to team admins.\"; sourcing_note: \"...and the entry follows Cursor.\""
  summary: "Record-keeping narration about the actions[] field in the record summary, and a composition-rationale sentence in sourcing_note ('the entry follows Cursor'); sourcing_note is also five sentences where two of provenance suffice. Drop the actions sentence from the summary and trim sourcing_note to provenance."
- code: F11
  category: editorial-advisory
  section: entry
  item: "2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (techniques[])"
  url_or_quote: "techniques: [T1133, T1078, T1135, T1558.003, T1110, T1078.003, T1078.002, T1021.006, T1105, T1003, T1555, T1547.001, T1048, T1484.001, T1685, T1685.005, T1486]"
  summary: "The body describes EtherRAT as a Node.js implant that reads its command address from an Ethereum smart contract and the report's own ATT&CK table lists T1059.007 (JavaScript), T1059.001 (PowerShell) and T1568 (Dynamic Resolution); none is mapped. techniques[] is meant to be the complete source-supported mapping. T1685 / T1685.005 are correctly the v20 successors of the source's T1562.001 / T1070.001."
- code: F11
  category: editorial-advisory
  section: entry
  item: "2026-11-15/gentlemen-affiliate-vpn-no-mfa-da-gpo-locker-failed (relevance framing)"
  url_or_quote: "notable single-victim incident; no sentence says why it earns its place"
  summary: "A single unnamed small-company victim with no nexus stated. The strict bar for incident entries expects the entry to say which ground it clears; the store already carries The Gentlemen entries against Swiss public-sector suppliers (entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md, entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md), so the actor-targets-the-constituency ground is available; one clause in the Defender takeaway would state it without pipeline wording. Priority notable is defensible."
- code: F11
  category: editorial-advisory
  section: entry
  item: "2026-11-15/screenconnect-crypto-bait-guest-sessions-118-servers (action and Detection line)"
  url_or_quote: "\"guest version 25.3.4.9288\""
  summary: "(low confidence) A claimed client version string used as a hunting key; Huntress itself lists it as 'context indicator, not unique on its own'. Borderline against the zero-IOC rule; consider describing it as 'a uniform, outdated guest client version' and keeping the literal only if the team judges it detection logic, not an indicator."
- code: F11
  category: editorial-advisory
  section: entry
  item: "2026-11-15/polinrider-forged-commits-npm-hijacks-fake-recruiter (entities)"
  url_or_quote: "entities: [\"campaign:polinrider\"]"
  summary: "(low confidence) The fake-recruiter route is the registry's campaign:contagious-interview playbook (JFrog's post is titled 'Contagious Interview'; the registry already records an overlaps-with edge from this entry), yet the entry lists only campaign:polinrider. Consider adding campaign:contagious-interview so the entity page picks the entry up."
```
