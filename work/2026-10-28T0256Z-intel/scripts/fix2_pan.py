import subprocess, re
P = "entries/2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release.md"
HTML = "https://security.paloaltonetworks.com/CVE-2026-109618"
JSON = "https://security.paloaltonetworks.com/json/CVE-2026-109618"
s = open(P).read()
head = subprocess.check_output(["git", "show", "HEAD:" + P], text=True)

def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)

# 1. restore the 2026-10-27T05:15:00Z section verbatim from HEAD
m_new = re.search(r"## Update — 2026-10-27T05:15:00Z\n\n.*?(?=\n## Update — 2026-10-28T03:38:43Z)", s, re.S)
m_old = re.search(r"## Update — 2026-10-27T05:15:00Z\n\n.*?(?=\Z)", head, re.S)
s = s[:m_new.start()] + m_old.group(0).rstrip("\n") + "\n" + s[m_new.end():]

# 2. main text: ETA and FAQ clauses back to the HTML page, 'released' clause on the JSON
sub("and nine others carry estimated dates from 2026-10-27 to 2026-10-30; the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-27](%s))" % JSON,
    "([Palo Alto Networks, 2026-10-27](%s)) and nine others carry estimated dates from 2026-10-27 to 2026-10-30; the same hotfix covers the PHP and the Brotli flaws, except 11.2.10-h16, which has only the PHP fix, while 11.2.10-h17 has both ([Palo Alto Networks, 2026-10-27](%s))" % (JSON, HTML))
sub("and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-27](%s))" % JSON,
    "and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-27](%s))" % HTML)

# 3. paragraph 1: PAN cite after the first clause
sub("as affected by CVE-2026-109618 and CVE-2026-109619, the unauthenticated remote-code-execution bugs in the PHP runtime that the PHP project fixed in its releases of the same day ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5)).",
    "as affected by CVE-2026-109618 and CVE-2026-109619 ([Palo Alto Networks, 2026-10-21](%s)); these are the unauthenticated remote-code-execution bugs in the PHP runtime that the PHP project fixed in its releases of the same day ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5))." % HTML)

# 4. cite the KEV statement in the new section
sub("CISA's catalog flags both PHP flaws with forensic triage requirements.",
    "CISA's catalog flags both PHP flaws with forensic triage requirements ([CISA KEV, 2026-10-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).")
open(P, "w").write(s)
