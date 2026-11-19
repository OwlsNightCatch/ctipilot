FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:28],a[:60],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
SY="https://www.security.com/threat-intelligence/power-management-software-attack-vector"
# ---------- Airlock
a=E('entries/2026-11-19/airlock-gateway-cve-2026-19707-smart-form-protection.md')
a.rep("overflows a heap buffer in the Smart Form Protection entity decoder and can cause","overflows a buffer in the Smart Form Protection feature and can cause")
a.rep("can overflow a heap buffer in the Smart Form Protection feature","can overflow a buffer in the Smart Form Protection feature")
a.rep("list the same fix as a buffer overflow when decoding HTML entities (","list a fix for a buffer overflow when decoding HTML entities in the same releases, without a CVE id (")
a.rep("regions: [global, switzerland]","regions: [global]")
a.rep('entities: []','entities: ["product:airlock-gateway"]')
a.rep("The finders and any technical write-up are not named in the sources read.","The finders and any technical write-up are not named in the sources read, and the documentation pages carry no dateline, so their citations carry the retrieval date.")
a.save()
# ---------- CyberPower
c=E('entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc.md')
c.rep("techniques: [T1072, T1059.003, T1059.001, T1105, T1003.003, T1574.001]","techniques: [T1072, T1059.003, T1059.001, T1105, T1140, T1620, T1003.003, T1574.001]")
c.rep('entities: ["incident:cyberpower-powerpanel-dc-intrusion-2026-11"]','entities: ["incident:cyberpower-powerpanel-dc-intrusion-2026-11"]')
c.rep("powershell.exe and then the implant upnpcont.exe ([Symantec","powershell.exe and then the implant ([Symantec")
c.rep("and then side-loaded the implant with upnpcont.exe and atl.dll ([Symantec","and then side-loaded the implant, a signed-looking binary that loads a DLL of the attacker's choosing ([Symantec")
c.rep("a DLL named atl.dll beside upnpcont.exe marks the side-loaded implant (","an unexpected DLL beside a binary launched from the SYSTEM profile path marks the side-loaded implant (")
c.rep("pp?????.cmd files in extcmd, inbound requests","every script in extcmd, not only the pp?????.cmd names (Symantec also saw ifm.cmd to ifm4.cmd staged there), certutil downloads and decodes, curl downloads and powershell -ep bypass loading .NET code in memory, inbound requests")
c.rep("look for pp?????.cmd scripts and for cmd.exe or powershell.exe started under ppbed.exe; where either is found,","look for scripts that differ from the product defaults and for children of ppbed.exe that are not shutdown or notification routines with no preceding power event; where either is found,")
c.rep("**Defender takeaway:** treat PPB hosts as privileged execution surfaces; where the audit finds a deviation,","**Defender takeaway:** treat PPB hosts as privileged execution surfaces: restrict TCP port 3052 to named administrator hosts, change the default administrator password and keep PPB patched, since CISA names 4.10.1 as the fixed build for its 2024 advisory ([Symantec, 2026-11-18](%s); [CISA, 2024-05-02](https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)); where the audit finds a deviation,"%SY)
c.rep("Symantec does not cite CISA's advisory.","Symantec does not cite CISA's advisory, and the vendor and documentation pages carry no dateline, so their citations carry the retrieval date.")
c.save()
# ---------- tcherber
t=E('entries/2026-11-19/tcherber-access-broker-fortigate-sonicwall-vpn-ldap-sweep.md')
t.rep("without mentioning VPN access (","without mentioning VPN access brokerage (")
t.rep("VPN gateway logs for successful logins by default-named accounts and for sustained sessions from one source that reconnect about every 30 seconds;","VPN gateway logs for successful logins by default-named accounts and for repeated reconnect attempts from one source about every 30 seconds, the interval of the FortiGate client's retry loop;")
t.rep("search VPN logs since May 2026 for sustained sessions by such accounts that reconnect about every 30 seconds and are followed by a broad LDAP enumeration from the VPN address pool,","search VPN logs since May 2026 for logins by such accounts that are followed by a broad LDAP enumeration from the VPN address pool,")
t.save()
print('FAIL',FAIL)
