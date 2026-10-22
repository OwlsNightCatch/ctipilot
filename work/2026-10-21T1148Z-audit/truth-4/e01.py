import sys; sys.path.insert(0,'/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4')
from rec import save
B='work/2026-10-21T1148Z-audit/truth-4/bodies/'
M='https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41091'
T='https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html'
R='https://learn.microsoft.com/en-us/defender-endpoint/configure-remediation-microsoft-defender-antivirus'
V='https://www.vectra.ai/blog/when-the-defender-becomes-the-door-bluehammer-redsun-and-undefend-in-the-wild'
BC='https://www.bleepingcomputer.com/news/security/microsoft-warns-of-new-defender-zero-days-exploited-in-attacks/'
HN='https://helpnetsecurity.com/2026/04/17/microsoft-defender-zero-days-exploited/'
d={
'entry':'2026-05-20/cve-2026-41091-microsoft-defender-engine-link-following-eop',
'verdict':'factual-error',
'defects':[
 {'where':'actions[0]; body paragraph 2 (Detection/Exposure text)',
  'claim':'For hosts with auto-updates blocked (GPO "Turn off routine remediation"), push the Engine signature update manually',
  'defect':'The named GPO does not control Defender engine or signature updates; it controls whether detected threats are remediated automatically or the user is prompted. Body paragraph 2 repeats it: "for any host where the GPO "Turn off routine remediation" disables auto-remediation, push the Engine update manually."',
  'ground_truth':'Microsoft Learn, remediation settings table: "Turn off routine remediation. Specify whether Microsoft Defender Antivirus automatically remediates threats, or whether to prompt the user. Disabled. Threats are remediated automatically." MSRC FAQ: engine and definition updates arrive via the default automatic-update configuration; Defender AV updates doc lists Windows Update, WSUS and other channels.',
  'ground_truth_url':R,
  'fix':'Drop the GPO name from actions[0] and body paragraph 2. Say instead: confirm AMEngineVersion >= 1.1.26040.8 and manually push the engine update on hosts where Windows Update/WSUS/Intune hold engine updates back or that are offline.',
  'class':'factual-error'},
 {'where':'section 2026-05-22T05:00:07Z first sentence; updates[0].summary',
  'claim':'Both Microsoft Defender vulnerabilities confirmed as actively exploited in the wild in a combined out-of-band engine update',
  'defect':'The cited Hacker News page and MSRC describe two separate fixes (Malware Protection Engine for CVE-2026-41091, Antimalware Platform for CVE-2026-45498); neither calls the release out-of-band. Cited clause binds a release characterisation the page does not carry (and THN itself mislabels 1.1.26040.8 a Platform version).',
  'ground_truth':'THN: "The two vulnerabilities have been addressed in Microsoft Defender Antimalware Platform versions 1.1.26040.8 and 4.18.26040.7, respectively." MSRC CVE-2026-41091: "First version of the Microsoft Malware Protection Engine with this vulnerability addressed Version 1.1.26040.8"; MSRC CVE-2026-45498: "First version of the Microsoft Defender Antimalware Platform ... addressed Version 4.18.26040.7". MSRC FAQ: engine updates ship "once a month or as needed".',
  'ground_truth_url':T,
  'fix':'Write: both flaws are exploited in the wild (MSRC exploited=Yes, CISA KEV 2026-05-20); fixes are Engine 1.1.26040.8 (CVE-2026-41091) and Platform 4.18.26040.7 (CVE-2026-45498). Drop "combined out-of-band". Drop "(originally covered 2026-05-20)" from the record summary.',
  'class':'imprecision'},
 {'where':'section 2026-05-22T05:00:07Z, CVE-2026-41091 sentence',
  'claim':'CWE-59 improper link resolution / link following in `MsMpEng.exe`) allows an authorized local standard-user to abuse Defender\'s privileged process\'s symbolic-link resolution during file-system operations to elevate to `NT AUTHORITY\\SYSTEM`',
  'defect':'No cited page names MsMpEng.exe, a standard-user attacker, or symbolic-link resolution during file-system operations. The advisory names the Microsoft Malware Protection Engine and an "authorized attacker".',
  'ground_truth':'MSRC: "Improper link resolution before file access (\'link following\') in Microsoft Defender allows an authorized attacker to elevate privileges locally." and "The Microsoft Malware Protection Engine, mpengine.dll, provides the scanning, detection, and cleaning capabilities".',
  'ground_truth_url':M,
  'fix':'Use the advisory wording: authorized local attacker, Microsoft Malware Protection Engine, SYSTEM. If the RedSun mechanism is wanted (researcher-confirmed mapping, reported by BleepingComputer and THN), cite Vectra: Cloud Files API, oplocks and a directory junction redirecting a Defender-triggered rewrite into a protected system path.',
  'class':'imprecision'},
 {'where':'body paragraph 2 (hunt sentence); section 2026-05-22T05:00:07Z last sentence',
  'claim':'Hunt signal: Sysmon EID 1 for SYSTEM-level process spawns from `MsMpEng.exe` as parent.',
  'defect':'(low confidence) No cited source supports this hunt signal, and the one technical description of the researcher-confirmed RedSun mechanism has SYSTEM execution arriving through the Cloud Files infrastructure, not as a child of MsMpEng.exe. The paragraph-2 hunt ("junction / hard-link creation events (Sysmon EID 11 ... pointing to privileged Defender / Program Files paths)") is likewise carried by no source; Vectra describes a junction redirecting a Defender-triggered rewrite into a protected system path.',
  'ground_truth':'Vectra: "Defender sees a known signature, initiates a remediation cycle, and RedSun wins the race to redirect the resulting file rewrite. At that point, the Cloud Files Infrastructure executes the attacker-planted binary as SYSTEM." HelpNet/Huntress: exploit files dropped "into the user\'s Pictures and Downloads folders".',
  'ground_truth_url':V,
  'fix':'Remove both Sysmon-specific hunt statements or replace with the sourced behaviour: low-privilege user staging an exploit binary in Pictures/Downloads, a Defender remediation cycle on a test string, a junction in a user-writable path, then a SYSTEM-context process from a system service.',
  'class':'factual-error'},
 {'where':'cves[CVE-2026-45498]; cves[CVE-2026-41091]; cves[]',
  'claim':'id: CVE-2026-45498 ... type: lpe ... auth: post-auth (and affected: null, fixed: null on both records)',
  'defect':'CVE-2026-45498 is a denial of service (CWE-400, AV:L/AC:L/PR:N, impact Denial of Service), not an LPE and not privileged-access-required. Both records leave affected/fixed null although MSRC gives them. CVE-2026-45584 is named in actions[0] but absent from cves[].',
  'ground_truth':'MSRC CVE-2026-45498: impact "Denial of Service", CWE-400, vector CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L, baseScore 4.0, "Last version of the Microsoft Defender Antimalware Platform affected ... 4.18.26030.3011", fixed 4.18.26040.7. MSRC CVE-2026-41091: last affected Engine 1.1.26030.3008, fixed 1.1.26040.8.',
  'ground_truth_url':'https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45498',
  'fix':'CVE-2026-45498: type dos, auth none. Fill affected "Malware Protection Engine <= 1.1.26030.3008" / fixed "1.1.26040.8" for CVE-2026-41091 and affected "Antimalware Platform <= 4.18.26030.3011" / fixed "4.18.26040.7" for CVE-2026-45498. Either add CVE-2026-45584 to cves[] or reference its own entry and drop the id from actions[0].',
  'class':'factual-error'},
 {'where':'evidence[0..1]; sourcing_note; updates[0].summary',
  'claim':'publisher: ctipilot v2 brief (migrated) ... sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"; "UPDATE (originally covered 2026-05-20)"',
  'defect':'Both evidence quotes are the pipeline quoting itself and prove nothing; sourcing_note and the record summary carry pipeline self-reference. The second source is a news outlet labelled role: primary.',
  'ground_truth':'Verbatim carriers exist: MSRC "Systems that have disabled Microsoft Defender are not in an exploitable state."; THN "Huntress has since observed exploitation of both the vulnerabilities, alongside BlueHammer (CVE-2026-33825)."',
  'ground_truth_url':T,
  'fix':'Replace evidence with verbatim MSRC and THN passages, set the sourcing_note to two sentences of provenance (MSRC advisory, CISA KEV listing, Hacker News and BleepingComputer reporting), mark the Hacker News record secondary.',
  'class':'imprecision'},
 {'where':'body paragraph 1 (uncited clauses); summary',
  'claim':'The flaw is an **improper link resolution before file access** (CWE-59, "link following") ... CVSS 7.8 (AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). Vulnerable Engine builds: ≤ 1.1.26030.3008; fixed in Engine 1.1.26040.8.',
  'defect':'The sole inline citation terminates the first sentence (the 2026-05-19 release date); the CWE, CVSS vector, affected and fixed builds are uncited though MSRC carries them. The summary says the engine "auto-remediates via signature channel", which loosens MSRC: the default configuration keeps the engine and definitions up to date automatically (two separate things).',
  'ground_truth':'MSRC: "the default configuration in Microsoft antimalware software helps ensure that malware definitions and the Microsoft Malware Protection Engine are kept up to date automatically."',
  'ground_truth_url':M,
  'fix':'Cite the MSRC page on the CVSS, builds and fix clauses; summary: "the default configuration updates the engine automatically".',
  'class':'imprecision'},
],
'upgrade':{
 'techniques':[
  {'id':'T1068','behavior':'Local privilege escalation to SYSTEM through link following in the Microsoft Malware Protection Engine by an authorized local attacker','url':M},
  {'id':'T1687','behavior':'CVE-2026-45498, exploited alongside it, is a Defender denial of service that standard users use to block Defender definition updates (researcher-confirmed UnDefend mapping, reported by BleepingComputer)','url':BC},
 ],
 'rating':{'reliability':'A','credibility':1,'basis':'MSRC is the vendor PSIRT for its own product and states exploited=Yes; CISA KEV (dateAdded 2026-05-20) and Huntress in-the-wild observation of the researcher PoCs (via Help Net Security) are independent of Microsoft. THN and BleepingComputer restate. The PoC-to-CVE mapping is the researcher\'s own confirmation.'},
 'exposure':[
  {'quote':'Systems that have disabled Microsoft Defender are not in an exploitable state.','url':M},
  {'quote':'Defender runs on all supported version of Windows.','url':M},
  {'quote':'Yes, Microsoft System Center Endpoint Protection, Microsoft System Center 2012 R2 Endpoint Protection, Microsoft System Center 2012 Endpoint Protection and Microsoft Security Essentials.','url':M},
 ],
 'detection':[
  {'quote':'The attacker dropped the exploit files into the user’s Pictures and Downloads folders and renamed them to avoid suspicion. Then, before launching the exploits, they ran commands to map out user privileges, discovered stored credentials, and the Active Directory structure.','url':HN},
  {'quote':'The exploit baits Defender\'s real-time protection engine using an embedded EICAR test string.','url':V},
 ],
 'triage':[],
 'takeaway':[
  {'quote':'Best practices recommend that customers regularly verify whether software distribution, such as the automatic deployment of Microsoft Malware Protection Engine updates and malware definitions, is working as expected in their environment.','url':M},
 ],
 'bodies':[B+'msrc-cve-2026-41091.txt',B+'msrc-cve-2026-45498.txt',B+'thn-defender-two-actively.txt',B+'bleeping-defender-zerodays.txt',B+'helpnet-defender-zerodays.txt',B+'vectra-defender-door.txt',B+'ms-config-remediation.txt',B+'ms-defender-av-updates.txt',B+'cisa-kev.json'],
 'extra':{'ioc_scan_note':'Four-part version strings (1.1.26030.3008, 1.1.26040.8, 4.18.26030.3011, 4.18.26040.7) appear bare in summary, body, actions and section; write them as "Engine version 1.1.26040.8" / "Platform version 4.18.26040.7" so the IOC scan does not read them as IPv4 addresses.',
          'cisa_kev':'CVE-2026-41091 and CVE-2026-45498 both in CISA KEV, dateAdded 2026-05-20, dueDate 2026-06-03, knownRansomwareCampaignUse Unknown (cisa-kev recipe, 2026.10.20 catalog)',
          'affected_products':'Microsoft Defender (Malware Protection Engine <= 1.1.26030.3008; Antimalware Platform <= 4.18.26030.3011); also Microsoft System Center Endpoint Protection and Microsoft Security Essentials per MSRC FAQ',
          'timeline':'PoCs published 2026-04-16 by researcher Nightmare Eclipse; Huntress observed use on 2026-04-16 (Help Net Security); MSRC advisory 2026-05-19; KEV 2026-05-20; researcher confirmed CVE-2026-41091 = RedSun and CVE-2026-45498 = UnDefend (BleepingComputer update 2026-05-25).'},
},
'possible_twin_outside_batch':None,
}
save(d)
