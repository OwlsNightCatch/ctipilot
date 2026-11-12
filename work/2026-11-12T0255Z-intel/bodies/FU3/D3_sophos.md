---
title: Malicious ScreenConnect deployments observed
author: About the Author
url: https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed
hostname: sophos.com
description: Multiple third-party extensions may linked to the activity
sitename: SOPHOS
date: "2026-11-11"
fingerprint: e3bf463b93d5345
---
Sophos researchers are investigating an active campaign of malicious activity involving unauthorized ScreenConnect client deployments. ConnectWise [released an advisory](https://www.connectwise.com/company/trust/advisories) confirming the incident and is investigating multiple third-party extensions possibly linked to the activity. The advisory recommends disabling the identified extensions as a precautionary measure.

In one case observed by Sophos researchers, curl.exe downloaded ScreenConnect.ClientSetup.msi from 185\[.\]99\[.\]255\[.\]28 to C:\Windows\TEMP\sc.msi. A ScreenConnect-generated command file then launched msiexec.exe to install the client silently. The researchers also observed ScreenConnect scripts staging batch files and using PowerShell with execution-policy bypass to retrieve a second-stage script from ns\[.\]mo7sen\[.\]dev/EadF.php?p=4.

The observed malicious activity has originated from three ScreenConnect instance IDs: d905b2b1b165d0a9, 4b8f4089ddaac6a9, and df1f7ef0cfacd0d8. These are likely compromised instances that are being used to execute commands and deploy the malicious instances. The IDs of those malicious instances are 2588ef5c15954b10 and ed630cc2c873b091.

## Recommended actions

Organizations using ScreenConnect should follow the advice in the ConnectWise advisory. To identify malicious activity, review ScreenConnect command history for unexpected client deployments or remote commands. Usage of curl and PowerShell activity that downloads ScreenConnect installers or scripts from Windows Temp, followed by msiexec.exe installation, should also be investigated.
