---
title: Backdoors in the Dungeon – TURN & MQTT Abused by DragonForce
url: https://lab52.io/blog/backdoors-in-the-dungeon-turn-mqtt-abused-by-dragonforce/
hostname: lab52.io
sitename: lab52.io
date: "2026-10-01"
---
“There are paths that lead into darkness, and once you set foot upon them, the way back is never certain. Somewhere ahead, the dragon waits.”


One of the latest operations uncovered involving DragonForce is the abuse of legitimate TURN (Traversal Using Relays around NAT) servers to encapsulate communications between a malicious implant and the attacker’s infrastructure.

In this article, we provide information on two backdoors used by the attackers. While the first type is better known and can be linked to [Symantec’s report](https://www.security.com/blog-post/dragonforce-msteams-backdoor), the second type is notable for its use of MQTT as an additional communication channel in the event that communication through TURN fails.

The first type has been observed during an initial deployment phase, while the second type corresponds to a backdoor that is expected to remain resident on disk, albeit protected.

# Backdoor 1 – TURN

The first backdoor is injected directly into memory. Its metadata name is **Shell.dll**, and it is a binary written in Go. To deploy this backdoor, the attackers use TURN, resolving the IP address of their C2 server directly in memory through decryption. Among its features, this backdoor retains the use of a private key for its SSH communications.

The following diagram illustrates the deployment model. The attackers abuse legitimate Microsoft Teams TURN servers, thereby masking their traffic.

# Backdoor 2 – TURN | MQTT

The second backdoor is used for persistence, as it is executed through a scheduled task left behind by a previous stage.

In this case, it is loaded via DLL sideloading, abusing the legitimate **javaw.exe** executable, which loads **jli.dll**, the first-stage loader. This loader, in turn, loads **rvsdiqw.txt**, the next stage, which is encrypted with DPAPI to make the file dependent on the PC on which it is executed. Additionally, **jli.dll** will have a different hash on each system where it is executed.

There is another **jli.dll** artifact with the hash **6bbf10bcbef7ac5102b54c81137859891a3802dbacd888be90f990d50e18b0b4** that can be directly linked to DragonForce through previous reports. That other artifact is different from the one used in this loader and is not included in this post, although it is already available on VirusTotal.

Returning to the case at hand, the following diagram summarizes the observed deployment operation, identifying the TURN communication flow as well as an **additional flow via MQTT for communication with the C2**.

Details of these communication flows are provided below.

## TURN Flow

The C2 communication flow over TURN first sends a request using the same protocol observed previously, with the following format:

**TRN1<UUID:16>22222222@@@**

Next, the beacon generates a random 8-byte nonce using the **BCryptGenRandom** API and sends this value in a request with the following format:

**TRN1<UUID:16>33300000<NONCE:8>@@@**

The binary then checks whether the received string is **nocmd**, indicating that there is no task for the beacon.

It then checks whether the message starts with **[33300000**. This indicates that a task is available. The beacon begins downloading data from the server, receiving a message containing an MD5 hash and the number of blocks to be received:

**[33300000<Nonce:8><MD5:32><Count:4>**

After validating the nonce, the program sends a request to retrieve the files:

**TRN1<UUID:16>33299999<NONCE:8>@@@**

The request is parsed by searching for the [ character. Each time one is found, the program attempts to interpret a record with the following structure:

**[<NONCE:8><INDEX:4><MD5:32><LENGTH:8><SEPARATOR:1><DATA:N>]**

After parsing the record, the code iterates through all expected indexes, checks whether any are missing, and validates the MD5 hash of each block. If a block is missing, it can be retrieved using the following request:

**TRN1<UUID:16>3320<INDEX:4><NONCE:8>@@@**

Once all blocks have been obtained, the program reconstructs the final package and validates its MD5 hash. Finally, it sends an acknowledgment message:

**TRN1<UUID:16>33100000<NONCE:8>@@@**

The contents of the package are then Base64-decoded. The package has the following format:

**<Value1:8><XOR_Material:8><Encrypted_Payload:N>**

A key is then derived by performing an XOR operation using the 8 bytes of **XOR_Material**, which is subsequently used to decrypt the code. Finally, the decrypted code is executed using **CreateThread**.

The program also contains code that allows data to be sent from the beacon to the C2, but this functionality is only used during the initial handshake.

### Sending Beacon Data to the C2 After the Initial Handshake

The beacon can upload data blocks with a maximum size of 930 bytes using the following format:

**[<UUID:16><TRANSFER_ID:8><INDEX:4><MD5:32><LENGTH:8>]<DATA:N>**

Once all blocks have been generated, the beacon calculates the MD5 hash of the complete content and sends a request to initiate the transfer using the following format:

**TRN1<UUID:16>4440<NUMBER_OF_BLOCKS:4><TRANSFER_ID:8><MD5:32>@@@**

After sending the request, the beacon waits 5 seconds and checks whether the response begins with the string **NEXT**. If a valid response is received, it performs another communication, waits 3 seconds, and then starts querying the transfer status using the following request:

**TRN1<UUID:16>4410????<TRANSFER_ID:8>@@@**

The server can respond with the string **DONE** followed by the transfer identifier:

**DONE<TRANSFER_ID:8>**

If any blocks are missing, the server can request their retransmission using a response with the following format:

**RESEND<TRANSFER_ID:8><INDEX:4>**

### Command Summary

| Command | Description | 
| 22222222 | Initiates communication with the C2. | 
| 33300000 | Checks for new tasks. | 
| 33299999 | Requests the blocks of a task. | 
| 3320<INDEX:4> | Requests retransmission of a downloaded block. | 
| 33100000 | Confirms the complete receipt of a task. | 
| 4440<COUNT:4> | Initiates a transfer from the beacon to the C2. | 
| 4410???? | Queries the status of a transfer. | 

## MQTT Flow

In the case of MQTT, the program uses a similar protocol. After validating the timestamp received during the authentication process, the beacon generates a random 16-character string that acts as a session identifier. It then sends a message to the MQTT broker using the identifier stored in the sample’s configuration as the topic.

The message contains only the previously generated session identifier:

**<SESSION_ID:16>**

After completing the registration, the program queries the task-receiving topic using the system’s UUID. If the server returns no content, or if the received response contains only the value `0`, the beacon assumes that there are no pending tasks and terminates the communication.

If a task is received, the program waits 3 seconds and calculates the length of the received message. It then Base64-decodes its contents using the **CryptStringToBinaryA** API. The decoded package has the following format:

**<XOR_Material:8><Encrypted_Payload:N>**

The beacon derives a one-byte key by XORing the 8 bytes of **XOR_Material**. This key is then used to decrypt the remainder of the package by performing an XOR operation on each byte of the encrypted content.

After decrypting the message, the program checks that its contents begin with a JSON structure containing the **cmdnum** field. The check is performed by verifying that the string **cmdnum** appears starting at the third byte, meaning that the expected message has a structure similar to:

**{“cmdnum”:…}**

After obtaining **cmdnum**, the beacon queries another MQTT topic to retrieve the metadata associated with the payload. This message differs from the task JSON and includes a 16-byte transfer identifier, the MD5 hash of the content, the number of blocks, and the total size. The received format is:

**<TRANSFER_ID:16>;TotalMD5:<MD5:32>;chnkNum:<COUNT>;totalSize:<SIZE>**

The program then uses this identifier to generate the topics corresponding to each block, appending a four-digit decimal index:

**<TRANSFER_ID:16>0001 <TRANSFER_ID:16>0002<TRANSFER_ID:16>0003**

Each block is retrieved through a new MQTT request and concatenated with the previous blocks. If a request returns no content, the index is not incremented and the program requests the same block again.

After downloading all the blocks, the beacon removes the headers delimited by the [ and ] characters. It then checks that the length of the reconstructed content matches the value specified in **totalSize**.

After validating the content by calculating its MD5 hash, the package is Base64-decoded. The resulting data has the following format:

**<XOR_KEY:8><Encrypted_Payload:N>**

The decrypted content is an executable code template. Depending on the value of **cmdnum**, the JSON message is accompanied by different parameters that are inserted into the payload regions identified by a sequence of **0xAA** bytes. The following actions are performed according to **cmdnum**:

| cmdnum | Fields accompanying the command | Usage | 
| 1 | **shk_url** ,**tedByUID** | Inserts both values into the payload, separated by 256 bytes. | 
| 2 | **ps_line** ,**cmdid** | Inserts the PowerShell command line into the payload and copies 8 bytes of **cmdid** at offset**5000** . | 
| 3 | None | Directly uses the payload without adding any parameters. | 
| 4 | **rhost** ,**rport** | Inserts the remote host and port into the payload, separated by 256 bytes. | 

Finally, the program executes the payload by changing the memory region’s protection using **VirtualProtect** and executing it via **CreateThread**.

If any of the communications fail, the beacon calls **Sleep** for 5 minutes and encrypts the contents of the memory region where it is executing in order to evade detection by security tools while it is inactive.

# Conclusion

DragonForce is a ransomware-as-a-service (RaaS) operation that emerged around 2023 and has since evolved into a significant player in the ransomware ecosystem. Beyond its role as a conventional ransomware group, DragonForce provides infrastructure, tooling, and services that enable affiliates and other operators to conduct attacks against organizations. Recent activity associated with DragonForce also highlights a broader focus on maintaining persistent access and establishing resilient communication channels. In particular, observed operations have involved the deployment of multiple backdoors that abuse legitimate infrastructure, including Microsoft Teams TURN servers, to communicate with attacker-controlled infrastructure while blending malicious traffic with legitimate services.

The backdoor analysed here also incorporate MQTT as an alternative communication channel, providing redundancy in the event that TURN-based communications fail. The observed tooling includes in-memory execution, DLL sideloading, scheduled-task persistence, encrypted payloads, and mechanisms designed to protect or conceal malicious code while inactive. This activity illustrates how DragonForce has expanded beyond the deployment of ransomware itself toward a more mature operational model combining access, persistence, custom tooling, and resilient command-and-control infrastructure. Over time, DragonForce has consequently evolved from a traditional RaaS model into what has been described as a “ransomware cartel,” making it a particularly relevant case study in the evolution and professionalization of modern cybercrime.

# Intelligence Availability Notice

This article presents selected insights derived from our broader threat intelligence operations and coverage. Additional details related to this campaign, as well as other investigations and ongoing intelligence activities, are enriched and available through our private intelligence feed.

## Indicators of Compromise (IOC)

### Artifacts

| Name | Hash SHA256 | 
| jli.dll | f8eabae53e9dc8c529b6e38c58040ff28a07728cb5e896e16fb64e84bed5cd88 | 
| jli.dll | e9cd052f2d9514d40235ec04c9592f4274d0a4161b846e59bbb5a1a2c806a1c5 | 
| jli.dll | 6bbf10bcbef7ac5102b54c81137859891a3802dbacd888be90f990d50e18b0b4 | 
| 25vtps.txt | 1657b22a553feae422dab77886ac60c06b8fad7cbd2cfaf482ba9066ba9922be | 
| dldwuibjn_chShllcodeTrn.txt | 5275579f539812ff66d060e12c9b7e99a22c625018f1aae9c5642ab0ba058ccb | 
| dldwuibjn_chShllcodeTrn.bin | c91852bfb8f1d428875595c14cfada8fb234483adb8c6ba78ca2b5ae2a0683e2 | 
| rvsdiqw.txt | 01d638ddd9d780e934305422bc9ee8fa3a5b3163ba66514ae5e5a34ff24df9db | 

### Network indicators

hxxp://188.190.4[.]111/25vtps.txt

hxxp://188.190.4[.]111/dldwuibjn_chShllcodeTrn.txt

62.164.177[.]145:3478

217.156.8[.]181:7586

hxxps://accesscapfunding[.com/wp-

content/themes/twentytwentyfour/v4wwy9.php

hxxps://www[.paigeinfull[.com/wp-content/themes/twentyeleven/g5kq2b.php 

hxxps://cncluxurywater[.com/wp-content/themes/twentytwentythree/wd9o9v.php

hxxps://printpro.com[.pl/wp-content/themes/twentytwentytwo/ghq4sk.php

hxxps://pymsolutions[.com.ar/wp-content/plugins/easypost/mn3fda.php

hxxps://whapido.com[.ar/wp-content/themes/elessi-theme/ze1edd.php

hxxps://prolabgest[.it/language/ove
