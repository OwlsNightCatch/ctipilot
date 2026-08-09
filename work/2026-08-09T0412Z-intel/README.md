# Forensic surface for this run

Every entry in this run was composed against a full body fetched in the Phase 4
deep read, and every `evidence[]` quote plus every quoted string in the entry
bodies was checked as a literal contiguous substring of that fetched text before
the entry was written.

Those fetched bodies are **not** in git: `.gitignore` excludes `work/**/*.txt`,
and the 5.9 MB CERT Polska PDF was removed from the working tree after
extraction rather than committed. What is kept here is the run's own record —
the research findings, both verification reports, the triage dispositions, the
URL-liveness ledger, the per-agent source allocations and the timestamps.

To reproduce a quote check, re-fetch the URL from the entry's `sources[]` and
run a literal substring search against the extracted text. Two transport notes
worth carrying forward:

- The CERT Polska follow-up report (19 pages) could not be read usefully by
  local zlib text extraction — it truncated sentences mid-clause and would have
  produced a false-green quote check against a corrupted copy. The reader
  transport returned it intact; that is the text the deep dive was written from.
- `raw.ghsa-metabase.json` records the OSV miss for GHSA-vwf4-m7j8-wcjf, which
  is why the Metabase entry cites that advisory only through BleepingComputer's
  reproduction of it rather than directly.
