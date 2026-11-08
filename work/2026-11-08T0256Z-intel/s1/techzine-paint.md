Title: Paint vulnerability allows RCE, patch is hard to find

URL Source: https://www.techzine.eu/news/security/145581/paint-vulnerability-allows-rce-patch-is-hard-to-find/

Published Time: 2026-11-05T08:40:43+00:00

Markdown Content:
**Microsoft Paint contains a remote code execution vulnerability with a CVSS score of 8.1. Microsoft released a fix in October, but many administrators are unable to obtain the patched version. There is also confusion regarding the correct version number.**

A vulnerability in Microsoft Paint allows attackers to remotely execute code on Windows 11 PCs. This vulnerability is known as CVE-2026-83844. Microsoft publicly disclosed its existence on October 13 and released a fix. However, administrators report that the update is not reaching them.

The vulnerability involves an out-of-bounds read in Paint. Using a specially crafted image, an attacker can execute malicious code. According to Microsoft’s own classification, the attack occurs over the network and does not require any privileges. Nevertheless, the company rates the attack complexity as “High.” Windows Latest, however, describes it as a [no-click bug that can remain unpatched even with automatic updates enabled](https://www.windowslatest.com/2026/11/05/windows-11s-paint-has-a-no-click-hacking-bug-and-even-with-auto-updates-on-you-may-not-have-the-fix/).

## Which version is secure?

In the Security Update Guide, Microsoft initially listed version 11.2605.91.0 as the patched, and therefore secure, release. On a Microsoft Q&A forum, someone asked where that version could be found, since the Microsoft Store was still offering the insecure version 11.2605.81.0. On Reddit, a moderator shared PowerShell output showing that Paint remained stuck on that older version, even after checking for updates in the Store and running WSReset.

This may be a phased rollout, somewhat unusual for a dangerous vulnerability but common for a patch. One user claims that the patch is currently only available in South Asian regions. However, the [MSRC page](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844) now lists version 11.2609.401.0 as the fix. It appears the earlier version contained a typo, though Microsoft has not confirmed this. [Other sources](https://borncity.com/news/microsoft-paint-sicherheitsluecke-mit-cvss-81-version-11-2609-401-0-schuetzt/) also identify 11.2609.401.0 as the secure version.

## Check for yourself

So the fact that the Store marks Paint as up-to-date doesn’t mean much. You can check the version actually installed using PowerShell: `Get-AppxPackage Microsoft.Paint | Select-Object Name, Version`. As long as the patch isn’t available everywhere, organizations can temporarily restrict unreliable image attachments. And anyone who doesn’t need Paint for whatever reason can also uninstall the app.

**See also:**[Vulnerability in Windows Defender leads to file loss](https://www.techzine.nl/nieuws/security/544821/kwetsbaarheid-in-windows-defender-leidt-tot-bestandsverlies/)

Links/Buttons:
- [Skip to content](https://www.techzine.eu/news/security/145581/paint-vulnerability-allows-rce-patch-is-hard-to-find/#main)
- [Techzine Global](https://www.techzine.eu/)
- [Topstories](https://www.techzine.eu/topstories/)
- [Topics](https://www.techzine.eu/news/security/145581/paint-vulnerability-allows-rce-patch-is-hard-to-find/#)
- [Analytics](https://www.techzine.eu/insights/analytics/)
- [Applications](https://www.techzine.eu/applications/)
- [Collaboration](https://www.techzine.eu/collaboration/)
- [Data Management](https://www.techzine.eu/data-management/)
- [Devices](https://www.techzine.eu/devices/)
- [Devops](https://www.techzine.eu/devops/)
- [Infrastructure](https://www.techzine.eu/infrastructure/)
- [Privacy & Compliance](https://www.techzine.eu/privacy-compliance/)
- [Security](https://www.techzine.eu/tag/security/)
- [All Insights](https://www.techzine.eu/insights/)
- [Agentic AI](https://www.techzine.eu/insights/agentic-ai/)
- [Cloud ERP](https://www.techzine.eu/insights/cloud-erp/)
- [Generative AI](https://www.techzine.eu/insights/gen-ai/)
- [IT in Retail](https://www.techzine.eu/insights/it-in-retail/)
- [NIS2](https://www.techzine.eu/insights/nis2/)
- [RSAC 2025 Conference](https://www.techzine.eu/insights/rsac-2025-conference/)
- [Security Platforms](https://www.techzine.eu/insights/security-platforms/)
- [SentinelOne](https://www.techzine.eu/insights/sentinelone/)
- [Become a partner](https://www.dolphin.pub/)
- [About us](https://www.techzine.eu/about-us/)
- [Contact us](https://www.techzine.eu/contact)
- [Terms and conditions](https://www.techzine.eu/conditions)
- [Privacy Policy](https://www.techzine.eu/privacy)
- [Techzine Netherlands](https://www.techzine.nl/)
- [Techzine Belgium](https://www.techzine.be/)
- [Techzine TV](https://www.techzine.tv/)
- [ICTMagazine Netherlands](https://www.ictmagazine.nl/)
- [ICTMagazine Belgium](https://www.ictmagazine.be/)
- [News](https://www.techzine.eu/news/)
- [Erik van Klinken](https://www.techzine.eu/author/erik-van-klinken/)
- [November 5, 2026 9:40 amNovember 5, 2026](https://www.techzine.eu/news/security/145581/paint-vulnerability-allows-rce-patch-is-hard-to-find/)
- [no-click bug that can remain unpatched even with automatic updates enabled](https://www.windowslatest.com/2026/11/05/windows-11s-paint-has-a-no-click-hacking-bug-and-even-with-auto-updates-on-you-may-not-have-the-fix/)
- [MSRC page](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844)
- [Other sources](https://borncity.com/news/microsoft-paint-sicherheitsluecke-mit-cvss-81-version-11-2609-401-0-schuetzt/)
- [Vulnerability in Windows Defender leads to file loss](https://www.techzine.nl/nieuws/security/544821/kwetsbaarheid-in-windows-defender-leidt-tot-bestandsverlies/)
- [CVE-2026-83844](https://www.techzine.eu/tag/cve-2026-83844/)
- [Microsoft](https://www.techzine.eu/tag/microsoft/)
- [Paint](https://www.techzine.eu/tag/paint/)
- [patch](https://www.techzine.eu/tag/patch/)
- [remote code execution](https://www.techzine.eu/tag/remote-code-execution/)
- [vulnerability](https://www.techzine.eu/tag/vulnerability/)
- [windows 11](https://www.techzine.eu/tag/windows-11/)
- [Microsoft patches 137 vulnerabilities and deploys AI scanner](https://www.techzine.eu/news/security/141284/microsoft-patches-137-vulnerabilities-and-deploys-ai-scanner/)
- [January patches fix vulnerabilities in Windows and Excel](https://www.techzine.eu/news/security/127816/january-patches-fix-vulnerabilities-in-windows-and-excel/)
- [Patch Tuesday brings 84 new Microsoft fixes](https://www.techzine.eu/news/security/83163/patch-tuesday-brings-84-new-microsoft-fixes/)
- [Microsoft fixes Defender’s zero-day vulnerability on Patch Tuesday](https://www.techzine.eu/news/applications/54474/microsoft-fixes-defenders-zero-day-vulnerability-on-patch-tuesday/)
- [vSphere Express: A return to an affordable VMware?](https://www.techzine.eu/blogs/infrastructure/145578/vsphere-express-a-return-to-an-affordable-vmware/)
- [AI in Europe is a race for trust, not capabilities](https://www.techzine.eu/blogs/devops/145628/ai-in-europe-is-a-race-for-trust-not-capabilities/)
- [The most powerful local AI relies on full-stack support](https://www.techzine.eu/blogs/devices/145626/the-most-powerful-local-ai-relies-on-full-stack-support/)
- [“Don’t blindly trust open source, take control”](https://www.techzine.eu/blogs/analytics/145490/dont-blindly-trust-open-source-take-control/)
- [](https://www.techzine.eu/whitepapers/infrastructure/131104/how-to-choose-the-right-enterprise-linux-platform/)
- [Berry Zwets](https://www.techzine.eu/author/berry-zwets/)
- [Mels Dees](https://www.techzine.eu/author/mels-dees/)
- [Kim Loohuis](https://www.techzine.eu/author/kim-loohuis/)
- [Expert Talks](https://www.techzine.eu/experts/)
- [Keeping up with F1: How high-performance storage powers live media production](https://www.techzine.eu/experts/infrastructure/143979/keeping-up-with-f1-how-high-performance-storage-powers-live-media-production/)
- [Why uniform governance fails with enterprise AI agents (and how to fix it)](https://www.techzine.eu/experts/devops/143606/why-uniform-governance-fails-with-enterprise-ai-agents-and-how-to-fix-it/)
- [Tech calendar](https://www.techcalendar.eu/)
- [Benelux Cyber Summit](https://www.techcalendar.eu/events/benelux-cyber-summit-2/)
- [Celosphere 2026](https://www.techcalendar.eu/events/celosphere-2026/)
- [Whitepapers](https://www.techzine.eu/whitepapers/)
- [Enhance your data protection strategy for 2025](https://www.techzine.eu/whitepapers/infrastructure/129552/enhance-your-data-protection-strategy-for-2025/)
- [Strengthen your cybersecurity with DNS best practices](https://www.techzine.eu/whitepapers/security/129390/strengthen-your-cybersecurity-with-dns-best-practices/)
- [Twitter](https://x.com/techzine)
- [LinkedIn](https://www.linkedin.com/company/techzine-eu)
- [YouTube](https://www.youtube.com/@Techzine)
- [Contact](https://www.techzine.eu/contact/)
- [Terms & Conditions](https://www.techzine.eu/conditions/)
- [Privacy Statement](https://www.techzine.eu/privacy/)
