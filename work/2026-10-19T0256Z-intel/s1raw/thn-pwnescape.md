---
title: Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory
author: The Hacker News
url: https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html
hostname: thehackernews.com
description: A critical Linux kernel flaw let a guest VM read host memory in Vercel's live sandboxes; host code execution was shown only in lab tests.
sitename: The Hacker News
date: "2026-10-16"
categories: ['Article']
fingerprint: "1fb3519acc314626"
---
A newly disclosed critical flaw in the Linux kernel allows code inside a virtual machine to read memory on the host computer it runs on. A researcher demonstrated the leak against Vercel's live cloud sandboxes, and Vercel confirmed it.

The flaw, now tracked as **CVE-2026-99999** and nicknamed **PwnEscape**, is in the Linux kernel's networking code, not in any one cloud's setup, so it reaches the shared layer that cloud providers use to keep customers' workloads apart.

It was found in a Vercel security challenge and reported privately before any public release, and there is no sign it has been used in a real attack.

### What the Researcher Showed

Paulos Yibelo of the security firm pwn.ai found that specially made network packets sent from inside a virtual machine could do three things, he explained in a [technical write-up](https://pwn.ai/blog/pwnescape): read the host's memory, crash the host, and run code on it. All three come from the same kernel flaw.

Vercel said in its [report on the challenge](https://vercel.com/blog/findings-from-the-1-million-dollar-vercel-sandbox-challenge) that the memory leak was demonstrated against its production sandboxes. Each packet the guest sent out could carry back about 32 bytes of the host's memory, and the guest could keep going as long as it kept sending packets.

The crash and code execution were observed only on the researcher's own machines, which were set up to match Vercel's. Two specially crafted packets were enough to crash a host and take down every sandbox running on it.

Using the same flaw, the researcher then reached administrator control of a host, breaking out of the virtual machine. He stressed this was a lab result, "not a claim of root command execution in any vendor's production environment."


"Our research ran through **Omega-Pwn**, an internal harness combining our own security research tooling with elements of [SingularityNET's OmegaClaw architecture](https://github.com/asi-alliance/OmegaClaw-Core). It let us carry hypotheses, code traces, failed attempts, and experimental results across long-running research sessions. **GPT-5.6 Sol** was the primary reasoning engine. We directed the investigation, challenged its findings, and validated the interesting ones against actual kernel behavior on systems we controlled," Paulos Yibelo told The Hacker News.

Vercel said no report in the challenge showed anyone reading a customer's files, secrets, or application data.

### How Severe It Is, and Who Can Set It Off

The kernel's maintainers assigned the flaw [CVE-2026-99999](https://nvd.nist.gov/vuln/detail/CVE-2026-99999) and, in the published record, rated it 9.3 out of 10, or Critical. The U.S. National Vulnerability Database had received that entry but had not yet finished its own review.

The same record lists the attack vector as local. In plain terms, the attacker has to already be running code inside a guest, as the researcher was. This is not a flaw that an outsider can exploit by sending packets across the open internet.

It is not in CISA's catalog of actively exploited vulnerabilities, and no real-world use has been reported.

### Why It Reaches Beyond Vercel

Vercel Sandbox runs each customer's code in its own Firecracker microVM, a small virtual machine with its own copy of the Linux kernel, on bare-metal Amazon EC2 hosts. That microVM is the wall between one customer and the host, and between one customer and another.

The flaw is not in that wall. It is in the Linux kernel's networking code, which the host runs. pwn.ai said Vercel's sandbox was already hardened beyond normal industry standards, with no misconfiguration it could find.

Because almost every large cloud separates customer workloads on the same layer of the Linux kernel, Vercel said that a flaw there poses a risk to shared infrastructure rather than to any one provider.

### The Fix and the Fixed Versions

The fix is a single Linux kernel change, [commit 6785011f8b16](https://github.com/torvalds/linux/commit/6785011f8b16abf40b1e9d8b2e332232b3e68822), written by Red Hat's Michael S. Tsirkin and merged into the mainline kernel. It adds a check that a packet's checksum data cannot point into the IPv4 header before the kernel acts on it, and applies that check at five places in the networking code.

The change is deliberately partial. Its author calls it "a defence in depth measure" and notes that a fuller check on the way packets enter the kernel still needs work.

The maintainers backported the fix to the stable kernel branches. According to the CVE record, these are the first fixed versions in each supported branch:

| Stable branch | First fixed version | 
|---|---|
| 5.10 | 5.10.272 | 
| 5.15 | 5.15.223 | 
| 6.1 | 6.1.190 | 
| 6.6 | 6.6.159 | 
| 6.12 | 6.12.113 | 
| 6.18 | 6.18.57 | 
| 7.2 | 7.2.11 | 

Linux distributions ship their own kernels and often add this kind of fix without changing the version number, so check your distribution's advisory and whether the fix is in the kernel the host is actually running, not only the number from uname.

### What to Do

Update the host kernel to one of the fixed versions above, or to the vendor build that includes the fix, and reboot into it. Updating only a guest's kernel does not fix the host. The sources give no separate workaround for this flaw if you cannot update yet.

Where patching has to wait, the usual step is to limit what a break-in could reach. Vercel said it keeps host kernels up to date, disables nested virtualization, and runs each microVM under Firecracker's jailer, which grants the microVM process only the permissions it needs. That does not fix the flaw, but it narrows what an attacker who used it could do.

### Found in a $1 Million Challenge

The flaw was found in a two-week challenge Vercel ran in August that [offered up to $1 million in total](https://vercel.com/blog/one-million-dollar-hacker-challenge-for-vercel-sandbox) to anyone who could break out of its sandbox. No single payout reached that figure. The top reward per report was $50,000; Vercel paid $242,000 across 1,285 reports, and this flaw was the one Critical finding.

pwn.ai said it found the flaw in three days using its own AI-assisted research system, with the model doing the source-code analysis and human researchers directing the work. The firm put the cost at under $700 in API tokens. It was the latest case of researchers using a large language model to help find and chain real flaws, after a separate team used one [earlier this year to reach internal systems at OpenAI](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html).

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
