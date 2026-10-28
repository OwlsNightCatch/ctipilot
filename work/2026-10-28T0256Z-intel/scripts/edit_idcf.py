import yaml
p='entries/2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('title: "IDC Frontier: ransomware stops four zones of IDCF Cloud for 495 companies and local governments; the provider now says its backups are safe and retrievable for 194 customers and that it found no trace of data taken from customers\' virtual servers"',
    'title: "IDC Frontier: ransomware stops four zones of IDCF Cloud for 495 companies and local governments; the provider\'s final report traces it to an open-source flaw in the customer portal\'s authentication system and says no server data left"')
rep('headline: "IDCF Cloud outage: backups now retrievable for 194 of 495 customers; provider finds no trace of server data taken"',
    'headline: "IDCF Cloud ransomware began with an open-source flaw in the customer portal\'s login system; no server data left"')
old=t[t.index('summary: >\n'):t.index('discovered_at:')]
new='''summary: >
  IDC Frontier, a SoftBank Group subsidiary, says a ransomware attack from about 3:40 a.m. on 2026-10-07 stopped four zones of its IDCF Cloud
  East Japan Region 1, affecting 495 companies and local governments. Its final report of 2026-10-27 says an open-source flaw in the
  authentication system of the customer portal was exploited, after which the attacker took administrator rights on the virtualisation
  platform through the management console, stopped customers' virtual servers and encrypted them; it finds no trace of server data leaving,
  says portal registration data of up to 71 customers was queried and that backups are retrievable for 206 customers. The software is not named.
'''
t=t.replace(old,new)
rep('techniques: [T1486]','techniques: [T1190, T1486, T1489]')
rep('''    date: "2026-10-14"
    role: primary
  - url: "https://www.idcf.jp/news/topics/20261007002"''','''    date: "2026-10-14"
    role: primary
  - url: "https://www.idcf.jp/news/topics/20261027001"
    publisher: "IDC Frontier (seventh and final report, Japanese)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.idcf.jp/news/topics/20261007002"''')
rep('''    source_url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
verification: multi-source''','''    source_url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
  - quote: "The third-party unauthorised access occurred because a vulnerability in the open-source software used in the IDCF Cloud Portal was exploited. (translated from Japanese)"
    original: "第三者による不正アクセスは、「IDCFクラウドポータル」で採用しているオープンソースソフトウェアの脆弱性が悪用されたことにより発生しました。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
  - quote: "After entering the authentication system of the IDCF Cloud Portal, the attacker obtained administrator rights on the virtualisation platform via the management console, stopped customers' virtual servers and encrypted the virtual servers themselves. (translated from Japanese)"
    original: "攻撃者は「IDCFクラウドポータル」の認証システムに侵入した後、管理コンソールを経由して仮想化基盤の管理者権限を不正に取得し、お客さまの仮想サーバーを停止するとともに仮想サーバー自体を暗号化しています。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
  - quote: "restricting connections to the IDCF Cloud Portal to customer IP addresses and making multi-factor authentication mandatory (translated from Japanese)"
    original: "「IDCFクラウドポータル」への接続をお客さまIPアドレスに制限して、多要素認証を必須化"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
verification: multi-source''')
rep('''  that no data left is the provider's own judgement, reached with an external security firm and based on finding no trace.''','''  that no data left is the provider's own judgement, reached with an external security firm and based on finding no trace. The cause and the
  attack path are the provider's own account in its final report, which does not name the software.''')
rep('''no source names the actor, the ransomware family or the intrusion route ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002); [IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001); [BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/); [Jiji Press via nippon.com, 2026-10-07](https://www.nippon.com/en/news/yjj2026100700867/)). The lesson is supplier concentration: local governments sat behind one provider whose recovery first depended on copies the customers held, until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495.''',
'''no source names the actor or the ransomware family ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002); [IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001); [BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/); [Jiji Press via nippon.com, 2026-10-07](https://www.nippon.com/en/news/yjj2026100700867/)). The provider's final report of 2026-10-27 gives the route: a flaw in open-source software used in the customer portal's authentication system was exploited, and the attacker then obtained administrator rights on the virtualisation platform through the management console, stopped customers' virtual servers and encrypted them; the software is not named ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)). The lesson is supplier concentration: local governments sat behind one provider whose recovery first depended on copies the customers held, until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495.''')
rep('''A copy in the provider's own environment is not one to count on for the recovery window.''','''A copy in the provider's own environment is not one to count on for the recovery window. Ask a hosting or cloud supplier in writing how its customer portal authenticates and whether the open-source components behind that login are inventoried and patched, because here the path to the hypervisor ran from the portal's login system through the management console; the supplier's own remediation, a rebuilt portal, an external identity provider, access limited to customer IP addresses with mandatory multi-factor authentication and an automated software inventory, is the checklist ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)).''')
open(p,'w',encoding='utf-8').write(t)
fm=yaml.safe_load(t.split('\n---\n',1)[0].split('---\n',1)[1]); print(len(fm['headline']))
