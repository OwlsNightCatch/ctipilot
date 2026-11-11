# Iteration 3 findings and remediation applied (verify each before the cold pass)

- F3 kernel (2026-10-31/cve-2026-98432-...): the blanket "HWE, cloud and FIPS (and Raspberry Pi) kernels in progress" is replaced by "some HWE, FIPS, NVIDIA and Azure variant kernels" (title, summary, cves[].affected, Defender takeaway, the 2026-11-11 section and the record summary); the Defender takeaway says "20.04 and older and some variant kernels were not out on 2026-11-10".
- F3 kernel cves[].fixed: "Debian trixie security 6.12.115-2" replaced by "6.12.116-1" (Debian tracker).
- F3 Barracuda: the Campus citation label is now 2026-11-02 (the page's own date).
- F3 SAP Exposure: "applies under certain configurations of the SAML 2.0 service provider" (the CNA record's words).
- F8 SAP ProxyGate: the paragraph now opens with Onapsis's statement that ProxyGate lets an unauthenticated attacker with network access run operating system commands as `<sid>adm` on the Gateway, with its dependence on the proxy access list; cves[CVE-2026-89103].type is now rce; the full kernel patch-level list in the main analysis is shortened to two examples (the full list stays in cves[].fixed) to keep the main analysis at 548 words.
- F3 N-able: the "2026-11-08" date is dropped from the Defender takeaway's credential-rotation clause.
- F4 Vates actions[1]: "the dynamic-linker preload file Vates lists".
