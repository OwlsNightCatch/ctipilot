import re, json, sys, os
V3 = '/home/user/ctipilot/work/2026-10-04T0405Z-intel/v3/'
F = {
 'ctx174':('0365e601.txt','https://support.citrix.com/external/article/CTX697174/citrix-netscaler-adc-and-citrix-netscale.html'),
 'cblog':('6397da34.txt','https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/'),
 'cguid':('f3656a9c.txt','https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/'),
 'cyber':('1b048d9c.txt','https://cyberpress.org/new-citrix-netscaler-saml-flaw-triggers-crashes-and-suspected-exploitation-attempts/'),
 'heisens':('51cd0dd2.txt','https://www.heise.de/en/news/Netscaler-admins-beware-Zero-day-causes-crashes-and-code-execution-11474996.html'),
 'acsc':('23b2d965.txt','https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products'),
 'kev':('kev.json','https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'),
 'ctx096':('fba74e7e.txt','https://support.citrix.com/external/article/CTX697096/citrix-netscaler-adc-and-citrix-netscale.html'),
 'wt':('5673e34b.txt','https://watchtowr.com/intelligence/citrix-netscaler-zero-day-vulnerabilities-faq/'),
 'certeu':('0b4e42d7.txt','https://cert.europa.eu/publications/security-advisories/2026-014/'),
 'bc':('f8e4339e.txt','https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/'),
 'ncslnl':('b888d6ae.txt','https://advisories.ncsc.nl/advisory?id=NCSC-2026-0394'),
 'certat':('bb7d82fd.txt','https://www.cert.at/de/warnungen/2026/9/kritische-sicherheitslucken-in-citrix-netscaler-adc-und-netscaler-gateway-aktiv-ausgenutzt-updates-verfugbar'),
 'csh':('ncsc13005.txt','https://security-hub.ncsc.admin.ch/#/posts/13005'),
 'u42':('89c35569.txt','https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/'),
 'gtig':('gtig.txt','https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances'),
 'zst':('4caab10d.txt','https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297'),
 'zncsc':('524cb1e4.txt','https://www.ncsc.nl/alerts/actief-misbruik-van-zeroday-kwetsbaarheden-in-zammad-update-nu'),
 'd14':('4929ff0d.txt','https://csirt.divd.nl/cases/DIVD-2026-00014/'),
 'd15':('bdb7b46c.txt','https://csirt.divd.nl/DIVD-2026-00015'),
 'c489':('92ae9adc.txt','https://csirt.divd.nl/cves/CVE-2026-102489'),
 'c490':('3fd5dc0b.txt','https://csirt.divd.nl/cves/CVE-2026-102490'),
 'fheise':('8250dfa9.txt','https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html'),
 'fnl':('4e3bd09d.txt','https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data'),
 'frn':('3f350efe.txt','https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/'),
 'hgpt':('huntress-gpt.txt','https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat'),
 'hpk':('huntress-parks.txt','https://www.huntress.com/blog/parks-recreation-platform-webshell-attack'),
 'sk':('480fdf71.txt','https://support.checkpoint.com/results/sk/sk1000171/'),
 'cpb':('5efdab5b.txt','https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/'),
 'thn':('8d53b768.txt','https://thehackernews.com/2026/09/check-point-warns-of-management-server.html'),
 'bf':('bf-post.txt','https://bishopfox.com/blog/weaponizing-check-point-management-cve-2026-93616'),
 'tenable':('tenable.txt','https://www.tenable.com/blog/frequently-asked-questions-about-reported-citrix-netscaler-zero-day-vulnerabilities'),
 'bfgh':('bf-gh.txt','https://github.com/BishopFox/CVE-2026-93616-check'),
}
def nz(t):
    t=t.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')
    return re.sub(r'\s+',' ',t)
cache={}
def text(k):
    if k not in cache:
        t=open(V3+F[k][0],encoding='utf-8').read()
        cache[k]=nz(t)
    return cache[k]
# claim_id: (verdict, srckey, passage)
R = {}
def add(cid, src, passage, verdict='ok'):
    R[cid]=(verdict,src,passage)
exec(open(V3+'rows.py').read())
ids = re.findall(r'- claim_id: (\w+)', open('/home/user/ctipilot/work/2026-10-04T0405Z-intel/claims.iter3.yaml').read())
missing=[i for i in ids if i not in R]
extra=[i for i in R if i not in ids]
print('ids',len(ids),'rows',len(R),'missing',missing,'extra',extra)
bad=0
out=['claims:']
for i in ids:
    v,s,p=R[i]
    if s and not p.startswith('DERIVED') and not p.startswith('ABSENT'):
        norm=nz(p)
        if norm not in text(s):
            print('NOT VERBATIM',i,s,p[:80]); bad+=1
    url = F[s][1] if s else None
    out.append('  - {claim_id: %s, verdict: %s, source_url: %s, passage: %s}'%(i,v,json.dumps(url),json.dumps(p[:200])))
open('/home/user/ctipilot/work/2026-10-04T0405Z-intel/verification.iter3.claims.yaml','w').write('\n'.join(out)+'\n')
print('bad',bad)
