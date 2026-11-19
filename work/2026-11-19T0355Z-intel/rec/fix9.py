FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:26],a[:70],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
OB="https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce"
l=E('entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i.md')
l.rep("**Defender takeaway:** upgrade to v1.83.14-stable or later and block the guardrail endpoint at the reverse proxy until then, as LiteLLM's advisory says (","**Defender takeaway:** upgrade to v1.83.14-stable or later, the first release with the complete fix set ([Obsidian Security, 2026-06-11](%s)), and block the guardrail endpoint at the reverse proxy until then, as LiteLLM's advisory says ("%OB)
i=l.s.index("  - id: CVE-2026-47101"); j=l.s.index("  - id: CVE-2026-47102")
blk=l.s[i:j]
if 'cvss: "8.8"' in blk: l.s=l.s[:i]+blk.replace('cvss: "8.8"','cvss: "n/a"')+l.s[j:]
else: FAIL.append(('obsidian','47101 cvss',0))
l.rep("the 8.8 on the two other CVEs is VulnCheck's score for CVE-2026-47102 as The Hacker News relays it.","the 8.8 on CVE-2026-47102 is VulnCheck's score as The Hacker News relays it, and no listed source scores CVE-2026-47101 on its own.")
l.save()
n=E('entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws.md')
a="F5 and the nginx project fixed five memory-corruption flaws in the data plane ("
i=n.s.index(a)
j=n.s.index("))",n.s.index("CERT-EU says all five can lead",i))+2
newp=("F5 and the nginx project published the nginx2root fixes on 2026-11-18 ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html)); CERT-EU counts five vulnerabilities, all of which can lead to unauthenticated code execution with the privileges of the NGINX worker process ([CERT-EU, 2026-11-18](https://cert.europa.eu/publications/security-advisories/2026-022/))")
print(n.s[i:j][-130:])
n.s=n.s[:i]+newp+n.s[j:]
n.rep("with the mail proxy; NGINX Plus before 37.3.0.1 and 37.0.8.1 and R33 to R36\"","with the mail proxy; NGINX Plus 37.1.0 to 37.2.0, 37.0.0 to 37.0.7 and R33 to R36 per CERT.at\"")
n.save()
o=E('entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router.md')
o.rep("in the Optimizely account, to audit all Project JavaScript fields for unauthorized code and to rotate the Optimizely API tokens, session tokens and integration keys (","in the Optimizely account (")
o.save()
print('FAIL',FAIL)
