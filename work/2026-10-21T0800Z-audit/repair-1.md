# repair-1 report, cleanup wave 02 (2026-10-21T0800Z-audit)

Batch: `work/2026-10-21T0800Z-audit/batch-1.yaml`, 10 entries, 10 records written (3 correction, 7 improvement; 4 of them internal). Sources fetched with `tools/fetch_source.py extract` (trafilatura installed in this container with `.claude/hooks/setup-deps.sh`; the first fetches had fallen back to raw HTML) and saved under `repair-1/src/`; every new quote and phrase was checked with `grep -F` against the saved body. EUVD ids were looked up by CVE through the EUVD search API (`repair-1/notes-euvd.txt`); the per-vulnerability pages return HTTP 200. Record files: `repair-1/rec/`.

Gate: `check_run.py --all` shows no FAIL on these entries; the only warning on them is the expected "run_id does not resolve to a run record". The one store FAIL is `cve-sync` on `2026-10-07/ninja-forms-wpc-bundles-stored-xss-hidden-admin-campaign` (CVE-2026-92438), outside this batch. `--page-checks-since 2026-10-21`: no quote-literal or citation-cve line on these entries (`repair-1/page-checks.txt`).

## Per entry

### 2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after
- Record: improvement, `2026-10-21T08:16:23Z`, fields `[techniques, body]`, with section.
- Applied: T1005 replaced by T1213.006 (Databases). BleepingComputer reports Eurail's February disclosure that the attackers took the data "after breaching its customer database"; the main text now says so (one cited sentence). An empty mapping was not an option for an incident, and T1213.006 names what a source states. Ground truth: https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/
- Declined: none. Legacy duty: not required (`legacy_duty: false`).

### 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n
- Record: improvement, internal, `2026-10-21T08:16:39Z`, fields `[headline, summary]`.
- Applied: headline and summary now say "parts of its IT infrastructure" (party statement: "Teile der IT-Infrastruktur wurden vorsorglich vom Netz genommen", translated from German: parts of the IT infrastructure were taken off the network as a precaution). The headline also drops from 127 to 117 characters. The body already said "parts", so the record is internal. W1-F draft re-derived; its wording "parts of its IT offline" was not used. Ground truth: https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/
- Declined: none. Legacy duty: not required.

### 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u
- Record: improvement, `2026-10-21T08:17:40Z`, fields `[tags, sectors, techniques, body]`, with section.
- Applied: `infostealer` tag removed (Sophos: "a relatively simple backdoor" with shell and file commands; the taxonomy has no backdoor or loader tag). Sectors set to [] (no source names a sector). Ground truth: https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor and https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer
- Legacy duties: classification B/2 present. Exposure added (Malwarebytes: misspelled `Cluade` install directory plus the Startup-folder files). Detection moved into its own paragraph, telemetry class first. Triage added (Malwarebytes: the signed parent "may appear benign to endpoint security tools"; the discriminator is WScript.exe writing the three files into Startup and launching the updater with a hidden window). Labelled lines are now in contract order. Mapping extended with behaviors the body describes: T1059.005, T1140, T1620, T1070.004, T1564.003.
- Declined: none. The W1-F draft (tags and sectors only, internal) was folded into this one non-internal record.

### 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x
- Record: correction, `2026-10-21T08:18:40Z`, fields `[title, headline, summary, body]`, with section.
- Applied: the summary and the 2026-09-05 section now attribute the Kubernetes PoC statement to Aikido and to the Dirty Frag family as a whole (CVE-2026-43284, CVE-2026-43500, CVE-2026-46300). Aikido's container-escape link points at Ubuntu's CVE-2026-43284 page. The summary states the Fragnesia PoC overwrites /usr/bin/su in the page cache (Help Net Security, Wiz). Em dashes removed from the title and headline. Ground truth: https://www.aikido.dev/blog/dirty-frag
- Legacy duties: Exposure and Defender takeaway were already present. Main-body Detection added (process and syscall telemetry: unprivileged user and network namespaces, an ESP SA over NETLINK_XFRM, then `su` giving a root shell with no authentication; per Wiz). Triage added (Red Hat RHSB-2026-003: unprivileged user namespaces are routine for rootless containers, sandboxed browsers and Flatpak, and IPsec for VPNs; the combination in one unprivileged process tree is the signal). Classification B/2 and techniques [T1068, T1611] unchanged.
- Declined: evidence[2] is kept unchanged. It is a verbatim Aikido quote and now supports the reattributed sentence. The 2026-09-05 record summary ("now target Kubernetes specifically") is append-only and was not edited.

### 2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s
- Record: improvement, internal, `2026-10-21T08:18:50Z`, fields `[techniques]`.
- Applied: T1556 removed (GTIG describes MFA code relay and attacker MFA device registration, nothing that modifies an authentication process). Added mappings that GTIG states and the body describes: T1684.001 Impersonation (the active successor of revoked T1656), T1583.001 (Tucows-registered domains), T1078.004, T1059.006, T1059.001, T1657 (extortion). Ground truth: https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/
- Legacy duties: classification and all four labelled lines were already present. Declined: none.

### 2026-05-16/node-ipc-npm-package-backdoored-via-expired-domain-account-t
- Record: improvement, `2026-10-21T08:19:25Z` (summary amended), fields `[sources, body]`, with section.
- Applied (optional finding): as of 2026-10-21 the npm registry no longer lists 9.1.6, 9.2.3 or 12.0.1, and `latest` is 14.0.0. This is cited to https://registry.npmjs.org/node-ipc, added to `sources[]` dated 2026-10-21. No removal date is claimed: the document was last modified when 14.0.0 was published on 2026-08-24. The 2026-09-30 sentence about the sources was left as it stands. Exposure was moved ahead of Detection (contract order).
- Declined: the CSO date finding was already fixed by 2026-10-11T1307Z-audit (body citations and `sources[3]` both say 2026-05-15).
- Legacy duties: classification B/1, mapping, Exposure, Detection and Defender takeaway present. No Triage was added: the sources give no benign baseline for the detached-child-Node or DNS TXT signals.

### 2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv
- Record: improvement, internal, `2026-10-21T08:19:40Z`, fields `[summary, techniques]`.
- Applied: the summary now reads "Vanilla Tempest (which in some cases deployed Rhysida)" (Microsoft: "In some observed cases, Vanilla Tempest also deployed Rhysida ransomware"). T1204.002 added for the user-run trojanized Teams installer in Microsoft's case study. Ground truth: https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/
- Legacy duties: classification and all four labelled lines were already present. Declined: none.

### 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
- Record: improvement, internal, `2026-10-21T08:20:08Z`, fields `[cves, sources, techniques]`.
- Applied, CVE records:
  - CVE-2026-48027: "9.3 (CVSS 4.0)" from EUVD-2026-32550; affected Nx Console 18.95.0 and fixed 18.100.0 from GHSA-c9j4-9m59-847w.
  - CVE-2026-45321: "9.6 (CVSS 3.1)" from GHSA-g7cv-rxg3-hmpx, which shows the score and vector; affected "84 versions across 42 @tanstack/* npm packages, published 2026-05-11"; fixed "the patched release per package in GHSA-g7cv-rxg3-hmpx".
  - CVE-2026-8398: "9.3 (CVSS 4.0)" from EUVD-2026-30514; affected 12.5.0.2421 to 12.5.0.2434 (Kaspersky); fixed 12.6 (Disc Soft).
- The CVSS 3.1 9.8 for CVE-2026-8398 that the W1-B finding and the W1-F draft carry was not used: EUVD shows only the 4.0 score, and the 3.1 score is on the CVE record alone, which cannot be cited. Two EUVD pages were added to `sources[]`. The ground-truth URL in the finding (cveawg.mitre.org) is uncitable and was not used.
- Legacy duties: the mapping was extended from 3 to 15 ids, each naming a behavior the body describes and the postmortem, the advisory or Kaspersky states: T1195.001, T1550.001, T1059.006, T1543.001, T1548.003, T1552.004, T1552.005, T1555.005, T1555.006, T1553.002, T1105, T1048. Classification and labelled lines were already present. Declined: none.

### 2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p
- Record: correction, `2026-10-21T08:20:41Z`, fields `[summary, cves, sources, body]`, with section.
- Applied: the IBM page (modified 13 October 2026) now offers IFDT503301, which supersedes IFPH71594 and still includes the PH71265 fix. The summary, `cves[].fixed` and the Defender takeaway now name IFDT503301 and the levels it is published for (9.0.5.27 to 9.0.5.29, 8.5.5.30 and 8.5.5.31), with the prerequisite fix pack applied first. The page's citation date moved from 2026-06-26 to 2026-10-13 in `sources[]` and in both inline citations. The section adds that IBM removes superseded ifixes from Fix Central. Ground truth: https://www.ibm.com/support/pages/ibm-http-server-latest-cumulative-security-interim-fix
- Typed correction, not update: the PH71265 fix content is unchanged and the entry named a fix IBM has withdrawn.
- Legacy duties: classification A/2, techniques [T1190], Exposure and Defender takeaway present. No Detection line: neither IBM's bulletin nor the cumulative page gives detection or version-check guidance, and exploitation status is unknown. Declined: none.

### 2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen
- Record: correction, `2026-10-21T08:21:30Z`, fields `[actions, cves, body]`, with section.
- Applied: "force one re-authentication" was removed from `actions[0]`, the 2026-06-10 section and the 2026-10-06 section. PSIRT says users must re-authenticate once after the upgrade because the firewall regenerates the cookie. `cves[].affected`/`fixed` were filled from the PSIRT table, in the format of the sibling PAN-OS entries. A Triage line was added: Rapid7 says cookie logins are routine where Authentication Override is on; Arctic Wolf saw "Cannot decrypt cookie" followed quickly by a successful cookie login, though not in every intrusion. Ground truth: https://security.paloaltonetworks.com/CVE-2026-0257, plus the Arctic Wolf 2026-06-11 and Rapid7 pages.
- Declined:
  - The 06-17 "SMB lateral movement / European targets" body text was already fixed by 2026-10-11T1307Z-audit. Its 2026-06-17 record summary is append-only.
  - "auth-method=cookie" was already fixed by 2026-10-11T1307Z-audit.
  - `public-sector` stays: Unit 42's update of 2026-10-19/20, already on the entry, lists "Government" among the industries in its investigations.
- Legacy duties: classification A/1, techniques, Exposure, Detection with a compromise check, and Defender takeaway were present; Triage is now added.

## State changes for the main agent

- `state/cves_seen.json`: bump `last_seen` to 2026-10-21 for CVE-2026-48027, CVE-2026-45321, CVE-2026-8398 (Nx records changed), CVE-2026-9170 (fixed changed) and CVE-2026-0257 (affected and fixed added). CVE-2026-46300's record did not change.
- `entities/registry.yaml`: no change needed.

## Residuals noticed (not fixed)

- Headlines over 120 characters: Beagle (127), GTIG UNC6671 (158), node-ipc (155).
- Fox Tempest `sources[].publisher` strings carry two em dashes.
- PAN-OS 2026-06-10 section still gives fixed builds as "12.1.7+, 11.2.12+, 11.1.15+, 10.2.18-h6+", omitting the earlier hotfix builds. The main text and CVE record are complete.
- The Aikido citation now redirects to `/blog/dirty-frag-cve-2026-43284`, whose page metadata dates it 2026-04-07, while the Fragnesia entry dates it 2026-09-04.
- The registry key `tool:beagle-fake-claude-stac4713-2026` embeds the STAC4713 link that the 2026-09-30 correction withdrew (the key is permanent, but its name and aliases may need review).
- The Nx entry's "Hardening:" paragraph (extension allow-list, `--ignore-scripts`, approval for install scripts) is largely uncited.
- The Beagle `sources[]` records have no `date` field (the date sits in the publisher string).
