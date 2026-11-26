---
title: SEPPmail IME with the exclusive utilisation of the GINA technology
author: SEPPmail GmbH
url: https://www.seppmail.com/03_wp_05_af_03_ime_02_seppmail-ime-using-only-gina.html
hostname: seppmail.com
description: This version is exclusively based on the GINA technology, whereby the sender already registers at the GINA portal for sending the email.
sitename: seppmail.com
date: "2023-01-01"
fingerprint: "6edf3d993968be1d"
language: de
filedate: "2026-11-26"
---
This version is exclusively based on the GINA technology, whereby the sender already registers at the GINA portal for sending the email.


1.At the email client (1), an SSL connection (2) to the GINA portal of the SEPPmail Secure E-Mail Gateway (3) is established.


2.Once logged on to the GINA portal, an email is directly addressed and sent to internal (and, if applicable, external) users in the web mailer.


3.The SEPPmail Secure E-Mail Gateway forwards the thus created, known GINA emails (5) to the internal email server (6) as well as to the Internet for any possibly addressed external users (4), encrypted with the best procedure possible (please refer to [Encryption Hierarchy](https://docs.seppmail.com/en/03_wp_02_pap_03_encryption-hierarchy.html)), via the Internet.


4.The internal email server (6) transmits the GINA emails to the recipient(s) (8) as well as the sender (7).


5.The recipient (9) as well as the sender (1) can open the email in the email client and, by opening the encrypted HTML attachment via the SSL encrypted path \[(10) and/or (2)\], can access the known GINA web mailer (3), by means of which the original email from the HTML attachment can be decrypted and read.


Advantage: of this solution is the absolute independence from the intermediate components such as email client or email server.


Disadvantage: the disadvantage of this concept is the lack of access to address lists and databases.
