---
title: PolinRider Loader Reappears in Hijacked npm Packages
author: Sonatype Research Team
url: https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages
hostname: sonatype.com
description: Hijacked npm packages contain PolinRider loaders that use Ethereum transactions to locate and execute remote payloads. Learn how to identify exposure.
sitename: Sonatype
date: "2026-11-04"
fingerprint: "3444535780b60768"
---
# PolinRider Loader Reappears in Hijacked npm Packages

10 minute read time

## TL;DR

- [Sonatype Research Labs](https://www.sonatype.com/sonatype-research-labs) identified concealed runtime loaders in 12 npm releases across 10 hijacked packages.
- All 12 releases contain loaders designed to decode payload-server IP addresses from Ethereum transactions sent by the same hard-coded wallet previously reported in PolinRider activity, then retrieve, XOR-decode, and execute JavaScript. Six conceal the loader in eval(atob(...)); six use a character-permutation bootstrap and the JavaScript Function constructor.
- The manifests show no consumer install or postinstall hooks. The code can run when an affected entrypoint is loaded or, for server-hemera-mongo, when the bundled application starts.
- Check direct and transitive dependencies, lockfiles, internal npm mirrors, and build records. If affected code ran, treat the host as compromised and investigate its processes, network activity, and accessible credentials.

## Hidden Loaders Found in 12 npm Releases

On November 4, 2026, Sonatype Research Labs investigated [malicious runtime loaders in npm packages](https://guide.sonatype.com/security-event/b96b3873-a726-4723-b850-de24916452b7) and confirmed 12 affected releases across 10 hijacked packages. The examined releases contain two loader variants that use the same Ethereum sender wallet and payload-retrieval infrastructure. Sonatype tracks the finding as [sonatype-2026-010515](https://guide.sonatype.com/vulnerability/sonatype-2026-010515/sonatype-research).

The affected packages support unrelated developer functions, from Redux integration and health APIs to browser activity tracking, utilities, and server examples. Their shared issue is concealed behavior embedded in code that otherwise serves those ordinary purposes.

These releases don't rely on a consumer-side installation script to activate that behavior. An application can reach the code when it loads an affected package; the server-hemera-mongo releases run it as the service starts.

| **Package** | **Affected Releases** | **Observed Behavior** | 
| @adminide-stack/client-redux | 0.0.16-18 | Ethereum-based loader concealed by Base64 | 
| @adminide-stack/health-api-server | 0.0.18-alpha.465 | Ethereum-based loader concealed by Base64 | 
| @adminide-stack/user-activity-browser | 1.1.3-alpha.114 | Ethereum-based loader concealed by Base64 | 
| @adminide-stack/utils | 0.0.16-129, 0.0.16-130 | Ethereum-based loader concealed by Base64 in 0.0.16-129 and a character-permutation bootstrap in 0.0.16-130 | 
| server-hemera-mongo | 0.0.15, 0.0.16 | Ethereum-based loader concealed by Base64 | 
| cdeops | 13.5.31 | Ethereum-based loader concealed by a character-permutation bootstrap | 
| @adminide-stack/forms-core | 5.1.9-alpha.3 | Ethereum-based loader concealed by a character-permutation bootstrap | 
| @adminide-stack/yantra-help-browser | 12.0.194 | Ethereum-based loader concealed by a character-permutation bootstrap | 
| @cdmbase/wiki-browser | 12.0.18-alpha.53 | Ethereum-based loader concealed by a character-permutation bootstrap | 
| @pubngo-stack/help-browser | 12.0.23-alpha.3 | Ethereum-based loader concealed by a character-permutation bootstrap | 

## The Shared Loader Uses Ethereum Transactions to Find Remote Code

All 12 releases contain loaders designed to query public Ethereum RPC endpoints, with a Blockscout API fallback, to locate a transaction sent by the hard-coded wallet 0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3. The loader interprets the first four bytes of the transaction's recipient address as a primary IPv4 address and the next four as a secondary address. It retrieves XOR-encoded JavaScript from the primary address over plain HTTP on TCP port 443, using the paths /0x/cls and /0x/ls.

After XOR-decoding the responses, the loader passes the JavaScript retrieved from /0x/cls to eval in the application process and to a detached node -i process through piped standard input. The JavaScript retrieved from /0x/ls is passed only to a detached node -i process. The child processes are unreferenced, allowing them to continue independently of the application process.

The Ethereum wallet acts as a dead-drop resolver: the operator can advertise a new payload-server IP address by sending another transaction without updating the malicious packages. Blocking an individual server therefore does not disable the loader's ability to discover a replacement.

## Six Releases Conceal the Ethereum Loader With a Different Bootstrap

Six releases use a character-permutation bootstrap designed to reconstruct and execute an Ethereum-based loader: @adminide-stack/utils@0.0.16-130, cdeops@13.5.31, @adminide-stack/forms-core@5.1.9-alpha.3, @adminide-stack/yantra-help-browser@12.0.194, @cdmbase/wiki-browser@12.0.18-alpha.53, and @pubngo-stack/help-browser@12.0.23-alpha.3. The decoded loader bodies recovered from these six releases are byte-identical. They differ from the loader in the six Base64-wrapped releases but use the same Ethereum wallet, retrieval paths, and XOR keys.

- In utils@0.0.16-130, an obfuscated routine follows the package's logger code. It permutes and decodes an embedded blob, obtains the JavaScript Function constructor indirectly, and executes the decoded content.
- In cdeops@13.5.31, an obfuscated bootstrap appears in client.js before the module's normal delegation to global.require('cdeops/client'). It decodes embedded content and executes it dynamically, then continues to the expected client delegation. The hidden execution is separate from the documented purpose of that shim.

## Shared Wallet and C2 Infrastructure Link the Releases to PolinRider

Sonatype Research Labs independently decoded the loaders in all 12 releases and recovered the same hard-coded Ethereum sender wallet, 0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3. This exact wallet appears in GitGuardian's October 27, 2026 report, "[GhostAction Crosses Paths With PolinRider: Inside the October Escalation](https://blog.gitguardian.com/ghostaction-x-polinrider/?utm_source=chatgpt.com)," where it is identified as the Ethereum resolver used by PolinRider loaders found in compromised GitHub repositories. Those earlier loaders also retrieved stages from /0x/cls and /0x/ls on port 443, matching the retrieval paths and port in the npm samples.

The connection extends to the payload-server infrastructure. Greenflagged's [analysis of these npm releases](https://blog.greenflagged.dev/posts/2026-11-03-adminide-stack-eth-dead-drop/) decoded transactions from that wallet and reported 95.135.181.151 as the advertised C2 address at its November 3 observation. GitGuardian had already listed the same IP on port 443 as a fallback C2 in a PolinRider persistence script. The exact wallet match, overlapping server infrastructure, and matching stage-retrieval paths support linking these malicious npm releases to [previously documented PolinRider activity](https://www.sonatype.com/blog/hijacked-npm-package-attempts-to-deliver-polinrider-linked-rat). This connection does not depend solely on similarities in obfuscation, and it does not definitively establish that PolinRider and GhostAction share an operator.

## The Malicious Code Doesn't Wait for an Install Hook

The package manifests show no consumer install or postinstall hooks. Execution occurs when the runtime reaches an injected JavaScript file. For example, require('cdeops/client') selects the affected client.js, while the package's ES module import maps to a separate client.mjs file. In server-hemera-mongo, the injection is in dist/main.js, the application bundle referenced by its start script.

Assess exposure by correlating dependency records with execution evidence. Lockfiles identify resolved dependency versions, while cached artifacts and download logs help trace package acquisition. Build commands, application configuration, process telemetry, and runtime logs help establish whether an injected JavaScript file was executed.

Disabling npm install scripts does not address code that runs during module loading or application startup. The relevant question is whether the affected package code ran in a developer environment, CI worker, build host, or deployed service.

## What Teams Should Do Now

Organizations should take these steps to identify affected systems and limit further exposure:

- **Find affected versions**: Check direct and transitive dependencies, package-lock.json, yarn.lock, pnpm-lock.yaml, internal npm mirrors, caches, build records, and artifact metadata.
- **Evaluate repository protections**: Determine whether your repository manager or dependency firewall blocked these releases before they reached developers or build systems. Review download and policy logs to identify any deliveries, and ensure all eight versions are blocked from future use.
- **Remove affected dependencies**: Replace affected versions in projects and prevent internal mirrors and caches from serving them. Preserve copies needed for investigation, and use replacement versions that have been independently verified as clean.
- **Determine whether the code ran**: Check which entrypoint the application loaded and whether the runtime could execute the injected code. Correlate this with process and network activity. A lockfile entry does not prove the malicious code ran, and an import error does not prove it didn’t. The import may have failed after the injected code executed.
- **Investigate affected hosts**: If the code ran, treat the host as compromised. Look for detached node -i processes launched by another Node process with piped standard input, and plain HTTP requests to TCP port 443 using /0x/cls or /0x/ls. Payload requests carry a Sec-V header containing A10-npm\_inject in the six Base64-wrapped releases, A10-II in utils@0.0.16-130, or A10-E in cdeops@13.5.31. Use these indicators alongside process ancestry, timestamps, and dependency records to identify affected systems.
- **Assess access and rotate credentials**: Identify the credentials and systems available to the affected process. Rotate credentials where exposure is possible, including publishing credentials, source repository access, cloud keys, and CI secrets.

The operator can change the remotely served JavaScript without publishing another npm release. Use available process, network, build, and runtime records to determine what affected systems executed and which credentials and resources those processes could access.

For ongoing details and response guidance, see the [Sonatype Security Event](https://guide.sonatype.com/security-event/b96b3873-a726-4723-b850-de24916452b7) and [Sonatype Guide research](https://guide.sonatype.com/vulnerability/sonatype-2026-010515/sonatype-research).

*Thanks to Sonatype Research Labs' Adam Reynolds for analysis of the affected npm releases and their PolinRider activity. Connect with Adam on LinkedIn.*

Written by **Sonatype Research Team**

Sonatype's Research Team is focused on bringing real-time, in-depth intelligence and actionable information about open source and third party vulnerabilities to Sonatype customers.

[Explore All Posts by Sonatype Research Team](https://www.sonatype.com/blog/author/sonatype-security-research-team)

Tags
