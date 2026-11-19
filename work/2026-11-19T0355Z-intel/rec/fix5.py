import re
FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:26],a[:70],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
OB="https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce"
# Confluence #0
c=E('entries/2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce.md')
c.rep("on evidence of active exploitation, naming no product and no actor; the exploitation reported so far is against N-able N-central, not Confluence","on evidence of active exploitation, naming neither Confluence nor N-able N-central and no actor; the exploitation reported so far is against N-able N-central, not Confluence")
c.save()
# LiteLLM #1 #12 #20
l=E('entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i.md')
l.rep("on any instance that an untrusted user could reach on an older build rotate the master key, the salt key and every provider API key and audit every Custom Code Guardrail, the callbacks loaded under litellm_settings.callbacks and the holders of proxy_admin, as Obsidian advises ([Obsidian Security, 2026-06-11](%s))."%OB,"on any instance that an untrusted user could reach on an older build rotate every provider API key, the database credentials and any MCP tokens stored in the proxy, and audit every Custom Code Guardrail, the callbacks loaded under litellm_settings.callbacks and the holders of proxy_admin, as Obsidian advises ([Obsidian Security, 2026-06-11](%s)); the master key and the salt key that the chain reaches belong on the same rotation."%OB)
l.rep("on any instance an untrusted user could reach on an older build, rotate the master key, the salt key and every provider API key and audit","on any instance an untrusted user could reach on an older build, rotate every provider API key, the database credentials, any MCP tokens stored in the proxy and the master and salt keys, and audit")
l.rep("the CNA record held by VulnCheck scores CVE-2026-40217","the CVE record published by MITRE scores CVE-2026-40217")
l.rep("event_date: 2026-06-15","event_date: 2026-06-11")
l.save()
# nginx
n=E('entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws.md')
n.rep("NCSC.ch, NCSC-NL and Rapid7 score them CVSS 4.0 9.2.","NCSC-NL scores all five CVSS 4.0 9.2, and NCSC.ch and Rapid7 the HTTP/2 pair.")
n.rep("NGINX Plus 37.3.0.1 and 37.0.8.1 fix the flaws, while 37.2.0.1 and 37.0.7.1 fix only CVE-2026-123633, and NGINX Plus R33 to R36 have no update (translated from German)","NGINX Plus 37.3.0.1 and 37.0.8.1 fix the flaws; CERT.at says 37.2.0.1 and 37.0.7.1 already carry the fix for CVE-2026-123633 but stay affected by CVE-2026-123007 and CVE-2026-121810, and NGINX Plus R33 to R36 have no update (translated from German)")
n.rep("headline: \"NGINX nginx2root: five unauthenticated worker-RCE flaws, Rapid7 PoC public; update to 1.31.9, 1.30.7 or Plus 37.3.0.1\"","headline: \"NGINX nginx2root: five unauthenticated flaws can reach worker RCE, Rapid7 PoC public; update 1.31.9, 1.30.7, Plus 37.3.0.1\"")
# R-release ranges
n.rep("NGINX Plus 37.1.0 to before 37.3.0.1 and 37.0.0 to before 37.0.8.1; NGINX Plus R33 to R36\"\n    fixed: \"nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R33 to R36\"","NGINX Plus 37.1.0 to before 37.3.0.1 and 37.0.0 to before 37.0.8.1; NGINX Plus R34 to R36\"\n    fixed: \"nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R34 to R36\"")
n.rep("NGINX Plus before 37.2.0.1 and 37.0.7.1 and the R33 to R36 releases\"","NGINX Plus before 37.2.0.1 and 37.0.7.1 and R34 to R36\"")
n.rep("(37.3.0.1 and 37.0.8.1 carry all five fixes); none for NGINX Plus R33 to R36\"","(37.3.0.1 and 37.0.8.1 carry all five fixes); none for NGINX Plus R34 to R36\"")
n.rep("with the mail proxy; NGINX Plus before 37.3.0.1 and 37.0.8.1\"\n    fixed: \"nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1\"","with the mail proxy; NGINX Plus before 37.3.0.1 and 37.0.8.1 and R33 to R36\"\n    fixed: \"nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R33 to R36\"")
# ASLR sentence + compress
n.rep("Rapid7 says execution has the worker's permissions and that execution as the master process or root is not established, Wiz says ASLR does not protect against these flaws because attackers can use them to read memory before executing code, and Wiz withholds its exploits (","Rapid7 says execution has the worker's permissions and root is not established; F5, as CERT.at relays it, frames the base effect as worker crashes, with code execution possible where ASLR is disabled or can be bypassed, which Wiz says attackers can do by reading memory first (translated from German) (")
n.rep(" ([Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed); [Wiz Research, 2026-11-18](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)). CERT-EU reports"," ([Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed); [CERT.at, 2026-11-18](https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar); [Wiz Research, 2026-11-18](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)). CERT-EU reports")
n.rep("The fixes are in nginx 1.31.9 and 1.30.7, and Rapid7 sends open-source 1.9.5 to 1.30.6 to 1.30.7 ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html); [Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed)).","The fixes are in nginx 1.31.9 and 1.30.7 ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html)).")
n.save()
# Java4Shell
j=E('entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce.md')
j.rep("Fortinet lists FortiOS, FortiProxy and FortiWeb as not impacted, the other products it names as under investigation and none as affected","Fortinet lists FortiOS, FortiProxy, FortiWeb and others as not impacted, dozens of products as under investigation and none as affected")
m=re.search(r"the running build, not the installed package, decides \(\[NCSC\.ch, 2026-11-17\]\(https://security-hub\.ncsc\.admin\.ch/#/posts/13198\)\)",j.s)
if m: j.s=j.s.replace(m.group(0),"BACS says to check that the running applications actually use the corrected Java version ([BACS, 2026-11-18](https://www.bacs.admin.ch/de/warnung-java-2-de))")
else: FAIL.append(('java','running build',0))
j.save()
# Airlock
a=E('entries/2026-11-19/airlock-gateway-cve-2026-19707-smart-form-protection.md')
a.rep("Smart Form Protection heap overflow can crash","Smart Form Protection buffer overflow can crash")
a.s=a.s.replace("[Airlock documentation, 2026-11-18]","[Airlock documentation, 2026-11-19]")
for u in ["1781491741687","1755485389146","1648621032215","1755485389142"]:
    pat=re.compile(r'(url: "https://docs\.airlock\.com/[^"]*%s\.html"\n    publisher: "[^"]*"\n    date: )"2026-11-18"'%u)
    a.s,k=pat.subn(r'\1"2026-11-19"',a.s)
    if k!=1: FAIL.append(('airlock','docs date '+u,k))
a.save()
# CyberPower
y=E('entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc.md')
y.rep("a signed-looking binary that loads a DLL of the attacker's choosing (","an old trusted executable paired with an unknown DLL in a user-profile path (")
y.rep("beside a binary launched from the SYSTEM profile path marks","next to a trusted binary in a user-profile path marks")
y.rep(", named pp followed by five random lowercase letters and staged first under temp\\profile\\extcmd,"," and staged first under temp\\profile\\extcmd,")
y.rep("every script in extcmd, not only the pp?????.cmd names (Symantec also saw ifm.cmd to ifm4.cmd staged there), certutil","every script staged under extcmd, whatever its name, certutil")
y.rep("look for scripts that differ from the product defaults and for children of ppbed.exe that are not shutdown or notification routines with no preceding power event; where either is found, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation, because","compare the extcmd folders and the console's event-to-command assignments with what administrators configured and treat unknown scripts as hostile; where the techniques Symantec lists are found (children of ppbed.exe that are not shutdown or notification routines with no preceding power event, ntdsutil or esentutl on a domain controller, a side-loaded implant), assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation, because")
y.rep('entities: ["incident:cyberpower-powerpanel-dc-intrusion-2026-11"]','entities: ["incident:cyberpower-powerpanel-dc-intrusion-2026-11", "product:cyberpower-powerpanel-business"]')
y.save()
# Synology
s=E('entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write.md')
s.rep("those builds close only CVE-2024-10441, so also move","those builds close only the SA-24:20 flaws, so also move")
s.save()
# REDCap
r=E('entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev.md')
r.s=r.s.replace("Securifera (discoverer and CNA)","Securifera (discoverer)")
r.rep("Securifera, which found the flaw and is its CNA, describes","Securifera, which found the flaw, describes")
r.rep("Securifera, which found the flaw and is the CNA, is the source for the mechanism","Securifera, which found the flaw, is the source for the mechanism")
r.save()
# Idunno
x=E('entries/2026-11-19/idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce.md')
x.rep("treating an internet-reachable server that ran the module as a candidate for the same rotation because request bodies are rarely logged, since Mandiant","treating an internet-reachable server that ran the module as a candidate for the same rotation as a precaution beyond Mandiant's condition, since Mandiant")
x.save()
# tcherber
t=E('entries/2026-11-19/tcherber-access-broker-fortigate-sonicwall-vpn-ldap-sweep.md')
t.rep("headline: \"Cyderes: broker 'tcherber' tunnels into FortiGate and SonicWall VPNs with default logins, then sweeps AD over LDAP\"","headline: \"Cyderes: 'tcherber' broker toolkit for FortiGate and SonicWall VPNs, a credential file with default logins, then an LDAP sweep\"")
t.rep("an access broker's Go toolkit that tunnels into FortiGate and SonicWall VPNs, then maps internal routes and sweeps Active Directory over LDAP automatically;","an access broker's Go toolkit with VPN clients for FortiGate and SonicWall that, once a tunnel is up, maps internal routes and sweeps Active Directory over LDAP;")
t.save()
print('FAIL',FAIL)
