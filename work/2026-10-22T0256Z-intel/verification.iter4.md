**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T05:26:32Z · ended_at=2026-10-22T05:43:40Z · duration_seconds=1028

## Verification report — 2026-10-22T0256Z-intel (iteration 4)

Scope walked: all 16 claims of `claims.changed.iter4.yaml`, every other claim of the seven remediated entries (k0t, Cisco, PHP, ARTEX, PAN-OS, GitLab, Publica) and a random quarter (20 of 78) of the remaining ConnectWise, OVHcloud and LiteLLM claims, plus one extra LiteLLM claim found while reading: 196 rows in `verification.iter4.claims.yaml` (190 ok, 2 F3, 4 unreadable). Unreadable: the ConnectWise Trust Center advisory (403 on extract, url, jina and WebFetch; two claims) and the BLVK notice PDF (connection reset / maintenance page; two claims). Pages read this iteration: the saved run bodies plus live fetches of the Publica sources (admin.ch, PK Softech, watson, Publica, BPK PDF, Pensionskasse Post x2, PKZH, NZZ, Cybercrimepolice, Inside IT, Tages-Anzeiger), the Palo Alto advisory, the Palo Alto CVE-2026-0257 advisory, FG-IR-25-910, FG-IR-19-007, the KEV catalogue, CrowdStrike and Recorded Future date metadata.

### Prior-iteration deltas (all eleven checked against the pages)

- k0t CVE-2019-6693 `fixed`: FG-IR-19-007 says "In versions 5.6.11 and above, 6.0.7 and above, and 6.2.1 and above, administrators can choose to be prompted for a password ... set private-data-encryption enable /* disabled by default */"; affected list "6.2.0, 6.0.0 to 6.0.6, 5.6.10 and below". Correct. (Two qualifiers on the same page are not reflected: see F9 and the F8 below.)
- k0t CVE-2025-64446 and CVE-2026-0257 records: affected/fixed match FG-IR-25-910 (8.0.0-8.0.1 to 8.0.2, 7.6.0-7.6.4 to 7.6.5, 7.4.0-7.4.9 to 7.4.10, 7.2.0-7.2.11 to 7.2.12, 7.0.0-7.0.11 to 7.0.12, 6.4 not affected, workaround, post-upgrade review) and the Palo Alto page (CVSS-B 7.8, per-branch fixed builds, Prisma Access 11.2.7-h13 and 10.2.10-h36). cvss null for CVE-2025-64446 is right (no score on the Fortinet page). KEV: all three listed, ransomware use Known for CVE-2026-0257 and CVE-2019-6693, Unknown for CVE-2025-64446. Correct.
- k0t techniques: all ten added ids (T1110.003, T1550.002, T1059.001, T1018, T1046, T1135, T1069.002, T1083, T1518.001, T1078.003) are in Group-IB's table and active in the ATT&CK pin (v20.0); every id of every entry checked active, none revoked or deprecated.
- Cisco "persistent cookies": summary now matches "This vulnerability is due to the use of persistent cookies". Correct.
- Cisco takeaway citations: the Unified CM and Snort 3 advisories are now on the clause; 15SU5, the FTD builds and "not known to be actively exploited" are on those pages. Correct.
- Cisco wording: "two further hardening releases whose worst classes are exploitable over the network without authentication" holds (voice Base 9.8 AV:N/PR:N, Snort 3 Base 9.0 AV:N/AC:H/PR:N); summary no longer says "three". "Cisco IOS XE Software" is an alias of `product:cisco-ios-xe`; `sync_products --check` ok.
- PHP CVSS citation: the 2026-10-20-1 item carries "both rated CVSS v4.0 9.2" and is now on the first clause. Correct.
- ARTEX: "another actor" fits (CrowdStrike and Recorded Future describe one South Korean campaign, TAG-217); parentheses balanced in every body; `okta-workforce-identity` has 0 occurrences in the registry, single `product:okta` key.
- PAN-OS and GitLab wording: the phrases "Palo Alto does not say which logs record request bodies" and "GitLab and its detection pages report no public proof of concept" read as honest absence statements (the pages mention neither); no defect.
- Publica relay attribution: NOT fully fixed, see F3 #1.

### Citation does not support the claim

- **F3 #1 (low confidence)** `publica-pk-softech-supplier-malware-intrusion-data-outflow` summary: "Tamedia reports that Akira holds about 100 GB and demands ransom, as Inside IT relays, and that the authorities now assume ... as Netzwoche relays". Inside IT (fetched, dated 2026-10-20) says "Die Gruppe habe die gestohlenen Daten zurückgehalten und fordere Lösegeld" and "weit über 100'000" persons, with no volume; Tages-Anzeiger carries "Die Hackergruppe Akira stahl rund hundert Gigabyte komprimierte Pensionskassendaten." The iteration-3 finding asked for exactly this split and the new wording still ties "100 GB" to Inside IT. Fix: "Tamedia reports that Akira holds about 100 GB, and Inside IT relays that it demands ransom".
- **F3 #2 (low confidence)** `litellm-1-107-0-pypi-docker-credential-stealer-lookalike` Detection: "an encrypted archive posted to a health-check path on a domain imitating the project's ([Socket])". Socket only records "The archive is POSTed to hxxp://www[.]litellm[.]dev/healthcheck". Wiz: "This domain is attacker controlled, impersonating LiteLLM infrastructure"; Aikido: "this domain is attacker-controlled and is not affiliated with the legitimate LiteLLM project". Fix: add the Wiz or Aikido citation to the clause.

### Needs more research

- **F8 #3** `cve-2026-76466-cisco-expressway-cluster-unauth-root-rce` Exposure, actions[0], Defender takeaway: "A standalone Expressway is outside the advisory's vulnerable-product statement." and "On every Cisco Expressway-C and Expressway-E that runs in a cluster, upgrade to X15.5.20". The cited Expressway hardening advisory (cisco-sa-exwy-hardening-FhcqBVcs) states "These vulnerabilities affect Cisco Expressway-C and Cisco Expressway-E, both virtual and appliance versions, regardless of device configuration" (eight CVEs, worst 8.6 AV:N/PR:N, same fix X15.5.20, X14 and earlier migrate). The body mentions that release only as "also carries Expressway's own hardening fixes", so a standalone Expressway-E on X15.5.3 or earlier reads as unaffected and the action and takeaway cover clustered units only. State that every Expressway on X15.5.3 or earlier still needs X15.5.20.
- **F8 #4** `cve-2026-110264-gitlab-org-mode-renderer-unauth-rce` Detection: the cited GitLab detection (Investigation step) gives the host-level code-execution check "Hunt for code execution: unexpected child processes of Puma, new files owned by `git` in `/tmp`, outbound connections, changed crontabs or SSH keys for the `git` user". The entry gives log signatures and "treat the secrets as at risk" but not the check that answers whether an already-exposed instance was hit. Add it.
- **F8 #5 (low confidence)** `k0t-fortiweb-fortigate-globalprotect-edge-device-campaign` actions[0] and Defender takeaway: FG-IR-19-007 (now cited) adds "Enabling private-data-encryption on FortiGates that are centrally managed by a FortiManager or are in High Availability mode may lead to some bugs including an install errors on the FortiManager side and split-brain. This issue is fixed in FortiManager versions 6.2.7 and above and in FortiGate versions 6.2.6, 6.4.4, 6.6.0 and above." The "every FortiGate" action does not name it.

### Surface contradiction

- **F9 #6 (low confidence)** `k0t-fortiweb-fortigate-globalprotect-edge-device-campaign` summary, actions[0], Exposure: "decrypts its stored LDAP, Active Directory and administrator secrets offline" and "every FortiGate is exposed to the offline decryption step". Group-IB (cited) says "administrator and local-user credentials" are recovered. Fortinet's FG-IR-19-007 (cited on the same Exposure clause) says the hard-coded key "impacts all credential data of type "ENC" in FortiOS CLI configuration except the administrator's password" and "FIPS-CC devices are not impacted as the encryption method is overridden". The entry takes Group-IB's reading silently. Add a Contradiction line or scope the two statements.

### Editorial / less-is-more flags (advisory)

- **F11 #7** `ovhcloud-cli-release-assets-replaced-secret-stealing-build` Detection and Update section: "a working folder named envchecker followed by digits" and "color-picker-universal 2.8.91" are file-name and package indicators under the style rule. Open since iteration 1 and declined each time; defensible as detection content, may be left.

### Checks that came back clean

Change contracts (4c): PHP, ConnectWise, OVHcloud and Publica records carry this run's id, `at` equals `updated_at`, each non-internal record has its `## Update` section with the same `at`, every changed frontmatter line in `git diff HEAD` is named in `fields`, the main analyses do not contradict the new state, and each record is a genuine delta of the same finding. No em dash outside the `## Update` headings, no pipeline vocabulary, no IOCs of the hash/IP/domain kind in any new or updated entry. Gate re-run: 57 pass, 1 warn (empty verification block), 0 fail; `sync_products --check` ok. Dedup: the PAN-OS entry shares CVEs with the PHP entry and declares it in `references[]`; it carries vendor-specific exposure, Threat IDs and CVSS-B that the PHP entry does not, so it stands as a distinct finding. Missed angles: the KEV window holds only the 2026-10-20 additions already dispositioned, the Oracle CPU, Exchange, Citrix, Ivanti and Adobe items are in the store, and two web searches for in-window items returned nothing further; coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 4, advisory: 1)

### Findings summary (machine-readable)

See `work/2026-10-22T0256Z-intel/verification.iter4.findings.yaml` (7 records: F3 x2, F8 x3, F9 x1, F11 x1).
