import re
P = "entries/2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave.md"
s = open(P).read()
def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)

sub("fixes a further unauthenticated SQL injection present in every earlier build.\n",
    "fixes a further unauthenticated SQL injection present in every earlier build. Gridbox 2.20.4.2 (27 October) fixes two more unauthenticated SQL injections, CVE-2026-102788 and CVE-2026-102789, with no exploitation reported.\n")

cve = """  - id: CVE-2026-102788
    cvss: "9.3 (CVSS 4.0, Joomla CNA)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Gridbox 1.0.0 to 2.20.4.1"
    fixed: "2.20.4.2; no fix for sites on the Joomla 3 line, which stops at Gridbox 2.17.0.2"
  - id: CVE-2026-102789
    cvss: "9.3 (CVSS 4.0, Joomla CNA)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Gridbox 1.0.0 to 2.20.4.1"
    fixed: "2.20.4.2; no fix for sites on the Joomla 3 line, which stops at Gridbox 2.17.0.2"
"""
sub("\nsources:\n  - url: \"https://mysites.guru/blog/gridbox-critical-authentication-bypass/\"",
    "\n" + cve + "sources:\n  - url: \"https://mysites.guru/blog/gridbox-critical-authentication-bypass/\"")

src = """  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    date: 2026-10-27
    role: corroborating
  - url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
    publisher: mySites.guru
    date: 2026-10-27
    role: primary
"""
sub("\nclosed_sources: []\n", "\n" + src + "closed_sources: []\n")

ev = """  - quote: "Gridbox 2.20.4.1 and earlier"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    source_url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
  - quote: "Neither needs a login, and about 95% of the Gridbox sites we monitor were on an affected version on the morning of the release."
    publisher: mySites.guru
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
  - quote: "There is no public report of exploitation yet"
    publisher: mySites.guru
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
"""
sub("\nverification: multi-source\n", "\n" + ev + "verification: multi-source\n")

sub("2.20.3.1 SQL injection rests on mySites.guru's reading of the release diff and carries no CVE\n  yet.\n",
    "2.20.3.1 SQL injection rests on mySites.guru's reading of the release diff and carries no CVE\n  yet. The 2.20.4.2 pair rests on Balbooa's notice for the affected and fixed versions and the two\n  fixes, and on mySites.guru for the Joomla CNA scores and records, the comparison of the two\n  packages and the share of affected sites, which are its own measurements; no source reports\n  exploitation of these two flaws.\n")

sub("update every one to 2.20.3.1, which also closes an unauthenticated blind SQL injection in the front-end blog author parameter present in every earlier build, 2.20.3 and 2.20.2.3 included.",
    "update every one to 2.20.4.2, which also closes two unauthenticated SQL injections, CVE-2026-102788 and CVE-2026-102789, and the unauthenticated blind SQL injection in the front-end blog author parameter fixed in 2.20.3.1, present in every earlier build, 2.20.3 and 2.20.2.3 included.")

sub("The version to be on is therefore 2.20.3.1.", "The version to be on then was 2.20.3.1; the later update below moves it to 2.20.4.2.")
open(P, "w").write(s)
