P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
BR = 'https://www.security.com/blog-post/fast16-nuclear-sabotage'
TH = 'https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html'
ZE = 'https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/'
ENTRY = {
 'entry': '2026-05-19/symantec-carbon-black-document-fast16-hook-engine-targeting',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'summary; body Background paragraph',
   'claim': 'Fast16 ... was first disclosed by SentinelOne at LABScon 2026 in April 2026 ... Earlier reporting also speculated that the malware operated against physical centrifuge equipment. Both framings now appear incorrect on closer expert review.',
   'defect': 'No source names LABScon (Broadcom: SentinelOne "published the first public analysis" in April 2026; THN: SentinelOne "presented an analysis"). No source reports earlier speculation that Fast16 hit centrifuges; centrifuges appear only in the Stuxnet comparison. "Both framings ... incorrect" overstates: Broadcom itself still titles Fast16 "Pre-Stuxnet", and Zetter\'s contemporaneous reading is conditional on Iran targeting and US/Israeli authorship.',
   'ground_truth': 'In April 2026, our peers in SentinelOne published the first public analysis of fast16 ... whose oldest components appear to date from around 2005, approximately two years before Stuxnet first became active. (Broadcom) / All of this suggests that if Fast16 did target Iran in 2005, and if the US or Israel were behind it, it did not really predate Stuxnet, but was contemporaneous with it (Zetter)',
   'ground_truth_url': BR,
   'fix': 'SentinelOne published the first analysis in April 2026 and dated the oldest components to about 2005, about two years before Stuxnet; Zetter argues it was contemporaneous with Stuxnet if it targeted Iran; Contradiction: Broadcom still calls it pre-Stuxnet. Drop LABScon and the centrifuge speculation.',
   'class': 'factual-error'},
  {'where': 'body paragraph 2 (sentence 1); sources[0]',
   'claim': 'Broadcom\'s Symantec and Carbon Black teams published a technical analysis on 2026-05-18 ... [Broadcom Security, 2026-05-18]',
   'defect': 'The Broadcom post is dated 2026-05-16; 2026-05-18 is The Hacker News date (two-day drift).',
   'ground_truth': 'page metadata and dateline: 2026-05-16 (security.com post "Fast16: Pre-Stuxnet Sabotage Tool Was Built to Subvert Nuclear Weapons Simulations")',
   'ground_truth_url': BR,
   'fix': 'Broadcom Security, 2026-05-16; event_date 2026-05-16.',
   'class': 'factual-error'},
  {'where': 'evidence[0]',
   'claim': '"Fast16\'s hook engine is selectively interested in high-explosive simulations inside LS-DYNA and AUTODYN, and the malware checks for the density ... the threshold uranium can only be reached under the shock compression of an implosion device"',
   'defect': 'Not contiguous: it joins two separate key-findings bullets with ", and" and changes "can only reach" to "can only be reached".',
   'ground_truth': 'Fast16\'s hook engine is selectively interested in high-explosive simulations inside LS-DYNA and AUTODYN. / The malware checks for the density of the material being simulated and only acts when that value passes 30 g/cm³, the threshold uranium can only reach under the shock compression of an implosion device.',
   'ground_truth_url': BR,
   'fix': 'Quote one bullet verbatim, for example the density bullet.',
   'class': 'factual-error'},
  {'where': 'body paragraph 2 (LS-DYNA/AUTODYN sentence; Defender relevance sentence)',
   'claim': 'LS-DYNA and AUTODYN — the canonical high-explosive simulation codes used for weapons design / Broadcom appears to describe the first publicly-documented use of a filesystem-driver-level instruction-rewriting hook engine to corrupt scientific-simulation output',
   'defect': 'Broadcom describes LS-DYNA and AUTODYN as general simulation software (crashworthiness, material modelling, explosive simulation), not weapons-design codes as such. No source says this is the first documented use of the technique.',
   'ground_truth': 'Both are software applications used to simulate real-world problems such as vehicle crashworthiness, material modelling, and explosive simulation.',
   'ground_truth_url': BR,
   'fix': 'LS-DYNA and AUTODYN, general-purpose explicit-dynamics simulation software also used for explosive simulation; drop "first publicly-documented".',
   'class': 'imprecision'},
  {'where': 'summary; headline; body (uncited clauses; Defender guidance)',
   'claim': 'summary = Background paragraph only / headline ends "corrects \\"pre-Stuxnet\\" framing to" / add filesystem-driver-load monitoring (Sysmon EID 6, Windows boot-start driver enumeration) and integrity checking',
   'defect': 'The summary restates background and never states the finding (Broadcom\'s confirmation of LS-DYNA/AUTODYN targeting and the 30 g/cm³ trigger); the headline is cut mid-phrase. Background and architecture sentences carry no inline citation. The detection advice is composed; Broadcom gives concrete install artifacts (service, SCSI-class filter driver loaded at boot, IFEO Debugger hijack, timestomping) that would support a sourced Detection line.',
   'ground_truth': 'It then drops the fast16.sys kernel driver into the system drivers folder, matches its timestamps to beep.sys, and configures the registry to load it as a SCSI-class filter driver on the next boot. ... fast16 abuses Image File Execution Options by writing its own path into the Debugger value',
   'ground_truth_url': BR,
   'fix': 'Rewrite the summary around the Broadcom finding; complete the headline; cite Broadcom on architecture; base Detection on the documented install artifacts (described generically, no file names).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1014', 'behavior': 'Boot-start kernel filesystem filter driver patches executables on the fly as they are read from disk', 'url': BR},
   {'id': 'T1565.003', 'behavior': 'Hook engine rewrites instruction sequences in LS-DYNA/AUTODYN to scale down simulation outputs once uranium density passes 30 g/cm³', 'url': BR},
   {'id': 'T1543.003', 'behavior': 'Registers itself as a Windows service and loads its driver as a SCSI-class filter at boot', 'url': BR},
   {'id': 'T1546.012', 'behavior': 'Image File Execution Options Debugger value hijacks a chosen application for persistence', 'url': BR},
   {'id': 'T1070.006', 'behavior': 'Clones creation dates and ACLs from system binaries onto its own files', 'url': BR},
   {'id': 'T1518.001', 'behavior': 'Checks for 18 endpoint-security registry keys and refuses to propagate if any exist', 'url': BR},
   {'id': 'T1135', 'behavior': 'Propagates inside the target network using share enumeration', 'url': BR},
   {'id': 'T1569.002', 'behavior': 'Remote installation and execution mode via remote service control', 'url': BR},
   {'id': 'T1059', 'behavior': 'Main behavior implemented in Lua code run by an embedded Lua 5.0 VM', 'url': BR},
  ],
  'note': 'Historic (circa 2005) framework; no initial-access vector is described.',
  'rating': {'reliability': 'B', 'credibility': 1, 'basis': 'Symantec/Carbon Black reverse-engineered the hook engine and independently confirmed SentinelOne\'s identification of the targeted applications; Zetter adds expert interpretation. Two research labs agree on the technical core.'},
  'exposure': [
   {'quote': 'Once the driver is installed, it creates a kernel file system filter to monitor all accessed files. It first waits until EXPLORER.EXE is launched and then targets any files with the extension .EXE that are compiled with the Intel compiler', 'url': BR},
  ],
  'detection': [
   {'quote': 'It then drops the fast16.sys kernel driver into the system drivers folder, matches its timestamps to beep.sys, and configures the registry to load it as a SCSI-class filter driver on the next boot.', 'url': BR},
   {'quote': 'On execution, the malware deletes that registry key, launches the original application, re-adds the key to maintain persistence', 'url': BR},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'Fast16 took a different approach and fed operators false data about nuclear warheads testing to make engineers believe the tests were *not* fine, while in fact they may have been.', 'url': ZE},
  ],
  'bodies': [P + 'f16-broadcom.txt', P + 'f16-thn.txt', P + 'f16-zetter.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
56fd186f81 ¦ ok ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ Symantec's Threat Hunter Team ... can confirm LS-DYNA and AUTODYN as targeted applications; Zetter: "didn't predate Stuxnet but was contemporaneous with it"; headline truncated (logged)
bd8bdc464b ¦ F4 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ SentinelOne "published the first public analysis" in April 2026 (no LABScon); ~two years before Stuxnet confirmed; no source on centrifuge speculation
ef62256c21 ¦ F3 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ Broadcom post dated 2026-05-16 (entry cites 2026-05-18, THN's date)
0dd4478297 ¦ ok ¦ https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/ ¦ dated 2026-05-16: "Fast16 didn't predate Stuxnet but was contemporaneous with it ... feeding false data to engineers"
5b889e5953 ¦ F4 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ "In April 2026, our peers in SentinelOne published the first public analysis"; LABScon in no source
a16e44a6bd ¦ F4 ¦ https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/ ¦ centrifuges appear only for Stuxnet ("Stuxnet increased the pressure inside centrifuges"); no earlier Fast16 centrifuge speculation in any source
da69f75270 ¦ F4 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ Broadcom title still "Pre-Stuxnet Sabotage Tool"; Zetter's contemporaneous view is conditional ("if Fast16 did target Iran ... if the US or Israel were behind it")
6313162a6c ¦ F5 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ a service binary that embeds an early Lua 5.0 virtual machine, a boot-start filesystem driver that intercepts and patches executable code ... a rule-driven hook engine
9d3056e701 ¦ F5 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ only acts when that value passes 30 g/cm³, the threshold uranium can only reach under the shock compression of an implosion device ("canonical weapons-design codes" overstated)
35713bce80 ¦ F14 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ no source calls it the first publicly documented use of a filesystem-driver instruction-rewriting hook engine
a4a919436f ¦ F5 ¦ https://www.security.com/blog-post/fast16-nuclear-sabotage ¦ composed guidance; Broadcom: driver loaded "as a SCSI-class filter driver on the next boot" (supports a boot-driver check)
'''
