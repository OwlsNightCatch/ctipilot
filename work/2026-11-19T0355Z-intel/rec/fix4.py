FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:28],a[:60],n)); return
        s.s=s.s.replace(a,b)
    def cut(s,start,end):
        i=s.s.find(start)
        if i<0: FAIL.append((s.p.split('/')[-1][:28],'cut '+start[:50],0)); return
        j=s.s.index(end,i)+len(end); s.s=s.s[:i]+s.s[j:]
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
j=E('entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce.md')
j.cut("Calif publishes a trigger proof of concept and withholds the product exploits (","calif.io/java4shell)). ")
j.rep("Tenable relays Immersive's Kevin Breen's claim of a working exploit, with no release stated, that reaches the flaw before login through Tomcat's Basic authentication and java-jwt (","Tenable relays a claim by Immersive's Kevin Breen of a working exploit with no release stated (")
j.rep("covering standalone runtimes, runtimes bundled in applications and appliances, and containers; ","")
j.save()
n=E('entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws.md')
n.cut("CVE-2026-123633, also in HTTP/2, is a use-after-free caused by an active connection remaining eligible for draining (","xint.io/blog/nginx2root-remote-code-execution)). ")
n.rep("the exploit needs about 128 GB of HTTP/2 traffic and a specific glibc memcpy implementation, and the repository says it will likely fail against a server with several concurrent clients","the exploit needs about 128 GB of HTTP/2 traffic and likely fails against a server with several concurrent clients")
n.save()
r=E('entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev.md')
r.cut("Unit 42 names no actor, and says REDCap released an update within two days of learning of the flaw in September (","XMRig-campaign-through-CVE-2026-90817.txt)). ")
r.rep("upgrade now, and on a server that was reachable on an older build check crontabs, the authorized_keys of all accounts, ~/.profile and running processes, because an upgrade removes none of the persistence Unit 42 lists","upgrade now and check crontabs, authorized_keys, ~/.profile and processes on any server that was reachable on an older build, because an upgrade removes none of the persistence Unit 42 lists")
r.save()
print('FAIL',FAIL)
