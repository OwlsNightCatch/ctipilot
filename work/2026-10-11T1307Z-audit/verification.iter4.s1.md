**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T16:27:21Z · ended_at=2026-10-19T16:52:47Z · duration_seconds=1526

## Verification report — 2026-10-11T1307Z-audit (iteration 4, slice s1)

Scope: 28 entries read whole (27 audit-updated entries plus the new NeedyMantis entry); claim ledger `claims.iter4.s1.yaml`, 286 claims, 286 answered (284 ok, 2 F3; no unreadable). Publica (2026-10-09) is unchanged against HEAD, carries no record for this fire and is not in `updated_entry_ids`, so the withdrawal in the deltas holds and it has no claims. Every cited source page was fetched this iteration (bridge extract/url, `ncsc-csh post`, `cisa-kev`, `msrc cve`, `enisa-euvd advisory`, `pdf`, FIRST EPSS API); the Citrix community blog for CVE-2026-88779 and the ENISA EUVD web page returned JS shells (the EUVD record was read through its API; the Citrix blog quote belongs to the 2026-10-04 fire, not this one).

**Prior-iteration deltas walked (21 findings):** landed and correct: closedquorum F4 (hedge restored in the body quote, section clean), citrix F11 (self-reference gone), denic F3 (heise time marked as CEST reading) and the denic 05-10 'later addendum' wording, cisco F4 (06-03), rogueplanet F3/F8/F11 (cadence sentence gone, action floor 1.1.26080.3 verified on MSRC CVE-2026-69414, quotation marks dropped), gitlab F3 (foothold marked analyst judgement) and F18 (hunting action dropped), exchange F3 (TA488 clause), F4 (headline/summary) and F11 ('Russia-aligned', em dashes gone), virtualizor F18 (actions empty) and F11 (record now reader-facing with a section), dirty-frag F11 (EPSS URL carries `date=2026-09-04`, values 0.9324/0.9286 match the API), publica F11 (record withdrawn). Not landed or declined with a rationale that fails: exchange F3 on 'must' (only the title changed; the body, 07-31 section and takeaway keep 'must'/'has to'), virtualizor F7 (re-raised), cisco F11 second half (record summary still narrates the fold), denic F11 point 2 (kind: policy; advisory), gitlab F11 em dashes (advisory).

### Citation does not support the claim

1. `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — where: body para 2: 'installing either does not remove the earlier mitigation, which administrators must roll back by hand' (cited to June blog, July blog, MSRC); same strength in the 2026-07-31 section ('must remove the M2.1.0 IIS rules') and its Defender takeaway ('the mitigation has to be dismantled by hand afterwards')
   - Iteration-3 finding on 'must' stands; only the title was changed. No cited page says administrators must roll the mitigation back: the June blog recommends keeping it in place and says 'if you choose to remove mitigations after installation, you should', the July blog says 'you should', MSRC says the mitigations 'can be removed'. The sentence cites the June blog for a duty that blog contradicts. What the sources state is that the update does not remove the mitigation automatically and that Microsoft advises removing it after the July update.
   - Source: June blog: 'We recommend that customers keep CVE-2026-42897 mitigation in place ... Installing the June 2026 update does not automatically remove already applied CVE-2026-42897 mitigations. Therefore, if you choose to remove mitigations after installation, you should: ...'. July blog: 'Installing the July 2026 update does not automatically remove already applied CVE-2026-42897 mitigations. Therefore, once you install July SU, you should: ...'. MSRC: 'Mitigations that have been applied ... can be removed after July 2026 update is installed.' (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Reword to the vendors' strength: 'the update does not remove the mitigation automatically; Microsoft advises removing it after the July update (the June post advised keeping it)'; same in the 07-31 Patching paragraph and the takeaway.
2. `2026-09-12/cve-2026-85706-gitlab-unauth-path-traversal-file-read.md` — where: body para 2: 'watchTowr reproduced the vulnerability and validated exposure across client environments within roughly a day of GitLab's patch ... meaning attackers had independently reverse-engineered a working exploit within roughly 24 hours of disclosure ([watchTowr, 2026-09-11])'
   - (low confidence) The watchTowr page gives no timing for its own reproduction and exposure validation and does not say the attackers worked 'independently'. It says: 'is already seeing behavioral probes for this vulnerability against Attacker Eye ... meaning attackers have already successfully reverse engineered and reproduced the vulnerability'. 'Within roughly a day' is the entry's inference from the page date (2026-09-11) against the release date (2026-09-10), and 'independently' is added.
   - Source: watchTowr: 'watchTowr reviewed the technical details published by GitLab, reproduced the vulnerability, and validated exposure across client environments ... is already seeing behavioral probes for this vulnerability against Attacker Eye, our global honeypot network, meaning attackers have already successfully reverse engineered and reproduced the vulnerability' (https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/)
   - Fix: Drop 'independently' and mark the timing as the entry's reading of the page date, or write 'by the time of watchTowr's 2026-09-11 post, one day after the release'.
3. `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — where: ## Update 2026-07-31T04:09:14Z, **Patching.** 'organisations that were enrolled only in Period 1, which ended in April 2026, do not receive it ([Microsoft Exchange Team Blog, 2026-07-14](.../released-july-2026-exchange-server-security-updates/4534146))' (not a ledger claim)
   - (low confidence) The July 2026 post that terminates the clause says Exchange 2016 and 2019 updates 'are available only under the Period 2 ESU program' and are for customers enrolled in Period 2 for updates 'released between May and October 2026', but it does not state that Period 1 'ended in April 2026' or that Period-1-only customers do not receive the update. That sentence is on the May 2026 post (CVE-2026-42897 advisory), which is cited elsewhere in the entry but not here.
   - Source: May blog: 'Period 1 only ESU customers will not receive this update as that ESU program ended in April 2026.' July blog: 'Only customers who enrolled in the Period 2 Extended Security Update (ESU) program are eligible to receive Exchange Server 2016 and 2019 security updates released between May and October 2026.' (https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498)
   - Fix: Co-cite the May 2026 Exchange Team post for the Period 1 clause or trim the clause to what the July post states.

### Unsupported / hallucinated facts

1. `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — where: ## Update 2026-07-31T04:09:14Z, **Defender takeaway:** 'an organisation that patches, resets passwords and re-images the affected workstation can still be read indefinitely; the folder-permission audit is the part that actually evicts them'
   - (low confidence) The iteration-3 F4 removed 'outlives the patch' from the headline and summary because Proofpoint never mentions patching, but the takeaway keeps the same inference as fact. Proofpoint says the server-side grant 'requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user's device will not evict the actor'. Patching is not mentioned and neither is 'indefinitely'. The inference is logically sound (a patch does not revoke a folder permission) but is not marked as the entry's own reading.
   - Source: Proofpoint: 'This persistent access lives on the server-side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user's device will not evict the actor.' (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Reword to Proofpoint's scope ('resetting passwords and re-imaging the endpoint will not remove the grant') and add 'patching does not revoke it' as the entry's reading, or drop 'patches' and 'indefinitely'.
2. `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — where: frontmatter sectors: [public-sector, healthcare, education, telco, finance, aviation]
   - (low confidence) The frontmatter overstates the body's sources: the cited Proofpoint report and the body name government, telecommunications, finance, hospitality and aerospace targets; no cited page names healthcare or education (grep of the Proofpoint report and the three Microsoft Exchange Team posts finds none). 'Hospitality' has no taxonomy tag, so aviation is the nearest, but healthcare and education are unsupported. Unchanged by this fire but the entry was rewritten whole.
   - Source: Proofpoint: 'The campaign targeted US and European government entities, as well as the telecommunications, financial, hospitality, and aerospace sectors.' (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Drop healthcare and education from sectors (keep public-sector, telco, finance, aviation).

### Claims missing inline citation

1. `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — where: ## Update 2026-07-31T04:09:14Z: paragraphs '**Execution.**', '**Credential and token theft.**', '**Persistence, in three independent layers.**' (contains a quotation 'requires deliberate removal from the Exchange server' with no link) and '**Command and control.**'
   - (low confidence) Four technical paragraphs of OWAReaper behaviour (onload= loader, hidden icon payload, autofill harvesting, GetClientAccessToken, localStorage PageDataPayload.OwaUserDefaultSettings persistence, UpdateFolder Owner grant, GitHub Commit Search every 24 hours, five-minute cache polling, image-CDN relay and DNS fallback) carry no inline citation at all; the facts are all on the Proofpoint page (checked), so the defect is attribution only. The ledger did not list them as uncited, so earlier passes did not walk them.
   - Source: Proofpoint: 'The script queries GitHub's Commit Search API every 24 hours ... The decrypted data contains a four-character header for command type'; 'calls UpdateFolder to grant itself Owner-level permissions to the Default user ... requires deliberate removal from the Exchange server' (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Append the Proofpoint, 2026-07-29 inline citation to each of the four paragraphs (or to each clause chain); the Detection and Triage paragraphs are derived guidance and may stay uncited.
2. `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md` — where: actions[0]: '(e.g. via Get-MpComputerStatus AMEngineVersion)'
   - (low confidence) The cmdlet and property are the entry's own addition and appear on none of the cited pages (MSRC says only 'regularly verify whether ... automatic deployment ... is working'); accurate as a hint but unsourced. Advisory-level.
   - Source: MSRC CVE-2026-50656 FAQ: 'Best practices recommend that customers regularly verify whether ... automatic deployment of Microsoft Malware Protection Engine updates ... is working as expected in their environment.' (no cmdlet named) (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Either cite Microsoft's Defender documentation for Get-MpComputerStatus or drop the parenthetical.
3. `2026-05-08/amazon-ses-weaponised-for-authenticated-phishing-and-bec-kas.md` — where: **Detection:** second paragraph sentence 'On the AWS side, SES sending activity by an IAM key that has no history of sending mail is the signal for a hijacked key.'
   - (low confidence) An uncited detection claim stated as fact in a body this fire rewrote; Kaspersky's report names no such AWS-side signal. It is a sound inference, and sibling entries mark such lines ('analyst inference', 'by inference from the mechanism'), so mark it or cite the AWS documentation.
   - Source: Kaspersky says only that attackers 'verify the key's permissions and email sending limits' before sending; no AWS-side detection is described. (https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)
   - Fix: Prefix with 'By inference from the mechanism,' or drop the sentence.

### Drop (low relevance / off-audience / duplicate)

1. `2026-09-23/virtualizor-billing-hook-unauth-root-rce.md` — where: whole entry: priority: routine yet body of about 900 words of decoded code-path detail (billing_unsuspend() to vexec() to proc_open(), php-fpm pool users, MySQL 5.5.62 sql_mode, timing oracle)
   - (iteration-2/3 finding re-raised; the decline rationale does not answer check 11 / the repo rule) This fire itself rates the entry routine and says in its Correction section: 'no exploitation is reported, a vendor fix has existed since 2026-09-01, the root path needs an existing suspended billing account, and Virtualizor sits outside the typical public-administration estate'. An unexploited, six-week-patched flaw in hosting-provider billing software that is outside the constituency's estate demands no action beyond the regular cycle, so it fails the vulnerability inclusion gate (check 11) or, if kept, belongs at two sentences. The decline ('the code-path detail is VulnCheck's research the detection rests on') keeps length that a routine item should not carry; the Detection and Triage lines rest on three facts (act=login with from_billing_module and billing_data; admin ports 4084/4085; root php-fpm pool) that fit in a short paragraph.
   - Source: Entry's own Correction 2026-10-11T14:10:01Z: 'The entry moves to routine priority: no exploitation is reported, a vendor fix has existed since 2026-09-01 ... Virtualizor sits outside the typical public-administration estate.' VulnCheck post: 'the three CVEs were allocated through the VulnCheck CNA' (no exploitation statement) (https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)
   - Fix: Cut the main analysis to the exposure, the fixed builds, the exploitation status, the detection signature and the takeaway (about 150 words), or fold the entry out if the audit judges it below the gate.

### Needs more research

1. `2026-05-09/cve-2026-43284-cve-2026-43500-linux-dirty-frag-deterministic.md` — where: main analysis (this fire's rewritten body): ends at '**Detection:**'; no '**Exposure:**' and no '**Defender takeaway:**' line
   - The body carries a Detection line only. The actionability contract requires a Defender takeaway on every entry and an Exposure line where sources support it; the cited sources clearly support both (ESP flaw needs user-namespace creation, RxRPC needs the rxrpc module which Ubuntu loads by default, kernel update fixes both, module block is the interim, CVE-2026-46300 follow-on must also be fixed on RHEL). The priority is high, so the missing decision line matters most here.
   - Source: Ubuntu: 'Linux kernel package updates are available that fix these vulnerabilities ... mitigations ... only if that is not possible'; Red Hat RHSB-2026-003: 'both vulnerabilities can be mitigated by disabling unprivileged user namespaces'; README: rxrpc.ko 'on Ubuntu ... loaded by default' (https://ubuntu.com/blog/dirty-frag-linux-vulnerability-fixes-available)
   - Fix: Add a short **Exposure:** line (who is affected: any Linux kernel from 2017 (ESP) / 2023 (RxRPC) until fixed; ESP needs unprivileged user-namespace creation; RxRPC needs the rxrpc module; not RHEL for CVE-2026-43500) and a **Defender takeaway:** line (install the distribution kernel update, confirm the CVE-2026-46300 fix on RHEL; module block only where an update cannot be installed), each inline-cited.

### Editorial / less-is-more flags (advisory)

1. `2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.md` — where: frontmatter kind: policy (low confidence, advisory; restates iteration-3 point 2, declined as a stopgap)
   - (low confidence) kind: policy is defined in site/taxonomy.yaml as 'a regulatory action, deadline or authority guidance that changes what the constituency is obliged or advised to do'; a non-adversarial registry outage post-mortem is not that. The rationale (stopgap because incident would need techniques) is a rule workaround, not a fit.
   - Source: site/taxonomy.yaml line 41: 'kind: policy -- a regulatory action, deadline or authority guidance that changes what the constituency is obliged or advised to do.'
   - Fix: Advisory; may be left. If a better-fitting kind exists without a technique requirement (research), consider it, else leave.
2. `2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary.md` — where: updates[2026-10-11T14:48:28Z].summary: '... absorbing the separate disclosure-day entry, plus the KEV and vendor confirmation ...'; sources[0].date 2026-07-01 (low confidence, advisory)
   - (low confidence) The iteration-3 point on the record summary was not answered: the decline rationale addresses only the sources[0] date. The record summary still narrates the fold ('absorbing the separate disclosure-day entry'), which is pipeline bookkeeping rather than the reader-facing delta (4c(d)); sources[0] still carries the 2026-07-01 revision date while the advisory's initial public release is 2026-06-03 (the body discloses both dates, so this is minor).
   - Source: Cisco advisory revision table: '1.1 Added information about active exploitation ... 2026-JUL-01; 1.0 Initial public release ... 2026-JUN-03' (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
   - Fix: Advisory; drop 'absorbing the separate disclosure-day entry' from the record summary (merged_from already records the fold). The source date may stay.
3. `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md` — where: ## Correction 2026-10-11T14:55:23Z: ShieldBreak fix build stated twice ('Microsoft lists engine 1.1.26080.3 as the first build that addresses it' and, two sentences later, 'Microsoft lists Malware Protection Engine 1.1.26080.3 as the first build that addresses the ShieldBreak bypass'); also 'The priority moves from notable to routine' (record-keeping about metadata); em dashes in title and in body paragraph 1 ('closes it — last vulnerable')
   - Advisory. The section repeats the same cited fact twice back to back (a fix-up residue from the iteration-3 edit), narrates a priority change as reader text, and the title and first body paragraph still contain em dashes (rule 12).
   - Source: MSRC CVE-2026-69414: 'First version of the Microsoft Malware Protection Engine with this vulnerability addressed | 1.1.26080.3' (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
   - Fix: Delete the second ShieldBreak sentence; drop the priority sentence or make the record internal for it; replace the em dashes.
4. `2026-09-24/closedquorum-llm-orchestrated-c2-implant.md (also gitlab 09-12, rogueplanet 07-09, and the titles of fortisandbox 06-12, chrome-v8 09-04, acronis 09-18)` — where: em dashes in reader-facing text: closedquorum summary (2) and body (5: 'providers — DeepSeek', 'mechanisms — a Windows-Update-themed', 'effort displacement" — an entire', 'action — but its architecture' and one more); gitlab body (2, 09-16 section); rogueplanet body (1) and title; titles of fortisandbox, chrome-v8, acronis, gitlab, rogueplanet
   - Advisory (low priority; the iteration-3 advisory stands for these entries). Rule 12 allows the em dash only in the section heading. The site strips them at render and the gate checks only new text; the closedquorum body and summary were edited in place this fire, so they are in scope.
   - Fix: Replace with commas, colons or parentheses in the text this fire rewrote; titles may be left.
5. `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md; 2026-09-23/virtualizor-billing-hook-unauth-root-rce.md; 2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence.md` — where: reader-facing Correction sections: 'The priority moves from notable to routine: the flaw is local and the engine fix installs automatically.' (RoguePlanet); 'The entry moves to routine priority: no exploitation is reported ...' (Virtualizor); 'so the entry no longer presents the campaign as conference-targeted' (conference-phishing)
   - Advisory. These sentences narrate a change to the entry's own metadata (priority, framing) as reader text; rule 4c(i)/12 reserve that for an internal record or for a section that tells the reader what changed in the finding. Each section has other reader-facing content, so the sentence can simply be dropped.
   - Fix: Delete the priority/framing sentence from each section (the priority is visible in the entry header).

### Observations outside this slice (not counted)

- `python3 tools/check_run.py 2026-10-11T1307Z-audit --pre-verify` run just now (read-only) reports 1 FAIL and 1 WARN: `run-clock` (record `completed` 16:38:52Z precedes verification iteration 3 `ended_at` 17:21:22Z; the record needs re-stamping at the end of the loop) and `entry-run-binding` (Citrix `updates[].at` 2026-10-19T16:17:18Z outside the run window). Both are run-record matters for the main agent/s6; the Citrix record itself is correct and carries a genuine delta (CCB 2026-10-06 PoC, checked on the CCB page).
- No missed-angle finding for this slice; the recovered NeedyMantis entry matches the Microsoft post (2026-09-28) and its registry entities and DAEMON Tools reference exist.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 5, advisory: 5)

Truth = 3x F3 (Exchange 'must' 87dc39aa73, Exchange Period-1 clause cited to the wrong post, GitLab 'independently' 5f02971c75 low confidence) + 2x F4 (Exchange takeaway inference, Exchange sectors; both low confidence). Editorial = F8 Dirty Frag, F7 Virtualizor, 3x F5 (Exchange uncited 07-31 paragraphs, RoguePlanet cmdlet, SES inference; all low confidence). Advisory = 5x F11.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  entry: entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md
  where: 'body para 2: ''installing either does not remove the earlier mitigation, which administrators must roll back by hand'' (cited to June blog, July blog, MSRC); same strength in the 2026-07-31 section
    (''must remove the M2.1.0 IIS rules'') and its Defender takeaway (''the mitigation has to be dismantled by hand afterwards'')'
  summary: 'Iteration-3 finding on ''must'' stands; only the title was changed. No cited page says administrators must roll the mitigation back: the June blog recommends keeping it in place and says ''if
    you choose to remove mitigations after installation, you should'', the July blog says ''you should'', MSRC says the mitigations ''can be removed''. The sentence cites the June blog for a duty that blog
    contradicts. What the sources state is that the update does not remove the mitigation automatically and that Microsoft advises removing it after the July update.'
  ground_truth: 'June blog: ''We recommend that customers keep CVE-2026-42897 mitigation in place ... Installing the June 2026 update does not automatically remove already applied CVE-2026-42897 mitigations.
    Therefore, if you choose to remove mitigations after installation, you should: ...''. July blog: ''Installing the July 2026 update does not automatically remove already applied CVE-2026-42897 mitigations.
    Therefore, once you install July SU, you should: ...''. MSRC: ''Mitigations that have been applied ... can be removed after July 2026 update is installed.'''
  ground_truth_url: https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491
  fix: 'Reword to the vendors'' strength: ''the update does not remove the mitigation automatically; Microsoft advises removing it after the July update (the June post advised keeping it)''; same in the
    07-31 Patching paragraph and the takeaway.'
- code: F3
  category: claim-not-supported
  entry: entries/2026-09-12/cve-2026-85706-gitlab-unauth-path-traversal-file-read.md
  where: 'body para 2: ''watchTowr reproduced the vulnerability and validated exposure across client environments within roughly a day of GitLab''s patch ... meaning attackers had independently reverse-engineered
    a working exploit within roughly 24 hours of disclosure ([watchTowr, 2026-09-11])'''
  summary: '(low confidence) The watchTowr page gives no timing for its own reproduction and exposure validation and does not say the attackers worked ''independently''. It says: ''is already seeing behavioral
    probes for this vulnerability against Attacker Eye ... meaning attackers have already successfully reverse engineered and reproduced the vulnerability''. ''Within roughly a day'' is the entry''s inference
    from the page date (2026-09-11) against the release date (2026-09-10), and ''independently'' is added.'
  ground_truth: 'watchTowr: ''watchTowr reviewed the technical details published by GitLab, reproduced the vulnerability, and validated exposure across client environments ... is already seeing behavioral
    probes for this vulnerability against Attacker Eye, our global honeypot network, meaning attackers have already successfully reverse engineered and reproduced the vulnerability'''
  ground_truth_url: https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/
  fix: Drop 'independently' and mark the timing as the entry's reading of the page date, or write 'by the time of watchTowr's 2026-09-11 post, one day after the release'.
- code: F3
  category: claim-not-supported
  entry: entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md
  where: '## Update 2026-07-31T04:09:14Z, **Patching.** ''organisations that were enrolled only in Period 1, which ended in April 2026, do not receive it ([Microsoft Exchange Team Blog, 2026-07-14](.../released-july-2026-exchange-server-security-updates/4534146))''
    (not a ledger claim)'
  summary: (low confidence) The July 2026 post that terminates the clause says Exchange 2016 and 2019 updates 'are available only under the Period 2 ESU program' and are for customers enrolled in Period
    2 for updates 'released between May and October 2026', but it does not state that Period 1 'ended in April 2026' or that Period-1-only customers do not receive the update. That sentence is on the May
    2026 post (CVE-2026-42897 advisory), which is cited elsewhere in the entry but not here.
  ground_truth: 'May blog: ''Period 1 only ESU customers will not receive this update as that ESU program ended in April 2026.'' July blog: ''Only customers who enrolled in the Period 2 Extended Security
    Update (ESU) program are eligible to receive Exchange Server 2016 and 2019 security updates released between May and October 2026.'''
  ground_truth_url: https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498
  fix: Co-cite the May 2026 Exchange Team post for the Period 1 clause or trim the clause to what the July post states.
- code: F4
  category: hallucinated-fact
  entry: entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md
  where: '## Update 2026-07-31T04:09:14Z, **Defender takeaway:** ''an organisation that patches, resets passwords and re-images the affected workstation can still be read indefinitely; the folder-permission
    audit is the part that actually evicts them'''
  summary: (low confidence) The iteration-3 F4 removed 'outlives the patch' from the headline and summary because Proofpoint never mentions patching, but the takeaway keeps the same inference as fact. Proofpoint
    says the server-side grant 'requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user's device will not evict the actor'. Patching is not
    mentioned and neither is 'indefinitely'. The inference is logically sound (a patch does not revoke a folder permission) but is not marked as the entry's own reading.
  ground_truth: 'Proofpoint: ''This persistent access lives on the server-side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user''s
    device will not evict the actor.'''
  ground_truth_url: https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit
  fix: Reword to Proofpoint's scope ('resetting passwords and re-imaging the endpoint will not remove the grant') and add 'patching does not revoke it' as the entry's reading, or drop 'patches' and 'indefinitely'.
- code: F4
  category: hallucinated-fact
  entry: entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md
  where: 'frontmatter sectors: [public-sector, healthcare, education, telco, finance, aviation]'
  summary: '(low confidence) The frontmatter overstates the body''s sources: the cited Proofpoint report and the body name government, telecommunications, finance, hospitality and aerospace targets; no
    cited page names healthcare or education (grep of the Proofpoint report and the three Microsoft Exchange Team posts finds none). ''Hospitality'' has no taxonomy tag, so aviation is the nearest, but
    healthcare and education are unsupported. Unchanged by this fire but the entry was rewritten whole.'
  ground_truth: 'Proofpoint: ''The campaign targeted US and European government entities, as well as the telecommunications, financial, hospitality, and aerospace sectors.'''
  ground_truth_url: https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit
  fix: Drop healthcare and education from sectors (keep public-sector, telco, finance, aviation).
- code: F5
  category: missing-citation
  entry: entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md
  where: '## Update 2026-07-31T04:09:14Z: paragraphs ''**Execution.**'', ''**Credential and token theft.**'', ''**Persistence, in three independent layers.**'' (contains a quotation ''requires deliberate
    removal from the Exchange server'' with no link) and ''**Command and control.**'''
  summary: (low confidence) Four technical paragraphs of OWAReaper behaviour (onload= loader, hidden icon payload, autofill harvesting, GetClientAccessToken, localStorage PageDataPayload.OwaUserDefaultSettings
    persistence, UpdateFolder Owner grant, GitHub Commit Search every 24 hours, five-minute cache polling, image-CDN relay and DNS fallback) carry no inline citation at all; the facts are all on the Proofpoint
    page (checked), so the defect is attribution only. The ledger did not list them as uncited, so earlier passes did not walk them.
  ground_truth: 'Proofpoint: ''The script queries GitHub''s Commit Search API every 24 hours ... The decrypted data contains a four-character header for command type''; ''calls UpdateFolder to grant itself
    Owner-level permissions to the Default user ... requires deliberate removal from the Exchange server'''
  ground_truth_url: https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit
  fix: Append the Proofpoint, 2026-07-29 inline citation to each of the four paragraphs (or to each clause chain); the Detection and Triage paragraphs are derived guidance and may stay uncited.
- code: F5
  category: missing-citation
  entry: entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md
  where: 'actions[0]: ''(e.g. via Get-MpComputerStatus AMEngineVersion)'''
  summary: (low confidence) The cmdlet and property are the entry's own addition and appear on none of the cited pages (MSRC says only 'regularly verify whether ... automatic deployment ... is working');
    accurate as a hint but unsourced. Advisory-level.
  ground_truth: 'MSRC CVE-2026-50656 FAQ: ''Best practices recommend that customers regularly verify whether ... automatic deployment of Microsoft Malware Protection Engine updates ... is working as expected
    in their environment.'' (no cmdlet named)'
  ground_truth_url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656
  fix: Either cite Microsoft's Defender documentation for Get-MpComputerStatus or drop the parenthetical.
- code: F5
  category: missing-citation
  entry: entries/2026-05-08/amazon-ses-weaponised-for-authenticated-phishing-and-bec-kas.md
  where: '**Detection:** second paragraph sentence ''On the AWS side, SES sending activity by an IAM key that has no history of sending mail is the signal for a hijacked key.'''
  summary: (low confidence) An uncited detection claim stated as fact in a body this fire rewrote; Kaspersky's report names no such AWS-side signal. It is a sound inference, and sibling entries mark such
    lines ('analyst inference', 'by inference from the mechanism'), so mark it or cite the AWS documentation.
  ground_truth: Kaspersky says only that attackers 'verify the key's permissions and email sending limits' before sending; no AWS-side detection is described.
  ground_truth_url: https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/
  fix: Prefix with 'By inference from the mechanism,' or drop the sentence.
- code: F7
  category: drop
  entry: entries/2026-09-23/virtualizor-billing-hook-unauth-root-rce.md
  where: 'whole entry: priority: routine yet body of about 900 words of decoded code-path detail (billing_unsuspend() to vexec() to proc_open(), php-fpm pool users, MySQL 5.5.62 sql_mode, timing oracle)'
  summary: '(iteration-2/3 finding re-raised; the decline rationale does not answer check 11 / the repo rule) This fire itself rates the entry routine and says in its Correction section: ''no exploitation
    is reported, a vendor fix has existed since 2026-09-01, the root path needs an existing suspended billing account, and Virtualizor sits outside the typical public-administration estate''. An unexploited,
    six-week-patched flaw in hosting-provider billing software that is outside the constituency''s estate demands no action beyond the regular cycle, so it fails the vulnerability inclusion gate (check
    11) or, if kept, belongs at two sentences. The decline (''the code-path detail is VulnCheck''s research the detection rests on'') keeps length that a routine item should not carry; the Detection and
    Triage lines rest on three facts (act=login with from_billing_module and billing_data; admin ports 4084/4085; root php-fpm pool) that fit in a short paragraph.'
  ground_truth: 'Entry''s own Correction 2026-10-11T14:10:01Z: ''The entry moves to routine priority: no exploitation is reported, a vendor fix has existed since 2026-09-01 ... Virtualizor sits outside
    the typical public-administration estate.'' VulnCheck post: ''the three CVEs were allocated through the VulnCheck CNA'' (no exploitation statement)'
  ground_truth_url: https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce
  fix: Cut the main analysis to the exposure, the fixed builds, the exploitation status, the detection signature and the takeaway (about 150 words), or fold the entry out if the audit judges it below the
    gate.
- code: F8
  category: needs-more-research
  entry: entries/2026-05-09/cve-2026-43284-cve-2026-43500-linux-dirty-frag-deterministic.md
  where: 'main analysis (this fire''s rewritten body): ends at ''**Detection:**''; no ''**Exposure:**'' and no ''**Defender takeaway:**'' line'
  summary: The body carries a Detection line only. The actionability contract requires a Defender takeaway on every entry and an Exposure line where sources support it; the cited sources clearly support
    both (ESP flaw needs user-namespace creation, RxRPC needs the rxrpc module which Ubuntu loads by default, kernel update fixes both, module block is the interim, CVE-2026-46300 follow-on must also be
    fixed on RHEL). The priority is high, so the missing decision line matters most here.
  ground_truth: 'Ubuntu: ''Linux kernel package updates are available that fix these vulnerabilities ... mitigations ... only if that is not possible''; Red Hat RHSB-2026-003: ''both vulnerabilities can
    be mitigated by disabling unprivileged user namespaces''; README: rxrpc.ko ''on Ubuntu ... loaded by default'''
  ground_truth_url: https://ubuntu.com/blog/dirty-frag-linux-vulnerability-fixes-available
  fix: 'Add a short **Exposure:** line (who is affected: any Linux kernel from 2017 (ESP) / 2023 (RxRPC) until fixed; ESP needs unprivileged user-namespace creation; RxRPC needs the rxrpc module; not RHEL
    for CVE-2026-43500) and a **Defender takeaway:** line (install the distribution kernel update, confirm the CVE-2026-46300 fix on RHEL; module block only where an update cannot be installed), each inline-cited.'
- code: F11
  category: editorial-advisory
  entry: entries/2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.md
  where: 'frontmatter kind: policy (low confidence, advisory; restates iteration-3 point 2, declined as a stopgap)'
  summary: '(low confidence) kind: policy is defined in site/taxonomy.yaml as ''a regulatory action, deadline or authority guidance that changes what the constituency is obliged or advised to do''; a non-adversarial
    registry outage post-mortem is not that. The rationale (stopgap because incident would need techniques) is a rule workaround, not a fit.'
  ground_truth: 'site/taxonomy.yaml line 41: ''kind: policy -- a regulatory action, deadline or authority guidance that changes what the constituency is obliged or advised to do.'''
  ground_truth_url: ''
  fix: Advisory; may be left. If a better-fitting kind exists without a technique requirement (research), consider it, else leave.
- code: F11
  category: editorial-advisory
  entry: entries/2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary.md
  where: 'updates[2026-10-11T14:48:28Z].summary: ''... absorbing the separate disclosure-day entry, plus the KEV and vendor confirmation ...''; sources[0].date 2026-07-01 (low confidence, advisory)'
  summary: '(low confidence) The iteration-3 point on the record summary was not answered: the decline rationale addresses only the sources[0] date. The record summary still narrates the fold (''absorbing
    the separate disclosure-day entry''), which is pipeline bookkeeping rather than the reader-facing delta (4c(d)); sources[0] still carries the 2026-07-01 revision date while the advisory''s initial public
    release is 2026-06-03 (the body discloses both dates, so this is minor).'
  ground_truth: 'Cisco advisory revision table: ''1.1 Added information about active exploitation ... 2026-JUL-01; 1.0 Initial public release ... 2026-JUN-03'''
  ground_truth_url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW
  fix: Advisory; drop 'absorbing the separate disclosure-day entry' from the record summary (merged_from already records the fold). The source date may stay.
- code: F11
  category: editorial-advisory
  entry: entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md
  where: '## Correction 2026-10-11T14:55:23Z: ShieldBreak fix build stated twice (''Microsoft lists engine 1.1.26080.3 as the first build that addresses it'' and, two sentences later, ''Microsoft lists
    Malware Protection Engine 1.1.26080.3 as the first build that addresses the ShieldBreak bypass''); also ''The priority moves from notable to routine'' (record-keeping about metadata); em dashes in title
    and in body paragraph 1 (''closes it — last vulnerable'')'
  summary: Advisory. The section repeats the same cited fact twice back to back (a fix-up residue from the iteration-3 edit), narrates a priority change as reader text, and the title and first body paragraph
    still contain em dashes (rule 12).
  ground_truth: 'MSRC CVE-2026-69414: ''First version of the Microsoft Malware Protection Engine with this vulnerability addressed | 1.1.26080.3'''
  ground_truth_url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414
  fix: Delete the second ShieldBreak sentence; drop the priority sentence or make the record internal for it; replace the em dashes.
- code: F11
  category: editorial-advisory
  entry: entries/2026-09-24/closedquorum-llm-orchestrated-c2-implant.md (also gitlab 09-12, rogueplanet 07-09, and the titles of fortisandbox 06-12, chrome-v8 09-04, acronis 09-18)
  where: 'em dashes in reader-facing text: closedquorum summary (2) and body (5: ''providers — DeepSeek'', ''mechanisms — a Windows-Update-themed'', ''effort displacement" — an entire'', ''action — but
    its architecture'' and one more); gitlab body (2, 09-16 section); rogueplanet body (1) and title; titles of fortisandbox, chrome-v8, acronis, gitlab, rogueplanet'
  summary: Advisory (low priority; the iteration-3 advisory stands for these entries). Rule 12 allows the em dash only in the section heading. The site strips them at render and the gate checks only new
    text; the closedquorum body and summary were edited in place this fire, so they are in scope.
  ground_truth: ''
  ground_truth_url: ''
  fix: Replace with commas, colons or parentheses in the text this fire rewrote; titles may be left.
- code: F11
  category: editorial-advisory
  entry: entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md; entries/2026-09-23/virtualizor-billing-hook-unauth-root-rce.md; entries/2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence.md
  where: 'reader-facing Correction sections: ''The priority moves from notable to routine: the flaw is local and the engine fix installs automatically.'' (RoguePlanet); ''The entry moves to routine priority:
    no exploitation is reported ...'' (Virtualizor); ''so the entry no longer presents the campaign as conference-targeted'' (conference-phishing)'
  summary: Advisory. These sentences narrate a change to the entry's own metadata (priority, framing) as reader text; rule 4c(i)/12 reserve that for an internal record or for a section that tells the reader
    what changed in the finding. Each section has other reader-facing content, so the sentence can simply be dropped.
  ground_truth: ''
  ground_truth_url: ''
  fix: Delete the priority/framing sentence from each section (the priority is visible in the entry header).
```
