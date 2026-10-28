import re,sys,yaml
sys.path.insert(0,'tools')
import check_run as c
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def rep(t,old,new,count=1):
    assert t.count(old)==count,(t.count(old),old[:90]); return t.replace(old,new)
U='https://security.paloaltonetworks.com/CVE-2026-109618'
AR='https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618'
KEV='https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
src_block=f'''  - url: "{U}"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    date: "2026-10-28"
    role: primary
  - url: "{AR}"
    publisher: "Palo Alto Networks PSIRT (advisory, Internet Archive copy of 2026-10-27 17:10 UTC)"
    date: "2026-10-27"
    role: corroborating
  - url: "{KEV}"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.27)"
    date: "2026-10-27"
    role: corroborating
'''
# ============ PAN-OS entry
p='entries/2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release.md'
t=load(p)
t=rep(t,'tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]','tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]')
t=rep(t,'closed_sources: []\nevidence:',src_block+'closed_sources: []\nevidence:')
t=rep(t,'''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"''',f'''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    source_url: "{U}"
  - quote: "Very limited exploitation has been observed targeting the Palo Alto Networks management interface."
    publisher: "Palo Alto Networks PSIRT (advisory, Internet Archive copy of 2026-10-27 17:10 UTC)"
    source_url: "{AR}"''')
old=t[t.index('summary: >\n'):t.index('discovered_at:')]
HF="10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11 and 12.2.4-h1"
new=f'''summary: >
  Palo Alto Networks' advisory of 2026-10-21 now says, as read on 2026-10-28, that active exploitation has been observed targeting the
  PAN-OS management interface exposed to the internet, after a copy of 2026-10-27 said very limited exploitation, rates the flaw Critical with
  urgency Highest (CVSS-B 9.2) and lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama as affected by the PHP flaws
  CVE-2026-109618 and CVE-2026-109619 through the management web interface (the HTTPS web UI and the XML API service). Eleven hotfixes are
  released ({HF}) and nine others carry estimated dates up to 2026-10-30; the advisory names no actor or victim, and GlobalProtect and the
  captive portal are not affected. CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
'''
t=t.replace(old,new)
t=rep(t,'sourcing_note: >\n  Palo Alto Networks\' advisory is the first-party record','sourcing_note: >\n  Palo Alto Networks\' advisory is the first-party record')
t=rep(t,'''The statement that exploitation has been observed is Palo Alto's own, in the advisory revised on 2026-10-27;
  no third-party report of an attack on PAN-OS was found.''','''The statement that exploitation has been observed is Palo Alto's own: an Internet Archive copy of 2026-10-27 17:10 UTC says very limited
  exploitation, and the page read on 2026-10-28 says active exploitation against the management interface exposed to the internet, with no
  matching entry in the vendor timeline; no third-party report of an attack on PAN-OS was found.''')
head,rest=t.split('\n---\n\n',1)
i=rest.index('Its revision of 2026-10-27 states'); j=rest.index('**Exposure:**')
newp=f'''The advisory now states that active exploitation has been observed targeting the management interface exposed to the internet ([Palo Alto Networks, 2026-10-28]({U})); a copy of the page taken on 2026-10-27 at 17:10 UTC said that very limited exploitation had been observed ([Palo Alto Networks, 2026-10-27]({AR})), and the vendor timeline records only the change of 16:40 UTC that day, severity raised to Critical and urgency to Highest ([Palo Alto Networks, 2026-10-27]({U})). The vendor score is CVSS-B 9.2, with high impact on confidentiality, integrity and availability, and 7.7 where management is reachable only from an adjacent network such as a jump box ([Palo Alto Networks, 2026-10-27]({U})). The advisory names no actor, victim or post-exploitation behaviour. Eleven hotfixes are released ({HF}) and nine others carry estimated dates from 2026-10-27 to 2026-10-30; the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-27]({U})). Until a build is installed, Palo Alto recommends restricting management access to a jump box or trusted internal addresses and offers Threat Prevention coverage (Threat IDs 543004 and 97622 to 97625 and further IDs from 97643) that applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, inbound management traffic is decrypted and threat prevention is enabled on it ([Palo Alto Networks, 2026-10-27]({U})).

'''
rest=rest[:i]+newp+rest[j:]
rest=rest.replace(f'and that is the exposure Palo Alto says is being attacked ([Palo Alto Networks, 2026-10-27]({U}))',f'and that is the exposure Palo Alto says is being attacked ([Palo Alto Networks, 2026-10-28]({U}))')
rest=rest.replace(f'Palo Alto publishes no indicator for the observed attacks, so no post-compromise check is defined ([Palo Alto Networks, 2026-10-27]({U})).',f'Palo Alto publishes no indicator for the observed attacks and defines no post-compromise check, while CISA flags both PHP flaws in its catalog with forensic triage requirements under its directive BOD 26-04 ([CISA KEV, 2026-10-27]({KEV})).')
assert 'forensic triage requirements' in rest
t=head+'\n---\n\n'+rest
# rewrite my own section in place
k=t.index('## Update — 2026-10-28T')
sec='''## Update — 2026-10-28T03:38:43Z

Palo Alto Networks' advisory now states that active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet ([Palo Alto Networks, 2026-10-28](%s)). A copy of the page taken on 2026-10-27 at 17:10 UTC said instead that very limited exploitation had been observed ([Palo Alto Networks, 2026-10-27](%s)); the vendor timeline records no change of wording and carries only the 16:40 UTC entry of 2026-10-27, which raised the severity to Critical and the urgency to Highest ([Palo Alto Networks, 2026-10-27](%s)). The vendor score is now CVSS-B 9.2 with high impact on confidentiality, integrity and availability when management is reachable from the internet, and 7.7 when it is reachable only from an adjacent network; the earlier text scored availability impact only (8.7) and knew of no exploitation. The advisory names no actor, victim or post-exploitation behaviour. CISA's catalog flags both PHP flaws with forensic triage requirements. The hotfix table is unchanged from the previous record: eleven builds released, nine due by 2026-10-30.
''' % (U,AR,U)
m=re.search(r'## Update — 2026-10-28T[0-9:]+Z\n',t)
at=m.group(0).split('— ')[1].strip()
sec=sec.replace('2026-10-28T03:38:43Z',at)
t=t[:m.start()]+sec
save(p,t)
fm,body=c._frontmatter_and_body(t); print('pan words',c._main_words(body), 'headline',len(yaml.safe_load(head.split('---\n',1)[1])['headline']))
# ============ PHP entry
p='entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md'
t=load(p)
t=rep(t,'''  Palo Alto Networks' advisory of 2026-10-27 now reports active exploitation against internet-exposed PAN-OS management interfaces, SRF links a''','''  Palo Alto Networks' advisory now reports active exploitation against internet-exposed PAN-OS management interfaces, SRF links a''')
t=rep(t,'''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"''',f'''  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    source_url: "{U}"''')
t=rep(t,'''  2026-10-27 states, without further detail, that active exploitation has been observed against its own management interface exposed to
  the internet; no production victim is named.''','''  2026-10-27 first said very limited exploitation and the page of 2026-10-28 says active exploitation against its own management interface
  exposed to the internet, without further detail; no production victim is named.''') if '  2026-10-27 states, without further detail' in t else t
open('/tmp/_chk','w').write('')
save(p,t)
