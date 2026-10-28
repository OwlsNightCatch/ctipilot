import re,sys,yaml
sys.path.insert(0,'tools')
import check_run as c
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def rep(t,old,new,count=1):
    assert t.count(old)==count,(t.count(old),old[:90]); return t.replace(old,new)
def words(t):
    fm,b=c._frontmatter_and_body(t); return c._main_words(b)
# ---------- .NET
p='entries/2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix.md'
t=load(p)
t=rep(t,"which still carry CVE-2026-70197, and treat the Brotli flaw as exploited ([.NET Blog, 2026-10-25](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/)).","which still carry CVE-2026-70197 ([.NET Blog, 2026-10-25](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/)), and treat the Brotli flaw as exploited, since CISA lists it ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog)).")
save(p,t); print('dotnet',words(t))
# ---------- Camping.Care
p='entries/2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud.md'
t=load(p)
w=load('work/2026-10-28T0256Z-intel/bodies/watson.txt')
orig='Betrüger konnten im Zusammenhang mit der internationalen Sicherheitslücke bei der Programmiersprache PHP Kundschafts- und Buchungsinformationen entwenden'
assert orig in w
WU='https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke'
t=rep(t,'''  - url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
    publisher: "Netzwoche"
    date: "2026-10-27"
    role: corroborating''',f'''  - url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
    publisher: "Netzwoche"
    date: "2026-10-27"
    role: corroborating
  - url: "{WU}"
    publisher: "watson.ch (Keystone-SDA dispatch)"
    date: "2026-10-26"
    role: corroborating''')
t=rep(t,'''    source_url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
verification: single-source-victim''',f'''    source_url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
  - quote: "Fraudsters were able to steal customer and booking information in connection with the international security hole in the PHP programming language, as a spokesperson of the Touring Club Schweiz (TCS) confirmed (translated from German)"
    original: "Betrüger konnten im Zusammenhang mit der internationalen Sicherheitslücke bei der Programmiersprache PHP Kundschafts- und Buchungsinformationen entwenden, wie ein Sprecher des Touring Club Schweiz (TCS)"
    publisher: "watson.ch (Keystone-SDA dispatch)"
    source_url: "{WU}"
verification: single-source-victim''')
assert t.count('SRF and Blick tie this theft to the PHP flaws')==1
m=re.search(r'## Update — (2026-10-28T[0-9:]+Z)\n',t); at=m.group(1)
sec_old=t[m.start():]
sec_new=sec_old.replace("The link to the PHP flaws therefore rests on SRF, Blick and the TCS statements, not on the supplier.",f"The link to the PHP flaws therefore rests on SRF, Blick and a TCS spokesperson's statement to Keystone-SDA ([watson.ch, 2026-10-26]({WU})), not on the supplier.")
assert sec_new!=sec_old
t=t[:m.start()]+sec_new
t=rep(t,"because SRF and Blick tie this theft to the PHP flaws although","because SRF, Blick and a TCS spokesperson tie this theft to the PHP flaws although") if "because SRF and Blick tie this theft to the PHP flaws although" in t else t
save(p,t)
# ---------- IDC Frontier
p='entries/2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups.md'
t=load(p)
t=rep(t,"the provider's final report traces it to an open-source flaw","the provider's seventh report traces it to an open-source flaw")
t=rep(t,"Its final report of 2026-10-27 says an open-source flaw","Its seventh report of 2026-10-27, which closes the investigation, says an open-source flaw")
t=rep(t,'''  - url: "https://www.nippon.com/en/news/yjj2026100700867/"
    publisher: "Jiji Press via nippon.com"
    date: "2026-10-07"
    role: corroborating
''','')
t=rep(t,"outage itself is corroborated by Jiji Press, which reports the downstream website failures, and by BleepingComputer.","outage itself is corroborated by BleepingComputer.") if "outage itself is corroborated by Jiji Press, which reports the downstream website failures, and by BleepingComputer." in t else t
t=rep(t,"affecting 495 companies and local governments, among them the websites of Ibaraki Prefecture and the city of Kodaira, and has suspended","affecting 495 companies and local governments, and has suspended")
t=rep(t,"; [Jiji Press via nippon.com, 2026-10-07](https://www.nippon.com/en/news/yjj2026100700867/))",")")
t=rep(t,"until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495.","until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495 (206 by 2026-10-20).")
t=rep(t,"became retrievable for 194 of the 495 customers only a week into the outage","became retrievable for 194 of the 495 customers only a week into the outage, 206 by 2026-10-20")
t=rep(t,"IDC Frontier's final report","IDC Frontier's seventh report") if "IDC Frontier's final report" in t else t
m=re.search(r'## Update — (2026-10-28T[0-9:]+Z)\n',t)
sec=t[m.start():]
sec=sec.replace("says the improper queries of portal registration data reached up to 71 customers, up from 48, and reports that backups are retrievable for 206 customers.","says the improper queries of portal registration data reached up to 71 customers, up from 48, that up to four customer login passwords were improperly changed and have been reset, and that backups are retrievable for 206 customers.")
assert 'four customer login passwords' in sec
t=t[:m.start()]+sec
save(p,t)
print('idc ok', 'nippon' in t, 'final' in t.lower())
