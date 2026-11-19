---
title: Unit42-timely-threat-intel/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt at main · PaloAltoNetworks/Unit42-timely-threat-intel
url: https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt
hostname: github.com
description: A collection of files with indicators supporting social media posts from Palo Alto Network's Unit 42 team to disseminate timely threat intelligence. - PaloAltoNetworks/Unit42-timely-threat-intel
sitename: GitHub
date: "2026-10-07"
categories: ['repository:684806858']
fingerprint: e5828991878c978b
---
## Repository navigation


## Expand file tree

/
# 2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt


Copy path
More file actions

116 lines (86 loc) · 5.6 KB

/
# 2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt


Copy path
## File metadata and controls

116 lines (86 loc) · 5.6 KB

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

2026-10-07 (WEDNESDAY): EXPLOITATION OF CVE-2026-90817 FOR EVASIVE CRYPTOCURRENCY MINING CAMPAIGN

AUTHORS:

\- Nithin Chenthur Prabhu, Somil Tyagi, Alex Payne

REFERENCES:

\- https://www.linkedin.com/posts/weve-observed-in-the-wild-exploitation-of-ugcPost-7515577085759963136-eS2m/

\- https://x.com/Unit42\_Intel/status/2109811397617992120

NOTES:

\- Attackers are actively exploiting CVE-2026-90817

\- CVE-2026-90817 allows for Remote Code Execution (RCE) in vulnerable versions of public-facing REDCap servers

\- Successful exploitation leads to an in-memory execution chain utilizing:

-- Native bash networking

-- Steganographic payload delivery disguised as image files

-- Process masquerading

-- Anti-forensic measures

\- This in-memory execution chain has deployed Monero (XMRig) cryptocurrency miners

\- Intelligence derived from the configured XMRig mining pool wallet confirms:

-- An active campaign

-- At least four live worker instances concurrently mining cryptocurrency

\- Per REDCap:

-- Research Electronic Data Capture (REDCap) is committed to maintaining a secure platform and responding promptly to identified vulnerabilities.

-- After learning of this vulnerability in September, REDCap released a software update addressing it within two days.

-- We will continue to work closely with REDCap partner institutions and their administrators to provide timely, transparent communication about security-related matters.

DETAILS:

Initial Access for Exploitation:

\- Attackers attempt to exploit CVE-2026-90817 through an unauthenticated HTTP POST request:

\- The request is: POST /redcap/surveys/?s=NXCJMDCWXE&\_\_passthru=%2569ndex.php&route=DataImportController%3Aindex

Web Shell Staging:

\- These exploitation attempts leverage:

-- An accessible public survey hash parameter (s=NXCJMDCWXE) to route execution through 'php-fpm'

--- 'php-fpm' runs under web server permissions

-- A successful execution stages a transient Blade template web shell under:

/var/www/html/redcap/temp/cache/d3f11fc8ee9c2d986425eff26ecace5b4004eb8e.bladec

Fileless Reverse Shell & Payload Delivery:

\- The webshell uses an injected command to execute a Base64-encoded bash cradle entirely in memory

\- The cradle opens a raw socket to an S3 bucket via native bash networking

-- This is done to evade perimeter network inspection and avoid dropping binaries

\- An HTTP GET request fetches a secondary payload

-- The payload is  disguised as a JPEG image (URL ending in /banner\_avp\_800x800.jpg)

-- HTTP response headers are stripped using 'sed'

-- The resulting bash script is piped directly into execution (| bash)

\- The secondary payload is an archive for XMRig v6.26.0

Cryptocurrency Miner Staging & Execution:

\- The XMRig archive is saved to a hidden, host-derived staging directory established at:

/var/tmp/.syslog-a224be51/xmrig.tar.gz

\- The miner is configured via a multi-pool configuration file

-- This configuration file is also fetched as a disguised image (URL ending in /banner-ver2\_800x800.jpg)

-- This configuration directs mining to auto.c3pool\[.\]org

-- Uses a 0% donation fee and binds an administrative JSON-RPC API to 127.0.0.1:50001 with bearer token '123'

Campaign Telemetry:

\- Public telemetry from the mining pool reveals the attackers' configured XMR payout wallet at:

87maYgt7bMvgDxQsBavYNVDr6BQgJNaaRKXg2yBh8A3GLVoizCq9eeycBT7v6kdnm8f41Vfz84x6XLeEUJDRqvYbSrhvzTw

-- This wallet activity confirms at least four active worker nodes currently mining

-- These four nodes indicate wider ongoing exploitation

Defense Evasion & Process Masquerading:

\- The cryptocurrency miner binary is executed using 'exec -a'

-- The 'exec -a' command uses randomized, syslog-themed process names (e.g., syslog-ng-{hash})

-- These syslog-themed process names are an attempt to blend into legitimate Linux system services

\- An inline, Base64-obfuscated watchdog daemon (syslog-helper) runs in a continuous 0.1-second loop

-- It polls the 'w' command to detect interactive user sessions

-- This daemon looks for active sessions with idle times under 300 seconds

--- If detected, the daemon pauses mining via the local JSON-RPC API

--- This is likely an attempt to avoid detection

Competitor Miner Neutralization:

\- The deployment script actively inspects running process memory and strings

-- This is done to identify and kill rival mining instances

-- Matching strings for rival mining instances include 'stratum+tcp' or 'randomx'

\- Known competitor staging directories are locked by changing file permissions to '000'

-- Examples of these directory paths include '/dev/shm/duet' and '/var/tmp/.bin

Persistence & Anti-Forensics:

\- The script modifies system crontabs to establish scheduled execution

-- The script periodically pulls payloads (grepb2.jpg)

\- An unauthorized RSA public key is appended to all accessible 'authorized\_keys' files across user profiles

-- The associated fingerprint is: Ant3qLKQ9

\- Attackers modify '\~/.profile'

\- Attackers also explicitly wipe session history by unsetting 'HISTFILE' and purging '\~/.bash\_history'

INDICATORS:

\- 202.61.130\[.\]221

-- Attacker IP address (exploit source)

\- 39a435123dc1fffd499aa2acf11ef46e3ee2e805bf137811af0c2c5b12546920

-- SHA-256 hash for secondary stage payload script (dropper for cryptocurrency miner)

\- /var/www/html/redcap/temp/cache/d3f11fc8ee9c2d986425eff26ecace5b4004eb8e.bladec

-- Path for dropped web shell file

\- /var/tmp/.syslog-a224be51/xmrig.tar.gz

-- Path for staged cryptocurrency miner archive

\- 87maYgt7bMvgDxQsBavYNVDr6BQgJNaaRKXg2yBh8A3GLVoizCq9eeycBT7v6kdnm8f41Vfz84x6XLeEUJDRqvYbSrhvzTw

-- Address for attacker's XMRig wallet (used by active worker fleet)
