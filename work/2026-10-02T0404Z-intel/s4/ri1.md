---
title: XCTDH Adopts Hash Hiding
author: Ransom-ISAC; Ellis Stannard; Nick Smart
url: https://ransom-isac.org/blog/xctdh-adopts-hash-hiding/
hostname: ransom-isac.org
description: A blockchain-based C2 technique discovered in the XCTDH campaign's September 2026 evolution, where C2 addresses are steganographically encoded in Ethereum transaction destination addresses.
sitename: Ransom-ISAC
date: "2026-09-25"
categories: ['Threat Intelligence']
tags: ['ransomware,threat intelligence,cybersecurity,ISAC,security community,ransomware defense', 'DPRK', 'HashHiding', 'Blockchain', 'Ethereum', 'XCTDH', 'APT']
---
## Context

Ransom-ISAC first documented this DPRK-attributed campaign in October 2025, in a four-part series on **Cross-Chain TxDataHiding (XCTDH)** ([four-part XCTDH series](https://ransom-isac.org/blog/cross-chain-txdatahiding-crypto-heist/)). In that work, malware payloads are hidden in BSC blockchain transaction calldata and retrieved through a TRON and Aptos indexing layer.

The Ethereum recipient-address encoding described in this report was also documented publicly as [NullReceiver by OpenSourceMalware in August 2026](https://opensourcemalware.com/blog/nullreceiver-dprk-c2-technique). We credit that work for the technique and the name. Ransom-ISAC tracks the wider XCTDH campaign that uses it, which we first documented in October 2025 and still track today. The analysis below is our own, and it is built on 90 days of on-chain collection. The on-chain record shows the first beacon on 23 June 2026, several weeks before that public disclosure. The campaign delivered DEV#POPPER.js (a cross-platform Node.js RAT) and OmniStealer (a Python-based credential harvester targeting 153 wallet targets, browsers, password managers, and cloud storage).

During analysis of the campaign's **September 2026** samples, we identified a new JavaScript module (`_Z`) in the C2's `/init` response that was not present in the October 2025 report. After deobfuscating 69,470 characters of CFF-obfuscated code, we found the campaign using the Ethereum mainnet for C2 address distribution. This method places the C2 address in a different location from both EtherHiding and TxDataHiding.

## How the Existing XCTDH Chain Works

To understand what HashHiding adds, it helps to see the existing attack flow. In the XCTDH campaign, malware payloads are delivered via a multi-chain resolution process:

1. The malware queries a **TRON** wallet (e.g.`TMfKQEd7TJJa5xNZJZ2Lep838vrzrs7mAP` ) for its latest transaction, with**Aptos** as a fallback
2. The TRON transaction's `raw_data.data` field contains a hex-encoded, reversed BSC transaction hash
3. The malware decodes and reverses this to get a **BSC** transaction hash (e.g.`0xf46c86c886bbf99...` )
4. It calls `eth_getTransactionByHash` on BSC RPC nodes to fetch the BSC transaction
5. The BSC transaction's `input` field contains kilobytes of encrypted JavaScript, the actual malware payload
6. After XOR decryption, the payload is executed via `eval()` or spawned as a detached process

This is **TxDataHiding**: large payloads hidden in the `input` (calldata) field of blockchain transactions, with a cross-chain indexing layer for indirection. It delivers full malware stages: RAT loaders, dropper code, and persistence mechanisms.

The limitation is that this chain requires specific TRON/Aptos wallets and BSC transactions to be reachable. If those RPC endpoints are blocked or the wallets are flagged, the chain breaks. HashHiding was built to solve that problem, not as another payload delivery mechanism, but as a lightweight **C2 address recovery channel** that can bootstrap the entire infection from scratch.

We first documented this actor in our XCTDH series, and a year on they are still live with very few changes. The September 2026 samples show a fourth blockchain, Ethereum, used as a C2-address recovery channel. We track this channel as **Hash Hiding**.

*The sender address was fetched in order to obtain the recipient address that carries the encoded C2 endpoint.*

This does not look out of the ordinary unless you have been following this code along the way. The code itself uses base16 obfuscation and fetches two characters for each byte of an IP address and port.

*CyberChef recipe decoding the recipient address into an IPv4 address and port.*

## The HashHiding Technique

HashHiding takes a fundamentally different approach. Instead of hiding large payloads in transaction data, it encodes an IPv4 address and port, six bytes in total, directly into the `to` address of plain Ethereum coin transfers. No smart contracts, no calldata, no input data. The `to` field is a 20-byte value, and the malware reads the first six bytes as the C2 endpoint it needs:

```
to = 0xB5D6959401bbb5D69594005000ff8C84e0b715b1
       ││││││││││││
       ││││││││└┴┴┴── Port:  01bb → 443
       └┴┴┴┴┴┴┴────── IP:    B5.D6.95.94 → 181[.]214[.]149[.]148
The remaining bytes hold a secondary endpoint and padding. The malware reads only the first here.
The address is fabricated. Nobody holds the private key.
Most transfers send 0 wei. A few send 150 wei. The value is burned.
```
The decoding in JavaScript:

```
// IP: 4 hex pairs → 4 decimal octets
tx.to.substring(2, 10).match(/.{2}/g).map(h => parseInt(h, 16)).join('.')
// Port: 2 hex bytes → decimal
parseInt(tx.to.substring(10, 14), 16)
// Result: "hxxp://181[.]214[.]149[.]148:443/boot"
```
| Technique | Data Location | Capacity | Transaction Type | Purpose | 
|---|---|---|---|---|
| EtherHiding | Smart contract storage slots | Large payloads (KB) | Contract call ( `eth_call` ) | Malware delivery | 
| TxDataHiding / XCTDH | Transaction `input` / calldata | Large payloads (KB) | Contract call or data TX | Malware delivery via cross-chain index | 
| HashHiding | Transaction `to` address hash | 6 bytes (IP:PORT) | Plain coin transfer (150 wei) | C2 address recovery | 

The key distinction: TxDataHiding delivers **payloads** (full malware code). HashHiding delivers an **address** (where to fetch payloads from). They solve different problems and complement each other in the campaign's architecture.

## Where HashHiding Sits in the Kill Chain

In the October 2025 campaign documented by Ransom-ISAC, the attack chain began with a weaponised repository file (e.g. `tailwind.config.js`) that executed two Cross-Chain TxDataHiding fetches from BSC. One of those BSC payloads delivered a blockchain-based RAT fetcher, which downloaded the DEV#POPPER.js RAT, a 530-line cross-platform Node.js Remote Access Trojan with full RCE capabilities and VSCode/Cursor IDE injection for persistence. The other BSC payload delivered an HTTP stager that fetched `/$/boot` from the hardcoded C2, which in turn acted as a Python dropper: it installed Python silently on the victim's machine, then used it to fetch `/$/z1`, the OmniStealer payload, a 3,500-line Python credential harvester targeting browsers, crypto wallets, password managers, and cloud storage across Windows, macOS, and Linux.

In the September 2026 samples, this architecture has been restructured. The BSC transaction chain no longer delivers the RAT and dropper directly. Instead, the BSC payload now calls a new `/init` endpoint on the C2 server, which returns a JSON object containing four components: `_U` (C2 base URL), `_H` (bootstrap code), `_B` (the RAT itself), and `_Z`, the HashHiding module. All four are delivered in a single HTTP response, rather than through separate blockchain fetches and HTTP requests as in the earlier campaign.

`_B` is the **DEV#POPPER RAT** itself: a roughly 2,500-line Node.js RAT with WebSocket C2 communications, keylogging, clipboard monitoring, shell spawning and full remote code execution, a much larger build than the 530-line October version. When `_B` executes, it unconditionally extracts `_Z` from the `/init` JSON (`NtuXTb = ZtoHUM._I?._Z`) and concatenates it onto the code of every detached child process it spawns. The only gate is an anti-double-run flag (`global._t_h`). This means `_Z` runs on **every infection**, in parallel with the RAT, from the moment `_B` executes. It is not behind any "if the other channels failed" branch.

`_Z` operates independently of both the DEV#POPPER.js RAT and the OmniStealer dropper chain, but it is launched **by** `_B`, not alongside it. In the payload numbering, `_Z` sits at `Payload1_1_1_Z`, a sub-component of `_B` (the RAT, `Payload1_1_1`), which is itself loaded by the `/init` JSON fetcher (`Payload1_1`, BSC TX `0x84e8ce`), which is fetched from the BSC contract (`Payload1`). The October 2025 campaign had two parallel first-stage paths. The September 2026 campaign restructures this into a unified `/init` endpoint that bundles the RAT, the dropper, and the HashHiding scanner into a single response: three parallel channels, all always-on, launched together.

The BSC contract address remains the same (`0x9bc1355344b54dedf3e44296916ed15653844509`), confirming continuity of the underlying XCTDH infrastructure even as the delivery architecture evolves around it.

## Discovery: The _Z Module

HashHiding was found inside `_Z`, a 69,470-character JavaScript module delivered by the XCTDH campaign's `/init` endpoint. After deobfuscating two layers of protection (base-91 string encoding with 18 custom alphabets, and generator-based Control Flow Flattening), `_Z` reduces to 8,777 bytes of clean code that does one thing: **scan Ethereum mainnet for the current C2 address**.

`_Z` runs as a detached, hidden background process. Its logic:

1. Picks a random public ETH RPC endpoint (`publicnode[.]com` ,`drpc[.]org` , or`blastapi[.]io` )
2. Gets the current block number
3. Searches blocks using exponential offsets: 0, 1, 2, 4, 8, … 4096 × 256 blocks back
4. For each block, scans all transactions for `tx.from.includes('33ff3edaf55a8e03dcbc7cb40d498a49')`
5. When found, decodes IP:PORT from `tx.to` and fetches`/boot` from the decoded C2
6. Spawns the response as a new detached Node.js process, rebuilding the infection chain

## Active Heartbeat

The signal wallet (`0x33ff3edaf55a8e03dcbc7cb40d498a49cd499891`) is an actively maintained channel, not dormant infrastructure. It sent 2,655 outbound transactions between 23 June 2026 and 21 September 2026, and it still beacons. The current `to` address encodes `181[.]214[.]149[.]148:443`. Most transactions carry 0 wei and a few carry 150 wei, which keeps the gas cost low. The steady stream keeps a fresh signal in recent blocks, so `_Z`'s exponential search always finds a recent beacon whatever block it samples.

To rotate C2, the operator sends transactions to a **new** `to` address encoding the new IP:PORT. Every infected machine picks up the change on its next scan.

## On-Chain IOC Timeline

We queried the full outbound history of the signal wallet `0x33ff3edaf55a8e03dcbc7cb40d498a49cd499891` on Ethereum mainnet. The wallet sent 2,655 beacon transactions. The first beacon was on 23 June 2026. The last beacon in this data set was on 21 September 2026. The channel ran for about 90 days and it is still active.

*Beacon volume over the 90-day collection window, with the four observed C2 rotations.*

Each beacon pays a fabricated `to` address. Bytes 1 to 6 encode the primary C2 endpoint, an IPv4 address and port 443. Bytes 7 to 12 encode a secondary endpoint, the same IPv4 address and port 80. The last 8 bytes are padding. The observed decode logic reads the primary endpoint.

The operator rotated the encoded C2 address four times in 90 days. Each `to` address is a separate IOC. The table lists them in time order.

| Period (UTC) | Encoded to address | Decoded C2 | Beacons | 
|---|---|---|---|
| 23 Jun 2026 15:21 to 24 Jun 2026 15:32 | `0x171B14bB0050171b14Bb01BB398EAAB6441Fbd47` | `23[.]27[.]20[.]187:80` | 55 | 
| 24 Jun 2026 16:04 to 03 Sep 2026 14:53 | `0x171B14bb01bB171B14BB0050EB7f39C35C47E682` | `23[.]27[.]20[.]187:443` | 1,987 | 
| 03 Sep 2026 15:39 to 07 Sep 2026 13:52 | `0xB5D6959301bbB5D69593005000FfABa8a5A2ADA2` | `181[.]214[.]149[.]147:443` | 111 | 
| 07 Sep 2026 14:43 to 21 Sep 2026 21:25 | `0xB5D6959401bbb5D69594005000ff8C84e0b715b1` | `181[.]214[.]149[.]148:443` | 502 | 

The IP address stayed on `23[.]27[.]20[.]187` for the first two rotations. The operator changed only the primary port, from 80 to 443. In September 2026 the operator moved to a new IP block. The C2 went to `181[.]214[.]149[.]147`, and then to `181[.]214[.]149[.]148`. The current `to` address matches the IOC listed above.

**Single-byte rotation.** The last two C2 addresses differ by one byte. `181[.]214[.]149[.]147` became `181[.]214[.]149[.]148`, a change of one in the final octet. In the encoded `to` address this is a single hex change, `0x93` to `0x94`. A one-byte change like this is hard to see by eye in a list of indicators. It is likely deliberate. A near-identical successor IP can slip past a manual review, and past any blocklist that holds only the previous address.

**Beacon cadence.** The mean interval between beacons is about 49 minutes. The median is about 51 minutes. This is close to one beacon every 50 minutes, or about 29 beacons per day. Most beacons carry 0 wei. A few carry 150 wei. The gas cost per beacon is low, and the beacons keep a fresh signal in recent blocks.

**Always-on parallel channel.** The Ethereum HashHiding channel is not a failover that waits for other channels to fail. It runs unconditionally on every infection, in parallel with the hardcoded C2 and the TRON/Aptos/BSC chain. The BSC contract `0x9bc1355...` stores the malware payloads. The Ethereum signal wallet delivers only the current C2 address. Because `_Z` always runs, if the hardcoded IP is blocked or the BSC chain is disrupted, the malware already has an independent path: it reads the latest `to` address from Ethereum and rebuilds the infection from `/boot`. The on-chain record shows a stable operator. The operator kept the same wallet, the same BSC contract, and the same XOR key for the whole 90 days. The operator changed only the encoded C2 address.

**Assessment.** This four-chain design shows a high level of creativity and strong resourcefulness by the DPRK operator. The actor uses Ethereum, TRON, Aptos, and BSC together, and each chain does one clear job. The actor keeps all three C2-resolution channels active in parallel for 90 days at a very low cost. The actor rotates the C2 address with no change to the malware code. This is a deliberate and mature use of public blockchain infrastructure.

**New indicators from this analysis.**

- Historic C2 IP `23[.]27[.]20[.]187` , on ports 80 and 443
- Historic C2 IP `181[.]214[.]149[.]147` , on port 443
- Historic encoded `to` addresses, as listed in the table above

## Role in the Attack Chain

HashHiding is one of three **parallel, always-on C2 resolution channels** in the September 2026 campaign. All three run simultaneously from the moment of infection, and none waits for the others to fail:

1. **Hardcoded IP.** The C2 address (`181[.]214[.]149[.]148:443` ) is baked into payloads at delivery time. Fast and direct. Blocking the IP kills this channel, but the other two continue.
2. **XCTDH (TRON/Aptos → BSC).** The malware resolves a C2 by querying TRON (or Aptos) for a BSC transaction hash, then fetching encrypted payloads from BSC calldata. Spans three blockchains with immutable transactions. Requires specific wallet addresses and RPC endpoints to be reachable.
3. **HashHiding (Ethereum mainnet).**`_Z` scans recent Ethereum blocks through any of three public RPC providers, finds a dust transaction from the operator's wallet, and decodes the current C2 from the`to` address. Nearly impossible to block: Ethereum mainnet is decentralised and immutable, the RPC endpoints are public infrastructure, and there are no smart contracts to delist or wallets to freeze (the`to` address is fabricated and holds no funds).

The resilience comes from **redundancy, not sequencing**. Because all three channels are active at once, a defender must disrupt all of them simultaneously to cut off C2 communication. Blocking the hardcoded IP does nothing if the XCTDH and HashHiding channels are still live. Taking down specific RPC endpoints does nothing if the malware rotates to another provider. The architecture is designed so that any single channel can independently rebuild the full infection chain.

This gives the campaign a **four-blockchain architecture** spanning Ethereum, TRON, Aptos, and BSC, with each chain serving a distinct function: Ethereum for C2 signaling, TRON/Aptos for indexing, and BSC for payload storage.

## The New Kill Chain

*The full September 2026 XCTDH kill chain. Delivery runs through Telegram social engineering, a weaponised GitHub repository, and trojanised NPM and OpenClaw libraries. The obfuscated loader extracts TRON and Aptos addresses, XOR keys and API endpoints, then retrieves payloads from BSC calldata via `eth_getTransactionByHash`. **Chain 1** fetches `/init` on port 443 and evaluates `_B` (the RAT) and `_Z` (the HashHiding scanner). **Chain 2** fetches `/$/boot`, installs Python 3.13 and 7-Zip, then pulls OmniStealer from `/$/1`. Both persistence loops return to `/init`.*

**Step-by-step:**

1. **Delivery.** The victim receives a fake job offer via Telegram, directing them to a GitHub repository or a trojanised NPM package. The repository contains a weaponised file (for example`config.js` ) with the malicious payload hidden after kilobytes of whitespace padding, appended after a benign`export default config;` line.
2. **Initial Code.** The hidden payload (`global.i = '5-3-132'` ) runs an obfuscated loader that uses two string-shuffling functions (`lyR` and`TpC` ) to decode and execute the next stage. The loader queries two TRON wallet addresses for their latest outbound transactions, with Aptos as a fallback for each.
3. **Cross-Chain Resolution.** Each TRON wallet's latest transaction contains a hex-encoded, reversed BSC transaction hash in its`raw_data.data` field. The loader decodes and reverses this to obtain two BSC transaction hashes, one per chain. It calls`eth_getTransactionByHash` on BSC RPC nodes (`bsc-dataseed.binance.org` ) to fetch each transaction. The`input` (calldata) field of each contains kilobytes of XOR-encrypted JavaScript.
4. **Chain 1 — RAT and HashHiding (eval path).** The first BSC payload (TX`0x84e8ce...` , XOR key`2\[gWfGj;<:-93Z^C` ) decrypts to a loader that sets the C2 to`http://181[.]214[.]149[.]148:443` and fetches`/init` . The endpoint returns a 303KB JSON object, from which the loader evals`_B` .`_B` unconditionally extracts`_Z` from the same response and spawns it as a detached background process.`_Z` is the HashHiding scanner, which periodically scans Ethereum mainnet for the current C2 address encoded in transaction`to` addresses.
5. **Chain 2 — Dropper and OmniStealer (spawn path).** The second BSC payload (TX`0x610c9e...` , XOR key`m6:tTh^D)cBz?NM]` ) decrypts to a loader that sets the C2 to`http://181[.]214[.]149[.]148` on port 80 and fetches`/$/boot` with a spoofed`Python-urllib/3.13` User-Agent and a`Sec-V` header. The response is XOR-decrypted with key`ThZG+0jfXE6VAGOJ` to produce the Dropper, a 20KB JavaScript module that silently downloads and installs Python 3.13 and 7-Zip on the victim's machine. The Dropper then fetches`/$/1` , XOR-decrypts it, and executes it as a Python script. This is**OmniStealer** , a credential harvester targeting 153 wallet targets, browsers, password managers and cloud storage. It exfiltrates stolen data as an AES-encrypted ZIP archive via the Telegram bot API. It is one-shot: it runs once and does not persist.
6. **Re-bootstrap loops.** Two independent mechanisms keep the RAT alive through C2 disruption, both converging on`/init` .**ETH loop (from Chain 1):**`_Z` scans Ethereum mainnet blocks via public RPC endpoints for transactions from the operator's signal wallet (`0x33ff3edaf55a8e03dcbc7cb40d498a49cd499891` ). When it finds one, it decodes the C2 IP and port from the transaction's`to` address and fetches`/boot` , which returns`boot.js` ; that fetches`/init` and evals`_B` only, because`_Z` is already running.**BSC loop (from Chain 2):** the Dropper stores Chain 1's TRON address (`_t_1` ) and Aptos address (`_t_2` ) together with Chain 1's XOR key, and re-resolves the TRON to BSC path to retrieve the Chain 1 payload, which fetches`/init` again.

Neither re-bootstrap mechanism re-runs OmniStealer. The stealer is fire-and-forget.

## Evolution from October 2025

HashHiding was not present in the campaign documented by Ransom-ISAC in October 2025. The following changes were observed in the September 2026 samples:

| Aspect | October 2025 | September 2026 | 
|---|---|---|
| C2 IP | `23[.]27[.]20[.]143` | `181[.]214[.]149[.]148` | 
| C2 Port | 27017 (MongoDB, easily flagged) | 443 (blends with HTTPS traffic) | 
| C2 Resolution Channels | 2 parallel (Hardcoded IP + XCTDH) | 3 parallel (Hardcoded IP + XCTDH + HashHiding) | 
| Blockchains Used | TRON, Aptos, BSC | TRON, Aptos, BSC, **Ethereum mainnet** | 
| String Obfuscation | Character-shuffling arrays | Base-91 with 18 custom alphabets | 
| Control Flow | Standard obfuscator.io | Generator-based CFF | 
| BSC Contract | `0x9bc1355...` | `0x9bc1355...` (same) | 
| XOR Key | `2\[gWfGj;<:-93Z^C` | `2\[gWfGj;<:-93Z^C` (same) | 

The shared BSC contract and XOR key confirm the same operator. The addition of Ethereum as a fourth blockchain, and the shift from payload delivery (TxDataHiding) to lightweight C2 signaling (HashHiding), represents a deliberate architectural evolution: adding a redundant, always-on C2 recovery channel that operates independently of the existing infrastructure.

## Indicators of Compromise

### BSC Transaction Hashes (September 2026)

| BSC TX Hash | Chain | Decrypted Payload | 
|---|---|---|
| `0x84e8cecd5b077eef530e7d69d546e2555199cb61759d1224d31cb31750788f62` | Chain 1 | Sets C2 to `http://181[.]214[.]149[.]148:443` , fetches`/init` , evals`_B` | 
| `0x610c9ec972545b8df6e3aaecc7a8ab5f2f2445cf0bfbd6ee026e618d07b29e22` | Chain 2 | Sets C2 to `http://181[.]214[.]149[.]148` , fetches`/$/boot` with XOR key`ThZG+0jfXE6VAGOJ` and UA`Python-urllib/3.13` | 

**BSC sender** (same as October 2025): `0x9bc1355344b54dedf3e44296916ed15653844509`

### TRON Wallet Addresses

| TRON Address | Chain | Aptos Fallback | 
|---|---|---|
| `TCqf6ZkaQD84vYsC2cuu1jRwB6JveTaRrF` | Chain 1 (→ `/init` ) | `0x9d202c824402ca89e9aaccd2390b6f8b332ae743caa1469c695feb2781d56519` | 
| `TFMryB9m6d4kBMRjEVyFRbqKSV1cV2NcpH` | Chain 2 (→ `/$/boot` ) | `0x3d2075f97b7b1e3234bd653779d21c605d7d8c6ec9c98d983880be5c7f4f9471` | 

### XOR Keys

| Key | Used By | 
|---|---|
| `2\[gWfGj;<:-93Z^C` | Chain 1 BSC payload decryption | 
| `m6:tTh^D)cBz?NM]` | Chain 2 BSC payload decryption | 
| `ThZG+0jfXE6VAGOJ` | `/$/boot` response decryption | 

### C2 Endpoints

| Endpoint | Port | Returns | 
|---|---|---|
| `/init` | 443 | 303KB JSON containing `_B` (the RAT) and`_Z` (the HashHiding scanner) | 
| `/$/boot` | 80 | XOR-encrypted Dropper (installs Python 3.13 and 7-Zip, fetches OmniStealer) | 
| `/$/1` | 80 | XOR-encrypted OmniStealer | 
| `/boot` | 443 | ETH re-bootstrap only — returns `boot.js` , which fetches`/init` and evals`_B` | 

### Other Indicators

- **C2 IP:**`181[.]214[.]149[.]148`
- **ETH wallet (signal source):**`0x33ff3edaf55a8e03dcbc7cb40d498a49cd499891`
- **Current encoded C2:**`0xB5D6959401bbb5D69594005000ff8C84e0b715b1` →`181[.]214[.]149[.]148:443`
- **Wallet match pattern:**`33ff3edaf55a8e03dcbc7cb40d498a49`
- **Campaign marker:**`global.i = '5-3-132'`
- **UA spoofing:**`Python-urllib/3.13` (Node.js spoofing a Python request)
- **`/$/boot` custom header:**`Sec-V` (injection version marker)
- **OmniStealer build:**`B9=260924` (24 September 2026)
- **`_Z` version marker:**`/*RS260605*/`

**ETH wallet transactions:** all 2,655 outbound beacon transactions from the signal wallet, spanning 23 June 2026 to 21 September 2026, are available as a CSV: [eth_hashhiding_tx_hashes.csv](https://ransom-isac.org/data/blog/xctdh-adopts-hash-hiding/eth_hashhiding_tx_hashes.csv).

## Detection

- **Blockchain monitoring:** watch for`to` address changes from the signaling wallet; a new address means C2 rotation
- **Network:**`eth_getBlockByNumber` JSON-RPC calls to public ETH endpoints followed by HTTP requests to non-standard IPs
- **Endpoint:** Node.js processes with`-eval` flags containing`global.i=` and`global.r=require`
- **YARA:** match wallet prefix`33ff3edaf55a8e03dcbc7cb40d498a49` alongside`eth_getBlockByNumber` or`eth_blockNumber`

## YARA Rule

```
rule XCTDH_HashHiding_NullReceiver
{
    meta:
        description = "XCTDH / NullReceiver Ethereum HashHiding C2-resolution module (_Z), DPRK Contagious Interview"
        author = "Ransom-ISAC"
        date = "2026-09-25"
        reference_technique = "NullReceiver (OpenSourceMalware, Aug 2026)"
        reference_campaign = "XCTDH series (Ransom-ISAC, Oct 2025)"
        tlp = "CLEAR"
    strings:
        $init_i    = "global.i" ascii
        $init_r1   = "global.r=require" ascii
        $init_r2   = "global.r = require" ascii
        $marker    = "RS260605" ascii
        $wallet    = "33ff3edaf55a8e03dcbc7cb40d498a49" ascii nocase
        $rpc_pn    = "ethereum-rpc.publicnode.com" ascii
        $rpc_drpc  = "eth.drpc.org" ascii
        $rpc_blast = "blastapi.io" ascii
        $m_block   = "eth_getBlockByNumber" ascii
        $m_bnum    = "eth_blockNumber" ascii
        $dec_ip1   = ".to.substring(2, 10)" ascii
        $dec_ip2   = ".to.substring(2,10)" ascii
        $dec_port1 = ".to.substring(10, 14)" ascii
        $dec_port2 = ".to.substring(10,14)" ascii
        $boot      = "/boot" ascii
    condition:
        filesize < 4MB and
        (
            $marker or
            $wallet or
            (
                $init_i and any of ($init_r1, $init_r2) and
                (
                    2 of ($rpc_pn, $rpc_drpc, $rpc_blast) or
                    any of ($m_block, $m_bnum) or
                    any of ($dec_ip1, $dec_ip2, $dec_port1, $dec_port2)
                )
            )
        )
}
```
## Our XCTDH Series

This report builds on our earlier work on the XCTDH campaign, which we first documented in October 2025. The full series is below.

- [Part 1: A Very Chainful Process](https://ransom-isac.org/blog/cross-chain-txdatahiding-crypto-heist/) . The discovery of the technique and the takedown-proof C2 across TRON, Aptos, and BSC.
- [Part 2: The Malware Analysis](https://ransom-isac.org/blog/cross-chain-txdatahiding-crypto-heist-part-2/) . A full breakdown of the DEV#POPPER.js RAT and the OmniStealer payload across the kill chain.
- [Part 3: The Infrastructure](https://ransom-isac.org/blog/cross-chain-txdatahiding-crypto-heist-part-3/) . The adversary infrastructure, operational security, C2 clusters, and links to known threat groups.
- [Part 4: Following the On-Chain Activity](https://ransom-isac.org/blog/cross-chain-txdatahiding-crypto-heist-part-4/) . Tracking the campaign's on-chain activity across the blockchains it uses.

Facing a cyber security incident?

If you believe your organisation has been affected by the activity described in this report, please reach out to Ransom-ISAC.

Found this article helpful?

Share it with your network
