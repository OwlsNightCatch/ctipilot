p='entries/2026-10-23/hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth.md'
s=open(p,encoding='utf-8').read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(old[:90],s.count(old)); s=s.replace(old,new)
J="https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json"
T="https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt"
rep("wireless: 72 CVEs fixed in one bulletin, 19 of them","wireless: 76 CVEs fixed in one bulletin, 19 of them")
rep("fixes 72 CVEs in AOS-8 and AOS-10 for Mobility Conductors, Controllers,","fixes 76 CVEs (72 in its first release, four added and one id replaced in revision 2 of 2026-11-17) in AOS-8 and AOS-10 for Mobility Conductors, Controllers,")
rep("  - id: CVE-2026-79845\n","  - id: CVE-2026-95787\n")
n1=s.count('fixed: "AOS-8.13.3.1, AOS-8.10.0.24"'); n2=s.count('fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14, AOS-8.13.3.1, AOS-8.10.0.24"')
print('aos8 rows',n1,'mixed rows',n2)
s=s.replace('fixed: "AOS-8.13.3.1, AOS-8.10.0.24"','fixed: "AOS-8.13.3.1, AOS-8.10.0.24, AOS-8.13.3.2-FIPS"')
s=s.replace('fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14, AOS-8.13.3.1, AOS-8.10.0.24"','fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14, AOS-8.13.3.1, AOS-8.10.0.24, AOS-8.13.3.2-FIPS"')
# sources: find last sources record before closed_sources
rep("closed_sources: []","  - url: \"JSON\"\n    publisher: \"HPE Networking CSAF (revision 2)\"\n    date: \"2026-11-17\"\n    role: primary\n  - url: \"TXT\"\n    publisher: \"HPE Networking bulletin text (revision 2)\"\n    date: \"2026-11-17\"\n    role: primary\nclosed_sources: []".replace('JSON',J).replace('TXT',T))
rep("(10.8.1.2, 10.7.2.7, 10.4.1.14, 8.13.3.1 or 8.10.0.24), and until then","(10.8.1.2, 10.7.2.7, 10.4.1.14, 8.13.3.1 or 8.10.0.24; AP-5xx access points in a FIPS-compliant environment need AOS 8.13.3.2 FIPS or later), and until then")
rep("fixes 72 CVEs in the wireless operating systems AOS-8 and AOS-10","fixes 76 CVEs in the wireless operating systems AOS-8 and AOS-10")
rep("33 of the 72 rate 9.0 or higher","33 of the 76 rate 9.0 or higher")
rep("The CSAF scores 33 of the 72 flaws","The CSAF scores 33 of the 76 flaws")
# add rev2 sentence after the HPE says... sentence: append to first paragraph end -> find paragraph end marker
old="and the 33 of the 76"  # placeholder guard
# P2: fixed builds + FIPS
rep("fixed builds are AOS-10.8.1.2, 10.7.2.7 and 10.4.1.14 and AOS-8.13.3.1 and 8.10.0.24 (","fixed builds are AOS-10.8.1.2, 10.7.2.7 and 10.4.1.14 and AOS-8.13.3.1 and 8.10.0.24, and customers with AP-5xx access points in a FIPS-compliant environment must use AOS 8.13.3.2 FIPS or later ([HPE Networking CSAF, 2026-11-17](TXT)); the AOS-10 PAPI authentication bypass carries CVE-2026-95787 since revision 2 of 2026-11-17, which replaced CVE-2026-79845 and added CVE-2026-95788, CVE-2026-95789, CVE-2026-95790 and CVE-2026-95791, all below CVSS 3.1 9.0 ([HPE Networking CSAF, 2026-11-17](JSON)) (".replace('TXT',T).replace('JSON',J))
open(p,'w',encoding='utf-8').write(s)
print('ok')
