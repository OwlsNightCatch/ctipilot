---
title: Findings from the $1M Vercel Sandbox challenge
author: Andy Riancho
url: https://vercel.com/blog/findings-from-the-1-million-dollar-vercel-sandbox-challenge
hostname: vercel.com
description: Vercel’s $1M Sandbox challenge drew 1,285 reports, uncovered a Linux kernel zero day, and resulted in $242,000 in bug bounties payouts.
sitename: Vercel
date: "2026-10-14"
fingerprint: bdb38b9ec81f07e1
---
In August, we launched the [$1M hacker challenge for Vercel Sandbox](https://vercel.com/blog/one-million-dollar-hacker-challenge-for-vercel-sandbox), inviting security researchers to try and escape Vercel Sandbox. We also coordinated with cybersecurity experts Trail of Bits to review the source code and security architecture.

Here is a summary of the challenge:

- 1,285 reports over two weeks
- $242,000 in bounties paid out
- One Linux kernel zeroday vulnerability uncovered

No reports showed anyone accessing customer data in Vercel Sandbox. The most severe finding was the defect in the upstream Linux kernel.

## [Copy link to heading](https://vercel.com#the-kernel-zero-day)The kernel zero day

The program's most important report arrived on day three.

[Paulos Yibelo](https://hackerone.com/paulos__?type=user) (pwn.ai), a HackerOne researcher working from a standard sandbox with no special access, found a defect in the Linux kernel's networking stack. Paulos discovered that specially crafted packets sent from within the microVM enabled three different attacks:

1. Leak host memory over the network
2. Crash the host machine
3. Execute code on the host

#### [Copy link to heading](https://vercel.com#leaking-host-memory)Leaking host memory

In the first attack, memory from the host, the machine your sandbox shares with other tenants, shows up in packets the guest sends over the internet. This can happen continuously, for as long as the guest keeps sending.

This attack was demonstrated against Vercel production sandboxes.

#### [Copy link to heading](https://vercel.com#crashing-the-host-and-executing-code-on-the-host)Crashing the host and executing code on the host

The researcher also found that by sending specific packets, they could compromise the host.

First, by sending two packets, the researcher crashed the host machine, shutting down every sandbox running on it. Second, using the same flaw, they were able to run commands with full administrator privileges on the host, breaking out of the sandbox’s isolation boundary.

The packet-related crash and code execution attacks were demonstrated on the researcher’s own KVM and Firecracker machines matching Vercel Sandbox configuration.

### [Copy link to heading](https://vercel.com#responsibly-disclosing-the-kernel-vulnerability)Responsibly disclosing the kernel vulnerability

Almost every major cloud provider isolates customer workloads on this same layer of the Linux kernel, so any defect is shared-infrastructure risk.

Immediately after being notified, we collaborated with the researcher to understand and mitigate the vulnerability, working with AWS and other industry partners to prioritize a fix, and ensuring that Vercel customers and other developers using the kernel were safe.

The researcher also contacted the kernel maintainers and worked with them to create candidate patches. Fixes are under private review and CVEs are pending, so we are not publishing additional details until the patches are public. We are disclosing the existence of the vulnerability because it was separately disclosed in public.

## [Copy link to heading](https://vercel.com#our-approach-to-pressure-testing-vercel-sandbox)Our approach to pressure-testing Vercel Sandbox

The HackerOne challenge made bounties available to any researcher, but we also extended our program to include internal evaluations and an independent investigation.

Before launching the public bounty, we performed live security assessments internally with full source access and support from the engineers who created and maintain Vercel Sandbox. We also engaged Trail of Bits, bringing on two engineers to evaluate our security architecture.

Not every finding came from the outside. Marcos Hernanz, a Vercel intern, found a cross-tenant data leak in the Linux device-mapper storage layer. This vulnerability let any sandbox read recycled disk blocks from previously deleted sandboxes.

## [Copy link to heading](https://vercel.com#the-white-box-deep-dive)The white-box deep dive

Trail of Bits spent four engineer-weeks inside our source code, with full access to the repositories and two enterprise test teams. They delivered 20 findings, and each was tested, confirmed, and referenced to the exact code.

They also performed an architectural review and concluded that our virtualization boundary is sound. Each sandbox runs on its own Firecracker microVM with a dedicated guest kernel, and the device model is deliberately tiny. No guest shares a running kernel with the host, or with another tenant.

On top of that foundation, they gave us three structural recommendations, which we implemented:

- **Find and eliminate all trust in the guest.** Our control plane accepted values returned by software running inside the microVM, and every one of those values is tenant input. Anything that crosses the boundary should be derived server-side or signed with a key the guest cannot reach.
- **One policy, one decider.** Egress enforcement was split across subsystems that each parsed the same network policy independently, and they did not always agree. We now use one canonicalization routine per data type, one component per decision, and revalidate connections when policy changes.
- **Assume the next zero day.** We strengthened the protections around each sandbox to limit the damage if an attacker exploits the virtualization software. We keep host kernels up to date, have disabled nested virtualization, and use Firecracker’s jailer to run each microVM process with restricted permissions and isolate it from the rest of the host.

## [Copy link to heading](https://vercel.com#vercel-sandbox-findings)Vercel Sandbox findings

We received 1,285 reports in two weeks. This volume is only possible because researchers now hunt at AI speed.

Here is a breakdown of reports by category:

- 877 duplicates
- 319 not applicable
- 57 valid
- 32 informative

In our report triage we have validated:

- 1 Critical finding
- 5 High findings
- 9 Medium findings
- 42 Low findings
- 32 Informative findings

We have paid out $242,000 in bug bounties.

The medium, Low, and Informative findings are small policy-boundary gaps, like a firewall rule that behaved differently than documented and a field that trusted the guest more than it should.

The most severe finding was the Linux kernel zero day defect, and no reports showed anyone reading a customer’s files, secrets, or application data.

We were most impressed with the heterogeneity of the reports. It was clear that researchers used different setups and have different obsessions. Some clearly know Linux namespaces and steered their agents straight at the kernel boundary. Others went after the network policies, and many went after areas we didn’t think to put on the menu.

That variety is what you're funding with a public challenge. Here's one of the more interesting findings it produced.

### [Copy link to heading](<https://vercel.com#cross-tenant-disk-snapshot-restore-(with-limits)>)Cross-tenant disk snapshot restore (with limits)

Filed on day one of the challenge, this report is our favorite example of why we run a public bug bounty, even after internal assessments and a white-box engagement.

When you snapshot a sandbox, the control plane has to record where the snapshot data landed: `{storage_url, size, checksum}`. The flaw the researcher found was subtle: that answer came from software running inside the guest, and services running on the host trusted it. That is a trust-boundary violation. The guest is where our customers (and hackers) run untrusted code, so the host can never take its word as authoritative.

The researcher combined a known, documented container-escape primitive with this trust flaw. They intercepted the snapshot response inside their own sandbox and rewrote it, swapping the storage objects of two snapshots belonging to two separate accounts they owned. That meant restoring "your" snapshot materialized the other account's entire filesystem.

The researcher demonstrated that each account could read and modify the other’s files, verified the results using hashes, and preserved the test resources so we could independently reproduce the findings.

The limits of this attack matter. Aiming the swap at a specific victim required knowing that victim's internal snapshot storage key, a random 96-bit identifier the platform generates per snapshot and never exposes through the API. The only place that key appears is inside the victim's own sandbox. The researcher owned both accounts, which is what made the proof possible; there was no demonstrated path for a stranger to target another tenant. We still treated it as a priority fix, because a boundary that depends on a secret staying secret is not a boundary.

Trail of Bits independently flagged the same root cause in their assessment, which told us the finding was real, important, and discoverable from two completely different angles.

The fix shipped within a week, and the control plane now binds every snapshot object to the project that created it and rejects anything else. Snapshot creation moved out of the guest-reachable environment into a host-side service, and storage paths are project-scoped with strictly validated URLs.

## [Copy link to heading](https://vercel.com#thank-you-to-the-research-community)Thank you to the research community

We would like to thank every researcher who filed a report, whether their finding was a zero day or a duplicate. Every technique discovered in the challenge informs how we protect the workloads running on Vercel Sandbox.

Thank you also to Trail of Bits for your comprehensive internal investigation and guidance.

Read the [original challenge announcement](https://vercel.com/blog/one-million-dollar-hacker-challenge-for-vercel-sandbox) and learn more about Vercel Sandbox in [the documentation](https://vercel.com/docs/sandbox).
