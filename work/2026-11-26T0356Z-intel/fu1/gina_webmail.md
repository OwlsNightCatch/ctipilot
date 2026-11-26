---
title: GINA webmail
author: SEPPmail GmbH
url: https://www.seppmail.com/03_wp_02_pap_02_et_04_gina__gina-webmail.html
hostname: seppmail.com
description: The SEPPmail Secure E-Mail Gateway uses a technology for spontaneous communication, the GINA technology.
sitename: seppmail.com
date: "2023-01-01"
tags: ['GINA', 'Web Mail', 'Webmail']
fingerprint: ae14a85b0641faed
language: de
filedate: "2026-11-26"
---
The SEPPmail Secure E-Mail Gateway uses a technology for spontaneous communication, the GINA technology.

By means of this technology, it is guaranteed that emails which are to be encrypted can also be encrypted if the communication partner does not have any standard technologies available to them.

For reading the emails encrypted by means of this technology, the communication partner only requires Internet access, the means for receiving emails\* and a web browser.

There are no additional requirements to the user's infrastructure.


\* If a separate email client is used to receive emails, it must be able to handle file attachments, especially in HTML format.


See also our [explanatory video](https://vimeo.com/847984884) for the GINA technology.


GINA offers substantial advantages for the secure email communication with any partner compared to other solutions available in the market:


|  | encryption | "Normal" Secure Web Mail | Self- extracting archive | Special Client |  | 
| Recipient only needs standard components (email client/browser/Internet) | x | √ | x | x | √  | 
| Change of password possible | x | √ | x | x |  | 
| Secure reply possible | x | √ | x | √ |  | 
| The email is delivered immediately and completely | √ | x | √ | √ |  | 
| The corporate identity can be individually adapted | √ | √ | x | x |  | 
| The recipient may store their public key | x | √ | x | x |  | 
| The recipient may set their desired password in advance | √ | √ | x | x |  | 
| The appliance does not include any user data | √ | x | x | x |  | 
| Phishing resistant | x | x | √ | √ |  | 
| Resistant against brute force attacks | x | √ | x | √ |  | 
| "Email as registered letter"; read confirmation possible | x | √ | x | x |  | 
| Password self service | x | √ | x | x |  | 
| Two-factor authentication | x | x | x | x |  | 
| Queue-less operation (no data loss in the event of a failure) | x | x | x | x |  | 


[a) Step 1: Sender – Creating the email](https://docs.seppmail.com/en/03_wp_02_pap_02_et_04_gina__gina-webmail.html#step1)

The sender writes an email in their standard email client and classifies it as confidential. Several options are available for doing this (Figure 1):


•Selecting "confidential" in the email client on-board resources (1)


•Using a keyword which is defined across the entire company (2)

By default, this keyword is \[confidential\]. This method is available on all email clients and is often also used for system users, i.e. the automated control.


•Via the free of charge  [SEPPmail Microsoft Outlook Add-In](https://docs.seppmail.com/en/06_moa__microsoft-outlook-add-in.html) (3).

Here, the user can choose between

a)"Encrypt"

Initiates the encryption using the most suitable technology for the recipient (see also [Encryption Hierarchy](https://docs.seppmail.com/en/03_wp_02_pap_03_encryption-hierarchy.html)).


b)"Encryption with read confirmation"

Enforces the GINA technology in connection with the read confirmation request on the client side. This triggers a read confirmation which cannot be suppressed by the recipient. This procedure can be compared to a registered letter with return receipt.


Figure 1: Screenshot for Outlook with Encrypt button and Confidential tag


Thereafter, the email is sent as usual.


The email marked this way reaches the SEPPmail Secure E-Mail Gateway. It evaluates the set marks and carries out the actions initiated by it.

If, due to missing key material or a mandatory read confirmation, GINA is used, the process is as follows:


If not already available, a GINA account or auxiliary account is created for the relevant recipient email address – depending on the procedure – whereby an individual, password-protected AES256 key is generated and saved for the recipient email address.


Various methods are available for authenticating recipients of GINA messages. These differ primarily in terms of user-friendliness and security.

When selecting a method, the protection requirements of the information to be sent should be the primary consideration. The level of protection required in each individual case is always determined by several factors, in particular the probability of a risk occurring and the possible consequences of a data breach. The risk assessment is the responsibility of the customer (the controller).

As a rule, the criteria to be applied can be found in the respective company policy.
