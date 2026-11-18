from fu2_lib import *
M = 'mitel/misa-2026-0012.extract.md'
M6 = 'mitel/misa-2026-0006.extract.md'
CF = 'mitel/certfr-avi-1547.extract.md'
CFR = 'mitel/certfr-avi-1547.rawtext.txt'
BD = 'mitel/wid-sec-2026-4608.decoded.txt'
BC = 'mitel/wid-sec-2026-4608.csaf.json'
UM = 'https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012'
UM6 = 'https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006'
UCF = 'https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/'
UBS = 'https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608'
out = []
A = out.append
A('## 2. MITEL MiCollab MISA-2026-0012\n')
A('Primary: ' + UM + ' (read with `extract`, `trafilatura-direct`, fetched 2026-11-18 ~04:43Z; raw HTML also saved `mitel/misa-2026-0012.raw.html`). Page metadata date 2026-11-16.\n')
A('### 2.1 Advisory facts\n')
A(table([
 ('Advisory id and dates (first issue = last update = 2026-11-16, revision 1.0)', UM, M, 'First Issue Date: 2026-11-16'),
 ('Last updated', UM, M, 'Last Updated: 2026-11-16'),
 ('Revision', UM, M, 'Revision: 1.0'),
 ('Revision history shows only the initial version (no later revision at fetch time)', UM, M, '| 1.0 | 2026-11-16 | Initial version |'),
 ('Affected versions (single row; no other branch named)', UM, M, '10.3 (10.3.0.18) and earlier'),
 ('Fix: patch for 10.3 (10.3.0.18) PLUS upgrade; "or upgrade to a later release" (no later release number is named)', UM, M, 'Mitel provided a patch available for release 10.3 (10.3.0.18) that addresses these vulnerabilities. Upgrade to this release and apply the provided patch, or upgrade to a later release.'),
 ('Patch KB (title lists all five ids)', UM, M, 'MiCollab Security Update, MTLVULN-1861, MTLVULN-1862, MTLVULN-1863, MTLVULN-1864, MTLVULN-1877'),
 ('KB id', UM, M, 'KB000129195'),
 ('KB is behind the customer portal; partners can help', UM, M, 'If you do not have access to this link, please contact your Mitel Authorized Partner for support.'),
 ('Fix will also ship in later releases (future tense; no release named)', UM, M, 'The security update will be included in later MiCollab releases.'),
 ('Scope limiter: only supported versions assessed; End-of-Support products not considered', UM, M, 'Product statements are related only to supported product versions. Products that have reached End of Support status are not considered.'),
 ('Mitigation (verbatim; AWV component; patch is the recommended action, mitigation is the fallback)', UM, M, 'For customers who are not currently able to implement the recommended solution in a timely manner, the risk may be mitigated by restricting external access to the AWV component. For further details, please refer to the security Knowledge Base article.'),
 ('Chaining statement', UM, M, 'Exploiting these vulnerabilities together can significantly amplify their impact.'),
 ('CVE status', UM, M, 'Note: The above issue is referenced here by our internal tracking ID. A CVE identifier has been requested but is not yet assigned'),
 ('Summary severity line', UM, M, 'The identified vulnerabilities carry varied levels of severity including critical'),
]))
A('')
A('### 2.2 Each MTLVULN row (CVSS 3.1 vector as published by Mitel; no CVE ids)\n')
A(table([
 ('MTLVULN-1861 Medium 5.3: arbitrary file upload, unauthenticated, weak file-type validation', UM, M, '| MiCollab | MTLVULN-1861 | Medium / 5.3 | AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N |'),
 ('MTLVULN-1862 Critical 9.0: XML injection, AC:H, scope changed', UM, M, '| MiCollab | MTLVULN-1862 | Critical / 9.0 | AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H |'),
 ('MTLVULN-1863 Medium 5.9: unauthorized access, AC:H, confidentiality only', UM, M, '| MiCollab | MTLVULN-1863 | Medium / 5.9 | AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N |'),
 ('MTLVULN-1864 Critical 10.0: blind command injection, scope changed, C:N I:H A:H', UM, M, '| MiCollab | MTLVULN-1864 | Critical / 10.0 | AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H |'),
 ('MTLVULN-1877 Medium 5.3: authentication bypass', UM, M, '| MiCollab | MTLVULN-1877 | Medium / 5.3 | AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N |'),
 ('MTLVULN-1861 text (component AWV; file upload)', UM, M, 'could allow an unauthenticated attacker to conduct an arbitrary file upload attack due to insufficient file type validation.'),
 ('MTLVULN-1861 impact', UM, M, 'A successful exploit of this vulnerability could allow an attacker to upload arbitrary files to the target system.'),
 ('MTLVULN-1862 text: "pre-staged malicious content" is a stated precondition', UM, M, 'could allow an unauthenticated attacker to leverage pre-staged malicious content to conduct an XML injection attack due to insufficient parameter validation.'),
 ('MTLVULN-1862 impact (arbitrary commands; C, I and A)', UM, M, 'A successful exploit of this vulnerability could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts on the confidentiality, integrity and availability of the system.'),
 ('MTLVULN-1863 text: needs knowledge of a system-generated random identifier or pre-staged content', UM, M, 'with knowledge of a specific system-generated random identifier or pre-staged content, to conduct an unauthorized access attack due to improper authentication mechanisms.'),
 ('MTLVULN-1863 limiter: does not give access to arbitrary files elsewhere', UM, M, 'The vulnerability is limited to the affected functionality and does not provide unrestricted access to arbitrary files elsewhere on the system.'),
 ('MTLVULN-1864 text: blind command injection, unauthenticated; NOTE the sentence that follows is garbled in the original ("requires could allow") and may have lost a stated precondition', UM, M, 'could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization. A successful exploit of this vulnerability requires could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts to the integrity, and availability of the system.'),
 ('MTLVULN-1877 text', UM, M, 'could allow an unauthenticated attacker to conduct an authentication bypass attack due to improper handling of authentication.'),
 ('MTLVULN-1877 impact', UM, M, 'A successful exploit of this vulnerability could allow an attacker to bypass authentication controls and perform unauthorized actions within the context of the application.'),
]))
A('')
A('### 2.3 Exploitation statement\n')
A('The advisory contains NO statement either way about exploitation or public exploits: every occurrence of "exploit" on the page (6 lines, listed by `grep -n -i exploit mitel/misa-2026-0012.extract.md`) is conditional ("if successfully exploited") or the chaining sentence above. The first pass wrote "No exploitation or public PoC is stated in the advisory" - that is accurate as an absence, and must not be rendered as "Mitel says it is not exploited".\n')
A('### 2.4 CVE assignment since publication (checked 2026-11-18)\n')
A(table([
 ('Mitel page still says CVE requested, not assigned', UM, M, 'A CVE identifier has been requested but is not yet assigned'),
 ('ENISA EUVD search text=micollab, 2026-11-10..2026-11-18: zero records', 'https://euvdservices.enisa.europa.eu/api/search?text=micollab&fromDate=2026-11-10&toDate=2026-11-18&page=0&size=50', 'mitel/euvd-micollab.json', '{"items":[],"total":0}'),
 ('ENISA EUVD search text=mitel, same window: zero records', 'https://euvdservices.enisa.europa.eu/api/search?text=mitel&fromDate=2026-11-10&toDate=2026-11-18&page=0&size=50', 'mitel/euvd-mitel.json', '{"items":[],"total":0}'),
 ('NVD CVE API keywordSearch=MiCollab, published 2026-11-10..2026-11-18: zero results', 'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=MiCollab&pubStartDate=2026-11-10T00:00:00.000&pubEndDate=2026-11-18T23:59:59.000', 'mitel/nvd-micollab.json', '"totalResults":0'),
 ('BSI CSAF lists five vulnerability objects with no CVE id (release date only)', 'https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json', BC, '"release_date": "2026-11-16T23:00:00.000+00:00"'),
]))
A('')
A('### 2.5 Third-party authorities (none states exploitation)\n')
A(table([
 ('CERT-FR lists the advisory the next day (CERTFR-2026-AVI-1547; initial version 17 November 2026)', UCF, CFR, '17 novembre 2026\nVersion initiale'.replace('\n', '\n')),
 ('CERT-FR affected range: "before 10.3.0.18" - differs from Mitel ("10.3 (10.3.0.18) and earlier")', UCF, CF, '- MiCollab versions antérieures à 10.3.0.18'),
 ('CERT-FR risk summary: some of them allow remote code execution, remote denial of service and loss of confidentiality (CERT-FR\'s wording, not Mitel\'s)', UCF, CF, 'Certaines d\'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données.'),
 ('CERT-FR points to Mitel bulletin 2026-0012 of 16 November 2026', UCF, CF, 'Bulletin de sécurité Mitel 2026-0012 du 16 novembre 2026'),
 ('BSI WID-SEC-2026-4608 (hoch, initial 2026-11-16T23:00Z, generated 2026-11-17 11:57Z): remote anonymous attacker; manipulate files, run code with service rights, bypass security, disclose information', UBS, BD, 'Ein entfernter, anonymer Angreifer kann mehrere Schwachstellen in Mitel MiCollab ausnutzen, um Dateien zu manipulieren, beliebigen Programmcode mit den Rechten des Dienstes auszuführen, Sicherheitsmaßnahmen zu umgehen, Informationen offenzulegen, oder nicht spezifizierte Angriffe durchzuführen.'),
 ('BSI product tree: affected "<10.3.0.18", fixed 10.3.0.18 (again differs from Mitel)', 'https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json', BC, '"name": "<10.3.0.18"'),
 ('BSI severity', UBS, BD, 'aggregate_severity: hoch'),
]))
A('')
A('### 2.6 Version table\n')
A('| source | affected | fixed / action |')
A('|---|---|---|')
A('| Mitel MISA-2026-0012 | MiCollab 10.3 (10.3.0.18) and earlier (supported versions only) | patch from KB000129195 on release 10.3 (10.3.0.18), or a later release; no later release number named |')
A('| CERT-FR AVI-1547 (17 Nov) | versions before 10.3.0.18 | see vendor bulletin |')
A('| BSI WID-SEC-2026-4608 (CSAF product tree) | < 10.3.0.18 | 10.3.0.18 listed as fixed |')
A('| Mitel MISA-2026-0006 (2026-07-22, prior entry `2026-07-24/mitel-micollab-awv-unauth-command-injection`) | 10.0 (10.0.0.26) to 10.2 SP1 FP2 (10.2.1.205) and 9.8 SP3 FP2 (9.8.3.203) and earlier | "Upgrade to version 10.3 (10.3.0.18) or subsequent releases"; patches for 10.2 SP1 FP2 and 9.8 SP3 FP2 (KB000128275) |')
A('')
A(table([
 ('Prior advisory MISA-2026-0006 fixed MTLVULN-1694 (9.8) in 10.3 (10.3.0.18)', UM6, M6, 'This issue is addressed in MiCollab version 10.3 (10.3.0.18).'),
 ('Prior advisory affected range for 0006', UM6, M6, '10.0 (10.0.0.26) to 10.2 SP1 FP2 (10.2.1.205) and 9.8 SP3 FP2 (9.8.3.203) and earlier'),
 ('Prior row MTLVULN-1694 Critical / 9.8', UM6, M6, '| MiCollab | MTLVULN-1694 | Critical / 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H |'),
]))
A('')
A('Consequence stated by the two Mitel pages together (inference, labelled): a site that moved to 10.3.0.18 after MISA-2026-0006 in July is within "10.3 (10.3.0.18) and earlier" of MISA-2026-0012 and still needs the new patch. Mitel does not say this in words.\n')
A('### 2.7 Contradictions with the first pass (item 7) and open gaps\n')
A('- CONFIRMED: affected 10.3 (10.3.0.18) and earlier; each MTLVULN row and score (1864 10.0, 1862 9.0, 1863 5.9, 1861 5.3, 1877 5.3); KB000129195; mitigation sentence; no CVE ids yet; no exploitation statement in the advisory; CERT-FR AVI-1547 on 2026-11-17 and BSI WID-SEC-2026-4608.')
A('- First pass says CERT-FR words the range as "before 10.3.0.18"; confirmed. Not in the first pass: BSI\'s own product tree also says "<10.3.0.18" with 10.3.0.18 fixed, i.e. both CERTs differ from Mitel.')
A('- First pass summary calls MTLVULN-1862 "XML injection that lets an unauthenticated attacker leverage pre-staged malicious content to execute commands": consistent with the page, but the page states the XML injection "could allow an attacker to execute arbitrary commands" (a possibility), so keep "could".')
A('- First pass cites BSI as "describes ... bypass security measures": confirmed (BSI line above). BSI lists "Windows, Linux, MacOS X, UNIX" as OS (BSI boilerplate, not Mitel).')
A('- NEW: the MTLVULN-1864 impact sentence is garbled in the original ("requires could allow"); a precondition may have been deleted. Mitel\'s vector still scores it PR:N/UI:N/AC:L.')
A('- OPEN: "and earlier" is not mapped to branches: the page names only 10.3 and gives no patch for 10.2 or 9.8 branches, although MISA-2026-0006 had patches for 10.2 SP1 FP2 and 9.8 SP3 FP2. Whether those branches are affected, fixed or simply unsupported is not stated. The KB (portal login) probably says; it could not be read.')
A('- OPEN: no later release number is named although the page says "or upgrade to a later release" and "will be included in later MiCollab releases".')
A('- OPEN: Mitel\'s own security-advisory index was not separately checked for a revision after 2026-11-16 (the advisory page itself shows revision 1.0 only). No CERT or vendor states exploitation as of 2026-11-18 ~04:45Z.\n')
SECTION = '\n'.join(out)
