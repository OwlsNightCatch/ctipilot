p='entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('''  code executions on PHP 8.4.26 under single-worker mod_php and VulnCheck extended its working exploit across builds of PHP 8.2 to 8.5; the
  one production victim the sources name is a Dutch booking-system supplier of TCS Camping whose theft SRF links to the flaws without naming a CVE, and
  Palo Alto Networks' Unit 42 retracted on 2026-10-25 its update that linked an attack on a European government agency to them. As of''',
'''  code executions on PHP 8.4.26 under single-worker mod_php and VulnCheck extended its working exploit across builds of PHP 8.2 to 8.5;
  Palo Alto Networks' advisory of 2026-10-27 now reports active exploitation against internet-exposed PAN-OS management interfaces, SRF links a
  data theft at TCS Camping's booking-system supplier to the flaws without naming a CVE, and Unit 42 retracted on 2026-10-25 its update
  that linked an attack on a European government agency to them. As of''')
rep('''    Two unauthenticated remote-code-execution flaws in PHP itself are on CISA's exploited list since 2026-10-26 and honeypots recorded working code execution, fixed builds (8.5.12, 8.4.27,''',
'''    Two unauthenticated remote-code-execution flaws in PHP itself are on CISA's exploited list since 2026-10-26, honeypots recorded working code execution and Palo Alto reports attacks on internet-exposed PAN-OS management interfaces, fixed builds (8.5.12, 8.4.27,''')
rep('''  - quote: "we observed attack traffic targeting our customers"''','''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "we observed attack traffic targeting our customers"''')
rep('''  successful code execution is Karimi's honeypot report, relayed by SecurityWeek and BleepingComputer, with no production victim named.''',
'''  successful code execution is Karimi's honeypot report, relayed by SecurityWeek and BleepingComputer. Palo Alto Networks' advisory of
  2026-10-27 states, without further detail, that active exploitation has been observed against its own management interface exposed to
  the internet; no production victim is named.''')
rep('''No source ties a named CVE to a production compromise: Palo Alto Networks' Unit 42 retracted on 2026-10-25 its update of 2026-10-23 that had linked an attack on a European government agency to these flaws and says it is unable to confirm that the initial access is associated with them ([Unit 42, 2026-10-25](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)), and CrowdStrike''',
'''Palo Alto Networks' advisory for both flaws, revised on 2026-10-27, states that active exploitation has been observed targeting its management interface exposed to the internet, and names no victim or actor ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)); beyond that statement no source ties a named CVE to a production compromise: its Unit 42 retracted on 2026-10-25 its update of 2026-10-23 that had linked an attack on a European government agency to these flaws and says it is unable to confirm that the initial access is associated with them ([Unit 42, 2026-10-25](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)), and CrowdStrike''')
open(p,'w',encoding='utf-8').write(t)
