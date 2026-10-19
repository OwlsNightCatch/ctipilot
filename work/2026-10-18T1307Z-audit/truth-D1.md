**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:59Z · ended_at=2026-10-18T14:03:57Z · duration_seconds=2158

## Retrospective truth pass D1 (run 2026-10-18T1307Z-audit)

17 entries checked, 336 claims walked (every ledger row has a verdict in truth-D1.claims.yaml). All 17 entries carry at least one factual-error. Group records (survivor, current state, duplicate-only facts) are in truth-D1.yaml under groups:.

### 2026-05-10/cve-2026-26030-cve-2026-25592-microsoft-semantic-kernel-prom
Verdict: factual-error (8 defects)

1. [factual-error] summary
   - Claim: prompt-injection-to-RCE in the AI agent orchestration framework that backs Azure AI Foundry, Copilot Studio and many self-hosted agents
   - Defect: No cited source says Semantic Kernel backs Azure AI Foundry or Copilot Studio.
   - Ground truth: Microsoft blog: "Semantic Kernel is Microsoft's open-source framework for building AI agents and integrating AI models into applications." (no Foundry / Copilot Studio statement anywhere in the post or the GHSAs) (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Drop "that backs Azure AI Foundry, Copilot Studio and many self-hosted agents"; say "Microsoft's open-source AI agent framework".

2. [factual-error] summary / body paragraph 1
   - Claim: `SessionsPythonPlugin.DownloadFileAsync` and `SessionsPythonPlugin.UploadFileAsync` carry a `[KernelFunction]` attribute that should not have been applied
   - Defect: Only DownloadFileAsync was wrongly exposed as a kernel function; UploadFileAsync is intentionally a kernel function (it received path validation, not attribute removal).
   - Ground truth: Blog: "DownloadFileAsync was accidentally marked with a [KernelFunction] attribute". Fix PR #13478 diff removes `[KernelFunction, Description("Downloads a file ...")]` from DownloadFileAsync only; the UploadFileAsync `[KernelFunction, Description("Uploads a file ...")]` line is retained; its unit test asserts "Only ExecuteCode, UploadFile, and ListFiles should be exposed". (https://api.github.com/repos/microsoft/semantic-kernel/pulls/13478/files)
   - Fix: State that the unintended [KernelFunction] was on DownloadFileAsync (host-side file write via localFilePath); upload_file lacked path validation (host-file read into the sandbox).

3. [factual-error] body paragraph 1
   - Claim: An f-string composes the LINQ-like filter expression directly from an LLM-controlled parameter ... bypasses with the well-known `__class__.__bases__[0].__subclasses__()` class-hierarchy traversal pattern ... `os.system`-equivalent execution
   - Defect: Mechanism misdescribed: the filter is a Python lambda string executed via eval(); bypass traversed the type system from tuple() to BuiltinImporter and used load_module/system; no f-string, LINQ, or __bases__[0] chain in the source.
   - Ground truth: Blog: "The default filter function ... is implemented as a Python lambda expression executed using eval()"; "kwargs[param.name] is AI model-controlled and not sanitized"; payload "traversed Python's class hierarchy to locate BuiltinImporter, and used it to dynamically load os and call system()"; blocklist missed __name__, load_module, system, BuiltinImporter. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Rewrite: unsanitised model-controlled parameter interpolated into a lambda filter evaluated with eval(); AST blocklist bypassed via class-hierarchy traversal to BuiltinImporter.

4. [factual-error] body paragraph 2
   - Claim: Microsoft characterises both flaws as systemic of agentic-AI patterns that "trust LLM-controlled parameters without explicit validation"
   - Defect: The quoted phrase is not on the cited page (invented quote); AutoGen is also not named by Microsoft as likely affected.
   - Ground truth: Blog: "The vulnerability lies in how the framework and tools trust the parsed data."; "frameworks like Semantic Kernel, LangChain, and CrewAI ... a single vulnerability in how they map AI model outputs to system tools carries systemic risk." No "without explicit validation" string; AutoGen not mentioned. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Remove the quotation marks or quote the blog sentence verbatim; name only LangChain and CrewAI as the blog does, and label wider spread as analyst inference.

5. [imprecision] cves[] CVE-2026-26030 / CVE-2026-25592 auth
   - Claim: auth: pre-auth; affected: null; fixed: null
   - Defect: CVSS vectors of both GHSAs carry PR:L (low privileges required), so "pre-auth" contradicts the authority; affected/fixed left null although the GHSAs give them.
   - Ground truth: GHSA-xjw9-4gw8-4rqx: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H (9.9), vulnerable "< 1.39.4", first patched 1.39.4; GHSA-2ww3-72rp-wpp4: same vector, nuget "< 1.71.0" first patched 1.71.0, pip "< 1.39.3" first patched 1.39.3. (https://api.github.com/advisories/GHSA-xjw9-4gw8-4rqx)
   - Fix: Set affected/fixed per GHSA; drop or qualify auth: pre-auth (attack needs a prompt-injection channel into the agent, not an unauthenticated network exploit of the SDK).

6. [imprecision] sources[] publisher labels / body citation labels
   - Claim: GitHub Security Advisory GHSA-xjw9-4gw8-4rqx, 2026-05-07 ; GitHub Security Advisory GHSA-2ww3-72rp-wpp4, 2026-05-07
   - Defect: The GHSAs were published 2026-02-19 and 2026-02-06; 2026-05-07 is the Microsoft blog date.
   - Ground truth: API: GHSA-xjw9-4gw8-4rqx published_at 2026-02-19T19:34:14Z (NVD 2026-02-19); GHSA-2ww3-72rp-wpp4 published_at 2026-02-06T18:37:24Z (NVD 2026-02-06). (https://api.github.com/advisories/GHSA-2ww3-72rp-wpp4)
   - Fix: Correct the dates in the sources[] publisher strings and the body link labels; note the CVEs predate the May blog by 2-3 months.

7. [imprecision] summary / body last sentence
   - Claim: Full breakdown in § 5. / Full deep dive in § 5.
   - Defect: Dangling pointer to a section of the migrated brief that does not exist in this entry.
   - Ground truth: Entry body has no section 5; the deep dive is a separate entry. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Remove the "§ 5" references.

8. [imprecision] priority
   - Claim: priority: high
   - Defect: No in-the-wild exploitation, not in CISA KEV (catalog 2026.10.16), exploitation needs a prompt-injection vector plus a specific default-config component; research disclosure, a high-bar disqualifier.
   - Ground truth: Blog frames both as researcher-found, "have since been fixed"; no exploitation statement; neither CVE in KEV. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Context only: priority should be notable/routine unless a constituency product exposure is shown.

### 2026-05-10/microsoft-semantic-kernel-cve-2026-26030-cve-2026-25592-prom
Verdict: factual-error (10 defects)

1. [factual-error] body "Why this matters"
   - Claim: Semantic Kernel is the open-source orchestration SDK behind Azure AI Foundry, Copilot Studio, and a growing fraction of self-hosted enterprise AI agents in EU government modernisation pilots.
   - Defect: Unsupported: no cited source links Semantic Kernel to Foundry/Copilot Studio or to EU government pilots.
   - Ground truth: Blog: "Semantic Kernel is Microsoft's open-source framework for building AI agents ... With over 27,000 stars on GitHub". (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Delete the Foundry/Copilot Studio/EU-pilot claims.

2. [factual-error] body CVE-2026-26030 section
   - Claim: composes its LINQ-like filter expression by f-string interpolation ... The SDK applies a string-blocklist validator ... the validator is a denylist on the *literal text*
   - Defect: Validator is AST-based (parses filter string into an AST, rejects dangerous Name/Attribute nodes, runs eval with empty __builtins__); not a literal-text scan; no f-string/LINQ.
   - Ground truth: Blog: "implemented a validator that parses the filter string into an Abstract Syntax Tree (AST) before execution"; "scans every element in the code for dangerous identifiers and attributes (for example, strings like eval, exec, open, __import__ ...)"; "If the code passes both checks, it is executed in a restricted environment where Python's built-in functions ... are deliberately removed." (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Describe it as an AST identifier/attribute blocklist; bypass worked because __name__, load_module, system, BuiltinImporter were not blocked and ast.Subscript was unchecked.

3. [factual-error] body CVE-2026-26030 section
   - Claim: "".__class__.__bases__[0].__subclasses__()[<index>]("...") — walking `object`'s subclass list to reach an arbitrary class ... (typically `subprocess.Popen` or a `os` reference reached via reflection)
   - Defect: Not the cited payload: it started from tuple(), located BuiltinImporter and called load_module/system; subprocess.Popen is not mentioned.
   - Ground truth: Blog: "it started with tuple() ... and crawled through Python's type system"; "traversed Python's class hierarchy to locate BuiltinImporter, and used it to dynamically load os and call system()". (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Replace the generic idiom and the subprocess.Popen aside with the blog's BuiltinImporter/load_module/system chain, or drop the snippet.

4. [factual-error] body CVE-2026-26030 prerequisites
   - Claim: default for self-hosted Semantic Kernel agents until a customer wires in a different vector backend ; indirect prompt injection via retrieved documents or tool output is sufficient; a direct user-input vector is not required
   - Defect: Source states the condition as "Search Plugin backed by In-Memory Vector Store functionality using the default configuration"; the "default for self-hosted agents" and indirect-vs-direct statements are uncited.
   - Ground truth: Blog: "The targeted agent must have the Search Plugin backed by In-Memory Vector Store functionality using the default configuration"; "The attacker must have a prompt injection vector, allowing influence over the agent's inputs". (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Use the blog wording; drop the unsupported default-for-self-hosted aside.

5. [factual-error] body CVE-2026-25592 section
   - Claim: Two of its methods — `DownloadFileAsync` and `UploadFileAsync` — were mistakenly annotated with `[KernelFunction]`
   - Defect: Only DownloadFileAsync was mistakenly annotated.
   - Ground truth: Blog: "DownloadFileAsync was accidentally marked with a [KernelFunction] attribute"; PR #13478 removes [KernelFunction] from DownloadFileAsync only (UploadFileAsync keeps it, gains path validation). (https://api.github.com/repos/microsoft/semantic-kernel/pulls/13478/files)
   - Fix: Say only DownloadFileAsync was mis-annotated.

6. [factual-error] body CVE-2026-25592 section
   - Claim: (a) call `UploadFileAsync` to write attacker-chosen bytes to an attacker-chosen path *on the host* ... and (b) call `DownloadFileAsync` symmetrically to read host-side files back into the agent context.
   - Defect: Directions are reversed: DownloadFileAsync is the host-side file-write primitive; upload_file is the host-file-read/exfiltration primitive into the sandbox.
   - Ground truth: Blog: DownloadFileAsync's "localFilePath parameter, which dictates exactly where File.WriteAllBytes() saves data on the host device, was now entirely AI controlled"; "upload_file() ... accepted any local file path without validation, allowing prompt injections to exfiltrate sensitive host files ... directly into the sandbox"; chain writes the script to the host Windows Startup folder. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Swap: DownloadFileAsync = arbitrary host file write (Startup-folder code execution on next sign-in); upload_file = arbitrary host file read into the sandbox (Python and .NET).

7. [factual-error] body hardening
   - Claim: implement a Function Invocation Filter (the SDK-supported hook documented in the Microsoft research post) ... reduces the Python-side blast radius even if the validator is bypassed
   - Defect: The Function Invocation Filter workaround is documented in GHSA-2ww3-72rp-wpp4 for the .NET flaw, not in the Microsoft post; no source offers it as a Python-side mitigation. Python GHSA workaround is "Avoid using InMemoryVectorStore for production scenarios". "patched releases also include the upstream test additions" is uncited.
   - Ground truth: GHSA-xjw9: "Workarounds: Avoid using InMemoryVectorStore for production scenarios."; GHSA-2ww3: "Users can create a Function Invocation Filter which checks the arguments being passed to any calls to DownloadFileAsync or UploadFileAsync and ensures the provided localFilePath is allow listed." (https://api.github.com/advisories/GHSA-xjw9-4gw8-4rqx)
   - Fix: Attribute the filter workaround to the .NET GHSA only and add the Python GHSA workaround (avoid InMemoryVectorStore in production); drop the Python-blast-radius and test-additions sentences.

8. [imprecision] cves[] / ATT&CK mapping
   - Claim: T1565.001 Stored Data Manipulation (write primitive)
   - Defect: The documented write primitive drops a script in the Windows Startup folder for code execution at next sign-in; stored-data manipulation for integrity impact is not what the source describes. Also auth: pre-auth contradicts PR:L; affected/fixed null.
   - Ground truth: Blog: "writes it directly to the host's Windows\Start Menu\Programs\Startup folder"; "On the next user sign-in, the script runs, granting full host compromise." GHSA vectors PR:L. (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Map to Startup-folder autostart persistence/execution instead of T1565.001; qualify auth; fill affected/fixed.

9. [imprecision] body (analysis paragraphs)
   - Claim: EDR vendors classify this under hunt-pack categories ...; Many self-hosted agent deployments do not log plugin-method calls ...; The same class of bug is highly likely to exist in LangChain, CrewAI, AutoGen, Haystack, LlamaIndex; Both bypass any of the existing prompt-side mitigations ...; The deployment surface inside an EU public-sector tenant ...
   - Defect: Uncited generalisations stated as fact; the Microsoft post names only LangChain and CrewAI and says prompt-layer guardrail bypass needs host-level detection, not that all prompt-side mitigations are bypassed.
   - Ground truth: Blog: "frameworks like Semantic Kernel, LangChain, and CrewAI"; "If an attacker bypasses the AI model guardrails, traditional endpoint defense must be in place". (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
   - Fix: Mark as analyst inference or remove.

10. [imprecision] sources[] publisher labels / header links
   - Claim: GitHub GHSA ... 2026-05-07
   - Defect: GHSA publication dates are 2026-02-19 and 2026-02-06 (not 2026-05-07).
   - Ground truth: GHSA-xjw9 published_at 2026-02-19T19:34:14Z; GHSA-2ww3 published_at 2026-02-06T18:37:24Z. (https://api.github.com/advisories/GHSA-xjw9-4gw8-4rqx)
   - Fix: Correct dates.

### 2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898
Verdict: factual-error (9 defects)

1. [factual-error] immediate_action; ## Update 2026-06-02 section; updates[0].summary
   - Claim: On 1 June, Belgium's Centre for Cybersecurity (CCB) and multiple outlets reported active in-the-wild exploitation ; Belgium's Centre for Cybersecurity (CCB) confirmed active exploitation on 1 June
   - Defect: The CCB warning is dated 29 May 2026 (a Friday); 1 June is the date BleepingComputer, Help Net Security and SecurityWeek reported it.
   - Ground truth: CCB advisory: "Last Update: 29/05/2026 ... Updated on May 29, 2026 CVE-2026-41089 (Windows Netlogon) is now actively exploited in the wild." BleepingComputer (2026-06-01): CCB "warned on Friday"; CCB tweet id 2060392708259131674 decodes to 2026-05-29T16:07Z. (https://ccb.belgium.be/advisories/warning-microsoft-patch-tuesday-may-2026-patches-118-vulnerabilities-16-critical-102)
   - Fix: Say CCB warned on 29 May 2026 and outlets reported it on 1 June.

2. [factual-error] cves[CVE-2026-41103].type / cves[CVE-2026-42898].auth
   - Claim: CVE-2026-41103 type: rce, vector: zero-click, auth: pre-auth ; CVE-2026-42898 auth: pre-auth, vector: zero-click
   - Defect: MSRC classifies CVE-2026-41103 as Elevation of Privilege (authentication forgery), not RCE; CVE-2026-42898 requires an authorized (low-privilege) attacker (PR:L), the body itself says "authenticated code injection".
   - Ground truth: MSRC CVE-2026-41103: impact "Elevation of Privilege", CWE-303, CVSS 9.1 AV:N/AC:L/PR:N/UI:N/C:H/I:H/A:N. MSRC CVE-2026-42898: "allows an authorized attacker to execute code over a network", CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H (9.9); ZDI: "any authenticated user". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-41103)
   - Fix: Set CVE-2026-41103 type to privilege escalation/auth-bypass and CVE-2026-42898 auth to authenticated (low privilege); fill affected/fixed from MSRC.

3. [factual-error] body, CVE-2026-41089
   - Claim: unauthenticated remote attacker over the network reaches the domain-controller Netlogon RPC endpoint
   - Defect: No cited source says RPC; independent root-cause analyses place the flaw in the CLDAP DC-locator ping handler on UDP/389 of the Netlogon service, and exploitability depends on long DNS domain/host names.
   - Ground truth: Aretiq: "An unauthenticated remote attacker can send a single crafted CLDAP packet to a domain controller's UDP port 389 ... domain controllers with longer DNS domain names and hostnames are vulnerable"; BuildSamLogonResponse 528-byte stack buffer; GS stack cookie. Securonix (2026-06-03) same. (https://aretiq.ai/research/vul260513-cve-2026-41089-microsoft-windows-netlogon-buildsamlogonresponse-stack-based-buffer-overflow-rce/)
   - Fix: Replace "Netlogon RPC endpoint" with "a crafted network request to a domain controller (CLDAP DC-locator ping on UDP/389 per public root-cause analyses)".

4. [factual-error] body, CVE-2026-41096
   - Claim: heap overflow in `dnsapi.dll`: a crafted DNS response ... yields code execution as `NetworkService` on every Windows host
   - Defect: dnsapi.dll and the NetworkService context appear in no cited source; Microsoft says exploitation is only possible "in certain configurations".
   - Ground truth: ZDI: "heap-based buffer overflow in the DNS Client triggered by a malicious DNS response ... An attacker with a position to influence DNS responses (MitM, rogue server)"; Help Net Security quoting Microsoft: "In certain configurations, this could allow the attacker to run code remotely". (https://www.thezdi.com/blog/2026/5/12/the-may-2026-security-update-review)
   - Fix: Remove dnsapi.dll/NetworkService; add the "certain configurations" qualifier.

5. [imprecision] body, ATT&CK / Detection
   - Claim: `T1071.004 Application Layer Protocol: DNS` (DNS Client) ; monitor Netlogon authentication-pattern anomalies (`4624 Logon Type 3` ... paired with `4769`)
   - Defect: T1071.004 is C2-over-DNS, not exploitation of a DNS Client memory-corruption flaw; 4624/4769 are not indicators of a CLDAP stack overflow. Sources name Netlogon crashes/restarts, anomalous Netlogon traffic from non-DC addresses, UDP/389 CLDAP anomalies, lsass.exe faults.
   - Ground truth: Help Net Security (Automox): "The Netlogon service unexpectedly crashing or restarting; Anomalous Netlogon traffic patterns from non-DC source addresses; Authentication failures or domain trust errors immediately after suspicious network activity hits a domain controller". Securonix: Application Event ID 1000 lsass.exe/netlogon.dll, exception 0xC0000409. (https://www.helpnetsecurity.com/2026/06/01/windows-netlogon-rce-exploited-cve-2026-41089/)
   - Fix: Drop T1071.004 (T1210 stands); use the source-supported Netlogon-crash / non-DC-source traffic detections.

6. [imprecision] cves[CVE-2026-41089].status; immediate_action; body
   - Claim: status: exploited, patch-available ; Microsoft had not yet updated its advisory to reflect exploitation
   - Defect: Exploitation rests on the CCB statement alone (sourced from "trusted partners", no details); Microsoft told BleepingComputer and SecurityWeek it has no evidence supporting it, the MSRC record still says Exploited: No (revision 1 only), and the CVE is not in CISA KEV (catalogue 2026.10.16). The entry omits the vendor denial.
   - Ground truth: BleepingComputer (update 2 June 08:51 EDT): "A Microsoft spokesperson also told BleepingComputer that the company does not currently have any evidence to support the CBC's claims"; SecurityWeek: "Microsoft said it has found no evidence to support CCB's claims." MSRC: "exploited":"No","latestSoftwareRelease":"Exploitation Less Likely". (https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/)
   - Fix: Qualify: reported exploited by CCB (29 May); disputed by Microsoft; not in KEV; add Contradiction line; reconsider priority critical.

7. [imprecision] immediate_action
   - Claim: grants remote code execution as SYSTEM on a domain controller with no credentials and no user interaction (Microsoft MSRC)
   - Defect: The MSRC advisory text does not mention SYSTEM; SYSTEM comes from CCB/CERT-EU/Krebs.
   - Ground truth: MSRC: "Stack-based buffer overflow in Windows Netlogon allows an unauthorized attacker to execute code over a network." CCB: "run code on the affected system with SYSTEM privileges". (https://ccb.belgium.be/advisories/warning-microsoft-patch-tuesday-may-2026-patches-118-vulnerabilities-16-critical-102)
   - Fix: Attribute SYSTEM to CCB/CERT-EU, not MSRC.

8. [imprecision] summary / actions[0]
   - Claim: Netlogon (CVE-2026-41089) and DNS Client (CVE-2026-41096) are the wormable-candidate pre-auth RCEs ; 16 of the CVEs were discovered by Microsoft's new MDASH AI scanning harness
   - Defect: Only Netlogon is called wormable by a cited source (ZDI); the DNS Client flaw needs attacker influence over DNS responses and MSRC rates it Exploitation Unlikely. The MDASH sentence is true but no cited source carries it.
   - Ground truth: ZDI: Netlogon "Yup - that makes it wormable"; DNS Client "An attacker with a position to influence DNS responses". CSO Online 2026-05-13: "MDASH ... identified 16 previously unknown Windows vulnerabilities". (https://www.csoonline.com/article/4170785/microsofts-new-ai-system-finds-16-windows-flaws-including-four-critical-rces.html)
   - Fix: Drop "wormable-candidate" for DNS Client; cite the Microsoft/CSO MDASH source.

9. [imprecision] actions[] / record summary
   - Claim: See § 2 ; (. ; see the Immediate Action below and the §4 update
   - Defect: Dangling references to brief sections that do not exist; action[1] ends in a truncated "(.".
   - Ground truth: n/a (editing artefacts) (https://ccb.belgium.be/advisories/warning-microsoft-patch-tuesday-may-2026-patches-118-vulnerabilities-16-critical-102)
   - Fix: Remove the dangling references and the truncated fragment.

### 2026-06-11/windows-netlogon-rce-cve-2026-41089-now-confirmed-exploited
Verdict: factual-error (7 defects)

1. [factual-error] title / headline / summary / actions[0]
   - Claim: now confirmed exploited in the wild in the EU by Belgium's CCB ; CERT-EU published advisory 2026-007 ... confirming that CVE-2026-41089 ... is being actively exploited
   - Defect: CERT-EU does not confirm exploitation: it relays the CCB statement. CCB gave no details; Microsoft says it has no evidence; MSRC still marks Exploited: No; not in CISA KEV.
   - Ground truth: CERT-EU 2026-007: "According to The Centre for Cybersecurity Belgium (CCB), this vulnerability is currently exploited by threat actors." BleepingComputer: Microsoft "does not currently have any evidence to support the CBC's claims". (https://cert.europa.eu/publications/security-advisories/2026-007/)
   - Fix: Say "reported exploited by CCB (relayed by CERT-EU advisory 2026-007); Microsoft disputes"; drop "confirmed".

2. [factual-error] evidence[0].quote
   - Claim: UPDATE (originally covered 2026-W23 weekly): CERT-EU published advisory 2026-007 on 10 June 2026 confirming that CVE-2026-41089 ... citing Belgium's Centre for Cybersecurity …
   - Defect: The quote is the entry's own migrated prose (publisher "ctipilot v2 brief (migrated)"), not a passage of any cited page; it also contains an ellipsis.
   - Ground truth: CERT-EU page carries: "According to The Centre for Cybersecurity Belgium (CCB), this vulnerability is currently exploited by threat actors \[2\]. It is strongly recommended updating affected Windows servers as soon as possible." (https://cert.europa.eu/publications/security-advisories/2026-007/)
   - Fix: Replace with the CERT-EU sentence above.

3. [factual-error] body paragraph 1
   - Claim: roughly 20 days after the May 2026 Patch Tuesday fix
   - Defect: CERT-EU advisory (2026-06-10) came 29 days after Patch Tuesday (2026-05-12); the CCB warning (29 May) came 17 days after.
   - Ground truth: CERT-EU history: "10/06/2026 --- v1.0 -- Initial publication"; "On 12 May 2026, Microsoft published a security advisory". (https://cert.europa.eu/publications/security-advisories/2026-007/)
   - Fix: Say 29 days (CERT-EU) or 17 days (CCB).

4. [factual-error] body paragraph 2
   - Claim: sends a crafted Netlogon RPC packet ... functionally a full Active Directory forest compromise, in the ZeroLogon lineage of Netlogon-channel attacks (BleepingComputer, 2026-06-01)
   - Defect: The cited BleepingComputer article says only "a specially crafted network request" to a DC and carries no forest-compromise or ZeroLogon statement; independent analyses put the vector at CLDAP UDP/389, not RPC.
   - Ground truth: BleepingComputer: "An attacker could send a specially crafted network request to a Windows server that is acting as a domain controller". Securonix (2026-06-03): CLDAP DC Locator ping on UDP 389; compares blast radius to Zerologon. (https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/)
   - Fix: Say "crafted network request to a DC"; attribute forest-takeover to Automox/ZDI/Securonix commentary or drop; drop the ZeroLogon lineage or cite it.

5. [imprecision] actions[0]
   - Claim: legacy Server 2012/2012 R2 past ESU
   - Defect: "Past ESU" is in no cited source; CERT-EU lists 2012/2012 R2 as affected and CCB/Krebs say patches exist for all Windows Server from 2012 onward; MSRC lists fixed builds 6.2.9200.26079 and 6.3.9600.23181.
   - Ground truth: CCB: "Patches are available for all versions of Windows Server from 2012 onwards." MSRC CVRF fixed builds for 2012 / 2012 R2. (https://ccb.belgium.be/advisories/warning-microsoft-patch-tuesday-may-2026-patches-118-vulnerabilities-16-critical-102)
   - Fix: Drop "past ESU" or cite it.

6. [imprecision] cves[CVE-2026-41089].status
   - Claim: status: exploited, patch-available; affected: null; fixed: null
   - Defect: Vendor record does not mark exploited, CISA KEV does not list it; per-branch fixed builds are available but not recorded.
   - Ground truth: MSRC "exploited":"No"; CERT-EU build table; MSRC CVRF KB5087537/38/24/41/23 fixed builds. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-41089)
   - Fix: Qualify the exploited status; fill fixed per branch.

7. [imprecision] body first sentence; sourcing_note
   - Claim: UPDATE (originally covered 2026-W23 weekly) ; migration: evidence backfilled from v2 brief body ... update target unresolved
   - Defect: Workflow-internal text in reader-facing fields; the entry duplicates a finding already carried (with its exploitation update) by the 2026-05-13 entry.
   - Ground truth: n/a (https://cert.europa.eu/publications/security-advisories/2026-007/)
   - Fix: Rewrite as a plain-prose changelog section on the survivor.

### 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days
Verdict: factual-error (10 defects)

1. [factual-error] title / headline / summary / actions[] / body
   - Claim: public PoC, no patch ; YellowKey (no CVE) ... no patch available ; Neither vulnerability has been assigned a CVE nor received a Microsoft patch as of 2026-05-15 ; Public PoC, no patch
   - Defect: Superseded: CVE-2026-45585 was assigned 2026-05-19 (the entry's own update and cves[] say so while the headline, summary and action 1 still say "no CVE"), and Microsoft shipped fixes for YellowKey (CVE-2026-45585) and GreenPlasma (CVE-2026-45586) in the 2026-06-09 June Patch Tuesday.
   - Ground truth: BleepingComputer 2026-06-10: "On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday updates". MSRC CVE-2026-45585 revision 2 (2026-06-09): "Added links to June 2026 Windows security updates. Microsoft recommends installing this updates as soon as possible." (https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)
   - Fix: Bring the headline, summary, labelled lines and actions to the current state: CVE-2026-45585 (YellowKey) and CVE-2026-45586 (GreenPlasma, CTFMON EoP CWE-59, CVSS 7.8) fixed in the June 2026 updates; record fixed builds from the vendor table.

2. [factual-error] cves[CVE-2026-45585].status
   - Claim: status: poc-public, mitigation-only; fixed: null
   - Defect: A security update has been available since 2026-06-09; MSRC also states TPM+PIN is not exploitable.
   - Ground truth: MSRC: "Added links to June 2026 Windows security updates"; FAQ: "I am using TPM+PIN, am I at risk ... No, if you are using TPM+PIN the vulnerability is not exploitable." (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-45585)
   - Fix: Set status to patch-available, fill fixed from MSRC software update table; exploited remains No; not in CISA KEV (2026.10.16).

3. [imprecision] body (YellowKey / TPM+PIN)
   - Claim: the researcher asserts the full bypass also defeats TPM+PIN but the unpublished variant is unconfirmed
   - Defect: True to the BleepingComputer text but omits the vendor's direct statement that TPM+PIN is not exploitable and Dormann's finding that the current exploit does not work against TPM+PIN (a standing contradiction the entry never surfaces).
   - Ground truth: MSRC: "No, if you are using TPM+PIN the vulnerability is not exploitable."; BleepingComputer: Dormann "the current YellowKey exploit does not work in a TMP+PIN environment". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-45585)
   - Fix: Add a Contradiction line: researcher claims TPM+PIN bypass (unpublished), Microsoft says not exploitable.

4. [imprecision] body (YellowKey mechanism)
   - Claim: crafted `FsTx` folder contents placed on a USB drive or the EFI partition are replayed by WinRE
   - Defect: Omits that Dormann could reproduce only with the USB drive, not with files on the EFI partition.
   - Ground truth: BleepingComputer: Dormann "could not reproduce the bug using the EFI partition". (https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)
   - Fix: Say USB confirmed; EFI-partition variant claimed by researcher but not reproduced by Dormann.

5. [imprecision] body (ATT&CK)
   - Claim: T1542.001 (Pre-OS Boot: System Firmware)
   - Defect: YellowKey replays NTFS transaction logs in WinRE to spawn a shell; no firmware is modified, T1542.001 is System Firmware.
   - Ground truth: BleepingComputer/Dormann: "Windows looks for \System Volume Information\FsTx directories on attached drives, and will replay any NTFS logs ... winpeshl.ini is deleted ... it pops up a CMD.EXE". (https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)
   - Fix: Drop T1542.001 (T1006 may stay) or map to a source-supported technique.

6. [factual-error] body ("Microsoft states")
   - Claim: Microsoft states it is "actively investigating."
   - Defect: The quoted phrase appears in none of the cited sources; the Microsoft statement in BleepingComputer is that it is "committed to investigating reported security issues".
   - Ground truth: BleepingComputer: a spokesperson stated the company is committed to investigating reported security issues, "and update impacted devices to protect customers as soon as possible." (https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)
   - Fix: Replace with the verbatim statement or drop the quotation marks.

7. [imprecision] body (total)
   - Claim: bringing the total of unpatched Nightmare Eclipse Windows zero-days to four
   - Defect: The cited BleepingComputer article says two unpatched vulnerabilities and does not count four; BleepingComputer says RedSun was silently patched while The Register says RedSun and UnDefend remain unfixed and counts five zero-days this year.
   - Ground truth: The Register: "a series of five Microsoft zero-day bugs the researcher has exposed this year ... Both RedSun and UnDefend remain unfixed"; BleepingComputer: "Microsoft silently patched the RedSun vulnerability". (https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)
   - Fix: Drop the total or attribute it and flag the BC/Register disagreement (Contradiction line).

8. [imprecision] actions[1]; ## Update body
   - Claim: Microsoft's WinRE `BootExecute` registry mitigation is per-device and fragile under Windows feature updates ; The WinRE registry edit is fragile and breaks on Windows feature updates
   - Defect: No source states the mitigation breaks on feature updates; MSRC revision 1.2 (2026-05-21) replaced the manual steps with a script.
   - Ground truth: MSRC: "removed the manual mitigations ... The script is for WinRE and removes autofstx.exe from the BootExecute registry value ... re-sealing WinRE so BitLocker trust remains intact." (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-45585)
   - Fix: Remove the fragility claim or cite it; describe the MSRC script.

9. [imprecision] actions[0] / body (mitigations)
   - Claim: disable USB/external-media boot ; disable WinRE where operationally viable (`reagentc /disable`)
   - Defect: Not in any cited source (sources give BitLocker PIN and BIOS password).
   - Ground truth: BleepingComputer (Beaumont): "recommended using a BitLocker PIN and a BIOS password"; NCSC-CH #12574: "Implement BIOS passwords and setting a BitLocker PIN". (https://security-hub.ncsc.admin.ch/#/posts/12574)
   - Fix: Cite or drop the reagentc and USB-boot items.

10. [imprecision] priority
   - Claim: priority: high
   - Defect: Physical-access-only BitLocker bypass (CVSS 6.8, AV:P) for TPM-only devices; no exploitation reported; vendor patch exists since 2026-06-09.
   - Ground truth: MSRC: "exploited":"No"; "bypass a security feature with a physical attack". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-45585)
   - Fix: Context only: high is hard to defend on today's facts.

### 2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes
Verdict: factual-error (8 defects)

1. [factual-error] cves[CVE-2026-45585]
   - Claim: cvss: n/a; type: lpe; vector: local; auth: post-auth; status: poc-public, no-patch
   - Defect: CVE-2026-45585 is the YellowKey BitLocker security-feature bypass (physical attack, CVSS 6.8, PR:N), not a local privilege escalation; and it has been patched since 2026-06-09.
   - Ground truth: MSRC: "Windows BitLocker Security Feature Bypass Vulnerability", CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, "bypass a security feature with a physical attack"; rev 2 2026-06-09 links June 2026 security updates. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-45585)
   - Fix: Correct the record (SFB, physical, 6.8, patched) or drop the cves[] record: this entry is about Microsoft's disclosure-dispute statement, not a single CVE.

2. [factual-error] summary / body paragraph 1
   - Claim: Microsoft's Digital Crimes Unit issued a formal public statement on 28–29 May 2026
   - Defect: The statement is an MSRC blog post dated 2026-05-27 (Wednesday); The Record reported it 2026-05-29. It also was a Microsoft Security Response Center post, with the DCU named in one sentence.
   - Ground truth: MSRC blog "A shared responsibility: Protecting customers through Coordinated Vulnerability Disclosure", date 2026-05-27; The Record: "In a blogpost on Wednesday, Microsoft said". (https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure)
   - Fix: Say Microsoft (MSRC) published it on 27 May 2026.

3. [factual-error] title / headline
   - Claim: Microsoft's Digital Crimes Unit threatens criminal action
   - Defect: Overstates: The Record reports Microsoft "stopped short of directly threatening legal action" (heise.de reads it as threatening lawsuits), a source disagreement the entry resolves silently.
   - Ground truth: The Record: "The company stopped short of directly threatening legal action, but said: 'Our Digital Crimes Unit will continue bringing cases against these actors and those that enable their criminal activity'". heise: "Microsoft is threatening lawsuits and the police." (https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)
   - Fix: Say "warns its Digital Crimes Unit will keep bringing cases" and add a Contradiction line.

4. [factual-error] body paragraph 1
   - Claim: responded by threatening a new vulnerability release on 14 July 2026 (the next Patch Tuesday)
   - Defect: 14 July is the Patch Tuesday after next (the next one after 29 May was 9 June 2026); the sources do not say the threat was a response to Microsoft's statement.
   - Ground truth: The Record: "The researcher threatened a further release on July 14 — the date scheduled for Microsoft's Patch Tuesday"; June Patch Tuesday was 2026-06-09 (BleepingComputer 2026-06-10). (https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)
   - Fix: Drop "responded" and "the next"; say "the July Patch Tuesday".

5. [factual-error] body (final sentence)
   - Claim: Next Patch Tuesday: 10 June 2026.
   - Defect: June 2026 Patch Tuesday was 9 June.
   - Ground truth: BleepingComputer 2026-06-10: "On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday updates". (https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)
   - Fix: Change to 9 June 2026 (and bring the entry current: all three were patched that day).

6. [imprecision] title / body paragraph 2
   - Claim: GreenPlasma and MiniPlasma remain unpatched as of 30 May 2026 ; no CVE yet assigned to MiniPlasma itself ; root cause is assessed as an incomplete remediation of CVE-2020-17103
   - Defect: Accurate for 30 May but superseded: on 2026-06-09 Microsoft fixed YellowKey (CVE-2026-45585), GreenPlasma (CVE-2026-45586, CTFMON EoP) and MiniPlasma (via re-release of CVE-2020-17103). The incomplete-fix statement is the researcher's claim (BleepingComputer) and is uncited here.
   - Ground truth: MSRC CVE-2020-17103 rev 2 (2026-06-09): "This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2020-17103". MSRC CVE-2026-45586 released 2026-06-09, CVSS 7.8, CWE-59, "Exploitation More Likely". BleepingComputer 2026-06-10. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2020-17103)
   - Fix: Add the June 2026 fix state and the CVE mappings; cite BleepingComputer 2026-05-17 for the MiniPlasma facts and attribute the incomplete-fix claim to the researcher.

7. [imprecision] headline
   - Claim: GreenPlasma and MiniPlasma (cldflt.sys SYSTEM escalation)
   - Defect: cldflt.sys is the MiniPlasma component; GreenPlasma is a CTFMON flaw (heise conflates the two via CVE-2020-17103).
   - Ground truth: BleepingComputer: GreenPlasma = "Windows CTFMON Arbitrary Section Creation Elevation of Privileges Vulnerability"; MiniPlasma = cldflt.sys HsmOsBlockPlaceholderAccess. (https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)
   - Fix: Reword the headline so cldflt.sys is tied to MiniPlasma only.

8. [imprecision] body / summary / sourcing_note
   - Claim: UPDATE (originally covered 2026-W21) ; migration: update target unresolved
   - Defect: Workflow-internal text in reader-facing fields.
   - Ground truth: n/a (https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)
   - Fix: Rewrite in plain prose.

### 2026-05-16/cve-2026-42897-microsoft-exchange-server-2016-2019-se-stored
Verdict: factual-error (9 defects)

1. [factual-error] title / headline / summary / immediate_action / actions[] / cves[].status / body
   - Claim: no permanent patch ; Active Exploitation Without a Patch ; Permanent fixes are forthcoming ; mitigation-only
   - Defect: Superseded: Microsoft released the CVE-2026-42897 fix in the June 2026 Exchange Security Updates on 2026-06-09 (SE RTM publicly; 2019 CU14/CU15 and 2016 CU23 only for Period 2 ESU customers); the July 2026 SUs (2026-07-14) are also recommended by MSRC.
   - Ground truth: Exchange Team 2026-06-09: "The June 2026 SUs address ... CVE-2026-42897"; FAQ: "When CVE-2026-42897 mitigations were released ... Are those solved in the CVE-2026-42897 fix (June 2026 SU)? Yes". MSRC rev 2 2026-06-09 "Added links to June 2026 Exchange Server security updates"; Learn M2 "Highest version applicable ... June 2026 SU". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Rewrite headline, summary, labelled lines and actions for the current state: fix available since 2026-06-09, mitigation removable after the July SU, exploitation by TA488 documented 2026-07-28.

2. [factual-error] title / headline / immediate_action / body
   - Claim: stored XSS in OWA ; a stored / reflected cross-site scripting flaw
   - Defect: No source characterises the flaw as stored (or reflected); Microsoft says "cross-site scripting" with spoofing impact.
   - Ground truth: MSRC: "Microsoft Exchange Server Spoofing Vulnerability ... Improper neutralization of input during web page generation ('cross-site scripting')"; Proofpoint: "the server does not adequately sanitize HTML in the message body". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Say "cross-site scripting (spoofing) in OWA".

3. [factual-error] body (mitigation / EEMS)
   - Claim: enabled by default on Exchange 2016 SP1 and later and auto-applies without requiring a service restart ; EEMS Mitigation M2
   - Defect: The EM service applies from the September 2021 CU (2016 CU22 / 2019 CU11) and can only fetch new mitigations on builds from March 2023 or later; "2016 SP1" does not exist as a threshold; the no-restart statement and the "M2" (rule M2.1.x) naming are not as sourced.
   - Ground truth: Exchange Team: "EM Service will not be able to check for new mitigations if your server is running Exchange Server version older than March 2023"; Learn: M2 lowest version "Exchange 2016: RTM" but EM service from "September 2021 CU"; mitigation ID "M2.1.x". (https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498)
   - Fix: State the real prerequisites (September 2021 CU or later; build from March 2023 or later for new mitigations; officeclient.microsoft.com:443) and drop the restart claim.

4. [factual-error] actions[0]; body (verification)
   - Claim: Run `Get-ExchangeDiagnosticInfo -Server <name> -Process MSExchangeHMWorker -Component EemsMitigation -SettingName MitigationsApplied` ; look back to 2026-05-09
   - Defect: The command appears in no cited source (Microsoft documents Get-ExchangeServer | fl Name,MitigationsApplied, Get-Mitigations.ps1 and the Health Checker); the 2026-05-09 lookback has no basis (Proofpoint dates the actor infrastructure to March 2026).
   - Ground truth: Learn: "Get-ExchangeServer -Identity <ServerName> | Format-List Name,MitigationsApplied"; Exchange Team: run Exchange Health Checker. (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Use the Microsoft-documented checks; drop or justify the lookback date.

5. [imprecision] body (Detection)
   - Claim: IIS access logs ... `/owa/` URLs containing `<script>` fragments ... in query strings; Exchange Application Event Log EID 4 ...; EDR alerts on browser processes spawning unexpected children from OWA sessions
   - Defect: Does not fit the documented mechanism: the payload is JavaScript in the email body run in the browser with no host footprint; no source supports these log fields.
   - Ground truth: Proofpoint: "OWAReaper runs inside the OWA browser context, operating as a stealthy implant with no host footprint"; detections: Default-user folder grants, EWS add-in tokens, IndexedDB/localStorage. (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Replace with source-supported detections (mailbox folder-permission grants to Default, add-in token abuse, GetClientAccessToken, OWA localStorage/IndexedDB artefacts).

6. [imprecision] body ("three tiers")
   - Claim: Exploitation Detected (the highest of its three exploitation-status tiers)
   - Defect: Microsoft's exploitability assessments are Exploitation Detected / More Likely / Less Likely / Unlikely (four).
   - Ground truth: MSRC records show "Exploitation Detected", "Exploitation More Likely", "Exploitation Less Likely", "Exploitation Unlikely". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Drop the tier count.

7. [imprecision] body (first paragraph)
   - Claim: disclosed by Microsoft on 2026-05-14 alongside the May 2026 Patch Tuesday cycle
   - Defect: Patch Tuesday was 2026-05-12; the CVE was an out-of-band disclosure on Thursday 2026-05-14 (NCSC-NL: "out-of-band update").
   - Ground truth: MSRC release 2026-05-14T07:00-07:00; NCSC-NL NCSC-2026-0159: mitigations "middels een out-of-band update". (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Say out-of-band disclosure on 2026-05-14, two days after Patch Tuesday.

8. [imprecision] evidence[1]
   - Claim: Microsoft is supplying a temporary mitigation for this vulnerability through the Exchange Emergency Mitigation Service. We are working on developing and testing a more permanent fix.
   - Defect: (low confidence) The sentence is on neither the current MSRC page nor the Exchange blog (both revised since); cannot be verified verbatim today.
   - Ground truth: MSRC record revised 2026-05-18, 2026-06-09, 2026-07-14; current FAQ has no such sentence. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Replace with a quote verifiable on the current page, or drop.

9. [imprecision] body / actions[1]
   - Claim: See § 5 (Deep Dive, "Permanent-patch availability" paragraph)
   - Defect: Dangling pointer to a section of the migrated brief that does not exist in this entry.
   - Ground truth: n/a (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Remove.

### 2026-05-16/microsoft-exchange-cve-2026-42897-active-exploitation-withou
Verdict: factual-error (9 defects)

1. [factual-error] title / headline / summary / immediate_action / actions[] / cves[].status / body
   - Claim: no permanent patch ; Active Exploitation Without a Patch ; Permanent fixes are forthcoming ; mitigation-only
   - Defect: Superseded: Microsoft released the CVE-2026-42897 fix in the June 2026 Exchange Security Updates on 2026-06-09 (SE RTM publicly; 2019 CU14/CU15 and 2016 CU23 only for Period 2 ESU customers); the July 2026 SUs (2026-07-14) are also recommended by MSRC.
   - Ground truth: Exchange Team 2026-06-09: "The June 2026 SUs address ... CVE-2026-42897"; FAQ: "When CVE-2026-42897 mitigations were released ... Are those solved in the CVE-2026-42897 fix (June 2026 SU)? Yes". MSRC rev 2 2026-06-09 "Added links to June 2026 Exchange Server security updates"; Learn M2 "Highest version applicable ... June 2026 SU". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Rewrite headline, summary, labelled lines and actions for the current state: fix available since 2026-06-09, mitigation removable after the July SU, exploitation by TA488 documented 2026-07-28.

2. [factual-error] body, Mitigation M2 mechanism
   - Claim: Mitigation M2, which rewrites the specific request format the in-the-wild exploit uses to deliver the XSS payload — the mitigation does not require an Exchange restart
   - Defect: M2 is a URL Rewrite outbound rule adding a Content-Security-Policy (CSP) to OWA responses (which is why IE / IE-mode clients are not protected); the blog says nothing about request-format rewriting or restart.
   - Ground truth: Learn: rollback removes the "EEMS M2.1 OWA CSP - outbound" outbound rule and "EEMS M2.1 OWA SPA HTML shell - precondition"; MSRC FAQ: "No, because Content Security Policy (CSP) is not supported by Internet Explorer nor Microsoft Edge using Internet Explorer Mode". (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Describe M2 as a CSP-injecting URL Rewrite rule; drop the restart claim.

3. [factual-error] body, EEMS paragraph
   - Claim: `Set-Server -MitigationsEnabled $false` ; `Get-Server <server> | Select-Object MitigationsEnabled` ; via Group Policy ; hardened with custom IIS rewrite rules that conflict ; For all four cases ... EOMT
   - Defect: Non-existent cmdlets (Set-Server / Get-Server); Group Policy and the custom-rewrite-rule case are in no source; Exchange 2013 is not an affected version, so (a) does not describe an exposed state.
   - Ground truth: Learn: "Set-OrganizationConfig -MitigationsEnabled $false" and "Set-ExchangeServer -Identity <ServerName> -MitigationsEnabled $false"; Exchange blog: affected 2016, 2019, SE. (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Use Set-ExchangeServer / Get-ExchangeServer and drop unsupported cases.

4. [imprecision] body, EEMS verification and hunt
   - Claim: Get-ExchangeDiagnosticInfo ... EemsMitigation ... ; w3wp.exe spawning unexpected children ... post-exploitation tell of XSS-to-execution chains ; Exchange Application Event Log EID 4 ; query strings
   - Defect: Unsupported command; detections do not fit a browser-side JavaScript implant with no host footprint.
   - Ground truth: Proofpoint: "no host footprint"; Learn: Get-ExchangeServer | Format-List Name,MitigationsApplied. (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Use Microsoft-documented verification and Proofpoint-sourced detections.

5. [factual-error] body, exploitation and attribution
   - Claim: Microsoft notes the scale and identity of the exploitation activity are not yet detailed publicly (The Hacker News) ; No named threat-actor attribution has been published
   - Defect: The statement is The Hacker News's, not Microsoft's; and attribution is now published (Proofpoint 2026-07-28: TA488 / Void Blizzard / LAUNDRY BEAR).
   - Ground truth: THN: "There are currently no details on how the vulnerability is being exploited, the identity of the threat actor behind the activity, or the scale of such efforts." Proofpoint: "Proofpoint attributes this activity to TA488". (https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html)
   - Fix: Attribute to THN with date, and add the TA488 attribution.

6. [imprecision] body, attack chain
   - Claim: T1566.001 Phishing: Spearphishing Attachment ... T1078 ... T1534 Internal Spearphishing ... payload reads OWA session cookies / auth tokens
   - Defect: The delivery is an email body with no attachment or URL; the chain steps (cookie theft, valid-account reuse, internal spearphishing) are analyst conjecture that later primary reporting does not confirm (observed: autofill credential harvest, add-in OAuth token theft via GetClientAccessToken, Default-user folder grants).
   - Ground truth: Proofpoint: "no suspicious URLs or attachments present"; "creates two invisible input elements ... waits for the browser's autofill"; "uses those add-ins to call GetClientAccessToken to steal OAuth tokens". (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Replace with the Proofpoint-observed behaviour; drop T1566.001.

7. [imprecision] body, quantifiers
   - Claim: CVE-2026-42897 is the first 2026 case where EEMS ... is the line of defence ; repeated EEMS-only mitigations across the 2021-2026 Exchange CVE history ; Hafnium and dozens of follow-on clusters
   - Defect: Unsupported quantifiers: Learn lists only two CVE mitigations (M1 in 2022, M2 in 2026); "dozens of clusters" is not in the cited Microsoft post.
   - Ground truth: Learn mitigation list: PING1, M1 (CVE-2022-41040), M2 (CVE-2026-42897). (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Remove the superlative and counts or cite them.

8. [imprecision] body, patch details
   - Claim: a security update for Exchange 2016 CU23 and Exchange 2019 CU14 / CU15 (cited to the May Exchange blog)
   - Defect: The May blog gives no CU numbers (they appear in the June 2026 SU blog); the September 2021 blog cited for the EEMS introduction could not be read by any transport in this audit, so that adjacency is unverified (the Learn doc confirms the September 2021 CU).
   - Ground truth: June SU blog: "Exchange Server 2019 CU14 and CU15 ... Exchange Server 2016 CU23 (... Period 2 ESU program)". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Cite the June SU blog.

9. [imprecision] body ("PD-13"), sourcing_note, evidence[0]
   - Claim: per PD-13 in this brief series ; migration: evidence backfilled ; quote "Background."
   - Defect: Workflow-internal text in reader-facing fields; evidence[0] quote is just the word "Background." with publisher "ctipilot v2 brief (migrated)", not a source passage.
   - Ground truth: n/a (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Replace the evidence quote with a verbatim source passage; strip workflow text.

### 2026-05-17/exchange-cve-2026-42897-pwn2own-devcore-three-bug-system-rce
Verdict: factual-error (7 defects)

1. [factual-error] summary / body paragraph 1 / body paragraph 2
   - Claim: achieve unauthenticated remote code execution at SYSTEM privilege level ; a fresh unauthenticated SYSTEM RCE class
   - Defect: "Unauthenticated" is in neither ZDI nor BleepingComputer.
   - Ground truth: ZDI: "chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange"; BleepingComputer: "chaining three bugs to gain remote code execution with SYSTEM privileges on Microsoft Exchange". (https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)
   - Fix: Drop "unauthenticated" or cite a source.

2. [factual-error] body (ZDI verbatim)
   - Claim: ZDI verbatim: "Orange Tsai (DEVCORE Research Team) earned $200,000 after chaining three bugs to gain remote code execution with SYSTEM privileges on Microsoft Exchange."
   - Defect: The quoted sentence is not ZDI's; it is BleepingComputer's wording. ZDI's text differs.
   - Ground truth: ZDI: "Orange Tsai (@orange_8361) of DEVCORE Research Team chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points." (https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)
   - Fix: Quote ZDI verbatim or attribute to BleepingComputer.

3. [factual-error] cves[CVE-2026-42897]
   - Claim: type: rce; status: exploited, cisa-kev, mitigation-only
   - Defect: This entry is about a different, CVE-less Pwn2Own Exchange chain; tagging CVE-2026-42897 as RCE is wrong (XSS/spoofing) and the mitigation-only status is superseded by the 2026-06-09 SUs.
   - Ground truth: MSRC: "Microsoft Exchange Server Spoofing Vulnerability", Impact Spoofing. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Drop the cves[] record (reference the CVE entry instead) or correct type and status.

4. [imprecision] body (blog 502 note)
   - Claim: the Microsoft Exchange blog post ... linked from the MSRC advisory returns 502 on direct fetch and the MSRC entry itself is the operational primary
   - Defect: Process narration that is false today: the post is reachable and is the primary mitigation guidance.
   - Ground truth: Exchange Team post fetched 2026-10-18 (full text, last updated 2026-07-14). (https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498)
   - Fix: Remove.

5. [factual-error] actions[0]; body (stale state)
   - Claim: through August Patch Tuesday 2026 ; CVE-2026-42897 active XSS, no permanent patch ; until Microsoft ships permanent fixes for both ; Exchange Online tenants are not in scope for either
   - Defect: The CVE-2026-42897 fix shipped 2026-06-09; Microsoft's "Exchange Online is not impacted" statement covers CVE-2026-42897 only, not the Pwn2Own chain; Get-ExchangeDiagnosticInfo command unsupported; "§ 4 UPDATE" dangling.
   - Ground truth: Exchange Team June 2026: SUs address CVE-2026-42897; May blog: "Exchange Online is not impacted by this vulnerability". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Bring to current state; scope the Exchange Online statement to the CVE.

6. [imprecision] body (KEV link)
   - Claim: CISA KEV (added 2026-05-15)
   - Defect: Cited URL is the generic KEV catalogue landing page (not a per-CVE page); the fact itself is correct (dateAdded 2026-05-15).
   - Ground truth: KEV 2026.10.16: CVE-2026-42897 dateAdded 2026-05-15, dueDate 2026-05-29. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Cite MSRC or the CISA alert instead of the catalogue landing page.

7. [imprecision] evidence[0]; sourcing_note
   - Claim: UPDATE (originally covered ...) quote ; migration: ...
   - Defect: evidence[0] is entry prose from the migrated brief (publisher "ctipilot v2 brief (migrated)"), with an ellipsis, not a passage of any cited page.
   - Ground truth: n/a (https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)
   - Fix: Replace with a verbatim ZDI passage.

### 2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen
Verdict: factual-error (10 defects)

1. [factual-error] title / headline / summary / immediate_action / body paragraph 1
   - Claim: Exchange Team Blog update confirms the EM Service auto-mitigation requires outbound HTTPS connectivity ... to officemitigations.microsoft.com ; The Microsoft Exchange Team Blog post ... was last modified 2026-05-17 to clarify an operational dependency
   - Defect: The cited blog carries no connectivity-dependency statement (its 2026-05-17 update added only an OWACalendar.Proxy known issue) and the host name appears in no source; Microsoft documents the Office Config Service endpoint as officeclient.microsoft.com on port 443 in the EM-service doc. The dependency itself is real but the title, summary, immediate action and body bind it to the wrong host and the wrong source.
   - Ground truth: Learn: "Office Config Service | officeclient.microsoft.com/* | 443 | Required endpoint for the Exchange EM service"; Exchange blog update log: "5/17/2026: Added a known issue with OWACalendar.Proxy healthset showing unhelathy". (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Use officeclient.microsoft.com and cite the Learn doc; drop "last modified 2026-05-17 to clarify".

2. [factual-error] actions[0]; body paragraph 2
   - Claim: Run `Get-ExchangeDiagnosticInfo -Server <server> -Process EdgeTransport -Component EmergencyMitigation` ... confirm `Status: Active`
   - Defect: The command and output field appear in no source; Microsoft documents Get-ExchangeServer | Format-List Name,MitigationsApplied and the Health Checker.
   - Ground truth: Learn: "Get-ExchangeServer -Identity <ServerName> | Format-List Name,MitigationsApplied". (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service)
   - Fix: Use the documented commands.

3. [factual-error] summary / immediate_action / actions[0] / body paragraphs 1-2
   - Claim: no permanent patch is available yet ; No permanent patch yet ; no permanent cumulative-update fix as of 2026-05-18
   - Defect: The entry was updated on 2026-07-31 with a section stating the July SU is the fix, yet summary, immediate_action and actions[0] still say no permanent patch exists (self-contradiction), and the fix actually shipped 2026-06-09.
   - Ground truth: Exchange Team 2026-06-09: "The June 2026 SUs address ... CVE-2026-42897". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Rewrite summary / immediate_action / actions[0] to the current state; keep the May text only as dated history.

4. [factual-error] cves[CVE-2026-42897].affected / fixed; ## Update 2026-07-31 Patching
   - Claim: all update levels prior to the July 2026 Security Update ; The permanent fix is the July 2026 Security Update ; May shipped a mitigation, July shipped the fix
   - Defect: The first fix shipped in the June 2026 SUs (2026-06-09); the July SUs are cumulative and also fix sibling CVE-2026-55008. "Prior to the July 2026 SU" misstates the affected range.
   - Ground truth: Learn M2: "Highest version applicable: Exchange SE: June 2026 SU - Exchange 2019: June 2026 SU - Exchange 2016: June 2026 SU"; June blog FAQ: "the CVE-2026-42897 fix (June 2026 SU)"; MSRC FAQ 7/14: install July SUs "to be protected from this vulnerability and related CVE-2026-55008". (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Set fixed to the June 2026 SU (SE RTM public; 2019 CU14/15 and 2016 CU23 via Period 2 ESU) and note the July SU and CVE-2026-55008; affected = versions before the June 2026 SU.

5. [imprecision] body paragraph 2 / evidence[1]
   - Claim: Microsoft states verbatim "We are working on developing and testing a more permanent fix which we will provide when it meets our quality standards."
   - Defect: (low confidence) The quoted sentence is not on the current Exchange blog or MSRC page (both revised); it cannot be verified verbatim today.
   - Ground truth: Exchange blog current text: "Microsoft is working on and will release and announce a security update for impacted versions of Exchange Server in the future." (https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498)
   - Fix: Quote a sentence verifiable on the current page or drop.

6. [imprecision] tags
   - Claim: no-patch together with patch-available
   - Defect: Contradictory tags on one entry.
   - Ground truth: n/a (June 2026 SU exists) (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Drop no-patch.

7. [imprecision] evidence[0] attribution; sources[] dates
   - Claim: publisher Microsoft Exchange Team Blog for "The Exchange Emergency Mitigation Service will provide mitigation automatically ... " ; Proofpoint 2026-07-29
   - Defect: The sentence is the MSRC FAQ, not the Exchange blog; Proofpoint's post is dated 2026-07-28 on the page.
   - Ground truth: MSRC FAQ: "The Exchange Emergency Mitigation Service will provide mitigation automatically, and is on by default."; Proofpoint page date 2026-07-28. (https://api.msrc.microsoft.com/sug/v2.0/sugodata/v2.0/en-US/vulnerability/CVE-2026-42897)
   - Fix: Attribute to MSRC; use 2026-07-28 (or note timezone).

8. [imprecision] techniques[]
   - Claim: T1552 Unsecured Credentials
   - Defect: Autofill harvesting is Credentials from Web Browsers and the GetClientAccessToken abuse is Application Access Token theft; T1552 fits neither; T1528 and T1555.003 are not mapped.
   - Ground truth: Proofpoint: "waits for the browser's autofill to enter the username and password"; "call GetClientAccessToken to steal OAuth tokens". (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Map T1555.003 and T1528 (both active in the pinned dataset) instead of T1552.

9. [imprecision] ## Update 2026-07-31 / ## Improvement 2026-08-30 (reader-facing wording)
   - Claim: The May entry tracked ... ; which this pipeline registers as LAUNDRY BEAR ; **A1** on the NATO Admiralty scale
   - Defect: Workflow-internal wording and Admiralty letters in reader-facing sections; the Improvement section is metadata-only and should have been internal.
   - Ground truth: n/a (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)
   - Fix: Strip internal wording; make the metadata-only record internal.

10. [imprecision] priority
   - Claim: priority: critical
   - Defect: On 2026-07-31 a vendor fix had existed for seven weeks; the new element is an actor campaign (TA488) against government targets in the US and Europe.
   - Ground truth: Exchange Team 2026-06-09 SUs; Proofpoint 2026-07-28. (https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491)
   - Fix: Context only: critical is hard to defend for a patched flaw; high may fit given on-prem Exchange exposure.

### 2026-06-08/cve-2026-3300-everest-forms-pro-wordpress-unauthenticated-ev
Verdict: factual-error (7 defects)

1. [factual-error] body / summary
   - Claim: mass exploitation running since 13 April (29,300+ blocked attempts, a single-day spike of 17,900 on 16 May, still active as of 6 June) ; sustained mass exploitation from 13 April through at least 6 June
   - Defect: Wordfence says exploitation began 13 April and "mass exploitation" occurred on 16 May; nothing says it was sustained mass exploitation through 6 June; 26,300 of the 29,300 blocked requests came from one IP and The Hacker News (2026-06-05) counts 16 attempts in the last 24 hours.
   - Ground truth: Wordfence: "attackers started targeting websites on April 13th, 2026 ... mass exploitation occurring on May 16th, 2026"; "Over 26,300 blocked requests" from the top IP; THN: "16 attack attempts occurred in the last 24 hours". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Say exploitation observed from 13 April with a 17,900-attempt spike on 16 May, most volume from one source; drop "still active as of 6 June".

2. [factual-error] body (inclusion gate)
   - Claim: Inclusion gate: vendor-confirmed in-the-wild exploitation at scale.
   - Defect: Exploitation is reported by Wordfence (a security vendor, from its firewall telemetry); the plugin vendor (WPEverest) made no confirmation in any source; the sentence is also pipeline-internal language.
   - Ground truth: Wordfence / BleepingComputer / THN report Wordfence telemetry only. (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Delete the sentence.

3. [factual-error] evidence[0]
   - Claim: A pre-authentication PHP code-injection (CVSS 9.8) in the Calculation Addon ... lets an unauthenticated visitor break out of a calculated form field ...
   - Defect: The quote is the entry's own prose from the migrated brief (publisher "ctipilot v2 brief (migrated)") with an ellipsis; it is not a passage of any cited page.
   - Ground truth: Wordfence: "This is due to the Calculation Addon's process_filter() function concatenating user-submitted form field values into a PHP code string without proper escaping before passing it to eval()." (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Replace with a verbatim Wordfence passage.

4. [imprecision] summary / body citation labels
   - Claim: [Wordfence, 2026-06-06]
   - Defect: The Wordfence post is dated 2026-06-03 (16:59Z); 2026-06-06 is the BleepingComputer date.
   - Ground truth: Wordfence post "Published Time: 2026-06-03T16:59:22+00:00"; BleepingComputer date 2026-06-06; THN 2026-06-05. (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Label the Wordfence source 2026-06-03.

5. [imprecision] body (prerequisite)
   - Claim: the form must include the Calculation Addon ; submits a form containing a calculation field
   - Defect: Prerequisite is a form using the "Complex Calculation" feature; the payload goes in any string-type field (text, email, URL, select, radio), not a calculation field.
   - Ground truth: Wordfence: "by submitting a crafted value in any string-type form field (text, email, URL, select, radio) when a form uses the 'Complex Calculation' feature". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Use the Wordfence wording.

6. [imprecision] summary / body
   - Claim: full technical analysis in § 5 ; Full mechanics, detection and hardening in § 5
   - Defect: Dangling references to a section that does not exist in the entry.
   - Ground truth: n/a (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Remove.

7. [imprecision] cves[CVE-2026-3300]; priority
   - Claim: affected: null; fixed: null; priority: high
   - Defect: Affected (<= 1.9.12) and fixed (1.9.13) are known and not recorded; the plugin has about 4,000 active installations and the entry shows no exposure of the constituency (a high with no exposure evidence).
   - Ground truth: CVE record (CNA Wordfence): affected lessThanOrEqual 1.9.12, CVSS 9.8; Wordfence/THN: "estimated 4,000 active installations". (https://cveawg.mitre.org/api/cve/CVE-2026-3300)
   - Fix: Fill affected/fixed; context only: priority high is weak.

### 2026-06-08/cve-2026-3300-unauthenticated-eval-injection-in-a-commercial
Verdict: factual-error (9 defects)

1. [factual-error] body / summary
   - Claim: mass exploitation running since 13 April (29,300+ blocked attempts, a single-day spike of 17,900 on 16 May, still active as of 6 June) ; sustained mass exploitation from 13 April through at least 6 June
   - Defect: Wordfence says exploitation began 13 April and "mass exploitation" occurred on 16 May; nothing says it was sustained mass exploitation through 6 June; 26,300 of the 29,300 blocked requests came from one IP and The Hacker News (2026-06-05) counts 16 attempts in the last 24 hours.
   - Ground truth: Wordfence: "attackers started targeting websites on April 13th, 2026 ... mass exploitation occurring on May 16th, 2026"; "Over 26,300 blocked requests" from the top IP; THN: "16 attack attempts occurred in the last 24 hours". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Say exploitation observed from 13 April with a 17,900-attempt spike on 16 May, most volume from one source; drop "still active as of 6 June".

2. [factual-error] headline
   - Claim: the patch-lag that turned a March fix into a June mass-exploitation campaign
   - Defect: No June mass-exploitation campaign in the sources: exploitation began 13 April, the mass spike was 16 May, the reports appeared 3-6 June.
   - Ground truth: Wordfence: attackers started 13 April; "mass exploitation occurring on May 16th". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Reword to "mass exploitation from mid-May".

3. [factual-error] evidence[0]
   - Claim: Why this is the deep dive now.
   - Defect: Not a quote from any source; it is the entry's own opening sentence (publisher "ctipilot v2 brief (migrated)").
   - Ground truth: n/a (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Replace with a verbatim Wordfence passage.

4. [imprecision] body (The bug)
   - Claim: builds a PHP expression string ... with eval() ([BleepingComputer, 2026-06-06]) ... `process_filter()` function of the plugin's Calculation Addon
   - Defect: The cited BleepingComputer article names the "Complex Calculation feature" and eval() but not process_filter() or the Calculation Addon; those are in the Wordfence post.
   - Ground truth: BleepingComputer: "The CVE-2026-3300 vulnerability is in the plugin's Complex Calculation feature ... executes the resulting code using PHP's 'eval ()' function." (https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/)
   - Fix: Cite Wordfence for process_filter() and the addon name.

5. [imprecision] summary / body citation labels
   - Claim: [Wordfence, 2026-06-06]
   - Defect: The Wordfence post is dated 2026-06-03 (16:59Z); 2026-06-06 is the BleepingComputer date.
   - Ground truth: Wordfence post "Published Time: 2026-06-03T16:59:22+00:00"; BleepingComputer date 2026-06-06; THN 2026-06-05. (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Label the Wordfence source 2026-06-03.

6. [imprecision] body (prerequisite)
   - Claim: the form must include the Calculation Addon ; submits a form containing a calculation field
   - Defect: Prerequisite is a form using the "Complex Calculation" feature; the payload goes in any string-type field (text, email, URL, select, radio), not a calculation field.
   - Ground truth: Wordfence: "by submitting a crafted value in any string-type form field (text, email, URL, select, radio) when a form uses the 'Complex Calculation' feature". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Use the Wordfence wording.

7. [imprecision] body (relevance)
   - Claim: WordPress underpins a large share of cantonal, municipal and agency web estates, so any public-sector site still running Everest Forms Pro ≤ 1.9.12 is exposed
   - Defect: Uncited; omits that the plugin has about 4,000 active installations and that Wordfence/THN show no public-sector victims.
   - Ground truth: THN: "a WordPress plugin with about 4,000 active installations". (https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html)
   - Fix: Add the install base; keep the exposure statement conditional.

8. [imprecision] body (observed chain)
   - Claim: from which attackers typically install webshells, SEO-spam injectors or redirect malware
   - Defect: Wordfence names webshells, theme/plugin modification and backdoors; SEO-spam and redirect malware are not stated.
   - Ground truth: Wordfence: "uploading webshells, modifying themes or plugins, or installing further backdoors for persistent access". (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Match the source or drop the extras.

9. [imprecision] summary / body / sourcing_note
   - Claim: Why this is the deep dive now ; migration: evidence backfilled
   - Defect: Workflow-internal wording in reader-facing fields; actions[0] contains a truncated "(." artefact.
   - Ground truth: n/a (https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/)
   - Fix: Rewrite in plain prose and fix the action.

### 2026-06-16/cisco-catalyst-sd-wan-manager-cve-2026-20262-authenticated-a
Verdict: factual-error (9 defects)

1. [factual-error] body (exploitation / detection / hardening) and actions[0]
   - Claim: write a `.jsp`/`.war` artefact into the Tomcat deployment directory ; newly written files in the Tomcat webapps/deploy directories ; validate the integrity of the Tomcat deploy directory ; the Tomcat deploy directory for planted `.jsp`/`.war` web shells ; Writing a JSP/WAR into the Tomcat deploy path
   - Defect: Cisco's own indicators show a WildFly application server: the malicious WAR is written to /var/lib/wildfly/standalone/deployments/ and deployed by the WildFly DeploymentScanner (WFLYSRV0010). "Tomcat" appears in no source.
   - Ground truth: Cisco PSIRT: vmanage-server.log "SdraAnyConnectFileUploadHandler ... uploaded Remote Access Anyconnect profile file: ../../../../var/lib/wildfly/standalone/deployments/suspicious.war"; vmanage-appserver.log "WFLYSRV0010: Deployed \"suspicious.war\""; serviceproxy-access.log "POST /suspicious/index.jsp". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Replace Tomcat with the WildFly deployments directory and cite Cisco's three log indicators (vmanage-server.log AnyConnect profile-upload handler with ../ path, appserver deployment, service-proxy POST to index.jsp).

2. [imprecision] body (KEV citation)
   - Claim: CISA added CVE-2026-20262 to the Known Exploited Vulnerabilities catalog on 2026-06-15 ([BleepingComputer, 2026-06-15]) ; Cisco confirms active exploitation and CISA added it to the KEV catalog on 2026-06-15 (BleepingComputer)
   - Defect: The fact is true (KEV dateAdded 2026-06-15) but the cited BleepingComputer article does not mention a KEV listing for this CVE; The Register and the KEV record carry it. Cisco says "limited exploitation".
   - Ground truth: The Register 2026-06-15: CISA "added CVE-2026-20262 to its Known Exploited Vulnerabilities catalog, citing 'evidence of active exploitation'"; Cisco: "In June 2026, the Cisco PSIRT became aware of limited exploitation of this vulnerability." (https://www.theregister.com/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916)
   - Fix: Cite The Register or the KEV record for the listing; say Cisco reports limited exploitation.

3. [imprecision] body (vulnerability description)
   - Claim: does not validate the user-supplied filename, so an authenticated request can traverse out of the intended directory ; the file-upload handler fails to validate the supplied filename
   - Defect: The Cisco advisory says "user-supplied input during a file upload process"; filename and directory traversal appear only in Cisco's log sample; the entry cites the NVD per-CVE page as a source.
   - Ground truth: Cisco: "the affected software does not properly validate user-supplied input during a file upload process"; Cisco CNA CWE-22 Path Traversal. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Use Cisco's wording, cite the CNA record for CWE-22, drop the NVD link.

4. [imprecision] cves[CVE-2026-20262]
   - Claim: affected: null; fixed: null
   - Defect: Cisco's table gives the first fixed release per train and the affected status is "regardless of device configuration"; neither is recorded.
   - Ground truth: Cisco: 20.9.9.1 and earlier -> 20.9.9.2; 20.12.7.1 and earlier -> 20.12.7.2; 20.15.4.4 and earlier -> 20.15.4.5; 20.15.5.2 and earlier -> 20.15.5.3; 20.18.3 -> 20.18.3.1; 26.1.1.1 and earlier -> 26.1.1.2. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Fill affected/fixed from the Cisco table. (CVSS 6.5, KEV 2026-06-15 and exploited status are correct.)

5. [factual-error] evidence[0]
   - Claim: quote of entry prose (A: "Vulnerable component."; B: "A path-traversal weakness in the web UI ... (NVD CVSS 6.5; Cisco PSIRT, 2026-06-15).")
   - Defect: The evidence quote is the entry's own migrated prose (publisher "ctipilot v2 brief (migrated)"), not a passage of a cited page.
   - Ground truth: Cisco PSIRT: "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or overwrite any file on the filesystem of an affected system." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Replace with a verbatim Cisco passage.

6. [factual-error] body (exploitation chain)
   - Claim: Reporting describes the practical path as: (1) Initial access with valid low-privilege SD-WAN Manager credentials — obtained through prior phishing, credential reuse, or chaining an earlier auth-affecting SD-WAN bug ... (3) ... because the SD-WAN Manager application services run with high privilege, the web shell yields root-equivalent control
   - Defect: No cited source describes this chain: Cisco says only that the written file "could later be used to elevate to root"; the credential-acquisition routes and the "application services run with high privilege" rationale are the entry's conjecture attributed to "Reporting"; T1078.004 (Cloud Accounts) does not fit appliance credentials.
   - Ground truth: Cisco: "A successful exploit could allow the attacker to create or overwrite any file on the underlying operating system. This file could later be used to elevate to root."; BleepingComputer: "execute arbitrary commands as root". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Attribute only what Cisco/BC state; label the rest analyst inference; use T1078 not .004.

7. [imprecision] body (privilege requirement)
   - Claim: a low-privilege/single-task account ; prune low-privilege/single-task accounts
   - Defect: Cisco's advisory (v1.1) says valid credentials with at least write access; "single-task" is The Register's wording; the entry picks one silently.
   - Ground truth: Cisco v1.1: "Specified write access privilege in Summary"; "the attacker must have valid credentials with at least write access"; The Register: "at least a lower-privileged, single-task user account". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Use Cisco's wording and add a Contradiction line.

8. [imprecision] entities / body (Talos paragraph)
   - Claim: entities: actor:uat-8616 ; Cisco Talos tracks a highly capable cluster it designates UAT-8616 behind a 2026 wave of Cisco Catalyst SD-WAN exploitation
   - Defect: No source ties UAT-8616 to CVE-2026-20262 (Talos covers CVE-2026-20127 on the SD-WAN Controller, published 2026-02-25); the body hedges but the actor entity link on the entry asserts an association.
   - Ground truth: Talos: "Talos is tracking the active exploitation of CVE-2026-20127, a vulnerability in Cisco Catalyst SD-WAN Controller, formerly vSmart". (https://blog.talosintelligence.com/uat-8616-sd-wan/)
   - Fix: Drop the actor entity link or reference the Talos item instead.

9. [imprecision] summary / body
   - Claim: Vulnerable component. (summary field is the first body sentence)
   - Defect: Summary field carries the label "Vulnerable component." sentence rather than a finding summary; no mention of exploitation/KEV.
   - Ground truth: n/a (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Write a real summary.

### 2026-06-16/cve-2026-20262-cisco-catalyst-sd-wan-manager-authenticated-a
Verdict: factual-error (7 defects)

1. [factual-error] body (exploitation / detection / hardening) and actions[0]
   - Claim: write a `.jsp`/`.war` artefact into the Tomcat deployment directory ; newly written files in the Tomcat webapps/deploy directories ; validate the integrity of the Tomcat deploy directory ; the Tomcat deploy directory for planted `.jsp`/`.war` web shells ; Writing a JSP/WAR into the Tomcat deploy path
   - Defect: Cisco's own indicators show a WildFly application server: the malicious WAR is written to /var/lib/wildfly/standalone/deployments/ and deployed by the WildFly DeploymentScanner (WFLYSRV0010). "Tomcat" appears in no source.
   - Ground truth: Cisco PSIRT: vmanage-server.log "SdraAnyConnectFileUploadHandler ... uploaded Remote Access Anyconnect profile file: ../../../../var/lib/wildfly/standalone/deployments/suspicious.war"; vmanage-appserver.log "WFLYSRV0010: Deployed \"suspicious.war\""; serviceproxy-access.log "POST /suspicious/index.jsp". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Replace Tomcat with the WildFly deployments directory and cite Cisco's three log indicators (vmanage-server.log AnyConnect profile-upload handler with ../ path, appserver deployment, service-proxy POST to index.jsp).

2. [imprecision] body (KEV citation)
   - Claim: CISA added CVE-2026-20262 to the Known Exploited Vulnerabilities catalog on 2026-06-15 ([BleepingComputer, 2026-06-15]) ; Cisco confirms active exploitation and CISA added it to the KEV catalog on 2026-06-15 (BleepingComputer)
   - Defect: The fact is true (KEV dateAdded 2026-06-15) but the cited BleepingComputer article does not mention a KEV listing for this CVE; The Register and the KEV record carry it. Cisco says "limited exploitation".
   - Ground truth: The Register 2026-06-15: CISA "added CVE-2026-20262 to its Known Exploited Vulnerabilities catalog, citing 'evidence of active exploitation'"; Cisco: "In June 2026, the Cisco PSIRT became aware of limited exploitation of this vulnerability." (https://www.theregister.com/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916)
   - Fix: Cite The Register or the KEV record for the listing; say Cisco reports limited exploitation.

3. [imprecision] body (vulnerability description)
   - Claim: does not validate the user-supplied filename, so an authenticated request can traverse out of the intended directory ; the file-upload handler fails to validate the supplied filename
   - Defect: The Cisco advisory says "user-supplied input during a file upload process"; filename and directory traversal appear only in Cisco's log sample; the entry cites the NVD per-CVE page as a source.
   - Ground truth: Cisco: "the affected software does not properly validate user-supplied input during a file upload process"; Cisco CNA CWE-22 Path Traversal. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Use Cisco's wording, cite the CNA record for CWE-22, drop the NVD link.

4. [imprecision] cves[CVE-2026-20262]
   - Claim: affected: null; fixed: null
   - Defect: Cisco's table gives the first fixed release per train and the affected status is "regardless of device configuration"; neither is recorded.
   - Ground truth: Cisco: 20.9.9.1 and earlier -> 20.9.9.2; 20.12.7.1 and earlier -> 20.12.7.2; 20.15.4.4 and earlier -> 20.15.4.5; 20.15.5.2 and earlier -> 20.15.5.3; 20.18.3 -> 20.18.3.1; 26.1.1.1 and earlier -> 26.1.1.2. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Fill affected/fixed from the Cisco table. (CVSS 6.5, KEV 2026-06-15 and exploited status are correct.)

5. [factual-error] evidence[0]
   - Claim: quote of entry prose (A: "Vulnerable component."; B: "A path-traversal weakness in the web UI ... (NVD CVSS 6.5; Cisco PSIRT, 2026-06-15).")
   - Defect: The evidence quote is the entry's own migrated prose (publisher "ctipilot v2 brief (migrated)"), not a passage of a cited page.
   - Ground truth: Cisco PSIRT: "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or overwrite any file on the filesystem of an affected system." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Replace with a verbatim Cisco passage.

6. [imprecision] summary / body
   - Claim: Full deep dive in § 5 ; Full kill-chain, hunt and hardening detail in § 5
   - Defect: Dangling references to a section that does not exist in the entry (the deep dive is a separate entry).
   - Ground truth: n/a (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Remove.

7. [imprecision] actions[0]
   - Claim: take the management UI off the internet, enforce MFA
   - Defect: Cisco's advisory says internet-exposed Managers are at risk; MFA is not a sourced control for this flaw (exploit needs valid credentials; MFA does not stop an authenticated upload).
   - Ground truth: Cisco: "Cisco Catalyst SD-WAN Manager systems that are exposed to the internet and that have ports exposed to the internet are at risk"; "There are no workarounds". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ)
   - Fix: Keep the exposure advice; drop or justify MFA.

### 2026-07-01/cve-2026-46817-oracle-e-business-suite-oracle-payments-pre-a
Verdict: factual-error (7 defects)

1. [factual-error] title / headline / summary / body
   - Claim: pre-auth RCE ; unauthenticated remote-code-execution flaw ; unauthenticated RCE in the File Transmission component
   - Defect: No source calls CVE-2026-46817 an RCE: Oracle/BleepingComputer/SecurityAffairs say an unauthenticated attacker can "take over Oracle Payments"; CISA names it "Improper Privilege Management"; the only observed exploitation was an unauthenticated file read.
   - Ground truth: BleepingComputer: "enables unauthenticated malicious actors with HTTP network access to take over vulnerable systems through low-complexity attacks"; Help Net Security (Defused): "a single source running an unauthenticated file-read against the Payments component". (https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)
   - Fix: Say "unauthenticated takeover of Oracle Payments (observed: unauthenticated file read)"; drop "RCE".

2. [factual-error] summary / body
   - Claim: roughly six weeks post-patch ; six weeks after the fix ; Patch-adoption six weeks after the May CPU
   - Defect: The cited BleepingComputer/SecurityAffairs pages do not say "six weeks" (only Defused via Help Net Security does) and it conflicts with Oracle's release date: Oracle published the May 2026 update on 2026-05-28, first exploitation was 2026-06-27 (30 days).
   - Ground truth: Oracle: "2026-May-28 | Rev 1. Initial Release."; Help Net Security quoting Defused: "roughly six weeks after Oracle's May 2026 patch"; BleepingComputer: "Over the weekend, we observed an actor exploiting the vulnerability". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Say about four weeks (Oracle 2026-05-28 to Defused 2026-06-27) or attribute "six weeks" to Defused and flag the discrepancy.

3. [factual-error] body (exploitation status)
   - Claim: Defused did not publicly disclose the technical mechanics ; Because the exploit mechanics are not public
   - Defect: Help Net Security (2026-06-30), quoting Defused's own post, gives the mechanics: unauthenticated file read through the ibytransmit endpoint of the Payments File Transmission component; the 2026-07-16 CISA/KEV follow-up repeats them. (SecurityAffairs' earlier statement was superseded the same day.)
   - Ground truth: Help Net Security: "The exploit targets the ibytransmit endpoint in Oracle Payments' File Transmission component, and calls an internal Oracle Java function directly, redirecting it to read a file (/etc/passwd) from the server." (https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)
   - Fix: State the file-read mechanics and the POST /OA_HTML/ibytransmit detection; drop the "exploit mechanics are not public" reasoning.

4. [imprecision] summary / body / actions / cves[].fixed / sources[] label
   - Claim: May 2026 CPU ; May 2026 Critical Patch Update ; Oracle (Critical Patch Update Advisory, May 2026)
   - Defect: Oracle's advisory is the "Critical Security Patch Update (CSPU) - May 2026", a distinct program from the quarterly Critical Patch Update.
   - Ground truth: Oracle: "Oracle Critical Security Patch Update Advisory - May 2026"; "Critical Security Patch Updates complement Oracle's existing quarterly cumulative Critical Patch Updates (CPUs)"; next dates "16 June 2026 (CSPU), 21 July 2026 (CPU)". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Name it the May 2026 Critical Security Patch Update.

5. [imprecision] cves[CVE-2026-46817].status / affected / fixed
   - Claim: status: exploited, patch-available; affected: null; fixed: null
   - Defect: CISA added the CVE to KEV on 2026-07-15 (status lacks cisa-kev); affected 12.2.3-12.2.15 and the fixing update are not recorded.
   - Ground truth: CISA 2026-07-15: "CVE-2026-46817: Oracle E-Business Suite Improper Privilege Management Vulnerability"; Oracle matrix: Oracle Payments / File Transmission / 12.2.3-12.2.15. (https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)
   - Fix: Add cisa-kev, affected and fixed.

6. [factual-error] evidence[0]
   - Claim: Critical (CVSS 9.8) unauthenticated RCE in the File Transmission component of Oracle Payments ... patched in the May 2026 Critical Patch Update.
   - Defect: The quote is the entry's own migrated prose (publisher "ctipilot v2 brief (migrated)"), not a passage of any cited page.
   - Ground truth: BleepingComputer: "This security flaw was found in the File Transmission component of EBS's Oracle Payments product and enables unauthenticated malicious actors with HTTP network access to take over vulnerable systems through low-complexity attacks." (https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/)
   - Fix: Replace with a verbatim source passage.

7. [imprecision] summary / actions[0] / body
   - Claim: Details in § 5 ; (§ 5) ; Exposure and defender guidance in § 5
   - Defect: Dangling references to a section that does not exist in the entry.
   - Ground truth: n/a (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Remove.

### 2026-07-01/oracle-e-business-suite-cve-2026-46817-pre-auth-rce-in-the-p
Verdict: factual-error (9 defects)

1. [factual-error] title / headline / summary / body
   - Claim: pre-auth RCE ; unauthenticated remote-code-execution flaw ; unauthenticated RCE in the File Transmission component
   - Defect: No source calls CVE-2026-46817 an RCE: Oracle/BleepingComputer/SecurityAffairs say an unauthenticated attacker can "take over Oracle Payments"; CISA names it "Improper Privilege Management"; the only observed exploitation was an unauthenticated file read.
   - Ground truth: BleepingComputer: "enables unauthenticated malicious actors with HTTP network access to take over vulnerable systems through low-complexity attacks"; Help Net Security (Defused): "a single source running an unauthenticated file-read against the Payments component". (https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)
   - Fix: Say "unauthenticated takeover of Oracle Payments (observed: unauthenticated file read)"; drop "RCE".

2. [factual-error] summary / body
   - Claim: roughly six weeks post-patch ; six weeks after the fix ; Patch-adoption six weeks after the May CPU
   - Defect: The cited BleepingComputer/SecurityAffairs pages do not say "six weeks" (only Defused via Help Net Security does) and it conflicts with Oracle's release date: Oracle published the May 2026 update on 2026-05-28, first exploitation was 2026-06-27 (30 days).
   - Ground truth: Oracle: "2026-May-28 | Rev 1. Initial Release."; Help Net Security quoting Defused: "roughly six weeks after Oracle's May 2026 patch"; BleepingComputer: "Over the weekend, we observed an actor exploiting the vulnerability". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Say about four weeks (Oracle 2026-05-28 to Defused 2026-06-27) or attribute "six weeks" to Defused and flag the discrepancy.

3. [factual-error] body (exploitation status)
   - Claim: Defused did not publicly disclose the technical mechanics ; Because the exploit mechanics are not public
   - Defect: Help Net Security (2026-06-30), quoting Defused's own post, gives the mechanics: unauthenticated file read through the ibytransmit endpoint of the Payments File Transmission component; the 2026-07-16 CISA/KEV follow-up repeats them. (SecurityAffairs' earlier statement was superseded the same day.)
   - Ground truth: Help Net Security: "The exploit targets the ibytransmit endpoint in Oracle Payments' File Transmission component, and calls an internal Oracle Java function directly, redirecting it to read a file (/etc/passwd) from the server." (https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)
   - Fix: State the file-read mechanics and the POST /OA_HTML/ibytransmit detection; drop the "exploit mechanics are not public" reasoning.

4. [imprecision] summary / body / actions / cves[].fixed / sources[] label
   - Claim: May 2026 CPU ; May 2026 Critical Patch Update ; Oracle (Critical Patch Update Advisory, May 2026)
   - Defect: Oracle's advisory is the "Critical Security Patch Update (CSPU) - May 2026", a distinct program from the quarterly Critical Patch Update.
   - Ground truth: Oracle: "Oracle Critical Security Patch Update Advisory - May 2026"; "Critical Security Patch Updates complement Oracle's existing quarterly cumulative Critical Patch Updates (CPUs)"; next dates "16 June 2026 (CSPU), 21 July 2026 (CPU)". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Name it the May 2026 Critical Security Patch Update.

5. [imprecision] cves[CVE-2026-46817].status / affected / fixed
   - Claim: status: exploited, patch-available; affected: null; fixed: null
   - Defect: CISA added the CVE to KEV on 2026-07-15 (status lacks cisa-kev); affected 12.2.3-12.2.15 and the fixing update are not recorded.
   - Ground truth: CISA 2026-07-15: "CVE-2026-46817: Oracle E-Business Suite Improper Privilege Management Vulnerability"; Oracle matrix: Oracle Payments / File Transmission / 12.2.3-12.2.15. (https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)
   - Fix: Add cisa-kev, affected and fixed.

6. [factual-error] evidence[0]
   - Claim: What it is.
   - Defect: The quote is the entry's own migrated prose (publisher "ctipilot v2 brief (migrated)"), not a passage of any cited page.
   - Ground truth: BleepingComputer: "This security flaw was found in the File Transmission component of EBS's Oracle Payments product and enables unauthenticated malicious actors with HTTP network access to take over vulnerable systems through low-complexity attacks." (https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/)
   - Fix: Replace with a verbatim source passage.

7. [imprecision] entities / body ("Why this product line")
   - Claim: entities: actor:shinyhunters ; the separate, still-active ShinyHunters Oracle PeopleSoft campaign (CVE-2026-35273) continues to acquire named victims
   - Defect: The body says no named cluster is attributed, yet the frontmatter links actor:shinyhunters; SecurityAffairs only reports a Mandiant/GTIG ShinyHunters PeopleSoft campaign (27 May-9 June) and nothing about continuing victims or any link to CVE-2026-46817.
   - Ground truth: SecurityAffairs: "the activity ran from May 27 to June 9"; "Defused Cyber did not disclose technical details about the attacks ... or the motivation of the attackers." (https://securityaffairs.com/194463/security/attackers-actively-exploit-the-oracle-e-business-suite-flaw-cve-2026-46817.html)
   - Fix: Drop the actor entity link and the "continues to acquire named victims" claim.

8. [imprecision] body (exposure)
   - Claim: EBS Payments/financial modules are common in government, higher-education and large-enterprise finance back offices
   - Defect: Uncited usage-profile claim.
   - Ground truth: BleepingComputer cites only Shadowserver: "over 450 Oracle EBS instances exposed online, with nearly 200 in the United States and in Europe". (https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/)
   - Fix: Cite or drop.

9. [imprecision] headline
   - Claim: Payments File Transmission servlet
   - Defect: "Servlet" appears in no source (sources say component / ibytransmit endpoint).
   - Ground truth: Oracle risk matrix: component "File Transmission"; Help Net Security: "ibytransmit endpoint". (https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/)
   - Fix: Say component/endpoint.

### 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed
Verdict: factual-error (6 defects)

1. [factual-error] body paragraph 2
   - Claim: This is the same EBS product family already under sustained ShinyHunters/UNC6240 extortion pressure
   - Defect: No cited source places ShinyHunters/UNC6240 on Oracle EBS: SecurityAffairs ties ShinyHunters to a PeopleSoft campaign and BleepingComputer ties Clop to EBS CVE-2025-61882 in 2025.
   - Ground truth: SecurityAffairs: "ShinyHunters campaign" against "Oracle PeopleSoft"; BleepingComputer: "The Clop extortion gang exploited another Oracle EBS security flaw (CVE-2025-61882)". (https://securityaffairs.com/194463/security/attackers-actively-exploit-the-oracle-e-business-suite-flaw-cve-2026-46817.html)
   - Fix: Drop the ShinyHunters/UNC6240 claim or cite it; the sourced EBS history is the 2025 Clop campaign.

2. [imprecision] body paragraph 1
   - Claim: Oracle characterises it as improper privilege management, improper authentication and missing authentication for a critical function ... (CVSS 9.8; Oracle CPU, 2026-05-28)
   - Defect: The CWE-style labels are in Help Net Security and the KEV record, not in Oracle's advisory (the risk matrix lists component, protocol, auth, CVSS only).
   - Ground truth: Help Net Security: "caused by improper privilege management, improper authentication, and missing authentication for a critical function"; Oracle matrix row: "CVE-2026-46817 | Oracle Payments | File Transmission | HTTP | Yes | 9.8". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Attribute the labels to Help Net Security/CISA.

3. [imprecision] summary / body paragraph 2
   - Claim: roughly six weeks after the patch
   - Defect: Oracle published the update on 2026-05-28; first exploitation 2026-06-27 is 30 days later; "six weeks" is Defused's wording only.
   - Ground truth: Oracle: "2026-May-28 | Rev 1. Initial Release." (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Say about four weeks or attribute to Defused.

4. [imprecision] summary / actions[0] / cves[].fixed / sources[] label
   - Claim: May 2026 Critical Patch Update ; Oracle (Critical Patch Update Advisory, May 2026)
   - Defect: The advisory is the "Critical Security Patch Update - May 2026" (CSPU).
   - Ground truth: Oracle: "Oracle Critical Security Patch Update Advisory - May 2026". (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Use the correct program name.

5. [imprecision] cves[CVE-2026-46817].type
   - Claim: type: rce
   - Defect: No source states remote code execution; Oracle/CISA say takeover / improper privilege management and the observed activity was an unauthenticated file read.
   - Ground truth: CISA: "Oracle E-Business Suite Improper Privilege Management Vulnerability". (https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)
   - Fix: Use a type matching the sources (auth bypass / privilege management / file read).

6. [imprecision] evidence[2]
   - Claim: CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog, based on evidence of active exploitation.
   - Defect: (low confidence) Page read only through the summarising reader (cisa.gov is walled out); the alert text quoted is consistent but the final words could not be matched verbatim.
   - Ground truth: CISA alert 2026-07-15 (via WebFetch): "CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog, based on evidence of active ..." (truncated by the reader); KEV record agrees. (https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)
   - Fix: None unless a verbatim check fails.
