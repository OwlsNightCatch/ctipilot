P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
BC = 'https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/'
TH = 'https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html'
MO = 'https://moselwal.com/blog/dirtydecrypt-linux-kernel-rxgk-cve-2026-31635'
CNA = 'https://cveawg.mitre.org/api/cve/CVE-2026-31635'
V12 = 'https://api.github.com/repos/v12-security/pocs/commits?path=dirtydecrypt&per_page=5'
ENTRY = {
 'entry': '2026-05-20/cve-2026-31635-dirtydecrypt-linux-kernel-rxgk-page-cache-wri',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (PoC sentence); actions[0]; sources[0].publisher',
   'claim': 'A **working PoC was published by V12 on 2026-05-19** / Public PoC released 2026-05-19 ([BleepingComputer, 2026-05-19](...))',
   'defect': 'V12 committed the PoC on 2026-05-17 and BleepingComputer reported it in an article dated 2026-05-18; 2026-05-19 is The Hacker News date.',
   'ground_truth': 'V12 repository commit "add dirtydecrypt / dirtycbc" at 2026-05-17T02:26:21Z; BleepingComputer article dated 2026-05-18: "A recently patched local privilege escalation vulnerability in the Linux kernel\'s rxgk module now has a proof-of-concept exploit"',
   'ground_truth_url': V12,
   'fix': 'V12 published a working PoC on 2026-05-17 (BleepingComputer, 2026-05-18; The Hacker News, 2026-05-19).',
   'class': 'factual-error'},
  {'where': 'title; headline; summary; cves[CVE-2026-31635]',
   'claim': 'CVE-2026-31635 is a page-cache write due to a missing copy-on-write guard in rxgk_decrypt_skb() / "cvss": "7.5", "vector": "local", type lpe',
   'defect': 'The CVE binding is contested and not surfaced. The kernel CNA record for CVE-2026-31635 describes a different fix ("rxrpc: fix oversized RESPONSE authenticator length check": an inverted auth_len check lets oversized authenticators reach rxgk_decrypt_skb() and hit BUG_ON), scored CVSS 3.1 7.5 as a network denial of service (AV:N/C:N/I:N/A:H). BleepingComputer says the flaw has no official CVE and the mapping rests on Will Dormann\'s reading; THN bases it on NVD linking the PoC. The 7.5 and its network vector belong to the CNA\'s DoS description, not to an LPE.',
   'ground_truth': 'CNA title: rxrpc: fix oversized RESPONSE authenticator length check ... The existing check is inverted, so oversized RESPONSE authenticators are accepted and passed to rxgk_decrypt_skb(), which can later reach skb_to_sgvec() with an impossible length and hit BUG_ON(len). CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 7.5 / BleepingComputer: "While there is no official CVE ID associated with this security flaw, according to Will Dormann ... the information ... aligns with the details of CVE-2026-31635"',
   'ground_truth_url': CNA,
   'fix': 'DirtyDecrypt (DirtyCBC) is a page-cache write from a missing copy-on-write guard in rxgk_decrypt_skb() (V12); researchers map it to CVE-2026-31635. Contradiction: the kernel CNA describes CVE-2026-31635 as an inverted RESPONSE length check causing BUG_ON, scored 7.5 (network DoS). Keep cvss with that attribution or leave it null for the LPE.',
   'class': 'factual-error'},
  {'where': 'summary; body paragraph 1 (sentence 1)',
   'claim': 'in `rxgk_decrypt_skb()` in `net/rxrpc/rxgk_crypt.c`',
   'defect': 'No source names rxgk_crypt.c; the CNA stack trace places rxgk_decrypt_skb() in net/rxrpc/rxgk_common.h and lists net/rxrpc/rxgk.c as the program file.',
   'ground_truth': 'rxgk_decrypt_skb() [net/rxrpc/rxgk_common.h:81] ... "programFiles": ["net/rxrpc/rxgk.c"]',
   'ground_truth_url': CNA,
   'fix': 'in rxgk_decrypt_skb() (net/rxrpc, RxGK)',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Debian/RHEL/Ubuntu sentence)',
   'claim': 'Debian Stable, RHEL, and Ubuntu LTS build kernels without `CONFIG_RXGK` and are not affected.',
   'defect': 'No readable source states this. The CNA record limits affected kernels to 6.16 and later (fixed 6.18.23, 6.19.13, 7.0), which is the sourced exposure boundary; BleepingComputer adds that V12\'s PoC was only tested on Fedora and mainline.',
   'ground_truth': 'versions: 6.16 affected; 0 lessThan 6.16 unaffected; 6.18.23 (6.18.*) unaffected; 6.19.13 (6.19.*) unaffected; 7.0 unaffected / V12\'s proof-of-concept exploit has only been tested against Fedora and the mainline Linux kernel.',
   'ground_truth_url': CNA,
   'fix': 'Affected: kernels 6.16 up to before 6.18.23 / 6.19.13 built with CONFIG_RXGK (in practice rolling or recent distributions such as Fedora, Arch, openSUSE Tumbleweed); kernels older than 6.16 are outside the affected range.',
   'class': 'factual-error'},
  {'where': 'sources[1]; body paragraph 1 (Moselwal clause)',
   'claim': 'the [Moselwal technical write-up](https://moselwal.com/blog/dirtydecrypt-linux-kernel-rxgk-cve-2026-31635) characterises the LPE class as in the 7.8–8.1 range without a settled NVD score',
   'defect': 'The Moselwal URL is dead: moselwal.com does not resolve (DNS failure on the bridge, reader and WebFetch). The 7.8-8.1 range cannot be checked and no other source carries it.',
   'ground_truth': 'fetch_source: cannot resolve moselwal.com (No address associated with hostname); WebFetch: getaddrinfo ENOTFOUND moselwal.com',
   'ground_truth_url': MO,
   'fix': 'Remove the Moselwal source and the 7.8-8.1 range; THN quotes Moselwal on the mechanism if a corroborating quote is needed.',
   'class': 'factual-error'},
  {'where': 'cves[] affected/fixed; event_date; body paragraph 1 (disclosure sentence)',
   'claim': '"affected": null, "fixed": null / event_date: null / Researchers at Zellic/V12 disclosed the issue on 2026-05-09; kernel maintainers traced the regression and noted it was a duplicate of a vulnerability quietly patched in mainline on 2026-04-25.',
   'defect': 'Affected/fixed versions are in the CNA record. May 9 is when V12 reported the bug to maintainers, not a public disclosure; "traced the regression" is unsupported; Delphos Labs found and reported the same flaw independently (DirtyCBC) and is omitted. event_date should be set.',
   'ground_truth': '"We found and reported this on May 9, 2026, but was informed it was a duplicate by the maintainers," V12 said. ... this security flaw was also autonomously found and reported by Delphos Labs and the V12 security team',
   'ground_truth_url': BC,
   'fix': 'affected ">= 6.16, < 6.18.23 / < 6.19.13"; fixed "6.18.23, 6.19.13, 7.0"; V12 (with Zellic) and Delphos Labs reported it in May; maintainers said it duplicated a fix already in mainline (patched 2026-04-25); event_date 2026-05-17.',
   'class': 'imprecision'},
  {'where': 'body paragraph 2 (Mitigation and Detection sentences)',
   'claim': 'temporarily blacklist the `rxrpc` module via `/etc/modprobe.d/` — the latter breaks IPsec/AFS-VPN ... Detection: Falco / Tetragon rules on unexpected `rxrpc` module load events; Sysmon-for-Linux EID 8 for UID changes from unprivileged processes',
   'defect': 'The sourced mitigation blocks esp4, esp6 and rxrpc together; blocking rxrpc breaks AFS, the esp modules break IPsec. (low confidence) Sysmon for Linux has no event 8 for UID changes; the detection list is composed and uncited. THN notes the container-escape angle (worker nodes) that supports the container alert.',
   'ground_truth': 'those who can\'t immediately patch their devices should use the same mitigation used for Dirty Frag (however, this will also break IPsec VPNs and AFS distributed network file systems) / In containerized environments, worker nodes running a vulnerable version of Linux could provide a pathway to escape the pod.',
   'ground_truth_url': BC,
   'fix': 'Mitigation per BleepingComputer: block esp4, esp6 and rxrpc via modprobe.d (breaks IPsec VPNs and AFS); mark detection as derived and drop the Sysmon EID 8 item.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1068', 'behavior': 'Unprivileged local user writes to the page cache of privileged files or SUID binaries through the missing copy-on-write guard, gaining root', 'url': TH},
   {'id': 'T1611', 'behavior': 'On vulnerable container worker nodes the flaw could provide a pathway to escape the pod', 'url': TH},
  ],
  'note': 'Local exploit; no access vector beyond local code execution.',
  'cve_facts': {'CVE-2026-31635': {'cna': 'Linux kernel CNA, published 2026-04-24', 'cna_title': 'rxrpc: fix oversized RESPONSE authenticator length check', 'cvss_3_1_cna': '7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)', 'affected': '6.16 up to before 6.18.23 / 6.19.13', 'fixed': '6.18.23, 6.19.13, 7.0', 'ssvc': 'Exploitation poc (CISA ADP 2026-05-18)', 'kev': 'not in CISA KEV 2026-10-21', 'mapping': 'DirtyDecrypt/DirtyCBC mapped to this CVE by Will Dormann and NVD PoC link; CNA text describes a length-check BUG_ON'}},
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'BleepingComputer and THN report the discoverers\' (V12/Zellic, Delphos Labs) statements and PoC; the CVE binding is contested by the CNA description, which would be credibility 3 on its own.'},
  'exposure': [
   {'quote': 'Successful exploitation requires running a Linux kernel with the CONFIG_RXGK configuration option, which enables RxGK security support for the Andrew File System (AFS) client and network transport.', 'url': BC},
   {'quote': 'This limits the attack surface to Linux distributions that closely follow the latest upstream kernel releases, including Fedora, Arch Linux, and openSUSE Tumbleweed.', 'url': BC},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'Linux users on distros potentially affected by this security flaw are advised to install the latest kernel updates as soon as possible.', 'url': BC},
  ],
  'bodies': [P + 'dd-bc.txt', P + 'dd-thn.txt', P + 'dd-cverecord-31635.txt', P + 'dd-v12-commits.txt'],
 },
 'possible_twin_outside_batch': 'not a twin: entries/2026-05-20/vm2-node-js-sandbox-12-critical-cves-cve-2026-43997-43999-44 carries a CVE-2026-31635 summary-table row citing the same dead Moselwal URL',
}
CLAIMS = '''
af8d154135 ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-31635 ¦ (low confidence) CNA describes CVE-2026-31635 as "rxrpc: fix oversized RESPONSE authenticator length check" (BUG_ON); BC: "no official CVE ID", mapping per Dormann; Fedora/Arch/Tumbleweed confirmed
4b051f522d ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-31635 ¦ CNA stack: rxgk_decrypt_skb() [net/rxrpc/rxgk_common.h:81], programFiles net/rxrpc/rxgk.c; no rxgk_crypt.c; CNA text is a length-check BUG_ON
3c713a6db5 ¦ F4 ¦ https://api.github.com/repos/v12-security/pocs/commits?path=dirtydecrypt&per_page=5 ¦ PoC commit 2026-05-17T02:26:21Z; BleepingComputer dated 2026-05-18 (not 05-19); fix 2026-04-25 confirmed (BC)
e19a58718d ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-31635 ¦ CNA cvssV3_1 7.5 CVSS:3.1/AV:N/.../C:N/I:N/A:H (network DoS), not a local LPE; affected 6.16, fixed 6.18.23/6.19.13/7.0
9beb2af59c ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ BC dated 2026-05-18 already reports the PoC; V12 commit 2026-05-17
ddfccd94bc ¦ unreadable ¦ https://moselwal.com/blog/dirtydecrypt-linux-kernel-rxgk-cve-2026-31635 ¦ moselwal.com does not resolve (bridge, reader, WebFetch); THN carries "CVE-2026-31635 (CVSS score: 7.5)"
9e27d21b73 ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ V12: "It's a rxgk pagecache write due to missing COW guard in rxgk_decrypt_skb"; file rxgk_crypt.c in no source
2a9048c1b6 ¦ F5 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ "We found and reported this on May 9, 2026, but was informed it was a duplicate"; patched April 25; Delphos Labs also reported it
217c8fd1e1 ¦ F5 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ requires CONFIG_RXGK ... Fedora, Arch Linux, and openSUSE Tumbleweed; PoC tested only against Fedora and mainline
ea6a4a830e ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-31635 ¦ no source states the CONFIG_RXGK status of Debian, RHEL or Ubuntu LTS; CNA: kernels before 6.16 unaffected
c87524f934 ¦ F5 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-31635 ¦ CISA ADP SSVC Exploitation "poc" (2026-05-18); not in KEV 2026-10-21; neither article reports exploitation
ed4ef563ae ¦ F5 ¦ https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html ¦ per Zellic, a variant of Copy Fail (CVE-2026-31431), Dirty Frag (CVE-2026-43284 and CVE-2026-43500), and Fragnesia (CVE-2026-46300)
e2844804a1 ¦ F5 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ mitigation blocks esp4, esp6 and rxrpc ("will also break IPsec VPNs and AFS"); rxrpc alone breaks AFS (conflation logged)
3d78e4e066 ¦ F5 ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ exposure hinges on CONFIG_RXGK (supports a config check); the grep command itself is composed
aa2dc6c8a5 ¦ F4 ¦ https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html ¦ (low confidence) composed detection; Sysmon for Linux has no UID-change event 8; THN supports the pod-escape concern only
ac834d090d ¦ ok ¦ https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/ ¦ relevance judgement consistent with "distributions that closely follow the latest upstream kernel releases"
'''
