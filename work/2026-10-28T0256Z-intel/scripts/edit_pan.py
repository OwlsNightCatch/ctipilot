import re
p='entries/2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:80])
    t=t.replace(old,new)
HF="10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11 and 12.2.4-h1"
# frontmatter
rep('title: "CVE-2026-109618 / CVE-2026-109619, Palo Alto Networks PAN-OS and Panorama: the PHP2Shell flaws affect every release, reaching PAN-OS through its management web interface; eleven hotfixes are out and the rest are due by 2026-10-30"',
    'title: "CVE-2026-109618 / CVE-2026-109619, Palo Alto Networks PAN-OS and Panorama: the PHP2Shell flaws affect every release through the management web interface, and Palo Alto reports active exploitation against internet-exposed management interfaces; eleven hotfixes are out and the rest are due by 2026-10-30"')
rep('headline: "Palo Alto: eleven PAN-OS hotfixes for PHP2Shell are out, nine still due by 30 October; CISA now lists the PHP flaws"',
    'headline: "Palo Alto reports active exploitation of PAN-OS management interfaces via PHP2Shell; 11 hotfixes out, 9 due by 30 October"')
old_sum=t[t.index('summary: >\n'):t.index('discovered_at:')]
new_sum='''summary: >
  Palo Alto Networks' advisory of 2026-10-21, revised on 2026-10-27, now says active exploitation has been observed targeting the PAN-OS
  management interface exposed to the internet, rates the flaw Critical with urgency Highest (CVSS-B 9.2) and still lists every release of
  PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619 through the
  management web interface (the HTTPS web UI and the XML API service). Eleven hotfixes are released (%s) and nine others carry estimated
  dates up to 2026-10-30; the advisory names no actor or victim, and GlobalProtect and the captive portal are not affected. CISA added both
  PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
''' % HF
t=t.replace(old_sum,new_sum)
rep('priority: notable','priority: high')
rep('cvss: "8.7 (CVSS-B 4.0, Palo Alto\'s rating of the PAN-OS impact, availability only)"',
    'cvss: "9.2 (CVSS-B 4.0, Palo Alto\'s rating of the PAN-OS impact with management reachable from the internet; 7.7 where it is reachable only from an adjacent network)"',count=2)
rep('status: [cisa-kev, patch-available, mitigation-only]','status: [exploited, cisa-kev, patch-available, mitigation-only]',count=2)
# evidence: drop superseded quote, add new
stale='''  - quote: "Palo Alto Networks is not aware of any malicious exploitation of this issue against our products."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
'''
new_ev='''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Severity Updated to Critical and Urgency updated as Highest"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "The risk is highest on PAN-OS when you allow access to the management interface from external IP addresses on the internet."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
'''
rep(stale,new_ev)
rep('''  speaks of upcoming releases. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself.''',
'''  speaks of upcoming releases. The statement that exploitation has been observed is Palo Alto's own, in the advisory revised on 2026-10-27;
  no third-party report of an attack on PAN-OS was found. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities catalog
  comes from the catalog itself.''')
old_act=t[t.index('actions:\n  - "Install the released hotfix'):t.index('updates:\n')]
new_act='''actions:
  - "Take the management interface of every PA-Series and VM-Series firewall and Panorama off the internet now by restricting it to a jump box or trusted internal addresses, because Palo Alto reports active exploitation against internet-exposed management interfaces, and install the hotfix for your maintenance release: %s (11.2.10-h17 adds the Brotli fix); the other trains' hotfixes are due 2026-10-27 to 2026-10-30."
''' % HF.replace(' and 12.2.4-h1',' or 12.2.4-h1')
t=t.replace(old_act,new_act)
# body
head,rest=t.split('\n---\n\n',1)
body_start=rest
idx=rest.index('## Update — 2026-10-23T03:42:16Z')
tail=rest[idx:]
U='https://security.paloaltonetworks.com/CVE-2026-109618'
new_body=f'''Palo Alto Networks' advisory of 2026-10-21 lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama as affected by CVE-2026-109618 and CVE-2026-109619, the unauthenticated remote-code-execution bugs in the PHP runtime that the PHP project fixed in its releases of the same day ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5)). Palo Alto says no special configuration is required to be affected and that the issue strictly affects the management web interface, which includes the HTTPS web UI and the XML API service; a dataplane interface is affected only where a management profile is attached to it, and the GlobalProtect portal and gateway and the captive portal are not ([Palo Alto Networks, 2026-10-21]({U})).

Its revision of 2026-10-27 states that active exploitation has been observed targeting the management interface exposed to the internet, and raises the severity to Critical and the urgency to Highest: the vendor score is CVSS-B 9.2, with high impact on confidentiality, integrity and availability, and 7.7 where management is reachable only from an adjacent network such as a jump box ([Palo Alto Networks, 2026-10-27]({U})). The advisory names no actor, victim or post-exploitation behaviour. Eleven hotfixes are released ({HF}) and nine others carry estimated dates from 2026-10-27 to 2026-10-30; the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-27]({U})). Until a build is installed, Palo Alto recommends restricting management access to a jump box or trusted internal addresses and offers Threat Prevention coverage (Threat IDs 543004 and 97622 to 97625 and further IDs from 97643) that applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, inbound management traffic is decrypted and threat prevention is enabled on it ([Palo Alto Networks, 2026-10-27]({U})).

**Exposure:** every PAN-OS firewall and Panorama appliance below its train's hotfix, whatever the configuration, through its management web interface; the service is reachable from the internet where the management port, or a dataplane interface carrying a management profile, answers HTTPS or XML API requests from outside the administrator range, and that is the exposure Palo Alto says is being attacked ([Palo Alto Networks, 2026-10-27]({U})).

**Detection:** in management-plane access and system logs, any request from an address outside the administrator range, though Palo Alto does not say which logs record request bodies; in threat logs, hits on the Threat IDs above where the signatures are active and the four conditions hold. Palo Alto publishes no indicator for the observed attacks, so no post-compromise check is defined ([Palo Alto Networks, 2026-10-27]({U})).

**Defender takeaway:** move management access behind a jump box or trusted internal addresses now, on Panorama as on PAN-OS, and remove management profiles from dataplane interfaces that face untrusted networks; Palo Alto lists no workaround beyond that restriction and the Threat Prevention coverage. Install the hotfix released for your maintenance line (10.2.13, 10.2.16, 10.2.18, 11.1.4, 11.1.6, 11.1.10, 11.1.13, 11.1.16, 11.2.10, 12.1.7 or 12.2.4) ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/json/CVE-2026-109618)) and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-27]({U})).

'''
t=head+'\n---\n\n'+new_body+tail
open(p,'w',encoding='utf-8').write(t)
import yaml
fm=yaml.safe_load(t.split('\n---\n',1)[0].split('---\n',1)[1])
print(len(fm['headline']), fm['priority'])
body=new_body.split('**Exposure:**')[0]
print('main analysis words',len(re.sub(r'\(\[[^\]]*\]\([^)]*\)\)','',body).split()))
