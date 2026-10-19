---
title: MediaMarkt pulls Ledger wallets as more spy implant reports emerge
author: Alex Lekander
url: https://cyberinsider.com/mediamarkt-pulls-ledger-wallets-as-more-spy-implant-reports-emerge/
hostname: cyberinsider.com
description: MediaMarktSaturn has withdrawn Ledger products from its stores following reports of hardware wallets containing unauthorized electronics.
sitename: CyberInsider
date: "2026-10-13"
categories: ['Hardware', 'News', 'Security']
fingerprint: "3d9eba95fb0df5cc"
---
MediaMarktSaturn has reportedly withdrawn Ledger products from its stores and online platforms following fresh reports of hardware wallets containing unauthorized electronics.

The situation has raised concerns beyond the company’s initial investigation into Southeast Asian reseller CryptoBilis.

The development comes as Ledger’s Donjon security team disclosed how an implant captures recovery phrases and sends them over cellular networks. In its October 13 update, Ledger said it is reviewing reports involving other devices and locations, while stressing that all confirmed fund losses tied to the incident disclosed on October 9 involve CryptoBilis purchases.

A MediaMarktSaturn spokesperson announced today that the group had removed the manufacturer’s products from physical and online sales channels and was contacting Ledger. The withdrawal follows a buyer’s claims that two wallets purchased at separate MediaMarkt stores contained suspicious components.

Ledger manufactures cryptocurrency hardware wallets that protect private keys and authorize transactions. Their recovery phrases allow owners to restore access to their assets, making theft of those words sufficient to compromise a wallet without taking control of its original device.

### Reports beyond CryptoBilis

X user [Johannes said](https://x.com/0xJohannes_/status/2109634513957527974) on October 12 that he found similar modifications in two MediaMarkt purchases, including additional cables and what he identified as an LTE module. He published a video of the second device’s unboxing and said he sent one unit to Ledger for examination. The devices’ purchase history and alleged implants have not been independently authenticated.

Separately, former Mt. Gox CEO [Mark Karpelès reported](https://x.com/MagicalTux/status/2109916873689280900) finding an implant inside a Ledger Flex that owner [Ben Yorke said](https://x.com/BenYorke/status/2109083315424891296) he bought from Metapod at Singapore airport. Yorke said the device had never been used. Karpelès published photographs and a teardown video, but the report does not establish where the modification occurred or connect it to the CryptoBilis thefts.

### Implant details emerge

According to [Ledger’s latest analysis](https://x.com/Ledger/status/2109896739985453358), the implant sits inside the enclosure and monitors information displayed on the screen. When the wallet shows its 24-word recovery phrase during setup, an added microcontroller decodes the words and transmits them over LTE using a provisioned eSIM.

Ledger says the implant operates separately from the wallet’s Secure Element and operating system, without modifying transactions or signatures.

This exposes a limitation of its authenticity verification: Ledger’s own [documentation states](https://support.ledger.com/article/4404382029329-zd) that Genuine Check cannot detect spying implants when the original Secure Element remains intact. A successful check therefore does not establish that a device contains no unauthorized hardware.

Ledger has not confirmed the total number of affected users or the value stolen, and says third-party estimates circulating online remain incompletely verified. It has also not verified a wallet drain involving a device purchased outside CryptoBilis.

CryptoBilis customers should leave unused devices uninitialized and contact Ledger Support. Those who already configured a device should promptly move assets to a new signer with a newly generated recovery phrase.

Owners of suspected tampered devices should contact Ledger Support and preserve the hardware for investigation. Ledger warns that disassembly can damage devices and that recovery phrases must never be disclosed to support agents or entered into websites, apps, or forms.

## Leave a Reply Cancel reply
