import re
def edit(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        if isinstance(old, re.Pattern):
            assert len(old.findall(s)) == 1, (path, old.pattern[:70])
            s = old.sub(new, s)
        else:
            assert s.count(old) == 1, (path, s.count(old), old[:70])
            s = s.replace(old, new)
    open(path, "w").write(s)

CPHP = "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
CVCS = "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t"
edit("entries/2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes.md", [
    ("For Expressway the PHP fix is 15.5.21, while the release Cisco names for the unauthenticated root command execution on clustered units, CVE-2026-76466, is X15.5.20 ([Cisco PSIRT, 2026-10-21](%s))." % CVCS,
     "For Expressway the PHP fix is 15.5.21 ([Cisco PSIRT, 2026-10-27](%s)), while the release Cisco names for the unauthenticated root command execution on clustered units, CVE-2026-76466, is X15.5.20 ([Cisco PSIRT, 2026-10-21](%s))." % (CPHP, CVCS)),
    ("the fixed releases the table names; an Expressway already upgraded to X15.5.20 for the clustered-device flaw is not listed as fixed for these flaws, so apply the bug record's workaround until 15.5.21 is installed ([Cisco PSIRT, 2026-10-27](%s))." % CPHP,
     "the fixed releases the table names ([Cisco PSIRT, 2026-10-27](%s)); an Expressway already upgraded to X15.5.20 for the clustered-device flaw ([Cisco PSIRT, 2026-10-21](%s)) is not named as fixed in the PHP table, which lists only 15.5.21 (an inference from the table, not a Cisco statement), so apply the bug record's workaround until 15.5.21 is installed ([Cisco PSIRT, 2026-10-27](%s))." % (CPHP, CVCS, CPHP)),
    ("**Exposure:** every Expressway Series and Expressway Select unit below 15.5.21 and every Duo Access Gateway below 3.2.0; the advisory names no version-check command, no component that runs the PHP and no affected-version ranges; its bug records",
     "**Exposure:** every Expressway Series and Expressway Select unit and every Duo Access Gateway not on a release Cisco lists as fixed (15.5.21 and 3.2.0), since Cisco gives no affected-version ranges; the advisory names no version-check command and no component that runs the PHP; its bug records"),
])

HPE = "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
edit("entries/2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171.md", [
    ("without the hotfix; guest portals are reachable by users by design, and HPE names them next to the management interfaces as the surfaces to remove from public access ([HPE Networking, 2026-10-23](%s))." % HPE,
     "without the hotfix; HPE asks customers to consider removing guest portals and all management interfaces from public access ([HPE Networking, 2026-10-23](%s))." % HPE),
    ("and treat any guest portal or management interface that was reachable from untrusted networks as the first to restrict; the guest portal is the first surface to take off public networks ([HPE Networking, 2026-10-23](%s))." % HPE,
     "and take any guest portal or management interface reachable from untrusted networks off public access, as HPE asks ([HPE Networking, 2026-10-23](%s))." % HPE),
    (re.compile(r"The flaws are in the PHP runtime and\n  are covered by the entry listed under references\. The bulletin is inconsistent"),
     "The flaws themselves are in the PHP runtime. The bulletin is inconsistent"),
])

edit("entries/2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27.md", [
    (re.compile(r"the two flaws themselves are in the PHP runtime and are\n  covered by the entries listed under references\. Neither"),
     "the two flaws themselves are in the PHP runtime. Neither"),
])

W = "https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke"
edit("entries/2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud.md", [
    ("as a spokesperson of the Touring Club Schweiz (TCS) confirmed (translated from German)",
     "as a spokesperson of the Touring Club Schweiz (TCS) confirmed on Monday at the request of the news agency Keystone-SDA (translated from German)"),
    ("wie ein Sprecher des Touring Club Schweiz (TCS)\"", "wie ein Sprecher des Touring Club Schweiz (TCS) am Montag auf Anfrage der Nachrichtenagentur Keystone-SDA bestätigte\""),
])

edit("entries/2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi.md", [
    ("Bun 1.0.21 to before 1.4.4; Envoy v1.39.2,", "Bun 1.0.21 to before 1.4.4; Istio before 1.29.9, 1.30.6 and 1.31.2; Envoy v1.39.2,"),
    ("Ubuntu brotli before the fixed packages\"", "Ubuntu, Debian and Alpine brotli packages and the Ruby brotli gem before the fixed builds listed\""),
])
