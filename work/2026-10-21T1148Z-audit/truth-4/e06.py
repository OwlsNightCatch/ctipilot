import sys; sys.path.insert(0,'/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4')
from rec import save
B='work/2026-10-21T1148Z-audit/truth-4/bodies/'
SA='https://www.drupal.org/sa-core-2026-004'; PSA='https://www.drupal.org/psa-2026-05-18'; NC='https://security-hub.ncsc.admin.ch/#/posts/12584'
RISK='https://www.drupal.org/drupal-security-team/security-risk-levels-defined'
THN='https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html'
REG='https://www.theregister.com/security/2026/05/19/drupal-warns-admins-to-brace-for-highly-critical-core-patch/5242728'
d={
'entry':'2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00',
'verdict':'factual-error',
'defects':[
 {'where':'immediate_action.action; body paragraph 1',
  'claim':'"highly critical" (20/25 on Drupal\'s own scale, the second-highest tier)',
  'defect':'Highly critical (20-25) is Drupal\'s top tier.',
  'ground_truth':'Drupal risk levels page: "20 to 25 is considered Highly Critical"; "15 to 19 is considered Critical"; PSA: "Highly critical 20 / 25 AC:None/A:None/CI:All/II:All/E:Theoretical/TD:Uncommon".',
  'ground_truth_url':RISK,
  'fix':'"20/25, Drupal\'s highest tier (Highly critical)".',
  'class':'factual-error'},
 {'where':'immediate_action.action; body paragraph 1 last sentences; summary',
  'claim':'All current branches (10.5.x, 10.6.x, 11.2.x, 11.3.x) plus emergency manual patches for EOL 8.9 / 9.5 / 10.4 / 11.1 are in scope. / plus EOL 8.9 / 9.5 / 10.4 / 11.1 patch files.',
  'defect':'Only 8.9 and 9.5 receive manual patch files. EOL minors 11.1/11.0 and 10.4 and earlier get security releases, with an instruction to be on at least 11.1.9 / 10.4.9 before the window.',
  'ground_truth':'PSA: "we will provide patch files for Drupal 8.9 and 9.5" and "These patches must be applied manually."; "Sites on Drupal 11.1 or 11.0 should update to at least Drupal 11.1.9." and "Sites on Drupal 10.4, 10.3, 10.2, 10.1, or 10.0 should update to at least Drupal 10.4.9."',
  'ground_truth_url':PSA,
  'fix':'"Supported branches 11.3.x, 11.2.x, 10.6.x, 10.5.x get the release; EOL 11.1.x/10.4.x get releases (be on 11.1.9/10.4.9 beforehand); Drupal 8.9 and 9.5 get manually applied patch files."',
  'class':'factual-error'},
 {'where':'body paragraph 1, last sentence',
  'claim':'No technical mitigation exists pre-patch.',
  'defect':'The PSA states the issue is protected by Drupal Steward, and trade press reports Steward customers were protected against known attack vectors.',
  'ground_truth':'PSA: "This issue is being protected by Drupal Steward." The Register: "sites using Drupal Steward, its paid web application firewall service, are protected against known attack vectors".',
  'ground_truth_url':PSA,
  'fix':'"Drupal Steward (paid WAF) protects known vectors; mitigation details follow in the advisory."',
  'class':'factual-error'},
 {'where':'summary; immediate_action.action; body paragraph 1',
  'claim':'exploits expected within hours / the Team has explicitly warned that exploits may surface within hours of release',
  'defect':'The PSA says "might be developed within hours or days"; "expected within hours" and the NCSC.ch citation overstate and drop "or days".',
  'ground_truth':'PSA (via THN/Register): "The Drupal Security Team urges you to reserve time for core updates at that time because exploits might be developed within hours or days."',
  'ground_truth_url':THN,
  'fix':'Quote the PSA sentence as is; cite NCSC.ch only for "exploits may be developed shortly after the disclosure".',
  'class':'imprecision'},
 {'where':'event_date',
  'claim':'event_date: 2026-05-19',
  'defect':'The primary source (PSA) is dated 2026-05-18; 2026-05-19 is the press and NCSC.ch date.',
  'ground_truth':'PSA: "Date: 2026-May-18"; BSI WID-SEC-2026-1579 initial release 2026-05-18.',
  'ground_truth_url':PSA,
  'fix':'event_date: 2026-05-18',
  'class':'imprecision'},
 {'where':'summary (last sentence); whole entry (twin and stale)',
  'claim':'See Immediate Action callout below and § 6.',
  'defect':'Pipeline self-reference to the v2 brief layout. The entry is the brief\'s Immediate Action callout of the same finding the survivor entry carries; the patch window it prepares for passed on 2026-05-20 and CVE-2026-9082 and its exploitation are not recorded here (cves: [], tag no-patch).',
  'ground_truth':'SA-CORE-2026-004 (2026-05-20): patches released; updated 2026-05-22: "exploit attempts are now being detected in the wild"; KEV dateAdded 2026-05-22.',
  'ground_truth_url':SA,
  'fix':'Fold into 2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate; if kept, remove "See Immediate Action callout below and § 6".',
  'class':'imprecision'},
],
'upgrade':{
 'techniques':[
  {'id':'T1190','behavior':'Anonymous, page-visit exploitation of Drupal core (AC:None, A:None); the PSA gives no vulnerability class, so only the exposure-implied initial access is mapped','url':PSA},
 ],
 'rating':{'reliability':'A','credibility':2,'basis':'Drupal Security Team PSA is the vendor authority for its own product; NCSC.ch, BSI WID-SEC-2026-1579 and trade press restate it, so one assessor. No exploitation was known when filed.'},
 'exposure':[
  {'quote':'Not all configurations are affected.','url':THN},
  {'quote':'Drupal also noted that Drupal 7 is not affected by the issue.','url':THN},
 ],
 'detection':[],
 'triage':[],
 'takeaway':[
  {'quote':'Reserve time on May 20 during the release window to determine whether your sites are affected and in need of an immediate update. Mitigation information will be included in the advisory.','url':THN},
 ],
 'bodies':[B+'drupal-psa-webfetch.txt',B+'drupal-risk-levels-webfetch.txt',B+'ncsc-csh-12584.txt',B+'thn-drupal-urgent.txt',B+'register-drupal-brace-article.txt',B+'securityweek-drupal-prepatch.txt',B+'bsi-wid-sec-2026-1579-csaf.txt',B+'drupal-sa-core-2026-004.txt'],
 'extra':{'note':'Twin of the survivor; nothing here is unique except the change-control advice (emergency change record, freeze unrelated changes), which is the entry author\'s advice, not sourced.'},
},
'possible_twin_outside_batch':None,
}
save(d)
