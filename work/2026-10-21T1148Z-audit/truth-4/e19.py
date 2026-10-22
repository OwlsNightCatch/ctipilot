import sys; sys.path.insert(0,'/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4')
from rec import save
B='work/2026-10-21T1148Z-audit/truth-4/bodies/'
L='https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms'
W='https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html'
BC='https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/'
T='https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html'
d={
'entry':'2026-05-22/calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and',
'verdict':'factual-error',
'defects':[
 {'where':'body paragraph 1 (victims); regions',
  'claim':'Confirmed victims include a Middle East ISP, an Afghanistan ISP, and entities in Azerbaijan, the US, and Ukraine; European telecoms are within the actor\'s documented targeting pattern.',
  'defect':'Lumen ties the US and Ukrainian connections to secondary C2 clusters that it believes belong to other PRC-aligned groups sharing the tooling, and calls the US cases "potential compromises". No source documents European telecom targeting; PwC places Red Lamassu\'s targeting in Asia (Kazakhstan, Afghanistan, India). regions: europe follows from this claim.',
  'ground_truth':'Lumen: "we positively confirm at least two victims. We first observed connections from an Outlook server belonging to an Afghanistan-based ISP provider"; "identified two potential compromises—both stemming from the United States"; on Ukraine: "we believe with moderate confidence this focus on the Donbas region is another example of shared tooling among distinct groups." PwC: "associated with the targeting of telecommunications organisations based in Asia, predominantly Kazakhstan, Afghanistan, and India." THN: "an Afghanistan-based internet service provider (ISP) and another unknown entity located in Azerbaijan".',
  'ground_truth_url':L,
  'fix':'"Victims: a Middle East telecom provider, an Afghanistan-based ISP and an entity in Azerbaijan; Lumen links US and Ukrainian connections to separate PRC-aligned clusters using the same tooling." Drop the European-targeting clause and the europe region.',
  'class':'factual-error'},
 {'where':'summary; body paragraph 2; Detection',
  'claim':'Showboat is a modular ELF binary masquerading as a Linux kernel worker thread (`kworker` — `T1036.005 ...`) / kworker-masquerading ELF implant / hunt for `kworker` ELF processes whose parent is not `kthreadd`',
  'defect':'No source says Showboat masquerades as a kernel worker thread: "kworker" is PwC\'s name for the malware family, and the sample in the open directory was named systemd-ac-update. The masquerade, its ATT&CK id and the kthreadd hunt are unsupported.',
  'ground_truth':'PwC: "an ELF binary we respectively call kworker or Showboat"; "the latter being a sample of the kworker malware (which Lumen names Showboat in its blog)", file "systemd-ac-update". Lumen: functions to "hide the agent itself from the process list, obtain persistence as a service".',
  'ground_truth_url':W,
  'fix':'"Showboat (PwC: kworker) is a modular Linux ELF post-exploitation framework that can hide its own process and persist as a service"; drop T1036.005 and the kthreadd hunt, or hunt for the documented behaviours (Pastebin fetch from a server process, SOCKS5 listener, PNG-field beacons).',
  'class':'factual-error'},
 {'where':'body paragraph 1 (actor dating); paragraph 2-3 (capabilities, clustering, ATT&CK ids)',
  'claim':'Calypso (also tracked as Red Lamassu, Bronze Medley — active since at least mid-2022 ...) / providing remote shell, file operations, SOCKS5 proxy, and self-removal / X.509 certificate SAN/CN patterns link the victim set / `T1574.002`',
  'defect':'Mid-2022 is Lumen\'s start date for the Showboat campaign, not the actor (PwC tracks it since 2019; THN cites activity since 2016). JFMBackdoor proxies TCP sessions (not SOCKS5) and also captures screenshots. Lumen clustered C2 infrastructure by certificate fingerprint and subject/issuer DN, not victims by SAN/CN. T1574.002 is revoked in the pinned ATT&CK v20 dataset.',
  'ground_truth':'Lumen: "The campaign has been active since at least mid-2022." PwC: "tracking a China-based threat actor we call Red Lamassu (a.k.a. Calypso) since 2019"; "Network Proxying: Ability to establish TCP proxy sessions"; "Screenshot Capture". attack/enterprise-attack.json: T1574.002 revoked.',
  'ground_truth_url':W,
  'fix':'Date the campaign, not the actor; "TCP proxying, screenshots"; "C2 nodes cluster on a shared self-signed certificate"; use T1574.001 in techniques[] and drop prose ids.',
  'class':'imprecision'},
 {'where':'headline; summary; sources[0].publisher; priority',
  'claim':'...disclosed by Lumen Black Lotus Labs / (BleepingComputer, 2026-05-21) / "Lumen Black Lotus Labs, 2026-05-21" / priority: high',
  'defect':'The headline is cut off ("and PwC ..." missing) and the summary credits BleepingComputer instead of the researchers; the Lumen post is dated 2026-05-20. The high priority rests on the unsourced European targeting claim; the documented victims are in the Middle East and Central/South Asia.',
  'ground_truth':'Lumen page date 2026-05-20; PwC 2026-05-21.',
  'ground_truth_url':L,
  'fix':'Finish the headline, cite Lumen and PwC in the summary, date Lumen 2026-05-20, and reconsider priority on the sourced victim set.',
  'class':'imprecision'},
],
'upgrade':{
 'techniques':[
  {'id':'T1059.004','behavior':'Showboat spawns a remote shell on Linux hosts','url':L},
  {'id':'T1090.001','behavior':'Showboat SOCKS5 and portmap functions pivot to internal hosts not exposed to the internet','url':L},
  {'id':'T1105','behavior':'"hide" command retrieves process-hiding code from Pastebin or forums used as a dead drop','url':L},
  {'id':'T1543.002','behavior':'Showboat can obtain persistence as a service (sample named systemd-ac-update)','url':W},
  {'id':'T1132.001','behavior':'Host data sent to C2 in a PNG field as an encrypted, base64-encoded string','url':L},
  {'id':'T1574.001','behavior':'JFMBackdoor delivered by DLL side-loading: legitimate fltMC.exe loads malicious FLTLIB.dll dropped by a batch script','url':W},
  {'id':'T1113','behavior':'JFMBackdoor captures screenshots, base64-encodes and XOR-encrypts them for exfiltration','url':W},
  {'id':'T1070.006','behavior':'JFMBackdoor file operations include timestomping','url':W},
 ],
 'rating':{'reliability':'B','credibility':1,'basis':'Two independent research teams (Lumen Black Lotus Labs, PwC Threat Intelligence) published coordinated, complementary analyses; PwC makes the Red Lamassu attribution, Lumen says only PRC-aligned clusters. BleepingComputer and THN restate.'},
 'exposure':[
  {'quote':'As the malware was not directly observed on any live systems, we are unable to comment on the initial access vector or exploit.','url':L},
 ],
 'detection':[
  {'quote':'we encourage organizations to be mindful of their perimeter and continue to monitor events such as east-west traffic from servers that do not clearly map to business processes.','url':L},
 ],
 'triage':[],
 'takeaway':[
  {'quote':'The presence of such threats should be taken as an early warning sign, indicating the potential for broader and more serious security issues within affected networks.','url':L},
 ],
 'bodies':[B+'lumen-showboat.txt',B+'pwc-red-lamassu.txt',B+'bc-showboat.txt',B+'thn-showboat.txt'],
 'extra':{'iocs_in_source':'Lumen and PwC list C2 IPs, domains, certificate fingerprints and hashes; none may enter the entry',
          'actor':'Red Lamassu = Calypso (PwC); Bronze Medley alias per THN; PwC: likely operating out of Sichuan Province'},
},
'possible_twin_outside_batch':None,
}
save(d)
