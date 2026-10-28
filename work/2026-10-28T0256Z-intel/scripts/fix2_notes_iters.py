import yaml, json, re
W = "work/2026-10-28T0256Z-intel"
# ---- run notes
P = f"{W}/records/run_notes.md"
s = open(P).read()
def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)
sub("Five new entries (Cisco PHP2Shell advisory, HPE ClearPass PHP2Shell, Balbooa Gridbox SQL injections, ARA-Region Lyss-Limpachtal, DeadTag) and eight changelog records.",
    "Five new entries (Cisco PHP2Shell advisory, HPE ClearPass PHP2Shell, the CISA-listed Adobe Commerce upload flaw CVE-2026-48356, ARA-Region Lyss-Limpachtal, DeadTag) and nine changelog records.")
sub(re.search(r"- borderline-drop: CVE-2026-48356.*?\n", s).group(0),
    "- CVE-2026-48356 (Adobe Commerce and Magento upload flaw, KEV 2026-10-27): NOT COVERED, shipped as a short notable entry. CISA is the only exploitation source and gives no detail, Adobe's bulletin APSB26-73 (2026-07-14, updated 2026-08-11) still says no exploits are known, and the fix is three months old. It was first held back as borderline (no constituency nexus for an e-commerce platform); the store already carries four Adobe Commerce or Magento entries, so the KEV listing is covered like the others.\n")
sub(re.search(r"- Borderline include: Balbooa Gridbox.*?\n", s).group(0),
    "- Borderline include: Balbooa Gridbox CVE-2026-102788 and CVE-2026-102789, an unauthenticated read-side SQL injection with no exploitation report, folded into the July Gridbox entry as an `update` record (the store's pattern for later Gridbox batches, which moved its action to 2.20.4.2). Kept under the \"otherwise\" limb of PD-11 (b), the leg that holds being a two-file fix diff that hands over the technique; the July Gridbox flaws were exploited, these two are not reported exploited, and no Swiss nexus is established.\n")
sub("IDC Frontier: the final report names the cause,", "IDC Frontier: the seventh report names the cause,")
sub("- Cisco, HPE ClearPass, Balbooa (with mySites.guru): vendor first-party; Cisco and HPE carry `cvss: n/a` or the vendor's score only.",
    "- Cisco, HPE ClearPass, Balbooa (with mySites.guru, on the Gridbox update): vendor first-party; Cisco and HPE carry `cvss: n/a` or the vendor's score only.\n- Adobe Commerce CVE-2026-48356: the exploitation rests on CISA's listing alone, confidence medium, and the vendor's bulletin disagrees.")
open(P, "w").write(s)

# ---- iteration 2 record
fnd = yaml.safe_load(open(f"{W}/verification.iter2.findings.yaml"))
rem = [
 "fixed: the estimated-dates and FAQ clause cites the advisory page again; the JSON stays on the released-builds clause",
 "fixed: the estimated-dates clause cites the advisory page",
 "fixed: the 2026-10-27T05:15:00Z section is restored verbatim from the earlier fire; this run's changes stay in its own record",
 "fixed: the 206 figure cites the seventh report in the main analysis and the takeaway",
 "fixed: each fix release carries its own advisory's citation",
 "fixed: the clustered-device flaw cites the VCS advisory and the point is labelled an inference from the PHP table",
 "resolved by the F7 fold: the stand-alone Balbooa entry became an update record on the July Gridbox entry, where the allowlist and permission-check clauses cite Balbooa",
 "fixed: the advisory is cited after the first clause",
 "fixed: the guest-portal clause states only what HPE says",
 "fixed: the repeated first-surface clause is cut",
 "fixed: exposure is every unit not on a release Cisco lists as fixed, since Cisco gives no ranges",
 "fixed: the original quotation and its translation now carry the Keystone-SDA request wording",
 "fixed: folded into the July Gridbox entry as an update record, as the store did for earlier Gridbox batches; its summary, actions and sourcing note now point to 2.20.4.2 and the stand-alone entry, never published, was removed",
 "fixed: the Istio ranges and the Debian, Alpine and Ruby gem builds are in cves[].affected",
 "fixed: CVE-2026-48356 ships as a short notable entry (CISA listing, Adobe's July fix, the vendor and CISA disagreement)",
 "fixed: the notes carry borderline-drop lines for Moldova, Tailworm, Yoba and the other flagged slice items",
 "fixed: the sourcing notes name the PHP runtime without pointing at store entries",
 "declined: left to the audit; the entry shrank by 21 words this run",
 "fixed: the two September entries are in references[], a cited clause says the kit has appeared in other campaigns and affected_products names Apple iOS",
 "fixed: the notes say seventh report",
]
assert len(fnd) == len(rem), (len(fnd), len(rem))
fl = []
for f, r in zip(fnd, rem):
    entry = str(f.get("section", "")).split(" (")[0].split(";")[0].strip()
    if not entry.startswith("entries/") and not entry.startswith("runs/"):
        entry = "whole-run"
    fl.append({"category": f["category"], "code": f["code"], "entry": entry, "remediation": r, "summary": " ".join(str(f["summary"]).split())[:300]})
it = json.load(open(f"{W}/verification_iters.json"))
assert len(it) == 1
it.append({"n": 2, "model": "Sonnet 5.5", "model_id": "claude-sonnet-5-5", "subagent_type": "cti-verification",
           "started_at": "2026-10-28T04:47:34Z", "ended_at": "2026-10-28T05:18:09Z", "duration_seconds": 1835,
           "verdict": "NEEDS_FIXES", "truth": 12, "editorial": 4, "advisory": 4, "claims_in_scope": 280, "claims_checked": 280, "findings": fl})
json.dump(it, open(f"{W}/verification_iters.json", "w"), indent=1, ensure_ascii=False)

# ---- builder counters
B = "work/2026-10-28T0256Z-intel/scripts/build_run_record.py"
b = open(B).read()
assert "'entries_updated':8" in b
b = b.replace("'entries_updated':8", "'entries_updated':9")
b = b.replace("'updated_entry_ids':['2026-10-21/php-critical", "'updated_entry_ids':['2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave','2026-10-21/php-critical")
open(B, "w").write(b)
print("ok", len(fl))
