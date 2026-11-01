# Fix plan — 2026-11-01T1312Z-audit (Phase 4 working list)

Status key: [ ] open · [x] done · [-] declined (reason)

## Records on entries (one record per entry this fire)

| Entry | Type | Basis | Status |
|---|---|---|---|
| 2026-10-30/vapor-panda-artex-agentic-campaign-foreign-ministries | improvement, internal | TC F5 x2: Exposure/takeaway uncited -> CrowdStrike citations | [x] |
| 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day | improvement, internal | TE F3: Rapid7 clause cited to BeyondTrust | [x] |
| 2026-10-29/veeam-cve-2026-108142-cdp-coordinator-authorization-bypass | correction, internal | TE F3: "Veeam reports no exploitation" is a relay | [x] |
| 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev | improvement | TE F3 x2 (pre-pass lead; GHSA binding), F8 Volexity host artefacts dropped by 10-31 rewrite, CERT-FR translation marker | [x] |
| 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates | correction | TC F3 Python versions (10-25 section), F5 orphan sentence, Oracle quote edited by publisher (pre-pass lead) | [x] |
| 2026-10-30/privatim-cloud-merkblatt-v3-02-own-keys-saas-residual-risk | correction, internal | TF F3 "standard SaaS" not in the PDF | [x] |
| 2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev | correction, internal | TD F3 "among other devices" | [x] |
| 2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi | correction | TC F4 supersession (10-26 sentence), F3 NCSC status, Ubuntu date, Prisma Transporter; G3 Datadog/Zscaler detection | [x] |
| 2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix | correction | TC F4 CVE-2026-114148 fixed versions; F5 crash clause | [x] |
| 2026-10-30/wordpress-core-7-1-4-unauthenticated-upgrade-window-rce-race | correction | TF F4 CVE-2026-119977 assigned 2026-10-31 | [x] |
| 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root | update | TF: CIQ patched kernels 2026-10-31; stable backports in CNA record | [x] |
| 2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10 | improvement | TF F8 Web Admin console restriction (CVE-2026-90867) | [-] declined (see report) |
| 2026-10-28/cve-2026-48356-adobe-commerce-magento-upload-flaw-cisa-kev | improvement | TE F8 Adobe Commerce Events <=1.20.0 | [-] declined (see report) |
| 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x | correction | TD F4 10-29 section superseded (PAN-OS named), Exposure, cites | [x] |
| 2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave | correction | TD factual error: para 3 superseded, lower bound as start date, CNA score, type, priority | [x] |
| 2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape | correction | TD: Broadcom .1/.2 revisions, Infosecurity wording, KEV ransomware flag, vectors | [x] |
| 2026-10-13/cve-2026-97229-gitlab-ci-regex-compiler-unauthenticated-rce | improvement | TD F8 CVE-2026-110264 scope from 7.0 + backports; Ruby-wide exposure | [x] |
| 2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft | update | G3: GitGuardian 2026-10-27 escalation | [x] |
| 2026-09-11/canton-bern-icsg-cybersecurity-law-2026-11-01 | update | G2: in force 2026-11-01, KAIO page 2026-10-30 | [x] |

## Pending returns
none (all nine returned).

## Fetch list (after all sub-agents return; guard #9)
- Wordfence intel record 4b4da0cf (CVE-2026-119977 CVSS/CWE/affected)
- CIQ KB cve-2026-98432-mitigation; Linux stable fixed list
- GitGuardian 2026-10-27 GhostAction post
- KAIO Bern ICSG page
- Datadog + Zscaler Node2Shell posts
- Adobe APSB bulletin for CVE-2026-48356 (Commerce Events row)
- Broadcom VMSA-2026-0006 change log
- GitLab 19.5.1 notes; Ruby 2026-10-23 advisory
- Palo Alto CVE-2026-111497 (Transporter client)
- dotnet/announcements #495 (or .NET blog) for CVE-2026-114148 fixed versions
- source repairs: ico-uk, sans-isc, ssd-disclosure, connectwise-trust-center
- out-of-scope pre-pass leads: Danfoss AFP quote, LiteLLM docs quotes (2)

## Added after TA / G1 returns
| 2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider | correction/update | TA factual error: Belden PSIRT-10 v1.1 names NRSW 5.0.0.105; Schneider v3.x Foxboro H90; Wibu 5.2.3 | [x] |
| 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 | update | TA: Siemens SSA-566512 V1.1 upgrade path; THN retraction note; G1 Morphisec IIS/PHP-CGI chain | [x] |
| 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release | correction, internal | TA F3: summary dates exploitation statement to 2026-10-21 advisory | [x] |
| 2026-10-14/cve-2026-96951-windows-shell-motw-bypass-zero-day-kev | update | G1: MSRC rev 2 (2026-10-26) adds Edge 154.0.4258.62 | [x] |
| Adobe Campaign Classic APSB26-162 (2026-10-27) | decide | G1: 8 critical incl. 9.8 pre-auth SQLi, fixed 9403; 2026-10-02 entry says 9402 fixed | [x] update on 2026-10-02 entry |
