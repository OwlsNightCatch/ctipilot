P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
U = 'https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/'
ENTRY = {
 'entry': '2026-05-16/unit-42-gremlin-stealer-evolved-with-net-resource-xor-obfusc',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (exfiltration sentence)',
   'claim': 'Exfiltration is HTTPS POST to a private web panel; a Telegram Bot API channel is the secondary channel.',
   'defect': 'The post shows the new variant uploading to a plain-HTTP site (defanged "hxxp", i.e. http), not HTTPS, never says POST, and does not rank the Telegram channel as secondary.',
   'ground_truth': 'This variant exfiltrates stolen data to a newly deployed site at hxxp[:]<IP> ... uploads it to the attacker-controlled site / the core architecture and exfiltration methods via private web panels or the Telegram Bot API remain consistent',
   'ground_truth_url': U,
   'fix': 'Exfiltration is by upload of a ZIP archive (named with the victim\'s public IP address) to an attacker-controlled web panel over plain HTTP in the analyzed variant; the Telegram Bot API remains an alternative exfiltration path.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (crypto-clipper sentence)',
   'claim': 'replaces Bitcoin and Ethereum wallet addresses with attacker-controlled equivalents in real time',
   'defect': 'The post names no coin: it says the clipper matches "cryptocurrency wallet patterns" and swaps in the attacker\'s wallet.',
   'ground_truth': 'This crypto clipper functionality continuously monitors the system clipboard for strings matching cryptocurrency wallet patterns. When it detects a match, the malware replaces the victim\'s address with the attacker\'s wallet in real time, diverting funds during transactions.',
   'ground_truth_url': U,
   'fix': 'replaces copied cryptocurrency wallet addresses with the attacker\'s wallet in real time',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (WebSocket session-hijack sentence; Detection line)',
   'claim': 'reads active browser process memory (Chrome-based browsers) to extract session tokens directly from running processes, bypassing the cookie-encryption mitigations modern browsers apply at disk ... Detection: Sysmon EID 10 (process access) targeting `chrome.exe` or `msedge.exe` ...',
   'defect': '(low confidence) The post says the WebSocket module hijacks live browser sessions "by requesting the data directly from the running browser process" and calls it memory-resident; it does not say the module reads process memory or name "cookie-encryption mitigations ... at disk". The Sysmon EID 10 hunt is the entry\'s own composition resting on that unstated memory-read premise, and the post offers no telemetry guidance. "Chrome-based"/Chromium is stated; msedge.exe is not.',
   'ground_truth': 'The WebSocket-based session hijacking module represents its most significant technical upgrade. This allows Gremlin stealer to hijack active, live browser sessions and bypass modern cookie protections by requesting the data directly from the running browser process. / Gremlin now targets Chromium-based browsers. It uses memory-resident techniques to hijack active session tokens and sensitive data directly from running processes',
   'ground_truth_url': U,
   'fix': 'The WebSocket module hijacks live Chromium-based browser sessions by requesting session data directly from the running browser process, bypassing modern cookie protections (Unit 42). Mark the process-access/clipboard hunting line as derived hunting concept, not source guidance, and do not assert a memory-read mechanism.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (credential scope sentence)',
   'claim': 'Credential scope includes browser cookies, session tokens, saved passwords, payment-card details, FTP and VPN credentials, Discord tokens (dedicated regex scanner), clipboard content, and cryptocurrency wallet files.',
   'defect': '"saved passwords" is not in the post\'s list of targeted data (payment cards, cookies, session tokens, wallet data, FTP and VPN credentials, plus clipboard contents and Discord tokens).',
   'ground_truth': 'It targets web browsers, system clipboard and local storage to exfiltrate sensitive information like: Payment card details, Browser cookies, Session tokens, Cryptocurrency wallet data, FTP and VPN credentials',
   'ground_truth_url': U,
   'fix': 'Remove "saved passwords".',
   'class': 'imprecision'},
  {'where': 'summary; body paragraph 1 (sentence 1)',
   'claim': 'adding three new capability tiers operationally relevant to defenders running endpoint detections tuned for older Gremlin samples',
   'defect': '"three new capability tiers" is not a count in the post, which lists the XOR-encoded .NET resource payload, a Discord token module, the clipper and the WebSocket module (and, at its start, a commercial packer with instruction virtualization). The "tuned for older samples" clause is the entry\'s gloss.',
   'ground_truth': 'Gremlin stealer\'s evolution from a basic credential harvester to a modular toolkit is evident in several key architectural upgrades: Expanded target scope (Discord) / Active financial fraud (clipper) / Advanced persistence (WebSocket session hijacking)',
   'ground_truth_url': U,
   'fix': 'Replace the count with the named capabilities; note the commercial packer with instruction virtualization the post leads with.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (T1115 and T1185 links)',
   'claim': '[T1115](https://attack.mitre.org/techniques/T1115/) ... [T1185](https://attack.mitre.org/techniques/T1185/) Browser Session Hijacking',
   'defect': 'The two clauses are cited to ATT&CK pages, not to Unit 42; the T1115 page covers clipboard collection, not address replacement (a transmitted-data manipulation). The post cites no ATT&CK ids; ids belong in techniques[].',
   'ground_truth': 'This crypto clipper functionality continuously monitors the system clipboard ... replaces the victim\'s address with the attacker\'s wallet in real time',
   'ground_truth_url': U,
   'fix': 'Cite the Unit 42 post on these clauses; map T1115 (monitoring) and T1565.002 (replacement) in techniques[].',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Hardening line; closing line; sentences 3-5)',
   'claim': 'Hardening: browser isolation for high-value sessions; clipboard-API access audited in EDR telemetry. Single-source — Unit 42 only; flagged for verification.',
   'defect': 'No inline Unit 42 citation after sentence 1; the hardening line is composed advice no source gives; "Single-source ... flagged for verification" is pipeline self-reference. The post\'s lead (a commercial packer with instruction virtualization) and the control-flow obfuscation are omitted.',
   'ground_truth': 'We analyze a variant protected by a sophisticated commercial packing utility that employs instruction virtualization, transforming the original code into a custom, non-standard bytecode executed by a private virtual machine.',
   'ground_truth_url': U,
   'fix': 'Cite Unit 42 on each clause, mark hardening as derived guidance, replace the closing line with sourcing_note provenance (single vendor research post).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1027.013', 'behavior': 'Malicious payload placed in the .NET resource section and masked with XOR encoding', 'url': U},
   {'id': 'T1027.002', 'behavior': 'Variant protected by a commercial packer with instruction virtualization (custom bytecode on a private VM)', 'url': U},
   {'id': 'T1140', 'behavior': 'Runtime string decoder and staged decryption of critical functions from the resource section only when needed', 'url': U},
   {'id': 'T1115', 'behavior': 'Continuous clipboard monitoring for wallet-address patterns; clipboard contents exfiltrated', 'url': U},
   {'id': 'T1565.002', 'behavior': 'Clipper replaces the victim\'s wallet address with the attacker\'s in real time', 'url': U},
   {'id': 'T1185', 'behavior': 'WebSocket-based module hijacks live browser sessions through the running browser process', 'url': U},
   {'id': 'T1539', 'behavior': 'Browser cookies and session tokens stolen', 'url': U},
   {'id': 'T1555.003', 'behavior': 'Targets web browsers for payment card details and credentials', 'url': U},
   {'id': 'T1528', 'behavior': 'Dedicated Discord token extraction module scanning multiple paths with regex validation', 'url': U},
   {'id': 'T1005', 'behavior': 'Cryptocurrency wallet data and local storage collected', 'url': U},
   {'id': 'T1560', 'behavior': 'Harvested artifacts bundled into a ZIP archive named with the victim public IP', 'url': U},
   {'id': 'T1041', 'behavior': 'Archive uploaded to an attacker-controlled web panel', 'url': U},
   {'id': 'T1567', 'behavior': 'Telegram Bot API as alternative exfiltration channel', 'url': U},
  ],
  'note': 'The post does not describe how Gremlin is delivered or executed first; no initial-access technique is mapped.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Unit 42 is an original research lab analysing samples from its own telemetry; single source, no independent corroboration.'},
  'exposure': [
   {'quote': 'It targets web browsers, system clipboard and local storage to exfiltrate sensitive information like: Payment card details, Browser cookies, Session tokens, Cryptocurrency wallet data, FTP and VPN credentials', 'url': U},
   {'quote': 'By transitioning from a simple data exfiltration tool to a more advanced modular stealer, Gremlin now targets Chromium-based browsers.', 'url': U},
  ],
  'detection': [
   {'quote': 'The malware names the file using the victim\'s public IP address to identify the source, and then uploads it to the attacker-controlled site', 'url': U},
   {'quote': 'This crypto clipper functionality continuously monitors the system clipboard for strings matching cryptocurrency wallet patterns.', 'url': U},
   {'quote': 'Each critical function is decrypted and mapped into memory from the .NET resource section only when needed. This method forces analysts to perform dynamic debugging to observe any meaningful program behavior.', 'url': U},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'Comparing past and present versions reveals a clear evolution in Gremlin stealer\'s anti-analysis techniques. Legacy samples ... lacked obfuscation, leaving function exports and internal symbols intact.', 'url': U},
  ],
  'bodies': [P + 'u42-gremlin.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
aae494f2a6 ¦ ok ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ payload shifted into .NET Resource section with XOR encoding; crypto clipper; WebSocket-based session hijacking module
717804357f ¦ F14 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ (low confidence) post lists "several key architectural upgrades" (Discord module, clipper, WebSocket) plus XOR resource and packer; no "three new capability tiers"
27ce2671a2 ¦ F14 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ date 2026-05-15 and evolved-variant analysis confirmed; "three new capability tiers" is not a count the post gives
2417f46a49 ¦ F4 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ "strings matching cryptocurrency wallet patterns ... replaces the victim's address with the attacker's wallet"; Bitcoin/Ethereum not named; T1115 page does not carry replacement
d0585bfc85 ¦ F4 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ (low confidence) "bypass modern cookie protections by requesting the data directly from the running browser process"; no statement that it reads process memory or about disk cookie encryption
0fcda3fb42 ¦ F5 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ shifted the malicious payload into the .NET Resource section, masking it with XOR encoding; short names a,b,c,hf,ze; decoder method <Module>.c(int,int,int)
604b5d8af2 ¦ F4 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ list: payment card details, cookies, session tokens, wallet data, FTP and VPN credentials, clipboard contents, Discord tokens; "saved passwords" absent
912843647f ¦ F4 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ exfiltrates stolen data to a newly deployed site at hxxp[:]<IP> (plain HTTP); "private web panels or the Telegram Bot API remain consistent"; no POST, no "secondary"
b63e1652d7 ¦ F4 ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ (low confidence) post contains no detection guidance; Sysmon EID 10 hunt rests on an unstated process-memory-read premise
562091abf6 ¦ F5 ¦ null ¦ composed hardening advice (browser isolation, clipboard-API auditing); no fetched source states it
d6846bc45c ¦ ok ¦ https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/ ¦ only Unit 42 cited (true); phrasing "flagged for verification" is pipeline self-reference, logged
'''
