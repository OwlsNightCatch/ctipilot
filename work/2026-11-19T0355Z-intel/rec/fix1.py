import re,sys
FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:30],a[:70],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
# ---------------- Java4Shell
j=E('entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce.md')
j.rep("no exploitation reported (CVSS 3.1 8.1)","GreyNoise reports exploitation attempts, none confirmed successful (CVSS 3.1 8.1)")
j.rep("update Java, no attacks yet","update Java, attempts seen")
j.rep("a second researcher claims a working exploit with no release stated, and no source reports attacks.","a second researcher claims a working exploit with no release stated, GreyNoise reports exploitation attempts without a confirmed success, and VulnCheck says a working exploit is available to its customers.")
j.rep("Tenable relays Immersive's Kevin Breen's claim of a working, unreleased exploit that reaches","Tenable relays Immersive's Kevin Breen's claim of a working exploit, with no release stated, that reaches")
j.rep("Upwind reproduced the overflow and says Spring Security, Tomcat, Jetty 12 and java-jwt pass attacker-supplied tokens straight to the decoder ([Upwind, 2026-11-17](https://www.upwind.io/blog/java4shell-what-we-know-now-and-what-comes-next/)). ","")
j.rep("Talos has seen no exploitation in the wild yet and expects probing ([Talos, 2026-11-18](https://blog.talosintelligence.com/java4shell/)).","Talos has seen no exploitation in the wild yet and expects probing ([Talos, 2026-11-18](https://blog.talosintelligence.com/java4shell/)), while Tenable relays GreyNoise's report of exploitation attempts as of 2026-11-18, none confirmed successful, and VulnCheck's statement that a working RCE exploit is available to its customers ([Tenable, 2026-11-17](https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability)).")
j.rep("unexplained hs_err_pid crash logs on internet-facing Java applications (","unexplained hs_err_pid crash logs on internet-facing Java applications, where the log may not name Base64 because the crash comes later (")
j.rep("starting with Authorization headers (","starting with Authorization headers, and bursts of IllegalArgumentException from java.util.Base64$Decoder or of restarts (")
j.rep("Fortinet lists none as affected while it investigates","Fortinet lists FortiOS, FortiProxy and FortiWeb as not impacted, the other products it names as under investigation and none as affected")
j.rep("Upwind reproduced only the heap overflow.","Upwind reproduced only the heap overflow. The NCSC.ch hub and Talos say no malicious exploitation is established, while Tenable relays GreyNoise's exploitation attempts (none confirmed successful) and VulnCheck's customer exploit.")
j.save()
# ---------------- Confluence
c=E('entries/2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce.md')
c.rep("BSI CERT-Bund's bulletin rates the issue high ([BSI CERT-Bund, 2026-11-10]","BSI CERT-Bund's bulletin rates the issue critical and its second revision notes that an exploit was added (translated from German) ([BSI CERT-Bund, 2026-11-10]")
c.rep("    publisher: Apache Axis project (announcement thread)\n    date: '2026-11-06'","    publisher: Apache Axis project (announcement thread)\n    date: '2026-11-01'")
c.rep("[Apache Axis project, 2026-11-06](https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz)","[Apache Axis project, 2026-11-01](https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz)")
# type improvement -> update for this run's record
m=re.search(r"  - at: '?(\d{4}-\d\d-\d\dT[\d:]+Z)'?\n    run_id: 2026-11-19T0355Z-intel\n    type: improvement\n",c.s)
if m:
    at=m.group(1)
    c.s=c.s.replace(m.group(0),m.group(0).replace('type: improvement','type: update'))
    c.rep("## Improvement — %s"%at,"## Update — %s"%at)
    c.s=re.sub(r"updated_at: '?[\dT:\-Z]+'?\n","updated_at: '%s'\n"%at,c.s,count=1)
else: FAIL.append(('confluence','record not matched',0))
c.save()
# ---------------- Synology
y=E('entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write.md')
y.rep("on the branches for which SA-26:13 names no fix), taking","on the branches for which SA-26:13 names no fix; on DSM 7.1, 7.2 and 6.2 those builds close only CVE-2024-10441, so also move to a branch with an SA-26:13 fix), taking")
y.rep("CISA added CVE-2024-10441 to its Known Exploited Vulnerabilities catalog on 2026-11-18, which supports","Synology's notice says December 2024 while SA-24:20's revision table runs from 2024-11-05 to 2024-11-14 and BleepingComputer calls it a November 2024 advisory. CISA added CVE-2024-10441 to its Known Exploited Vulnerabilities catalog on 2026-11-18, which supports")
y.save()
# ---------------- Drupal
d=E('entries/2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16.md')
d.rep("; the advisories list neither a component beyond the installer nor any exploitation.","; neither advisory reports exploitation.")
d.rep("exploit status Proof and target distribution Uncommon)","exploit status Proof, meaning a proof of concept exists with documented methods for developing an exploit in the wild, and target distribution Uncommon, meaning only uncommon module configurations are exploitable)")
d.rep("**Exposure:** any Drupal site on core before 10.6.22, 11.3.22 or 11.4.13, and every site on an end-of-life line, which has no fix;","**Exposure:** any Drupal site on core before 10.6.22, 11.3.22 or 11.4.13, though Drupal's own rating says only uncommon module configurations are exploitable, and every site on an end-of-life line, which has no fix;")
d.save()
# ---------------- OptimJack
o=E('entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router.md')
o.rep("counts more than 450 domains, among them a crypto clipper and card skimmer in the Optimizely files.","counts more than 450 domains; the Optimizely files carry a crypto clipper and card skimmer.")
o.save()
print('FAIL',FAIL)
