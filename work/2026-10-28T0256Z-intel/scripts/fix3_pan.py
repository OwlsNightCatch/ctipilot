import re
def load(p): return open(p).read()
class E:
    def __init__(s,p): s.p=p; s.s=load(p)
    def sub(s,old,new,count=1):
        assert s.s.count(old)==count,(s.p,s.s.count(old),old[:80])
        s.s=s.s.replace(old,new)
    def save(s): open(s.p,"w").write(s.s)

HTML="https://security.paloaltonetworks.com/CVE-2026-109618"
JSON="https://security.paloaltonetworks.com/json/CVE-2026-109618"
REL14="12.2.4-h1, 12.1.7-h11, 11.2.7-h23, 11.2.10-h16, 11.2.13-h4, 11.2.16-h1, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 10.2.13-h27, 10.2.16-h12 and 10.2.18-h13"

p=E("entries/2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release.md")
p.sub("; eleven hotfixes are out and the rest are due by 2026-10-30\"","; fourteen hotfixes are out and six are due by 2026-10-30\"")
p.sub("11 hotfixes out, 9 due by 30 Oct","14 hotfixes out, 6 due by 30 Oct")
p.sub("Eleven hotfixes are\n  released (10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11 and 12.2.4-h1) and nine others carry estimated dates up to 2026-10-30;",
      "Fourteen hotfixes are\n  released (%s) and six others carry estimated dates of 2026-10-29 or 2026-10-30;"%REL14)
newfixed=('fixed: "Released per the advisory as read on 2026-10-28: 12.2.4-h1; 12.1.7-h11; 11.2.7-h23, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 11.2.13-h4, 11.2.16-h1; '
          '11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4; 10.2.13-h27, 10.2.16-h12, 10.2.18-h13; estimated dates: 12.1.4-h13 (10/29), 12.1.10-h3 (10/30); '
          '11.2.4-h23 (10/30); 11.1.7-h12 (10/30); 10.2.7-h39 (10/30), 10.2.10-h42 (10/29); Panorama: the table no longer distinguishes it from the PAN-OS trains"')
s=p.s
pat=re.compile(r'fixed: "Released per the advisory\'s revisions of 2026-10-25 to 2026-10-27:.*?"\n')
assert len(pat.findall(s))==2
p.s=pat.sub(lambda m:newfixed+"\n",s)
p.sub("install the hotfix for your maintenance release: 10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11 or 12.2.4-h1 (11.2.10-h17 adds the Brotli fix); the other trains' hotfixes are due 2026-10-27 to 2026-10-30.",
      "install the hotfix for your maintenance release: 10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.7-h23, 11.2.10-h16, 11.2.13-h4, 11.2.16-h1, 12.1.7-h11 or 12.2.4-h1 (11.2.10-h17 adds the Brotli fix); the other trains' hotfixes are due 2026-10-29 or 2026-10-30.")
# JSON source record for 2026-10-28
p.sub("\nclosed_sources: []\n",'\n  - url: "%s"\n    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, as read on 2026-10-28)"\n    date: "2026-10-28"\n    role: corroborating\nclosed_sources: []\n'%JSON)
# body paragraph 2
p.sub("and the vendor timeline records only the change of 16:40 UTC that day, severity raised to Critical and urgency to Highest ([Palo Alto Networks, 2026-10-27](%s))."%JSON,
      "and the vendor timeline's three entries of that day are two removals of hotfix estimated dates and the 16:40 UTC change that raised severity to Critical and urgency to Highest, none of which mentions exploitation ([Palo Alto Networks, 2026-10-28](%s))."%JSON)
p.sub("Eleven hotfixes are released (10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11 and 12.2.4-h1) ([Palo Alto Networks, 2026-10-27](%s)) and nine others carry estimated dates from 2026-10-27 to 2026-10-30; the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-27](%s))."%(JSON,HTML),
      "Fourteen hotfixes are released (%s) and six others carry estimated dates of 2026-10-29 or 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s)); the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-28](%s))."%(REL14,HTML,HTML))
p.sub("Install the hotfix released for your maintenance line (10.2.13, 10.2.16, 10.2.18, 11.1.4, 11.1.6, 11.1.10, 11.1.13, 11.1.16, 11.2.10, 12.1.7 or 12.2.4) ([Palo Alto Networks, 2026-10-27](%s)) and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-27](%s))."%(JSON,HTML),
      "Install the hotfix released for your maintenance line (10.2.13, 10.2.16, 10.2.18, 11.1.4, 11.1.6, 11.1.10, 11.1.13, 11.1.16, 11.2.7, 11.2.10, 11.2.13, 11.2.16, 12.1.7 or 12.2.4) and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s))."%HTML)
# my own 2026-10-28 section
p.sub("the vendor timeline records no change of wording and carries only the 16:40 UTC entry of 2026-10-27, which raised the severity to Critical and the urgency to Highest ([Palo Alto Networks, 2026-10-27](%s))"%JSON,
      "the vendor timeline records no change of wording, and its entries of 2026-10-27 are two removals of hotfix estimated dates and the 16:40 UTC change that raised the severity to Critical and the urgency to Highest ([Palo Alto Networks, 2026-10-28](%s))"%JSON)
p.sub("The hotfix table is unchanged from the previous record: eleven builds released, nine due by 2026-10-30.",
      "The hotfix table has moved on since the previous record: as read on 2026-10-28, fourteen builds are released and six are due by 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s))."%HTML)
p.save()

q=E("entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md")
q.sub("with eleven hotfixes released and the rest due by 2026-10-30","with most of its hotfixes released and the rest due by 2026-10-30")
q.save()

H2="https://security.paloaltonetworks.com/CVE-2026-111497"
n=E("entries/2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi.md")
n.sub("PAN-OS hotfixes 12.2.4-h1, 12.1.4-h13, 12.1.7-h11, 12.1.10-h3, 11.2.4-h23, 11.2.7-h23, 11.2.10-h17, 11.2.13-h4 and 11.2.16-h1 (estimated 2026-10-27 to 2026-10-30);",
      "PAN-OS hotfixes 12.2.4-h1, 12.1.7-h11, 11.2.7-h23, 11.2.10-h17, 11.2.13-h4 and 11.2.16-h1 (released), 12.1.4-h13 (estimated 2026-10-29), 12.1.10-h3 and 11.2.4-h23 (estimated 2026-10-30), as read on 2026-10-28;")
n.sub("until the hotfix for the release is installed, due 2026-10-27 to 2026-10-30.","until the hotfix for the release is installed; 12.1.4-h13, 12.1.10-h3 and 11.2.4-h23 are still due, on 2026-10-29 and 2026-10-30.")
n.sub("and the hotfixes carry estimated dates from 2026-10-27 to 2026-10-30 ([Palo Alto Networks, 2026-10-26](%s))."%H2,
      "and six of the nine hotfixes are released while the other three carry estimated dates of 2026-10-29 and 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s))."%H2)
n.sub("\nclosed_sources: []\n",'\n  - url: "%s"\n    publisher: "Palo Alto Networks PSIRT (CVE-2026-111497 portfolio status, as read on 2026-10-28)"\n    date: "2026-10-28"\n    role: corroborating\nclosed_sources: []\n'%H2)
n.save()
print("ok")
