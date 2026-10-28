import yaml, json, re
W = "work/2026-10-28T0256Z-intel"
P = f"{W}/records/run_notes.md"
s = open(P).read()
def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)
sub(re.search(r"- CVE-2026-48356 \(Adobe Commerce and Magento upload flaw, KEV 2026-10-27\): NOT COVERED.*?\n", s).group(0),
    "- CVE-2026-48356 (Adobe Commerce and Magento upload flaw, KEV 2026-10-27): NOT COVERED, shipped as a notable entry. It was first held back as borderline (CISA's listing and Adobe's bulletin give no exploitation detail, no constituency nexus); the verifier then found Sansec's PolyShell reporting, which the CVE record itself links: attacks since 2026-03-19, a mass wave on 2026-03-30 and the fix timeline (2.4.9 on 2026-05-12, supported-line backport 2026-07-14). The entry now rests on Sansec, Adobe and CISA together, and the store already carries four Adobe Commerce or Magento entries.\n")
sub("- Adobe Commerce CVE-2026-48356: the exploitation rests on CISA's listing alone, confidence medium, and the vendor's bulletin disagrees.",
    "- Adobe Commerce CVE-2026-48356: the exploitation history rests on Sansec's own telemetry and scans (a security vendor) with CISA's listing and Adobe's bulletin; confidence high, reliability B.")
sub("- Contradiction: HPE HPESBNW05171 names",
    "- Contradiction: Adobe's bulletin APSB26-73 (2026-07-14, updated 2026-08-11) says no exploits are known for CVE-2026-48356, while Sansec reports attacks since 2026-03-19 and CISA lists the flaw as exploited; Adobe's CVE record scores it 9.3 where the bulletin says 9.6. The entry states both.\n- Contradiction: HPE HPESBNW05171 names")
open(P, "w").write(s)

fnd = yaml.safe_load(open(f"{W}/verification.iter3.findings.yaml"))
rem = [
 "fixed: Sansec's PolyShell advisory, the mass-wave report and the October campaign report are sources; summary, body, sourcing note, verification (multi-source), rating (B2) and confidence are rewritten and Exposure and Detection use Sansec's specifics",
 "fixed: counts and lists refreshed to the advisory as read on 2026-10-28 (14 released, 6 due) in the title, headline, summary, action, both cves[].fixed, body, takeaway and the 2026-10-28 section, with a 2026-10-28 source record for the JSON",
 "fixed: the PHP entry now says most hotfixes are released and the rest due by 2026-10-30, with no count to go stale",
 "fixed: the Node2Shell fixed list, action and body say six of nine hotfixes are released and three are due on 2026-10-29 and 2026-10-30, with a 2026-10-28 source record",
 "fixed: the 2026-10-27 timeline entries are described as two ETA removals and the 16:40 UTC severity change",
 "fixed: the statement that the bulletin reports no exploitation cites HPE's CSAF record",
 "fixed: mySites.guru is cited for the CVE-to-flaw mapping and Balbooa for the fixes",
 "fixed: the 9.6 versus 9.3 scores and the user-interaction versus anonymous-upload readings are stated in the cvss field and the sourcing note",
 "fixed: see the first finding; Sansec is a source and the entry is rebuilt on it",
 "fixed: Exposure and Detection now carry Sansec's routes, directory, server configurations and compromise checks",
 "fixed: the Cisco Detection line cites CISA's PHP alert and labels the application to Cisco products an inference; the unsupported multipart and crash pattern is removed",
 "fixed: the HPE Detection line is rewritten the same way",
 "fixed: the source-build and ASP.NET Core tarball scope is restored and words were trimmed elsewhere to stay within the bound",
 "declined: the entry's priority and exploited tag still describe the July wave that unpatched sites face; the new section says plainly that nothing in it is reported exploited",
 "declined: left to the audit; unchanged by this run",
 "fixed: the Cisco sourcing note no longer narrates what was not read",
]
assert len(fnd) == len(rem), (len(fnd), len(rem))
fl = []
for f, r in zip(fnd, rem):
    entry = str(f.get("section", "")).split(" (")[0].split(";")[0].strip()
    if not (entry.startswith("entries/") or entry.startswith("runs/")): entry = "whole-run"
    fl.append({"category": f["category"], "code": f["code"], "entry": entry, "remediation": r, "summary": " ".join(str(f["summary"]).split())[:300]})
it = json.load(open(f"{W}/verification_iters.json"))
assert len(it) == 2
it.append({"n": 3, "model": "Sonnet 5.5", "model_id": "claude-sonnet-5-5", "subagent_type": "cti-verification",
           "started_at": "2026-10-28T05:35:25Z", "ended_at": "2026-10-28T06:06:24Z", "duration_seconds": 1859,
           "verdict": "NEEDS_FIXES", "truth": 7, "editorial": 6, "advisory": 3, "claims_in_scope": 330, "claims_checked": 330, "findings": fl})
json.dump(it, open(f"{W}/verification_iters.json", "w"), indent=1, ensure_ascii=False)
print("ok", len(fl))
