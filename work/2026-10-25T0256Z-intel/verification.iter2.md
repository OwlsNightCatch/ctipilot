**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-25T04:13:23Z · ended_at=2026-10-25T04:29:42Z · duration_seconds=979

## Verification report — 2026-10-25T0256Z-intel (iteration 2)

Scope (post-fix pass): all 20 claims in `claims.changed.iter2.yaml`; every other claim of the remediated entries (eMudhra 44, NTLM 18, Danfoss 48, ZDI 17); a seeded random quarter of the 103 remaining PHP and Publica claims (26 drawn, seed 20261025); the run record's notes, checked by hand (6 synthetic `run:` rows). 159 rows in `verification.iter2.claims.yaml` (156 ok, 2 F3, 1 F4). Pages were fetched live this pass (extract, raw url, pdf, `ncsc-csh post`, `cisa-kev` bridge); the gate's cached bodies were used for older Danfoss, PHP and Publica sources and cross-checked on load-bearing facts. Sources with no cached body (Dixell PDF, BLVK PDF, IPCT letter, NCSC posts, php.net archive) were read live.

### Prior-iteration deltas (all 11 walked)
1. NTLM F4: confirmed fixed. Title, summary and sourcing note now say SpecterOps "never received a response to that MSRC report" and Blackfield "could not find a CVE for this specific change" (SMB only). Nothing in the entry claims a CVE position for the LDAP fix.
2. eMudhra evidence[5]: confirmed gone. The nine remaining evidence records each match a `sources[]` URL and each quote is a verbatim substring of the live page (Google, tracker x2, Go, Oracle x2, openjdk.org/emudhra, PSF, The Hacker News).
3. eMudhra body intro: supported. openjdk.org/emudhra (2026-10-24): standalone section tells the reader to back up "your runtime's keystore ... `$JDK_HOME/lib/security/cacerts`"; OS-package section says such runtimes "most likely use the operating system's certificates".
4. eMudhra Exposure: matches the live tracker (Python 3.15.1, 3.14.9, 3.13.17; pip 26.2.2; certifi 2026.10.19; Composer ca-bundle 1.4.16/1.6.0; Erlang certifi 2.18.0; Node.js, Bun, FreeBSD fixed; Bottlerocket, Godot, LibreOffice pending). One omission: the RHEL row also reads "Pending for RHEL 7" (finding F8 #5).
5. Danfoss: both fixes confirmed. BleepingComputer: "While no information is available on how the Danfoss refrigeration controllers were compromised"; Le Monde Informatique: "L'Anssi peut alerter et conseiller, mais elle ne dispose d'aucun moyen d'imposer ... des règles de raccordement"; Public Sénat carries the health-sector check ("travail rapide et intense avec l'ensemble des acteurs de la santé"). Public Sénat and LMI dates and counts (night of 12-13 vs 11-12 October; over 700 vs at least 300) are stated correctly.
6. Run record: "twelve changelog records, eleven with a dated section" holds (12 `updates[]` records, 11 `##` sections, the 2026-10-18T1307Z-audit correction is internal).
7. Cisco: matches advisory v1.1 (2026-10-24): FMC TLS policy, Duo Access Gateway 3.2.0, Duo Network Gateway 3.4.1, Duo Agentic Authorization Connector 1.0.1, ThousandEyes Application-hosting Agent 5.2.2 (Oct 23, 2026), Meraki MV Smart Camera Firmware (Nov 18, 2026), IOS XR 26.4.1 (Nov 30, 2026), Ultra Cloud Core SMI 2026.04.1 (Nov 2026); "Cisco PSIRT is not aware of any malicious use".
8. Python: PSF announcement names no release; ENISA EUVD-2026-109299 gives 9.4 (CVSS 4.0) and CPython `0 <3.16.0`; Discourse (Christian Heimes, 2026-10-20): "users must update pip to >= 26.2.2 ... any pip < 26.2.2 will keep trusting the compromised intermediate CAs regardless of the system trust store"; blog.python.org: the three releases bundle pip 26.2.2. His Discourse user title is "CPython core developer" in the page JSON. Status `mitigation-only` and the action text are consistent.
9. eMudhra exit and ACME: eMudhra press release (2026-10-22) and The Hacker News support the exit, G1 roots, ~30,800 certificates, 99.9 percent InCommon and the ACME renewal-window point; attribution nit in finding #2.
10. NTLM KB pairing: KB5126646 page is "October 13, 2026 ... cumulative update for Windows Server 2025"; KB5122882 page is "September 8, 2026 ... cumulative update for Windows Server 2022"; the stated pairing and "each release needs its own cumulative update of the month" are correct against SpecterOps ("vulnerable until the October 2026 cumulative update").
11. F18: ZDI `actions: []` confirmed; eMudhra actions[0] is shorter but still bundles two tasks (finding #7).

Walked and found sound: NTLM entry end to end against SpecterOps, Blackfield and both KB pages (dates, report 2026-10-06, no response, fix 2026-10-13, September SMB patch, 389/TCP condition, attribute names, "workstations too" remains only an Exposure wording nuance); ZDI entry against Sysdig, TuxCare, The Hacker News and Phoronix (counts, distributions, CVE-2026-90049 caveat, ksmbd prerequisites, detection sequence, mitigation scope, RHEL ksmbd default); Danfoss update against Public Sénat, LMI, Forescout (12,976 / 6,017 / 99 / 7,075 / 4,697 / 80 percent, over 20 hacktivist claims, port-forwarding documentation) and CERT-FR live (last version 16 October 2026); Publica EDÖB update against the EDÖB release and Der Bund (22 and 14 October dates, "several important occupational pension institutions", the fund list); PHP Tenable (SC-202610.2, PHP 8.2.35), Siemens (PAN-OS 10.2 to 12.2, "Contact customer support") and ReliaQuest log sequence; CISA KEV catalogue 2026.10.23 live (neither PHP CVE listed, newest dateAdded 2026-10-23); NCSC.ch posts 13054 and 13091 (Actively Exploited; UNKNOWN). Changelog contract (4c): all four updated entries carry exactly one `update` record with this run id, `updated_at` equals the record `at`, a matching `## Update` section, and every changed line in `git diff HEAD` is covered by the record's `fields`. No em dash, IOC or workflow vocabulary in reader-facing text of the six entries.

### Unsupported / hallucinated facts
- **#1 (F4)** run record, notes paragraph "Published (2 new)": "Both carry one `actions[]` task each". `entries/2026-10-25/zdi-linux-kernel-reports-public-skb-zerocopy-root-exploit.md` now has `actions: []` (emptied for iteration 1's F18 and recorded as such in the run record's own verification block). Only the NTLM entry carries one action. Fix the sentence.

### Citation does not support the claim
- **#2 (F3, low confidence)** eMudhra, Update 2026-10-25 last paragraph: "The Hacker News counts about 30,800 unexpired certificates ... 99.9 percent of them issued through InCommon". THN: "About 30,800 unexpired certificates chained to that root as of October 21, by Chrome's count of public Certificate Transparency (CT) logs. Of those, 99.9% were issued through InCommon". The count is Chrome's and carries an as-of date the entry drops.
- **#3 (F3, low confidence)** eMudhra, Update 2026-10-25 para 1 (also summary, `cves[CVE-2026-91403].fixed`, Update 2026-10-23, record summary): "among them the builds that the incident tracker had listed as the fixed ones". The sentence is cited to Oracle and OpenJDK, which do not mention the tracker, and the live tracker's Java row no longer lists builds (`| Java | [OpenJDK] | [Oracle JDK] |`). The 2026-10-23 fire's verifier saw the list, so it was true then; it cannot be confirmed now. Add the as-of or removal note, or restate from Oracle's affected list alone.

### Surface contradiction
- **#4 (F9, low confidence)** Danfoss: AFP's PM-aide ("a vulnerability in software supplied by a Danish company") and Copeland's "existence de la vulnérabilité ... XWEB EVO" sit beside ANSSI's director general ("des défauts de sécurisation élémentaire") with no `Contradiction:` line while the headline adopts the DG's reading. Not strictly incompatible; one sentence would settle it.

### Needs more research
- **#5 (F8, low confidence)** eMudhra Exposure: "lists Bottlerocket, Godot and LibreOffice as still pending"; the tracker's RHEL row also reads "Pending for RHEL 7". Add it.
- **#6 (F8, low confidence)** ZDI: TuxCare (cited) says "KernelCare's rebootless patch for EL10 shipped on October 23, with EL9 and EL8 next" (AlmaLinux, CloudLinux, RHEL, Oracle Linux, Rocky Linux 10). The entry says "patch the day the distribution ships the fix", tags `no-patch`, and the sourcing note says "TuxCare lists no CVE and no vendor advisory yet". One clause, and check the tag.

### Action-item discipline
- **#7 (F18, low confidence)** eMudhra actions[0] (about 125 words): client trust-store updates and certificate replacement before 2026-10-27 are two tasks with different owners and deadlines in one action, and the rebuild-and-verify tail repeats the Defender takeaway. Split.

### Editorial / less-is-more flags (advisory)
- **#8 (F11)** ZDI body: "bypassed)([Sysdig" missing space (raised in iteration 1, still present).
- **#9 (F11)** eMudhra Update 2026-10-23 now narrates the 2026-10-24 Oracle alert; the 2026-10-25 section already carries it.
- **#10 (F11)** NTLM sourcing_note: three sentences, "each in its own lab" is in neither source, "Neither reports use in attacks" is a finding, not provenance.
- Not flagged: eMudhra summary's "removes four root CAs" rests on the four aliases on openjdk.org/emudhra and on ops.java ("Remove the four relevant root certificates", linked from Oracle's alert, not cited); true, and acceptable.

### Missed angles
None found. Coverage looks complete for critical/high signal. Checked: KEV (no addition in window), NCSC.ch Security Hub 13092 (Fortinet hardening release, covered by `fortinet-hardening-release-fortios-fortimanager-fortimail`) and 13101 (HPE Aruba AOS, covered by `hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth`), and two open-web sweeps for 2026-10-24/25 exploitation and Swiss municipal or cantonal incidents (nothing in window).

### Verdict
NEEDS_FIXES (truth: 3, editorial: 4, advisory: 3)

Priority for remediation: #1 (definitive, run-record text); #3 and #2 (low confidence but cheap); #5 to #7 and #4 optional.

### Findings summary (machine-readable)
See `work/2026-10-25T0256Z-intel/verification.iter2.findings.yaml`.
