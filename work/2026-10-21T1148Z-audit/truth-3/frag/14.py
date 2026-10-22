P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
BC = 'https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/'
TH = 'https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html'
MS = 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103'
ENTRY = {
 'entry': '2026-05-19/chaotic-eclipse-windows-zero-days-miniplasma-is-third-poc-in',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'cves[CVE-2020-17103].cvss',
   'claim': '"cvss": "7.8"',
   'defect': 'Microsoft scores CVE-2020-17103 CVSS 3.1 base 7.0 (AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H), severity Important.',
   'ground_truth': 'baseScore = 7.0; temporalScore = 6.1; severity = Important (MSRC); CNA record CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H',
   'ground_truth_url': MS,
   'fix': 'cvss 7.0',
   'class': 'factual-error'},
  {'where': 'cves[CVE-2020-17103].status; tags no-patch; title/summary/body "unpatched"',
   'claim': '"status": ["poc-public", "no-patch"] / released a third unpatched Windows LPE PoC',
   'defect': 'True when filed, superseded since 2026-06-09: Microsoft re-released CVE-2020-17103 to fix "Mini-Plasma" and recommends the June 2026 updates; MSRC marks it not exploited. The entry has no record of the fix.',
   'ground_truth': 'This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2020-17103 Microsoft recommends installing the June 2026 updates for your Windows operating systems. (revision 2, 2026-06-09) / exploited = No',
   'ground_truth_url': MS,
   'fix': 'Add an update record: Microsoft re-released CVE-2020-17103 on 2026-06-09; the June 2026 Windows updates fix MiniPlasma; status patch-available, poc-public.',
   'class': 'factual-error'},
  {'where': 'evidence[0]; evidence[1]',
   'claim': '"researcher Will Dormann confirmed the exploit works reliably on Windows 11 Pro with the latest May 2026 Patch Tuesday updates" (BleepingComputer) / "the flaw impacts the \'cldflt.sys\' Cloud Filter driver and its \'HsmOsBlockPlaceholderAccess\' routine, which was originally reported to Microsoft by Google Project Zero researcher James Forshaw in September 2020" (The Hacker News)',
   'defect': 'evidence[0] is not on the BleepingComputer page and merges two facts: BleepingComputer itself tested on Windows 11 Pro with the May 2026 updates, and Dormann confirmed it on the latest public Windows 11. evidence[1] is BleepingComputer\'s sentence, not The Hacker News\'.',
   'ground_truth': 'BleepingComputer tested the exploit on a fully patched Windows 11 Pro system running the latest May 2026 Patch Tuesday updates. ... Will Dormann, principal vulnerability analyst at Tharros, also confirmed the exploit works in his tests on the latest public version of Windows 11. / According to the researcher, the flaw impacts the \'cldflt.sys\' Cloud Filter driver and its \'HsmOsBlockPlaceholderAccess\' routine, which was originally reported to Microsoft by Google Project Zero researcher James Forshaw in September 2020.',
   'ground_truth_url': BC,
   'fix': 'Use verbatim BleepingComputer sentences with BleepingComputer as publisher for both.',
   'class': 'factual-error'},
  {'where': 'title; headline; summary; body paragraph 1 (sentence 1)',
   'claim': 'MiniPlasma is third PoC in series / released a third unpatched Windows LPE PoC on 2026-05-17',
   'defect': 'BleepingComputer lists BlueHammer (CVE-2026-33825), RedSun and UnDefend in April, then YellowKey and GreenPlasma, before MiniPlasma; YellowKey is a BitLocker bypass, not an LPE. MiniPlasma is third only among the May releases. BleepingComputer also says the April tools were then exploited in attacks, context the entry omits.',
   'ground_truth': 'The disclosure spree began in April with BlueHammer, a Windows local privilege escalation flaw tracked as CVE-2026-33825, followed by another privilege escalation vulnerability, RedSun, and a Windows Defender DoS tool, UnDefend. After their disclosure, all three vulnerabilities were spotted being exploited in attacks.',
   'ground_truth_url': BC,
   'fix': 'MiniPlasma is the latest in the researcher\'s 2026 series (BlueHammer, RedSun, UnDefend, YellowKey, GreenPlasma); earlier tools in the series were exploited after release.',
   'class': 'imprecision'},
  {'where': 'body Defender takeaway paragraph (detection and hardening)',
   'claim': 'Sysmon EID 13 (RegistryEvent / SetValue) on the `.DEFAULT` hive from non-`SYSTEM` processes is the primary hunt pivot; Sysmon EID 6 driver-load monitoring catches related driver-abuse paths. ... disabling Cloud Files / OneDrive integration removes the MiniPlasma attack surface',
   'defect': '(low confidence) Composed guidance not in any source. The described primitive is registry key creation (Sysmon EID 12, not value set EID 13) performed through the inbox cldflt.sys driver, so no driver load occurs; no source says disabling OneDrive removes the cldflt.sys attack surface. The only sourced hunt is ThreatLocker\'s two registry paths.',
   'ground_truth': 'The exploit appears to abuse how the Windows Cloud Filter driver handles registry key creation through an undocumented CfAbortHydration API. ... ThreatLocker posted on X that organizations should monitor the following Registry keys for modifications using their EDR platform to detect exploitation',
   'ground_truth_url': BC,
   'fix': 'Detection: monitor the two ThreatLocker registry paths for key creation/modification by standard-user processes; post-fix, verify the June 2026 update is installed. Drop EID 6 and the OneDrive claim.',
   'class': 'imprecision'},
  {'where': 'summary; body sentence 1; sourcing_note',
   'claim': 'UPDATE (originally covered 2026-05-15): ... covered in the 2026-05-15 daily / sourcing_note: "migration: update target unresolved (originally covered 2026-05-15)"',
   'defect': 'Pipeline self-reference in reader-facing text and a migration note in sourcing_note. The item was a legacy UPDATE of the YellowKey/GreenPlasma entry; the relationship should be a references[] link or a changelog record on that entry.',
   'ground_truth': 'The Hacker News: "Chaotic Eclipse, the security researcher behind the recently disclosed Windows flaws, YellowKey and GreenPlasma, has released a proof-of-concept (PoC) for a Windows privilege escalation zero-day"',
   'ground_truth_url': TH,
   'fix': 'Rewrite the opening without "UPDATE"/"covered"; replace sourcing_note with two sentences of provenance; link 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days in references[].',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Dormann sentence; uncited clauses)',
   'claim': 'Will Dormann independently confirmed the PoC opens a SYSTEM `cmd.exe` reliably on Windows 11 Pro fully patched.',
   'defect': 'Dormann\'s test was on "the latest public version of Windows 11" / "Windows 11 systems running the latest May 2026 updates"; Windows 11 Pro was BleepingComputer\'s own test. The researcher also calls the exploit a race condition whose success rate may vary. Sentences after the first carry no inline citation.',
   'ground_truth': 'MiniPlasma works "reliably" to open a "cmd.exe" prompt with SYSTEM privileges on Windows 11 systems running the latest May 2026 updates ... "It seems to work reliably in my machines but success rate may vary since it\'s a race condition."',
   'ground_truth_url': TH,
   'fix': 'BleepingComputer (Windows 11 Pro, May 2026 updates, standard user) and Will Dormann (latest public Windows 11) both reproduced a SYSTEM shell; the researcher notes it is a race condition.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1068', 'behavior': 'Standard user exploits the cldflt.sys HsmOsBlockPlaceholderAccess path to spawn a SYSTEM command prompt', 'url': BC},
   {'id': 'T1112', 'behavior': 'Undocumented CfAbortHydration path creates arbitrary registry keys in the .DEFAULT user hive without access checks', 'url': BC},
  ],
  'note': 'Local exploit; requires prior code execution as a standard user. No initial-access mapping.',
  'cve_facts': {'CVE-2020-17103': {'title': 'Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability', 'cvss_3_1': '7.0 (AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H)', 'severity': 'Important', 'original_release': '2020-12-08', 're_release': '2026-06-09 (June 2026 updates address "Mini-Plasma")', 'exploited': 'No (MSRC)', 'kev': 'not in CISA KEV 2026-10-21'}},
  'rating': {'reliability': 'A', 'credibility': 1, 'basis': 'Microsoft (vendor for its own product) re-released the CVE to fix MiniPlasma; BleepingComputer and Will Dormann independently reproduced the PoC. Independent confirmations agree.'},
  'exposure': [
   {'quote': 'BleepingComputer tested the exploit on a fully patched Windows 11 Pro system running the latest May 2026 Patch Tuesday updates. In our test, we used a standard user account, and after running the exploit, it opened a command prompt with SYSTEM privileges', 'url': BC},
   {'quote': 'The researcher further pointed out that all Windows versions are likely affected by this vulnerability.', 'url': TH},
  ],
  'detection': [
   {'quote': 'ThreatLocker posted on X that organizations should monitor the following Registry keys for modifications using their EDR platform to detect exploitation', 'url': BC},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'To comprehensively address the vulnerability identified by CVE-2020-17103 and recently publicly referred to as "Mini-Plasma" Microsoft recommends installing the June 2026 updates for your Windows operating systems.', 'url': MS},
  ],
  'bodies': [P + 'mp-bc.txt', P + 'mp-thn.txt', P + 'mp-msrc-cve-2020-17103.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days (the "originally covered 2026-05-15" entry this legacy UPDATE item extends); see also entries/2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes',
}
CLAIMS = '''
f3ae4d1ba9 ¦ F14 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ series: BlueHammer, RedSun, UnDefend (April), YellowKey, GreenPlasma, then MiniPlasma; cldflt.sys/CfAbortHydration and CVE-2020-17103 claim confirmed
fc566e4a50 ¦ F14 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ not the third LPE in the series (BlueHammer, RedSun earlier; YellowKey is a BitLocker bypass); dates 2026-05-17/18 confirmed
034d931464 ¦ F4 ¦ https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103 ¦ baseScore = 7.0 (not 7.8); re-released 2026-06-09: "Microsoft recommends installing the June 2026 updates" (no-patch stale)
0ab5c44282 ¦ F14 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ "MiniPlasma is the latest in a string of Windows zero-day disclosures" after BlueHammer, RedSun, UnDefend, YellowKey, GreenPlasma
4f1107ce2e ¦ F5 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ appears to abuse ... registry key creation through an undocumented CfAbortHydration API ... arbitrary registry keys to be created in the .DEFAULT user hive without proper access checks
d8bc6d5372 ¦ F5 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ originally reported ... by Google Project Zero researcher James Forshaw in September 2020 ... CVE-2020-17103 ... reportedly fixed in December 2020
cd21ab33e7 ¦ F5 ¦ https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html ¦ Dormann: works "reliably" to open a "cmd.exe" prompt with SYSTEM privileges on Windows 11 ... latest May 2026 updates ("Pro" was BleepingComputer's test)
cc1541f769 ¦ F5 ¦ https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html ¦ "it does not seem to work on the latest Insider Preview Canary Windows 11"; fix inference is analysis
913d17444f ¦ F5 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ ThreatLocker ... monitor the following Registry keys ... \\Registry\\User\\Software\\Policies\\Microsoft\\CloudFiles\\BlockedApps* and \\Registry\\User\\.DEFAULT\\Volatile Environment*
dd5324ba7b ¦ F5 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ analysis consistent with the series; earlier tools "spotted being exploited in attacks"
f3ef276589 ¦ F4 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ (low confidence) primitive is registry key creation via cldflt.sys (EID 12, not EID 13); no driver load involved; Sysmon guidance in no source
6cd9eff951 ¦ F4 ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ (low confidence) YellowKey hits "TPM-only BitLocker configurations" (PIN inference ok); OneDrive-disable claim in no source
aa8be355d6 ¦ ok ¦ https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/ ¦ standard user account ... opened a command prompt with SYSTEM privileges (T1068 fits; active)
'''
