# Preflight ran on a stale clock AND a stale clone

At container boot this fire's `date -u` returned **2026-08-16T13:13:24Z** and its
first `git fetch origin main` advanced only to `b77d651` (the 2026-08-16T0411Z
intel run). Both were wrong. Ground truth, established mid-run from GitHub's
HTTP `Date` header and a second `git fetch`:

- true time at re-anchor: **2026-08-24T09:02Z** (container uptime was 0 min at
  that point, so the boot clock was unsynced and NTP corrected it ~15 min in)
- true `origin/main`: **8238738**, carrying run records through
  `2026-08-24T0110Z-weekly` — eight further fires the first fetch could not see

Consequences for this fire, and what was redone:

- `run_id` was `2026-08-16T1313Z-audit`; re-anchored to `2026-08-24T0902Z-audit`.
- the audit window was computed as 168 h ending 2026-08-16; the true window is
  2026-08-09T13:15:57Z → 2026-08-24T09:02Z (~355 h / 14.8 d, inside the 21-day cap).
- the first inventory saw 81 in-window entries; it was missing every entry from
  2026-08-17 onward.
- the five truth batches B1-B5 that had already returned are **valid and kept** —
  they verified real published entries against primary sources, and the wrong
  window label does not affect a truth check. They cover the 2026-08-09 →
  2026-08-16 slice of the window.
- the three coverage sweeps G1-G3 that had already returned swept with
  `window_hours: 168` ending 2026-08-16, so they are **valid for that slice only**
  and are re-run for 2026-08-16 → 2026-08-24.

For a moment this looked like an 8-day pipeline outage. It was not; no operator
notification was sent for it.
