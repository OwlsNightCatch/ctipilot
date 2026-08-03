## W1 source slice
### ESSENTIAL (mandatory attempt) — 11
- id=advisories-ncsc-nl | NCSC-NL — Security Advisories (RSS) | https://advisories.ncsc.nl/rss/advisories | rss=- | tier=essential | fetch=rss | rel=A | lang=['en', 'nl'] | cat=ch-eu,gov,active-breaking,vulns
- id=anssi-fr | ANSSI / CERT-FR | https://www.cert.ssi.gouv.fr/ | rss=- | tier=essential | fetch=api | rel=A | lang=['fr', 'en'] | cat=ch-eu,gov,active-breaking
- id=bsi-de | BSI Germany — CERT-Bund WID (RSS) | https://wid.cert-bund.de/content/public/securityAdvisory/rss | rss=- | tier=essential | fetch=rss | rel=A | lang=['de', 'en'] | cat=ch-eu,gov,active-breaking,vulns
- id=cert-eu | CERT-EU | https://cert.europa.eu/publications/security-advisories | rss=- | tier=essential | fetch=api | rel=A | lang=['en'] | cat=ch-eu,gov,active-breaking,vulns
- id=cert-pl | CERT Polska / NASK | https://cert.pl/en/news/ | rss=- | tier=essential | fetch=webfetch | rel=A | lang=['en', 'pl'] | cat=ch-eu,gov,active-breaking
- id=cisa-advisories | CISA Cybersecurity Advisories | https://www.cisa.gov/news-events/cybersecurity-advisories | rss=https://www.cisa.gov/cybersecurity-advisories/all.xml | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=active-breaking,gov
- id=cisa-directives | CISA Directives | https://www.cisa.gov/news-events/directives | rss=- | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=gov,active-breaking
- id=cisa-kev | CISA Known Exploited Vulnerabilities Catalog | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | rss=- | tier=essential | fetch=api | rel=A | lang=['en'] | cat=vulns,active-breaking
- id=enisa-euvd | ENISA EU Vulnerability Database (EUVD) | https://euvd.enisa.europa.eu/ | rss=- | tier=essential | fetch=api | rel=A | lang=['en'] | cat=vulns,active-breaking
- id=ncsc-ch-security-hub | NCSC Switzerland — Cyber Security Hub (CSH) / GovCERT.ch | https://security-hub.ncsc.admin.ch/#/dashboard | rss=- | tier=essential | fetch=api | rel=A | lang=['de', 'fr', 'it', 'en'] | cat=ch-eu,active-breaking,gov,vulns
- id=ncsc-uk | NCSC UK | https://www.ncsc.gov.uk/section/keep-up-to-date/reports-advisories | rss=https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=gov,active-breaking
### ROTATION (standard/candidate, oldest-first) — 16
- id=zdi | Zero Day Initiative | https://www.zerodayinitiative.com/blog/ | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-14 | cat=vulns,research
- id=aikido-security | Aikido Security (aikido.dev) | https://www.aikido.dev/blog | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-14 | cat=research,vulns
- id=onapsis | Onapsis Research Labs | https://onapsis.com/blog | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-14 | cat=research,vulns
- id=morphisec | Morphisec Labs | https://www.morphisec.com/blog/ | rss=- | tier=standard | fetch=webfetch | rel=C | lang=['en'] | last_fetch=2026-07-19 | cat=research,vulns
- id=push-security | Push Security Blog | https://pushsecurity.com/blog | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-19 | cat=research
- id=resecurity | Resecurity | https://www.resecurity.com/blog | rss=- | tier=standard | fetch=webfetch | rel=C | lang=['en'] | last_fetch=2026-07-19 | cat=research,vulns
- id=sans-ics | SANS ICS | https://www.sans.org/blog/?focus-area=industrial-control-systems-ics | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-19 | cat=ot-ics,research
- id=snyk-research | Snyk Security Research | https://snyk.io/blog/ | rss=- | tier=standard | fetch=rss | rel=B | lang=['en'] | last_fetch=2026-07-19 | cat=vulns,research
- id=socprime | SOC Prime | https://socprime.com/blog/ | rss=https://socprime.com/blog/feed/ | tier=standard | fetch=rss | rel=C | lang=['en'] | last_fetch=2026-07-19 | cat=research,vulns
- id=team-cymru | Team Cymru S2 Research | https://www.team-cymru.com/blog | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-19 | cat=research
- id=sonatype | Sonatype (Software Supply Chain Research) | https://www.sonatype.com/blog | rss=- | tier=standard | fetch=rss | rel=B | lang=['en'] | last_fetch=2026-07-19 | cat=research,vulns
- id=kela-cyber | KELA Cybercrime Threat Intelligence | https://www.kelacyber.com/blog/ | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-21 | cat=research
- id=searchlight-cyber | Searchlight Cyber | https://slcyber.io/research-center/ | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-21 | cat=research,vulns
- id=exodus-intelligence | Exodus Intelligence (blog.exodusintel.com) | https://blog.exodusintel.com | rss=- | tier=standard | fetch=rss | rel=B | lang=['en'] | last_fetch=2026-07-21 | cat=research,vulns
- id=sysdig | Sysdig Threat Research Team | https://www.sysdig.com/blog | rss=https://www.sysdig.com/blog/feed | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-21 | cat=research
- id=depthfirst | depthfirst.com (security research blog) | https://depthfirst.com | rss=- | tier=standard | fetch=webfetch | rel=C | lang=['en'] | last_fetch=2026-07-26 | cat=research,vulns

## W2 source slice
### ESSENTIAL (mandatory attempt) — 13
- id=advisories-ncsc-nl | NCSC-NL — Security Advisories (RSS) | https://advisories.ncsc.nl/rss/advisories | rss=- | tier=essential | fetch=rss | rel=A | lang=['en', 'nl'] | cat=ch-eu,gov,active-breaking,vulns
- id=anssi-fr | ANSSI / CERT-FR | https://www.cert.ssi.gouv.fr/ | rss=- | tier=essential | fetch=api | rel=A | lang=['fr', 'en'] | cat=ch-eu,gov,active-breaking
- id=bsi-de | BSI Germany — CERT-Bund WID (RSS) | https://wid.cert-bund.de/content/public/securityAdvisory/rss | rss=- | tier=essential | fetch=rss | rel=A | lang=['de', 'en'] | cat=ch-eu,gov,active-breaking,vulns
- id=cert-at | CERT.at (Austria) | https://www.cert.at/en/ | rss=- | tier=essential | fetch=webfetch | rel=A | lang=['en', 'de'] | cat=ch-eu,gov
- id=cert-eu | CERT-EU | https://cert.europa.eu/publications/security-advisories | rss=- | tier=essential | fetch=api | rel=A | lang=['en'] | cat=ch-eu,gov,active-breaking,vulns
- id=cert-pl | CERT Polska / NASK | https://cert.pl/en/news/ | rss=- | tier=essential | fetch=webfetch | rel=A | lang=['en', 'pl'] | cat=ch-eu,gov,active-breaking
- id=cisa-advisories | CISA Cybersecurity Advisories | https://www.cisa.gov/news-events/cybersecurity-advisories | rss=https://www.cisa.gov/cybersecurity-advisories/all.xml | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=active-breaking,gov
- id=cisa-directives | CISA Directives | https://www.cisa.gov/news-events/directives | rss=- | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=gov,active-breaking
- id=enisa | ENISA | https://www.enisa.europa.eu/news | rss=- | tier=essential | fetch=webfetch | rel=A | lang=['en'] | cat=ch-eu,gov
- id=ncsc-ch-focus | NCSC Switzerland — Im Fokus | https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus.html | rss=- | tier=essential | fetch=webfetch | rel=A | lang=['de'] | cat=ch-eu,gov
- id=ncsc-ch-incidents | NCSC Switzerland — Aktuelle Vorfälle | https://www.ncsc.admin.ch/ncsc/de/home/aktuell/aktuelle-vorfaelle.html | rss=- | tier=essential | fetch=bridge | rel=A | lang=['de'] | cat=ch-eu,gov
- id=ncsc-ch-security-hub | NCSC Switzerland — Cyber Security Hub (CSH) / GovCERT.ch | https://security-hub.ncsc.admin.ch/#/dashboard | rss=- | tier=essential | fetch=api | rel=A | lang=['de', 'fr', 'it', 'en'] | cat=ch-eu,active-breaking,gov,vulns
- id=ncsc-uk | NCSC UK | https://www.ncsc.gov.uk/section/keep-up-to-date/reports-advisories | rss=https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml | tier=essential | fetch=bridge | rel=A | lang=['en'] | cat=gov,active-breaking
### ROTATION (standard/candidate, oldest-first) — 14
- id=ccn-cert-es | CCN-CERT (Spain) | https://www.ccn-cert.cni.es/en/ | rss=- | tier=standard | fetch=jina | rel=A | lang=['es', 'en'] | last_fetch=2026-07-29 | cat=ch-eu,gov
- id=infoguard-labs | InfoGuard Labs (Switzerland) | https://labs.infoguard.ch/ | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en'] | last_fetch=2026-07-28 | cat=research,ch-eu,vulns
- id=jpcert | JPCERT/CC (Japan) | https://www.jpcert.or.jp/english/index.html | rss=- | tier=standard | fetch=webfetch | rel=A | lang=['en', 'ja'] | last_fetch=2026-07-29 | cat=gov,active-breaking,vulns
- id=synacktiv | Synacktiv Publications | https://www.synacktiv.com/publications.html | rss=- | tier=standard | fetch=webfetch | rel=B | lang=['en', 'fr'] | last_fetch=2026-07-29 | cat=ch-eu,research,vulns
- id=openssf-policy | OpenSSF Policy | https://openssf.org/policy/ | rss=- | tier=standard | fetch=webfetch | rel=C | lang=['en'] | last_fetch=2026-07-29 | cat=gov,research
- id=cisa-news | CISA News | https://www.cisa.gov/news-events/news | rss=https://www.cisa.gov/news.xml | tier=standard | fetch=bridge | rel=A | lang=['en'] | last_fetch=2026-07-30 | cat=gov,news
- id=cnil-fr | CNIL France | https://www.cnil.fr/en/news | rss=- | tier=standard | fetch=webfetch | rel=A | lang=['en', 'fr'] | last_fetch=2026-07-30 | cat=breaches,ch-eu
- id=compass-security | Compass Security Blog | https://blog.compass-security.com/ | rss=https://blog.compass-security.com/feed/ | tier=standard | fetch=webfetch | rel=B | lang=['en', 'de'] | last_fetch=2026-07-30 | cat=ch-eu,research
- id=edpb | European Data Protection Board | https://www.edpb.europa.eu/news/news_en | rss=- | tier=standard | fetch=bridge | rel=A | lang=['en'] | last_fetch=2026-07-30 | cat=ch-eu,gov
- id=govcert-at | GovCERT Austria | https://www.govcert.gv.at/en/ | rss=- | tier=standard | fetch=webfetch | rel=A | lang=['en', 'de'] | last_fetch=2026-07-30 | cat=ch-eu,gov
- id=ico-uk | UK ICO breach notifications | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/ | rss=- | tier=standard | fetch=jina | rel=A | lang=['en'] | last_fetch=2026-07-30 | cat=breaches,ch-eu
- id=ncc-research | NCC Group Research | https://www.nccgroup.com/research-blog/ | rss=- | tier=standard | fetch=bridge | rel=B | lang=['en'] | last_fetch=2026-07-30 | cat=ch-eu,research
- id=prodaft | PRODAFT — Reports | https://www.prodaft.com/reports | rss=- | tier=standard | fetch=jina | rel=B | lang=['en'] | last_fetch=2026-07-30 | cat=ch-eu,research
- id=truesec | Truesec | https://www.truesec.com/hub/blog | rss=https://www.truesec.com/hub/blog/feed/ | tier=standard | fetch=rss | rel=B | lang=['en'] | last_fetch=2026-07-30 | cat=ch-eu,research,vulns