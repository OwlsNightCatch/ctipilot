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
GH="https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p"
n=E('entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws.md')
n.rep("fixed five unauthenticated memory-corruption flaws in the nginx data plane on 2026-11-18, two in HTTP/2","fixed five memory-corruption flaws in the nginx data plane on 2026-11-18, two in HTTP/2")
n.rep("which CERT-EU says can lead to code execution with the privileges of the worker process; NCSC-NL scores all five CVSS 4.0 9.2, and NCSC.ch and Rapid7 the HTTP/2 pair.","which CERT-EU says can lead to unauthenticated code execution with the privileges of the worker process; NCSC-NL scores all five CVSS 4.0 9.2, NCSC.ch and Wiz the two HTTP/2 flaws and Rapid7 CVE-2026-123007.")
n.rep("fixed five unauthenticated memory-corruption flaws in the data plane (","fixed five memory-corruption flaws in the data plane (")
n.rep("CERT-EU says all five can lead to code execution with the privileges","CERT-EU says all five can lead to unauthenticated code execution with the privileges")
n.rep("(37.3.0.1 and 37.0.8.1 carry all five fixes)","(per CERT.at, 37.3.0.1 and 37.0.8.1 carry the fixes for four of the five)")
n.rep("as fixing four of the five (all but CVE-2026-123634);","as fixing four of the five (CVE-2026-123007, CVE-2026-121810, CVE-2026-123633 and CVE-2026-113425);")
n.rep("Wiz and Xint report code execution for the flaws they found and did not publish their exploits.","Wiz did not publish its exploits, and Xint reports code execution for the flaws it found.")
n.save()
r=E('entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev.md')
r.rep("Securifera disclosed CVE-2026-90817 on 2026-09-20,","Securifera described CVE-2026-90817 on 2026-09-27,")
r.save()
l=E('entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i.md')
l.rep("**Defender takeaway:** upgrade to v1.83.14-stable or later, block the guardrail endpoint at the reverse proxy until then, keep admin endpoints off the internet, and where exposure is suspected, rotate","**Defender takeaway:** upgrade to v1.83.14-stable or later and block the guardrail endpoint at the reverse proxy until then, as LiteLLM's advisory says ([LiteLLM advisory, 2026-05-07](%s)); where exposure is suspected, rotate"%GH)
l.rep("as Obsidian advises ([Obsidian Security, 2026-06-11](%s)); an instance that an untrusted user could reach on an older build counts as suspected, and the master key and the salt key that the chain reaches belong on the same rotation."%OB,"as Obsidian advises ([Obsidian Security, 2026-06-11](%s)); an instance that an untrusted user could reach on an older build counts as suspected, and the master key and the salt key that the chain reaches belong on the same rotation, with admin endpoints kept off the internet."%OB)
l.rep("**Detection:** proxy access logs for POST requests to /guardrails/test_custom_code, POST /guardrails and PUT /guardrails/{id}, and for /user/update calls that set `user_role` to `proxy_admin` (","**Detection:** proxy access logs for POST requests to /guardrails/test_custom_code, POST /guardrails and PUT /guardrails/{id}, for /key/generate calls that carry `allowed_routes`, and for /user/update and /user/bulk_update calls that set `user_role` to `proxy_admin` (")
m=re.search(r"; a conflict resolved here in favour of the vendor advisory's CVSS 4\.0 5\.9 and its proxy-admin prerequisite",l.s)
i=l.s.find("while the CVE record published by MITRE scores")
if i>=0:
    j=l.s.index("; the 8.8 on the two other CVEs",i)
    l.s=l.s[:i]+"and the vendor's CVSS 4.0 5.9 and its proxy-admin prerequisite are the figures recorded"+l.s[j:]
else: FAIL.append(('obsidian','sourcing mitre clause',0))
l.save()
d=E('entries/2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16.md')
d.rep("**Detection:** web access logs for requests to the installer on a site that is already installed; Drupal's advisory","**Detection:** web access logs for requests to the installer on a site that is already installed, which follows from the mechanism; Drupal's advisory")
d.save()
x=E('entries/2026-11-19/idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce.md')
x.rep("the ENISA record carries the score and description but not that statement.","the ENISA record carries the score and description but not that statement, and dates the record 2026-11-19 where Mandiant's advisory timeline dates its publication 2026-11-18.")
x.save()
o=E('entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router.md')
o.rep("audit every Project JavaScript field for code nobody wrote, review account-creation events and administrative access, and rotate the API tokens","audit every Project JavaScript field for code nobody wrote and rotate the API tokens")
o.save()
j=E('entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce.md')
if "customers, ([Tenable" in j.s: j.s=j.s.replace("customers, ([Tenable","customers ([Tenable")
else: FAIL.append(('java','stray comma',0))
j.save()
# run record body notes
rp='runs/2026-11-19/2026-11-19T0355Z-intel.md'
t=open(rp,encoding='utf-8').read()
for a,b in [("(update on the pre-announcement entry, priority notable to high)","(update on the pre-announcement entry; priority stays notable)"),
            ("`improvement` on the Confluence entry (the store already described exploitation through N-able N-central; CISA's listing and Apache's no-fix and handler statements are the reader-facing delta, no re-float)","`update` on the Confluence entry (CISA's listing and Apache's no-fix and handler statements are the reader-facing delta; an earlier draft typed it `improvement` and the verifier asked for `update`, so it moves updated_at)")]:
    if t.count(a)!=1: FAIL.append(('runrecord',a[:60],t.count(a)))
    else: t=t.replace(a,b)
open(rp,'w',encoding='utf-8').write(t)
print('FAIL',FAIL)
