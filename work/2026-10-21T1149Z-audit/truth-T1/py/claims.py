import yaml
U=dict(
 MS='https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585',
 BCYK='https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/',
 REGYK='https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758',
 NCSC='https://security-hub.ncsc.admin.ch/#/posts/12574',
 REC='https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more',
 BCPATCH='https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/',
 BCMINI='https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/',
 GH='https://github.com/TryGhost/Ghost/security/advisories/GHSA-w52v-v783-gw97',
 XL='https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/',
 BCG='https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/',
 D1='https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results',
 D2='https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results',
 D3='https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn',
 BC2='https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/',
 HR='https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/',
 ANN='https://www.thezdi.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026',
 M42='https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897',
 M62='https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62911',
 FR='https://www.frankysweb.de/en/exchange-public-exploit-for-critical-vulnerability-cve-2026-62911/',
)
R=[]
def c(cid,v,u,p):
    assert len(p)<=200,(cid,len(p))
    R.append(dict(claim_id=cid,verdict=v,source_url=(U[u] if u else None),passage=p))
FIXED="Added links to June 2026 Windows security updates.  Microsoft recommends installing this updates as soon as possible."
# entry 1
c('54fe91233d','F4','MS',FIXED)
c('3fd3dfeb97','F4','MS',FIXED)
c('e49a22e725','F4','BCYK','He recommended using a BitLocker PIN and a BIOS password as a mitigation.')
c('566688a254','F4','MS',FIXED)
c('1e8cbaed1c','F4','MS',FIXED)
c('7ba0331694','F14','REGYK','YellowKey and GreenPlasma are the latest in a series of five Microsoft zero-day bugs the researcher has exposed this year.')
c('cc010a3693','F4','BCYK','rather than launching the actual Windows Recovery environment, it pops up a CMD.EXE. With the disk still unlocked')
c('d5252a7d78','ok','BCYK','The researcher says that YellowKey is a BitLocker bypass that affects Windows 11 and Windows Server 2022/2025.')
c('8860f1aedb','F4','BCYK','Windows looks for \\System Volume Information\\FsTx directories on attached drives, and will replay any NTFS logs.')
c('f561d7f3b0','ok','BCYK','An unprivileged user can create arbitrary memory-section objects within directory objects writable by SYSTEM')
c('d1b290edd0','ok','BCYK','GreenPlasma is a privilege escalation security issue that could be exploited to obtain a shell with SYSTEM permissions.')
c('649f13473d','F4','BCYK','a spokesperson stated that the company is committed to investigating reported security issues')
c('39e8109f30','F5','NCSC','Implement BIOS passwords and setting a BitLocker PIN mitigates the current public PoC')
c('956b531347','ok','MS','A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device.')
c('674cb4aa55','ok','NCSC','Microsoft is now tracking the YellowKey flaw under CVE-2026-45585 and shared mitigation measures to defend against potential attacks.')
c('bd830ed909','F3','MS','Microsoft recommends that you consider implementing these mitigations if you are concerned your devices and data are at risk of being compromised or stolen.')
c('0c43acb346','ok','MS','A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device.')
c('0cd478c6ae','ok','MS','An attacker with physical access to the target could exploit this vulnerability to gain access to encrypted data.')
c('9d7ed264fe','F4','MS','No, if you are using TPM+PIN the vulnerability is not exploitable.')
c('3e50a6aba5','F4','MS','Added a script to implement a mitigation and removed the manual mitigations.')
c('435a119fc5','ok','NCSC','Microsoft is now tracking the YellowKey flaw under CVE-2026-45585 and shared mitigation measures to defend against potential attacks.')
# entry 2
c('e9e0b2ec05','F4','REC','The company stopped short of directly threatening legal action')
c('cafa7d5693','F4','REC','In a blogpost on Wednesday, Microsoft said')
c('aa72209f4c','F4','MS','allows an unauthorized attacker to bypass a security feature with a physical attack.')
c('62b277e528','F4','REC','In a blogpost on Wednesday, Microsoft said')
c('3fdccceb65','F4','REC',"The researcher threatened a further release on July 14 — the date scheduled for Microsoft's Patch Tuesday")
c('ff2fb46b58','ok','REC',"have been exploited in live intrusions, according to Microsoft's own patch advisories.")
c('c67b542d38','ok','REC','have no patches and no confirmed exploitation as of publication.')
c('e7af3c6bff','F5','BCMINI','the exact same issue that was reported to Microsoft by Google project zero is actually still present, unpatched')
c('bd80d8ae45','ok','REC',"The researcher threatened a further release on July 14 — the date scheduled for Microsoft's Patch Tuesday")
c('bcb46e1c37','F5','BCMINI','organizations should monitor the following Registry keys for modifications using their EDR platform to detect exploitation')
c('2b8eaa576c','F4','BCPATCH','On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday updates.')
# entry 3
c('1d57dabce5','ok','XL','we have cumulatively identified more than 700 poisoned victim domains')
c('a6e0975976','F3','XL','we have cumulatively identified more than 700 poisoned victim domains')
c('4b96579066','ok','GH','This vulnerability is present in Ghost v3.24.0 to v6.19.0.')
c('3aff790eab','ok','GH','as this vulnerability lets an attacker gain access to a site\'s API keys, we recommend reviewing staff users and rotating keys.')
c('5de384e922','ok','GH','As a temporary mitigation, a reverse proxy or WAF rule can be used to block Content API requests containing slug%3A%5B or slug:[ in the query string filter parameter.')
c('1ac12c2800','ok','XL','2026-05-10: First Round of Compromised Site Enumeration Completed: 156 victim domains confirmed.')
c('aa29cee47e','ok','XL','then used the Ghost Admin API to tamper with articles in bulk, injecting malicious JavaScript loaders at the bottom of the pages')
c('ff90d465f5','ok','XL','it uses the setLoginItemSettings API built into the Electron framework to achieve persistence; every 30 seconds, it sends a POST request to the remote server')
c('ab0aa1eed6','ok','BCG','confirmed impact on more than 700 domains, including university portals, AI/SaaS companies, media outlets, fintech firms, security sites, and personal blogs.')
c('238a9866b7','F3','GH','This vulnerability is present in Ghost v3.24.0 to v6.19.0.')
c('26533f718f','ok','XL','Whether there are abnormal PUT /ghost/api/admin/posts/:id/ requests, especially those from unfamiliar IPs, abnormal UAs, or bulk modifications in a short period of time')
c('579d165174','ok','XL','1. Use the WIN+R shortcut to open the command window')
c('c9e528c717','ok','XL','Rotate all credentials: Admin API Key, Content API Key, administrator password, Session')
c('54de0ae3f5','ok','GH','The Content API key is public by design, so restricting key access does not mitigate this vulnerability.')
c('c4d8e228f2','ok','GH','The Content API key is public by design, so restricting key access does not mitigate this vulnerability.')
c('58df173ff4','F4','BCG','an Electron-based malware sample named UtilifySetup.exe')
# entry 4
c('f81c6e2d7e','ok','BCG','A large-scale campaign is exploiting a critical SQL injection vulnerability (CVE-2026-26980) in Ghost CMS to inject malicious JavaScript code that triggers ClickFix attack flows.')
c('44ff2eecf0','ok','BCG','According to the researchers, threat actors planted malicious code on the websites of Harvard University, Oxford University, Auburn University, and DuckDuckGo.')
c('71e5c58581','ok','BCG','According to the researchers, threat actors planted malicious code on the websites of Harvard University, Oxford University, Auburn University, and DuckDuckGo.')
c('56967a9744','F3','BCG','The page instructs victims to verify that they are human by pasting a provided command on their Windows command prompt, which drops a payload on their systems.')
c('ed29216a3a','ok','BCG','The attacks that XLab observed begin by exploiting CVE-2026-26980 to steal the admin API keys, and then use the elevated rights to inject malicious JavaScript into articles.')
c('f3fc6958cf','F4','XL','covering multiple industries such as universities, blockchain, AI / SaaS, security research, media, and fintech.')
c('745b92cf7b','F14','XL','real victims will receive the malicious payload, while security researchers or crawlers will only see a harmless "safe page"')
c('0ee6a378b6','F4','XL','1. Use the WIN+R shortcut to open the command window')
# entry 5
c('d0e23ff4b6','F4','ANN','AI Databases, Coding Agents, Local Inferences, and a separate category for NVIDIA products.')
c('b55daeb831','F4','D1','FAILURE - Unfortunately, Park Jae Min could not get their exploit of Oracle Autonomous AI Database working within the time allotted.')
c('18777fbbd3','F4','D1','k3vg3n chained 3 bugs including SSRF and Code Injection to take down LiteLLM.')
c('b3ef3a2f53','F3','D2','chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points.')
c('15c018fc1b','F3','D3','used a Memory Corruption bug to exploit VMware ESXi with the Cross-tenant Code Execution add-on, earning $200,000 and 20 Master of Pwn points.')
c('30fa352c42','F3','D1','chained 5 bugs (incl. SSRF and Code Injection) to exploit LM Studio, earning $40,000 and 4 Master of Pwn points.')
c('75a7791711','F3','D3','used an integer overflow to escalate privileges on #Windows 11.')
c('16db3fbfa6','F4','ANN','After our inaugural competition last year, Pwn2Own returns to Berlin and OffensiveCon.')
c('f004fd63bd','F4','BC2','Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own.')
c('40ea354949','F14','ANN','After our inaugural competition last year, Pwn2Own returns to Berlin and OffensiveCon.')
c('d2cf7b67bd','F5','BC2','Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own.')
c('d3aab99ffd','F14','HR','For the first time in 19 years, Pwn2Own Berlin 2026 has reportedly run out of space.')
c('e9bd7c8752','ok','D3','DEVCORE claimed the title of Master of Pwn with a commanding 50.5 points and $505,000')
c('1c9264e88a','F14','D3','bringing the final totals to $1,298,250 awarded for 47 unique 0-day vulnerabilities across three days of competition.')
c('5988934e86','F4','M62','allows an authorized attacker to elevate privileges over a network')
c('84905a12ea','F4','M62','Authentication bypass by capture-replay in Microsoft Exchange Server allows an authorized attacker to elevate privileges over a network.')
c('c7d613377e','F5','BC2','Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own.')
c('4f325455f8','F4','M42','Added links to June 2026 Exchange Server security updates.  Microsoft recommends installing this updates as soon as possible.')
c('08d4af6d2b','F5',None,'(none: no cited page contains EEMS or posture advice; the ZDI day pages list contest results only)')
c('659a183f08','F5','ANN','Last year, we added Artificial Intelligence as a category with great results.')
c('8da5417b29','F4','D3','hitting a one-vulnerability collision with a previous attempt')
c('e097fc1e0c','F4','D2','used a Code Injection bug to exploit LM Studio in the second round, earning $20,000 and 4 Master of Pwn points.')
c('f84612d891','F4','D1','chained 5 bugs (incl. SSRF and Code Injection) to exploit LM Studio, earning $40,000 and 4 Master of Pwn points.')
c('5c8aac6141','ok','D2','used a Code Injection bug to exploit LM Studio in the second round, earning $20,000 and 4 Master of Pwn points.')
c('91b89867ef','F4','D1','used a single CWE-150 bug to exploit OpenAI Codex, earning $40,000 and 4 Master of Pwn points.')
c('687a699753','F5',None,'(none: no cited page describes localhost reachability, SSRF telemetry or SOC tooling baselines)')
c('30315373b0','F4',None,'(none: no cited page says anything about Swiss, EU, federal or cantonal adoption of coding agents)')
c('e826ff04d4','F4','ANN','The contest begins on May 14, but registration closes on May 7, so don\'t delay in getting those submissions in.')
c('2807a6cfdc','F4','HR','Because they were rejected, dozens of researchers are now releasing their secrets for free.')
c('82d698a7a8','F4','BC2','Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own.')
c('4670fe6868','ok',None,'(advice only; no factual claim to verify)')
# entry 6
c('c5e0480e56','ok','D2','chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points.')
c('adcd1c603c','ok','D2','chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points.')
c('b1a53e6c11','ok','D2','Orange Tsai (@orange_8361) of DEVCORE Research Team chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points.')
c('c4daa33e77','ok','BC2','Cheng-Da Tsai (also known as Orange Tsai) of DEVCORE Research Team earning $200,000 after chaining three bugs to gain remote code execution with SYSTEM privileges on Microsoft Exchange.')
c('6dafc00970','ok','BC2','Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own.')
c('9adb01635b','ok','M42','Improper neutralization of input during web page generation (\'cross-site scripting\') in Microsoft Exchange Server allows an unauthorized attacker to perform spoofing over a network.')
c('aa1f3b23ba','ok','FR','Working exploit code has surfaced for the critical Exchange vulnerability CVE-2026-62911 from the August update.')
c('7ecb66b56b','ok','D2','chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points.')
c('41946badb0','ok','M42','Improper neutralization of input during web page generation (\'cross-site scripting\') in Microsoft Exchange Server allows an unauthorized attacker to perform spoofing over a network.')
c('a5b282cbb8','ok','FR','He demonstrated the vulnerability at Pwn2Own Berlin 2026, where it was part of a chain of three vulnerabilities')
c('f76ff0c1d6','ok',None,'(editorial rationale for the priority change; no source claim)')
c('3a57825fd2','ok','BC2','Cheng-Da Tsai (also known as Orange Tsai) of DEVCORE Research Team earning $200,000 after chaining three bugs to gain remote code execution with SYSTEM privileges on Microsoft Exchange.')
led=yaml.safe_load(open('/home/user/ctipilot/work/2026-10-21T1149Z-audit/truth-T1.ledger.yaml'))['claims']
ids=[x['claim_id'] for x in led]
got=[r['claim_id'] for r in R]
assert sorted(ids)==sorted(got),(set(ids)-set(got),set(got)-set(ids))
assert len(set(got))==len(got)==99
# order as ledger
by={r['claim_id']:r for r in R}
out=[by[i] for i in ids]
with open('/home/user/ctipilot/work/2026-10-21T1149Z-audit/truth-T1.claims.yaml','w') as f:
    f.write('# run_id: 2026-10-21T1149Z-audit\n# batch: T1\nclaims:\n')
    for r in out:
        f.write('  - '+yaml.safe_dump(r,default_flow_style=True,width=10000,allow_unicode=True).strip().replace('\n',' ')+'\n')
from collections import Counter
print(Counter(r['verdict'] for r in out))
