# State changes the main agent applies (collected from worker reports)

- repair-4: cves_seen last_seen 2026-10-21 for CVE-2026-35616, CVE-2026-48558; title refresh suggestions for 35616, 48558, 46817 in repair-4.md
- repair-2: no registry or cves_seen change required (optional last_seen bump CVE-2026-42945, CVE-2026-42897: no cves[] record changed, skip)
- repair-2 residuals for the main agent (own entries): Exchange 05-18 headline 157 chars and `**Detection.**` label; Japan 09-12 2026-09-13 section contradicts the main analysis (minister said known) and sourcing_note says "this entry's frontmatter"; PAN-OS 05-12 and nginx 05-15 lack a Defender takeaway line
- repair-3: no registry or cves_seen change
- DONE main: Exchange 05-18 headline 157 -> 116 chars, `**Detection.**` -> `**Detection:**`, record amended (+headline)
- DONE main: Japan 09-12 2026-09-13 section and sourcing_note fixed (Piyolog 2026-09-11 line 45 confirms "known beforehand"), record amended; nginx 05-15 Defender takeaway added (nginx.org 1.30.1+/1.31.0+, depthfirst named-capture workaround), record amended. PAN-OS 05-12 takeaway gap: carried forward (no record this fire)
- repair-1: cves_seen last_seen 2026-10-21 for CVE-2026-42321, CVE-2026-43284, CVE-2026-43500; no registry change
- repair-5: cves_seen last_seen 2026-10-21 CVE-2026-45585, CVE-2026-45586 (+ title) DONE; registry summaries campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac and incident:pwn2own-berlin-2026 corrected from truth-T1 DONE
- fold: 2026-05-25/large-scale-clickfix... into ghost-cms survivor DONE; legacy --done for YellowKey, NE, roundup, twin DONE (402 pending locally)
- repair-5 residuals outside batch: 2026-06-11/rogueplanet... gives GreenPlasma as CVE-2026-50507 (MSRC: BitLocker bypass); 2026-05-19/chaotic-eclipse...miniplasma lacks the 2026-06-09 fix
