P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
CY = 'https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw'
THN = 'https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html'
G = 'https://github.com/openclaw/openclaw/security/advisories/'
ENTRY = {
 'entry': '2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (CVE-2026-44115 sentence)',
   'claim': 'CVE-2026-44115 (CVSS 8.8, High) is an incomplete allowlist in OpenClaw\'s command parser — shell-expansion tokens embedded in environment-variable names bypass the validation gate',
   'defect': 'The bypass is shell expansion hidden in unquoted heredoc bodies, not tokens in environment-variable names.',
   'ground_truth': 'An allowlisted command containing an unquoted heredoc could hide shell expansion in the heredoc body. That could make the approved command text look safer than what the shell would evaluate at runtime. (vendor GHSA-x3h8-jrgh-p8jx); THN: "bypass allowlist validation by embedding shell expansion tokens in a here document (heredoc) body to execute unapproved commands at runtime"',
   'ground_truth_url': G + 'GHSA-x3h8-jrgh-p8jx',
   'fix': 'CVE-2026-44115 (CVSS 8.8, High) is an exec-allowlist analysis flaw: shell expansion hidden in unquoted heredoc bodies lets an approved command evaluate differently at runtime, which Cyera says exposes environment variables such as API keys and tokens.',
   'class': 'factual-error'},
  {'where': 'summary; body paragraph 1 (exposure sentence)',
   'claim': '~245 K publicly accessible instances / summing to an estimated ~245 K exposed servers',
   'defect': 'No source states 245 K. Cyera gives two separate scanner counts (Shodan ~65,000, Zoomeye ~180,000); adding them double-counts overlapping hosts and is the entry\'s own arithmetic.',
   'ground_truth': 'Exposed Instances: ~65,000 (Shodan) · ~180,000 (Zoomeye) public-facing OpenClaw servers',
   'ground_truth_url': CY,
   'fix': 'Remove the sum; state "Cyera cites ~65,000 (Shodan) and ~180,000 (Zoomeye) public-facing OpenClaw servers as of May 2026".',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (chain sentence), title',
   'claim': 'chain the four primitives to a full sandbox-escape → credential-harvest → owner-level agent control → file-disclosure sequence whose steps each mimic normal agent behaviour and so evade controls calibrated to "human-attacker" indicators',
   'defect': 'The step order is wrong against the source and the quoted phrase is not in it. Cyera: foothold inside the sandbox; read escape (44113) plus env-var disclosure (44115) expose credentials and files; MCP loopback (44118) gives owner control; write escape (44112) plants backdoors and persistence. File disclosure is an early step, the write/sandbox escape is the last. Cyera also says three of the four chain "in parallel from one entry point". "human-attacker" indicators appears in neither Cyera nor THN.',
   'ground_truth': 'STEP 2 Data Exfiltration: TOCTOU read escape (CVE-2026-44113) and env-var disclosure (CVE-2026-44115) ... STEP 3 Privilege Escalation: MCP loopback flaw (CVE-2026-44118) ... STEP 4 Persistence: TOCTOU write escape (CVE-2026-44112) plants backdoors, modifies configuration. / Each step looks like normal agent behavior to traditional controls',
   'ground_truth_url': CY,
   'fix': 'Foothold in the OpenShell sandbox (malicious plugin, prompt injection, compromised input) -> credentials and files exposed (44113, 44115) -> owner-level control (44118) -> backdoor and persistence (44112); Cyera says each step looks like normal agent behavior to traditional controls. Drop the "human-attacker" phrase and fix the title order.',
   'class': 'factual-error'},
  {'where': 'cves[] (all four)',
   'claim': '"affected": null, "fixed": null, "vector": "local", "type": "priv-esc" (all four records)',
   'defect': 'Affected and fixed versions are in the vendor advisories and are missing. Vector "local" for 44112/44113/44115 contradicts the CNA CVSS vectors (AV:N); "type: priv-esc" on 44113 (read escape, confidentiality only) and 44115 (allowlist bypass) misstates the flaw class. (vector and type: low confidence, they encode the entry\'s own foothold-first reading).',
   'ground_truth': 'Affected versions: <= 2026.4.21; Fixed version: 2026.4.22 (all four GHSAs). CNA CVSS:3.1 vectors: 44112 AV:N/.../S:C/C:N/I:H/A:H 9.6; 44113 AV:N/.../S:C/C:H/I:N/A:N 7.7; 44115 AV:N/.../S:U/C:H/I:H/A:H 8.8; 44118 AV:L/.../S:U/C:H/I:H/A:H 7.8',
   'ground_truth_url': G + 'GHSA-wppj-c6mr-83jj',
   'fix': 'Set affected "<= 2026.4.21" and fixed "2026.4.22" on all four; map ids to advisories: 44112 = GHSA-wppj-c6mr-83jj (write escape), 44113 = GHSA-5h3g-6xhh-rg6p (read escape), 44115 = GHSA-x3h8-jrgh-p8jx (heredoc allowlist), 44118 = GHSA-r6xh-pqhr-v4xh (MCP loopback owner spoof).',
   'class': 'imprecision'},
  {'where': 'summary, body paragraph 1 (CVSS and "Critical" labels)',
   'claim': 'CVE-2026-44112 CVSS 9.6 ... (CVSS 9.6, Critical) ... CVE-2026-44115 (CVSS 8.8, High)',
   'defect': 'The scores are CVSS v3.1 base scores from the VulnCheck CNA record and Cyera; the vendor\'s own GitHub advisories rate 44112 "High" and 44115 "Moderate", and VulnCheck\'s advisory page shows CVSS v4 8.4 (High) for 44112. The entry states no CVSS version or scorer and silently omits the vendor severities.',
   'ground_truth': 'GHSA-wppj-c6mr-83jj (44112): "Severity High"; GHSA-x3h8-jrgh-p8jx (44115): Severity moderate. VulnCheck advisory for CVE-2026-44112: "Severity: HIGH | CVSS: 8.4" (CVSS:4.0). CNA CVSS:3.1 base: 9.6.',
   'ground_truth_url': 'https://www.vulncheck.com/advisories/openclaw-symlink-swap-race-condition-in-openshell-fs-bridge-writes',
   'fix': 'Write "CVSS v3.1 9.6 per Cyera and the CNA record (vendor advisory severity: High; CVSS v4 8.4)"; add a Contradiction-style note for 44115 (vendor Moderate vs 8.8).',
   'class': 'imprecision'},
  {'where': 'headline',
   'claim': '...four chainable flaws in autonomous-agent platform enable sandbox',
   'defect': 'The headline string is cut mid-phrase ("enable sandbox"), truncated at migration.',
   'ground_truth': 'title field: "...enable sandbox escape → credential leak → privilege escalation → file disclosure"',
   'ground_truth_url': 'entries/2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118.md',
   'fix': 'Shorten the headline to a complete clause, for example "OpenClaw Claw Chain: four chainable flaws (CVE-2026-44112 / 44113 / 44115 / 44118) fixed in 2026.4.22".',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentences 2, 5-8, 10, detection line)',
   'claim': 'All four CVEs are fixed by the OpenClaw release dated 2026-04-23 ... No in-the-wild exploitation reported at disclosure. Detection: alert on the agent process writing files outside designated sandbox mount directories; flag MCP loopback messages ...',
   'defect': 'Only the first sentence carries a citation. Fix release, per-CVE flaw descriptions and the exposure counts are carried by Cyera and the vendor GHSAs (fixed version is 2026.4.22, published on GitHub 2026-04-23, advisories 2026-04-23). The no-exploitation statement is in neither cited page (CISA ADP SSVC on the CVE records read "Exploitation: none" on 2026-05-07; none of the four ids is in the CISA KEV catalogue today). The Detection line is the entry\'s own composition; neither cited page gives detection guidance, and the second item (senderIsOwner=true from non-matching sources) is an inference since the fix stops trusting that header.',
   'ground_truth': 'Fixed version: 2026.4.22 ... The fix commit is contained in the public v2026.4.22 tag. / SSVC: {"Exploitation": "none"} (CVE record ADP, 2026-05-07)',
   'ground_truth_url': G + 'GHSA-r6xh-pqhr-v4xh',
   'fix': 'Cite each clause (GHSAs for fix version and mechanisms, Cyera for counts); write the no-exploitation line as "no exploitation reported by Cyera, THN or the vendor advisories as of 2026-05-15" or drop it; mark the detection line as a derived hunting concept (symlink swap in the sandbox mount followed by writes or reads outside the mount root; heredoc bodies containing expansion tokens; owner-gated MCP loopback calls made with a non-owner token).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentence 1)',
   'claim': 'OpenClaw (also marketed as Clawdbot), an autonomous AI-agent platform released in late 2025',
   'defect': 'Cyera says Clawdbot was the original name, not a parallel marketing name.',
   'ground_truth': 'Originally launched as "Clawdbot" in late 2025, OpenClaw connects LLMs directly to filesystems, SaaS applications, credentials, and execution environments',
   'ground_truth_url': CY,
   'fix': 'OpenClaw (originally launched as Clawdbot in late 2025)',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) Bar check on facts known 2026-05-16: no exploitation, the chain needs prior code execution inside the sandbox, vendor advisories rate the flaws High/Moderate, and no constituency nexus is shown; "research with no in-the-wild use" is a listed high-disqualifier.',
   'ground_truth': 'Cyera: "From a single supply-chain-style foothold, an attacker can chain three of them"; CISA ADP SSVC Exploitation: none (2026-05-07); not in KEV on 2026-10-21',
   'ground_truth_url': CY,
   'fix': 'Consider notable.',
   'class': 'imprecision'},
  {'where': 'actions[0]',
   'claim': '**Apply the OpenClaw / Clawdbot 2026-04-23 fixes (GHSA-...) or block OpenClaw instances from the internet; audit plugin supply chain.** The Claw Chain ... requires code execution inside the sandbox boundary ...',
   'defect': 'The action bundles three tasks, restates the body and carries hedged conditions; the fix is a version (2026.4.22), not "2026-04-23 fixes".',
   'ground_truth': 'Apply the April 23, 2026 fixes covering GHSA-5h3g-6xhh-rg6p, GHSA-wppj-c6mr-83jj, GHSA-r6xh-pqhr-v4xh, and GHSA-x3h8-jrgh-p8jx. / Fixed version: 2026.4.22',
   'ground_truth_url': CY,
   'fix': 'Upgrade every OpenClaw deployment to 2026.4.22 or later and rotate credentials reachable from the agent runtime.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1195.002', 'behavior': 'Foothold via a malicious or compromised OpenClaw plugin ("supply-chain-style foothold"; compromised external input)', 'url': CY},
   {'id': 'T1068', 'behavior': 'Sandbox escape and owner-level privilege escalation: MCP loopback senderIsOwner spoof (44118), TOCTOU write escape (44112)', 'url': CY},
   {'id': 'T1005', 'behavior': 'TOCTOU read escape (44113) reads system files, credentials and internal artifacts outside the sandbox mount root', 'url': G + 'GHSA-5h3g-6xhh-rg6p'},
   {'id': 'T1552.001', 'behavior': 'Credentials and configuration files outside the sandbox read via the read escape; env-var secrets exposed via heredoc expansion (44115)', 'url': CY},
   {'id': 'T1059', 'behavior': 'Shell expansion hidden in unquoted heredoc bodies executes unapproved commands at runtime (44115)', 'url': 'https://cveawg.mitre.org/api/cve/CVE-2026-44115'},
  ],
  'note': 'The sources do not say how an attacker reaches the entry point beyond "malicious plugin, prompt injection, or compromised external input"; no T1190 is claimed. All five ids active in attack/enterprise-attack.json (checked mechanically).',
  'cve_facts': {
   'CVE-2026-44112': {'ghsa': 'GHSA-wppj-c6mr-83jj', 'flaw': 'TOCTOU symlink swap redirects OpenShell FS bridge writes outside the mount root', 'affected': '<= 2026.4.21', 'fixed': '2026.4.22', 'cvss_v31_cna': '9.6', 'cvss_v4_cna': '8.4', 'vendor_severity': 'High'},
   'CVE-2026-44113': {'ghsa': 'GHSA-5h3g-6xhh-rg6p', 'flaw': 'TOCTOU symlink swap lets OpenShell FS bridge reads return bytes outside the mount root', 'affected': '<= 2026.4.21', 'fixed': '2026.4.22', 'cvss_v31_cna': '7.7', 'cvss_v4_cna': '8.3', 'vendor_severity': 'High'},
   'CVE-2026-44115': {'ghsa': 'GHSA-x3h8-jrgh-p8jx', 'flaw': 'exec allowlist analysis misses shell expansion in unquoted heredoc bodies', 'affected': '<= 2026.4.21', 'fixed': '2026.4.22', 'cvss_v31_cna': '8.8', 'cvss_v4_cna': '8.7', 'vendor_severity': 'Moderate'},
   'CVE-2026-44118': {'ghsa': 'GHSA-r6xh-pqhr-v4xh', 'flaw': 'MCP loopback accepts spoofable senderIsOwner header; non-owner loopback client acts as owner', 'affected': '<= 2026.4.21', 'fixed': '2026.4.22', 'cvss_v31_cna': '7.8', 'cvss_v4_cna': '8.5', 'vendor_severity': 'High'},
   'kev': 'none of the four ids in CISA KEV as of 2026-10-21',
  },
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'Vendor GitHub advisories (OpenClaw for its own product) confirm each flaw and the fix; Cyera, the discloser, and THN restate the same disclosure chain. One disclosure, no independent exploitation evidence, so 2.'},
  'exposure': [
   {'quote': 'Affected versions: <= 2026.4.21 - Fixed version: 2026.4.22', 'url': G + 'GHSA-r6xh-pqhr-v4xh'},
   {'quote': 'A malicious plugin, prompt injection, or compromised external input gains code execution inside the OpenShell sandbox.', 'url': CY},
   {'quote': 'Any deployment where OpenClaw is exposed to the public internet without authentication or network controls in front of it.', 'url': CY},
  ],
  'detection': [
   {'quote': 'A time-of-check/time-of-use race around OpenShell sandbox filesystem writes could let a symlink swap redirect a write outside the intended local mount root.', 'url': G + 'GHSA-wppj-c6mr-83jj'},
   {'quote': 'An allowlisted command containing an unquoted heredoc could hide shell expansion in the heredoc body.', 'url': G + 'GHSA-x3h8-jrgh-p8jx'},
   {'quote': 'The loopback MCP path accepted spoofable owner-context metadata from request headers, which could allow a non-owner loopback client to present itself as owner for owner-gated operations.', 'url': G + 'GHSA-r6xh-pqhr-v4xh'},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'Patch OpenClaw. Apply the April 23, 2026 fixes covering GHSA-5h3g-6xhh-rg6p, GHSA-wppj-c6mr-83jj, GHSA-r6xh-pqhr-v4xh, and GHSA-x3h8-jrgh-p8jx.', 'url': CY},
   {'quote': 'Rotate secrets. Assume any environment variable or credential reachable by OpenClaw processes may be compromised.', 'url': CY},
  ],
  'bodies': [P + 'oc-cyera.txt', P + 'oc-thn.txt', P + 'oc-GHSA-5h3g-6xhh-rg6p.txt', P + 'oc-GHSA-wppj-c6mr-83jj.txt', P + 'oc-GHSA-r6xh-pqhr-v4xh.txt', P + 'oc-GHSA-x3h8-jrgh-p8jx.txt', P + 'oc-vc-44112.txt', P + 'oc-vc-44115.txt', P + 'oc-release.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
60418fd734 ¦ ok ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ Cyera: four chainable vulnerabilities in OpenClaw (CVE IDs 44112, 44115, 44118, 44113); headline string truncated mid-phrase ("enable sandbox") - imprecision logged
72e57d8210 ¦ F4 ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ Exposed Instances: ~65,000 (Shodan) · ~180,000 (Zoomeye); no source states ~245 K (entry's own sum). CVSS 9.6/7.7/8.8/7.8 and fix 04-23 confirmed.
247aa1045c ¦ ok ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ Patch OpenClaw. Apply the April 23, 2026 fixes covering GHSA-5h3g-6xhh-rg6p, GHSA-wppj-c6mr-83jj, GHSA-r6xh-pqhr-v4xh, and GHSA-x3h8-jrgh-p8jx. (F18 hedging/restatement logged as imprecision)
d7359f68ae ¦ ok ¦ https://cveawg.mitre.org/api/cve/CVE-2026-44112 ¦ CNA VulnCheck: cvssV3_1 9.6 CRITICAL AV:N...; affected <2026.4.22. Entry has affected/fixed null and vector local (imprecision logged)
2f101b598b ¦ ok ¦ https://cveawg.mitre.org/api/cve/CVE-2026-44113 ¦ CNA VulnCheck: cvssV3_1 7.7 HIGH; OpenClaw before 2026.4.22 TOCTOU read escape. affected/fixed null in entry (logged)
ff1a7f6880 ¦ ok ¦ https://cveawg.mitre.org/api/cve/CVE-2026-44115 ¦ CNA VulnCheck: cvssV3_1 8.8 HIGH; before 2026.4.22. Vendor GHSA severity moderate (logged)
f070157f7e ¦ ok ¦ https://cveawg.mitre.org/api/cve/CVE-2026-44118 ¦ CNA VulnCheck: cvssV3_1 7.8 HIGH AV:L/PR:L; before 2026.4.22. affected/fixed null in entry (logged)
61c5d2be2d ¦ ok ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ Originally launched as "Clawdbot" in late 2025 ... integrations ... Microsoft Agent 365; date 2026-05-15 (THN 2026-05-15). "also marketed as" vs "originally" logged
318a98a3a1 ¦ F5 ¦ https://github.com/openclaw/openclaw/security/advisories/GHSA-r6xh-pqhr-v4xh ¦ Fixed version: 2026.4.22 ... advisory 2026-04-23; the four GHSA ids confirmed; no inline citation on this sentence
4590ea5daa ¦ F4 ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ Chain: foothold -> read escape (44113)+env-var (44115) -> owner control (44118) -> persistence (44112 write escape); entry order wrong; "human-attacker" phrase absent
db4d343317 ¦ F5 ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ A time-of-check / time-of-use race condition in the OpenShell sandbox lets attackers redirect writes outside the sandbox boundary - enabling configuration tampering, backdoor placement
0e665a0ec2 ¦ F4 ¦ https://github.com/openclaw/openclaw/security/advisories/GHSA-x3h8-jrgh-p8jx ¦ An allowlisted command containing an unquoted heredoc could hide shell expansion in the heredoc body (not environment-variable names)
2041ef5839 ¦ F5 ¦ https://github.com/openclaw/openclaw/security/advisories/GHSA-r6xh-pqhr-v4xh ¦ The loopback MCP path accepted spoofable owner-context metadata from request headers ... senderIsOwner derived from which token authenticated the request
9f23fc1926 ¦ F5 ¦ https://github.com/openclaw/openclaw/security/advisories/GHSA-5h3g-6xhh-rg6p ¦ A time-of-check/time-of-use race around OpenShell sandbox filesystem reads could let a symlink swap cause bytes outside the intended mount root to be read.
305299c586 ¦ F14 ¦ https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw ¦ ~65,000 (Shodan) and ~180,000 (Zoomeye) public-facing OpenClaw servers; no 245 K figure anywhere
66b31fa4b4 ¦ F5 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-44112 ¦ CISA ADP SSVC Exploitation: none (2026-05-07); not in KEV 2026-10-21; neither Cyera nor THN states exploitation status
22c49e4131 ¦ F5 ¦ null ¦ No fetched source gives detection guidance (Cyera: marketing line only); entry-composed hunting concept
'''
