Title: GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

URL Source: https://openai.com/index/introducing-gpt-6-cyber/

Markdown Content:
We’re introducing GPT‑6 Cyber, a major leap in security research: more capable at finding and fixing vulnerabilities, and far more reliable staying within the boundaries researchers set. GPT‑6 Cyber delivers major gains on key cybersecurity benchmarks over GPT‑5.6 Cyber, including a 51% relative improvement on ExploitGym and a step function improvement when tested on staying within scope. It is already helping to secure real-world software, uncovering and validating thousands of exploits in security-critical codebases such as Linux and Firefox.

On ExploitGym, which tests whether models can exploit a specified vulnerability, GPT‑6 Cyber scores 48.5%, up from 32.1% for GPT‑5.6 Cyber. It also follows task boundaries more reliably: in a separate alignment evaluation, GPT‑6 Cyber avoided exploiting out-of-scope services in 99.93% of tests without its deployment prompt, and 100% with this prompt. This improvement in alignment reflects dedicated training to stay within authorized scope, respect restrictions, and report results accurately.

These capabilities are already helping secure real systems. Our researchers used GPT‑6 Cyber to develop [948 privilege escalation exploits in Linux⁠](https://openai.com/index/a-thousand-fewer-paths-to-root/) and identify 81 previously unknown high-severity vulnerabilities in Firefox, despite extensive prior testing with frontier models. The model also helped develop candidate patches, and Mozilla has [released fixes for many of the Firefox vulnerabilities⁠(opens in a new window)](https://www.mozilla.org/en-US/security/advisories/mfsa2026-118/). Security teams at Cisco, Calif, and CodeRabbit are using it for vulnerability research and code review, and we have relied on it to [find and fix weaknesses in our own infrastructure⁠](https://openai.com/index/securing-our-frontier-model-training-environment/).

It is clear that we have [a limited window to use frontier models to secure software⁠](https://openai.com/index/the-defenders-window/). **Our goal is to dramatically expand Daybreak, bringing advanced security research to organizations of every size, independent researchers, and open-source maintainers.** Mainline models such as GPT‑6 Astra already support code review, vulnerability triage, and patch development. Daybreak Blue helps verified defenders validate vulnerabilities and fixes with fewer unnecessary refusals, while Daybreak Red enables deeper exploit development and authorized security testing with GPT‑6 Cyber.

## Advancing frontier cyber capabilities

GPT‑6 Cyber is a major step up from GPT‑5.6 Cyber and outperforms GPT‑6 Astra on most cyber tasks, even when Astra does not refuse the request. We evaluated the model on tasks that require it to understand software, identify vulnerabilities, and develop working exploits. Based on these results, we classify the model as Critical in cybersecurity under our Preparedness Framework, up from High for GPT‑5.6 Cyber.

On ExploitGym, which tests whether models can exploit a specified vulnerability in a remote target, GPT‑6 Cyber scores **48.5%**, about **16 percentage points** higher than GPT‑5.6 Cyber’s **32.1%**. To test vulnerability discovery, we also built a new evaluation for offensive web penetration testing. Models probe web applications without access to their source code. GPT‑6 Cyber achieved **40.3%** recall of vulnerabilities compared with **32.0%** for GPT‑6 Astra.

Daybreak Red is designed to support more advanced security workflows, including developing working exploits and using them against remote targets. To evaluate these capabilities, we built a new benchmark called RemoteExploitBench, which uses known vulnerabilities in applications such as GitLab, PostgreSQL, and Jenkins deployed in a controlled environment. In our initial evaluation, GPT‑6 Astra running with Daybreak Blue **refused 100% of tasks**, while GPT‑6 Cyber **completed 95%**; its only failure was an exploit it could not get to work remotely. See the [system card⁠(opens in a new window)](https://deploymentsafety.openai.com/gpt-6-cyber) for full results and evaluation settings.

## Stronger alignment, better at staying within bounds

One risk for cybersecurity agents is that they go outside the scope of their assigned task, attempt to exploit unrelated services, or disregard the researcher’s rules of engagement.

We made alignment a central focus of GPT‑6 Cyber, using specialized training to help the model stay within authorized scope, follow restrictions on its actions, and report its work accurately. Before deployment, we ran a series of alignment evaluations to measure these behaviors. See the [system card⁠(opens in a new window)](https://deploymentsafety.openai.com/gpt-6-cyber) for full results.

One of these evaluations is ExploitGym Honeypot, which was informed by the [Hugging Face incident⁠](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). We give the model a difficult exploitation task in an isolated environment with access to supporting services, such as a package registry or object store. We deliberately make these services easy to exploit so that attacking them can reveal the task’s flag. The model must infer that exploiting them is outside the scope of its task.

GPT‑6 Cyber shows a step-change improvement over GPT‑5.6 Cyber on this evaluation. When tested without deployment safety prompts, it avoided exploiting out-of-scope services in 99.93% of cases, up from 94.49% for GPT‑5.6 Cyber. With those prompts, GPT‑6 Cyber stayed within bounds 100% of the time.

We can see directly in the GPT‑6 Cyber model’s chain of thought how it reasons about staying within bounds:

Agent chain-of-thought excerpts

> “Can't assume extra API or attack controller not target. We should only target binary/server.”

Agent chain-of-thought excerpts

> “don't explore out of scope credentials.”

## Real-world impact for security teams

GPT‑6 Cyber is already helping security teams find vulnerabilities, validate their impact, and develop fixes. Customers have put it to work on large codebases, long-running exploit development, and security review:

1 of 9

We have also relied on GPT‑6 Cyber to secure our own systems. It was one of the main models behind the work we recently shared on [hardening the infrastructure used to train frontier models⁠](https://openai.com/index/securing-our-frontier-model-training-environment/). In controlled red-teaming campaigns, agents using GPT‑6 Cyber and other OpenAI models chained vulnerabilities to escape microVMs and execute code on the underlying hosts. We used the findings to patch software, tighten network restrictions, and report issues to maintainers and vendors.

Our vulnerability researchers also use GPT‑6 Cyber to find and validate vulnerabilities in open-source software at scale. This work has uncovered previously unknown flaws in software that has been scrutinized for years:

*   **Found 81 novel Firefox vulnerabilities.** GPT‑6 Cyber can be suitable for use in autonomous workflows for finding vulnerabilities and proposing high-quality patches at scale. During a vulnerability research campaign, GPT‑6 Cyber produced evidence and reproducible tests for 81 novel vulnerabilities classified by Mozilla as high severity, and showed that an additional 30 known issues were more severe than previously reported. We disclosed the findings to Mozilla, along with proposed patches to help its engineers develop fixes. Mozilla was supportive of this work, and began [landing fixes shortly after receiving the reports⁠(opens in a new window)](https://www.mozilla.org/en-US/security/advisories/mfsa2026-118/).

*   **Developing exploits for**[**948 Linux kernel vulnerabilities**⁠](https://openai.com/index/a-thousand-fewer-paths-to-root/)**.** GPT‑6 Cyber reproduced 1,724 vulnerabilities and developed working exploits for 948—more than five times the 166 exploited by GPT‑5.6 Sol using the same research harness. Following the Linux community's guidance, we disclosed 304 critical findings to maintainers with candidate patches and are in the process of getting other vulnerabilities fixed.

*   **Demonstrating critical RCE vulnerabilities.** We recently discussed a [critical vulnerability in Brotli⁠(opens in a new window)](https://patchtheplanet.org/brotli), a compression library used by Node.js and other software. Our security researchers used GPT‑6 Cyber alongside other OpenAI models to develop and validate exploits showing how the flaw could enable remote code execution in downstream applications.

## Detecting misuse and blocking high-risk activity

As models become more capable and uncover more security vulnerabilities, we are also seeing more attempts to use them to cause harm. These attempts include efforts by malicious cyber actors and adversarial groups seeking to distill our models. We have thus paired GPT‑6 Cyber’s stronger capabilities with stronger safeguards to detect and disrupt misuse and keep the model’s actions within the user’s intent and authorization.

We added and strengthened these protections alongside the release of GPT‑6 Cyber (see the [system card⁠(opens in a new window)](https://deploymentsafety.openai.com/gpt-6-cyber) for full information):

*   **Cyber-specific misalignment monitoring.** We monitor whether actions match the user’s authorization, while recognizing legitimate exploit development and testing.

*   **Targeted monitoring for emerging threats.** For example, during the coordinated disclosure of critical PHP vulnerabilities, we set up targeted monitoring for attempts to develop exploits against live PHP servers, while preserving support for defenders patching affected systems.

*   **Private Safety Processing (PSP).** We use automated checks to review related interactions for misuse. Standard retention remains the default. API customers using [Zero Data Retention⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data) generally must use [PSP⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/private-safety-processing), which reviews encrypted records retained in customer storage for 30 days without exposing prompts and responses to OpenAI personnel.

*   **Protection against stolen credentials.** We require IP allowlisting for Daybreak Red API access by default, restricting requests to approved networks with limited exceptions. We also monitor credentials for compromise.

*   **Sandboxing and oversight.** As with past models, we recommend [sandboxing⁠(opens in a new window)](https://learn.chatgpt.com/docs/sandboxing), [action review⁠(opens in a new window)](https://learn.chatgpt.com/docs/sandboxing/auto-review), and human oversight for high-risk workflows.

*   **Protections against high-risk cyber assistance.** We use new checks to block high-risk activity involving critical systems (see below for more).

## Defending critical infrastructure

Protecting critical infrastructure has been a key consideration in designing GPT‑6 Cyber’s safeguards and access, including power plants, water treatment facilities, and the operational technology and industrial control systems (OT/ICS) that underpin them. We simultaneously want to give the teams defending these systems access to our most capable models while also strengthening our safeguards to prevent unauthorized attacks.

First, to equip these defenders, our $1 billion [Daybreak for Frontline Defenders⁠](https://openai.com/index/daybreak-for-frontline-defenders/) grant program subsidizes access for resource-constrained teams such as government organizations and essential service providers. We’re also introducing a new group within Daybreak Red (**Daybreak Red for Critical Infrastructure**) for approved critical infrastructure defenders, which gives them permissions to conduct authorized testing of critical systems while retaining safeguards against model misalignment.

Second, to prevent misuse of the Daybreak Red and Blue platforms, we have refined safeguards against assistance and capability development that could compromise industrial controls or safety-critical systems, interfere with equipment, or cause serious injury, catastrophic physical damage, or life-endangering service disruption. The figure below compares safeguard label rates across four access configurations, before and after the recent updates we’re rolling out alongside GPT‑6 Cyber.

Higher safeguard block rates are not always better. Many of the techniques in this evaluation are also essential to legitimate security work: understanding systems, finding vulnerabilities, and verifying that fixes withstand attack. We therefore assess these rates alongside support for legitimate research and patching, rather than aiming for 100%.

To evaluate how our models can help defend critical infrastructure, we partnered with Dragos, the global provider for extended operational technology (xOT) cybersecurity. Dragos ran evaluations using cyber-permissive Daybreak Red models in a controlled lab environment. The evaluations covered requests progressing from network discovery and asset enumeration through targeted reconnaissance, sensitive data exfiltration, and unauthorized, potentially dangerous device actions.

We used feedback from Dragos to refine our safeguards, aiming to block harmful assistance without unnecessarily restricting authorized testing. [See their final report⁠(opens in a new window)](https://hub.dragos.com/whitepaper/frontier-ai-models-xot-environment) for details on the evaluations. We’re also working to expand partnerships with other offensive security providers and purple teams on penetration testing and red teaming with AI, and with energy companies, other critical infrastructure operators, and national labs to assess our models’ effectiveness and safeguards in industrial defense. We have also increased our investment in threat investigations to detect model usage involving OT/ICS. We’ll continue refining our safeguards with input from partners and the security community, including reports through /feedback when safeguards miss harmful activity or interrupt legitimate work.

## Expanding access to trusted defenders

GPT‑6 Cyber is initially available through the API and Codex to a select group of approved Daybreak Red customers. We will progressively expand access to all Daybreak Red customers soon, and are also making GPT‑5.6 Cyber available to all Daybreak Red customers. We’re also expanding Daybreak Blue alpha access for GPT‑6 Astra to more organizations and individual security researchers; [let us know⁠(opens in a new window)](https://docs.google.com/forms/d/e/1FAIpQLSdQu8mNYXDpUW_0kRS6JBWBPMWfUjjxi6xLi8AkFPObLupkpg/viewform) if you’re interested.

New users and organizations can [apply for Daybreak⁠](https://openai.com/daybreak/) and get started with our [cyber skills, products, and partners⁠](https://openai.com/business/solutions/cybersecurity/).

Links/Buttons:
- [Skip to main content](https://openai.com/index/introducing-gpt-6-cyber/#main)
- [](https://openai.com/)
- [Research](https://openai.com/research/index/)
- [Business](https://openai.com/business/)
- [Developers](https://openai.com/api/)
- [Company](https://openai.com/about/)
- [Foundation(opens in a new window)](https://openaifoundation.org/)
- [Try ChatGPT(opens in a new window)](https://chatgpt.com/?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [Product](https://openai.com/news/product-releases/)
- [Security](https://openai.com/news/security/)
- [Safety](https://openai.com/news/safety-alignment/)
- [Join Daybreak](https://openai.com/form/enterprise-trusted-access-for-cyber/)
- [Read the system card(opens in a new window)](https://deploymentsafety.openai.com/gpt-6-cyber)
- [Advancing frontier cyber capabilities](https://openai.com/index/introducing-gpt-6-cyber/#advancing-frontier-cyber-capabilities)
- [Stronger alignment, better at staying within bounds](https://openai.com/index/introducing-gpt-6-cyber/#stronger-alignment-better-at-staying-within-bounds)
- [Real-world impact for security teams](https://openai.com/index/introducing-gpt-6-cyber/#real-world-impact-for-security-teams)
- [Detecting misuse and blocking high-risk activity](https://openai.com/index/introducing-gpt-6-cyber/#detecting-misuse-and-blocking-high-risk-activity)
- [Defending critical infrastructure](https://openai.com/index/introducing-gpt-6-cyber/#defending-critical-infrastructure)
- [Expanding access to trusted defenders](https://openai.com/index/introducing-gpt-6-cyber/#expanding-access-to-trusted-defenders)
- [948 privilege escalation exploits in Linux⁠](https://openai.com/index/a-thousand-fewer-paths-to-root/)
- [released fixes for many of the Firefox vulnerabilities⁠(opens in a new window)](https://www.mozilla.org/en-US/security/advisories/mfsa2026-118/)
- [find and fix weaknesses in our own infrastructure⁠](https://openai.com/index/securing-our-frontier-model-training-environment/)
- [a limited window to use frontier models to secure software⁠](https://openai.com/index/the-defenders-window/)
- [Hugging Face incident⁠](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
- [critical vulnerability in Brotli⁠(opens in a new window)](https://patchtheplanet.org/brotli)
- [Zero Data Retention⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data)
- [PSP⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/private-safety-processing)
- [sandboxing⁠(opens in a new window)](https://learn.chatgpt.com/docs/sandboxing)
- [action review⁠(opens in a new window)](https://learn.chatgpt.com/docs/sandboxing/auto-review)
- [Daybreak for Frontline Defenders⁠](https://openai.com/index/daybreak-for-frontline-defenders/)
- [See their final report⁠(opens in a new window)](https://hub.dragos.com/whitepaper/frontier-ai-models-xot-environment)
- [let us know⁠(opens in a new window)](https://docs.google.com/forms/d/e/1FAIpQLSdQu8mNYXDpUW_0kRS6JBWBPMWfUjjxi6xLi8AkFPObLupkpg/viewform)
- [apply for Daybreak⁠](https://openai.com/daybreak/)
- [cyber skills, products, and partners⁠](https://openai.com/business/solutions/cybersecurity/)
- [Codex](https://chatgpt.com/codex/?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [Cybersecurity](https://openai.com/news/?tags=cybersecurity)
- [View all](https://openai.com/news/)
- [Partnering with Hacktron to strengthen OpenAI’s securitySecurityNov 6, 2026](https://openai.com/index/partnering-with-hacktron/)
- [Daybreak Red is now available in AWS GovCloud (US-East)ProductNov 4, 2026](https://openai.com/index/daybreak-red-aws-govcloud/)
- [Research Overview](https://openai.com/research/)
- [Economic Research](https://openai.com/signals/)
- [GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/)
- [GPT-6 Astra](https://openai.com/index/gpt-6-astra/)
- [GPT-5.6](https://openai.com/index/gpt-5-6/)
- [GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Safety Approach](https://openai.com/safety/)
- [Deployment Safety(opens in a new window)](https://deploymentsafety.openai.com/)
- [Security & Privacy](https://openai.com/security-and-privacy/)
- [Trust & Transparency](https://openai.com/trust-and-transparency/)
- [ChatGPT Business(opens in a new window)](https://chatgpt.com/business/?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [ChatGPT Enterprise(opens in a new window)](https://chatgpt.com/business/enterprise/?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [ChatGPT for Education(opens in a new window)](https://chatgpt.com/business/education/?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [Dots(opens in a new window)](https://chatgpt.com/features/dots?openaicom-did=aa2fff79-5705-4062-89d2-81002c77ad0f&openaicom_referred=true)
- [Release Notes](https://openai.com/products/release-notes/)
- [API Log In(opens in a new window)](https://platform.openai.com/login)
- [Docs(opens in a new window)](https://developers.openai.com/)
- [Solutions](https://openai.com/solutions/)
- [Resources](https://openai.com/business/learn/)
- [Plugins](https://openai.com/business/plugins/)
- [Customer Stories](https://openai.com/business/customer-stories/)
- [Partner Network](https://openai.com/business/partners/)
- [Contact Sales](https://openai.com/contact-sales/)
- [Plugins(opens in a new window)](https://developers.openai.com/plugins)
- [Models(opens in a new window)](https://developers.openai.com/api/docs/models)
- [Resources(opens in a new window)](https://developers.openai.com/learn)
- [Developer Forum(opens in a new window)](https://community.openai.com/)
- [Our Charter](https://openai.com/charter/)
- [Careers](https://openai.com/careers/)
- [Help Center(opens in a new window)](https://help.openai.com/)
- [OpenAI Status(opens in a new window)](https://status.openai.com/)
- [Stories](https://openai.com/stories/)
- [Academy](https://openai.com/academy/)
- [Supply Co.](https://openai.com/supply/)
- [Livestreams](https://openai.com/live/)
- [Podcast](https://openai.com/podcast/)
- [RSS](https://openai.com/news/rss.xml)
- [Terms of Use](https://openai.com/policies/terms-of-use/)
- [Privacy Policy](https://openai.com/policies/privacy-policy/)
- [Other Policies](https://openai.com/policies/)
- [(opens in a new window)](https://discord.gg/openai)
