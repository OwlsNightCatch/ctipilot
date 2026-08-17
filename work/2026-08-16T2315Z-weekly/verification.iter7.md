**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-17T01:40:25Z · ended_at=2026-08-17T01:44:10Z · duration_seconds=225

## Verification report — 2026-08-16T2315Z-weekly (iteration 7)

Scoped pass as tasked: (1) verify iteration 6's two fixes against their sources, (2) sweep the last three
iterations' remediations for the partial-application class, (3) verdict. Did not re-derive sourcing,
calibration, coverage or quote verbatimness beyond the entries touched.

### Fix verification (iteration 6)

**Fix 1 — MyDr ministerial title.** Half correct. Fetched Notes from Poland: the article calls Gawkowski
"digital affairs minister", so dropping "Deputy Prime Minister" is right and the title now matches the
outlet cited on it. But the same clause still attributes the ~19 million figure to him, and the article does
not. See F1.

**Fix 2 — macOS four-day interval.** Correct and verified. Calif's post (published 2026-08-10, matching the
source record's date) carries the in-post timeline entry "Sat Aug 8 (APAC) We start on the 26.6.1 diff, and
have a working exploit about four hours later", two independent pre-auth remote root exploits, ~40,000
internet-exposed Macs. NCSC-NL 2026-0280's revision table (saved capture) carries 07-08-2026 and 12-08-2026.
8 August to 12 August is four days. Every macOS timeline mention agrees: title ("days or hours"), headline
("two more inside a week" / "four hours"), summary (6 Aug patch, 12 Aug confirmation, 8 Aug build, "four days
before that confirmation"), body ("out-of-band macOS update of 6 August", "Four days after that"), and the
sibling roll-up's "confirmed exploitation followed six days later" (6 Aug → 12 Aug, the other clock, correct).
One residual readability issue, advisory only — F3 below.

### Citation does not support the claim

**F1 — `weekly-w33-compromised-party-was-not-the-notifying-party`: the 19 million figure is attributed to a
named minister the cited source never has stating it.**

Body (line 113): *"The following day Poland's digital affairs minister, Krzysztof Gawkowski, put the stolen
database at almost 19 million people ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/))"*.

Fetched this iteration. Notes from Poland attributes no number to Gawkowski. Every sentence quoting him:
"We are dealing with one of the largest incidents in Poland's history"; that "there is no indication we are
dealing with an external attack…from Russia or any other country"; that it is "very likely" cybercriminals
are behind it, with an "uncompromising" response pledged; and his advice to check the government database and
lock the PESEL number. The number appears twice, in neither case from him: the article's own opening framing
("The personal data of almost 19 million people, including medical information, has been compromised") and the
attackers' claim relayed by Zaufana Trzecia Strona ("The alleged perpetrators…claimed to have accessed the data
of around 18.8 million people").

This is iteration 5's citation-swap applied to the title but not to the figure it sits on — the same
partial-application shape iteration 6 caught one clause earlier. It recurs in two further places in the same
entry, so the fix is three-part:
- summary (lines 12–13): *"confirmed a criminal intrusion the government put at nearly 19 million people"*
- sourcing_note (lines 85–87): *"The MyDr scale figure is a government minister's statement rather than a
  company or forensic finding and is attributed as such"*

Cheapest correct repair: de-attribute in all three ("reported at almost 19 million people, with the alleged
perpetrators claiming 18.8 million"), and rewrite the sourcing_note sentence to say the figure is press framing
over an attacker claim rather than a company or forensic finding — which is a stronger caveat than the one it
currently makes, not a weaker one. Attributing it to Gazeta Prawna instead is only valid if that page is
confirmed to carry the minister stating a number; it was not fetched this iteration.

### Quantifier without source

**F2 — same entry: the displaced-duty count of three is refuted by the entry's own sourcing_note, which
enumerates two.**

Asserted three times over the six-disclosure set:
- headline: *"in three of them the notification duty landed where the intrusion did not"*
- summary: *"in three of them that displaced the duty to tell the affected people onto organisations that had
  no facts to write"*
- body (line 111): *"In three of them that separation ran all the way to the notification"*

The entry's own sourcing_note (lines 87–89): *"The notification duty is displaced in the MyDr and CEVA cases
and, through CEVA, for bol.com; in the DGFiP, Żabka, Retelit and ACRO cases the compromised body is also the
notifying body."* Four of six are explicitly on the not-displaced side, leaving two. The third case is bol.com
— which iteration 5 removed from the disclosure count precisely because it is "a downstream notification
arising from the CEVA intrusion rather than a separate disclosure" (run record, iteration 5, F14). The seven→six
correction was applied to the disclosure count and not to the count derived from it.

Fix: two in all three places, or scope explicitly ("in two of them… and, downstream of the CEVA case, for
bol.com as well"). The body's supporting prose needs no change — it already narrates exactly MyDr and CEVA.

### Editorial / less-is-more flags (advisory)

**F3 — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: the body's four-day interval has no visible
anchor date.** Body: *"Four days after that, NCSC-NL revised its advisory…"*. The antecedent sentence ends in
the citation label "[Calif, 2026-08-10]", so a reader computing off the body alone lands on 14 August, against
the "2026-08-12" label on the next citation. The summary states the anchor ("in about four hours on 8 August")
but the body does not — iteration 5's remediation note said the date would be stated explicitly, and it was
applied to one half of the entry. No fact is wrong; leave it or spend one clause: "Four days after that build,
on 12 August, NCSC-NL revised its advisory". Advisory.

### Coverage note

No new coverage gap surfaced. The sweep also re-checked the derived counts the earlier iterations repaired
and found them internally consistent: the roll-up's eight newly exploited / catalogued reconciles with its own
enumeration (three in the lead paragraph plus five), its eight-with-no-fix reconciles with its bullet
(ShieldBreak + three FreeBSD + GeoServer + three of five NatJack), its "two within seventy-two hours" agrees
between title, headline and body, and the ETSI entry's 17 categories agree between frontmatter, headline and
prose. Both remaining defects are in one entry, and both are single-line edits.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

### Findings summary (machine-readable)

```yaml
# see work/2026-08-16T2315Z-weekly/verification.iter7.findings.yaml
```
