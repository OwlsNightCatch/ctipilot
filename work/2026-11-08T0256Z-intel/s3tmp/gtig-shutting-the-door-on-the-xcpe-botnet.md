---
title: Shutting the Door on the XCPE Botnet | Google Cloud Blog
author: Google Threat Intelligence Group
url: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet
hostname: google.com
description: Google and industry partners have dismantled the XCPE backdoor and botnet, which was intentionally developed and operated by OEM Videostrong Technology Co. for financial gain.
sitename: Google Cloud Blog
date: "2026-11-02"
tags: ['Threat Intelligence']
fingerprint: a4b499518cbf21c1
---
# Shutting the Door on the XCPE Botnet

##### Google Threat Intelligence Group

##### Google Threat Intelligence

Visibility and context on the threats that matter most.

[Contact Us & Get a Demo](https://cloud.google.com/security/resources/google-threat-intelligence-demo?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY25-Q2-global-GCP30649-website-su-dgcsm-GTI-interest)

### Introduction 

Last week, Google and industry partners dismantled the XCPE backdoor which enrolled more than 1.3 million set-top boxes into a botnet. We assess with high confidence that the backdoor and botnet were intentionally developed, deployed, and operated for financial gain by Videostrong Technology Co., an Android Original Equipment Manufacturer (OEM) and Original Design Manufacturer (ODM).

Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at least 10 million additional compromised devices.

We found this malicious software built directly into many different device models and brands over multiple years, supported by dedicated infrastructure and constantly evolving configurations to evade detection and manage their affiliates. We believe this campaign wasn’t an isolated rogue insider or a development oversight. As a result, Google has cut ties with Videostrong and banned them from making devices with preloaded Google apps.

Google requires OEMs go through a comprehensive suite of compatibility and security tests to ensure a consistent and safe user experience across the Android ecosystem. However, Videostrong employed obfuscation techniques to exploit a gap in our tests and load malicious code after the device's first boot. As a result, Google has implemented changes to its existing review process to better safeguard against similar activity in the future. A device manufacturer intentionally infecting their users with malware is an unacceptable breach of trust, and represents a serious risk to those users. Without users’ knowledge or consent, infected devices were offered as a distribution mechanism for a wide array of criminal actors. This led to a variety of malicious activities being conducted on and through the devices, including ad-fraud, data exfiltration, and [routing malicious network traffic](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks?e=48754805) through the devices.

We worked closely with Japan’s National Police Agency, Lumen, HUMAN Security, Plume, Synthient, and TrendAI to analyze this malware ecosystem and disrupt its operations.

While we expect this disruption to have a significant effect on these criminal operations, this is not the end of our work combatting malicious activity. Backdoor operators, ad-fraud rings, and residential proxy providers operate as an interconnected supply chain. Point-in-time disruptions are a critical tool to protect our users, but lasting disruption in this fluid ecosystem will require continued targeting of this infrastructure.

Google undertook the following actions to support disruption of the XCPE botnet:

- Legal action to take down the domains and servers Videostrong used to control the botnet and install malware modules
- Legal action to take down C2 domains used by over a dozen malware families loaded as modules via this backdoor
- Banned Videostrong and any future subsidiaries or affiliates from building and selling certified Android devices in the future, or supplying software to other certified vendors
- Implementing improvements to how we ensure the integrity of firmware on certified Android TV devices

### Overview

The x.cpe network was built for ongoing profit. By giving malware affiliates backdoor access, the operators conspired to monetize these devices long after purchase.

Figure 1: XCPE malware overview

#### Malware

Since at least late 2024, Videostrong has evolved its pre-installed malware from simple single-stage droppers into a modular, three-stage architecture designed for resilience and multi-tenant monetization:

- **Primary Backdoor:** Operating at the `android.uid.system` privilege level, `x.cpe` (running as `com.oemservice` in some builds) is preloaded in the firmware partition. If uninstalled by a user, it automatically reinstalls from the `/oem/` partition upon reboot, maintaining persistent system-level access. Its main function is to establish and facilitate communications between the C2 server and the loader and execution engine.
- **Loader and Execution Engine:** To evade security scans, `x.cpe` acts primarily as the C2 communicator and offloads module execution to an external loader, `com.abc.nexus`. This file employs native anti-analysis utilities to thwart sandbox detection, and configures and initializes the monetization modules. Most recently, `com.abc.nexus` has itself been phased out in favor of using more tailored dropper malware that loads and executes single modules.
- **Monetization Modules:** Videostrong monetizes its backdoored devices by loading monetization modules which are developed by entities other than Videostrong that act as affiliates. These modules are deployed as native ELF daemons, embedded SDKs compiled directly into the `com.abc.nexus` DEX bytecode, or are fetched as secondary APKs from the malware staging infrastructure.  The loaded modules transform infected devices into residential proxy exit nodes (e.g., Linkfog, AppSalt, NetNut), ad-fraud engines (e.g., CBOXTV, HiddenView), or execute additional backdoors that load even more monetization modules (e.g. Moyu, Spirit).

#### **Infrastructure**

- **Command and Control:** The botnet uses a two-stage C2 process. It first initiates HTTP POST requests to fetch dynamic configuration settings, geolocation data, and STUN server parameters. It then establishes a persistent, real-time Message Queuing Telemetry Transport (MQTT) connection to receive instructions for silent app installations, arbitrary shell commands, screen captures, and network reconnaissance. MQTT is a lightweight, publish-and-subscribe network protocol designed for low-bandwidth, high-latency, or unreliable remote networks.
- **Malware staging infrastructure:** Additional monetization modules as well as various shell scripts and legitimate applications are hosted remotely and downloaded by infected devices upon command from the operator via the MQTT broker. A significant majority of these files are hosted as Github releases on operator-owned Github pages. Other files are hosted on operator-controlled servers and file hosting sites.

#### **Malware Deep Dive**

#### Backdoor Initialization

The infection chain begins with a stub package (called `x.cpe` in some builds and `com.oemservice` in others) preloaded in the system partition of the firmware and running at the `android.uid.system` privilege level. This stub has limited functionality. Upon boot, it checks the device's `oem/` directory for the corresponding `x.cpe` package and initiates installation into the `/data/app/` directory as outlined below.

To maintain inter-process state across the firmware ecosystem, `x.cpe` exports two ContentProviders, which expose structured configuration tables storing runtime parameters, device identifiers, proxy configuration blobs, and execution flags accessible by co-installed system applications. This enables other apps in Videostrong’s ecosystem, such as their YokaTV Player streaming software, to fetch configuration parameters provided by the C2 server mentioned below.

#### C2 Configuration

The malware utilizes a two-stage communications protocol. It first fetches initial bootstrap configurations via an HTTP request, followed by a persistent MQTT subscription to receive commands and module download instructions.

To dynamically derive the HTTP C2 bootstrap server, it follows the following routine:

- Queries `content://com.release.debug.provider/configs` for `private_url` via `x.cpe.util.ExtraReadUtils`.
- Queries the Android system property to determine if `ro.mecool.device` is true.
- If true, it defaults to `http://mcstb.anyevonline.com:8000`
- If false, it dynamically generates the following: `http://stb[AndroidVersion][Type].anyevonline.com:8000`.

Using the selected hostname, the client makes an HTTP POST request with an AES-encrypted JSON object containing hardware telemetry (SN, MAC, model, firmware version) to the following endpoints:

- **/router/config/mqtt:** This endpoint provides MQTT broker details (including Broker Hostname, TCP Port, Authentication Tokens/Passwords, and the specific Topic structure: `/device/{model}/{chipId}/{action}`. After receiving this data, the device initiates a persistent, real-time socket connection to the MQTT broker.
- **/router/config/acs:** This endpoint response returns URLs for `ip-api[.]com` and a Google STUN server to enable the malware to identify geolocation and public IP and port mapping to traverse network address translation (NAT) boundaries. It also returns a URL (`http://ott.szbboys[.]com:8000/cpe/file/upload` for uploading files, logs, or diagnostic dumps from the device, and returns flags to configure ad modules (`adBwmActive`, `adDevourUse`, `adDevourCode`), and to enable or disable core malware modules.
- **/router/config/app:** This endpoint provides module-level configs, including server mappings and parameters, which `x.cpe` decrypts and passes to a SQLite `ContentProvider` named `ShareProvider` (`com.oem.share.provider`). By exposing this inter-process data interface, `x.cpe` enables modules to retrieve up-to-date upstream infrastructure parameters (such as URLs for additional configs, user manuals, etc).

#### MQTT Capabilities

Following initial configuration, persistent real-time C2 communication is managed by the MQTT library (`x.cpe.mqtt.MqttUtils`). All identified samples analyzed to date utilize a single broker hostname, `mqtt.szbboys[.]com`.

Specific MQTT topics are mapped to specific actions, including:

- **Silent Application Installation**: Fetches remote APKs to a temporary directory.
- **Disable Google Play Protect**: To bypass security, `AppUtils.disablePackageVerify()` targets the global setting "`package_verifier_user_consent`" via `Settings.Global.putInt` and sets it to `-1`, disabling Google Play Protect app verification.
- **Arbitrary Shell Execution**: Executes remote commands via `sh` under system UID privilege level. Results are published to the MQTT broker.
- **Shell Script Execution**: Downloads and executes shell scripts via `x.cpe.util.RunCmds`.
- **Remote Desktop Monitor & Screen Capture**: Utilizes `android.app.Instrumentation.sendKeyDownUpSync()` to inject keycodes and Java reflection on hidden APIs (`android.view.SurfaceControl.screenshot` / `SurfaceControl$ScreenshotHardwareBuffer`) to continuously capture the screen, compress to JPEG, and publish over MQTT.
- **Network Reconnaissance**: Invokes embedded binaries (`libtraceroute.so`) to fingerprint the victim network, and perform standard ping tests. The binaries also perform robust AS-lookup WHOIS routing queries.

Our analysis of the C2 data indicates the preponderance of interactions with victim devices were related to module install, uninstall, and configuration actions. We also observed Videostrong operators executing sensitive actions on the device, including capturing live screenshots; injecting keystrokes; exfiltrating sensitive data including account information, device information, package inventories, and system logs; and executing shell scripts and commands, including to establish reverse shells on devices.

#### Loader and Execution Engine Details

Earlier versions of `x.cpe` directly embedded malicious monetization modules. In late 2024 – possibly as a response to [earlier Google enforcement](https://blog.google/innovation-and-ai/technology/safety-security/google-taking-legal-action-against-the-badbox-20-botnet/) related to BadBox – Videostrong removed malicious modules from `x.cpe` and introduced a separate malicious package they developed, `com.abc.nexus`, which `x.cpe` routes instructions and data to via Inter-Process Communication (IPC). Modern variants of `x.cpe` facilitate C2 communications but pass configuration parameters, module updates, and other payloads to `com.abc.nexus` as the execution engine. We believe the actor may have evolved the malware in this way in an attempt to ensure `x.cpe` could remain undetected.

Upon boot, `com.abc.nexus.broadcast.BootReceiver` broadcasts the `com.abc.nexus.data` intent, bootstrapping `com.abc.nexus.service.CoreService`. Within `CoreService.onCreate`, the application performs maintenance and persistence tasks. The main logic sets up a listener through `RemoteMessageHandler` for IPC communications from `x.cpe,`and parses JSON payloads received from it.

After these steps, `CoreService` initializes the monetization modules. `com.abc.nexus` services extract and orchestrate a series of nested native libraries and dynamically downloaded secondary payloads which vary significantly based on sample. Many versions of `com.abc.nexus` come preloaded with four or more embedded modules, while other versions contain as few as one. The most common malware modules include `TitanService`, `BwmService`, `AdtimeService`, `lb102Service`, and `LinkfogService` (sometimes called `AgentService)`. Discussion of these and other modules can be found in the monetization modules section.

### Persistence and Evasion

The malware operators implement a number of mechanisms to establish persistence and thwart detection and analysis.

As a system preload, `x.cpe` cannot be removed by the user. If `x.cpe` is uninstalled from `/data/app/`, upon reboot the `x.cpe` service `BootReceiver` follows the same routine outlined above and reinstalls the package.

The backdoor is able to silently download additional files to the device and execute them without user consent because it first wipes user consent configuration on the device and then disables Google Play Protect:


```
public static void disablePackageVerify() {
    PreferenceUtils.setPackageVerifyFromUser(CPEApp.instance, true);
    AppUtils.setPackageVerify(-1); // Actioning a bypass against GPP evaluation
}
```
Figure 2: Disabling Google Play Protect

In many variants of `com.abc.nexus,` we observed the extraction of a sophisticated anti-analysis and process hardening utility `libseccomp_guard.so`, which runs prior to the initialization of malware modules, to ensure they remain protected from automated sandboxes and security instrumentation. It filters system calls to prevent the pausing or termination of individual threads, denies cross-process interference to ensure isolation, and prevents the spawning of child processes.

#### Evolution

Since August 2026, new dropper packages have been installed via the MQTT channel, which appear to be synchronized with the mass-uninstallation of `com.abc.nexus` across the botnet. We assess this may represent a new evolution of the malware to further evade detection. These new packages are disguised as Android system applications, with names such as `com.android.system.ntp` and `com.android.sso.auth.handler`. Where `com.abc.nexus` could act as a general purpose loader and execution engine (executing instructions passed to it from `x.cpe`), these packages instead install single monetization modules (such as AppSalt).  Multiple variants of these packages extract a native ELF file, `libexploit.so`, which in turn executes functions `nativeAdbRoot()` and `nativeAdbShell()`. These functions restart the local `adbd` service as root, and initiate an ADB shell connection. Following this, the app uses the connection to install itself in the `system` partition.  The `system` partition is remounted as read-write and the payload replicates itself to a newly minted directory in `/system/priv-app/` and creates an XML file at `/system/etc/permissions/privapp-permissions-<app name>.xml`. This file grants the malware `android.permission.INSTALL_PACKAGES` and `android.permission.REBOOT`.

The app configures the malware modules through hardcoded configuration parameters, and does not listen for `x.cpe` IPC messages. The app itself is controlled by the operators via shell scripts pushed via the broker and executed by `x.cpe`. These include setting the property `persist.networkstack.uninstall` (which, when read by the app, triggers uninstallation and cleanup), `persist.networkstack.skip_system_install` (which skips system installation, forcing it to remain running in `/data/app/`), and `persist.networkstack.install_time` (which implements timestomping, overriding the default timestamp of the app to align with the other packages installed in the `system` directory).

### Botnet composition

The botnet is globally dispersed, with certain concentrations possibly implying market penetration for the brand distributor.

Figure 3: Global distribution of x.cpe

While the overwhelming majority of the infected devices in the XCPE botnet are Android TV set-top boxes, we observed a number of other infected Android-based IoT devices, including telehealth devices, karaoke machines, and digital signage devices.

#### Monetization

`x.cpe` loads a variety of malicious modules for monetization. Most often the modules are associated with residential proxy services and bandwidth sharing, but we've also observed ad fraud modules. Given that a single device may be running multiple modules providing the same or similar functionality (e.g., as many as three residential proxy SDKs installed on a single device) it is clear that Videostrong seeks to monetize every infected device to the greatest extent possible.

Services are loaded by `com.abc.nexus` via three methods:

- **Native Daemons**: Native ELF binaries prepackaged with `com.abc.nexus`, which are unpacked to data directories and spawned as background processes with system/root privileges.
- **Embedded SDKs / Services**: Java/Kotlin SDKs compiled directly into Nexus and invoked via Android Service lifecycles or IPC broadcast triggers.
- **Dynamic Droppers & Secondary APK Installers**: Downloader function that pulls remote native ELFs or secondary standalone APKs and invokes system package managers. Nexus receives messages from `x.cpe` directing it to download specific modules.

Malware modules loaded via the backdoor include the following:

#### Residential Proxy / Bandwidth Sharing Modules

**LINKFOG**

`Com.abc.nexus`’s `LinkfogService` unpacks a Go binary named `lw_android_agent`  from `assets/` to local app storage and supplies it with vendor parameters. This service silently turns infected devices into residential edge computing and PCDN proxy exit nodes. It connects to FRP reverse tunnels, and uploads bandwidth accounting metrics to Linkfog API backends. Linkfog (operated by Beijing Linkfog Technology via 点心云 / Dianxinyun) brands itself as a “Peer-to-Peer Content Delivery Network”.

**Jaguar**

The `com.abc.nexus` `AdtimeService` extracts `libjaguar.so` from `assets/`. The file is an unobfuscated 32-bit ELF binary written in C, compiled as a native Android binary. It utilizes JNI (Java Native Interface) to initialize its core routines, dynamically derives a ChaCha20 decryption key via ARM NEON SIMD instructions to decode heavily obfuscated configurations , and establishes an encrypted C2 channel. Upon successful registration, the C2 responds with JSON configuration specifying proxy endpoints. The proxy command loop `x_ctrl_do_ctrl_msg` delegates proxy operations based on incoming JSON variable commands, and is capable of both TCP and UDP relay.

**AppSalt / Honeygain**

AppSalt SDK is the residential proxy SDK owned by Honeygain, which is in turn owned by Oxylabs. `com.abc.nexus.service.CoreService` initializes Appsalt SDK. First, the application obtains an Appsalt SDK API key from a native library `libnative_keys.so` by calling its `getAppsaltKey()` function. Appsalt SDK is initialized without displaying a consent screen - instead it explicitly calls the `optIn()` method which sets a consent flag without displaying any user interface. During Appsalt SDK startup it checks the application's installation source and stops execution if the application was installed from the official Google Play Store.

Once Appsalt is successfully initialized it establishes a WebSocket connection with the primary command and control domain. Appsalt uses JSON-formatted messages for initial check-in (registration) and heartbeat requests. Appsalt command and control servers use MessagePack formatted messages to issue commands pertaining to proxy operations. Appsalt SDK is configured with an initial set of domains that act as proxy gateways. The list of proxy gateways can be updated by the command and control server. The device establishes UDP / QUIC connections with these gateways.

**BWM / IPWeb**

This residential proxy and bandwidth-sharing node is implemented through the `com.abc.nexus.service.BwmService` component (sometimes named `com.abc.nexus.service.SN4Service)` and its associated SDK. Upon initialization, it secures itself within an isolated sandbox environment, captures device telemetry, and registers with a remote server over UDP. From this C2, it receives instructions to initiate a Java NIO TCP multiplexed proxy tunnel. The service functions to route arbitrary traffic through the infected device on behalf of a remote threat actor.

**GaGaNode**

GaGaNode is the first-party SDK owned by residential proxy operator IPCola. It connects over TCP to a primary C2 server and sends heartbeat beacon data over HTTP POST to a separate server. The SDK both contains its own proxy relay functionality, and it initializes additional proxy SDKs from affiliates. Upon device registration to the C2, `com.gaganode.sdk.node.endpoint.a` receives incoming packets from relay servers and places them in queue for the client to read and proxy through its exit node socket. The service manages multiple proxy sessions at once (referred to as clients), and each client has its own tcp/udp queue for messages.

We observe GaGaNode initializing PopaNet/NetNut and EarnFM Fleet residential proxy SDKs. GaGaNode/IPCola is thus likely able to further monetize its SDK and offer these affiliates access to the infected exit nodes.

**NetNut / Popanet**

Popanet is a residential proxy SDK developed by NetNut, a residential proxy operator. The GaGaNode module initiates the Popanet SDK (`io.popanet.Popa`). This malware is identical to the malware described in our [previous disruption of NetNut](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks). All C2 infrastructure used by Popanet samples connected to `x.cpe` was taken down as part of the earlier Netnut disruption.

**Traffmonetizer**

The Traffmonetizer SDK is initialized inside the primary background service com.abc.nexus.service.CoreService. CoreService operation depends on the availability of policy JSON provided by the XCPE backdoor via IPC. Before calling Traffmonetizer SDK initialization methods, the application obtains a Traffmonetizer SDK API key from the native library `libnative_keys.so` by calling its `getTraffmonetizerKey()` function.

Traffmonetizer functionality is split between two components where the Android SDK acts as a state machine which handles native library callbacks through asynchronous event dispatchers. `ServiceBloc` monitors connection status updates from the native callbacks and `ConnectivityBloc` monitors Wi-Fi and mobile data network changes.

Traffmonetizer native library initialization and configuration is followed by a call to `baseClientStart()` which establishes a WebSocket connection to a C2 server. Traffmonetizer uses a single WebSocket (TLS) connection to the command and control server to multiplex control messages and tunneled connections (supports both TCP and UDP). Traffmonetizer also supports “Content Delivery” tunneling which allows nodes to tunnel bandwidth-intensive traffic.

**EarnFM**

EarnFM is a residential proxy provider, and Fleet SDK is the provider’s SDK that enrolls devices as exit nodes into the proxy network. In `com.abc.nexus`, FleetSDK is initialized by `com.gaganode.sdk` as mentioned above. FleetSdk then loads native binary `libfleetshare.so`.

FleetSDK establishes a persistent WebSocket connection with its primary C2 server for routing arbitrary network traffic. Incoming tasking frames are received over the WebSocket channel and processed in a continuous loop. Messages contain structured JSON commands instructing the daemon to connect to specific remote hosts, with support for both TCP and UDP.

#### Backdoor Modules

**Spirit**

Spirit is a dynamic code loading backdoor. Spirit employs multiple stages. The first stage payload fetches device information (hardware, operating system, and manufacturer/brand information and geolocation), posting it over HTTP to a hardcoded C2 server, and fetches a list of additional modules to download from the server. The second stage communicates with a separate server, and is used for tasking, config sync, module retrieval, heartbeats, and reporting. We have observed Spirit loading a significant amount of additional malware monetization modules, including some of the families already directly loaded by `com.abc.nexus`.

**Moyu**

Moyu is a 3-stage backdoor previously observed as part of the BadBox enterprise. On `x.cpe`-backdoored devices, we observed it initialized by `com.abc.nexus.service.DevourService.` The first stage is an offline dropper that reconstructs and loads an embedded second stage. Stage two polls an update C2 to download, decrypt, and load the third stage. Stage three implements a backdoor with hidden Double-WebView click/conversion fraud, persistent clipboard hijacking, and secondary dynamically loaded JAR execution and a separate residential proxy trojan.

**Bird**

Bird is a 2-stage backdoor previously tied to the BadBox enterprise. Stage 1 beacons a device and analysis-environment profile to its C2 server and, when the server approves, downloads, decrypts, and loads the Stage 2 JAR. Stage 2 implements a dynamic code loading backdoor (two plugin loaders plus a C2-driven reflective method invoker), a separate downloader (silent APK installation and Accessibility-driven Google Play installs), and ad abuse (lockscreen ads, overlays, browser launches).

**Fission**

Fission is a dynamic code loading (DCL) backdoor embedded within standard video applications (e.g., `com.newtv.cboxtv`). Upon initialization, the first stage plugin contacts its C2 server to download additional modules. The decrypted second stage payload fetches execution targets and tracking URLs from the C2. The request sends an unencrypted POST request with tracking metrics from the internal `DeviceManager.`

The payload we observed was configured to commit ad fraud. Rather than rendering visible advertisements in a `WebView` or UI component, the Stage 2 plugin executes headlessly in the background. The module queries ad server endpoints in the background to retrieve ad placement responses, parses out both primary impression beacons (`pvm`) and third-party tracking monitor URLs (`pvtpm`), and immediately fires HTTP GET requests to each tracking endpoint to register a fake ad view without displaying creative content. When executing inside specific smart-TV application stores (`com.changhong.appstore` or `com.tcl.appmarket2`), the plugin initializes and triggers the ad SDK directly to report synthetic ad exposures.

#### Ad-Fraud

**HiddenView**

We observed HiddenView loaded remotely from the attacker’s Github channel as `com.ota.service`. It is a standalone ad fraud application capable of running in the background using a transparent window overlay, using hidden WebViews to load targeted web pages and simulate user interaction (scrolling, clicking, typing, media playback), playing media unattended, and capturing the user’s screen.

#### How the pieces come together

Configuration messages pushed via MQTT (action `ext/lib/config`) demonstrate how `x.cpe`, `com.abc.nexus` and various monetization modules function together.

Upon registration, subscribed devices receive a `ext/lib/config` message, which contains configuration parameters for malicious plugins. This includes:

Limits on system resources:


```
"constraints": [
    {
      "cpu": 70,
      "ioRead": 5000,
      "ioWrite": 5000,
      "libCode": "linkfog",
      "memory": 50,
      "reportAlarm": true,
      "trigger": 3
    }
```
Figure 4: System resource limits configuration payload

Module name, download location per architecture, hashes, and weight (relative priority for system resources):


```
 "infos": [
    {
      "libChannel": "SZKJ",
      "libCode": "linkfog",
      "libResource": [
        {
          "address": "https://github.com/Aviciiii/ott/releases/download/cpe_ext_lib/lw_android_agent_special_ndk_64",
          "architecture": "arm64-v8a",
          "md5": "abd0b6de6fdf78234f5dab098d5dd229"
        },
        {
          "address": "https://github.com/Aviciiii/ott/releases/download/cpe_ext_lib/lw_android_agent_special_ndk_32_20250717",
          "architecture": "armeabi-v7a",
          "md5": "d8971688d1929b6ed915b80eca7e7e3f"
        }
      ],
      "libWeight": 5
    },
```
Figure 5: Module configuration payload

Devices are assigned to one of six timezone-separated pools on the `ott.szbboys[.]com` domain:


```
"region": "Iraq",
  "serverPool": {
    "defaultPool": "Pool5",
    "lastUpdated": "2025-08-06 17:00:00",
```
Figure 6: Server Pool configuration payload

The “`policys`” section instructs `com.abc.nexus` which modules to download and run:


```
 "status": [
    {
      "enable": true,
      "libCode": "linkfog"
    },
    {
      "enable": false,
      "libCode": "bwm"
    },
    {
      "enable": false,
      "libCode": "adtime"
    },
    {
      "enable": false,
      "libCode": "admoyu"
    },
    {
      "enable": false,
      "libCode": "titan"
    },
    {
      "enable": false,
      "libCode": "lb102"
    }
  ],
```
Figure 7: Module activation payload

`x.cpe` passes on these configuration parameters to `com.abc.nexus` for the given module on the device. Devices report bandwidth usage and alarms back to `serverPool` to stay within the configured constraints.

When `com.abc.nexus` acknowledges receiving the bundle, `x.cpe` immediately publishes `ext/lib/config/reply` back to the MQTT broker:


```
"code": 0,
  "msg": "success",
  "data": "received data success and applying",
  "async": true,
  "immediately": false
```
Figure 8: x.cpe response payload

#### Infrastructure

As previously mentioned, devices first connect to various endpoints on `*.anyevonline[.]com` for initial bootstrap, registration, and configuration. Earlier malware versions used various hostnames of `{*tms | *ott | *ota}.szbboys[.]com` for the same purpose.

While earlier versions of the malware used HTTP for C2, and then a blended C2 approach with both HTTP and MQTT, static analysis of current versions indicate they exclusively send/receive C2 communications via MQTT. A single MQTT broker orchestrates all MQTT C2 communications for samples we’ve identified. Hostname `mqtt.szbboys[.]com` is resolved by hosts `219.134.163[.]210` and `219.134.163[.]211.` It listens on non-standard MQTT ports 3885-3887.

The malware constructs OkHttp requests for file downloads after tasking via the MQTT broker. Files are hosted on several services:

- Several Github release pages
- The `filemail[.]com` file sharing service
- Two operator-controlled servers hosted on IPs `38.145.197[.]135` and `23.94.49[.]57`

Netflow telemetry on the broker nodes (`219.134.163[.]210/.211`) indicates that while infected devices communicate over ports 3885–3887, operators likely manage the broker and dispatch tasking via interactive HTTP REST API (port 8082), WebSocket (port 8083), and EMQX web administration console (port 18083) sessions originating from non-bot IP space.

### Call to Action

While we believe our actions have seriously impacted over a dozen malicious actors, the underlying illicit market is resilient. Backdoor operators, ad-fraud rings, and residential proxy providers operate as an interconnected supply chain, and when one component is disrupted, operators quickly pivot to new loaders or rival monetization SDKs. Creating lasting change requires accountability across the hardware supply chain, the residential proxy industry, and the broader technology ecosystem.

#### Accountability and Reform

A device manufacturer intentionally infecting their users with malware is an unacceptable breach of trust. By turning everyday hardware into persistent beachheads for criminal affiliates, Videostrong prioritized illicit post-sale recurring revenue over the safety and privacy of its users. Downstream hardware brands, white-label resellers, telecommunications providers, and online e-commerce marketplaces also share responsibility for closing this vector. Retailers and distributors should require independent security audits from Original Design Manufacturers (ODMs) and swiftly delist manufacturers implicated in supply-chain abuse.

Residential proxy providers have been able to flourish under the guise of legitimate businesses. While some providers may claim to behave ethically and only enroll devices with the clear consent of consumers, any claims of "ethical sourcing" must be backed by transparent, auditable proof of user consent. In our analysis, these proxy operators only seek consent when they are forced due to platform policy and enforcement. Silent opt-in without user consent remains the most prevalent means by which devices are turned into exit nodes.

#### Empowering and Protecting the Consumer

Residential proxies are an understudied area of risk for consumers, and more can be done to raise awareness. Consumers should be extremely wary of applications that offer payment in exchange for "unused bandwidth" or "sharing your internet." These applications are primary ways for illicit proxy networks to grow, and could open security vulnerabilities on the device’s home network. We urge users to stick to app stores you trust, review permissions for third-party VPNs and proxies, and ensure built-in security protections like Google Play Protect are active.

Consumers should only purchase connected devices, such as set-top boxes, from reputable manufacturers. Our [Android TV website](https://www.android.com/certified/partners/) provides the most up-to-date list of partners.

#### Industry Collaboration

We encourage mobile platforms, ISPs, online marketplaces and other tech platforms to continue sharing intelligence and implementing best practices to identify malicious backdoors, illicit proxy networks, and other harmful software and limit their harms.
