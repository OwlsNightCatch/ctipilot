P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
SL = 'https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/'
ENTRY = {
 'entry': '2026-05-17/kaspersky-great-documents-kimsuky-s-rust-based-hellodoor-and',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'evidence[0]; body paragraph 1 (Kaspersky verbatim quote)',
   'claim': '"Kimsuky has continuously introduced new malware variants based on the PebbleDash platform, a tool historically leveraged by the Lazarus Group but appropriated by Kimsuky since at least 2021... including the use of VSCode Tunneling, Cloudflare Quick Tunnels, DWAgent, large language models (LLMs), and the Rust programming language"',
   'defect': 'Not a contiguous passage: the inserted ellipsis splices the end of one sentence onto the middle of the next and drops "Our monitoring indicates various strategic updates to the group\'s arsenal".',
   'ground_truth': 'Kimsuky has continuously introduced new malware variants based on the PebbleDash platform, a tool historically leveraged by the Lazarus Group but appropriated by Kimsuky since at least 2021. Our monitoring indicates various strategic updates to the group\'s arsenal, including the use of VSCode Tunneling, Cloudflare Quick Tunnels, DWAgent, large language models (LLMs), and the Rust programming language.',
   'ground_truth_url': SL,
   'fix': 'Quote one sentence whole, for example "Our monitoring indicates various strategic updates to the group\'s arsenal, including the use of VSCode Tunneling, Cloudflare Quick Tunnels, DWAgent, large language models (LLMs), and the Rust programming language."',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (secondary additions sentence)',
   'claim': 'secondary additions are httpMalice (HTTP-only loader), MemLoad (reflective DLL loader), httpTroy (C2 backdoor)',
   'defect': 'httpMalice is a backdoor, not a loader, and not HTTP-only: Kaspersky describes version 1.9 over HTTP/HTTPS and the older version 1.8 over the Dropbox API. MemLoad and httpTroy are not new additions either (MemLoad versions since early 2025; httpTroy already documented by Gen Digital).',
   'ground_truth': 'The latest PebbleDash-based backdoor, httpMalice, emerged no later than December 2025 ... version 1.9 communicates over HTTP and version 1.8 uses Dropbox. / Since early 2025, we have observed several versions of MemLoad ... Since Gen Digital covers httpTroy\'s features and functionality in detail elsewhere',
   'ground_truth_url': SL,
   'fix': 'also covered: httpMalice (PebbleDash-based backdoor; HTTP/HTTPS in v1.9, Dropbox API in v1.8), MemLoad (loader that reflectively runs httpTroy in memory after anti-VM checks), httpTroy (long-term access and exfiltration backdoor), AppleSeed and HappyDoor.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Detection guidance sentence); actions[0]',
   'claim': 'Detection guidance from Kaspersky (paraphrased to avoid IOC reproduction): ... alert on Rust-compiled PE images loading from non-standard paths and on outbound `*.trycloudflare.com` connections that don\'t match a developer\'s legitimate tunnel-use profile.',
   'defect': 'The article contains no detection guidance; it is an analysis with IoCs. The dropper, scheduled-task and VSCode-tunnel items paraphrase observed behavior, but the Rust-PE and trycloudflare-profile items appear nowhere in it. Attributing the list to Kaspersky is unsupported.',
   'ground_truth': 'JSE droppers contain a minimum of two Base64-encoded blobs ... If elevated, the task is named ChromeCheck ... Otherwise, the task is named EdgeCheck / For VSCode, the attacker uses GitHub authentication method. (observations, no guidance section)',
   'ground_truth_url': SL,
   'fix': 'Present a Detection line derived from Kaspersky\'s observations, labelled as such: JSE/SCR/PIF droppers that decode Base64 blobs (certutil -decode) and launch DLLs via regsvr32 or rundll32; per-minute scheduled tasks running regsvr32 on a DLL; HKCU Run values launching regsvr32; VSCode CLI (code.exe tunnel) unpacked to C:\\Users\\Public with GitHub device-code authentication; DWAgent installed from C:\\ProgramData. Drop the Rust-PE and trycloudflare-profile items or mark them as the entry\'s own.',
   'class': 'factual-error'},
  {'where': 'summary; body paragraph 1 (sentence 1)',
   'claim': 'campaigns observed during late 2025 and Q1 2026, documenting six malware families the actor is currently rotating',
   'defect': 'The six families are right, but the period is wrong: HelloDoor was first identified in August 2025 and MemLoad versions date from early 2025; Kaspersky says only "over the past few months". "currently rotating" is the entry\'s gloss.',
   'ground_truth': 'HelloDoor is a DLL-based backdoor first identified in August 2025. / Since early 2025, we have observed several versions of MemLoad / The report covers the following PebbleDash malware: HelloDoor, httpMalice, MemLoad, httpTroy. It also covers AppleSeed and HappyDoor',
   'ground_truth_url': SL,
   'fix': 'covering Kimsuky activity from 2025 into early 2026 (samples dated August 2025 to February 2026), documenting six malware families',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (TryCloudflare sentence)',
   'claim': 'The most operationally significant capability change is that HelloDoor\'s C2 channel uses Cloudflare Quick Tunnels via TryCloudflare — short-lived `*.trycloudflare.com` hostnames ..., eliminating fixed C2 IPs and making network-layer indicator blocking impractical.',
   'defect': 'Kaspersky calls HelloDoor limited and probably early-stage, and frames the notable shifts as VSCode tunneling and DWAgent; it says TryCloudflare makes the infrastructure "difficult to trace", not that IP-based blocking becomes impractical. It also says tunneling services (Cloudflare Quick Tunnels, VSCode Tunneling, Ngrok) are used across the PebbleDash cluster, not only by HelloDoor.',
   'ground_truth': 'Since it has limited capabilities and a simplistic communication mechanism, the backdoor is most probably in the early stages of development. Nevertheless, it is noteworthy that HelloDoor employs a C2 server hosted through TryCloudflare ... making the infrastructure behind it difficult to trace.',
   'ground_truth_url': SL,
   'fix': 'HelloDoor, which Kaspersky judges early-stage, uses a C2 hosted through TryCloudflare (Cloudflare Quick Tunnels), which makes the infrastructure difficult to trace; the group also tunnels C2 through VSCode Tunneling and Ngrok.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Reported targeting sentence); actions[0]',
   'claim': 'Reported targeting: South Korean government, defence and medical sectors as the primary set, with documented spillover hits in Germany — the closest geographic proximity to Swiss government targets in recent Kimsuky reporting.',
   'defect': 'Kaspersky names a German defense firm among PebbleDash victims "throughout the past several years" and also Brazil, which is omitted; the German victim is not government and its date is not stated, so "recent" and the Swiss-government proximity framing are the entry\'s own.',
   'ground_truth': 'The PebbleDash cluster compromised Brazilian and South Korean defense organizations throughout the past several years, as well as a German defense firm. / Kimsuky mainly targets South Korean entities. However, PebbleDash attacks were also seen in Brazil and Germany.',
   'ground_truth_url': SL,
   'fix': 'Targets are mainly South Korean public and private entities (AppleSeed: government; PebbleDash: defense, also medical and military); PebbleDash victims also include Brazilian defense organizations and a German defense firm over several years.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (closing sentences; Technique class line); actions[0]',
   'claim': '**[SINGLE-SOURCE]** — only Kaspersky GReAT carries this depth ... Marked at edge of the 72 h developing window ... Reference: § 3 Kimsuky item. / Technique class: `T1071.001` ... + `T1090.002` External Proxy + `T1053.005` Scheduled Task. / flag scheduled tasks ... (e.g. `ChromeCheck`, `EdgeCheck`)',
   'defect': 'Pipeline self-reference (single-source flag, "72 h developing window", "run start", "§ 3 Kimsuky item") in reader text; "only Kaspersky carries this depth" is contradicted by the article itself, which defers to Gen Digital for httpTroy and cites AhnLab and Darktrace. The tunnel behavior fits T1572 Protocol Tunneling better than T1090.002, and the inline ids belong in techniques[]. The literal task names are artifact indicators the IOC rule may catch. Only sentence 1 carries a citation.',
   'ground_truth': 'Since Gen Digital covers httpTroy\'s features and functionality in detail elsewhere, we will not provide a thorough explanation here / they actively leverage tunneling services such as Cloudflare Quick Tunnels, VSCode Tunneling, and Ngrok to hide their infrastructure',
   'ground_truth_url': SL,
   'fix': 'Drop the self-reference lines; cite Securelist on each clause; describe the tasks as "per-minute scheduled tasks named after browser checks" instead of literal names; move the mapping into techniques[] (see upgrade).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1566.001', 'behavior': 'Spear-phishing emails with attachments disguised as documents (compressed JSE/EXE/PIF/SCR droppers)', 'url': SL},
   {'id': 'T1204.002', 'behavior': 'Recipient opens a dropper disguised as a quotation, job offer, survey or government document', 'url': SL},
   {'id': 'T1036.007', 'behavior': 'Lure filenames with document extensions before .jse/.pif', 'url': SL},
   {'id': 'T1059.007', 'behavior': 'JSE droppers decode Base64 blobs with JScript', 'url': SL},
   {'id': 'T1140', 'behavior': 'Second Base64 decode with certutil -decode launched from hidden PowerShell; XOR-encrypted payloads in SCR/PIF droppers', 'url': SL},
   {'id': 'T1218.010', 'behavior': 'Payloads executed with regsvr32.exe /s', 'url': SL},
   {'id': 'T1218.011', 'behavior': 'Payloads executed with rundll32.exe and an export function', 'url': SL},
   {'id': 'T1547.001', 'behavior': 'HelloDoor and httpMalice persist through HKCU Run values launching regsvr32/rundll32', 'url': SL},
   {'id': 'T1053.005', 'behavior': 'MemLoad persists via per-minute scheduled tasks running regsvr32 on its DLL', 'url': SL},
   {'id': 'T1543.003', 'behavior': 'httpMalice creates a Windows service when running elevated', 'url': SL},
   {'id': 'T1497.001', 'behavior': 'MemLoad runs anti-VM checks and reconnaissance before fetching httpTroy', 'url': SL},
   {'id': 'T1620', 'behavior': 'MemLoad decrypts and reflectively loads the httpTroy payload in memory', 'url': SL},
   {'id': 'T1071.001', 'behavior': 'HelloDoor and httpMalice C2 over HTTP/HTTPS with three-parameter query strings', 'url': SL},
   {'id': 'T1102.002', 'behavior': 'httpMalice v1.8 uses the Dropbox API for C2', 'url': SL},
   {'id': 'T1573.001', 'behavior': 'RC4 and ChaCha20 encryption of C2 traffic and payloads', 'url': SL},
   {'id': 'T1572', 'behavior': 'C2 hidden behind TryCloudflare (Cloudflare Quick Tunnels), VSCode Tunneling and Ngrok', 'url': SL},
   {'id': 'T1219', 'behavior': 'Legitimate VSCode Remote Tunneling (GitHub device-code auth) and DWAgent RMM for post-exploitation access', 'url': SL},
   {'id': 'T1113', 'behavior': 'httpMalice sends screen captures', 'url': SL},
   {'id': 'T1560', 'behavior': 'httpMalice archives directories before upload', 'url': SL},
   {'id': 'T1056.001', 'behavior': 'AppleSeed Spy collects keystrokes', 'url': SL},
   {'id': 'T1553.002', 'behavior': 'Samples signed with stolen legitimate certificates from South Korean organizations', 'url': SL},
  ],
  'note': 'All ids checked active in attack/enterprise-attack.json. T1090.002 in the entry is weaker than T1572 for the tunnel behavior.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Kaspersky GReAT/Securelist is an original research lab analysing its own telemetry; single source in the entry. Some families are corroborated by other vendors the article cites (Gen Digital on httpTroy, AhnLab on HappyDoor, Darktrace on VSCode tunneling) but the new HelloDoor/httpMalice findings are Kaspersky-only.'},
  'exposure': [
   {'quote': 'Kimsuky mainly targets South Korean entities. However, PebbleDash attacks were also seen in Brazil and Germany. This malware cluster focuses on defense sector, while AppleSeed most often targets government organizations.', 'url': SL},
   {'quote': 'Kimsuky obtains initial access to target systems by delivering spear-phishing emails containing malicious attachments disguised as documents.', 'url': SL},
  ],
  'detection': [
   {'quote': 'The malicious payload leverages powershell.exe -windowstyle hidden certutil -decode [src path] [dst path] for the second Base64 decoding before execution. Ultimately, the malicious payload is executed via command-line instructions such as regsvr32.exe /s [file path] or rundll32.exe [file path] [export function].', 'url': SL},
   {'quote': 'the JSE dropper downloads a legitimate Visual Studio Code (VSCode) CLI onto the infected device. The script establishes persistence by creating a tunnel via the application', 'url': SL},
   {'quote': 'The targeted device then begins communicating with Microsoft-owned servers without the user realizing that the communication is from an attacker.', 'url': SL},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'For post-exploitation activities Kimsuky uses legitimate tools Visual Studio Code (VSCode) and DWAgent. For VSCode, the attacker uses GitHub authentication method.', 'url': SL},
  ],
  'bodies': [P + 'kim-securelist.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
65a92eb962 ¦ ok ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ HelloDoor: first Rust-based PebbleDash variant ... employs a C2 server hosted through TryCloudflare
c57af1a725 ¦ F3 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ six families confirmed (HelloDoor, httpMalice, MemLoad, httpTroy, AppleSeed, HappyDoor); HelloDoor "first identified in August 2025", MemLoad "since early 2025" (not late 2025/Q1 2026)
0efef38f99 ¦ F4 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ no Rust-PE or trycloudflare-profile guidance in article; German victim is "a German defense firm" over "the past several years"
c3a9c925a1 ¦ F3 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ date 2026-05-14 and aliases APT43/Ruby Sleet confirmed; period stated in article is "Over the past few months", samples Aug 2025-Feb 2026
e8aa1f429b ¦ F4 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ "The latest PebbleDash-based backdoor, httpMalice ... version 1.9 communicates over HTTP and version 1.8 uses Dropbox" (backdoor, not HTTP-only loader)
b2081aec85 ¦ F5 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ HelloDoor C2 via TryCloudflare "making the infrastructure behind it difficult to trace"; HelloDoor "most probably in the early stages of development"
18f332ccca ¦ F4 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ quote splices two sentences with "..."; targeting: "compromised Brazilian and South Korean defense organizations ... as well as a German defense firm" (not recent/government)
6f990f54cd ¦ F4 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ article has no detection guidance; JSE droppers with Base64 blobs and ChromeCheck/EdgeCheck tasks are observations
ae87a80b71 ¦ F4 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ VSCode GitHub-auth tunnels observed; "Rust-compiled PE images loading from non-standard paths" and trycloudflare-profile alert in no source
3927aa50e6 ¦ ok ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ HTTP C2 (T1071.001) and schtasks persistence (T1053.005) supported; T1090.002 weaker than T1572 for tunnels (logged)
bb6ce63d20 ¦ F14 ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ article defers to Gen Digital for httpTroy detail and cites AhnLab and Darktrace; "only Kaspersky GReAT carries this depth" unsupported
c19a6d57d3 ¦ ok ¦ https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/ ¦ publication date 2026-05-14 confirmed; "72 h developing window"/"run start" is pipeline self-reference (logged)
'''
