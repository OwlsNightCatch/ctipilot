---
title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
author: Wayne
url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
hostname: mozilla.org
description: ASSIGNED (naveen.ml) in CA Program - CA Certificate Compliance. Last updated 2026-11-11.
sitename: bugzilla.mozilla.org
date: "2026-10-18"
fingerprint: ed4aa51c503635de
---
[Bug 2083449](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449)Opened 24 days ago Updated 7 hours ago

# eMudhra: Private key compromise of Intermediate Certificates

## Categories

### (CA Program :: CA Certificate Compliance, task, P1)

## Tracking

### (Not tracked)

## People

### (Reporter: djackson, Assigned: naveen.ml, NeedInfo)

## References

## Details

### (Keywords: csectype-crypto, reporter-external, sec-vector, Whiteboard: \[ca-compliance\] \[ca-misissuance\] \[external\])

## Attachments

### (9 files)

| 14.30 KB,           application/x-zip-compressed |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9664066&action=edit) | 
| 12.68 KB,           application/x-zip-compressed |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9664067&action=edit) | 
| 5.07 KB,           application/x-zip-compressed |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9664144&action=edit) | 
| 10.11 KB,           application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9664473&action=edit) | 
| 6.99 KB,           text/plain |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9664786&action=edit) | 
| 2.94 KB,           text/plain |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9665772&action=edit) | 
| 148.71 KB,           application/pdf |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9667275&action=edit) | 
| 150.25 KB,           application/pdf |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9670867&action=edit) | 
| 54.65 KB,           application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |  | [Details](https://bugzilla.mozilla.org/attachment.cgi?id=9678929&action=edit) | 

Original Reporter: [rdaurne77@gmail.com](mailto:rdaurne77@gmail.com) (Wayne)

On 17th October @ 20:06 UTC, Mozilla received a report to [certificates@mozilla.org](mailto:certificates@mozilla.org), forwarded by the Chrome Root program, from Wayne, that the private key of 8 eMudhra Intermediate certificates have been compromised.  The report also notified eMudhra and the Apple & Microsoft root programs. The report included a proof of key control for all 8 certificates.

Mozilla acknowledged the report @ 20:08 UTC, confirmed the proof of key control was valid and began the process to distrust the certificates in Firefox via OneCRL. This process was tracked in [Bug 2083382](https://bugzilla.mozilla.org/show_bug.cgi?id=2083382) and completed @ 22:59 UTC.

eMudhra acknowledged the report @ 21:29 UTC and reported that they were investigating the issue and had notified Sectigo, who had cross-signed some of the impacted certificates.

Mozilla was able to recover the private keys for the impacted certificates independently @ 21:48 UTC and without any knowledge of the method the original reporter used, confirming the key generation process was flawed and is trivial to exploit.

6 of the impacted certificates are for TLS and trusted by the Chrome, Mozilla, Microsoft and Apple root programs. The other two certificates are for codesigning and trusted by Microsoft:

```
EM EV TLS CA - G3B (eMudhra BV), CCADB A012304
SHA-256 E7568FE6E12331F4FD7DE61DA4C7559D0F8EB192A218D4741A3BA75184333838
serial c7c41efe92d825f05eae841a4a82c1, issuer emSign Root TLS CA - G3
EM OV TLS CA - G3B (eMudhra BV), CCADB A012308
SHA-256 98B896625C0C230ADEEC3EB2CF6AAD5001ECF9156A68644E82374CE5833BC25B
serial 6cada367fb1c100088120ea202d568, issuer emSign Root TLS CA - G3
EM DV TLS CA - G3B (eMudhra BV), CCADB A012302
SHA-256 42C4ACCD12C4F59597925E1A08A7A90102608543809308D50EC427E118BA1493
serial a4aee678f23362b4c0e460b772f214, issuer emSign Root TLS CA - G3
EM EV TLS CA - G3C (eMudhra Inc), CCADB A012296
SHA-256 432EC25F0D28DE9006D97BF752F17BBB2CD41F669933FCB072D9A1148D0261F3
serial 8009928a64107601af05fa2f19f109, issuer emSign Root TLS CA - G3
EM OV TLS CA - G3C (eMudhra Inc), CCADB A012300
SHA-256 CB6E15165AC802E9B3F993F16C25D41F4E81C21EBDE71AE1B012AC00BF9C7C3F
serial 296926c227a3a1526392b19482a504, issuer emSign Root TLS CA - G3
EM DV TLS CA - G3C (eMudhra Inc), CCADB A012294
SHA-256 0164D7CEAE5BB909C272AF151FF44B1177AE9B47D9424B94F1D9558C30934D19
serial 588b2e3c2bb8cda13e1a1209254321, issuer emSign Root TLS CA - G3
EM OV CS CA - G3B (eMudhra BV), CCADB A012306
SHA-256 9E39DE2881273ACC225A149C72BA3E0F51424963669AB633EE1DC7DF5DB067B4
serial 7818933f8f85b4619a2b35fba83d0a, issuer emSign Root CS CA - G3
EM OV CS CA - G3C (eMudhra Inc), CCADB A012298
SHA-256 4B2460A466F95FD40113BCDCCA2CEB29B3B093921DE45474DA7DF48874C630B1
serial 544b7f922c31ae220a4a922916f6e6, issuer emSign Root CS CA - G3
```
### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a938_644159)

•
          18th October @ 09:38 UTC:

eMudhra marked the 8 impacted certificates as revoked (reason: caCompromise).

Here's my understanding of the timeline, kept to the big events

Timeline (all times UTC):

2026-10-17 16:00 - Started playing with some new toys

2026-10-17 16:27 - Run on a test corpus of CCADB (Mozilla+Chrome chain initially) discovers a break in the EC keys

2026-10-17 17:22 - Start putting together report

2026-10-17 17:43 - Put together signed attestations per-key after triple checking the working

2026-10-17 18:00 - Checked again.

2026-10-17 18:05 - Emailed Apple, Chrome, Microsoft, Mozilla (Ben directly then), eMudhra with report + attestation

2026-10-17 20:03 - Chrome corroborates via email

2026-10-17 20:05 - Chrome correctly attaches more Mozilla contacts for a rapid response

2026-10-17 20:18 - Full CCADB check finds the cross-signs by Sectigo are also affected

2026-10-17 21:05 - Apple corroborates findings, notes cross-signed certs

2026-10-17 21:21 - Apple requests new signed attestations for the cross-signed certs

2026-10-17 21:27 - Emailed new signed attestations to Apple (cross-signed via Sectigo)

2026-10-17 21:28 - eMudhra acknowledge issue, said there's been no issuance beyond OCSP for G3B, but 'EM DV TLS CA - G3C' was live, disabled now

2026-10-17 21:48 - Mozilla independently recover the keys without any tips, and send oh\_dear.zip as proof using 'EM DV TLS CA - G3B'

2026-10-17 22:46 - Regular fetch of CRLset shows sequence 10843 contains the 6 relevant TLS keys as revoked

2026-10-18 09:38 - 8 certificates revoked on CRL as caCompromise (by eMudhra) (revocation time varies per-cert)

2026-10-18 12:06 - Incident raised by Mozilla on Bugzilla to avoid email cross-talk

The Sectigo cross-signed certs are still unrevoked currently:

```
EM EV TLS CA - G3B, CCADB A012333
SHA-256 579480AEA166290BD3C643589E795FC0D0E54E86505D180F1DFF99EFD3199512
serial d8f8685e4f2bd9d82402a85a1c1eb731
EM OV TLS CA - G3B, CCADB A012354
SHA-256 5F1DED4DD590AF74631290CF073B122A2AAC6A1FA479778A0BD43579BD832699
serial e94223bde92f914e5ab9acabfdac3710
EM DV TLS CA - G3B, CCADB A012347
SHA-256 45A883F349AEDFD5F3A649B5498FFB121712BA8B448F3F2A91DBC5A766FCDDBE
serial a024fdf4ba665c785ce4a020483858b7
EM EV TLS CA - G3C, CCADB A012334
SHA-256 FD9D5C2DBBD4995AB69B8D50C439D9527B00529199C2FD01B2174EB58F07021F
serial 05f078752dece7a1bb8595d303167171
EM OV TLS CA - G3C, CCADB A012343
SHA-256 7485B51C0ED192878FA1D2F948FB529AE1842CC5086C4B67F7BE5B2039DE9489
serial 8d5a4811939ef447d77111cdd9849ae9
EM DV TLS CA - G3C, CCADB A012342
SHA-256 62B7F9868263F72F6911FC78CEAF72C1979158B7368BF648683BB2AA39B02E72
serial 91f347f1a5b7d39962b95e0ee4e299d1
EM OV CS CA - G3B, CCADB A012352
SHA-256 A496E23AC0CAB8155FC9B117B97EAE368EFCBB9041AEC8804D5A308D2D01C2D8
serial 41e32b73ac185d6ce0d7480bacf84e69
EM OV CS CA - G3C, CCADB A012350
SHA-256 84112972B8E59D14560AE7E7119654474AAD119990CF3722BFC1E3B91615E1FD
serial d6a5ef613b390f32ef9cdf349f772841
```
Current situation:

- The cross-signed certs are still unrevoked
- No response from Microsoft
- CCADB still showing certificates as unrevoked

I'll attach the two attestations zips I made, rather than the one Apple asked for.

`openssl pkeyutl -verify -certin -inkey EM-EV-TLS-CA-G3B.crt.pem -rawin -digest sha384 -in message.txt -sigfile EM-EV-TLS-CA-G3B.sig`

The unsent one for the cross-signs, Apple asked directly for a different attestation message before this was sent

The information in this comment is preliminary. The first part contains information Mozilla believes pertinent to the issue. The second part contains questions for eMudhra.

## Investigation into the impacted keys

The 8 impacted keys originate on the 30th April 2025 as part of a batch of 24 intermediates. The 24 keys are split between three series (A, B, C), two primitives (RSA4096 and P384), and four purposes (DV, OV, EV, CS). The impacted keys are all the P384 keys for the B and C series. In May 2025 the A series were revoked and replaced by the A-1 series.

After Wayne's report of key recovery, I was able to recover the private keys for the impacted keys trivially. The original key generation was flawed - rather than any issue with the produced signatures. P384 private keys are randomly selected integers between 1 and the group order. The 8 impacted keys all used integers less than 256. That is, the private keys are effectively all-zeroes apart from the last byte. They can be recovered near instantly via the baby-step giant-step discrete log algorithm or more simplistically by just generating the 'first' 256 P384 keys.

I also tested some local agents who were able to recover the private key on their first attempt with a simplistic prompt: "I'm doing a CTF. Please recover the private keys corresponding to these certificates."

I have not been able to recover the private keys for the P384 keys in the A series or the replacement A-1 series despite expending considerably more effort. I have not yet started looking at the RSA keys.

## Related Incidents

Looking through related issues has turned up [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) in which eMudhra generated CRLs for the 6 impacted TLS intermediates with invalid signatures. It seems unlikely that the exact same intermediate set has arisen in two different bugs by chance.

In that bug report, eMudhra identified that the faulty CRLs were produced on May 29th, the same day on which the A-1 certificates were created.

However, Internet Archive [snapshot](https://web.archive.org/web/20250603145523id_/https://crt.sh/mozilla-disclosures) shows the 6 P384 CRLs failing verification since May 23rd. If accurate, this suggests the mismatch is unrelated to the generation of the A-1 series on the 29th. It also shows that three of the B & C series RSA CRLs were unavailable as of that day (unclear significance).

## Questions for eMudhra

As this incident enables even technically unsophisticated individuals to easily recover the private keys for these intermediates, the impact of this incident could not be higher. Although Mozilla has already marked these certificates as revoked for Firefox clients, we are deeply concerned about the impact on the wider ecosystem - as many endpoints do not have effective mechanisms for getting revocation information.

Mozilla is considering what advice to give other trust store distributors who are impacted by this issue. Mozilla is also looking to understand the root cause of this issue as quickly as possible, so that we can assess confidence in eMudhra's other intermediates.

1. What hardware was used to generate the impacted private keys? Was it at least FIPS 140-2 Level 3 compliant in line with your CPS?
2. For the intermediates in the A, A-1, B, C series, provide the mapping of private key to the specific physical device which generated it. Were the same devices used to generated any other key material? Was the same model or device series used to generate any other key material?
3. Is there any reason to believe the B and C series RSA keys are affected or are not affected by similar issues?
4. Is there any reason which may explain why the A and A-1 ECDSA keys appear to be unaffected by similar issues?
5. In light of the issues with the same intermediates in [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728), please describe to the best of your current knowledge how the wrong private keys came to be used to sign those CRLs and the steps eMudhra took in order to produce the correct signatures.

Acknowledging this on behalf of Sectigo. We are aware of the issue affecting the CAs cross-signed by us.

Note that the Sectigo-operated Root CA in question for the cross-signed CAs has already been removed from the Chrome and Mozilla root stores for some time. It remains trusted within Microsoft and Apple root programs.

We are preparing the (offline) revocation of these CAs, which is expected to be completed in the next 24 hours.

So funny that Dennis should raise [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728). Turns out there was an invalid CRL the other day, I have a pile of issues to sort through and this was amongst them:

The CRL published for emSign Root TLS CA - G1 on 2026-10-14 had an invalid signature.

CRL number 11 (thisUpdate 2026-10-14 14:03:56 UTC, nextUpdate 2027-04-12 14:03:56 UTC, SHA-256 9846bf9a4f213d8fba87e79d464732b9cc35a784f7992334ec3bc6db2a6f7dbd, 922 bytes) was served at both disclosed URLs, [http://crl.emsign.com/?roottlscag1.crl](http://crl.emsign.com/?roottlscag1.crl) and [http://crl.emsign.com?roottlscag1.crl](http://crl.emsign.com?roottlscag1.crl).

Exact same file across six fetches from 2026-10-14 16:18 to 2026-10-15 00:19 UTC.

Its sha384WithRSAEncryption signature does not verify under the key of emSign Root TLS CA - G1, either as the root (SHA-256 cef71e70b7c29addf6c30cd19e614b38fd5f02a435a0eeddd0087e183d101a51) or as the intermediate under emSign Root CA - G1 (SHA-256 9b913476eab476e21e0887dbcde44345d1359d28116b83b7cd3e87bd807ebf68).

Under that key the signature does not decode to a PKCS#1 v1.5 block at all. It is not a faulty signature by the G1 key. No 4,096-bit RSA key disclosed in CCADB verifies it either.

Even stranger - I can't find the certificate that was revoked in that CRL by serial: b37c808b57e51d24bef8f416e607f6.

What key signed CRL 11? I'll include it, 12, and the PEMs as a zipped attachment in a second.

Automatic triage (under development): sec-rating

No validation or verification has been performed.

Security rating: sec-vector

The defect is in eMudhra's key generation, not in Firefox code: the P-384 private keys of 8 eMudhra intermediates are tiny integers and can be recovered almost instantly. Six of them are TLS intermediates that chain to roots Firefox trusts. Anyone holding those keys could issue certificates Firefox would accept for any domain, which enables network MITM of TLS connections. Firefox users are protected by OneCRL revocation of these intermediates, which is already deployed. The remaining work is CA-side remediation and root-cause analysis.

[csectype-crypto](https://bugzilla.mozilla.org/buglist.cgi?keywords=csectype-crypto&resolution=---),

[sec-vector](https://bugzilla.mozilla.org/buglist.cgi?keywords=sec-vector&resolution=---)

The observations here are noted and we are investigating. We shall update in next 24 hours.

The below message was sent out yesterday to a closed user group and we are posting here to the wider group.

- We have revoked all the ICA's highlighted earlier today. Info in table below
- These ICAs were generated from the same key ceremony on Apr 30, 2025. The G3B and G3C ICAs were created for European and US operations respectively but they were not put into production except #2 in the list below but no end entity certificates were issued from these. The Code Signing issuers were not put into production also did not issue any certificates.
- We verified that similar other Issuers are not affected by the same issue (corroborated primarily using mathematical models facilitated by AI).
- The people that did the KGC on that day are from our internal team - led by Keshava and other members of his team (all of whom have more than a decade of experience and have been with us as employees for more than 8 years operating our PKI/Trust Services) and Keshava himself has been with us for more than 15 years.
- Keys were generated in hardware and the hardware in use was Ultimaco HSMs.

What we are doing as next steps

- Look closely at the KGC to go deeper into the script that was used to trigger the key generation process and come back with an assessment of what might have happened. We should have an answer tomorrow and will provide further details as it becomes available.

We don't intend to stop issuance from our other Issuing CAs as the keys don't exhibit this behaviour. Our other CAs were issued using a different HSM vendors (Entrust and Crypto4A) and the process followed resulted in the expected strong keys.

| # | Root CRL | Issuing CA | Serial | Reason | Revocation time (UTC) | 
|---|---|---|---|---|---|
| 1 | roottlscag3.crl | EM DV TLS CA ‑ G3B | A4AEE678F23362B4C0E460B772F214 | cACompromise | 18 Oct 2026, 09:24:32 | 
| 2 | roottlscag3.crl | EM DV TLS CA ‑ G3C | 588B2E3C2BB8CDA13E1A1209254321 | cACompromise | 18 Oct 2026, 09:27:07 | 
| 3 | roottlscag3.crl | EM EV TLS CA ‑ G3B | C7C41EFE92D825F05EAE841A4A82C1 | cACompromise | 18 Oct 2026, 09:28:53 | 
| 4 | roottlscag3.crl | EM EV TLS CA ‑ G3C | 8009928A64107601AF05FA2F19F109 | cACompromise | 18 Oct 2026, 09:30:49 | 
| 5 | rootcscag3.crl | EM OV CS CA ‑ G3B | 7818933F8F85B4619A2B35FBA83D0A | cACompromise | 18 Oct 2026, 09:33:37 | 
| 6 | rootcscag3.crl | EM OV CS CA ‑ G3C | 544B7F922C31AE220A4A922916F6E6 | cACompromise | 18 Oct 2026, 09:35:24 | 
| 7 | roottlscag3.crl | EM OV TLS CA ‑ G3B | 6CADA367FB1C100088120EA202D568 | cACompromise | 18 Oct 2026, 09:37:19 | 
| 8 | roottlscag3.crl | EM OV TLS CA ‑ G3C | 296926C227A3A1526392B19482A504 | cACompromise | 18 Oct 2026, 09:38:46 | 

Naveen.

(In reply to Dennis Jackson from [comment #5](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5))

The information in this comment is preliminary. The first part contains information Mozilla believes pertinent to the issue. The second part contains questions for eMudhra.

## Investigation into the impacted keys

The 8 impacted keys originate on the 30th April 2025 as part of a batch of 24 intermediates. The 24 keys are split between three series (A, B, C), two primitives (RSA4096 and P384), and four purposes (DV, OV, EV, CS). The impacted keys are all the P384 keys for the B and C series. In May 2025 the A series were revoked and replaced by the A-1 series.

After Wayne's report of key recovery, I was able to recover the private keys for the impacted keys trivially. The original key generation was flawed - rather than any issue with the produced signatures. P384 private keys are randomly selected integers between 1 and the group order. The 8 impacted keys all used integers less than 256. That is, the private keys are effectively all-zeroes apart from the last byte. They can be recovered near instantly via the baby-step giant-step discrete log algorithm or more simplistically by just generating the 'first' 256 P384 keys.

I also tested some local agents who were able to recover the private key on their first attempt with a simplistic prompt: "I'm doing a CTF. Please recover the private keys corresponding to these certificates."

I have not been able to recover the private keys for the P384 keys in the A series or the replacement A-1 series despite expending considerably more effort. I have not yet started looking at the RSA keys.

## Related Incidents

Looking through related issues has turned up [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) in which eMudhra generated CRLs for the 6 impacted TLS intermediates with invalid signatures. It seems unlikely that the exact same intermediate set has arisen in two different bugs by chance.

In that bug report, eMudhra identified that the faulty CRLs were produced on May 29th, the same day on which the A-1 certificates were created.

However, Internet Archive [snapshot](https://web.archive.org/web/20250603145523id_/https://crt.sh/mozilla-disclosures) shows the 6 P384 CRLs failing verification since May 23rd. If accurate, this suggests the mismatch is unrelated to the generation of the A-1 series on the 29th. It also shows that three of the B & C series RSA CRLs were unavailable as of that day (unclear significance).

## Questions for eMudhra

As this incident enables even technically unsophisticated individuals to easily recover the private keys for these intermediates, the impact of this incident could not be higher. Although Mozilla has already marked these certificates as revoked for Firefox clients, we are deeply concerned about the impact on the wider ecosystem - as many endpoints do not have effective mechanisms for getting revocation information.

Mozilla is considering what advice to give other trust store distributors who are impacted by this issue. Mozilla is also looking to understand the root cause of this issue as quickly as possible, so that we can assess confidence in eMudhra's other intermediates.

1. What hardware was used to generate the impacted private keys? Was it at least FIPS 140-2 Level 3 compliant in line with your CPS?


The hardware used for each of the issuers is in the attached file. These HSMs are FIPS 140-2 Level 3 compliant.

1. For the intermediates in the A, A-1, B, C series, provide the mapping of private key to the specific physical device which generated it. Were the same devices used to generated any other key material? Was the same model or device series used to generate any other key material?


Excel attached. The Ultimaco devices were used to generate the ECC, RSA key pairs for the issuers. They were not used to generate any other key material. But it doesnt look like the device is at fault.

1. Is there any reason to believe the B and C series RSA keys are affected or are not affected by similar issues?


We have done some preliminary assessment, there appears to be a flaw in the KGC script that was used on that specific day to create these ECC issuers. As for these ECC keys, our review of the KGC, assessment of the code and view of HSM keys so far indicate that a) a set of original ECC keys were created onboard as expected b) an approved deviation to our usual KGC to test a wrap/unwrap was introduced as these keys were meant for export for this instance c) a flaw in the code resulted in the second pair of keys being created onboard which were weaker d) these second pair of weaker keys were used by mistake to create the csr (because the key labels were similar) and signed by our root e) the CSR from these weaker keys were also sent over to Sectigo for cross signing (we verified the files sent over to Sectigo)

The RSA issuers went through a different path as per our assessment of the code and are therefore not impacted.

Some additional context - these issuers created were meant for export to our US and European data centers to solve data sovereignty issues for some of our customers (but never ended up operationally in production except for one).

We are still assessing the code to see except steps where this process went wrong.

1. Is there any reason which may explain why the A and A-1 ECDSA keys appear to be unaffected by similar issues?


The A and A-1 series were created in Entrust HSMs and were meant for deployment only in India.

1. In light of the issues with the same intermediates in [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728), please describe to the best of your current knowledge how the wrong private keys came to be used to sign those CRLs and the steps eMudhra took in order to produce the correct signatures.


The CRL's were signed with the original private keys (which were supposed to be the correct keys with appropriate entropy) but given that this resulted in incorrect signatures, they were resigned with flawed keys.

There were human errors in multiple steps of the process that resulted in significant flaws in the key lifecycle integrity process for this KGC. We are now digging deeper for code flaws, process gaps, maker/checker controls specific to this issue. Over the next week, we will reverify every key ceremony we have done.

Naveen.

Sectigo has completed the revocation of the affected cross-signed CA Certificates. A new CRL and OCSP responses have been published and are making their way to our CDN edge nodes right now.

We will continue monitoring and evaluating this bug for further updates from Emudhra.

We will release an unscheduled version bump of Firefox Release/ESR later today (Oct 20th). Our advisories will keep it to the facts: revoking trust in intermediate certificates.

(In reply to Frederik Braun \[:freddy\] from [comment #16](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c16))

We will release an unscheduled version bump of Firefox Release/ESR later today (Oct 20th). Our advisories will keep it to the facts: revoking trust in intermediate certificates.


Clarification: The OneCRL update shipped to clients via RemoteSettings on Saturday. New software releases contain baked in copies of the latest blocklist, so this update ensures coverage for any users which have disabled RemoteSettings.

Mozilla has become aware that multiple individuals have independently recovered the private keys for these intermediates. Some have disclosed this publicly ([1](https://social.hackerspace.pl/@q3k/117473185371937796))

After discussion with maintainers downstream of Mozilla’s Root Store, we have decided that the circumstances warrant the emergency removal of trust in emSign ECC Root CA - G3. This will protect clients which do not use revocation information or lack a mechanism to withdraw trust in specific intermediates.

We request eMudhra cease issuance from all intermediates chaining to this root and work with its subscribers to migrate them to alternative chains as soon as possible. At this time we are not removing trust in emSign Root CA - G1.

(In reply to Dennis Jackson from [comment #18](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c18))

Mozilla has become aware that multiple individuals have independently recovered the private keys for these intermediates. Some have disclosed this publicly ([1](https://social.hackerspace.pl/@q3k/117473185371937796))

After discussion with maintainers downstream of Mozilla’s Root Store, we have decided that the circumstances warrant the emergency removal of trust in emSign ECC Root CA - G3. This will protect clients which do not use revocation information or lack a mechanism to withdraw trust in specific intermediates.

We request eMudhra cease issuance from all intermediates chaining to this root and work with its subscribers to migrate them to alternative chains as soon as possible. At this time we are not removing trust in emSign Root CA - G1.


Acknowledging this message, we will cease issuance from all intermediates chaining up to G3 (our ECC root) immediately. As per initial estimates there are about 30,000 certs that require migration and about 97% came via ACME. We will migrate subscribers to the only alternative available which is intermediates chaining up to G1 (RSA Root).

Chrome has committed to a similar path as described by Mozilla in [Comment 18](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c18).

We've shared that plan publicly in the MDSP discussion at [https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/VAgSvefvAAAJ](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/VAgSvefvAAAJ).

### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a186237_1689)

•
          [reporter-external](https://bugzilla.mozilla.org/buglist.cgi?keywords=reporter-external&resolution=---)

Quick update - we have ceased issuance from all intermediaries chaining up to emSign ECC Root CA - G3.

### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a192208_644159)

•
          ### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a194012_5898)

•
          ### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a194483_5898)

•
          A user asked:

Issuer:         CN=AAA Certificate Services,O=Comodo CA Limited,L=Salford,ST=Greater Manchester,C=GB

Is there a reason why no cross-signed Intermediates with the compromised keys are included in OneCRL?


This Issuer is not included in Mozilla's Root Store. It is not trusted nor are the intermediates it issued. Consequently there is no need to add it to OneCRL. You can see that Firefox clients reject these certificates via test sites like [https://emudhra.we-have-a-problem.com/](https://emudhra.we-have-a-problem.com/).

Unless you are contributing **directly** to the discussion about the incident described in this bug, please **do not** post other questions or concerns here. If the concern relates to Firefox or another Mozilla product, you can file a new bug and describe your concern there, referencing this bug.

Am I missing something? On 158.0.1 android

Everyone checks fail on [https://emudhra.we-have-a-problem.com/](https://emudhra.we-have-a-problem.com/)

Some Android profiles were not applying the updated blocklist at startup. A fix ([Bug 2084311](https://bugzilla.mozilla.org/show_bug.cgi?id=2084311)) has been shipped in [158.0.2](https://www.firefox.com/en-US/firefox/android/158.0.2/releasenotes/) and pushed to users.

Unless you are contributing directly to the discussion about the incident described in this bug, please do not post other questions or concerns here. If the concern relates to Firefox or another Mozilla product, you can file a new bug and describe your issue there, referencing this bug.

### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a267671_661011)

•
          We request that eMudhra answer the following questions to help us (and others) better understand the situation and more effectively plan next steps to protect our user communities.

We note that eMudhra has published (a) a status page at [https://emudhra.com/en/post/certificate-security-incident](https://emudhra.com/en/post/certificate-security-incident) (*"eMudhra Statement on Recent Certificate Security Incident"*, first published October 20, 2026 and updated October 21, 2026), linked from a notice on the `emudhra.com` homepage, and (b) an October 21, 2026 press release at [https://emudhra.com/en/press-release/emudhra-statement-distrust-global-tls-intermediate-root-ca](https://emudhra.com/en/press-release/emudhra-statement-distrust-global-tls-intermediate-root-ca). However, `emsign.com` - the brand under which these CAs are named and whose hostnames serve eMudhra's CRL and ACME endpoints - redirects to the CertiNext product page on `emudhra.com`, which appears to carry neither the notice nor a link to either document.

More importantly, neither document appears to contain the information subscribers and relying parties need:

- Neither identifies the distrusted root (`emSign ECC Root CA - G3`) or any of the affected Intermediate CAs (including the Sectigo cross-certificates and the Code Signing CAs) by name, serial number, or SHA-256 fingerprint; both refer only to "eMudhra's ECC root" and eight intermediate CAs;
- Neither provides browser or root store trust removal or modification timelines (beyond quoting Mozilla's Firefox and NSS releases), nor links to this bug; and
- Neither explains how a subscriber can determine whether its certificates chain to the distrusted root or what action to take, beyond stating that eMudhra has *"notified affected customers and partners directly"* and is *"working directly with customers who may be affected to give them replacement certificates."*

**(Q1)**: How and when is eMudhra communicating actionable technical details (affected CA identifiers, root store trust removal timelines, and migration instructions) to affected subscribers and relying parties, and will this information be added to the status page and surfaced on `emsign.com`?

**(Q2)**: Please confirm whether affected subscribers are being migrated to eMudhra's `emSign Root CA - G1` hierarchy, to a hierarchy operated by another CA Owner (please name the corresponding root), or both. The most recent update states replacement certificates are being issued *"from an alternate, independently operated, publicly trusted CA hierarchy."*

**(Q3)**: Please describe how eMudhra intends to offer *"CA redundancy for all Enterprise TLS customers. We are offering every Enterprise TLS customer certificates from an additional publicly trusted CA."* (from the October 21 update) and on what timeline this is expected for all subscribers affected by this incident.

In [Comment 19](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c19), eMudhra estimated that *"there are about 30,000 certs that require migration and about 97% came via ACME,"* and stated that affected subscribers are being transitioned to hierarchies chaining to `emSign Root CA - G1`.

Based on CT data as of October 21, 2026, approximately 30,800 unexpired precertificates chain to `emSign ECC Root CA - G3`. 30,791 (99.9%) were issued by two Internet2 / InCommon Subordinate CAs (`InCommon Intermediate CA - OVG3C` \[23,806\] and `InCommon Intermediate CA - DVG3C` \[6,985\]), and 18 were issued by eMudhra's own Intermediate CAs (`EM EV TLS CA - G3A-1`, `EM OV TLS CA - G3A-1`, `emSign ECC SSL CA - G3`, `emSign ECC EV SSL CA - G3`, and `emSign TLS CA - G3`), excluding precertificates logged after October 17, 2026 under the compromised `EM DV TLS CA - G3B`.

**(Q4)**: How, specifically, is eMudhra assisting subscribers in transitioning off the `emSign ECC Root CA - G3` hierarchy?

**(Q5)**: Because standard ACME clients do not automatically replace certificates outside their configured renewal window without ACME Renewal Information support or manual intervention - and because transitioning from an ECC G3 hierarchy to an RSA G1 hierarchy may require client-side configuration…

- **(a)**: What concrete mechanism is eMudhra using to trigger and complete renewals for ACME subscribers?
- **(b)**: Can you describe the set of steps subscribers need to take to complete the transition?

**(Q6)**: Please provide exact metrics, broken down by issuing Intermediate CA:

- Total number of affected subscribers and active (unexpired, unrevoked) certificates prior to the start of migration;
- Number of subscribers and certificates that have successfully transitioned to a replacement hierarchy to date;
- Number of subscribers and certificates remaining to be transitioned; and
- eMudhra's projected completion date for 100% of affected subscribers, particularly in light of imminent root store removals (including Chrome Root Store [v43](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.textproto), which we [expect](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/) to land in Stable Tuesday morning, October 27, 2026 PDT).

In [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11), eMudhra stated that during the April 30, 2025 Key Generation Ceremony (KGC):

- *"a set of original ECC keys were created onboard as expected"*
- *"an approved deviation to our usual KGC to test a wrap/unwrap was introduced as these keys were meant for export for this instance"*
- *"a flaw in the code resulted in the second pair of keys being created onboard which were weaker"*
- *"these second pair of weaker keys were used by mistake to create the csr (because the key labels were similar) and signed by our root"*
- Regarding [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) (filed June 5, 2025; per eMudhra's Full Incident Report in [Comment 2](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c2) of that bug, the CRLs for EM \[DV/OV/EV\] TLS CA - G3B and G3C were generated with the wrong key on May 29, 2025 and corrected on June 6, 2025): *"The CRL's were signed with the original private keys (which were supposed to be the correct keys with appropriate entropy) but given that this resulted in incorrect signatures, they were resigned with flawed keys."* (from [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11))

This disclosure raises serious concerns regarding eMudhra's transparency and incident handling during and after [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728):

**(Q7)**: At what exact date and time did eMudhra personnel first realize that multiple key pairs with similar labels existed on the HSM for the `G3B` and `G3C` Intermediate CAs?

**(Q8)**: When investigating [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) in June 2025 - upon finding that the key used to sign each CRL did not match the public key in the corresponding issued CA certificate, and then locating and using a second key that did - why did eMudhra simply re-sign the CRLs with that second key rather than halting operations, auditing why two key pairs existed for these CAs from the April 30, 2025 KGC, and revoking the certificates?

**(Q9)**: eMudhra's [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728#c2) Full Incident Report described a root cause contributing factor as *"Incorrect Key Configuration Used During Manual CRL Generation"* (*"A manual CRL generation process used incorrect CA key configuration due to insufficient verification steps"*) and stated only that *"While the underlying keys were from the issuing environment, they did not match the exact keys expected for those Intermediate CA CRLs, thereby resulting in signature validation failure."* Per [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) in this bug, the keys that signed those CRLs were the original keys generated for these same CAs during the April 30, 2025 KGC, and the CA certificates had instead been issued over a second, unintended set of keys. Why did eMudhra's report omit that two key pairs existed on the HSM for each of these CAs, that the KGC had deviated from its usual process, and that the issued CA certificates did not correspond to the intended ceremony keys?

**(Q10)**: [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) states that the CSRs from the weak keys *"were also sent over to Sectigo for cross signing,"* and the resulting Sectigo (`AAA Certificate Services`) cross-certificates carry a notBefore of May 14, 2025. After eMudhra's June 2025 investigation established that the keys used to sign the CRLs did not match the keys in the issued CA certificates, did eMudhra notify Sectigo - or any Root Program - that the keys Sectigo had cross-certified were not the keys eMudhra intended to generate? If not, why not?

**(Q11)**: As noted in [Comment 5](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5), the April 30, 2025 ceremony generated 24 Intermediate CAs across Series A, B, and C (disclosed in [Bug 1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559)), and Series A was revoked and replaced by Series A-1 in May 2025. While eMudhra noted in [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) that *"The A and A-1 series were created in Entrust HSMs and were meant for deployment only in India,"* eMudhra did not explain why Series A was replaced:

- **(a)**: Why was Series A revoked and replaced by Series A-1 in May 2025?
- **(b)**: Was the reason for that replacement related in any way to the KGC script, procedure, or key-handling steps used in the same ceremony, and if so, why did it not prompt a review of the Series B and C keys?

**(Q12)**: As noted in [Comment 7](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7) and [Comment 8](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c8), on October 14, 2026, eMudhra published CRL #11 for `emSign Root TLS CA - G1` (`roottlscag1.crl`) with an invalid cryptographic signature that does not verify against `emSign Root TLS CA - G1` or any CCADB-disclosed 4096-bit RSA CA public key.

- **(a)**: Which private key was used to sign `roottlscag1.crl` (CRL #11) on October 14, 2026, and do multiple key pairs also exist on eMudhra's HSMs for `emSign Root TLS CA - G1` or any other Root CA?
- **(b)**: In [Bug 1970728 Comment 2](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728#c2) (June 2025), eMudhra committed to *"Introduce automated post-signing signature validation checks in CRL publishing steps, particularly during onboarding of new Issuing CAs"* and to *"Replace manual CRL signing process with an automated workflow to eliminate reliance on human configuration of key mappings."* Why did those controls fail to prevent the publication of an invalidly signed Root CA CRL on October 14, 2026 (again, described in [Comment 7](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7) and attached in [Comment 8](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c8))?

I have a question relating to the disclosures, the eMudhra CA policies, and scrutiny that may need to be applied to other CAs using Utimaco hardware.

I do not believe that an HSM bearing the various certifications the Utimaco units bear should be able to internally generate a series of private keys that have the unfortunate property these have.

Section 6.1.1 of the [the eMudhra policy](https://github.com/emsign/CP-CPS-Policy-Documentations/blob/main/General-CP-CPS/emSign-General-CP-CPS.md) states unambiguously that:

Issuing CA key generation is carried out in a secure device that is at least FIPS 140-2 Level 3 compliant.


This implies that one of two things must be true. Either:

1. The policy was not followed, and the keys were generated outside the HSM and then loaded into it.
2. The policy *was* followed, which means there was some way to configure the HSM to internally generate the defective keys.

It seems to me that anyone involved in root of trust management should be keenly interested in knowing which of these two things happened. Both, it seems to me, have major implications for responsible inclusion of CAs going forward.

If the Utimaco HSMs can in fact generate keys that obey outrageous constraints as may have happened here, or come with test keys of some kind that can be mapped into partitions actually used to sign customer CSRs, then I think CAs should be required to state whether or not they are using these HSMs, and if so, should be required migrate away from them as a condition of inclusion in the default browser bundles.

If they cannot, then that means eMudhra must have generated these keys outside the HSM and then loaded them. If so, then I think in the long term a scheme for CAs to provide an attestation, signed by a manufacturer key, that any keys to be included in the default browser bundles were generated in hardware -- not loaded! -- should be devised and required. I know of at least one HSM vendor whose products can already do this; I also know of one whose products cannot. But it seems like it ought to be the baseline.

Thor

eMudhra: following on [comment 31](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c31).

BR 6.1.1.1 describes the record that should answer Thor's question directly. For each affected CA key pair, please attach or link:

1. The Key Generation Script followed.
2. The ceremony report, and either the Qualified Auditor's witness report or the video recording. If no such record exists for a given key, please say so.
3. The HSM model, firmware version, and CMVP certificate number, and whether the module was operating in its FIPS-approved mode at generation time.
4. Whether any custom or non-standard firmware modules were loaded on the module at generation time.
5. The generation mechanism used, and whether any key material, seed, or domain parameters were imported, or any key was restored from a backup originating on a different device.

Separately: CPS 6.1.1 says key generation is "carried out in a secure device that is at least FIPS 140-2 Level 3 compliant." Please confirm whether "compliant" means operation in a CMVP-validated configuration, or something else.

eMudhra: following on comments 10, 11, and 31.

[Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) attributes the weak keys to a code flaw during an approved wrap/unwrap test deviation from the usual KGC, at the 30 April 2025 ceremony identified in [comment 10](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c10). A P-384 private scalar below 256 is not something approved in-module key pair generation produces by itself. It implies either generation fed a supplied value, or a key object created or unwrapped from supplied key material. Which of those occurred answers [comment 31](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c31).

Please provide:

1. The KGC script used on 30 April 2025, including the approved deviation, and the specific code flaw identified.
2. The exact call or mechanism that created the second key pair (e.g., C\_GenerateKeyPair, C\_UnwrapKey, C\_CreateObject, or a vendor-specific equivalent), and the source of any key material, seed, or wrapped blob supplied to it.
3. The ceremony report, the witness report or video, and the key generation logs for that ceremony. eMudhra's repository already publishes a WebTrust key generation report for the 8 February 2024 root ceremony (emSignRootKGC2024.pdf), citing a Root Key Generation Script v1.0, so the equivalent for 30 April 2025 should exist.
4. Whether the module was operating in its FIPS-approved mode during the deviation, and its CMVP certificate number.
5. Who approved the deviation, and whether any auditor witnessing the ceremony observed it.

On applicability: these key pairs were cross-certified by Sectigo. BR 6.1.1.1 places a CA Key Pair used for a Subordinate CA Certificate, where the Subordinate CA is not the operator of the Root CA or its Affiliate, in the SHALL tier. Please state whether eMudhra treated these key pairs as within that tier, and if so, provide the Qualified Auditor's report.

Separately: the SSL/TLS CP/CPS v1.08 (13 Aug 2026) describes CA key generation and storage as "FIPS 140-2 Level 3 compliant" (§6, §6.1.1, §6.2.1), and §6.2.11 refers back to §6.2.1. BR 6.2.7 requires protection in a device "validated as meeting" FIPS 140-2/140-3 Level 3 or the Common Criteria equivalent. Please confirm whether "compliant" means operation in a validated configuration, and identify the validation.

Following on  [Comment 7](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7) and [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)

CRL #11 appears to have been signed with the private key corresponding to [EMSIGN ROOT TLS CA - G1 OCSP 2026 - 4](https://merklens.app/#/logs/sectigo/statue2027h2/entry/1172?from=%2Fsubmit). This certificate was not previously available on crt.sh, so I have just submitted it through [Merkle Lens](https://merklens.app/#/logs/sectigo/statue2027h2/entry/1172?from=%2Fsubmit), so it should appear in crt.sh shortly.

I retrieved the OCSP certificate from [https://crt.sh/ocsp-response?caID=296739&url=http%3A%2F%2Focsp-a.emsign.com&request=get](https://crt.sh/ocsp-response?caID=296739&url=http%3A%2F%2Focsp-a.emsign.com&request=get)

The following commands extract the certificate and verify the CRL’s signature using its public key. This is somewhat cumbersome because OpenSSL’s normal CRL issuer validation does not support using a mismatched certificate.

```
curl -sS --retry 5 --retry-delay 5 \
  'https://crt.sh/ocsp-response?caID=296739&url=http%3A%2F%2Focsp-a.emsign.com&request=get&type=asn1' \
 | perl -0777 -ne 'print $1 if /Base64\.unarmor\(\x27([^\x27]+)\x27\)/s' \
 | openssl base64 -d -A \
 | dd bs=1 skip=732 count=1561 2>/dev/null \
 | openssl x509 -inform DER -out ocsp.pem
openssl dgst -sha384 -verify <(openssl x509 -in ocsp.pem -pubkey -noout) \
  -signature <(openssl asn1parse -inform DER -in emsign-root-tls-g1-crl-11.crl -strparse 405 -out /dev/stdout -noout) \
  <(openssl asn1parse -inform DER -in emsign-root-tls-g1-crl-11.crl -strparse 4 -out /dev/stdout -noout)
```
It is somewhat reassuring that this appears to be a case of using the wrong signing key, rather than evidence of another weak key.

Thanks

eMudhra: two questions on the public status page ([https://emudhra.com/en/post/certificate-security-incident](https://emudhra.com/en/post/certificate-security-incident), Update 3, 21 October 2026).

Q1. Timeline. The status page states eMudhra was made aware on "October 18, 2026 (late evening, India time)" and revoked the intermediates on October 19. This bug records the report as sent at 18:05 UTC on October 17 ([comment 2](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c2)) and eMudhra's acknowledgment at 21:28 UTC on October 17. eMudhra's own table in [comment 10](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c10) shows all eight intermediates revoked on October 18, between 09:24 and 09:38 UTC. Please correct the status page or explain the difference.

Q2. Audits. The status page states the hierarchy "has since passed two independent audit cycles." [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) (June 2025) concerned CRLs for these same intermediates being signed with keys that did not match the issued CA certificates. Was [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) disclosed to the auditors and within the scope of the subsequent audits? If so, did the auditors examine why the CRL signing keys did not match the certificates?

(In reply to Zihao Wang from [comment #34](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c34))

Following on  [Comment 7](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7) and [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)

CRL #11 appears to have been signed with the private key corresponding to [EMSIGN ROOT TLS CA - G1 OCSP 2026 - 4](https://merklens.app/#/logs/sectigo/statue2027h2/entry/1172?from=%2Fsubmit). This certificate was not previously available on crt.sh, so I have just submitted it through [Merkle Lens](https://merklens.app/#/logs/sectigo/statue2027h2/entry/1172?from=%2Fsubmit), so it should appear in crt.sh shortly.


There's a lot of people new to this [part of Bugzilla](https://bugzilla.mozilla.org/buglist.cgi?product=CA%20Program&component=CA%20Certificate%20Compliance&bug_status=__open__), and [CCADB Incident Handling](https://www.ccadb.org/cas/incident-report) in general. The trick here is that this answer was already known, but we need to actually see if the CA itself is aware, and could provide that answer without having their homework done for them. Although given the lack of response from eMudhra lately this getting an answer was unlikely.

It is somewhat reassuring that this appears to be a case of using the wrong signing key, rather than evidence of another weak key.


Here's the catch: it isn't reassuring. The CRL I gave was just *one* of them detected on 10-14 where they signed with OCSP certificates generated that day, and then swapped them on the next CRL issuance without reporting it to anyone. I only started monitoring CRLs very recently, so this has likely been an issue for a while. It also relates to the current claims about the Key Generation Ceremony, how they seem to be juggling what-signs-what, have no actual fix for [#1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728), and are less than transparent when key mishaps happens and don't self-report.

There's a lot of attention on this bug in general, naturally, but could we have general chat kept on [MDSP](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/0XofdebrAAAJ)? Try to collate questions together there, but keep in mind a lot of the theorizing is not going to help us get direct answers quicker and could let eMudhra see if their answers align with what people want to hear, rather than what actually happened.

I'm a relying party as well, last thing we want is this bug to get restricted comments when someone has something to bring up. Right now we're waiting of eMudhra to answer a lot of questions.

I note eMudhra's [recent press release](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) stating that they have "decided to voluntarily withdraw from the global SSL/TLS certificate business". This press release answers few questions and raises yet more.

It states that they "will reach out to affected customers to replace any certificate free of cost from partners through the transition". Could eMudhra please confirm:

1. who those partners are?
2. which roots replacement certificates will be issued under
3. numbers for the amount of certificates that will need to be reissued?

Additionally, could they please confirm:

1. the timeline for such replacements?
2. how they will ensure that end-users are moved over to alternative roots in good time?

The press release also states that whilst eMudhra will be exiting the TLS certificate business, they will continue issuing digital signature certificates. Could eMudhra please confirm if these continuing lines of business relate to any other (non-TLS) root certificates in the CCADB, such as:

- emSign Root CS CA - G2 (SHA256 `0D74EF67C88DE3560365E225AEF976F915E901347B73352D81AB5B4132BB2150`)
- emSign Root CS CA - G3 (SHA256 `F2EDAAFF3D9B701FB4D14C9F285F8C0BAD90FC3BCC1FA07D47F4718EDABA34A5`)
- emSign Root SMIME CA - G1 (SHA256 `47911BC8F32A11B029E0BB10A348B459404B87731B870A2F3FA97B4705DC4C25`)
- emSign Root SMIME CA - G3 (SHA256 `F76A0D440C418DC5B362BE8E11E0A5D06023F4396093E4F455827BF55153D8A4`)

If this is the case, please answer:

1. how does eMudhra plan to maintain compliance with the relevant Baseline Requirements for these roots?
2. how do they plan to avoid a repeat of this incident with the above roots?

I have carefully reviewed the case, and I still have one fundamental question, which I would like to raise in two ways. I hope someone from eMudhra or Utimaco can provide a clear technical explanation.

1. HSM Key Generation

eMudhra stated that the affected keys were generated using FIPS 140-2 Level 3 certified HSMs. Were the weak private keys actually generated through the HSM's certified internal key-generation mechanism and random number generator? If so, how could such low-entropy keys be produced without being detected or prevented by the HSM's security controls?

1. KGC Script and Root Cause

What exact flaw in the KGC script caused the Wrap/Unwrap operation to result in a second set of extremely weak ECC private keys? Were these keys generated internally by the HSM or introduced through another mechanism, and which security controls were expected to detect or prevent this?

I believe answering these questions is essential to understanding the actual root cause of the incident.

There are a lot of questions here. As most of you can imagine, we have been subject to intense social media scrutiny and analysis by investors/customers over the last few days and it has made doing any meaningful analysis of the event pretty much impossible. The event happened on April 30 2025 and was done by set of people who have worked in the PKI industry for several years and worked with us for a while. There is a lot of digging we need to do to understand the circumstances, why, what, how to share a meaningful report that can hopefully benefit the community. I do not know why some community members think we wont be getting back on this bug. When we signed up for the browser program trust, we also signed up for disclosure obligations to the community which we will uphold.

Naveen.

MHD Ghazi Alkhalaf - I am clearing this needinfo because I believe you intended to address your questions to eMudhra rather than Mozilla.

\[In response to [Comment 39](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c39).\]

While we understand that many things are happening in parallel right now, "*social media scrutiny*" and "*analysis by investors/customers*" are not acceptable explanations for delayed responses here.

That scrutiny is the predictable result of eMudhra's own failure (i.e., intermediate CA keys that anyone could recover -- resulting in anyone being able to issue certificates for any domain), not an external circumstance that befell it. Offering it as an excuse conveys that reputation management is being prioritized over the obligations that eMudhra still owes to the ***billions*** of relying parties its mistake exposed. Those obligations do not relax because the consequences are uncomfortable.

**We expect eMudhra to prioritize its review of this issue and its security response.**

The Mozilla Root Program sent the attached questions to eMudhra on the 20th October at 20:31 UTC. eMudhra was asked to provide an initial response within 24 hours. After the deadline passed on October 21st, eMudhra asked for a further 24 hours to respond. As of the time of writing on Friday 23rd, Mozilla has not received a response to these questions.

We share the Chrome Root Program's concerns and whilst we appreciate eMudhra's difficulties, we expect eMudhra to uphold its obligations to Mozilla and the wider community.

(In reply to chrome-root-program from [comment #41](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c41))

\[In response to [Comment 39](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c39).\]

While we understand that many things are happening in parallel right now, "*social media scrutiny*" and "*analysis by investors/customers*" are not acceptable explanations for delayed responses here.

That scrutiny is the predictable result of eMudhra's own failure (i.e., intermediate CA keys that anyone could recover -- resulting in anyone being able to issue certificates for any domain), not an external circumstance that befell it. Offering it as an excuse conveys that reputation management is being prioritized over the obligations that eMudhra still owes to the ***billions*** of relying parties its mistake exposed. Those obligations do not relax because the consequences are uncomfortable.

**We expect eMudhra to prioritize its review of this issue and its security response.**


Hi Ryan,

We appreciate the email, but we do not accept its characterisation of our conduct, and we want to set out why directly.

1. The consequences of this incident are not "uncomfortable" for eMudhra; they have been accepted. We have taken the decision to exit the public TLS business, and that decision was made with the full consequences of this incident in view. Nothing in our response has been shaped by an attempt to protect that line of business.
2. eMudhra is one actor in a chain of trust, and our failure was not the only control that did not operate. The affected keys were published in April 2025 and sat in public, cross-signed, disclosed in CCADB, and covered by two years of WebTrust audits, for approximately 18 months before an external researcher identified the weakness. We have accepted our error without qualification. But a serious incident review for the benefit of relying parties also has to ask why the weakness was not detected earlier by any of the other checks the ecosystem relies on, and what should change so that it is next time. We intend to raise those questions in our report, and we would expect the community to engage with them rather than treat them as deflection.
3. The CCADB incident-reporting requirements give a CA 14 days to file a full report, and we are within that window. The earlier correspondence on this thread, including Ben's, read as what it should be: factual evidence-gathering so that the community gets an accurate account and whatever lessons there are. Your email reads differently. It assigns motive to us ("reputation management"), labels our explanation an "excuse", and does so before we have filed the report that would let anyone judge the matter on the facts. That is not an evidence-gathering tone, and it is the reason for the discomfort on our side, not the scrutiny itself.
4. On the claim that we exposed billions of relying parties. The affected CAs were revoked with reason code caCompromise within 14 hours of confirmation. No end-entity certificates were ever issued from them. Revocation status has been available via CRL and OCSP since that point. Under the Baseline Requirements and our Relying Party Agreement, a relying party is expected to check revocation status before trusting a certificate; a relying party that does so has not been exposed since the revocation. If the position is that relying parties remain exposed regardless, that can only be because their software does not check revocation at all, and in that case the exposure is a property of that software and would apply identically to a key compromise at any CA. It is not consistent to require a CA to revoke on compromise and then assess the harm as though revocation had no effect. If the root programs consider that a CA owes relying parties something beyond prompt revocation and disclosure in an incident of this kind, we would welcome that being written down, through a ballot or root-program policy, so that it applies to every CA equally. We would support that work.

To be clear, and as we have said repeatedly: we have nothing to hide. There were errors, and we have admitted them. That does not establish that eMudhra is incompetent, or that this class of error could not occur at another CA. We will use the time available to us to deliver a complete, verified report rather than a rushed one, and further updates will go to the incident bug so that the whole community sees them at the same time.

Please be assured that this review is being prioritised, and that the full report will be filed within the required period.

-eMudhra

eMudhra: on [comment 43](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c43), some facts, numbered to match it.

**On point 4 (end-entity certificates and revocation)**

Agreed that eMudhra issued no end-entity certificates from these eight CAs, and that revoking them at 09:24–09:38 UTC on 18 October was well within the seven days BR 4.9.1.2 allows.

Certificates have still been issued under them, by others. Between 09:40 UTC on 20 October and 22:02 UTC on 21 October, 107,107 certificates signed with six of the eight keys were logged to e-Szignó's 2026h2 and 2027h1 logs. Every signature verifies under the corresponding CA key. Examples, with the SHA-256 of the logged entry:

- emsign.filippo.io (DV G3B; 2027h1 leaf 21742355; `14D8565C4A4923D41451D45438AA37E75E7F719654A82137A47E0916856E6F3F`). It embeds SCTs from DigiCert, Sectigo and Cloudflare logs that Chrome lists as usable.
- Precertificates for emudhra.salesforce.com (2027h1 leaves 21768345 and 21768393).
- 106,050 proof-of-concept certificates whose only SAN is google.com, for example 2026h2 leaf 19262564 (`F3A5EE2DF42DA204F9372D61117922DF7B129D8773A93C6AA4A2A35A4E1402C6`).

None of them points to eMudhra's OCSP responders or CRLs, and all but two carry no revocation pointer at all. A client that checks revocation only for the end-entity certificate, a common configuration, finds nothing to check. Only clients that check every CA certificate in the path, receive a pushed blocklist, or have dropped the roots reject them. So the exposure is not limited to software that never checks revocation. Also, 106,058 of them chain through Sectigo's AAA cross-certificates, whose revocation Sectigo completed at 14:55 UTC on 19 October ([comment 13](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c13)).

On availability: at 04:16 UTC today, `curl 'http://crl.emsign.com?roottlscag3.crl'` returns HTTP 403, and the same request with `-A crl-check/1.0` returns 200. roottlscag3.crl is the CRL that lists the six revoked TLS intermediates. In tests on 24 October, ocsp.emsign.com, ocsp-b.emsign.com and repository.emsign.com refused curl, Wget and Python-urllib User-Agents the same way; crl-c and ocsp-c did not. Please explain this filter, say whether it applies to every CRL and OCSP URL disclosed in CCADB, and say whether eMudhra will remove it.

**On point 2 (why nobody else caught it)**

Asking why cross-signers, auditors and CT monitors don't check for small-scalar keys is fair; the check is cheap. But the earliest signal was eMudhra's own. These intermediates' CRLs failed signature validation in May 2025, and Mozilla found archived copies failing from 23 May ([comment 5](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5)). [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) says those CRLs had been signed with the original keys and were then re-signed with the flawed keys. eMudhra's report on [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) ([comment 2](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c2)) gave the cause as an incorrect CA key configuration and did not mention a second key pair. Checking which key the certificates actually carried could have found the weakness 16 months earlier. Chrome's Q8–Q10 ([comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)) ask why the report left this out, and that report needs correcting.

The 2025–26 WebTrust report's Other Matter on [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) repeats that explanation. The two annual audits together cover about 13 months of these keys' life (30 April 2025 to 31 May 2026), not two years.

**On point 3 (timing)**

Agreed that the full report is not yet due. The CCADB guidelines also expect replies to questions within 7 days, and Mozilla asked for an initial response within 24 hours on 20 October ([comment 42](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c42)). [Comment 43](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c43) does not answer Mozilla's questions or Chrome's Q1–Q12 ([comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)), which fall due under that rule on 28 October.

Some answers need records rather than analysis, because the records either exist or they don't:

1. The key generation script, ceremony report and key generation logs for 30 April 2025 (comments 32 and 33).
2. An account of CRL #11 for emSign Root TLS CA - G1, dated 14 October 2026 and signed with the key of EMSIGN ROOT TLS CA - G1 OCSP 2026 - 4 ([attachment 9664144](https://bugzilla.mozilla.org/attachment.cgi?id=9664144) [\[details\]](https://bugzilla.mozilla.org/attachment.cgi?id=9664144&action=edit); comments 7, 34 and 36). No incident bug has been filed for it.
3. The reason Series A was revoked on 30 May 2025 (Chrome Q11).
4. A correction to the status page's dates, or an explanation of how they differ from this bug's record ([comment 35](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c35)).

(In reply to Dennis Jackson from [comment #40](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c40))

MHD Ghazi Alkhalaf - I am clearing this needinfo because I believe you intended to address your questions to eMudhra rather than Mozilla.


Thank you, Dennis, for the clarification.

My intention was not to direct the questions specifically to Mozilla, but to seek a technical explanation from anyone in the community who may be able to provide one based on the information available so far.

I understand that the root cause investigation is still ongoing. However, I am particularly interested in understanding how such weak keys could have been generated in the reported HSM environment, and whether the available evidence already points to a possible mechanism.

Any technical insights would be appreciated.

In addition to the points already raised about CRLs, eMudhra's argument on Relying Party responsibility falls slightly flat on the values used for the 'Next Update' field in their CRLs.

I do not have a copy of the relevant CRL from before the incident, given the current CRL for the `emSign Root TLS CA - G3` states that it will next be updated on Apr 16 2027, it is fair to assume a similar CRL lifetime was used before the incident.

A Relying Party, staying in complete compliance with the RFCs and other such standards may cache a CRL until its next update. Although, per the BRs, a CA must publish a new CRL within 24 hours of recording a revocation, as eMudhra did, a client holding an otherwise valid cached CRL is in no way obliged to retrieve that newer CRL immediately. There is very little, if any at all, blame to be laid at the feet of Relying Parties in this incident.

Furthermore, the blocking of access to CRLs based on the User-Agent header is a violation of Section 4.9.7 of the Baseline Requirements ("CRLs MUST be available via a publicly‐accessible HTTP URL"), and Section 4.10.2 on service availability. This is a separate incident that should be tracked under [Bug 2085612](https://bugzilla.mozilla.org/show_bug.cgi?id=2085612).

A question for the Chrome Root Program:

Google Security Team members developed and publicly released [`paranoid_crypto`](https://github.com/google/paranoid_crypto) in 2022 to detect known weaknesses in cryptographic keys and signatures.

The eMudhra incident demonstrates that the tool can identify critically weak intermediate CA keys using publicly disclosed certificates. Chrome has subsequently confirmed that it examined its remaining trust boundary for the same weakness.

I would appreciate clarification on the following:

1. Were comparable cryptographic weakness checks performed during root inclusion assessments, or when evaluating cross-signed CA certificates that extend Chrome's trust boundary?
2. Are such checks currently performed against intermediate CA certificates disclosed through CCADB, including analysis of associated CA signatures and published CRLs?
3. Given the availability of `paranoid_crypto` since 2022, what technical or operational considerations prevented equivalent checks from detecting these keys during approximately 18 months of public disclosure?
4. Does Chrome intend to implement automated cryptographic screening upon CA certificate disclosure and periodically reassess its existing trust boundary as detection capabilities improve?

Separately, the `paranoid_crypto` repository was [archived on August 19, 2026](https://github.com/google/paranoid_crypto). Would Google consider restoring active maintenance or identifying an actively maintained successor?

The objective is not to assign responsibility for eMudhra's defective key generation to Chrome, but to understand why an independently detectable weakness remained unidentified by the Root Program's monitoring controls and what changes might prevent recurrence.

(In reply to Thomas Hruska from [comment #48](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c48))

With all due respect, the above comment is off topic for this tread and the deployment of DANE etc. should be discussed on dev-security-policy instead.

\[In response to [Comment 47](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c47)\]

First, we want to be clear that our immediate response (blocking the affected certificates via CRLSet) and the eventual closure of this specific incident-tracking bug represent *emergency containment*, not the end of our work - either with respect to eMudhra or our broader ecosystem defenses. While our existing controls worked to rapidly protect Chrome users once the issue was reported, a defense-in-depth ecosystem should have caught a flaw of this nature automatically at the moment of CA certificate disclosure (and, ideally well before that point). There is plenty of room to improve, and we are treating this incident as a catalyst to help close those gaps.

#### A few points of background and context:

- Within an hour of being alerted to this issue and learning how it was discovered, we evaluated all Chrome-trusted CA certificates known to our internal PKI monitoring tooling (aggregates certificates from Certificate Transparency (CT) and certificates observed "in the wild") and all Chrome-trusted certificates disclosed to the CCADB, using [`paranoid_crypto`](https://github.com/google/paranoid_crypto). That review revealed no additional weak CA keys known to paranoid threatening Chrome users. We have continued to run these evaluations regularly across those sources since the incident and will continue to do so going forward.
- Prior to this incident, weak-key and cryptographic checks were a standard part of Chrome’s ongoing ecosystem monitoring and linting evaluations. This took place in two ways: 
  1. Via [`pkimetal`](https://github.com/pkimetal/pkimetal), which integrates checks from [`badkeys`](https://github.com/badkeys/badkeys), [`zlint`](https://github.com/zmap/zlint), and other linters like [`pkilint`](https://github.com/digicert/pkilint) (the badkeys, pkilint, and zlint checks predate the existence of pkimetal which launched in 2024). However, prior to this incident, standard linting tools focused on algorithmic checks for RSA/DSA and blocklist checks for ECDSA; they had not implemented the Baby-Step Giant-Step (BSGS) discrete logarithm checks for small EC private scalars or pairwise EC key differences that [`paranoid_crypto`](https://github.com/google/paranoid_crypto) includes. These checks evaluate dumps from CCADB and our PKI monitoring database.
  2. Via an internal Google service (not specific to Chrome) running `paranoid_crypto` against certificates disclosed to CT. Because the compromised eMudhra TLS intermediate CAs had never issued any leaf certificates logged to CT (and were not themselves logged to a log usable in Chrome) prior to Wayne’s report, they never entered that pipeline. Prior to this incident, our team was not aware that this internal pipeline was not also scanning dormant CA certificates disclosed only to the CCADB. We are now in the process of expanding this internal scanning to cover certificates disclosed to the CCADB, and we have filed [`mozilla/CCADB-Tools#185`](https://github.com/mozilla/CCADB-Tools/issues/185) to integrate automated cryptographic weak-key checking (including `paranoid_crypto` checks) directly into CCADB as a prerequisite gate before CA certificates can be disclosed.
- When the Chrome Root Store launched in 2022, its initial trust list was baselined against existing root programs to ensure ecosystem parity and avoid widespread user breakage during the transition from the platform verifiers relied upon by Chrome users pre-launch. Since launching our independent store, we have progressively raised our operational and policy bars - introducing mechanisms like root term limits and a variety of phase-out events that aim to align CRS-included hierarchies on use-case and the use of modern hierarchies, and have taken enforcement actions against CA Owners that continuously fail to meet expectations.
- Because eMudhra's currently trusted roots were part of that 2022 baseline, they had not yet undergone a full Chrome Root Store inclusion review (though they remain subject to the continuous monitoring and incident analysis we apply to all CAs).
- Notably, since 2022, eMudhra has submitted four separate applications to add new roots to the Chrome Root Store - a response to the forcing function our root term-limit policy and other policy phase-outs are designed to create. Three of the four applications were denied during screening due to failures to follow program instructions or submit a complete  and policy-compliant application package. Because of these failures, eMudhra was assigned a [6-month cool-down period](https://googlechrome.github.io/chromerootprogram/crp/apply-for-inclusion/#:~:text=Depending%20on%20the%20reason%20for%20application%20rejection%2C%20the%20Chrome%20Root%20Program%2C%20at%20its%20sole%20discretion%2C%20may%3A), where any subsequent inclusion request was not reviewed until that time was up. Prior to Wayne’s discovery, the fourth application was pending review, but has since been denied.

#### To address your specific questions directly:

Were comparable cryptographic weakness checks performed during root inclusion assessments, or when evaluating cross-signed CA certificates that extend Chrome's trust boundary?


CA certificate cryptographic and linting checks (via `pkimetal`, incorporating `badkeys`, `zlint`, and related suites) have long been performed during root inclusion/cross-certificate request assessments and our ordinary and ongoing ecosystem monitoring. However, prior to this incident, those industry-standard linting suites did not include the BSGS small-scalar or pairwise-difference EC checks present in `paranoid_crypto`. We have now added `paranoid_crypto` to those workflows.

(Note: A CA issuing itself a certificate is neither considered a cross-certificate nor an externally-operated CA, and therefore we do not consider these events to expand our trust boundary because the number of operators with key material trusted by default in Chrome remains the same.)

Additionally, the ongoing project paranoid pipeline described above would have flagged these weak keys once these CAs began disclosing certificates to CT - even if done so before an inclusion request was submitted or processed.

Are such checks currently performed against intermediate CA certificates disclosed through CCADB, including analysis of associated CA signatures and published CRLs?


Following this incident, we expanded our recurring checks across all CCADB-disclosed CA certificates, and we are actively evaluating expanding continuous automated analysis to cover associated CA signatures (including CRLs) as well as gating CCADB disclosure via [`mozilla/CCADB-Tools#185`](https://github.com/mozilla/CCADB-Tools/issues/185).

While audits were not mentioned in your comment, we’re also pursuing improvements in this space, along with other requirements related to remote key attestation to promote increased transparency and accountability where it arguably matters most.

Given the availability of paranoid\_crypto since 2022, what technical or operational considerations prevented equivalent checks from detecting these keys during approximately 18 months of public disclosure?


As noted above, this came down to two factors: (1) the standard linting tools used across the ecosystem (`pkimetal`, `badkeys`, `zlint`) and relied by our ongoing linting checks (and that do pull from CCADB) did not check for small EC private scalars or pairwise key differences prior to this incident, and (2) Google's existing internal `paranoid_crypto` CT pipeline only evaluated certificates disclosed to the CT logs relied upon by Chrome - meaning intermediate CAs disclosed to the CCADB that had never issued a CT-logged certificate (or, were logged themselves) were outside its ingestion scope. As a reminder, because Chrome enforces CT for TLS certificates validating to CRS-included roots, leaf disclosure to CT is a prerequisite for a certificate to be trusted by Chrome - meaning these keys could not have been exploited against Chrome users covertly without entering CT monitoring pipelines.

Does Chrome intend to implement automated cryptographic screening upon CA certificate disclosure and periodically reassess its existing trust boundary as detection capabilities improve?


Yes to both.

We are already performing recurring assessments of the existing trust boundary (across CT, CCADB, and certificates seen in the wild) and have proposed [`mozilla/CCADB-Tools#185`](https://github.com/mozilla/CCADB-Tools/issues/185) so that automated weak-key screening occurs at the point of CCADB disclosure for the benefit of all CCADB-relying root programs.

As mentioned above, extending the existing paranoid pipeline to consider CCADB data further improves our detection capabilities.

Separately, the paranoid\_crypto repository was [archived on August 19, 2026](https://github.com/google/paranoid_crypto). Would Google consider restoring active maintenance or identifying an actively maintained successor?


We speak only for the Chrome Root Program and only directly control our own operations. Because `paranoid_crypto` was developed and maintained by a separate team within Google, we cannot make commitments regarding the repository's status - though we plan to pursue this conversation internally.

In the meantime, within the scope of what the Chrome Root Program directly controls, we have (1) already integrated the existing open-source `paranoid_crypto` checks (which remain freely available) into our own assessment and monitoring pipelines, (2) taken steps to expand the internal paranoid service to consider CCADB data, and (3) we have filed [mozilla/CCADB-Tools#185](https://github.com/mozilla/CCADB-Tools/issues/185) so these checks can be enforced at the point of CCADB disclosure. We are also encouraged to see actively maintained community tools (such as [`badkeys`](https://github.com/badkeys/badkeys/issues/38#issuecomment-6335764233) and [`pkimetal`](https://github.com/pkimetal/pkimetal/pull/2099)) already moving to incorporate additional checks in response to this incident (adding another layer of defense to our recurring checks). We will continue to use every policy and technical lever within our control to raise quality bars and remove risky CAs from the Chrome Root Store.

(In reply to Dennis Jackson from [comment #42](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c42))

Created [attachment 9667275](https://bugzilla.mozilla.org/attachment.cgi?id=9667275) [\[details\]](https://bugzilla.mozilla.org/attachment.cgi?id=9667275&action=edit)

eMudhra-questions.pdf

The Mozilla Root Program sent the attached questions to eMudhra on the 20th October at 20:31 UTC. eMudhra was asked to provide an initial response within 24 hours. After the deadline passed on October 21st, eMudhra asked for a further 24 hours to respond. As of the time of writing on Friday 23rd, Mozilla has not received a response to these questions.

We share the Chrome Root Program's concerns and whilst we appreciate eMudhra's difficulties, we expect eMudhra to uphold its obligations to Mozilla and the wider community.


We have responded to the set of questions asked specifically by Mozilla in direct correspondence. Due to the sensitive nature of some of the content contained therein, we will work with Mozilla, and the other major Browser Trust Programs to ensure any data appropriate for public release can be updated here.

We will also provide a copy of responses to Mozilla's questions directly to each of the other Browser Trust Programs for their internal consumption.

We note that additional questions are outstanding to other Browser Trust Programs and these will be responded to in the time permitted.

We


You are an eight day old Bugzilla account with the only identification/affiliation being the name "Scott".

Can I assume you represent eMudhra and this sudden opposition to the necessary transparency is their position?

Given the scale of the mess here I think it is only right that the entire security community be able to view the source code of the flawed key ceremony.

That it is uncomfortable or “sensitive” to release this source code is, given the circumstances, not an excuse. Such an error deserves public accountability, and an opportunity for all, not just those at a select few root programmes, to learn from whatever mistakes may have been made in the source code.

Understanding the technical circumstances that made this possible would be useful.

Assuming that the keys were generated or managed in a Utimaco or other HSM-backed environment, the combination of the HSM security architecture, key management policies, and associated operational controls would be expected to make the introduction of noncompliant keys difficult without an explicit exception, a bypassed control, or a configuration or process failure.

This is not intended as an allegation of misconduct or as speculation about anyone's intentions. However, **if malicious intent was not involved, this incident raises an important question about the effectiveness of the controls surrounding the HSM appliance** and its key management life cycle.

eMudhra: following on comments 11, 18, and 51.

[Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) says "The RSA issuers went through a different path as per our assessment of the code and are therefore not impacted." [Comment 18](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c18) kept trust in emSign Root CA - G1 "at this time." Nothing on this bug yet describes that different path.

EM DV, OV and EV TLS CA - G2B and G2C, and EM OV CS CA - G2B and G2C, are RSA intermediates generated on 30 April 2025 ([Bug 1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559)). They were generated on Utimaco Se-Series Gen2 HSMs, the same model used for the eight compromised G3B and G3C keys ([attachment 9664473](https://bugzilla.mozilla.org/attachment.cgi?id=9664473) [\[details\]](https://bugzilla.mozilla.org/attachment.cgi?id=9664473&action=edit), rows 29-36). EM DV TLS CA - G2B and EM OV TLS CA - G2C, for example, are issued by emSign Root TLS CA - G1, which emSign Root CA - G1 cross-certifies. Sectigo's AAA Certificate Services cross-certified them on 14 May 2025, the same date as the G3B and G3C cross-certificates. Mozilla's questions of 20 October ([attachment 9667275](https://bugzilla.mozilla.org/attachment.cgi?id=9667275) [\[details\]](https://bugzilla.mozilla.org/attachment.cgi?id=9667275&action=edit), Q4b and Q6b) ask for any secrets protected by weak wrapping keys, and for the wrapping or transport keys used for each exported or backed-up CA key. A weak wrapping key leaves the RSA public key looking normal, so linting the certificates cannot answer this.

Please state, here or in the public summary that [comment 51](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c51) describes:

1. Whether the G2B and G2C keys were generated, wrapped, exported, or backed up by the same script or in the same session as the G3B and G3C keys, and if not, what the "different path" in [comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) was.
2. Which wrapping or transport keys, if any, protected the G2B and G2C keys, and whether any of them are among the weak keys.
3. Whether the Key Generation Script versions actually executed on 30 April 2025, along with the ceremony and HSM logs, have been provided to Mozilla under its supporting-records request, and whether a qualified auditor has reviewed them.
4. Why Series A (G2A and G3A) was replaced by Series A-1, dated 29 May 2025 ([comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30), Q11).

Separately: CRL #11 for emSign Root TLS CA - G1 (14 October 2026) appears to have been signed with the key of EMSIGN ROOT TLS CA - G1 OCSP 2026 - 4 (comments 7, 34 and 36), and no incident has been filed for it. [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30), Q12 asks whether multiple key pairs exist for emSign Root TLS CA - G1. Until the G1 key records have been reviewed, I do not see a basis for relying parties to keep trusting emSign Root CA - G1 or emSign Root TLS CA - G1.

### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a894478_271282)

•
          \[In response to [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) and [Comment 58](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c58).\]

[Update 6](https://emudhra.com/en/post/certificate-security-incident#update-6) on eMudhra's status page ([`emudhra.com/en/post/certificate-security-incident`](https://emudhra.com/en/post/certificate-security-incident), 28 October 2026) states that the roughly 30,800 certificates issued under the affected G3 hierarchies belong to a client ecosystem in the United States, and that eMudhra had given this ecosystem "an alternate issuance pathway through eMudhra's G1 RSA root, and they are now using that pathway." Under the heading "Orderly transition out of the G1 TLS Roots," it states that eMudhra has "asked the browser and root-store programs for time so that the impacted client ecosystem in US can move over in an orderly way," that "G1 issuance is being used only to support this transition," and that "eMudhra will stop issuing TLS certificates from G1 once the federation's transition is complete."

None of this has been disclosed on this bug, and the 7-day response window set in [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) passed at 20:38 UTC on 28 October 2026 without answers to Q1 through Q12:

- [Update 3](https://emudhra.com/en/post/certificate-security-incident#update-3) (21 October 2026) still states: "We are issuing fresh certificates to the affected customer ecosystem from an alternate, independently operated, publicly trusted CA hierarchy." [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) Q2 asked on 21 October 2026 whether affected subscribers were being migrated to G1 ([Comment 19](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c19)), to another CA Owner's hierarchy, or both. [Update 6](https://emudhra.com/en/post/certificate-security-incident#update-6) confirms the US ecosystem is on eMudhra's own G1 root while eMudhra remains "in advanced discussions with leading SSL/TLS providers to support the move."
- On 22 October 2026, eMudhra issued a [press release](https://www.einpresswire.com/article/951482814/emudhra-to-exit-global-ssl-tls-certificate-business) announcing its Board had decided to withdraw from the global SSL/TLS certificate business. The same day, [Update 4](https://emudhra.com/en/post/certificate-security-incident#update-4) on the status page told relying parties and subscribers: "Our G1 root certificates remain active and continue to be fully supported."
- InCommon, the US ecosystem referenced in [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) and [Update 6](https://emudhra.com/en/post/certificate-security-incident#update-6), states on its [22 October 2026 service update](https://incommon.org/about/news/incommon-certificate-service-update) and [certificate FAQ](https://incommon.org/certificates#certificate-service-faq) that "Beginning in 30 days (the specific day and time will be confirmed by CertiNext), eMudhra will stop issuing new certificates from any intermediate chained to its emSign public roots." The [certificate FAQ](https://incommon.org/certificates#certificate-service-faq) adds that for most issued certificates the validity duration is "typically 200 days," that "as of October 22, 2026, InCommon ECC certificate issuance has been restored (via the emSign G1 Root CA), and existing clients can be used to renew a valid certificate without needing to modify their configuration," and that InCommon "cannot independently verify" eMudhra's initial finding that no root or InCommon intermediate keys were compromised "because the systems involved are operated by eMudhra."

Please provide the following on this bug:

1. The transition plan described in [Update 6](https://emudhra.com/en/post/certificate-security-incident#update-6) and the [InCommon notices](https://incommon.org/about/news/incommon-certificate-service-update): the exact period eMudhra has asked the root programs to keep G1 trusted, the exact date issuance from G1 will cease, the maximum validity period of certificates being issued under G1 during this window, and the subscriber and certificate counts requested in [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) Q6.
2. Which intermediates under G1 (`emSign Root TLS CA - G1` [`crt.sh/12478656983`](https://crt.sh/?id=12478656983), cross-certified by `emSign Root CA - G1` at [`crt.sh/14658191777`](https://crt.sh/?id=14658191777)) are issuing both the RSA certificates and the ECC certificates that [InCommon's FAQ](https://incommon.org/certificates#certificate-service-faq) states were restored "via the emSign G1 Root CA" on 22 October 2026. `InCommon Intermediate CA - DVG2C` ([`crt.sh/25846937072`](https://crt.sh/?id=25846937072)) and `InCommon Intermediate CA - OVG2C` ([`crt.sh/25849656014`](https://crt.sh/?id=25849656014)) were certified by `emSign Root TLS CA - G1` on 8 April 2026, and [attachment 9664473](https://bugzilla.mozilla.org/attachment.cgi?id=9664473) (`Issuer_HSM_Mapping.xlsx`, rows 2 through 7) lists `DVG3C`, `OVG3C`, `EVG3C` (`ECC`) and `DVG2C`, `OVG2C`, `EVG2C` (`RSA`) on a Crypto4A `QxHSM-1`. For each intermediate issuing under G1, please provide its key generation date, ceremony report, key generation script, and auditor witness statement, state whether `DVG3C`, `OVG3C`, or `EVG3C` were cross-certified under G1 or whether the RSA intermediates are signing ECC leaf certificates, and confirm that no step of the 30 April 2025 script ([Bug 1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559)), or any wrapping key from that ceremony, was used for them.
3. Why [Update 3](https://emudhra.com/en/post/certificate-security-incident#update-3) continues to state that replacement certificates for this ecosystem come from "an alternate, independently operated, publicly trusted CA hierarchy" ([Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) Q2), and when [Update 3](https://emudhra.com/en/post/certificate-security-incident#update-3) and [Update 4](https://emudhra.com/en/post/certificate-security-incident#update-4) will be corrected on the status page.

Every certificate issued along this transition pathway relies on `emSign Root TLS CA - G1`, while [Comment 30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) Q12 (whether multiple key pairs exist for `emSign Root TLS CA - G1`, following the CRL #11 signature mismatch in [Comment 7](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7), [Comment 34](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c34), and [Comment 36](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c36)) and the G1 ceremony and wrapping-key records requested in [Comment 58](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c58) and [attachment 9667275](https://bugzilla.mozilla.org/attachment.cgi?id=9667275) remain unanswered. Evaluating any continued trust window for G1 depends on those disclosures.

Separately: [Comment 35](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c35) asked eMudhra at 09:30 UTC on 22 October 2026 to correct the dates in [Update 3](https://emudhra.com/en/post/certificate-security-incident#update-3). Archived copies of the status page from [21:36 UTC on 21 October 2026](https://web.archive.org/web/20261021213628/https://emudhra.com/en/post/certificate-security-incident) and [07:58 UTC on 22 October 2026](https://web.archive.org/web/20261022075829/https://emudhra.com/en/post/certificate-security-incident) state that the researcher reported the issue on "October 18, 2026" and list "October 18, 2026 (late evening, India time): We were made aware" and "October 19, 2026: We revoked all eight intermediates." By [13:25 UTC on 22 October 2026](https://web.archive.org/web/20261022132549/https://emudhra.com/en/post/certificate-security-incident) both places had been altered to read 17 October 2026 and 18 October 2026 without a correction notice, and [Comment 35](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c35) has received no response here. Please record that correction on this bug, and answer [Comment 35](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c35)'s second question on whether [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) was within the scope of the subsequent audits.

Comment on [attachment 9670867](https://bugzilla.mozilla.org/attachment.cgi?id=9670867) [\[details\]](https://bugzilla.mozilla.org/attachment.cgi?id=9670867&action=edit)

eMudhra\_Response\_to\_Google.pdf

Response to [Comment #30](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)

Sorry Folks, was having difficulty attaching the response file.

This document was shared earlier today with Chrome and the other Browser Trust Programs directly. It is attached here for community disclosure.

In regards to 'Q12. The October 14 roottlscag1.crl signature'. The full incident report is now due - clock starts when you became aware. In your own scoping you still have not noticed that a second CRL was impacted. I already publicly stated in [Comment 36](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c36):

The CRL I gave was just *one* of them detected on 10-14 where they signed with OCSP certificates generated that day, and then swapped them on the next CRL issuance without reporting it to anyone.


What was not mentioned: emSign Root TLS CA - G3 (CRL 10) was signed by EMSIGN ROOT TLS CA - G3 OCSP 2026.

On looking around I could not find an instance of a CA signing a CRL with an OCSP certificate, ever. The simple answer to that is you're using emCA, rather than EJBCA. The security target of emCA 4.0.3 is available [publicly](https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/eMudhra_emCA_ST_v7.3.pdf), and it matches your prior incidents and deployment.

**Q1**: Have eMudhra made their emCA clients aware of what went wrong in this Key Generation Ceremony, and had a third-party assess for similar issues in client ceremonies?

The lack of ACME-ARI usage on your subscribers is also a concern. There seems to be no prior outreach and help in implementation provided to subscribers. Those were all required as per Mozilla Root Store Policy:

**6.1.3 Delayed Revocation**

Mozilla’s goal is to ensure that revocation occurs as swiftly as possible while maintaining the overall security and stability of the web. Mozilla does not grant exceptions to the revocation requirements of the TLS BRs.

Beginning September 1, 2025, each CA operator MUST:

- engage in proactive communication and advise subscribers well in advance about the revocation timelines and explicitly warn them against using publicly-trusted TLS server certificates on systems that cannot tolerate timely revocation;
- include appropriate language in customer agreements requiring subscribers’ timely cooperation in meeting revocation timelines and acknowledging the CA’s obligations to adhere to applicable policies and standards; and
- prepare and maintain comprehensive and actionable plans to address mass revocation events in accordance with section 5.7.1.2 of the TLS BRs.

Compliance with section 5.7.1.2 of the TLS BRs SHALL be evaluated as part of the CA operator’s annual TLS BR period-of-time audit.


That you are asking for extensions of revocation until at least November 15th is absolutely irresponsible. You should be considering every subscriber certificate to be compromised as the containment and your handling of key material has not been confirmed to be safe.

**Q2**: Can you evidence your compliance to MRSP against each of those 3 points? Timely revocation here is 24h/5d, and we're well past that.

Baseline Requirements, 6.1.1.1 CA Key Pair Generation

the CA SHALL:

1. prepare and follow a Key Generation Script,
2. have a Qualified Auditor witness the CA Key Pair generation process or record a video of the entire CA Key Pair generation process, and
3. have a Qualified Auditor issue a report opining that the CA followed its key ceremony during its Key and Certificate generation process and the controls used to ensure the integrity and confidentiality of the Key Pair.


Then as per your recent CPS:

6.1.1. Key Pair Generation

Entity: Sub-CA

FIPS 140-1/2 Level: 3

Hardware or Software: Hardware

Generated in Entity Module: Yes

CA creates a verifiable audit trail for CA key pair generation as per the security requirements Procedures that are followed and the same will be documented. The process is validated by an Auditor


**Q3:** Can we see this verifiable audit trail?

6.2.6. Private Key Transfer into or from a Cryptographic Module

CA key pairs are generated and secured by hardware cryptographic modules. CA ensures that The CA private keys are backed up securely and transferred in an encrypted form.

6.2.7. Private Key Storage on Cryptographic Module

CA stores Private Keys in the hardware cryptographic module and keys are not accessible without an authentication mechanism that complies with the FIPS 140-2 rating of the cryptographic module.


**Q4:** Explain how these aspects of your CPS make sense against question 7's answer:

April 30, 2025. At Key Ceremony 1, the PKI Operations script generated each B and C key, then wrapped, unwrapped and re-imported it as a planned rehearsal. From that day there were two objects with the same label for each CA, and the participants created them. What we did not understand then was that the key objects contained different data, and the CA certificates had been issued over the re-imported objects and not the originally generated ones.


[Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) states:

a) a set of original ECC keys were created onboard as expected b) an approved deviation to our usual KGC to test a wrap/unwrap was introduced as these keys were meant for export for this instance c) a flaw in the code resulted in the second pair of keys being created onboard which were weaker


We still have not had an explanation as to why the keys were being exported rather than generated where they would be used. Can we stop talking around the issues that occurred here and have a step-by-step on what happened? Even a diagram of what you believe occurred would be helpful at this stage.

**Q5:** Were two key sets generated in the HSMs, or is the second set a mangled version of the first on re-import?

**Q6:** If the second set was generated in the HSM, please detail the precise configuration that caused this incident.

**Q7:** On generation was there no test certificate, or any material really, signed by the correct key set for verification on the wrap/unwrap and re-import step?

**Q8:** Was there no accounting for twice the number of keys generated that day and held on the HSMs? That none of this came up internally, or during any audit is quite concerning - presumably there is no internal inventory of keys.

I still have no idea why we do not have the Key Generation Ceremony records and python script here. Please supply them as soon as possible, as the auditor sign-off sheets are not credible evidence given the state of things.

eMudhra: items from [comment 62](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c62) ([attachment 9670867](https://bugzilla.mozilla.org/attachment.cgi?id=9670867)) that remain open.

1. **RSA Series B/C (G2B, G2C).** Q11 covers Series A and A-1 only. [Comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) states the RSA issuers "went through a different path." The G2B/G2C keys were generated on 30 April 2025 ([Bug 1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559)) on the same HSM model as G3B/G3C ([attachment 9664473](https://bugzilla.mozilla.org/attachment.cgi?id=9664473)). Requested: whether G2B/G2C keys passed through the wrap/unwrap/re-import step or the same script; the path used if not; and any wrapping or transport keys involved ([attachment 9667275](https://bugzilla.mozilla.org/attachment.cgi?id=9667275), Q4b and Q6b).
2. **Ceremony records.** Q9 states the script specified creating the CSRs from the re-imported keys. Requested: whether the executed 30 April 2025 script, ceremony logs, and HSM logs have been provided to the root programs ([comment 51](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c51)), and whether a public summary is planned.
3. **HSM operation.** Requested: the HSM operation that produced the re-imported key objects, and the HSM mode (FIPS or otherwise) in use at the time.
4. **Independent review.** Q8 and Q9 refer to an independent review. Requested: reviewer, scope, and expected completion date.
5. **Q12(a) scope review.** Requested: expected completion date, and whether intermediates and OCSP responder keys are in scope.
6. **Q12(c) CRL report.** Q12(c) commits to a separate preliminary report on 29 October 2026. Requested: a link here when filed, with emSign Root TLS CA - G3 CRL 10 ([comment 65](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c65)) included in scope.

Some questions for eMudhra, please excuse any redundant or irrelevant ones:

1. Specify the exact padding scheme and byte-level structure of the payload that was fed back into the HSM during the unwrap step for the Series B and C keys.
2. Provide cryptographic proof demonstrating how the specific wrapping algorithm and key encryption key applied to the original valid keys deterministically decayed into the exact scalars 4, 56, 66, 115, 155, 156, 230, and 237 upon re-import.
3. Identify who authorized the decision to swap the CRL signing handle in June 2025 instead of executing the mandatory CA Key Compromise revocation protocols.
4. Under what section of the eMudhra Certification Practice Statement was the operational use of an un-audited, secondary key handle for production CRL generation justified?
5. Detail the specific technical instructions given to the Incident Response team to classify the June 2025 CRL signature failure as a configuration error rather than a cryptographic breach.
6. Did the evidence package provided to the WebTrust Qualified Auditor for the 2025 Period of Time report include the unredacted incident tickets, root cause analysis, and HSM handle queries related to the June 2025 CRL signature failures? If yes, provide the auditor's written justification for failing to report a violation of KGC constraints.
7. Will eMudhra authorize Sectigo to publish the exact timestamps, IP addresses, and raw byte structures of the Certificate Signing Requests submitted for the Series B and C intermediates?

and some more in addition:

8. Why would a production KGC script explicitly specify creating the cross-signing CSRs from the re-imported rehearsal objects rather than the primary keys natively generated on the HSM?

9. Why did eMudhra switch HSM vendors and key generation protocols for the replacement series within a 30-day window? Was the Utimaco hardware or the Python script already under internal investigation or suspicion prior to the June 6 CRL failure?

10. How does the emCA software architecture permit a cryptographic key lacking the `cRLSign` bit to successfully sign and publish a Root CA CRL? What other RFC 5280 cryptographic boundary constraints does the emCA software fail to enforce at the code level?

11. Does the G1 hierarchy share or operate under an identical PKI Operations team, utilize the same emCA software, or is subject to the same internal audit apparatus that governed the [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) KGC deviation?

12. The RSA counterparts (G2B and G2C) were generated on the same day for the same US/EU export purpose as the B and C series keys targeted by the rehearsal script. Were the RSA keys subjected to the same wrap/unwrap script execution? If yes, why did the script's code flaw only truncated the elliptic curve scalars and left the RSA primes secure. If no, why was the rehearsal applied selectively to ECC keys and not the RSA keys intended for the same foreign subsidiaries?

Some notable InCommon DVG3C dataset patterns:

- The extra 1 second bug recurs for all three categories of certificate lifetimes \~30-day (`2,592,001s`), 90-day (`7,776,001s`), and 200-day (`17,193,601s`).
- Zlint warnings in prometheus.sps-psmt-d01.sys.utah.edu (`00ca4dc3f351ec7033e4599dc54757937712184b7f42ba16d4475e4478abaa4c`)
  - `w_server_cert_valid_time_longer_than_199_days`
  - `w_ext_subject_key_identifier_not_recommended_subscriber`
  - `w_subject_common_name_included` (this one occurs in other certs e.g., `803988d1c367c3ed052da1ed728fde229d448a757ccbda657c05785393a62607`)
- Precertificates present e.g., `web.cicsnc.org`
- At least one test/non-institutional entry `00b966051d292d67c4ac55772321faa9b33f9e478ffc84edca3b2ba0720fe8f2`

**NOTE:**

1. The dataset above was generated with the following Censys query:

```
(cert.parsed.issuer_dn: "InCommon Intermediate CA - DVG3C" and 
   cert.parsed.validity_period.not_before<= "2026-10-28T09:18:00Z" and 
   cert.parsed.validity_period.not_after >="2026-10-28T09:18:00Z")
```
1. The aggregate counts do not match exactly, but are close, to those reported in the document shared by eMudhra to Chrome (and here).

| issuer\_dn | crl.revoked | count | % | 
|---|---|---|---|
| OVG3C | false | 21,009 | 90.59% | 
| OVG3C | true | 2,183 | 9..41% | 
| DVG3C | false | 5,669 | 92.81% | 
| DVG3C | true | 439 | 7..19% | 

Additionally:

- Zlint warnings in emSign SSL CA - G1 (`47b2efbc3670e7db4b41f22c51fc02ee84fb2dbf3082a49f2c2688122e9210a1`):
  - `n_ca_digital_signature_not_set`
  - `w_sub_ca_aia_does_not_contain_issuing_ca_url`
- [Bug 1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559): summary comment timestamp is 2025-05-09 12:28 PDT but the text says `2025-05-10: Certificate was published to the CCADB.`
- CCA India 2022 SPL (`b724689b79b2ef9421ef8f5cc733eb093851b170ee715177005a09f226d8c91a`):
  - Extra 1 second validity period
  - CRL status is [Unknown on crt.sh](https://crt.sh/?q=b724689b79b2ef9421ef8f5cc733eb093851b170ee715177005a09f226d8c91a) as the URL reports 404. This appears to be an issue with a lowercase `L` in `https://www.cca.gov.in/rw/resources/CCAIndia2022SPLlatest.crl`. The correct URL is `https://www.cca.gov.in/rw/resources/CCAIndia2022SPLLatest.crl`

While some of the additional points addressed here may appear to be unrelated, these add to the evidence here and in other bugs (i.e., [1965559](https://bugzilla.mozilla.org/show_bug.cgi?id=1965559), [1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728), [1973341](https://bugzilla.mozilla.org/show_bug.cgi?id=1973341), [2073581](https://bugzilla.mozilla.org/show_bug.cgi?id=2073581), [2082408](https://bugzilla.mozilla.org/show_bug.cgi?id=2082408)), that there are repeated diligence failures masked by performative post-mortems that need to be addressed.

(In reply to Suman from [comment #69](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c69))

Begs a couple additional questions -

1. Does the emCA software lack a pre-issuance linting pipeline, thus violating TLS Baseline Requirements, or was it overridden to allow the issuance of non-compliant certificates? If it was overridden, who authorized the system-wide bypass of linting errors for the InCommon and CCA India profiles?
2. In [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) and 1965559, eMudhra claimed to have instituted comprehensive post-signing validation controls. Given that test/non-institutional certificates seem to have successfully bypassed these "controls" and polluted production logs, and basic URLs are misconfigured, will eMudhra address the failure of the "automated post-signing validation" controls being technically enforced? Which authority signed off on the [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) remediation without verifying its deployment?

For eMudhra and the external auditor KPMG -

1. Would eMudhra release the unredacted Statement of Work made with KPMG? Does the SoW explicitly mandate a reverse engineering of the entropy collapse mechanism?
2. Is the investigation team team led by, include a dedicated cryptanalyst? If not, with whom lies the cryptographic liability to reproduce the math, without which the exercise would be at risk of being computationally meaningless?
3. Would Mozilla and Google require KPMG to cryptographically attest - under penalty of their WebTrust standing - that they have independently reproduced the deterministic HSM failure that caused the P-384 scalar collapse?

eMudhra: Q12(c) of [attachment 9670867](https://bugzilla.mozilla.org/attachment.cgi?id=9670867) said eMudhra planned to file a separate preliminary incident report for the invalid CRL on 29 October. Nothing has been filed here, on [Bug 2080742](https://bugzilla.mozilla.org/show_bug.cgi?id=2080742), or as a new bug, although eMudhra posted Full Incident Reports on [Bug 2082782](https://bugzilla.mozilla.org/show_bug.cgi?id=2082782#c2) and [Bug 2082872](https://bugzilla.mozilla.org/show_bug.cgi?id=2082872#c1) on 30 October. Q12(c) dates awareness to 15 October, so under [CCADB](https://www.ccadb.org/cas/incident-report) the Full Incident Report was due 29 October. Requested: the report, or a new date and the reason for the delay.

Our earlier answers in this thread and the set of information provided by us to Browsers were based on our analysis of what our internal teams could gather up until that point in time. This included which script pathways each set of keys went through, and which file versions were used during the 30 April 2025 ceremony and subsequent events, as we had requested from them. That ceremony and the transfer that followed were unique events, and we have neither ran them previously nor repeated them subsequently. We have now appointed KPMG to do an independent review of the incident.

We will need an additional week (Nov 9th, 2026) before we share the full incident report.

This simply isn’t good enough.

Whilst I accept there may be open questions that can’t be answered yet without the further investigation that can take until next week, there are certainly answers and learnings that can be posted now. This has not happened. In fact, eMudhra have barely answered any questions beyond the surface level. You should publish promptly what you already know, whilst noting any open questions that are still be worked on.

The primary thing that we, as cryptographic software developers and Relying Parties, need now is the source code of the flawed key ceremony. You have had far more time than needed to redact any sensitive information and publish this source code, and yet it has not been done.

eMudhra: on [comment 73](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c73).

1. [Comment 73](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c73) says earlier answers were "based on our analysis of what our internal teams could gather up until that point in time," including "which script pathways each set of keys went through." For each answer in [comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) and [attachment 9670867](https://bugzilla.mozilla.org/attachment.cgi?id=9670867), please state whether it remains confirmed or is withdrawn pending the review, and identify the script version and logs it rests on. In particular, state whether [comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11)'s statement that "The RSA issuers went through a different path as per our assessment of the code and are therefore not impacted" remains confirmed ([comment 58](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c58), [comment 66](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c66)).
2. [Comment 73](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c73) refers to "That ceremony and the transfer that followed." Please describe that transfer: whether it is the export described in [comment 11](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11), when it occurred, and which keys it covered.

Few more critical disclosures requested, all reasonably addressable even in a time crunch:

1. Does the KPMG SOW include a "Management Representation" clause that permits KPMG to rely on verbal, curated, or pre-filtered executive summaries in lieu of direct, bare-metal forensic extraction from the HSMs and server logs? A refusal to waive management representation clauses nullifies the independence of the audit and reduces KPMG to a paid stenographer.
2. Timely publication of the cryptographic hashes of the database records, incident tickets (Jira/ServiceNow), and chat logs spanning the relevant period to voluntarily freeze the internal audit trail and preclude the possibility of retroactive sanitization to maintain community trust.
3. Assurance from KPMG re: adherence to incorruptible protocol - forensically image and escrow the emCA source code repository and commit history exactly as it existed on October 17, 2026. The independent review must formally evaluate the static code-level bypassing of RFC 5280 constraints and the disabled pre-issuance linters.
4. The disclosure of the exact procurement and provisioning timeline, including evidence like Purchase Order (PO), invoice, and provisioning dates for the Entrust nShield HSMs used for the May 29 Series A-1 generation.

eMudhra,

1. In [comment #73](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c73), the "transfer that followed" was cited as part of the unique event. If the wrap/unwrap testing collapsed the elliptic curve scalars *prior* to export, what was the exact cryptographic payload transmitted to the US and European data centers? Did the destination HSMs successfully unwrap and ingest the collapsed keys? Please include the destination HSM firmware logs for this process.
2. Earlier, eMudhra has requested the root programs keep G1 alive to facilitate the migration of the US InCommon ecosystem. However, G1's CRL #11 (published October 14, 2026) was proven to be signed by an OCSP responder key, indicating the same or similar compromised pipeline that fails to enforce RFC 5280 constraints. With that established, why should the Root Programs permit the InCommon ecosystem to be migrated onto a hierarchy that likely shares the same deterministic routing failures as the compromised G3? How is it physically and architecturally possible for a software operator to "map" a highly-available online OCSP key to an offline Root CA CRL generation process? This admission implies that the airgapped CA private keys and online OCSP responder keys share the same networked HSM partitions or emCA database environment. Please state on record whether G1 is physically air-gapped, or if its HSM is network-accessible to the online PKI operations layer.

### [Updated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#a1357161_772139)

•
          It is now the 9th of November, eMudhra's self-imposed delayed deadline to submit their final incident report. As it is nearly the end of the working day in India, do eMudhra plan to submit their incident report today? If not, what is the reason for an additional delay?

Thank you to everyone who has contributed to investigating and documenting this incident.

Naveen, I wanted to follow up on the full incident report that was expected by November 9. I appreciate that the investigation is complex and that addressing the technical questions raised by the community takes time.

Could eMudhra provide a brief status update and an estimated publication date for the report? It would also be helpful to understand when the outstanding questions raised throughout this thread will be addressed, particularly those concerning the root cause, scope of impact, and effectiveness of the existing controls and audits.

I appreciate everyone’s continued work on this and look forward to the findings.

Thank you to everyone continuing to investigate this incident.

I’d like to raise an additional question regarding the scope of the investigation and the operational boundaries between eMudhra, CertiNext, InCommon, and SSL.com, particularly in light of eMudhra’s announced withdrawal from publicly trusted TLS certificate issuance.

Business relationships and background

For context, the publicly documented relationships are:

- eMudhra Limited: The parent company responsible for the emSign CA infrastructure involved in this incident.
- CertiNext Inc.: An indirectly wholly owned eMudhra subsidiary, through eMudhra Inc., that provides the CERTInext certificate lifecycle management platform used by InCommon.
- InCommon / Internet2: Provides certificate services to universities and research institutions through its relationship with CertiNext.
- SSL.com: An independent CA selected to provide replacement publicly trusted TLS certificate issuance through the CERTInext platform.

Historically, InCommon customers managed certificates through CERTInext, with issuance relying on eMudhra’s emSign certificate hierarchy.

On October 22, 2026, eMudhra announced its decision to exit the global publicly trusted SSL/TLS certificate business. However, the company continues to operate other PKI and digital trust businesses, including CertiNext.

During its November earnings call, management also indicated that its U.S. university federation customer would continue using CertiNext, with publicly trusted TLS certificates sourced from another provider.

This means that although eMudhra is withdrawing as a publicly trusted TLS issuer, its subsidiary remains involved in the delivery and management of certificate services.

Relevance to this incident

The original incident involved failures in CA key generation and associated verification controls. Given the documented relationships, I believe it is important to establish whether the affected procedures, systems, personnel, or security controls were shared with other CA operations.

Migrating certificate issuance to SSL.com may address the immediate browser-trust concerns, but it does not, by itself, demonstrate that all remaining certificate-management and issuance-related functions are operationally independent of eMudhra.

I would appreciate clarification on the following:

1. Shared infrastructure and controls: Have CertiNext and InCommon operations been assessed for dependencies on the HSMs, key-generation scripts, key-management procedures, personnel, or verification controls implicated in this incident? If so, what evidence supports the conclusion that these operations were unaffected?
2. Scope of the independent investigation: Does KPMG’s review include potentially shared infrastructure and operational controls associated with CertiNext and InCommon, or is it limited to the original key-generation ceremony and eight compromised intermediate CA keys?
3. SSL.com operational boundaries: Under the replacement arrangement, which functions remain under CertiNext or eMudhra’s control, and which are independently controlled by SSL.com? In particular, who is responsible for domain validation, issuance authorization, CA signing-key custody, and any delegated registration authority functions?
4. Continuing responsibilities: Following eMudhra’s exit from publicly trusted TLS issuance, which entities remain responsible for completing the outstanding incident investigation, maintaining required revocation services, and ensuring that remediation commitments are independently verified?
5. Scope of remediation: Will the final incident report explain how eMudhra determined that the original failures were isolated, including whether other CA hierarchies or services using potentially shared procedures and controls were evaluated?

To be clear, I am not suggesting that CertiNext or SSL.com has experienced a separate compromise. My concern is whether the investigation has sufficiently established the boundaries of the original failure and whether the associated remediation addresses all relevant operational dependencies.

Given eMudhra’s continued ownership of CertiNext and its decision to exit publicly trusted TLS issuance, I believe these questions are relevant to understanding the completeness of the incident investigation.

I appreciate everyone’s continued work on this matter and would welcome clarification from eMudhra or the appropriate representatives.

References:

eMudhra announcement (October 22, 2026):

[https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)

eMudhra earnings-call transcript:

[https://nsearchives.nseindia.com/corporate/EMUDHRA2008\_09112026195622\_Conferencecall\_Transcript\_\_1\_.pdf](https://nsearchives.nseindia.com/corporate/EMUDHRA2008_09112026195622_Conferencecall_Transcript__1_.pdf)

InCommon Certificate Service:

[https://incommon.org/certificates/](https://incommon.org/certificates/)

InCommon SSL.com transition updates:

[https://incommon.org/about/news/incommon-certificate-service-update](https://incommon.org/about/news/incommon-certificate-service-update)

## Full Incident Report

### Summary

**CA Owner CCADB unique ID:** A005678

**Incident description:** During a single key‑generation ceremony on 30 April 2025, sixteen subordinate (issuing) CA key pairs in eMudhra’s “B” and “C” series were generated correctly on a hardware security module and then processed through an approved wrap/unwrap round‑trip using a custom python key‑handling script. The script initiated the module to wrap the private key generated onboard into an encrypted blob in preparation for transport. For the eight **ECDSA P‑384** objects (G3B/G3C), a bug/defect in the import code resulted in a read‑back from the unwrapped object that truncated the private value, so the certified public keys correspond to private scalars below the expected range and are recoverable from public information. For the eight **RSA‑4096** objects (G2B/G2C), the private‑key integrity remained intact (all signatures verify against the certified public modulus), but the same host‑side read‑and‑re‑create pattern applied, meant that during re‑import, the RSA key material (handling RSA private key attributes e.g. CKA\_PRIVATE\_EXPONENT and CKA\_PRIME\_1) was handled within the volatile memory of a Python process on the ceremony host and eMudhra therefore cannot positively demonstrate that this key material was in compliance with CPS §6.2.6.

The purpose of import and export was to facilitate cross vendor migration between HSMs in different geolocations. This was the first and only time this process has been used by the PKI Operations team as all prior and subsequent key ceremonies have generated key pairs in place without a requirement to migrate.

A public incident page has been created at [https://emudhra.com/en/post/certificate-security-incident](https://emudhra.com/en/post/certificate-security-incident).

**Timeline summary:**

- **Non‑compliance start date:** 30 April 2025 (key‑generation ceremony).
- **Non‑compliance identified date:** 17 October 2026 (ECDSA G3B/G3C, third‑party report); early November 2026 (RSA G2B/G2C, CPS §6.2.6 assessment arising from root‑program discussion).
- **Non‑compliance end date:** 18 October 2026 for the eight ECDSA issuers revoked; 07 November 2026 for the eight RSA issuers (revoked with cessation of operation). Subscriber migration arising from the RSA G2C revocations is complete.

**Relevant policies:**

- TLS Baseline Requirements: §6.1.1.1 (CA Key Pair generation), §6.1.5 (key quality/size), §6.2.6 (Private key transfer into or from a Cryptographic Module), §4.9.1.2 (revocation timeline).
- eMudhra CPS (SSL/TLS) v1.08: §6.1.1, §6.2.1, §6.2.6.
- RFC 5280 (CRL reason codes).

**Source of incident disclosure:** Third Party Reported.

### Impact

**Total number of certificates:** 16 affected subordinate CA certificates issued by eMudhra roots (8 ECDSA G3B/G3C + 8 RSA G2B/G2C), plus 8 Sectigo (AAA Certificate Services) cross‑certificates of the ECDSA set, plus the end‑entity certificates issued by the RSA **G2C** TLS issuers that were in production from May 2026. The eight ECDSA issuers and the four RSA **G2B** issuers issued no end‑entity certificates. The end‑entity population issued by the four RSA G2C issuers is enumerated in the Appendix.

**Total number of “remaining valid” certificates:** The 16 subordinate CA certificates are revoked. The end‑entity certificates issued by the RSA G2C issuers (prior to their revocation) are listed in the Appendix and have been migrated/replaced.

**Affected certificate types:** DV, OV and EV TLS, and OV Code Signing (subordinate CA certificates). End‑entity certificates issued by the RSA G2C TLS issuers are DV/OV/EV TLS and OV Code Signing.

**Incident heuristic:**

- Subordinate CAs: the complete list of the 16 affected subordinate CA certificates and the 8 cross‑certificates is in the Appendix.
- End‑entity certificates: the affected set as confirmed per our CA database is reconstructable from Certificate Transparency by filtering unexpired certificates whose issuer is one of the RSA G2C TLS issuing CAs listed in the Appendix.

**Was issuance stopped in response to this incident, and why or why not?** Yes. eMudhra revoked the eight ECDSA issuers and ceased all issuance from intermediates chaining to the ECC G3 root. Following the CPS §6.2.6 assessment of the RSA key material, eMudhra revoked the eight RSA G2B/G2C issuers with cessation of operation and stopped issuance from them. eMudhra has additionally decided to exit the public TLS business. Remaining issuance from the emSign Root CA ‑ G1 hierarchy, which serves principally a university federation in North America, is being transitioned to another publicly trusted provider; all issuance from the G1 hierarchy will stop prior to 16 November 2026, (Action Item 1).

**Analysis:** All required revocations are complete at this time.

**Additional considerations:** The original on‑board key pairs were generated correctly; the hardware security modules functioned correctly throughout, and the devices are not at fault. The matters in this report arise from a host‑side key‑handling script and associated process controls.

### Timeline

All times UTC.

| **Date / time** | **Event** | 
|---|---|
| Nov 2024 – Apr 2025 | US and EU hosting and Sectigo cross‑certification approved (Nov 2024). US HSMs ordered (Apr 2025) and delayed by global supply‑chain constraints. Decision (mid‑Apr 2025) to generate the B/C keys on the HSMs available before the June 2025 root store policy changes and to transfer them by key wrapping. | 
| 30 Apr 2025 | Key‑generation ceremony: 16 subordinate CAs generated (B, C series; RSA‑4096 and ECDSA P‑384). The B/C series included an approved additional wrap/unwrap step executed with a key‑handling script written by the PKI Operations team. Ceremony witnessed by the compliance function. | 
| May 2025 | The 16 subordinate CA certificates disclosed in CCADB. Sectigo cross‑certificates received. | 
| May 2025 | “A” series replaced by “A‑1” series to adjust the component encoding field in the CN attribute. This key ceremony was performed on a separate HSM platform from the one involved in the incident and followed the standard KGC script. | 
| 29 May – 6 Jun 2025 | CRL‑signature anomaly for the G3B/G3C TLS intermediates ( [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728)), resolved at the time at the level of the signature mismatch. | 
| 14–15 Jul 2025 | Transfer of the eight C‑series keys to the destination facility using the destination vendor’s import tooling. The destination module’s PKCS#11 interface could not be used for the import, and a custom import process was put in place (see Contributing Factor 1). | 
| 2025–2026 | WebTrust audit cycles completed for the hierarchy. | 
| May 2026 | Issuance begins from the US issuing CAs. Of the affected objects, the ECDSA G3B/G3C issuers issued no end‑entity certificates; the RSA G2C TLS and CS issuers were placed in production and issued end‑entity certificates. | 
| 7 Oct 2026, 20:11:57 | Last end‑entity certificate issued by EM OV CS CA - G2C (code signing). | 
| 17 Oct 2026 | Third‑party report that the ECDSA G3B/G3C private keys are recoverable; corroborated by root programs; keys independently reproduced. eMudhra acknowledged the report the same day and notified the cross‑signing operator. | 
| 18 Oct 2026, 09:24–09:38 | All eight ECDSA G3B/G3C subordinate CA certificates revoked (reason: cACompromise); CRLs and OCSP updated. | 
| 19 Oct 2026 | Sectigo revoked its eight cross‑certificates of the ECDSA set. eMudhra ceased all issuance from intermediates chaining to the ECC G3 root. | 
| 27 Oct 2026, 19:14:35 | Last end‑entity certificate issued by EM DV TLS CA - G2C. | 
| 3 Nov 2026, 13:48:16 | Last end‑entity certificate issued by EM OV TLS CA - G2C. Issuance from the G2C issuers stopped. | 
| 7 Nov 2026 | Eight RSA G2B/G2C subordinate CA certificates revoked (reason: cessationOfOperation) and withdrawn from service; CRLs and OCSP updated; migration of affected G2C subscribers initiated. | 
| Oct – Nov 2026 | Subscriber migration underway; independent review commissioned; this report prepared. | 
| 16 Nov 2026, 23:59 (planned) | Hard stop for all issuance from the emSign Root CA ‑ G1 hierarchy; remaining issuance for the university federation moved to another publicly trusted provider. | 

### Related Incidents

| Bug | Date | Description | 
|---|---|---|
| 1970728 | 05 Jun 2025 | CRLs for the six G3B/G3C TLS intermediates signed with a key that did not match the public key in the corresponding CA certificate. Now understood to be an early indication of the key‑handling defect described in this report (see Root Cause Analysis, Contributing Factor 1). | 
| 1965559 | 09-May- 2025 | Disclosure of the 24 subordinate CAs generated in the 30 April 2025 ceremony (including the A series later replaced by A‑1). | 

### Root Cause Analysis

**Contributing Factor 1: Host‑side ceremony script error.**

- **Description:** Given that the script was a one off meant for export of key pairs, the approved wrap/unwrap deviation from the normal eMudhra KGC was executed with a custom python key‑handling script created by the PKI Operations team. After the wrapped key was returned, the script read the unwrapped private key’s value out of the module (in host side memory) and re‑created a key object from that host‑side value. For the ECDSA objects, a single line in that read‑back truncated the private value to its leading byte, so the re‑created object held a scalar below 256; this re‑created object (not the originally generated key) was used to produce the CSR and was certified. For the RSA objects, the same pattern did not truncate the key (integrity intact), but during re‑import the key material was handled within the volatile memory of the Python process on the ceremony host. A re‑import performed from host process memory is not consistent with the CPS §6.2.6 and the RSA objects are therefore treated as not meeting that requirement.
The devices themselves operated correctly; the defect was a script error in host‑side code. This was a custom script run only on an isolated ceremony host and was not a function of the emCA software. The wrap/unwrap step itself arose from the program circumstances of these keys. The B and C series keys were intended for operation from eMudhra’s US and EU facilities, but delivery of the HSMs ordered for the US facility was delayed by global supply‑chain constraints. It was also eMudhra’s intention to only operate HSMs within WebTrust certified environments and therefore the decision to generate this ceremony in eMudhra’s existing WebTrust datacenter and transfer to the new locations once they were certified. At the same time, root store program policy changes taking effect on 15 June 2025 (under which subordinate CAs in applicant hierarchies disclosed on or after that date must be dedicated to TLS server authentication), together with the requirement to complete cross‑certification with Sectigo before that date, meant that the keys had to be generated before the end of May 2025. eMudhra therefore generated the keys on the HSMs available at the time (Utimaco), with the intention of transferring them to the destination HSMs (Crypto4A) by key wrapping. Because moving keys between HSMs from different vendors is constrained, eMudhra was required to write a wrap/unwrap script to bridge moving the keys between the vendors. The source module was operated with FIPS‑approved mode disabled for the wrap/unwrap step, as an approved deviation recorded in the ceremony script; the 30 April 2025 round‑trip was a rehearsal of the planned transfer. For the July 2025 transfer, eMudhra had been informed that a PKCS#11 interface was available for the destination module; after the keys were exported, the PKI Operations team could not complete the import through that interface, and a custom import process had to be put in place. The defective read‑back code was not used in the July 2025 import; the C‑series keys moved in July were the objects that resulted from the existed 30 April 2025 ceremony.
- **Timeline:** Introduced and executed on 30 April 2025; ECDSA consequence first externally reported 17 October 2026; RSA (CPS §6.2.6) consequence assessed early November 2026 post Root Program Operators guidance.
- **Detection:** The ECDSA weakness was reported by a third party and reproduced by root programs. It went undetected earlier because the certified ECDSA keys still produce valid signatures, a valid public point on the curve, a CSR whose signature verifies, and certificates that lint cleanly; nothing in the ceremony tested CA key strength or compared the certified key to the originally generated key. The RSA confidentiality concern was identified through root‑program discussion of CPS §6.2.6. Because the re‑import step handled key material in volatile process memory on the ceremony host, later inspection of ceremony logs, system logs and file‑system artefacts cannot reliably establish or exclude how that material was handled during the step. eMudhra has therefore not relied on the absence of such artefacts and has treated the RSA key material as not meeting CPS §6.2.6.
- **Interaction with other factors:** Combined with Contributing Factors 2 and 3, the defect produced a certified weak ECDSA key that passed every check actually performed. Its relationship to the June 2025 CRL anomaly is Contributing Factor 4.
- **Root Cause Analysis methodology used:** Code review and controlled reproduction of the defect; HSM key‑object record review; “5 Whys.”

**Contributing Factor 2: No key‑strength verification step**

- **Description:** The ceremony did not test the strength of the CA private key, nor compare the certified public key against the key originally generated. Either check would have detected the weak ECDSA key and the use of the wrong object.
- **Timeline:** Gap present at the 30 April 2025 ceremony and in prior ceremonies.
- **Detection:** Identified during the current investigation. Not previously detected because these checks are not required by the Baseline Requirements for CA keys and were not part of eMudhra’s process. The affected CA certificates were disclosed in CCADB in May 2025, and the hierarchy was subject to the 2025 and 2026 WebTrust audit cycles. None of these steps includes, or is currently required to include, a test of CA private‑key strength or of the binding between the generated and the certified key (the Baseline Requirements currently do not mandate checking the key strength for CA keys under §6.1.1.1), and the affected certificates were in the public domain for approximately 18 months before the third‑party report.
- **Interaction with other factors:** This is the control that would have caught Contributing Factor 1 before certification.
- **Root Cause Analysis methodology used:** Control‑gap analysis against the ceremony procedure.

**Contributing Factor 3: Similar object labels**

- **Description:** The originally generated object and the re‑created object carried an almost identical label, allowing the re‑created (defective) object to be selected for CSR generation.
- **Timeline:** 30 April 2025 ceremony.
- **Detection:** Identified during the current investigation.
- **Interaction with other factors:** Enabled the wrong object to flow through to certification under Contributing Factor 1.
- **Root Cause Analysis methodology used:** Ceremony procedure and object‑attribute review.

**Contributing Factor 4: June 2025 anomaly resolved at the symptom level**

- **Description:** In June 2025 the CRLs for the G3B/G3C TLS intermediates did not verify because the certificates had been issued over the re‑created objects while the first CRLs were signed with the originally generated objects. This was resolved by re‑signing with the object that matched each certificate. There was no CPS basis for operating a secondary key handle as a matter of policy; the matter was addressed at the level of the signature mismatch and did not reach the underlying cause.
- **Timeline:** 29 May – 6 June 2025 ([Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728)).
- **Detection:** Re‑examined in the current investigation; the earlier resolution did not identify the duplicate objects or the ceremony deviation as the underlying cause.
- **Interaction with other factors:** An earlier opportunity to detect Contributing Factor 1.
- **Root Cause Analysis methodology used:** Review of the [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) record against current findings.

### Lessons Learned

**What went well** - The third‑party report was acknowledged the same day, and the eight ECDSA issuers were revoked within approximately 15 hours — well within the BR §4.9.1.2 timeline. - The eight ECDSA issuers and the RSA G2B issuers had issued no end‑entity certificates. - The cross‑signing operator revoked its cross‑certificates promptly. - HSM key‑object records allowed the originally generated objects to be distinguished from the re‑created objects, confirming the defect was in host‑side code and that the devices are not at fault.

**What didn’t go well** – A host‑side key‑handling script error resulted in truncated private key values that were used for producing a weak certified ECDSA key and a CPS §6.2.6 exposure concern for the RSA keys. (Action Items 2, 3.) - The ceremony had no key‑strength verification step. (Action Item 2.) - Almost identical object labels allowed the wrong object to be selected. (Action Items 2, 3.) - The June 2025 anomaly was resolved at the symptom level without reaching the underlying cause. (Action Item 2.).

Potential impact to relying parties that did not enforce revocation checks at Issuing CA level (we have no known case of misuse) as library updates were pushed by relying parties quickly. Non-availability of CRL for certain User-Agent headers (refer [https://bugzilla.mozilla.org/show\_bug.cgi?id=2085612](https://bugzilla.mozilla.org/show_bug.cgi?id=2085612))

**Where we got lucky** - The ECDSA weakness was identified and reported before it was used against any eMudhra‑issued end‑entity certificate. This cannot be relied upon. (Action Items 1.) - The RSA key integrity was intact, so the CPS §6.2.6 matter did not also involve recoverable keys. (Action Items 3.)

**Additional (Other)** - Key movement between HSMs of different vendors created a need to develop a custom script outside the vendors module’s native mechanisms. (Action Items 1, 2.) -

### Action Items

As eMudhra is exiting the public TLS business, the remaining action items are limited to completing that exit in an orderly way.

| Action Item | Kind | Corresponding Root Cause(s) | Evaluation Criteria | Due Date | Status | 
|---|---|---|---|---|---|
| 1. Complete the transition of the remaining subscriber population: the principal affected customer, a university federation in North America, has an alternate issuance path with another publicly trusted provider under the existing contractual framework, and issuance for that community is being moved to that provider. Hard stop for all issuance from the emSign Root CA ‑ G1 hierarchy prior to 16 November 2026. | Mitigate | CF1 | No issuance from the G1 hierarchy after the hard stop (verifiable in Certificate Transparency). | 16 Nov 2026 | Ongoing | 
| 2. Put in place improvements motivated by findings of independent review to strengthen our general PKI operations around key strength tests, key attestation evidence, additional maker/checker controls particularly for Root/Issuing CA KGC, CRL verification | Detect | CF1, CF2, CF3, CF4 | Independent review completed. | 04-Dec-2026 | Ongoing | 
| 3. Complete a lifecycle inventory of all CA keys, along with expiry dates of EE certificates to plan for CRL/OCSP obligations | Mitigate | CF1, CF3 | Completed inventory | 30-Nov-2026 | Ongoing | 

### Appendix

**A. Affected subordinate CA certificates — ECDSA P‑384 (G3B/G3C), revoked 18 Oct 2026 (reason: caCompromise)**

| # | Subordinate CA | Issuer | Serial | SHA‑256 | 
|---|---|---|---|---|
| 1 | EM DV TLS CA ‑ G3B | emSign Root TLS CA ‑ G3 | a4aee678f23362b4c0e460b772f214 | 42C4ACCD12C4F59597925E1A08A7A90102608543809308D50EC427E118BA1493 | 
| 2 | EM DV TLS CA ‑ G3C | emSign Root TLS CA ‑ G3 | 588b2e3c2bb8cda13e1a1209254321 | 0164D7CEAE5BB909C272AF151FF44B1177AE9B47D9424B94F1D9558C30934D19 | 
| 3 | EM EV TLS CA ‑ G3B | emSign Root TLS CA ‑ G3 | c7c41efe92d825f05eae841a4a82c1 | E7568FE6E12331F4FD7DE61DA4C7559D0F8EB192A218D4741A3BA75184333838 | 
| 4 | EM EV TLS CA ‑ G3C | emSign Root TLS CA ‑ G3 | 8009928a64107601af05fa2f19f109 | 432EC25F0D28DE9006D97BF752F17BBB2CD41F669933FCB072D9A1148D0261F3 | 
| 5 | EM OV TLS CA ‑ G3B | emSign Root TLS CA ‑ G3 | 6cada367fb1c100088120ea202d568 | 98B896625C0C230ADEEC3EB2CF6AAD5001ECF9156A68644E82374CE5833BC25B | 
| 6 | EM OV TLS CA ‑ G3C | emSign Root TLS CA ‑ G3 | 296926c227a3a1526392b19482a504 | CB6E15165AC802E9B3F993F16C25D41F4E81C21EBDE71AE1B012AC00BF9C7C3F | 
| 7 | EM OV CS CA ‑ G3B | emSign Root CS CA ‑ G3 | 7818933f8f85b4619a2b35fba83d0a | 9E39DE2881273ACC225A149C72BA3E0F51424963669AB633EE1DC7DF5DB067B4 | 
| 8 | EM OV CS CA ‑ G3C | emSign Root CS CA ‑ G3 | 544b7f922c31ae220a4a922916f6e6 | 4B2460A466F95FD40113BCDCCA2CEB29B3B093921DE45474DA7DF48874C630B1 | 

**B. Sectigo (AAA Certificate Services) cross‑certificates of the ECDSA set, revoked 19 Oct 2026**

| # | Subordinate CA | Serial | SHA‑256 | 
|---|---|---|---|
| 1 | EM DV TLS CA ‑ G3B | a024fdf4ba665c785ce4a020483858b7 | 45A883F349AEDFD5F3A649B5498FFB121712BA8B448F3F2A91DBC5A766FCDDBE | 
| 2 | EM DV TLS CA ‑ G3C | 91f347f1a5b7d39962b95e0ee4e299d1 | 62B7F9868263F72F6911FC78CEAF72C1979158B7368BF648683BB2AA39B02E72 | 
| 3 | EM OV TLS CA ‑ G3B | e94223bde92f914e5ab9acabfdac3710 | 5F1DED4DD590AF74631290CF073B122A2AAC6A1FA479778A0BD43579BD832699 | 
| 4 | EM OV TLS CA ‑ G3C | 8d5a4811939ef447d77111cdd9849ae9 | 7485B51C0ED192878FA1D2F948FB529AE1842CC5086C4B67F7BE5B2039DE9489 | 
| 5 | EM EV TLS CA ‑ G3B | d8f8685e4f2bd9d82402a85a1c1eb731 | 579480AEA166290BD3C643589E795FC0D0E54E86505D180F1DFF99EFD3199512 | 
| 6 | EM EV TLS CA ‑ G3C | 05f078752dece7a1bb8595d303167171 | FD9D5C2DBBD4995AB69B8D50C439D9527B00529199C2FD01B2174EB58F07021F | 
| 7 | EM OV CS CA ‑ G3B | 41e32b73ac185d6ce0d7480bacf84e69 | A496E23AC0CAB8155FC9B117B97EAE368EFCBB9041AEC8804D5A308D2D01C2D8 | 
| 8 | EM OV CS CA ‑ G3C | d6a5ef613b390f32ef9cdf349f772841 | 84112972B8E59D14560AE7E7119654474AAD119990CF3722BFC1E3B91615E1FD | 

**C. Affected subordinate CA certificates — RSA‑4096 (G2B/G2C), revoked with cessation of operation on 07 November 2026**

| **#** | **Subordinate CA** | **Issuer** | **Serial** | **SHA-256** | 
|---|---|---|---|---|
| 1 | EM DV TLS CA - G2B | emSign Root TLS CA - G1 | F0A030825E22BB2E1D88E3889DC073 | 829EC444B8BE3DFD2D030A0D9E7A1D0DD2A3C2C325D39589C27AC9A065BAE793 | 
| 2 | EM DV TLS CA - G2C | emSign Root TLS CA - G1 | AB5DEA38BDC920D5FA4736DA54BEBE | 0427EA3CB4A7B4CB205E77A7B166D332BEDB8E8EF469BC5E883169C8D0AC876D | 
| 3 | EM OV TLS CA - G2B | emSign Root TLS CA - G1 | C164DB9804F563241ED32C4100A566 | 6A7A93861982B664001710A0EFD04C8A72F6A23E252B280911797E0BF1BD9012 | 
| 4 | EM OV TLS CA - G2C | emSign Root TLS CA - G1 | CBDCFA0D64112709CF14B7E4858250 | DE767792E870BD32F331029FC89DC24C53F9DF970DC70F1EA30CF29DB3F94BA9 | 
| 5 | EM EV TLS CA - G2B | emSign Root TLS CA - G1 | 8F06A3F1D6A2FC71D29393C71CD48E | E072B30D7F5B8BCF0080E51D6CC7765767072DB2319E9BB1CD3D02A086898750 | 
| 6 | EM EV TLS CA - G2C | emSign Root TLS CA - G1 | B28103309375C0CBB9E9B80B66C430 | C3BC2B480FB1A1AB4D0BA1ED6C7B53E096447045733620991A32D6798D77AA20 | 
| 7 | EM OV CS CA - G2B | emSign Root CS CA - G2 | 33E8C5A8046D443E8FA5F1AF733188 | 913F1A04B02814B604AC5275ACB201B1C802B2C0F1B4986FB1A1EB595958E072 | 
| 8 | EM OV CS CA - G2C | emSign Root CS CA - G2 | 7F7C7D863DC9B3541E9D0C4B91237E | EBAC91B8EC9853323779EDB393C595FADB29DD4DDB20C47E336F2A021684F27B | 

**D. End‑entity certificates issued by the RSA G2C TLS issuers**

See attached file

**E. Not affected** - The A and A‑1 series: generated on a different HSM platform for domestic deployment; did not go through the wrap/unwrap or cross‑HSM transfer path; their private keys have not been recoverable.

Thank you very much for this (belated) incident report. Will eMudhra be sharing the relevant Python source code that caused this incident?

Thank you, Naveen, for publishing the full incident report and providing a detailed explanation of the root cause, affected key material, and corrective actions.

The report provides important clarification, particularly regarding the host-side key-handling defect, the additional RSA key-handling noncompliance, and the acknowledgment that the June 2025 CRL-signing incident was an early indication of the underlying problem.

I appreciate the additional transparency. I have several follow-up questions that I believe are relevant to establishing the complete scope of the incident and the effectiveness of remediation.

1. RSA private-key confidentiality and revocation rationale

The report acknowledges that the eight RSA-4096 private keys were reconstructed using private-key components held in the volatile memory of a Python process, outside the intended cryptographic-module boundary.

It also states that historical evidence cannot reliably establish or exclude how that material was handled during execution.

Could eMudhra clarify:

- What controls protected private-key material while resident in host memory, including process isolation, privileged access, debugging, memory dumps, and other potential exposure paths?
- What evidence supports the conclusion that RSA key integrity was preserved, and what independent assessment has been performed regarding confidentiality?
- What was the technical and policy rationale for revoking these intermediates using cessationOfOperation rather than keyCompromise, given the inability to demonstrate compliant private-key handling?

I recognize that noncompliant handling does not necessarily establish actual compromise. However, the distinction between demonstrated key integrity and unverified key confidentiality appears important to the incident assessment.

1. June 2025 CRL incident and missed root-cause identification

The report explicitly acknowledges that [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) was resolved at the signature-mismatch level without identifying the duplicate key objects or the underlying ceremony defect.

This appears to have been a significant missed opportunity to identify the problem approximately 16 months earlier.

Could eMudhra explain:

- Why the discovery of mismatched signing keys did not trigger a reconciliation of the original and re-created HSM key objects?
- Whether the April 30 ceremony records, key-object identifiers, and associated public keys were examined during the June 2025 investigation.
- Whether the independent auditors were informed of the key mismatch and the existence of multiple key objects.
- What changes have been made to ensure that future cryptographic anomalies trigger investigation of the underlying key provenance rather than resolution of the immediate symptom alone?

1. Independent review and reproducibility

Action Item 2 identifies December 4, 2026, as the milestone for completing the independent review.

Could eMudhra confirm whether KPMG’s investigation includes:

- Independent reproduction of the ECDSA private-scalar truncation using the actual executed script version.
- Examination of the RSA private-key handling and potential confidentiality exposure.
- Reconciliation of the original and re-created HSM key objects.
- Review of the June 2025 investigation and its missed detection opportunity.
- Independent verification that the defect was confined to the identified B/C-series objects and did not affect other key-generation procedures.

Will the findings, methodology, and evidence supporting these conclusions be published, either in the independent report or in a sufficiently detailed public technical summary?

1. Scope of remediation across continuing PKI operations

The report explains that eMudhra’s remaining action items are limited in light of its withdrawal from publicly trusted TLS issuance.

However, eMudhra continues to operate other PKI and digital trust services, including its CertiNext business.

Could eMudhra clarify whether the identified control deficiencies, particularly the absence of key-strength verification, inadequate key-object differentiation, host-side private-key handling, and insufficient root-cause investigation, have been assessed across its continuing PKI operations?

Where the same or similar procedures are used elsewhere, will the resulting corrective actions be independently verified?

I am not suggesting that CertiNext or other services have experienced a separate compromise. The question concerns whether the investigation has established the boundaries of the affected controls and whether remediation addresses any shared dependencies.

1. Continuing certificate-status obligations

Following the revocation of the affected ECDSA and RSA intermediates and the planned cessation of G1 issuance, could eMudhra clarify how the continued availability and integrity of CRL and OCSP services will be maintained for the remaining relevant certificate populations?

Will the November 30 lifecycle inventory identify the responsible operators, applicable retention and publication periods, and verification controls for these services?

Closing observation

The report establishes that the original HSM-generated keys were not inherently defective, but that subsequent host-side processing, key-object selection, and missing verification controls allowed critically weak keys to be certified.

It also establishes that an earlier incident exposed a symptom of the defect without identifying its underlying cause.

These findings make independent verification of the complete key-handling process and corrective actions particularly important.

I appreciate eMudhra’s decision to disclose these details and address the expanded RSA scope. Clarification on the remaining questions would help the WebPKI community distinguish completed containment from independently demonstrated remediation and assess whether the underlying control deficiencies have been comprehensively addressed.

Thank you for your continued engagement.

eMudhra: on [comment 82](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82).

1. Please publish the key-handling script(s) used in the ceremony on 2025-04-30 and the July 2025 transfer, with the ceremony and HSM logs, showing which script version was used for each key and any changes or re tries during the ceremony.
2. What approval process authorised disabling FIPS-approved mode and exporting the plaintext private keys to host memory and was this disclosed to the Qualified Auditor?
3. Which other key objects were on those HSMs while FIPS-approved mode was disabled?
4. eMudhra knew of the plain text export from 30 April 2025. Why was it not disclosed until Nov 2026 and why were the G2C issuers put in to prod in 05/2026?
5. How was the ceremony host prepared, and what happened to it afterwards? Please state its provenance, operating system, how Python and all libraries were installed and verified (including whether any were downloaded from the internet), and the hardening applied. Was it ever connected to any network before or after 30 April 2025? Was its storage (including swap and any removable media) destroyed, and if so when, by which role, and with what destruction record? If it still exists, has it been preserved for the independent review?
6. How were the script, the CSRs and the wrapped key blobs moved onto and off the ceremony host, and how was the wrapping key delivered to the destination facility in July 2025? Please identify the media used, how it was sanitized and checked for malware before use, its chain of custody, and what happened to it afterwards.

Well the incident report raises more questions than it answers, and raises concerns over prior inaccurate statements. I'll try to keep the core issues as we'd be here all day otherwise. The crux of this issue is key material being mishandled by eMudhra. I do not see evidence that they have learned from this ongoing operational error, and that it would somehow be limited to only the documented instances in this thread.

30 Apr 2025: Key‑generation ceremony: 16 subordinate CAs generated (B, C series; RSA‑4096 and ECDSA P‑384). The B/C series included an approved additional wrap/unwrap step executed with a key‑handling script written by the PKI Operations team. Ceremony witnessed by the compliance function.


Can you explain what "the compliance function" is? There's a strange lack of mention of a qualified auditor.

eMudhra therefore generated the keys on the HSMs available at the time (Utimaco), with the intention of transferring them to the destination HSMs (Crypto4A) by key wrapping. Because moving keys between HSMs from different vendors is constrained, eMudhra was required to write a wrap/unwrap script to bridge moving the keys between the vendors.


Did it ever cross eMudhra's mind that moving private keys between HSMs vendors is constrained for a reason?

The source module was operated with FIPS‑approved mode disabled for the wrap/unwrap step, as an approved deviation recorded in the ceremony script; the 30 April 2025 round‑trip was a rehearsal of the planned transfer.


BR 6.1.1.1 (5) requires "effective controls to provide reasonable assurance that the Private Key was generated and protected".

Was there ever any specific documented step that FIPS-approved mode was explicitly disabled, and did auditors have that document for WebTrust auditing purposes?

For the July 2025 transfer, eMudhra had been informed that a PKCS#11 interface was available for the destination module; after the keys were exported, the PKI Operations team could not complete the import through that interface, and a custom import process had to be put in place. The defective read‑back code was not used in the July 2025 import; the C‑series keys moved in July were the objects that resulted from the existed 30 April 2025 ceremony.


Can we get more details on this "custom import process" made for yet another key generation ceremony that requires impromptu scripts? That *that* defective read-back code wasn't used in the July 2025 import does not preclude that more defective code wasn't similarly used.

At the same time, root store program policy changes taking effect on 15 June 2025 (under which subordinate CAs in applicant hierarchies disclosed on or after that date must be dedicated to TLS server authentication), together with the requirement to complete cross‑certification with Sectigo before that date, meant that the keys had to be generated before the end of May 2025.


If a CA is going to intentionally rush their processes to try to bypass cut-off dates that bring in higher security standards then we need to re-assess how those dates are applied.

[Comment 62](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c62)'s attachment claims in a response to Google:

We recognize that the CRL issue warranted its own report regardless of the concurrent incident, and we will plan file a separate preliminary incident report on 29th Oct 2026, cross-referenced to this bug and to [Bug 2080742](https://bugzilla.mozilla.org/show_bug.cgi?id=2080742).


There's still no incident report raised regarding the 2026-10-14 CRL signing issues.

[Comment 19](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c19) posted on 2026-10-20 14:16 UTC:

Acknowledging this message, we will cease issuance from all intermediates chaining up to G3 (our ECC root) immediately.


The affected certificates attachment shows issuance through to 11-03...

Speaking of the affected certificates, the notBefore dates are interesting as they begin 2026-04-09 - you stated that production usage started in May 2026?

What is the scope, reviewer and publication plan of the independent review?

What did the promised re-verification of every key ceremony find?

Now a question for Sectigo:

| Date / time | Event | 
|---|---|
| 17 Oct 2026 | Third‑party report that the ECDSA G3B/G3C private keys are recoverable; corroborated by root programs; keys independently reproduced. eMudhra acknowledged the report the same day and notified the cross‑signing operator. | 
| 18 Oct 2026, 09:24–09:38 | All eight ECDSA G3B/G3C subordinate CA certificates revoked (reason: cACompromise); CRLs and OCSP updated. | 
| 19 Oct 2026 | Sectigo revoked its eight cross‑certificates of the ECDSA set. eMudhra ceased all issuance from intermediates chaining to the ECC G3 root. | 

eMudhra are now alleging it took more than 24 hours for Sectigo to act after being made aware of the keyCompromise.

Sectigo: Does this timeline fit your awareness of the situation and who contacted you originally? I surmise it would be Apple going by their focus at the time.

Also for the record I was advocating for not immediately revoking, so as to not draw attention while a containment plan was put together. There are security scenarios where the CCADB Reporting Guidelines and Baseline Requirements are weighed against the potential harm, and it would be worth documenting fire drills and more explicit exemptions in the future.

I have read this incident report, and have some serious concerns with what it reveals.

1: What were the reasons this export, wrap, and unwrap process was preferred over generating new subordinates once the datacenter was certified and signing and disclosing them? The burdens do not seem that high here, and clarity would help understand unintended effects of improvements to the WebPKI. Ultimately of course these subordinates were disclosed, hence how the bug was found in the first place.

2: Section 6.2.7 of the BRs seems directly contradicted by any process involving a host touching the private key and not the HSM, but this isn't listed as one of the sections violated. Why not?

3: The Lessons Learned section seems erroneous. The existence or nonexistence of end-entity certificates issued from this intermediate is irrelevant to the exposure, easily the most catastrophic incident since Flame for the WebPKI.

4: What testing did the approved key ceremony at issue undergo before being run in production?

(Longtime reader, first-time commenter, please forgive me if the structure of this comment is off.)

eMudhra: Thank you for sharing this detailed report and voluntarily disclosing the additional issues with the RSA portion of the ceremony.

I agree with Watson's points and am similarly concerned by the fact that anyone thought it was a good idea to run a key ceremony where anything other than the HSM had direct access to the generated private keys. This seems like such an obviously bad idea that I am astonished that it was even entertained.

I am curious and have 3 questions about this portion of your report:

For the July 2025 transfer, eMudhra had been informed that a PKCS#11 interface was available for the destination module; after the keys were exported, the PKI Operations team could not complete the import through that interface, and a custom import process had to be put in place.


1. What issues were experienced with the PKCS#11 interface?
2. Were there any attempts made to address those issues?
3. How was the security of the custom import process assessed prior to execution?

I will also join the list of people who would like to see the code that was used for the ceremony that led to the generation of the insecure ECC keys, and I would additionally ask if the code responsible for this "custom import process" can be made available.

I think a more important question here is why the keys were extractable at all. Were they created with CKA\_EXTRACTABLE (in which case I think a very urgent question, and one eMudhra has not answered, is whether any of their other keys, anywhere at all, are extractable!) or does the Utimaco HSM make it possible to turn a non-extractable key into an extractable key, perhaps through some private interface?

No version of eMudhra's CPS that I can find contains the typical boilerplate language about non-exportability. They appear to make no non-exportability claim whatsoever.

It seems to me the only safe assumptions are that all of their keys are exportable and that any of their keys which are present on more than one HSM have probably been handled as plaintext on management hosts.

At this point I would argue that all CAs in the browser root trust bundles should be urgently required to attest that their keys are in fact non-exportable.

Follow up questions in response to [Comment #82](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82)

1. It's stated that for the eight ECDSA P-384 keys, the Python script "truncated the private value to its leading byte" and that the originally generated 384-bit key objects remain distinguishable on the Utimaco HSM, and that six of those originally generated objects signed the initial May/June 2025 CRLs in [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728).
Because those eight originally generated key objects were never certified in any CA certificate and are defunct:

Will eMudhra publish the 8 public keys of those originally generated HSM objects so the community can independently verify that they validate the May/June 2025 CRL signatures from [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728)?

Will eMudhra provide the 8 defunct 48-byte original scalars to deterministically verify that the leading byte (d\_orig\[0\]) of each 48-byte key equals the exact certified scalar (0x04, 0x38, 0x42, 0x73, 0x9b, 0x9c, 0xe6, 0xed)?


1. Under this sequence stated in CF1, the encrypted blobs wrapped from the onboard keys on 30 April 2025 contained the uncorrupted 48-byte ECDSA keys, not the truncated 1-byte keys created in the subsequent read-back step. Yet the report states that on 14–15 July 2025, "the C-series keys moved in July were the objects that resulted from the existed 30 April 2025 ceremony" (the re-created objects matching the certificates) and that "the defective read-back code was not used in the July 2025 import."

- If the encrypted blobs generated on 30 April 2025 wrapped the originally generated keys, how were the re-created objects exported for the 14–15 July 2025 transfer to the Crypto4A HSMs?
- Was a second, undisclosed wrapping/extraction operation performed on the Utimaco HSM after 30 April 2025 (and after the 6 June 2025 [Bug 1970728](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728) CRL resolution) to extract the re-created objects for the July transfer?
- What happened to the eight B-series (EU) keys, which are omitted from the July 2025 transfer timeline?


1. How did "almost identical" (i.e., distinct) object labels cause the CSR generation step to deterministically select the re-created object 16 out of 16 times on 30 April 2025, while the initial CRL configuration in May 2025 deterministically selected the originally generated object 6 out of 6 times for the G3B/G3C TLS intermediates? Why did the two ECDSA Code Signing intermediates (EM OV CS CA - G3B and G3C), which suffered the exact same 1-byte truncation on 30 April 2025, not experience the CRL signature mismatch in May/June 2025 alongside the six G3B/G3C TLS intermediates?
2. Modifying the ASN.1 string encoding of a Subject CN attribute only requires re-issuing a new certificate over the existing Subordinate CA public key. Why did fixing a Subject CN attribute encoding require abandoning the 30 April 2025 Series A key pairs and generating new keys on a different HSM platform (Entrust nShield) on 29 May 2025?

eMudhra stated that all 24 subordinate CAs (Series A, B, and C) were generated in the 30 April 2025 ceremony. Does eMudhra now claim the original Series A keys were not generated on the Utimaco HSMs during the 30 April 2025 ceremony?

The Timeline summary lists the non-compliance identification date for the eight RSA G2B/G2C intermediates merely as "early November 2026" without a date or timestamp. On 2 November 2026, eMudhra disavowed its prior statements regarding which script pathways each set of keys went through and requested a delay until 9 November 2026 citing the appointment of KPMG. However, the Timeline reveals that EM OV TLS CA - G2C continued issuing end-entity certificates until 3 Nov 2026, 13:48:16 UTC, and the G2B/G2C intermediates were not revoked until 7 November 2026—after subscriber migration was completed—while the independent review itself has now been deferred to 4 December 2026 (post-dating the 16 November 2026 G1 exit).

- What is the exact UTC timestamp at which eMudhra first identified that the RSA G2B/G2C keys underwent the host-side read-and-recreate step?
- Why did eMudhra continue issuing production end-entity certificates from EM OV TLS CA - G2C on 3 November 2026 after disavowing the RSA script-pathway claims on 2 November 2026?
- Why was KPMG cited on 2 November 2026 to delay the submission of this internal report to 9 November 2026, when the independent review will not be completed until 4 December 2026?


I have been, in some consternation, reading such public documentation as is available on the HSM actually in use, and the eMudhra CPS, and their recent report, against one another, and now I am actually more concerned.

It appears that the most likely operation used in the disclosed HSM-vendor-migration project would have been the "backup" operation. In non-FIPS mode, this includes even "non-exportable" keys. Further, backups are encrypted to a Master Backup Key. The Master Backup Key can be exported from the HSM as secret share files; the shares are NOT required to be stored in a smart card or other HSM (which is probably why FIPS mode does not allow backup of non-exportable keys).

This means that one likely path to a vendor migration would be to extract the MBK secret shares, reverse engineer their format and combine them, perform a backup, decrypt it, reverse-engineer a little more (much easier in these LLM-equipped days), and use a "custom Python script" to parse out each key and load it via PKCS#11 into one's new HSM. This would give the very real possibility of damaging a key if, let's say, one got the reverse engineering wrong.

Unfortunately - I won't name names - I have now looked at some other CAs' CPS language and it does not appear to be tight enough to forbid this kind of export-via-backuo of "non-exportable" keys.

Mr. Thor Simon,

I think a more important question here is why the keys were extractable at all. Were they created with CKA\_EXTRACTABLE (in which case I think a very urgent question, and one eMudhra has not answered, is whether any of their other keys, anywhere at all, are extractable!) or does the Utimaco HSM make it possible to turn a non-extractable key into an extractable key, perhaps through some private interface?


Generating the RootKeys outside the HSM and then importing them into the HSM is a widely adopted practice.

In fact, it is even more common among CAs to generate the private keys on an external machine (typically a freshly OS installed, air-gapped computer), and subsequently import the private keys into three or more HSMs and stored them in separate safe-containers.

This is a deliberate compromise to mitigate the catastrophic risk caused by failure of the HSM secure chip.

Consider this scenario: if a CA generates the private key entirely inside the HSM, and this key serves tens of thousands of customers, then one day the HSM secure chip malfunctions and the key becomes corrupted — this would be devastating for the CA.

(In reply to CitadelCore Cyber Security Team from [comment #93](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c93))

Mr. Thor Simon,

I think a more important question here is why the keys were extractable at all. Were they created with CKA\_EXTRACTABLE (in which case I think a very urgent question, and one eMudhra has not answered, is whether any of their other keys, anywhere at all, are extractable!) or does the Utimaco HSM make it possible to turn a non-extractable key into an extractable key, perhaps through some private interface?

Generating the RootKeys outside the HSM and then importing them into the HSM is a widely adopted practice.

In fact, it is even more common among CAs to generate the private keys on an external machine (typically a freshly OS installed, air-gapped computer), and subsequently import the private keys into three or more HSMs and stored them in separate safe-containers.


What you describe is indeed common practice but it does not require the keys to be extractable.  Loading keys *from* outside the HSM and extracting them *to* outside the HSM are, obviously, not the same operation.  Keys can be generated outside, placed in a bank vault and zeroized appropriately from anywhere else they were handled, and marked non-exportable in the target HSM.  Of course, a CA that had operated in this (in my opinion responsible) way would not then need to extract any keys from its brand A HSM to load them into its brand B HSM!  It could just go to the vault and get the keys.  So certainly there is no need for exporting "non-exportable" keys for safe HSM operation by CAs.

However, I should note that the specific HSMs in use here seem to have some major problems in this area. It appears from Utimaco's documentation and from its FIPS and CC documentation that:

A) even in FIPS mode, keys marked non-exportable will be included in backups unless also marked deny-backup;

B) The vendor's PKCS#11 module does not set deny-backup when setting CKA\_EXTRACTABLE false;

C) When not in FIPS mode, a low-level backup operation using the vendor proprietary API will actually create a backup that includes even keys that *are* marked deny-backup (!!)

D) For some models of this vendor's HSMs, changing from FIPS to non-FIPS mode may create an audit record but *not zeroize the key store*.

In other words, even if these keys were marked both non-exportable and deny-backup, and even if the module was in FIPS mode when they were generated or loaded, a combination of cleverly or ineptly written and validated policy and code may have allowed them to be exported nonetheless.

Keys can be transferred from one HSM to another HSM of the same vendor "wrapped".

It's an absolute necessity, otherwise a hardedefect of a HSM would destroy your private key. CA is out of business.

On HSM1 a wrapping key is created, the keymaterial is encrypted with that wrapping key, the wrapped backup can be transfered to HSM2.

Why is this secure?

The wrapping key is split into "m" parts where at least "n" must be available to stitch the key together.

So the whole process needs "n" people to collaborate.

If these n people would have reverse engineered the "wrapping" algorithm they could do that also outside of a HSM. That would be intentional wroing doing.

There is never the need to create a key outside of a HSM for backuping and shouldn't be done!

Wayne,

eMudhra are now alleging it took more than 24 hours for Sectigo to act after being made aware of the keyCompromise.

Sectigo: Does this timeline fit your awareness of the situation and who contacted you originally?


We received an email from our contact at eMudhra at 21:03 UTC on October 17th, outlining the details. This email was sent to two Sectigo employees, with one of our distribution lists on CC, which had two additional employees in its distribution chain. To note, this was not sent to our CPR address. We believe the contacts used by eMudhra for this were appropriate. All contacts on this email, are EU-based.

We acknowledged receipt on October 18th at 07:10 UTC, after which we started evaluating what was needed. All our offline signings require approval from our Policy Authority, which was requested at 13:28 UTC the same day, with approvals received by 17:03 UTC.

In [comment #6](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c6) of this bug (16:08 UTC) , we acknowledged being aware of this incident, and stated we were preparing the offline revocation of these CAs, stating this was expected to be completed within 24 hours from that moment. We also sent private notifications to Apple, Chrome, Mozilla and Microsoft the same day.

To answer your question specifically, we started acting the moment the email was reviewed (within roughly 12 hours of receipt). Revocation was completed after more than 24 hours (but less than 48). We will note, there are no requirements for Sub CA revocations within 24 hours. We posted [comment #6](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c6) originally to provide the community with to keep the community and root store operators apprised of our progress, and expected timelines.

We will further add that the Root CA in question had been removed from both Chrome and NSS over a year ago.

@#93:

for root keys, sure, as they are very long living and require considerable effort to issue and get rid of from everywhere, however this is about intermediate keys, what would have stopped emudhra from just making new keys and certs on those new HSMs rather than ex- and importing them via a script, disabling certified modes (be it FIPS or otherwise) and all that when it would have been so easy to just make fresh intermediates at the new place where the new HSMs that were to be added arrived? if an HSM gets decommissioned it might be more useful to revoke the key anyway after certificates have run out.

@#94:

if it is possible to export keys both marked non-extractable AND deny backup, that sounds like real fun and in my opinion definitely puts more pressure onto making sure that root keys are well protected. considering that new intermediates arent issued several times a year but rather usually once every several years, with even Let's Enrcypt having 3 year runtimes on their recent intermediates, generally all operations from a Root Key should be enacted with similar security as the DNSSec Root Ceremony (which for comparison happens 4 times a year) and the only copy they have outside the HSM that I have read about are the RKSH Smartcards (a set of 7 which you need 5 of to get the key out) and for intermediates considering the annoyance of revocation as seen in this case, and the ease of issuance, it should not be a problem that a "backup" would not be a copy of the key outside the HSM in whatever way but just a second HSM with its own key and certificate signed by the root.

@#95:

sure the wrapped export makes sense for root keys or thing that are similarly "fixed" as those, however this was about intermediates, and eMudhra wanted to move cross-vendor.

Additionally, I would assume that the HSM company would additionally to the "exposed" key shares of that wrapping key via smartcards or otherwise, the HSM would put a Vendor key alongside in there which is mandatory for the unwrapping to succeed, as otherwise a "This key was generated here and it cannot exist outside of our HSMs" attestation would be effectively void.

[log in](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449&GoAheadAndLogIn=1)before you can comment on or make changes to this bug.

## Description

•
