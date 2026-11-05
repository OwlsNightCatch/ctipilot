# Binarly advisory BRLY-2026-057 (rendered from the page payload) - https://www.binarly.io/advisories/brly-2026-057
cveId: CVE-2026-107441
title: Out-of-bounds write vulnerability in Zyxel GS1900 switches allows unauthenticated remote code execution.
publishDate: 2026-11-03
cvssScore: 9.8
## description
**BINARLY REsearch team** has discovered an out-of-bounds write vulnerability in the `dispatcher.cgi` CGI program used by Zyxel GS1900 switches that could allow a potential unauthenticated remote attacker to execute arbitrary OS commands with root privileges.

## vulnerabilityInformation
- BINARLY internal vulnerability identifier: BRLY-2026-057
- Zyxel PSIRT assigned CVE identifier: [CVE-2026-107441](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-out-of-bounds-write-vulnerability-in-gs1900-series-switches-11-03-2026)
- CVSS v3.1: 9.8 Critical (`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`)

## potentialImpact
An unauthenticated remote attacker can execute arbitrary OS commands with root privileges.

## DETAIL: Affected firmware with confirmed impact by BINARLY team
| Device name         | Firmware version |
| ------------------- | ---------------- |
| Zyxel GS1900-8      | 2.90(AAHH.2)C0   |
| Zyxel GS1900-8HP    | 2.90(AAHI.2)C0   |
| Zyxel GS1900-10HP   | 2.90(AAZI.2)C0   |
| Zyxel GS1900-16     | 2.90(AAHJ.2)C0   |
| Zyxel GS1900-24     | 2.90(AAHL.2)C0   |
| Zyxel GS1900-24E    | 2.90(AAHK.2)C0   |
| Zyxel GS1900-24EP   | 2.90(ABTO.2)C0   |
| Zyxel GS1900-24HPv2 | 2.90(ABTP.2)C0   |
| Zyxel GS1900-48     | 2.90(AAHN.2)C0   |
| Zyxel GS1900-48HPv2 | 2.90(ABTQ.2)C0   |

All ten archives contain identical `.bix` firmware payload and therefore the same CGI binaries:

| Component                                | SHA-256                                                            |
| ---------------------------------------- | ------------------------------------------------------------------ |
| `.bix` firmware payload                  | `8fc87aeadd18e7d711e5fec8e0003f0283c40c06a5800580458937579d65af79` |
| `/home/web/cgi-bin/dispatcher.cgi`       | `7dc47078f0ff2d75de4a7cd71895d01f0cce4728517f5efd94e2212975ceb811` |
| `/home/web/cgi-bin/httprestorecfg.cgi`   | `4df2e411bffcabb04280dd297fd49d897a54b9309457cc610211a1b88bdb3aff` |
| `/home/web/cgi-bin/httpupload.cgi`       | `1a2f0bc1ddc1900d99be1a6fd4c6497d2f40e102bbb50d95bf6429acd399128a` |
| `/home/web/cgi-bin/httpuploadbakcfg.cgi` | `a14e0b2c11d20847108820ed0b13a8242e9f9ed2353f54b8dacbe4709578da51` |
| `/home/web/cgi-bin/httpuploadcert.cgi`   | `b19349edc51c644ad023efb882712b241bdc43ea487d03cbcf86fd731045a733` |
| `/home/web/cgi-bin/httpuploadruncfg.cgi` | `699b88458b434e25423292cf94ba0ba1615252bcd6fe51bd516ec390cf1a235f` |
| `/home/web/cgi-bin/login.cgi`            | `da1db59280f1752e3b5bdbd4f17dd8710e5f01cc6306ce2ff8c882500b78311e` |

## DETAIL: Vulnerability description
The vulnerable `web_util_initParaPairs` implementation is present in all seven CGI binaries. However, it is reachable from the program entry point only in `dispatcher.cgi`, `httprestorecfg.cgi`, and `httpupload.cgi`.

Let's consider the `dispatcher.cgi` binary. The pseudocode for the vulnerable function is shown below:

```c
int __fastcall web_util_initParaPairs(int use_query_string)
{
  int read_arg2; // $a1
  char *(**read_func)(char *, int, FILE *); // $t9
  char *req_method; // $v0
  int read_arg3; // $a2
  char *query_str; // $v0
  char *tok_start; // $s3
  char *amp; // $s2
  char *slot; // $s1
  char *sep; // $v0
  char *sep_; // $s0
  size_t tok_len; // $v0
  char *tail_slot; // $s2
  char *tail_sep; // $v0
  char *tail_sep_; // $s1
  const void *tail_ptr; // $s0
  size_t tail_len; // $v0
  int count; // $v1
  _BYTE s[4096]; // [sp+18h] [-2000h] BYREF
  char src[4096]; // [sp+1018h] [-1000h] BYREF

  memset(s, 0, sizeof(s));
  memset(src, 0, sizeof(src));
  memset(reqParameters, 0, sizeof(reqParameters));
  if ( use_query_string != 0 )
  {
    read_arg2 = getenv("QUERY_STRING");
    if ( read_arg2 == 0 )
      return 0;
    read_func = &strlcpy;
  }
  else
  {
    req_method = getenv("REQUEST_METHOD");
    if ( strcmp("POST", req_method) == 0 )
    {
      read_func = &fgets;
      read_arg3 = stdin;
      read_arg2 = 4096;
      goto _get_url;
    }
    query_str = getenv("QUERY_STRING");
    read_func = &strlcpy;
    read_arg2 = query_str;
  }
  read_arg3 = 4096;
_get_url:
  tok_start = src;
  (read_func)(src, read_arg2, read_arg3);
  for ( amp = strchr(src, '&'); amp != nullptr; amp = strchr(amp + 1, '&') )
  {
    slot = &reqParameters[1024 * g_count];
    memcpy(slot, tok_start, amp - tok_start);
    slot[amp - tok_start] = 0;
    sep = strchr(slot, '=');
    sep_ = sep;
    if ( sep != nullptr )
    {
      if ( sep[1] == '&' )
        slot[512] = 0;
      else
        urlDecode(slot + 512, sep + 1);
      *sep_ = 0;
    }
    tok_start = amp + 1;
    if ( ++g_count == 140 )
      return 0;
  }
  if ( -src < strlen(src) )
  {
    tail_slot = &reqParameters[1024 * g_count];
    tok_len = strlen(tok_start);
    memcpy(tail_slot, tok_start, tok_len);
    tail_slot[strlen(tok_start)] = 0;
    tail_sep = strchr(tail_slot, '=');
    tail_sep_ = tail_sep;
    if ( tail_sep != nullptr )
    {
      tail_ptr = tail_sep + 1;
      tail_len = strlen(tail_sep + 1);
      memcpy(tail_slot + 512, tail_ptr, tail_len);
      *tail_sep_ = 0;
    }
    ++g_count;
  }
  count = g_count;
  if ( g_count >= 141 )
    count = 140;
  g_count = count;
  return 0;
}
```

The CGI parser stores request parameters in the global `reqParameters` object. The object contains 140 entries of 1024 bytes each (143364 bytes in total) followed by the global parameter counter (`g_count`):

```
.bss:10004430                 .globl reqParameters
.bss:10004430  # char reqParameters[143364]
.bss:10004430 reqParameters:  .space 0x23000           # DATA XREF: LOAD:00409660↑o
.bss:10004430                                          # web_util_paramVal_ret+2C↑o ...
.bss:10027430 g_count:        .space 4                 # DATA XREF: web_util_paramVal_ret+38↑r
```

Each entry is treated as a 512-byte parameter name followed by a 512-byte value.

The parser checks the parameter count **only after copying a complete component**. It also does not limit the component to the 1024-byte entry or its two 512-byte fields:

```c
for ( amp = strchr(src, '&'); amp != nullptr; amp = strchr(amp + 1, '&') )
{
  slot = &reqParameters[1024 * g_count];
  // 1. when g_count is 139, slot will point to `reqParameters + 142336`
  //    (1024 bytes prior to the g_count address)
  // 2. `amp - tok_start` is not validated and may exceed the 1024 bytes allocated per slot;
  //    the size is only bounded by maximum size of `src`, which is 4096
  memcpy(slot, tok_start, amp - tok_start);
  slot[amp - tok_start] = 0;
  sep = strchr(slot, '=');
  sep_ = sep;
  if ( sep != nullptr )
  {
    if ( sep[1] == '&' )
      slot[512] = 0;
    else
      urlDecode(slot + 512, sep + 1);
    *sep_ = 0;
  }
  tok_start = amp + 1;
  // 3. check for g_count; at this point, g_count can be rewritten by a `memcpy` call
  if ( ++g_count == 140 )
    return 0;
}
```

In the affected binary, entry 139 starts at `0x10027030`, with `g_count` located immediately afterwards at `0x10027430`. Therefore, a 1028-byte value will overwrite entry 139 and replace `g_count` with an attacker-controlled value.

The loop body then reloads and increments the corrupted counter. The incremented value is used to derive the destination of the final parameter.

`g_count` is treated as an `int`, so by setting it to a negative value (for example, close to `uint32_max`), an attacker can write before `reqParameters`.

Attackers are therefore able to overwrite values from the GOT, which in the target binary begins at address `0x10002C40`:

```
.got:10002C40 web_radiusSrv_post_ptr:.word web_radiusSrv_post
.got:10002C44 web_igmp_port_filter_post_ptr:.word web_igmp_port_filter_post
.got:10002C48 tabs_monitor_error_disabled_ptr:.word tabs_monitor_error_disabled
.got:10002C4C __fputc_unlocked_ptr:.word __fputc_unlocked
.got:10002C50 web_vlan_voiceVlan_oui_post_ptr:.word web_vlan_voiceVlan_oui_post
.got:10002C54 web_trunk_config_lag_mgmt_add_get_ptr:.word web_trunk_config_lag_mgmt_add_get
.got:10002C58 sal_optical_diagMeasure_get_ptr:.word sal_optical_diagMeasure_get
.got:10002C5C sal_optical_diagOptionalStatus_get_ptr:.word sal_optical_diagOptionalStatus_get
.got:10002C60 free_ptr:       .word free
...
```13:T93

## DETAIL: Exploitation in the wild
[GreyNoise reported](https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation) that a threat actor exploited CVE-2026-7273 against 996 Zyxel GS1900 switches across 48 countries. The actor exfiltrated switch configurations, hashed root credentials, and networking information.

The PyArmor-obfuscated Python exploit described by GreyNoise matches the captured exploit analysed by Binarly team. It implements the parameter-counter corruption, and supports both a deterministic GOT overwrite and a stack target mode.

CISA added CVE-2026-7273 to its [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273) on September 21, 2026.

Zyxel describes CVE-2026-7273 as a stack-based buffer overflow and assigns it CVSS score of `8.8 High` (`CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`).

The binary diff shows that Zyxel added the following logic to the affected parameter parser:

```diff
>     if ( ++g_count == 140 )
>       return 0;
82a87,90
>   if ( g_count >= 141 )
>     count = 140;
>   g_count = count;
```

This change does not address the vulnerability. An unbounded copy into entry 139 occurs prior to the check. This means that the `g_count` value can be overwritten before it can be checked.

Additionally, the public vulnerability description does not correspond to the vulnerability described in current advisory:

- the overflowing object is the global `reqParameters` object in `.bss`, not a stack buffer
- exploitation uses HTTP and has no protocol-level adjacency requirement; an attacker only needs network reachability to the management service; we therefore assess the attack vector as `AV:N`, producing a CVSS v3.1 score of `9.8` rather than `8.8`

These findings allow for two possible interpretations:

1. if these parser changes are Zyxel's patch for CVE-2026-7273, then the patch is incorrect, as are the vulnerability description and CVSS
2. if these changes address a different vulnerability, then the GreyNoise-documented exploitation represents a different vulnerability; in this case, CISA's association of that activity with CVE-2026-7273 would be incorrect

In either case, the vulnerability described in the current advisory is present in all ten of the firmware releases that were advertised as fixes.

## DETAIL: Required remediation
Ensure that `g_count < 140` before deriving an entry address or copying input, bound parameter names and values up to a maximum of 511 bytes. Do not allow negative values for `g_count`. Full RELRO should also be enabled to ensure that resolved GOT entries are read-only.

## DETAIL: Disclosure timeline
| Disclosure activity | Date |
| --- | --- |
| Zyxel publishes its CVE-2026-7273 advisory and fixed releases | 2026-06-16 |
| GreyNoise publishes evidence of exploitation in the wild | 2026-09-21 |
| CISA adds CVE-2026-7273 to the KEV catalog | 2026-09-21 |
| BINARLY confirms that all ten fixed releases remain affected | 2026-09-28 |
| Zyxel PSIRT is notified | 2026-09-29 |
| Zyxel confirms the new vulnerability and reserves CVE-2026-107441 | 2026-10-11 |
| Zyxel [releases a fix](https://community.zyxel.com/en/discussion/34420/switch-gs1900-series-v2-90-patch-3-firmware-release) for CVE-2026-107441 | 2026-10-22 |
| Zyxel publishes an advisory on CVE-2026-107441 | 2026-11-03 |
| BINARLY public disclosure | 2026-11-03 |

## DETAIL: Acknowledgements
**BINARLY REsearch team**

## DETAIL: References
- [Zyxel security advisory for CVE-2026-7273](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026)
- [GreyNoise: Open Season on Kapibala](https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation)
- [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273)
