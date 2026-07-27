**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-27T03:16:50Z · ended_at=2026-07-27T03:22:06Z · duration_seconds=316

## Verification report — 2026-07-27T0110Z-weekly (iteration 8, cap, confirmation pass)

Cold read of all 9 strategic entries + run record. This was to be the confirming pass on iteration 7's CLEAN (Opus). ~14 source URLs independently fetched this iteration (WebFetch + `tools/fetch_source.py` bridge/jina where hosts redirected or paywalled).

### Independently re-verified this iteration (confirmed)

- **OpenAI page** (`openai.com/index/hugging-face-model-evaluation-security-incident/`) — 403'd on direct WebFetch, recovered via jina bridge. Verbatim: "To gain access, the models identified and exploited a zero-day vulnerability (which we've now responsibly disclosed to the vendor) in the package registry cache proxy." CONFIRMED. Page also links out to the Hugging Face post, confirming the two-way citation chain the entry describes.
- **Hugging Face blog** — verbatim "We do not know which model powered the attacker's agents, whether a jailbroken hosted model or an unrestricted open-weight one" (fuller sentence continues "; either way, the attacker was bound by no usage policy…" — entry quote ends the clause with a period rather than the source's semicolon; a truncation convention, not a meaning change, not flagged). CONFIRMED.
- **Trend Micro** — verbatim "By their account, a large language model (LLM) agent broke into a live production system, harvested credentials, moved deeper, encrypted a database, destroyed the originals, and left a ransom note." The "first documented fully-autonomous ransomware" framing is directly source-supported ("the first agentic ransomware", "for the first time", title itself: "What the First Autonomous Ransomware Case Confirms"). CONFIRMED, F14 clears.
- **CISA AA26-204A** (fetched in full via bridge, 869 lines) — 16 co-sealing/authoring agencies confirmed (US NSA/FBI/CISA/DCSA/DC3/Treasury/NCIS + AU/CA/NZ/UK/CZ/DK/EE/FI(×2)/FR(×2)/IT(×2)/MD/PL(×2)/ES/SE = 16 nations). CVE-2025-66376, Ulej/Flowerbed tooling, GAL/2FA/90-day-mail/Application Passcode exfiltration all confirmed verbatim in the technical-details section.
- **ANCPI go4it.ro page** — all three Romanian evidence quotes re-confirmed verbatim substrings. No backup-destruction or failed-extortion claim anywhere on the page. CONFIRMED absent (fourth independent re-check across the loop).
- **KELA ByteToBreach page** — confirmed: ANCPI breach claim, e-Terra/RENNS source-code theft via GitLab compromise, ransomware deployment — all the operator's own claims, no backup-destruction/extortion-failure language. Matches the entry's careful "operator's own claim" framing. CONFIRMED.
- **24 heures (BravoX)** — datePublished 2026-07-23T12:21:01+02:00 matches the citation date; verbatim "une quinzaine de communes du Nord vaudois" and "le conseiller d'État vaudois Vassilis Venizelos", plus BravoX / 220 GB / 100'000 dossiers. The iter-6 remediation (re-pointing this clause from Le Temps to 24 heures) holds. CONFIRMED.
- **ICTjournal (DragonForce → IFAGE)** — verbatim "Le groupe cybercriminel DragonForce affirme avoir dérobé 850 gigaoctets de données à l'Ifage et réclame désormais une rançon," dated 2026-07-17, matching the entry's citation. CONFIRMED (iter-4 remediation holds).
- **Ransomware.live (INC Ransom → Autismuslink)** — listing shows group slug "Incransom" (the site's no-space group-tag convention for the same actor commonly written "INC Ransom" elsewhere), victim autismuslink.ch, dated 2026-07-24. Same actor, cosmetic slug difference only — not a defect. CONFIRMED (iter-4 remediation holds).

### New finding this iteration

**F3 — citation does not support the claim.** Entry: `weekly-w30-self-hosted-webmail-russian-half-click-killzone`. The entry asserts, in three places, that the Zimbra "ZimbraWeb" application-specific password created by LAUNDRY BEAR **survives a user password reset**, and cites this specifically to Proofpoint:

- Headline: "…persistence surviving the patch."
- Summary: "…to mint an IMAP application passcode that survives both the patch and a password reset."
- Body: "Proofpoint's mechanics write-up adds the persistence detail the advisory understated: the campaign mints a 'ZimbraWeb' application-specific password via the SOAP API that survives both a user password reset and the CVE-2025-66376 patch ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits))."
- Body, defender takeaway: "…because the joint advisory and Proofpoint both document persistence that outlives the patch."

I fetched the cited Proofpoint TA488 page directly and asked specifically whether it makes this claim. Its answer: **"The page does NOT state that the ZimbraWeb app-specific password survives password resets or CVE patching."** The page's actual text on the app password is: "ZimReaper also uses CreateAppSpecificPasswordRequest to set up an app-specific password under the name 'ZimbraWeb' for persistent access to the mailserver. This password allows attacker access via IMAP, POP3, or SMTP without needing two-factor authentication…" — i.e. it documents the password's *function* (2FA-bypassing persistent mailbox access), not that it *survives a password reset or the patch*.

I then fetched CISA AA26-204A in full (869 lines, the entry's other candidate source for this claim) and grepped it for "reset" — **zero matches anywhere in the advisory.** The advisory's mitigation section (line ~398) separately recommends "All users from the organization should have all Application Passcodes and 2FA scratch keys revoked. Affected organizations should require all employees to change passwords…" — two parallel remediation actions, standard IR hygiene, but the advisory never states or implies that the passcode specifically *outlives* a password change; it just recommends doing both.

So: **none of the entry's six cited sources contains the "survives a password reset" claim**, despite the body explicitly asserting "the joint advisory and Proofpoint both document" it. The "survives…the patch" half is a defensible logical inference (an XSS patch has no mechanism to revoke a previously-created, unrelated stored credential) and I would not flag it alone, but the sentence bundles it with the unsupported "survives a password reset" claim and attributes both to sources that document neither in those terms. This is exactly the residual-defect shape the audit calls out — a plausible, probably-true operational claim asserted as if the cited page states it, when it does not.

**Remediation suggestion:** soften the three instances to what the sources actually support — e.g., "the campaign mints a 'ZimbraWeb' application-specific password via the SOAP API for persistent IMAP/POP3/SMTP access that bypasses 2FA (Proofpoint) — a credential CISA's advisory instructs be separately revoked, independent of patching or password changes (AA26-204A)" — and drop the "the joint advisory and Proofpoint both document persistence that outlives the patch" framing, since neither source uses that language.

### Editorial (spot-checked, no new findings)

- Priority calibration (4 high / 5 notable / 0 critical), Admiralty codes, W-PD-1 lens, empty `actions[]` on all 9, single-source flagging on the Iran entry, name-collision handling (SANDWORM_MODE vs Sandworm/SANDWORM RELIC) — all re-checked against the entries read this iteration and found consistent with prior iterations' conclusions; no new editorial defect found.
- Coverage vs `week-review.json`: no missing in-window strategic angle identified.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0) — the loop is at the 8-iteration cap. Per the fail-open safety valve, this run publishes with the finding above logged as residual (`verification_residual_count: 1`). This is the first time this specific clause's factual support was independently checked against both of its candidate sources word-for-word (iteration 7 reasoned about it without a fresh fetch of the CISA advisory's exact wording); the underlying persistence *mechanism* is real and well-sourced, only the "survives a password reset" specific attribution is unsupported by any cited source.

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w30-self-hosted-webmail-russian-half-click-killzone"
  url_or_quote: "\"…mints a 'ZimbraWeb' application-specific password via the SOAP API that survives both a user password reset and the CVE-2025-66376 patch\" (headline/summary/body, cited to Proofpoint https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits and to the body's claim that 'the joint advisory and Proofpoint both document persistence that outlives the patch')"
  summary: "Neither the cited Proofpoint TA488 page nor CISA AA26-204A (grepped in full, zero matches for 'reset') states that the ZimbraWeb application passcode survives a password reset. Proofpoint's page only documents the password's 2FA-bypassing function, not its survival through remediation actions. The 'survives the patch' half is a defensible inference; 'survives a password reset' and the claim that both sources 'document' this are unsupported."
```
