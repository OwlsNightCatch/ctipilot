import re
FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:26],a[:70],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
NA="https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
t=E('entries/2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap.md')
t.rep("9.15.1P20HF1, 9.16.1P16HF1","9.15.1P20HF1, 9.15.1P21, 9.16.1P16HF1",2) if t.s.count("9.15.1P20HF1, 9.16.1P16HF1")==2 else t.rep("9.15.1P20HF1, 9.16.1P16HF1","9.15.1P20HF1, 9.15.1P21, 9.16.1P16HF1",1)
t.rep("9.18.1P8HF1, 9.19.1P3HF1","9.18.1P8HF1, 9.18.1P9, 9.19.1P3HF1",1)
t.rep("lists hotfix builds from 9.12.1P20HF1 to 9.19.1P4, 9.17.1P12 among them ([NetApp, 2026-11-04](%s))"%NA,"lists hotfix builds from 9.12.1P20HF1 to 9.19.1P4, 9.17.1P12, 9.15.1P21 and 9.18.1P9 among them ([NetApp, 2026-11-18](%s))"%NA)
t.rep("  - url: https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1646\n    publisher: Trend Micro Download Center (Deep Discovery Analyzer, patch dated 2026-11-18)\n    date: '2026-11-18'\n    role: corroborating\n","  - url: https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1646\n    publisher: Trend Micro Download Center (Deep Discovery Analyzer, patch dated 2026-11-18)\n    date: '2026-11-18'\n    role: corroborating\n  - url: %s\n    publisher: NetApp (NTAP-20261021-0021, advisory data, revision 13.0)\n    date: '2026-11-18'\n    role: primary\n"%NA)
t.rep("  - product:netapp-ontap-9\ntechniques:","  - product:netapp-ontap-9\n  - product:trend-micro-deep-discovery-analyzer\ntechniques:")
t.rep("Trend Micro still says it has seen no successful exploitation in its products or services ([Trend Micro, 2026-11-18](https://success.trendmicro.com/en-US/solution/KA-0024802)).","Trend Micro still says it has seen no successful exploitation in its products or services ([Trend Micro, 2026-11-18](https://success.trendmicro.com/en-US/solution/KA-0024802)). NetApp's advisory data, revision 13.0 of 2026-11-18, adds ONTAP 9.15.1P21 and 9.18.1P9 to the fixed builds ([NetApp, 2026-11-18](%s))."%NA)
t.save()
j=E('entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce.md')
j.rep("entities: []",'entities: ["product:openjdk", "product:oracle-java-se", "product:oracle-graalvm-for-jdk", "product:cisco-catalyst-center", "product:cisco-secure-network-analytics", "product:cisco-secure-workload"]')
j.rep("BACS's warning of 2026-11-18 asks operators to prioritise","Tenable relays GreyNoise's report of exploitation attempts as of 2026-11-18, none confirmed successful, and VulnCheck's statement that a working RCE exploit is available to its customers, which replaces the entry's earlier statement that no source reports attacks ([Tenable, 2026-11-17](https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability)). BACS's warning of 2026-11-18 asks operators to prioritise")
j.save()
print('FAIL',FAIL)
