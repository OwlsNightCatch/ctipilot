P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
TA = 'https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/'
ENTRY = {
 'entry': '2026-05-20/cisco-talos-demo-pdb-badiis-variant-now-a-commodity-maas-iis',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'title; headline; body (IIS pipeline sentence; Detection concepts)',
   'claim': 'commodity MaaS IIS ISAPI backdoor / The ISAPI DLL hooks into the Windows IIS request pipeline by registering as an ISAPI filter or extension (loaded from `applicationHost.config` or per-site `web.config`) / enumerate ... for unexpected `<isapiFilters>` / `<httpModules>` entries',
   'defect': 'Talos never says ISAPI. Its installers register the malicious DLL in the IIS server module list, targeting the <globalModules> and <modules> configuration sections (native IIS modules). The detection advice points at the wrong configuration sections.',
   'ground_truth': 'this phase targets the "<globalModules>" and "<modules>" sections to register the malicious DLL at the server level. ... it searches for the BadIIS malware, copies the payloads to specific primary and backup directories, and registers them within the IIS server module list to ensure persistence.',
   'ground_truth_url': TA,
   'fix': 'BadIIS is a malicious native IIS module registered in the server module list (<globalModules>/<modules>); detection: review those sections for unknown modules and check for the hidden backup copy that restores the DLL on IIS restart.',
   'class': 'factual-error'},
  {'where': 'body (geography sentence)',
   'claim': 'the activity overlaps with the broader **DragonRank** SEO-poisoning ecosystem Talos previously documented under the actor cluster **UAT-8099**',
   'defect': 'DragonRank and UAT-8099 are two separate groups in two earlier Talos reports, and Talos contrasts the demo.pdb variant with their BadIIS variants rather than asserting overlap; it also says the attacks are hard to attribute to a single actor.',
   'ground_truth': 'Talos has been tracking multiple cybercrime groups, including those detailed in our previous reports on DragonRank and UAT-8099, that utilize various BadIIS variants ... However, the variant characterized by the "demo.pdb" strings represents a significant departure from these previous iterations. / it is difficult to attribute these attacks to a single threat actor.',
   'ground_truth_url': TA,
   'fix': 'Talos contrasts this commodity variant with the BadIIS variants used by the DragonRank and UAT-8099 groups (hardcoded C2, static payloads); it is likely sold or shared among several Chinese-speaking cybercrime groups.',
   'class': 'factual-error'},
  {'where': 'summary; body sentence 1',
   'claim': 'Cisco Talos published on 2026-05-19 the first MaaS-ecosystem analysis of a BadIIS variant',
   'defect': '"first" is not in the source; Talos notes Trend Micro, AhnLab, VNPT and Elastic also track these variants. The Chinese-speaking cybercrime-group context in Talos\' title and lead is omitted.',
   'ground_truth': 'While multiple security vendors are tracking the global spread of these variants, Talos\' observed tactics, techniques, and procedures (TTPs) show notable divergences from those documented by other vendors like Trend Micro, Ahnlab, VNPT, and Elastic.',
   'ground_truth_url': TA,
   'fix': 'Cisco Talos published on 2026-05-19 an analysis of a commodity "demo.pdb" BadIIS variant likely sold or shared among Chinese-speaking cybercrime groups under a MaaS model.',
   'class': 'imprecision'},
  {'where': 'body (prerequisite sentence; lwxat sentence; Detection concepts); event_date',
   'claim': 'it requires a prior IIS-server compromise (web-shell, vulnerable CMS plugin) to plant the DLL / PDB-metadata correlation traces development to a single developer alias "lwxat" / alert on IIS worker (w3wp.exe) loading DLLs from non-standard paths (Sysmon EID 7) ... / event_date: null',
   'defect': 'Talos does not describe the access vector (no web shell or CMS plugin). The "lwxat" alias comes from the builder\'s C2 authentication string, a config parameter and the "lwxatisme" user agent; the PDB paths give the timeline and a customer alias "xshen". The remaining detection items are composed (Talos gives none beyond its signatures). event_date should be 2026-05-19. All sentences after sentence 1 are uncited.',
   'ground_truth': 'Talos assesses with moderate-to-high confidence that the string "lwxat" is the author\'s alias or handle ... Builder authentication mechanism ... Configuration parameter ... User-agent signature',
   'ground_truth_url': TA,
   'fix': 'State that the access vector is not described; attribute "lwxat" to the builder authentication, config and user-agent evidence; mark composed detection as derived; set event_date 2026-05-19; cite Talos per clause.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1505.004', 'behavior': 'Malicious DLL registered in the IIS server module list (<globalModules>/<modules>) to hook requests and responses', 'url': TA},
   {'id': 'T1565.002', 'behavior': 'Responses rewritten for SEO fraud: content hijacking, injected links, JavaScript redirectors to illicit sites', 'url': TA},
   {'id': 'T1543.003', 'behavior': 'Installers run as Windows services and drop a secondary service component', 'url': TA},
   {'id': 'T1036.004', 'behavior': 'Services impersonate Winlogin, FaxService or AudiosService', 'url': TA},
   {'id': 'T1027', 'behavior': 'Commands and parameters obfuscated with custom Base64; C2 addresses XOR-encoded (single byte) or double Base64', 'url': TA},
   {'id': 'T1059.003', 'behavior': 'Installer executes assembled IIS registration commands, likely via cmd.exe /c', 'url': TA},
   {'id': 'T1105', 'behavior': 'Service installer downloads and executes additional payloads from a secondary C2', 'url': TA},
   {'id': 'T1071.001', 'behavior': 'HTTP C2 communication, some samples with a custom user agent; builder authenticates to C2', 'url': TA},
  ],
  'note': 'Initial access to the IIS server is not described by Talos.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Cisco Talos original research on its own investigations and recovered tooling; single source, other vendors track related BadIIS variants but not this ecosystem analysis.'},
  'exposure': [
   {'quote': 'Since 2024, Talos has investigated numerous attacks across the Asia-Pacific region (along with a few in South Africa, Europe and North America) that utilize a specific variant of BadIIS characterized by "demo.pdb" strings.', 'url': TA},
  ],
  'detection': [
   {'quote': 'The installer now copies the BadIIS malware not only to the active directory used for hooking IIS requests and responses but also to a hidden backup location. This ensures that the malicious BadIIS is automatically restored and launched every time the compromised IIS server is restarted.', 'url': TA},
   {'quote': 'this phase targets the "<globalModules>" and "<modules>" sections to register the malicious DLL at the server level.', 'url': TA},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'the variant characterized by the "demo.pdb" strings represents a significant departure from these previous iterations.', 'url': TA},
  ],
  'bodies': [P + 'badiis-talos.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
a9aecf96b7 ¦ F4 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ commodity MaaS, lwxat alias and builder confirmed; Talos never says ISAPI: DLL registered in "<globalModules>" and "<modules>" (native IIS module)
c51d32844e ¦ F14 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ date 2026-05-19 confirmed; "first" not stated; Trend Micro, AhnLab, VNPT and Elastic track these variants
99859daeaf ¦ F5 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ author operating under the alias "lwxat", spanning from at least September 2021 through January 2026 ... reactive evasion tactics targeting specific security vendors such as Norton
d645ea8267 ¦ F5 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ builder tool ... traffic redirection to illicit sites, reverse proxying for search engine crawler manipulation, content hijacking, and backlink injection
fe7c8f099c ¦ F4 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ registers the malicious DLL in the IIS server module list (<globalModules>/<modules>); no ISAPI filter/extension; crawler proxying confirmed
1d004ac75b ¦ F13 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ APAC plus "a few in South Africa, Europe and North America" confirmed; DragonRank and UAT-8099 are separate groups and the variant "represents a significant departure"
d1191e570c ¦ F4 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ (low confidence) Talos describes installers but no access vector; web-shell / CMS-plugin prerequisites in no source
e34cdee7fd ¦ F4 ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ composed detection points at <isapiFilters>/<httpModules>; Talos: <globalModules>/<modules>, hidden backup copy restored on IIS restart
304c082fc2 ¦ ok ¦ https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ ¦ APAC focus confirmed; relevance judgement (no factual claim beyond geography)
'''
