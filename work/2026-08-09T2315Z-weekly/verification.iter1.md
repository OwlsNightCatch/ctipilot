**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-10T00:12:13Z · ended_at=2026-08-10T00:46:40Z · duration_seconds=2067
**Self-telemetry:** urls_checked=57 · webfetch_calls=24 · websearch_calls=1 · bridge_fetches=31

## Verification report — 2026-08-09T2315Z-weekly (iteration 1)

Cold read of all 16 new strategic entries plus the run record. Every inline citation was fetched in this
iteration (WebFetch, `tools/fetch_source.py url`, `cisa page`, and the jina reader for two SPA/PDF targets).
Quotes were literal-substring checked against the fetched body, not against a summariser's paraphrase — this
matters: the WebFetch summariser returned a *paraphrased* "quote" for the admin.ch release and invented a CVE
id for the Traefik GHSA, both of which the raw fetch disproved. No finding below rests on a summariser.

Two citations could not be reached and are **not** counted as findings: `www.reuters.com/...metas-ai-model-hacked...`
(CAPTCHA wall to WebFetch and to the bridge; the run record already documents the HTTP 401 and the successful
run-time fetch) and the Dark Reading page, which 403s WebFetch but was recovered through the bridge and verified.

### Citation does not support the claim

**F3.1 — `weekly-w32-european-government-own-infrastructure-breached`: the CERT Polska detail is in the PDF report, not on the cited blog post.**
Claim (body ¶4): *"a combined heat and power plant supplying about 50,000 residents, where three Siemens PLCs were switched to STOP mode and password-locked … The attacker reached it from an already-compromised wind-farm substation by tunnelling over SSH through a cellular router into the distribution system operator's private APN … and then into a WAGO PFC200 controller whose WAN-side web interface answered on factory credentials"* — all terminated by `([CERT Polska, 2026-08-08](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/))`.
I fetched that page in full (81 KB, bridge). Its entire body is ~7 sentences: it names the 50,000 residents, the
steam turbine and water-treatment shutdown, the private-APN novelty and the misconfiguration, and links to the PDF.
It contains **no** occurrence of "WAGO", "PFC200", "Siemens", "substation", "SSH", "STOP", or "factory".
I then downloaded `https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf` and
extracted its text: it *does* carry all of them ("a WAGO PFC…PLC equipped with an integrated cellular modem";
"fully established connections to three Siemens PLC…"; "Activity at the Wind Farm"; "Leveraging the Private APN
for Lateral Movement"; "WAN interface, which was reachable from the APN"; "…dentials for the \"admin\" account").
The operational entry `2026-08-09/cert-polska-private-apn-pivot-into-ot-chp-plant-shutdown` correctly cites **both**
the blog and the PDF; this weekly entry cites only the blog. Fix: add the PDF as a `sources[]` record and attach
the mechanics clause to it.

**F3.2 — `weekly-w32-ci-exposure-outside-the-it-patch-estate`: identical defect, same source.**
Claim (body ¶2): *"traces an intrusion from a compromised wind-farm substation, over SSH through a cellular router,
into the distribution system operator's private APN … and from there into a controller whose WAN-side interface
answered on factory credentials, ending with three PLCs in STOP mode and a steam turbine offline"* — the paragraph's
only citation is the same blog URL. `affected_products: ["Zbtlink router and CPE models", "WAGO PFC200"]` likewise
names a product no cited page mentions. Same remedy: add the PDF record.

**F3.3 — `weekly-w32-european-government-own-infrastructure-breached`: "two files placed" is not in the Graubünden press release.**
Claim: *"a compromise of a SharePoint server hosting the cantonal administration's public web presence, with two
files placed and, on first analysis, no accounts compromised and no data exfiltrated ([Kanton Graubünden, 2026-08-05](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx))"*.
I fetched the page (raw, 2,896 chars of body text). It says *"Erste Erkenntnisse weisen darauf hin, dass dabei keine
Daten abgeflossen und keine Konten kompromittiert worden sind"* and *"Eine erste Analyse hat ergeben, dass es keine
Anzeichen darauf gibt, dass Konten kompromittiert oder Daten abgeflossen sind"* — and says nothing about any files.
The operational entry `2026-08-06/canton-graubuenden-sharepoint-server-breach` attributes the two files to
persoenlich.com/Keystone-SDA (`evidence[]`: *"Es wurden zwei Dateien platziert, deren Code allerdings nicht ausgeführt
worden sei." — persoenlich.com`). The weekly entry attributes it to the canton. Fix: cite persoenlich.com for that
clause or drop the file count.

**F3.4 — `weekly-w32-european-government-own-infrastructure-breached`: WIRED does not say the Flemish intrusion came through a contractor's workstation.**
Claim (body ¶4, and repeated in `summary`: *"a Flemish Government agency confirmed a North Korean intrusion via a
contractor"*, and in the takeaway as *"a third party's endpoint"*): *"Digitaal Vlaanderen confirmed to WIRED that
Belgium's Centre for Cybersecurity notified it on 3 March 2026 of a North Korean compromise reaching it through a
contractor's workstation ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/))"*.
I fetched the article via the bridge (datePublished `2026-08-05T19:30:00-04:00`, so the 2026-08-05 citation date is
right) and grepped every occurrence of "contractor". The Flemish spokesperson's quote is:
*"We can confirm that we were notified of this incident on March 3, 2026 by the Centre for Cybersecurity Belgium (CCB),
following the researcher's disclosure … the affected workstation was isolated and the potentially exposed credentials
and access were revoked and rotated."* No contractor. The "contractor's personal device" detail in that article belongs
to **Boston Children's Hospital** (*"involved a former independent contractor's personal device"*); the contractor
framing is otherwise a *general* observation by Stykas across the 1,640 victims, not a statement about Digitaal
Vlaanderen. Fix: say "a workstation" (per the source) or attribute the contractor framing to the campaign generally.

**F3.5 — `weekly-w32-the-vendor-fix-was-not-the-end-state`: the N-able "alternative method" quote is not on the cited page, and the citation date is wrong.**
Body: *"then confirmed that its own earlier remediation had failed: \"we identified an alternative method to exploit this
vulnerability, which was not mitigated in our previous fix\" ([N-able, 2026-08-02](https://www.n-able.com/blog/n-central-security-update-august-2-2026))"*,
and the identical string is `evidence[0]` attributed to publisher "N-able".
I fetched that URL raw. The page is now titled **"N-central Security Update – August 6, 2026"** with
`Published Time: 2026-08-06T00:22:07+01:00` (N-able edits this post in place). Literal substring test for the quote:
**False**. I also fetched both status-page advisories — `…/2026/08/02/n-central-2026-3-hotfix-1-…` and
`…/2026/08/06/n-central-2026-3-hotfix-2-…` — and the sentence is absent from both. This run's own quality audit
already recorded the defect on the *operational* entry (`work/2026-08-09T1315Z-audit/truth-B2.yaml`, verdict
"imprecision"); the weekly carried the unverifiable quote forward into a new entry. Two consequences: (a) the
`evidence[]` record is not a verbatim substring of any page in this entry's `sources[]`; (b) `date: "2026-08-02"`
is four days off the page's own published time. The *claim* is fine — the Hotfix 2 status page ("Hotfix 2 supersedes
Hotfix 1 with additional hardening measures", verified verbatim) supports it. Fix: drop the quote and rest the
sentence on the Hotfix 2 page, and correct or footnote the source date.

**F3.6 — `weekly-w32-the-vendor-fix-was-not-the-end-state`: the Tomcat 9.x and 10.x versions are not on `security-11.html`.**
Claim: *"so the only affected releases are the three that carried the broken fix, 9.0.116, 10.1.53 and 11.0.20 ([Apache Tomcat, 2026-04-09](https://tomcat.apache.org/security-11.html))"*.
The fetched page is the **Tomcat 11** security page. It carries the quoted sentence *"An error in the fix for
CVE-2026-29146 allowed the EncryptInterceptor to be bypassed"* verbatim and states affected **11.0.20**, fixed
11.0.21 — and nothing about 9.0.116 or 10.1.53, which live on `security-9.html` / `security-10.html`. Fix: cite the
9.x/10.x pages for those two versions (the operational entry `2026-08-05/cve-2026-34486-…` carries them as an action).

**F3.7 — `weekly-w32-cve-record-unreliable-in-both-directions`: CERT-FR carries none of the WALLIX facts attached to it.**
Claim: *"CERT-FR relayed a WALLIX Bastion authentication bypass rated CVSS 4.0 base 10.0 that hands a remote
unauthenticated caller full administrative control of a privileged-access appliance — its credential vault and session
recordings included — under a vendor advisory reference rather than a CVE ([CERT-FR, 2026-08-06](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/))"*.
I fetched the advisory raw; it is ~1,800 characters and reads in full: *"Risques: Contournement de la politique de
sécurité / Élévation de privilèges … De multiples vulnérabilités ont été découvertes dans les produits Wallix. Elles
permettent à un attaquant de provoquer une élévation de privilèges et un contournement de la politique de sécurité."*
plus affected/fixed versions and a pointer to the *"Bulletin de sécurité Wallix du 20 juillet 2026"*. There is **no
CVSS score**, no "unauthenticated", no "authentication bypass", and no mention of a vault or session recordings.
The operational entry `2026-08-09/wallix-bastion-rest-api-unauth-admin-cvss10` correctly makes
`https://www.wallix.com/support-services/alerts/` the primary and quotes it for exactly these facts. Fix: re-cite to
the WALLIX bulletin.

**F3.8 — `weekly-w32-looking-ahead`: the September-disclosure commitment and the CVSS score are attributed to CERT-FR, which states neither.**
Claim: *"WALLIX states that the reporting researchers intend to publish the complete write-up of the CVSS 4.0 base 10.0
flaw … in September ([CERT-FR, 2026-08-06](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/)). Bastion 12.3.7 and
12.4.1 and later are patched."* Same fetch as F3.7: CERT-FR carries the fixed versions (12.3.7 / 12.4.1) but neither
the score nor any September statement — and the sentence itself says "WALLIX states", so the citation should be the
WALLIX bulletin. Fix: cite `https://www.wallix.com/support-services/alerts/` for the clause.

**F3.9 — `weekly-w32-cve-record-unreliable-in-both-directions`: the Metabase exploitation date and victim count are not on the Metabase post.**
Claim: *"([Metabase, 2026-08-06](https://www.metabase.com/blog/security-update)) — exploited since 3 August, with two
customers confirming data theft, and no CVE assigned"*.
I fetched the post raw (published "Aug 6, 2026", quote *"We recently identified that Metabase Cloud was attacked by
someone utilizing an unknown (“0-day”) security vulnerability in versions 1.58 and above."* — verbatim ✓, including the
curly quotes). The post gives **no** exploitation date and **no** customer count. The operational entry
`2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally` sources those to BleepingComputer
(`https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/`, Framework and
Tally, 2026-08-03). Fix: add that citation for the clause.

**F3.10 — `weekly-w32-vuln-status-rollup`: the crypto-js version boundary and the CVE id are attributed to Coinspect, which names neither.**
Claim: *"Coinspect traced an active wallet-drain campaign to a weak pseudo-random generator in crypto-js below 4.0.0,
stating that \"attackers were already exploiting it while our investigation was underway\" ([Coinspect Security, 2026-08-05](https://www.coinspect.com/blog/ill-bloom-investigation/)); the identifier CVE-2026-71851 exists but the flaw is not catalogued"*.
I fetched the Coinspect post raw: the quoted sentence is present verbatim, but the page contains **zero** occurrences of
"4.0.0", "crypto-js" (it writes "CryptoJS"), or any CVE identifier. I confirmed the facts independently against NVD
(CVE-2026-71851, published 2026-08-07, CVSS 3.1 9.0, *"Versions of crypto-js prior to 4.0.0 generate randomness … using
a custom variation of the Multiply-With-Carry pseudorandom number generator, seeded from Math.random()"*). The fix is
one line: the entry already carries `https://github.com/advisories/GHSA-rg76-677x-56q9` in `sources[]` — attach that
citation to the version/identifier clause.

**F3.11 — `weekly-w32-vuln-status-rollup`: the Cisco FMC citation date matches nothing on the advisory, and the revision claim is stale.**
`sources[]` record: `cisco-sa-onprem-fmc-authbypass-5JPp45V2`, `date: "2026-08-03"`. The advisory's own metadata reads
**First Published: 4 March 2026 · Last Updated: 5 August 2026 · Version 2.4**. Neither is 3 August, so the citation date
drifts by more than two days from any date the page states. Relatedly, the body says *"per-train hot fixes on 2026-07-31
after five months unpatched; the compromise check was revised three times to 2026-08-03"* — the advisory has since gone
to v2.4 on 5 August, so a roll-up dated at the close of W32 (9 August) understates the revision count. Fix: set the
source date to the advisory's last-updated date and re-check the revision count.

**F3.12 — `weekly-w32-passkeys-attacked-from-four-directions`: the characterisation is Mollema's, not Microsoft's, and the cited article says Microsoft has not replied.**
Claim (body ¶2): *"Microsoft did not assign a CVE or ship a fix, characterising the behaviour as a consequence of how
Windows Hello for Business works ([The Hacker News, 2026-08-07](https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html))"*.
Repeated in `summary` (*"behaviour Microsoft declined to assign a CVE or patch"*) and in `sourcing_note`
(*"Microsoft declined to patch it as a consequence of the design"*).
I fetched the THN article raw. Its exact sentence is: *"**Mollema** describes the behavior as a consequence of how
Windows Hello for Business works and says it was left as-is."* Two sentences later: *"The Hacker News found no CVE or
Microsoft advisory tied to the technique in searches of Microsoft's Security Update Guide, NVD, and CVE.org as of
August 6, 2026. **The Hacker News has contacted Microsoft and Mollema; replies are pending.**"* The framing also
originates in Mollema's own post, which I substring-checked in `work/…/text.mollema.txt`: *"a technique that was left
as-is since it is more or less a consequence of how WHFB works"*. So the entry moves a researcher's characterisation
onto the vendor and turns an absence of a CVE into a vendor decision ("declined"), neither of which any cited source
states. This is the load-bearing sentence of the entry's lead paragraph. Fix: attribute the characterisation to Mollema
and say that no CVE or advisory exists and Microsoft has not commented.

**F3.13 — `weekly-w32-nis2-enforcement-phase-netherlands-germany`: the BSI press release is cited with a date the page contradicts.**
`sources[]`: `…/Presse2026/260601_NIS2_BSI-Portal.html`, `date: "2026-06-01"`; body: *"BSI's own **June** press release
establishes the population … ([BSI, 2026-06-01](…))"*. I fetched the page raw. Its own dateline field reads
`Ort Bonn · **Datum 06.01.2026**` — 6 January 2026 in the German DD.MM.YYYY convention. (The URL slug `260601` is what
appears to have driven the 1 June reading; the page's visible date field is the authority.) The entry's own argument
corroborates January: it cites 11,388 registrations *as of 5 March 2026*, which would be impossible if the BSI
registration portal only opened on 1 June. Everything else in the German block verified clean — I substring-checked
*"Die gesetzliche Registrierungsfrist ist bereits abgelaufen. Von NIS-2 betroffen und noch nicht registriert? Dann jetzt
umgehend im BSI-Portal registrieren!"* ✓, *"Für rund 29.500 Unternehmen in Deutschland und Institutionen der
Bundesverwaltung gelten seit Inkrafttreten des NIS-2-Umsetzungsgesetzes neue gesetzliche Pflichten in der
IT-Sicherheit."* ✓, and — via the jina reader on the 169-page PDF — *"Zum 5. März 2026 waren 11.388 wichtige und
besonders wichtige Einrichtungen beim Bundesamt für Sicherheit in der Informationstechnik (BSI) registriert."* ✓ in
Drucksache 21/4657, dated 13.03.2026 on its own cover ✓. **The provenance split the run record describes survives intact
and correctly** — the 11,388/5 March official figure and the ~18,500/31 July trade-press figures are separated in both
the body and the `sourcing_note`, and the trade-press figures are never asserted as fact. Fix is only the date.

**F3.14 — `weekly-w32-water-plc-lockout-status`: "IRGC-linked" and "under investigation" go beyond the cited article.**
Claim: *"even as technical consolidation ties the targeted-device profile and the PLC-lockout tradecraft to previously
documented IRGC-linked activity against industrial controllers, and reporting refers to an Iran connection under
investigation ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment))"*.
I fetched the article (byline "August 5th, 2026" ✓). It says: *"a campaign allegedly linked to Iranian hackers"* and
*"While federal agencies have declined to publicly attribute the attacks, multiple sources pointed the finger at Iran,
which since 2023 has repeatedly targeted a specific kind of operational technology used by water and wastewater
facilities."* The string "IRGC" does not appear, and nothing frames the connection as "under investigation". The
entry's own headline correctly says *"an attribution that no US authority will make"*, so the body sentence is a step
further than the entry's own thesis. Fix: use the source's own register ("Iran", "multiple sources", "no public
attribution"), or cite a source that names the IRGC.

### Unsupported / hallucinated facts

**F4.1 — `weekly-w32-vuln-status-rollup`: the headline and title say four new KEV listings; the entry's own body and table list five.**
`headline`: *"W32 CVE trajectory — **four new KEV listings**, two exploited flaws with no catalogue entry, and five
products with no fix coming"*. `title`: *"seven CVEs and one unnumbered zero-day stood at confirmed exploitation,
**four of them newly catalogued this week**"*.
The body says: *"CISA added three flaws to its Known Exploited Vulnerabilities catalogue on 4 August — … CVE-2026-18556
… CVE-2026-34486 … CVE-2026-9198 … — followed by … CVE-2026-63077 on 5 August … and … CVE-2026-8037 on 7 August"*, and
the status table carries five rows each stamped "KEV-listed". I verified all three CISA alerts through
`tools/fetch_source.py cisa page`: 2026/08/04 lists CVE-2026-9198, CVE-2026-18556, CVE-2026-34486; 2026/08/05 lists
CVE-2026-63077; 2026/08/07 lists CVE-2026-8037 — **five in-window additions**. Frontmatter therefore understates the
entry's own verified content. (The `evidence[]` quote *"based on evidence of active exploitation"* is verbatim on all
three alerts ✓.) Fix: four → five in both fields.

**F4.2 — `weekly-w32-assurance-moves-into-procurement-language`: the title says "a day apart"; both publications are the same day.**
`title`: *"**Two publications a day apart** moved security assurance out of guidance and into what buyers must ask for"*.
The entry's own `summary` says *"On 29 July NCSC UK published …"* and *"**The same day**, CISA, the NSA, the FBI and
fifteen international agencies … published the 2026 Minimum Elements"*; the body repeats *"The same day"*. I confirmed
both dates at source: the NCSC UK post's own field reads *"Published … Publish date 29 July 2026"*, and the CISA PDF's
cover reads *"2026 Minimum Elements for a Software Bill of Materials (SBOM) Publication: July 29, 2026"*. Everything
else on this entry verified clean — all four `evidence[]` quotes are verbatim (NCSC UK's forensic-observability
definition ✓, the "Buyers: … push for it" paragraph ✓, the reference-architecture sentence ✓, and CISA's *"which
incorporates feedback from more than 90 comments received during the public comment period…"* ✓), the new-element list
matches the PDF's own "New SBOM elements" bullets exactly ✓, the AI-scope caveat is the PDF's own *"this document does
not introduce additional elements for SBOMs for AI systems"* ✓, the hash definition matches *"The output generated from
applying a cryptographic hash algorithm to an executable component artifact"* ✓, and the 18-agency seal line does carry
BSI, ANSSI and NCSC-NL ✓. Fix: the title's "a day apart".

**F4.3 — `weekly-w32-passkeys-attacked-from-four-directions`: the `cves[]` record attributes "passkey data" to the CVE record, which does not say it.**
`cves[0].affected`: *"Windows Event Logging Service, per the CVE record — **passkey data** exposed to an authorized
attacker over a network"*. I pulled the NVD record for CVE-2026-34348 (`services.nvd.nist.gov/rest/json/cves/2.0`):
published 2026-07-14, CVSS 3.1 base 6.5 (both matching the entry ✓), description *"Protection mechanism failure in
Windows Event Logging Service allows an authorized attacker to disclose information over a network."* The record says
"information", not "passkey data". The specificity is true (independently: the event log wrote passkey-related key
material in cleartext) but it is **not** "per the CVE record". Fix: drop the "per the CVE record" attribution or
reword to what the record states.

### Claims missing inline citation

**F5.1 — `weekly-w32-passkeys-attacked-from-four-directions`: the entire Grafnetter / CVE-2026-34348 disambiguation is uncited.**
Body ¶2 closes: *"Separately at the same conference, Michael Grafnetter's \"Pass-the-Passkey\" work covered a related
class whose event-log passkey-data-exposure element carries CVE-2026-34348 and was closed by Microsoft on 14 July 2026"*,
and `sourcing_note` restates it. I fetched all four `sources[]` records in this iteration —
`dirkjanm.io/borrowing-windows-hello-keys/`, `unit42.paloaltonetworks.com/passwordless-authentication-security-risks/`,
`cloud.google.com/…/unc6671-…`, `thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html` — and **none of
them names Grafnetter or CVE-2026-34348**. (I grepped the THN body: `Grafnetter: False`, `34348: False`.) The claim
appears to be correct on the facts — an independent search surfaced SpecterOps/Grafnetter's Black Hat USA 26
"Pass-the-Passkey" talk and CVE-2026-34348 as the Windows event-log passkey exposure — but the entry cites nothing for
it. This matters more than usual because the paragraph exists specifically to keep the two Black Hat talks apart, i.e.
the disambiguating claim is doing the safety work. **Note for the record: I checked trap (a) and the entry nowhere
implies Microsoft patched the assertion-borrowing behaviour** — the separation is stated correctly in body,
`sourcing_note` and `cves[].fixed`; the defect is only that the Grafnetter half is unsourced (plus F3.12/F4.3 above).
Fix: add a source for the Grafnetter/CVE link.

**F5.2 — `weekly-w32-vuln-status-rollup`: the Metabase paragraph's closing sentence carries no citation.**
*"The Metabase SQL-injection zero-day, exploited since 3 August with two customers confirming data theft, has no CVE
identifier at all."* The preceding citation on that paragraph is Coinspect, which is about crypto-js. Same underlying
source gap as F3.9; needs its own fix because it is a different entry.

### Editorial / less-is-more flags (advisory)

**F11.1 — `weekly-w32-european-government-own-infrastructure-breached`: the frontmatter's "three of the five" enumerates two incidents, and the headline count does not match the body.**
`summary`: *"In **three of the five** the path ran through infrastructure that does not appear in an internet-facing
asset inventory: a mobile carrier's private APN, a controller answering on factory credentials on its WAN side, and an
Oracle WebLogic server whose last patches date to a 2017 cycle."* The first two items are both the Polish case, so the
list covers two incidents, not three — while the body's own takeaway names the three as *"the Polish, Hungarian and
Belgian cases … a carrier-provided private APN …, a legacy application server nine years behind its patch cycle, and a
third party's endpoint"*. Separately, `headline` says *"**Five** European public bodies compromised in one week"* while
six organisations are named (BIT, Canton Graubünden, Liechtenstein's Amt für Justiz, the Hungarian Treasury's MVH, the
Polish CHP plant, Digitaal Vlaanderen) and one of them is a power plant rather than a public body; the body's
*"five European jurisdictions"* is the accurate formulation. Advisory — no external fact is wrong.

**F11.2 — `weekly-w32-open-source-supply-chain-status`: one quotation carries inserted whitespace.**
Body: *"were published with a malicious preinstall hook **( setup.mjs )** that downloads a standalone Bun runtime…"*.
The Socket page (verified against `work/…/text.socket.txt`, line 325) reads *"(setup.mjs)"* without the inner spaces.
Everything else on this entry is verbatim: both `evidence[]` quotes pass the literal-substring test against the saved
body, and Unit 42's *"This is not forged provenance"* framing is confirmed on
`unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/` (2026-08-06). **Confirming the run record's own note: none of
the three dropped Socket figures (package-name count, poisoned-version count, mean detection latency) appears anywhere
in the entry.** Advisory only.

### Action-item discipline

**F18.1 — `weekly-w32-the-vendor-fix-was-not-the-end-state`: the single action duplicates two actions already carried by a same-day operational entry.**
Weekly action: *"Re-verify N-able N-central is on build 2026.3.1.10 (Hotfix 2) — 2026.3.1.7 is superseded — and treat
every endpoint the console manages as in scope for a compromise assessment, because the actor reached them through Take
Control and left a Cloudflare Tunnel service behind."*
`entries/2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1.md` — published the same day, so it renders
into the same § Action Items list — already carries: *"Upgrade on-premises N-central to 2026.3.1.10 even where
2026.3.1.7 was already applied — the vendor states Hotfix 2 is required regardless and supersedes…"* and *"Extend the
compromise assessment from the N-central server to the endpoints it manages, looking specifically for a newly registered
service running a …"*. The weekly action is a merge of those two with no delta. Per check 10b(d) an in-window duplicate
should not ship; `actions: []` is the correct output here (the entry's week-level point is the pattern, not the task).
For contrast, the other three weekly actions are **not** duplicates and should stay: the supply-chain entry's
persistence-before-rotation ordering is the week's genuine delta and inverts, rather than repeats, the 2026-08-06
ChainDrop actions; the water entry's MicroLogix 1100/1400 inventory rests on the device naming that only became
available this week; and the CI-exposure entry's dedicated-encryption-device lever comes from the CI Fortify guidance,
which no operational entry carried.

### Verdict

Everything not listed above verified clean, including material I checked specifically because the spawn message flagged
it. Confirmed as correct: the passkeys entry never implies Microsoft patched the assertion-borrowing behaviour (both
Mollema quotes are verbatim in `text.mollema.txt`, and the CVE-2026-34348 patch date 2026-07-14 matches NVD); the German
NIS2 provenance split is intact and the 11,388/5 March figure is verbatim in Drucksache 21/4657; the EU AI Act entry's
three EUR-Lex quotes are all verbatim in the amending regulation and the 27 July entry-into-force follows from its own
*"third day following that of its publication"* recital against an OJ date of 24.7.2026; the Semperis, Unit 42 (DNS and
passkeys), Socket, Tenable and CISA/KEV quotes all pass literal-substring checks; the Kerberos entry's two CVSS scores
and both NVD publication dates match the authority exactly (8.8/2026-03-10, 8.0/2026-04-14); CI Fortify's three quotes
and its 28 July "first published" field check out; the CPDLC advisory's `none_available` remediation and *"unlikely to
be exploited outside of a lab setting"* are both in CISA's own CSAF; and the ISV Art. 51(4) / Art. 52 derivation of the
1 January 2027 Swiss ISMS deadline is exact.

On the four questions the spawn message asked me to judge rather than verify: **W-PD-1** — every entry answers at least
one of the three questions, and the CVE-record entry's differentiation from W31's "both prioritisation feeds failed" is
real rather than cosmetic (W31's axis is the *feeds* — KEV listing and patch availability; W32's is the *identifier* —
fabricated ids, absent ids, and one-CVE-per-bug-class granularity), stated in its own opening sentence. **Recency
honesty** — all five backlog entries state their source's real publication date plainly and two say outright that the
item pre-dates the window; none reads as in-window. **Priority calibration** — the split is 8 `high` / 8 `notable`
(the spawn message said seven/nine), which tracks W31's 7/15 and I would not push back on any individual `high`; no
`critical`, correctly. **Coverage** — I found no in-window story I can name a plausible source for that the run missed;
the empty annual-reports section and the empty in-window policy sweep are both explained and both look right.

`NEEDS_FIXES (truth: 17, editorial: 3, advisory: 2)`


### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-european-government-own-infrastructure-breached"
  url_or_quote: "https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/ — \"three Siemens PLCs were switched to STOP mode and password-locked ... into a WAGO PFC200 controller whose WAN-side web interface answered on factory credentials\""
  summary: "Fetched the cited blog post in full: it contains no occurrence of WAGO, PFC200, Siemens, substation, SSH, STOP or factory. All those facts are in the linked PDF report (CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf), which I downloaded and confirmed carries them. The operational entry 2026-08-09/cert-polska-private-apn-pivot-into-ot-chp-plant-shutdown cites both. Add the PDF as a sources[] record and attach the mechanics clause to it."
- code: F3
  category: claim-not-supported
  section: weekly-sector-patterns
  item: "weekly-w32-ci-exposure-outside-the-it-patch-estate"
  url_or_quote: "https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/ — \"over SSH through a cellular router ... a controller whose WAN-side interface answered on factory credentials, ending with three PLCs in STOP mode\"; also affected_products includes \"WAGO PFC200\""
  summary: "Same defect as on the top-stories entry: the PDF-only mechanics are cited to the blog post, which carries none of them, and WAGO PFC200 is named as an affected product by no cited page. Add the PDF source record."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-european-government-own-infrastructure-breached"
  url_or_quote: "https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx — \"with two files placed\""
  summary: "Fetched the Graubuenden press release raw (2,896 chars of body). It states no accounts compromised and no data exfiltrated but says nothing about placed files. The two-files detail comes from persoenlich.com/Keystone-SDA, as the operational entry 2026-08-06/canton-graubuenden-sharepoint-server-breach attributes it. Re-cite or drop."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-european-government-own-infrastructure-breached"
  url_or_quote: "https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/ — \"a North Korean compromise reaching it through a contractor's workstation\""
  summary: "Fetched WIRED via the bridge and checked every occurrence of 'contractor'. The Flemish spokesperson says only that 'the affected workstation was isolated'; the contractor's-personal-device detail belongs to Boston Children's Hospital. Also propagates into summary ('via a contractor') and the takeaway ('a third party's endpoint'). Say 'a workstation' or attribute the contractor framing to the campaign generally."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-the-vendor-fix-was-not-the-end-state"
  url_or_quote: "https://www.n-able.com/blog/n-central-security-update-august-2-2026 — \"we identified an alternative method to exploit this vulnerability, which was not mitigated in our previous fix\" (body quote AND evidence[0]); source date 2026-08-02"
  summary: "Fetched the URL raw: the page is now titled 'N-central Security Update - August 6, 2026' with Published Time 2026-08-06T00:22:07+01:00, and literal-substring test for the quote is False. Also absent from both status.n-able.com Hotfix 1 and Hotfix 2 pages, which I fetched. This run's own audit already logged the defect on the operational entry (work/2026-08-09T1315Z-audit/truth-B2.yaml). Drop the quote and rest the sentence on the Hotfix 2 page (whose supersession language is verbatim); correct the source date."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-the-vendor-fix-was-not-the-end-state"
  url_or_quote: "https://tomcat.apache.org/security-11.html — \"the only affected releases are the three that carried the broken fix, 9.0.116, 10.1.53 and 11.0.20\""
  summary: "The cited page is the Tomcat 11 security page. It carries the CVE-2026-34486 sentence verbatim and states affected 11.0.20 / fixed 11.0.21, but says nothing about 9.0.116 or 10.1.53, which live on security-9.html and security-10.html. Cite those pages for the 9.x/10.x versions."
- code: F3
  category: claim-not-supported
  section: weekly-multi-day
  item: "weekly-w32-cve-record-unreliable-in-both-directions"
  url_or_quote: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/ — \"a WALLIX Bastion authentication bypass rated CVSS 4.0 base 10.0 that hands a remote unauthenticated caller full administrative control ... its credential vault and session recordings included\""
  summary: "Fetched the advisory raw (~1,800 chars). It states only 'Contournement de la politique de securite / Elevation de privileges' plus affected/fixed versions and a pointer to the WALLIX bulletin of 20 July 2026. No CVSS, no 'unauthenticated', no vault or session recordings. Re-cite to https://www.wallix.com/support-services/alerts/, as the operational entry 2026-08-09/wallix-bastion-rest-api-unauth-admin-cvss10 does."
- code: F3
  category: claim-not-supported
  section: weekly-looking-ahead
  item: "weekly-w32-looking-ahead"
  url_or_quote: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/ — \"WALLIX states that the reporting researchers intend to publish the complete write-up of the CVSS 4.0 base 10.0 flaw ... in September\""
  summary: "Same fetch as the preceding finding: CERT-FR carries the fixed versions 12.3.7 / 12.4.1 but neither the CVSS score nor any September statement. The sentence itself says 'WALLIX states', so cite the WALLIX bulletin."
- code: F3
  category: claim-not-supported
  section: weekly-multi-day
  item: "weekly-w32-cve-record-unreliable-in-both-directions"
  url_or_quote: "https://www.metabase.com/blog/security-update — \"exploited since 3 August, with two customers confirming data theft\""
  summary: "Fetched the Metabase post raw: the 0-day quote is verbatim, but the post gives no exploitation date and no customer count. Those come from BleepingComputer (Framework and Tally, 2026-08-03), which the operational entry 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally cites. Add that citation."
- code: F3
  category: claim-not-supported
  section: weekly-vuln-rollup
  item: "weekly-w32-vuln-status-rollup"
  url_or_quote: "https://www.coinspect.com/blog/ill-bloom-investigation/ — \"a weak pseudo-random generator in crypto-js below 4.0.0 ... the identifier CVE-2026-71851\""
  summary: "Fetched Coinspect raw: the quoted exploitation sentence is present, but the page contains zero occurrences of '4.0.0', 'crypto-js' (it writes CryptoJS) or any CVE id. Confirmed the facts against NVD (CVE-2026-71851, published 2026-08-07, CVSS 9.0, 'prior to 4.0.0'). GHSA-rg76-677x-56q9 is already in this entry's sources[] - attach that citation to the clause."
- code: F3
  category: claim-not-supported
  section: weekly-vuln-rollup
  item: "weekly-w32-vuln-status-rollup"
  url_or_quote: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2 — sources[] date \"2026-08-03\"; body \"the compromise check was revised three times to 2026-08-03\""
  summary: "The advisory's own metadata reads First Published 4 March 2026, Last Updated 5 August 2026, Version 2.4 - neither matches the cited 2026-08-03, so the citation date drifts more than two days from any date the page states, and the revision claim is stale for a roll-up dated at the close of W32."
- code: F3
  category: claim-not-supported
  section: weekly-research
  item: "weekly-w32-passkeys-attacked-from-four-directions"
  url_or_quote: "https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html — \"Microsoft did not assign a CVE or ship a fix, characterising the behaviour as a consequence of how Windows Hello for Business works\""
  summary: "Fetched THN raw. Its sentence is 'Mollema describes the behavior as a consequence of how Windows Hello for Business works and says it was left as-is', and it adds 'The Hacker News has contacted Microsoft and Mollema; replies are pending'. The framing originates in Mollema's own post (verbatim in work/.../text.mollema.txt). The entry moves a researcher's characterisation onto the vendor and turns an absent CVE into a vendor decision ('declined'). Also propagates into summary and sourcing_note."
- code: F3
  category: claim-not-supported
  section: weekly-policy
  item: "weekly-w32-nis2-enforcement-phase-netherlands-germany"
  url_or_quote: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/260601_NIS2_BSI-Portal.html — sources[] date \"2026-06-01\"; body \"BSI's own June press release\""
  summary: "Fetched raw: the page's own dateline field reads 'Datum 06.01.2026' = 6 January 2026 in German DD.MM.YYYY convention (the URL slug 260601 appears to have driven the 1 June reading). The entry's own argument corroborates January - a portal opened 1 June cannot yield 11,388 registrations as of 5 March. Everything else in the German block verified clean, including the 11,388 quote against Drucksache 21/4657."
- code: F3
  category: claim-not-supported
  section: weekly-long-running
  item: "weekly-w32-water-plc-lockout-status"
  url_or_quote: "https://therecord.media/iran-cyberattacks-water-treatment — \"previously documented IRGC-linked activity against industrial controllers, and reporting refers to an Iran connection under investigation\""
  summary: "Fetched the article: it says 'a campaign allegedly linked to Iranian hackers' and 'federal agencies have declined to publicly attribute the attacks, multiple sources pointed the finger at Iran'. 'IRGC' does not appear and nothing frames it as under investigation. Use the source's own register or cite something that names the IRGC."
- code: F4
  category: hallucinated-fact
  section: weekly-vuln-rollup
  item: "weekly-w32-vuln-status-rollup"
  url_or_quote: "headline \"four new KEV listings\"; title \"four of them newly catalogued this week\""
  summary: "The entry's own body and status table list five in-window KEV additions, which I verified against all three CISA alerts via tools/fetch_source.py cisa page: 08/04 = CVE-2026-9198, -18556, -34486; 08/05 = CVE-2026-63077; 08/07 = CVE-2026-8037. Change four to five in both frontmatter fields."
- code: F4
  category: hallucinated-fact
  section: weekly-policy
  item: "weekly-w32-assurance-moves-into-procurement-language"
  url_or_quote: "title \"Two publications a day apart moved security assurance out of guidance...\""
  summary: "Both publications are dated 29 July 2026 - confirmed at source (NCSC UK page field 'Publish date 29 July 2026'; CISA PDF cover 'Publication: July 29, 2026') and stated as 'The same day' in the entry's own summary and body. Fix the title."
- code: F4
  category: hallucinated-fact
  section: weekly-research
  item: "weekly-w32-passkeys-attacked-from-four-directions"
  url_or_quote: "cves[0].affected: \"Windows Event Logging Service, per the CVE record — passkey data exposed to an authorized attacker over a network\""
  summary: "Pulled CVE-2026-34348 from the NVD API: published 2026-07-14, CVSS 3.1 base 6.5 (both matching the entry), description 'Protection mechanism failure in Windows Event Logging Service allows an authorized attacker to disclose information over a network.' The record says 'information', not 'passkey data'. Drop the 'per the CVE record' attribution or reword."
- code: F5
  category: missing-citation
  section: weekly-research
  item: "weekly-w32-passkeys-attacked-from-four-directions"
  url_or_quote: "\"Michael Grafnetter's \\\"Pass-the-Passkey\\\" work covered a related class whose event-log passkey-data-exposure element carries CVE-2026-34348 and was closed by Microsoft on 14 July 2026\""
  summary: "I fetched all four sources[] records in this iteration; none names Grafnetter or CVE-2026-34348 (grep of the THN body: Grafnetter False, 34348 False). The claim appears factually correct on independent search but the entry cites nothing for it, and this is the sentence doing the safety work of keeping the two Black Hat talks apart. Add a source."
- code: F5
  category: missing-citation
  section: weekly-vuln-rollup
  item: "weekly-w32-vuln-status-rollup"
  url_or_quote: "\"The Metabase SQL-injection zero-day, exploited since 3 August with two customers confirming data theft, has no CVE identifier at all.\""
  summary: "No inline citation on the sentence; the paragraph's preceding citation is Coinspect, which is about crypto-js. Same source gap as the cve-record entry's Metabase clause, but needs its own fix."
- code: F18
  category: action-item-discipline
  section: weekly-top-stories
  item: "weekly-w32-the-vendor-fix-was-not-the-end-state"
  url_or_quote: "\"Re-verify N-able N-central is on build 2026.3.1.10 (Hotfix 2) — 2026.3.1.7 is superseded — and treat every endpoint the console manages as in scope for a compromise assessment...\""
  summary: "entries/2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1.md, published the same day and rendering into the same Action Items list, already carries both halves of this as two separate actions. The weekly action is a merge with no delta; actions: [] is correct here. The other three weekly actions are not duplicates and should stay."
- code: F11
  category: editorial-advisory
  section: weekly-top-stories
  item: "weekly-w32-european-government-own-infrastructure-breached"
  url_or_quote: "summary \"In three of the five the path ran through infrastructure that does not appear in an internet-facing asset inventory: a mobile carrier's private APN, a controller answering on factory credentials on its WAN side, and an Oracle WebLogic server\"; headline \"Five European public bodies\""
  summary: "The three listed artefacts map to two incidents (Poland twice, Hungary once), while the body's own takeaway names the three as the Polish, Hungarian and Belgian cases. Separately the headline's 'five European public bodies' sits against six named organisations, one of which is a power plant; the body's 'five European jurisdictions' is accurate. Advisory - no external fact is wrong."
- code: F11
  category: editorial-advisory
  section: weekly-long-running
  item: "weekly-w32-open-source-supply-chain-status"
  url_or_quote: "\"a malicious preinstall hook ( setup.mjs ) that downloads a standalone Bun runtime\""
  summary: "The Socket page reads '(setup.mjs)' without the inner spaces (verified against work/.../text.socket.txt line 325). Whitespace inserted inside a quotation. Everything else on this entry is verbatim, and none of the three dropped Socket figures survived into the text."
```
