---
title: auth0-customer-detections/detections/risk_of_signup_fraud_by_disposable_domains.yml at 5b3940da41120c9303cb4beae31526aa3e45862c · auth0/auth0-customer-detections
url: https://github.com/auth0/auth0-customer-detections/blob/5b3940da41120c9303cb4beae31526aa3e45862c/detections/risk_of_signup_fraud_by_disposable_domains.yml
hostname: github.com
description: Contribute to auth0/auth0-customer-detections development by creating an account on GitHub.
sitename: GitHub
date: "2025-08-15"
categories: ['repository:1038808312']
fingerprint: "2a0f290b0ef6ec6b"
language: en
image: https://opengraph.githubassets.com/48e48c44cd301dcbc8dd289462303bc8ec4447c2e9932683a9e7495d1759415b/auth0/auth0-customer-detections
pagetype: object
filedate: "2026-11-26"
---
## Repository navigation


## Expand file tree

/
# risk\_of\_signup\_fraud\_by\_disposable\_domains.yml


Copy path
More file actions

80 lines (80 loc) · 3.57 KB

/
# risk\_of\_signup\_fraud\_by\_disposable\_domains.yml


Copy path
## File metadata and controls

80 lines (80 loc) · 3.57 KB

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

title: Risk of signup fraud - rapid creation of fake accounts with disposable email domains

id: e92605d8-716d-11f0-b2ae-723487b9527c

name: selected\_events

status: experimental

description: |

Detect potential signup fraud by monitoring the use of disposable emails.

author: Okta

date: 2025-07-11

modified: 2025-09-17

logsource:

product: auth0

references:

\- https://blog.castle.io/fraudulent-email-domain-tracker-july-2025/

detection:

selection:

data.type: ss

data.user\_name|endswith: # examples of email domains, see reference (the custle blog)

\- "@mailinator.com"

\- "@yopmail.com"

\- "@10minutetempemail.com"

\- "@guerrillamail.com"

\- "@temp-mail.org"

\- "@disposable.com"

\- "@mailnesia.com"

\- "@sharklasers.com"

\- "@getnada.com"

condition: selection

explanation: >

The query monitors successful signups events when a disposable email has been used.

The Splunk query considers a number of signups within specified time chunks (e.g. 1h)

and alerts when the number of users with disposable emails exceeds a threshold.

splunk: |

index=auth0 data.tenant\_name="{your-tenant-name}"

data.type = ss

| fields data.user\_name, data.user\_id, data.type

| bin \_time span=1h

| search data.user\_name IN ("\*@mailinator.com", "\*@yopmail.com", "\*@10minutemail.com",

"\*@guerrillamail.com", "\*@temp-mail.org", "\*@disposable.com", "\*@mailnesia.com",

"\*@sharklasers.com", "\*@getnada.com", "\*@mohmal.com")

| stats dc(data.user\_name) as user\_count values(data.user\_name) as user\_names

values(data.user\_id) as user\_ids by \_time, data.type

| where user\_count > {thresholds\_disposable\_emails}

comments:

\- The Splunk query above shall be tuned to reflect a valid tenant name.

\- The value for thresholds\_disposable\_emails should be set based on the customer's environment and expected behavior.

\- To learn normality, it is recommended to run the query (excluding "where" clauses) for a period of time

and calculate the thresholds based on the observed data.

\- The query can be adjusted to account for a longer public blocklist, e.g. available on github, using a lookup table.

\- It also can be extended with a list of fraudulent email domains provided by the reference above (the catle blog).

tenant\_logs: |

type:"fs" OR type:"ss" OR type:"signup\_pwd\_leak"

prevention:

\- Use pre-registration actions to block any registration with disposable emails.

\- Force email OTP validation built-in feature of a Database connection on signup.

\- Enforce email link based validation on signup and deny access to unverified accounts

terminating sessions and revoking tokens.

\- Block or delete the created fraudulent accounts.

\- Instead of blocking users, consider to use additional risk signals to increase assurance in

further activities from these users.

\- Enable breached password protection and bot detection to detect and block suspicious activities.

\- For high-risk applications, consider to enforce identity proofing or closely monitoring activities from such accounts.

falsepositives:

\- Legitimate users using disposable email addresses for privacy reasons.

level: medium

tags:

\- attack.resource-development

\- attack.t1136

---

title: Surge in signup events from disposable domains

id: 7b4433e7-2857-4cfc-bfe0-29dc74feb63f

correlation:

type: value\_count

rules:

\- selected\_events # Referenced here

group-by:

\- data.ip

timespan: 1h

condition:

gte: 0

field: data.user\_name
