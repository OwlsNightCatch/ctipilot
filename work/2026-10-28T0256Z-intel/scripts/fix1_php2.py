import re,sys,yaml
sys.path.insert(0,'tools')
import check_run as c
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def rep(t,old,new,count=1):
    assert t.count(old)==count,(t.count(old),old[:90]); return t.replace(old,new)
U='https://security.paloaltonetworks.com/CVE-2026-109618'
AR='https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618'
p='entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md'
t=load(p)
t=rep(t,'''  - url: "https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping"
    publisher: "SRF (Espresso)"''',f'''  - url: "{U}"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    date: "2026-10-28"
    role: corroborating
  - url: "{AR}"
    publisher: "Palo Alto Networks PSIRT (advisory, Internet Archive copy of 2026-10-27 17:10 UTC)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping"
    publisher: "SRF (Espresso)"''')
old="Palo Alto Networks' advisory for both flaws, revised on 2026-10-27, states that active exploitation has been observed targeting its management interface exposed to the internet, and names no victim or actor ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)); beyond that statement"
new=f"Palo Alto Networks' advisory for both flaws now states that active exploitation has been observed targeting its management interface exposed to the internet, after a copy of 2026-10-27 said very limited exploitation, and names no victim or actor ([Palo Alto Networks, 2026-10-28]({U}); [Palo Alto Networks, 2026-10-27]({AR})); beyond that statement"
t=rep(t,old,new)
m=re.search(r'## Update — (2026-10-28T[0-9:]+Z)\n',t)
at=m.group(1)
sec=f'''## Update — {at}

Palo Alto Networks' advisory for both flaws now states that active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet, and its severity is Critical with urgency Highest ([Palo Alto Networks, 2026-10-28]({U})). A copy of the page taken on 2026-10-27 at 17:10 UTC said instead that very limited exploitation had been observed ([Palo Alto Networks, 2026-10-27]({AR})). The advisory names no victim, actor or post-exploitation behaviour and does not say which flaw was used. It is a vendor statement about its own product, Unit 42's retraction of 2026-10-25 stands, and Palo Alto's hotfixes for PAN-OS are due by 2026-10-30.
'''
t=t[:m.start()]+sec
save(p,t)
fm,body=c._frontmatter_and_body(t); print('php words',c._main_words(body))
