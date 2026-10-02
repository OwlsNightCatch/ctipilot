---
title: Bitget hacked via zero-day in third-party security products
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/
hostname: bleepingcomputer.com
description: Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products.
sitename: BleepingComputer
date: "2026-09-30"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Bitget, Breach, Crypto Exchange, Crypto theft, CryptoCurrency, Hack, Zero-Day,virus removal, malware removal, computer help, technical support']
---
Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products.

According to [Bitget](https://x.com/bitget/status/2105147238804537496), two separate investigations by blockchain security firm SlowMist and Google Cloud's cyber-defense arm Mandiant said the threat actors accessed Bitget's wallet environment after compromising two security appliances with zero-day exploits.

After the breach, the attackers dropped web shells on one of the hacked appliances and malware on the crypto exchange's production wallet job server, as well as a custom withdrawal tool used to launch the cryptocurrency theft after midnight on September 25.

"The earliest malicious activity identified in the available logs dates to August 31. A service running on one of Product A's nodes was affected by a zero-day vulnerability. The attacker ran a hidden script under the service process, launched a command to read the environment variable containing the database password, and connected to the database. Similar hidden-script activity was observed on two other nodes on September 23 and September 25," [SlowMist said](https://github.com/slowmist/Knowledge-Base/blob/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf).

"Forensic findings indicate that on September 24, 2026, a threat actor gained unauthorised privileged access to Bitget's third party security appliances A and B. The threat actor deployed a web shell onto the security appliance B and established a Command-and-Control (C2) connection. Using the persistent access on security appliance B, the threat actor moved laterally to Bitget's production wallet job server and deployed malicious packages," [Mandiant added](https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf).

SlowMist added that the earliest crypto theft transfer occurred on September 02:31 (UTC+8) and the last took place at 05:23, with the attack spanning nearly 3 hours across multiple blockchains.

Bitget suspended all withdrawals on Thursday after detecting multiple unauthorized transfers from its hot and warm crypto wallets and discovering that [attackers had stolen $387.5 million](https://www.bleepingcomputer.com/news/security/hackers-steal-3516-million-in-bitget-crypto-exchange-hack/) from them.

CEO Gracy Chen [noted](https://x.com/GracyBitget/status/2103359775723626736) the incident affected multiple assets, including ETH, XRP, BNB, AVAX, USDT, USDC, and other tokens, and involved the Ethereum, XRP Ledger, Arbitrum, Avalanche, Optimism, BSC, and Base chains.

Chen also [blamed the attack](https://x.com/GracyBitget/status/2103359775723626736) on North Korean hackers, citing IP behavior patterns and on-chain analysis as evidence, and added that they breached a critical backend system within Bitget's wallet infrastructure that was later used to spoof transaction data, triggering the exchange's authorization process to move funds out of compromised hot/warm wallets.

North Korean hackers have been behind many other major crypto heists, including the [Bybit hack](https://www.bleepingcomputer.com/news/security/fbi-confirms-lazarus-hackers-were-behind-15b-bybit-crypto-heist/), in which they [stole $1.5 billion](https://www.bleepingcomputer.com/news/security/hacker-steals-record-146-billion-from-bybit-eth-cold-wallet/) from the crypto exchange's ETH cold wallet.

Since the breach, Bitget has [launched a Recovery Bounty Program](https://www.bitget.com/support/articles/12560603896108#:~:text=The%20Bitget%20Recovery%20Bounty%20Program) that offers bounties of 5% to those who help recover or freeze funds stolen in the attack.

A Bitget spokesperson was not immediately available when BleepingComputer contacted them earlier today for more information on the zero-day flaw and the third-party security products compromised in the attack.

## 
            [Build your security blueprint for AI-powered attacks](https://hubs.li/Q04x67m50)
        

        Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed.

[Save your seat](https://hubs.li/Q04x67m50)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
