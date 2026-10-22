P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
KR = 'https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/'
GZ = 'https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330'
ENTRY = {
 'entry': '2026-05-19/cisa-contractor-nightwing-exposed-aws-govcloud-admin-keys-an',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'summary; body paragraph 1 (exposed material sentence)',
   'claim': 'credentials to CISA\'s internal Artifactory code-package repository ("LZ-DSO" — Landing Zone DevSecOps) / the LZ-DSO Artifactory build-package repo',
   'defect': 'Krebs describes two different things: LZ-DSO ("Landing Zone DevSecOps", the agency\'s secure code development environment) is one of the systems in the plaintext password file, and separately the archive holds credentials to CISA\'s internal "artifactory". LZ-DSO is not the Artifactory.',
   'ground_truth': 'According to Caturegli, those systems included one called "LZ-DSO," which appears short for "Landing Zone DevSecOps," the agency\'s secure code development environment. ... He said the archive also includes plain text credentials to CISA\'s internal "artifactory" — essentially a repository of all the code packages they are using to build software',
   'ground_truth_url': KR,
   'fix': 'Exposed material included passwords for dozens of internal systems, among them LZ-DSO (Landing Zone DevSecOps, the secure code development environment), and separately plaintext credentials to CISA\'s internal Artifactory package repository.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (last sentence)',
   'claim': 'CISA acknowledged a ~one-third workforce reduction from buyouts and resignations under the Trump administration may have weakened oversight of contractor behaviour.',
   'defect': 'The workforce figure is Krebs\'s own statement (linking Cybersecurity Dive), not a CISA acknowledgement, and no source ties it to contractor oversight. CISA\'s actual statement says there is no indication sensitive data was compromised.',
   'ground_truth': 'CISA is currently operating with only a fraction of its normal budget and staffing levels. The agency has lost nearly a third of its workforce since the beginning of the second Trump administration ... / "Currently, there is no indication that any sensitive data was compromised as a result of this incident," the CISA spokesperson wrote.',
   'ground_truth_url': KR,
   'fix': 'Replace with CISA\'s statement (aware, investigating, no indication sensitive data was compromised, adding safeguards); if kept, attribute the staffing context to Krebs and drop the oversight inference.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 1); headline; summary',
   'claim': 'used a public GitHub repository named "Private-CISA" as a personal sync mechanism between work and home machines, exposing ... from approximately 2025-11-13 to 2026-05-15 — about six months',
   'defect': 'The sync explanation is Caturegli\'s suspicion ("What I suspect happened"), stated as fact. The repo was created on 2025-11-13 and taken offline "this past weekend" after notification; 2026-05-15 is when Valadon contacted Krebs. Gizmodo notes the six months is an upper bound that "could have been much shorter".',
   'ground_truth': '"What I suspect happened is [the CISA contractor] was using this GitHub to synchronize files between a work laptop and a home computer" / the duration of the vulnerability seems to have been about six months—but it could have been much shorter depending on what information as added when. (Gizmodo)',
   'ground_truth_url': KR,
   'fix': 'Caturegli suspects the contractor used the repo to sync files between a work laptop and a home computer; the repo existed from 2025-11-13 until it was taken down around 2026-05-16/17, so exposure lasted up to about six months.',
   'class': 'imprecision'},
  {'where': 'body Why it matters paragraph; T-id line',
   'claim': 'Caturegli identified the Artifactory access as the highest-impact exposure — write access to a national cybersecurity agency\'s build-package repo would enable backdoor insertion ... (T1195.002 ...) ... T1552.001 (Credentials In Files) / T1552.004 (Private Keys).',
   'defect': 'Caturegli calls the Artifactory credentials a "juicy target" and "a prime place to move laterally"; he does not rank it highest-impact or say the credentials grant write access. No supply-chain compromise or malicious use is reported. Private keys (T1552.004) are not listed among exposed items (cloud keys, tokens, plaintext passwords, logs).',
   'ground_truth': 'this would represent a juicy target for malicious attackers looking for ways to maintain a persistent foothold in CISA systems. "That would be a prime place to move laterally," he said. "Backdoor in some software packages, and every time they build something new they deploy your backdoor left and right."',
   'ground_truth_url': KR,
   'fix': 'Quote Caturegli\'s assessment as a risk; drop "highest-impact" and "write access"; move ids into techniques[] (T1593.003, T1552.001, T1078.004) and keep T1195.002 out unless framed as risk.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (exposed material); event_date; Why it matters; uncited clauses',
   'claim': 'plaintext usernames and passwords (`AWS-Workspace-Firefox-Passwords.csv`) ... SSH keys and cloud tokens / event_date: 2026-05-19 / **Why it matters to us:**',
   'defect': 'The CISA statement ("no indication that any sensitive data was compromised") is omitted, a material qualifier. "SSH keys" as exposed items is not stated. The primary (Krebs) is dated 2026-05-18, not 2026-05-19. The literal leak file name may be read as a file-name indicator. Clauses after sentence 1 carry no inline citation; "to us" is pipeline voice; the hardening list is composed.',
   'ground_truth': 'the GitHub repository ... harbored a vast number of internal CISA/DHS credentials and files, including cloud keys, tokens, plaintext passwords, logs and other sensitive CISA assets.',
   'ground_truth_url': KR,
   'fix': 'Add CISA\'s statement; list exposed items as Krebs does; event_date 2026-05-18; cite Krebs per clause; describe the file generically ("a CSV of browser-saved passwords").',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1593.003', 'behavior': 'Secrets discoverable in a public GitHub repository (found by GitGuardian\'s public-repo scanning)', 'url': KR},
   {'id': 'T1552.001', 'behavior': 'Plaintext passwords in a CSV, cloud keys and tokens in repository files', 'url': KR},
   {'id': 'T1078.004', 'behavior': 'Exposed keys authenticated to three AWS GovCloud accounts at high privilege and stayed valid 48 hours after takedown', 'url': KR},
  ],
  'note': 'Accidental exposure; CISA reports no indication of compromise, so these map the exposed opportunity, not observed attacker activity. T1195.002 is only Caturegli\'s risk scenario.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Krebs on Security original reporting with two named researchers who examined and validated the material, and a CISA statement acknowledging the exposure; Gizmodo restates Krebs.'},
  'exposure': [
   {'quote': 'the commit logs in the offending GitHub account show that the CISA administrator disabled the default setting in GitHub that blocks users from publishing SSH keys or other secrets in public code repositories.', 'url': KR},
   {'quote': 'Caturegli said the exposed AWS keys inexplicably continued to remain valid for another 48 hours.', 'url': KR},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'many of the credentials used a password consisting of each platform\'s name followed by the current year. Caturegli said such practices would constitute a serious security threat for any organization even if those credentials were never exposed externally', 'url': KR},
  ],
  'bodies': [P + 'cisa-krebs.txt', P + 'cisa-gizmodo.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
3494b3d348 ¦ ok ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ contractor (Nightwing employee) public repo exposed credentials to highly privileged AWS GovCloud accounts; created November 13, 2025
01d84038e9 ¦ F4 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ LZ-DSO ("Landing Zone DevSecOps ... secure code development environment") and the internal "artifactory" are separate items; 48h validity confirmed
fbebf241cb ¦ F3 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ "What I suspect happened is ... synchronize files between a work laptop and a home computer" (suspicion); repo taken offline "this past weekend", not 05-15
f45c428c2e ¦ F5 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ On May 15, KrebsOnSecurity heard from Guillaume Valadon, a researcher with the security firm GitGuardian
ebf932959c ¦ F4 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ three GovCloud admin credentials and plaintext password CSV confirmed; LZ-DSO is not the Artifactory; SSH keys not listed as exposed
d958c7b320 ¦ F5 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ disabled the default setting in GitHub that blocks users from publishing SSH keys or other secrets; "explicit commands to disable GitHub secrets detection feature"
8771a9baed ¦ F5 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ validated that the exposed credentials could authenticate to three AWS GovCloud accounts at a high privilege level ... remain valid for another 48 hours
cf18a30bb2 ¦ F4 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ workforce figure is Krebs's statement, not CISA's; no oversight link; CISA: "no indication that any sensitive data was compromised"
f99bcb8984 ¦ F14 ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ Caturegli: "juicy target", "prime place to move laterally"; no "highest-impact" ranking and no write-access statement
913ec9e9b1 ¦ F5 ¦ null ¦ composed hardening recommendations for EU/CH CERTs; no fetched source
c0026c6f40 ¦ ok ¦ https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/ ¦ T1552.001 fits plaintext credentials in repository files; T1552.004 weakly supported (private keys not listed; logged)
'''
