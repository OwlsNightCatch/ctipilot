---
title: Notice and Apology Regarding a Data Breach Resulting from Unauthorized Access to Gyazo
url: https://corp.helpfeel.com/en/news/news-20260916
hostname: helpfeel.com
description: "Helpfeel Inc. (Head Office: Kyoto, Japan; Representative Director and CEO: Isshu Rakusai; hereinafter “Helpfeel”) has confirmed that Gyazo, our image-sharing service, was subject to unauthorized acces"
sitename: 株式会社Helpfeel
date: "2026-09-18"
---
Helpfeel Inc. (Head Office: Kyoto, Japan; Representative Director and CEO: Isshu Rakusai; hereinafter “Helpfeel”) has confirmed that Gyazo, our image-sharing service, was subject to unauthorized access by a third party, resulting in the unauthorized disclosure of user information and certain metadata associated with uploaded images.

We have blocked all access routes used in the incident and have completed remediation of the vulnerability that was exploited. We continue to prioritize measures to prevent further harm while investigating the scope and impact of the incident.

We sincerely apologize to all Gyazo users and other affected parties for the significant concern and inconvenience caused by this incident.

Our investigation remains ongoing, and additional information may come to light. The following summarizes the information we have confirmed as of September 16, 2026.

In this notice, the term “images” refers to all content captured and stored via Gyazo, including screenshots, GIFs, and videos. Unless otherwise stated, all dates and times are in Japan Standard Time (JST).

On September 11, 2026, a third party exploited a vulnerability in Gyazo’s image upload server to gain unauthorized access to our systems and execute arbitrary commands.

That evening, we detected suspicious activity and began investigating and responding to the incident. By the early hours of September 12, we had blocked the identified access routes and terminated unauthorized connections established by the third party.

Our subsequent investigation confirmed that the third party had accessed Gyazo’s database and that user information and metadata associated with uploaded images had been disclosed without authorization.

Our investigation remains ongoing, and additional information may come to light. The facts confirmed as of September 16, 2026, are as follows.

**(1) User Information: Approximately 23.62 Million Records**

We have confirmed that approximately 23.62 million records containing data related to Gyazo users were disclosed without authorization.

The data includes:

- Name (any text entered by the user, such as a name or nickname)
- Email address
- Password hash
- User ID
- Device ID
- Login session ID
- X (formerly Twitter) integration token (if connected)
- Email address associated with Google SSO (if connected)
- Profile information
- Language preference
- Registration date and time
- Last login date and time
- Subscription plan
- Billing status (does not include credit card numbers or other payment method information)
- Usage statistics

The types and extent of data involved vary by user. We are continuing to investigate the details of the affected data and the potential for further harm. We have carefully reviewed the technical characteristics of the authentication-related information involved in the breach and its potential for misuse, and have already implemented the necessary measures, including invalidation and restrictions.

The approximately 23.62 million affected records include records for anonymous accounts with no registered email address or similar information. We are continuing to determine the actual number of individuals whose personal information was disclosed without authorization.

We have confirmed that no payment information, including credit card numbers, was disclosed without authorization.

**(2) Image Metadata: Approximately 490 Million Records**

We have confirmed that approximately 490 million metadata records associated primarily with images registered in or before January 2019 (approximately 14.4% of all image-related data) were disclosed without authorization. In addition, metadata relating to approximately 2.4 million images was separately retrieved using specific filtering criteria and was also disclosed without authorization.

The metadata involved in the breach includes:

- Image ID (information used to construct the image URL)
- Source IP address used for the upload
- User-Agent
- EXIF location data (if contained in the image)
- OCR text extracted from the image
- Image title
- Source URL and other metadata
- Hashed passphrase for private images
- Other related information

The affected metadata includes information used to construct Gyazo image URLs. This information could be used by a third party to access and view the corresponding images without authorization. We have temporarily disabled viewing of some images to prevent further harm.

We have also confirmed that the third party obtained a list identifying private images. As we cannot rule out the possibility that some private images may have been viewed by the third party, we are continuing our detailed investigation.

Our investigation to date has not confirmed any loss of image data resulting from the unauthorized access.

**(3) Impact on Other Helpfeel Services**

Helpfeel and Cosense, which are also provided by Helpfeel Inc., have system architectures that differ from Gyazo’s. Based on our investigation to date, we have not confirmed any unauthorized disclosure of information from the Helpfeel or Cosense systems as a result of this incident.

However, some images displayed within Helpfeel and Cosense using Gyazo may currently be unavailable due to the suspension of Gyazo image delivery in response to this incident.

**(1) Notification to Users**

We plan to send notifications regarding this incident to the registered email addresses of Gyazo users who may have been affected. We are currently working to identify users whose information was disclosed without authorization and will determine which users to notify based on the progress of our investigation.

For users we are unable to reach by email, such as those with anonymous accounts without a registered email address or similar contact information, we plan to provide notifications through the Gyazo web interface.

We are continuing to investigate the details of the affected information. If we identify any additional information that should be shared, we will promptly publish an update.

**(2) Actions We Ask Users to Take to Prevent Further Harm**

To help prevent further harm resulting from this incident, we ask all Gyazo users to change their passwords.

If you use the same or a similar password for Gyazo and any other services, we ask that you also change your passwords for those services.

Please also remain vigilant for any suspicious emails, messages, or other communications related to this incident.

**(3) Contact Information**

For inquiries regarding this incident, please contact us through the appropriate form below.

Japanese:[https://help-ja.gyazo.com/contact-us](https://help-ja.gyazo.com/contact-us)

English:[https://help.gyazo.com/contact-us](https://help.gyazo.com/contact-us)

| September 11 | Unauthorized access to Gyazo occurred. We began investigating and responding to the incident. | 
| September 12 | We completed our initial response measures and remediated the vulnerability that was exploited. | 
| September 14 | Our investigation confirmed that information from Gyazo had been disclosed without authorization. We implemented precautionary measures, including suspending image delivery, while continuing to investigate the scope of the impact, with the prevention of further harm as our highest priority. | 
| September 15 | We implemented additional measures to prevent further harm. We resumed delivery of images newly uploaded after we had completed measures to address the unauthorized access. We also submitted a report to Japan’s Personal Information Protection Commission. | 
| September 16 | We published this notice setting out the scope and impact of the data breach confirmed as of this date. | 

(1) We will continue to prioritize measures to prevent further harm while investigating the scope and impact of the data breach through a forensic investigation conducted by external specialists. If our ongoing investigation identifies any additional information that should be shared, we will promptly publish an update.

(2) We are continuing to assess applicable reporting requirements and to prepare and submit the necessary reports to, and consult with, relevant data protection and regulatory authorities in Japan and other applicable jurisdictions. We are also preparing notifications for Gyazo users. We will determine which users to contact based on the progress of our investigation and will notify them on a rolling basis.

(3) To fully investigate this incident and prevent a recurrence, we will strengthen our security measures, including reviewing our authentication, authorization, and access controls; enhancing our monitoring and audit processes; and improving our secure design, development, and review practices. We will also review our other services for similar vulnerabilities.

We take this incident very seriously and are fully committed to preventing a recurrence and restoring the trust of our users and other stakeholders.
