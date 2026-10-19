**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T17:35:17Z · ended_at=2026-10-19T18:01:38Z · duration_seconds=1581

## Verification report — 2026-10-11T1307Z-audit (iteration 6, slice s1)

Scope: 27 entries (26 existing, 1 new: NeedyMantis), every entry read whole including every dated section, and all 245 ledger claims answered (241 ok, 2 F3, 2 F4; claims.iter6.s1.yaml fully covered, the 6 claims changed since iteration 5 included). Every cited page was fetched this pass: cached gate bodies reused for 49 URLs, the other 67 fetched with `extract`, `pdf`, `ncsc-csh post`, `cisa-kev`, raw `url` (FortiGuard PSIRT CVSS/known-exploited tables, SolarWinds vectors, ACSC and Onapsis dates, NVD API for CVE-2026-48611, CVE-2019-0708, CVE-2020-0688), `msrc cve`, and WebFetch for the cisa.gov FortiBleed alert. Unreadable on every rung: the phpBB community announcement (403 direct, jina block, WebFetch 403); it sits in sources[] of the phpBB entry and no claim cites it inline. The Register Cisco article extracts only navigation; the entry cites it only in sources[]. CVSS 4.0 scores for the two Unbound CVEs were recomputed from NLnet Labs' published vectors (9.1 and 8.4, both match).

### Delta walk (iteration-5 findings, 10 items)

- Unbound F4: holds. The main analysis now reads "in analyst judgement that is a normal condition for any DNSSEC-validating resolver ...".
- SAP August F8: holds. The five cves[] records name the affected releases exactly as SAP's patch-day page lists them (XMII 15.4/15.5 + MII_ADMIN, KRNL64/KERNEL list, SAP_BASIS 750-758/816/918/920, COM_CLOUD and DHUB_CLOUD 2211).
- G7 F11 (store-label clause): holds. The non-internal record summary no longer contains it.
- SES F3 (Message-ID hedge): holds. Detection keeps Kaspersky's "almost always". One smaller residual on the PDF wording is finding #1 below.
- SAP sector F11, SonicWall F11, Virtualizor F7/F11, Pentagon F11, Copy Fail F16 (all declined): checked each rationale. Accepted: Copy Fail (a patched, KEV-listed LPE from April; Dirty Frag's sibling status rests on a reopened primitive), Pentagon and Virtualizor length (the audit report documents both as left for the fires and Virtualizor was already lowered to routine; published entries cannot be removed, only folded). Not fully accepted, re-raised as advisory: SAP/other sectors beyond public-sector (#7), SonicWall tautology (#8), Virtualizor priority narration plus estate remark (#6).

### Citation does not support the claim
- #1 F3 (low confidence) Amazon SES body para 2 and Detection: "PDF attachments holding only payment details" / "payment-only PDFs". Securelist: "only payment details and supporting documentation".

### Unsupported / hallucinated facts
- #2 F4 (low confidence) Amazon SES Correction: "Attackers use leaked IAM access keys, not separate SES API credentials." Securelist: "In most cases ... leaked IAM access keys"; nothing on separate SES API credentials.
- #3 F4 (low confidence) NeedyMantis Detection: "an HTTPS request with an oversized cookie". Microsoft: Base64-encoded compressed JSON in the Set-Cookie value; no size statement.

### Needs more research
- #4 F8 (low confidence) Copy Fail Detection omits Xint's "Standard file integrity tools comparing on-disk checksums will miss it, because the on-disk file is unchanged."

### Editorial / less-is-more flags (advisory)
- #5 F11 em dashes in nginx, WinRAR, SAP August/September, CHOSEN BRICK, FortiSandbox, FortiBleed, OpenAI/Medicare (the audit calls them render-stripped style).
- #6 F11 priority-change narration in the G7 and Virtualizor sections, and the unsourced estate remark in the latter.
- #7 F11 (low confidence) sector tags no cited page supports (SAP finance; FortiSandbox technology, defense, healthcare; SonicWall finance, energy, healthcare, telco; Check Point finance, telco).
- #8 F11 SonicWall summary "no fix exists short of upgrading".
- #9 F11 (low confidence) file-name / marker-string indicators: `FortiEndpoint_Patch.exe` (FortiClient), `CHATGPTTEST1` and `OAI_META_1312` (UNCTAD).
- #10 F11 (low confidence) FortiBleed 10-08 section: unhedged, uncited FortiGate audit-log sentence.
- #11 F11 (low confidence) ACSC alert page now dated 25 Sep 2026 against the cited 2026-09-24 (secondary outlets say 24 Sep).

### Checks that came back clean
Internal records (phpBB cves/summary scores, voicemail relabel, OpenAI/Medicare ACSC URL move plus one added The Record citation): each frontmatter change is source-supported and carries no new reader-facing information; phpBB 9.8/8.0 are NVD's HackerOne-CNA secondary scores and heise's figures. Record summaries match their sections on all 26 existing entries. KEV dates (CVE-2026-31431, -35616, -50751, -25089, -39808, -20262, -83548/83549, CVE-2025-8088, CVE-2020-0688, CVE-2019-0708) match the live catalog; CVE-2026-58231, -81642/82717, -28324/28325 and phpBB CVEs are correctly not KEV-listed. CVSS per authority matches (Fortinet PSIRT 9.8/9.1 temporal, SAP, Cisco 6.5, SolarWinds vectors AV:N and AV:A, Check Point 9.3/7.4, SonicWall 10.0/7.8, Unbound vectors). Evidence quotes are verbatim or faithful translations with matching original (NCSC-NL Dutch quote). Classification blocks present and in vocabulary on all 27; org_triage null and watchlist false everywhere; single-source entries carry the verification flag and a plain sourcing_note. Priorities: considered and left Check Point critical (disclosure-time call, no change this fire), Copy Fail notable, Unbound high. New NeedyMantis entry: registry keys present with typed relations, references link the DAEMON Tools entry, ATT&CK ids active (T1574.001 is the live DLL technique, T1574.002 is revoked). Missed angles: none evidenced for this slice.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 1, advisory: 7)

All four non-advisory findings are low confidence and one-clause edits. The advisory items may be left.
