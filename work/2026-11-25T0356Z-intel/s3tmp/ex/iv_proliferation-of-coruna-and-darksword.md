---
title: Proliferation of Coruna and DarkSword
url: https://www.iverify.com/blog/proliferation-of-coruna-and-darksword
hostname: iverify.com
description: Explore how Coruna and DarkSword iOS exploit kits are evolving, proliferating, and being combined to expand mobile attack capabilities in the wild.
sitename: iVerify
date: "2026-09-15"
fingerprint: ac50015e9206bdc7
language: en
image: https://framerusercontent.com/images/HXLWRfzgj9BiO73m50pwnHSnZ7M.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
In March 2026, we published details about [Coruna](https://www.iverify.com/blog/coruna-inside-the-nation-state-grade-ios-exploit-kit-we-ve-been-tracking), a commercial spyware kit that leaked into the hands of cybercriminals which was later proved to have come from L3 Trenchant where Peter Williams had been convicted of stealing zero-day exploits from them and selling them to a Russian access broker. Two weeks after [Coruna](https://www.iverify.com/blog/coruna-inside-the-nation-state-grade-ios-exploit-kit-we-ve-been-tracking), we reported on another spyware framework, [DarkSword](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained), used in waterhole attacks in Ukraine which Google Threat Intelligence group had also seen used in attacks in Saudi Arabia, Turkey and Malaysia by different threat actors. Since then, we’ve continued tracking these threats and their evolution. We leveraged advanced capabilities of the [Validin](https://www.validin.com/) platform and custom-built tooling to hunt for new variants of both frameworks. At [Black Hat in Las Vegas](https://blackhat.com/us-26/briefings/schedule/#inside-coruna-and-darksword---ios-exploits-caught-in-the-wild-54085) this year, Matthias Frielingsdorf presented on how threat actors are proliferating these kits and even combining them in a single deployment to expand the range of devices they can infect from a single website visit. We called this combined deployment DarkCoruna. Advances in AI are accelerating the proliferation of these frameworks, enabling less sophisticated attackers - who previously couldn’t target mobile devices - to gain capabilities once reserved for the most advanced threat actors. Attackers continue to invest in exploit kit development and the infrastructure needed to infect devices. This blog post provides details on the samples discussed during the BlackHat talk.

# Coruna

We are not aware of any public leaks of Coruna’s source code. To repurpose this exploit kit, threat actors would need to obtain the leaked source code and recompile it with their desired changes, or patch the binaries and emulate the original deployment and C2 infrastructure. Because of this, Coruna hasn’t changed much since we first observed it, but threat actors are investing more in stealth to evade on-device detection, automated scanners, and detonation frameworks to remain operational for as long as possible.

Artifacts left by this exploit kit persist across reboots and updates. So it is possible for us to track past infections even though iVerify wasn’t running on the devices when they were first infected. Our September telemetry shows that both live and historic attacks against devices on vulnerable iOS versions now affect 5% of devices - compared to 1.5% measured in August.

The */private/var/mobile/Library/Preferences/com.apple.photolibraryd.plist* file is one of the persistent artifacts that is left behind by the kit. The threat actors have removed the hardcoded name for a 16 hex character variant: */private/var/mobile/Library/Preferences/com.apple.{16-hex-characters}.plist).* It still contains information about exfiltrated photos useful for photos re-processing over time or during device re-infection.

This file still persists in Encrypted Backups, and because of this, it’s easy to spot.

During further investigation we discovered that *Documents/.devcache* files exists in application containers because the implants injected into different processes communicate with the C2 server independently. To submit data under the same infection umbrella, the implants need shared identifiers.

Notable changes:

- Stage 2 implant runs from the watchdogd process (powerd can be used as a fallback mechanism).
- Stage 3 CorePayload implant runs inside configd, filecoordinationd or locationd.
- New Telegram implant module.
- *com.apple.photolibraryd.plist* file doesn’t have a constant name; it’s now *com.apple.{16-hex-characters}.plist.*
- Enhanced jailbreak detection.
- Updated and enhanced configuration file.

### Jailbreak Detection

- Checks for file and directory existence on : `/var/jb` , `/var/binpack` , `/Applications/Cydia.app` , `/Library/MobileSubstrate` , `/usr/sbin/sshd` , `/etc/apt` , `/var/LIB` , `/.installed_dopamine` , `/var/jb/.installed_dopamine` , `/Applications/blackra1n.app` , `/Applications/FakeCarrier.app/` , `/Applications/Icy.app` , `/Applications/IntelliScreen.app` , `/Applications/MxTube.app` , `/Applications/RockApp.app` , `/Applications/SBSettings.app/` , `/Applications/WinterBoard.app/` , `/Applications/Palera1n.app` , `/Applications/Sileo.app` , `/Applications/Zebra.app` , `/Applications/TrollStore.app/` , `/var/containers/Bundle/Application/TrollStore.app` , `/Applications/checkra1n.app` , `/var/jb/Applications/Cydia.app` , `/var/jb/Applications/Sileo.app` , `/var/jb/Applications/Zebra.app` , `/Library/MobileSubstrate/DynamicLibraries/LiveClock.plist` , `/Library/MobileSubstrate/DynamicLibraries/Veency.plist` , `/private/var/lib/apt` , `/private/var/lib/cydia` , `/private/var/mobile/Library/SBSettings/Themes` , `/private/var/stash` , `/private/var/tmp/cydia.log` , `/System/Library/LaunchDaemons/com.ikey.bbot.plist` , `/System/Library/LaunchDaemons/com.saurik.Cydia.Startup.plist` , `/usr/bin/sshd` , `/usr/libexec/sftp-server` , `/bin/bash` , `/Library/MobileSubstrate/MobileSubstrate.dylib` , `/var/containers/Bundle/tweaksupport` , `/var/mobile/Library/palera1n` , `/var/mobile/Library/xyz.willy.Zebra` , `/var/lib/undecimus` , `/var/jb/basebin` , `/var/jb/usr` , `/var/jb/etc` , `/var/jb/Library` , `/var/jb/.installed_palera1n` , `/var/binpack/Applications` , `/var/binpack/usr` , `/var/containers/Bundle/Application/trollstorehelper` , `/var/containers/Bundle/trollstore` , `/var/jb/preboot` , `/var/jb/var`
- Checks if directories are symlinks: `/var/lib`, `/Library`, `/usr/lib`, `/usr/bin`, `/bin`
- Iterates process list, looking for presence of:
`sshd`, `frida-server`, `debugserver`, `substrate`, `substituted`, `SSLKillSwitch`, `cycript`, `jailbreakd`, `lldb`
- Scans own environment variables `DYLD_INSERT_LIBRARIES` for `basebin/systemhook.dylib`
- Detects jailbreak-related services listening on ports: 22, 27010, 4444, 8022
- Checks if `P_TRACED` flag set for process, debugger detection.

### Virtualization Detection

While this isn’t new or unique to Coruna variants, we took a closer look at this aspect and found techniques that haven’t been disclosed in this context before.

- Check `_COMM_PAGE_CPU_CAPABILITIES64` if `kHasARMv8Crc32` flag is set on `_COMM_PAGE_CPUFAMILY` : `CPUFAMILY_ARM_CYCLONE` , `CPUFAMILY_ARM_TYPHOON` , `CPUFAMILY_ARM_TWISTER` . Emulated environment likely has that flag enabled on architectures that don’t support it.
- Check if `_COMM_PAGE_CACHE_LINESIZE` is equal to 128.
- IORegistry check for IOPlatformSerialNumber == "CORELLIUM" also documented in official Corellium documentation: [https://support.corellium.com/getting-started/distinguishing-a-virtualized-device-from-a-physical-device](https://support.corellium.com/getting-started/distinguishing-a-virtualized-device-from-a-physical-device)

### Updated Configuration

*Note: This config is not in its original form; it has been modified by us in order to show decrypted values for bundle IDs.*

### IOCs

| URLS | Notes | 
|---|---|
| noblegood\[.\]cc | Contained mix of Coruna and DarkSword | 
| http://greatweeeeb\[.\]com/static/report\[.\]html | N/A | 

| File | SHA256 | 
|---|---|
| report.html | fe500c68b48d164340d5f9671875900835cda5087a44b45663dab7deda89e8ea | 
| 399acf85aab3fcc5994fa191ee9ab2f6796b5be7.js | 33e7b049c267b1d14466077d4a59e8b559ecc390bf93ca6a444a4f7b2a5b1a8e | 
| 0fda9499b4a28b0852724141b687b512590207ad.js | 30976300ebd357033876969cdeec4faa17428c77d1b68d8fa4e1c3f9052fa526 | 
| 6146c119a7ec6ff367d0c735ddc6e46839ff09e2.js | d75efcc93aa0a7f7192731db6416600346c07593e0282dc5d6642c709108d186 | 
| bcecd7b9974ad7d4642e56b4677a13b467d2a9a8.js | 3fa6b825e113f51288aa91c908f1457699b6308d7140bdaaf2c9267356cd0a0a | 
| cbef8611084a7f83603a3c924a060dbb36fce035.js | 4e1ee68c9fa53333e86b1d30065d3948c87a2a9aca5a84a8077c907b8fb37f63 | 
| 4a42f9584da12c36362dd1e5b8bb03d6074aa74f.js | 0aa7c89780829a90629d4a0b28e6029ba7d0befbf273c451b39aa5b4309ec3be | 
| cd5f6717449048746c51c54c3029bcd5f730dae0.min.js | 0cd214510c0c3fd0a85acc22b0c6b2d6c54f62e760c8a48e19e35c79af3fc8ae | 
| shellcode.bin | f3d958350be201eda4bd226537809b68747709ee038263bede953e42bdde0800 | 
| bcecd7b9974ad7d4642e56b4677a13b467d2a9a8.bin | 96bc3008fbc2229d66eb51fcd11693377fe54d87d250be2172752541b180b3fb | 
| cbef8611084a7f83603a3c924a060dbb36fce035.bin | 33ed4d75902cb3f80b768bd1660b46ac1bbd662c16c8f0cfe990611150a39c57 | 
| 4a42f9584da12c36362dd1e5b8bb03d6074aa74f.bin | ad68e6db20e7d3d5d1630e9e694e2b85e313089a73ee7d71627d94747232d81d | 
| +Y85hbjoaOqtr06G\_\_OneSignalPush.dylib | 1b3ed0be667702c6026af9d0cde758721671d27a79dc13d99e7d1573d33e9092 | 
| 0y47\_qgAvX6quQD9i\_Hp\_\_ReachabilitySwift.dylib | d98bff98ad73c72589988c6ca67e5225fe5ae4208a82d6f10c69b7460c39dc88 | 
| 3aBLgZLpW1Yu7qbp\_\_IQKeyboardRetainer.dylib | fb6b831c33874010e0b58cd80b71621868b754d7be9962d2351c4a77e149b3ca | 
| 7Gl5gBi37m06q8g0\_\_BranchDeepLinker.dylib | e5fcb7f17224be5eeba80fc5011bc68fe79507a1d801057ff6e397bc98c18fde | 
| 8bKFe2o9cEwhtg6v\_\_FSCalendarCore.dylib | 7298d988c20fb93b5bd930b92d22bcbcbd62f37b4011d20710ca7d55828bfa61 | 
| A8OOWYyP7UCtmAbb\_\_LottieAnimation.dylib | 9c6bdc05ac415e702c97999961217dc76562bc0013941b02c33ee6db318e3bea | 
| B3f9XM1b3SusCHOM\_\_CocoaLumberjack.dylib | 7a45fed7bbafc32c6b0709cf7afc54d9c30de4c36ebff30806caaa5880e3eff2 | 
| B9vD+QU7nvwxAD19\_\_DGActivityIndicator.dylib | 52f438dd66067a9299e116ee49306d8359d41434f984712f223bd1a3bf317401 | 
| BGw5CKzDN0BMRRlK\_\_PINRemoteImage.dylib | 61e59740c44c84c4d1725662de1bb43bbbe640a7212887ab38b0a029f157c5d8 | 
| config.json | 9bb0ff78989f9a938baade3cf627c3a15534fc6dd7bba658c0a2f0a429a293f1 | 
| dj97gGdV8FFuUg1S\_\_libSystemPowerAssertion.dylib | 58f15d26d42150b5b40ca0f97d4901c7c0794b23341a6bae5271385b417d4390 | 
| gADATrgSk1+19Lzm\_\_MoyaProvider.dylib | 5bb333215a9a487d7f3290bbf7236682140894f4e04a30895a0cf64f7567e38a | 
| I4nAh6+ZLsERFV6c\_\_WeChat.dylib | a75a12c8e3b7f77fba26c6f97c4ad8b1d553c3f2cbe3b1086f3afea8625c99e3 | 
| il8TnQPKCEuUf6XO\_\_webclip.dylib | 4b6413e44b3a938536c01b05a3db19107de697b997a73e9cbb5da2d759ffb227 | 
| item\_27\_\_libAggregateDictionaryClient.dylib | ee886bf08a657a1886b2d003b9def81ebd93fc33f90e2dc79218a5aaec5a25aa | 
| KcD3c6WLYNOl\_9KFzSyp\_\_libFLAnimatedImageSupport.dylib | 36d677298a418d3dd51cbb311720e1fa570deb9d1d06d0c298e92ac338e60973 | 
| ksJW6NZ5yVOO1\_W4MtgG\_\_SkeletonViewLoader.dylib | a4a645be8b734e4f28f5ba38e6a8b34a1f06d053a0dcbafc7d9f5d4c9eea9219 | 
| ouiP7jReNxW\_rbz0sEip\_\_SegmentIntegration.dylib | b31067b9be5f37f525fc918a9173f741004f621bcb2a4b72319f9ffc6861eba7 | 
| ph.telegra.Teleg\_\_libSystemPowerAssertion.dylib | a1a206986901016e3342b7db9eb55d31bfa0dfff08718b33b837fcacb868f613 | 
| plDPQ9CdIKeezPgD\_\_DatadogMonitor.dylib | 1f439722fe7e96b74efbbee0f7c22f0292cd4abcfa47b581c007c2c9a511fd83 | 
| qnBLPYULctL7oa47\_\_ChameleonFramework.dylib | fe9ad37b8838b3f0e3e348520a4c128b0c5482a73c9f545ac8254121e8175cc3 | 
| SNsTvm6v7JFXbcsO\_\_ObjectMapperModel.dylib | 5ee2deaa28ef7d904b71e6ebe03602bdf22b2e152512d209e3203f8231542f9b | 
| SxHDH1pdnMrGP9Jw\_\_TextureDisplay.dylib | 3762e51d72e5fda9bf055e4521059976f49327430717062c2554b21e67235550 | 
| UrFIkawbmfnSLZwP\_\_whatsapp\_notnotify.dylib | d6bce6aaca10a32cf7afe16d8df2dd5cf3332b953fd8ca5d621c7fa6966b7586 | 
| v4IgYLx9BWXKvJhe\_\_libSnapKitLayoutHelper.dylib | c080ddea42f90f10aa84b83fb534ab51b901c60df6771d628a2fde4644b1acb9 | 
| VcuMCER1u8P7sSxL\_\_SAMKeychainStore.dylib | f9620f6e32411666050bd22a90125b1cbe4de3188c42d280448c526e36befe18 | 
| WqZI4gsTKzrI7WAC\_\_MarqueeLabel.dylib | c76ccfaf6462cb87c411f13b4834f20397072a2f577e8bdcd1b74a4e70162150 | 
| Xwl3u7mbSbsksFqH\_\_AdjustEventTracker.dylib | f0ac8ec4b5f1da03507ca6c8bfe0859df6e4c7273a65ca63d373101a0b0a6a65 | 

# DarkSword

Before our disclosure of the DarkSword exploit, we made sure that no domains serving it were still active and that it couldn’t be dumped in the wild. Because the entire exploit is written in JavaScript, repurposing and modifying it is extremely easy. Unfortunately, DarkSword’s source code was leaked by a third party not involved in the initial disclosure soon after our joint publication with Google and Lookout. Since then, we have seen multiple clusters of variants.

We observed multiple unsuccessful, likely LLM-assisted attempts to update the framework to support iOS 26.x.

Most of the new variants are focused on:

- Stability and reliability of exploitation.
- Stealth — no more syslog entries, no more logging via web requests.
- Quality, quantity, and format of stolen data.

Most of the old IOCs are still valid; below you can find new filesystem artifacts and log entries we haven’t blogged about before.

### Filesystem artifacts (static analysis)

| File | Notes | 
|---|---|
| /private/var/tmp/.lab\_device\_uuid | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/ioslab\_ctl | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/tmp/ioslab\_ctl2 | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/ioslab\_pe\_stage | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wifi\_dump.done | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/keychain\_copied.done | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/ioslab\_s5\_ok | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/ioslab\_pe\_reached | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wallet\_crypto\_hooks.txt | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wallet\_crypto\_hooks.txt | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wallet\_crypto\_hooks.done | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wallet\_memory\_heap.txt | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/wallet\_memory\_heap.done | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/.ghost\_upper/upper\_impl.js | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/.ghost\_upper/manifest.json | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/.ghost\_device\_uuid | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/.com.apple.analyticsd.metrics | Unique to: 47\[.\]80\[.\]242\[.\]98:443 (HTTPS), dsw.webtest\[.\]eu\[.\]cc:443 (HTTPS) | 
| /private/var/tmp/keychain\_extractor.host-status.json | Unique to: 47\[.\]129\[.\]224\[.\]84:443 (HTTPS), darksword\[.\]bitbrowserpro\[.\]com:443 (HTTPS) | 
| /private/var/tmp/keychain\_bundle.complete.json | Unique to: 47\[.\]129\[.\]224\[.\]84:443 (HTTPS), darksword\[.\]bitbrowserpro\[.\]com:443 (HTTPS) | 
| keychain\_dump.txt | /tmp/, /var/tmp/, /private/var/tmp/, /var/root/, /private/var/root/, /var/db/, /private/var/db/, /var/log/, /private/var/log/, /var/run/, /private/var/run/, /var/Keychains/, /private/var/Keychains/, /var/keybags/, /private/var/keybags/ | 
| keychain\_dump2.txt | /tmp/, /var/tmp/, /private/var/tmp/, /var/root/, /private/var/root/, /var/db/, /private/var/db/, /var/log/, /private/var/log/, /var/run/, /private/var/run/, /var/Keychains/, /private/var/Keychains/, /var/keybags/, /private/var/keybags/ | 
| /private/var/mobile/Media/PostLogs.txt | Common eg. 3z4\[.\]xyz, a\[.\]buffbuff\[.\]cam, web3a\[.\]cc, t3ios\[.\]com | 

### UnifiedLogs (forensic analysis)

We observed new sandbox failure log entry related to DarkSword:

`Sandbox: mediaplaybackd(245) deny(1) file-write-create /private/var/tmp/darksword.log`

# What’s next?

At the upcoming LABSCon 2026 conference, Kevin Hoganson and Mateusz Krzywicki will discuss threat hunting across variants of Coruna and DarkSword, with an in-depth look at a new interesting DarkSword variant featuring many new IOCs, on-device behavior, exfiltration techniques, and infection domains. Expect to hear from us soon!

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
