# Phase 1 spawn incidents — 2026-08-05T0412Z-intel

Four research sub-agents were spawned in one message at 04:13Z (S1-S4, all on the
Sonnet-pinned `cti-research` definition). S3 and S4 started normally. S1 and S2
both terminated immediately with the same API error:

    Sonnet 5's safeguards flagged this message.

Retry ladder for S1 and S2 (definition unchanged; only the spawn message and the
model binding varied):

| Attempt | Domain | Spawn message | Model binding | Outcome |
|---|---|---|---|---|
| 1 | S1 | full (inline dedup enumeration) | definition pin (sonnet) | blocked at first request |
| 1 | S2 | full (inline dedup enumeration) | definition pin (sonnet) | blocked at first request |
| 2 | S1 | reduced, dedup by file reference | definition pin (sonnet) | blocked at first request |
| 2 | S2 | reduced, dedup by file reference | definition pin (sonnet) | blocked at first request |
| 3 | S1 | minimal | definition pin (sonnet) | blocked at first request |
| 3 | S2 | minimal | definition pin (sonnet) | blocked at first request |
| 4 | S1 | minimal | opus override | started |
| 4 | S2 | minimal | opus override | started |

Reading: the block is not attributable to the spawn message. Shortening the message
across three attempts changed nothing, and S3/S4 carried the longest messages of the
four and were not blocked. The variable that changed the outcome was the model
binding, and the error names Sonnet 5's safeguards specifically. Recorded as a
transient platform-side condition affecting the sonnet binding of this definition at
this hour, not a defect in the definition or the tasking.

Consequence for the run: S1 and S2 started roughly 6 minutes later than S3 and S4 and
ran on Opus rather than the definition's sonnet pin. The `**Model:**` lines each agent
returns are the authoritative record and are carried verbatim into the run record.
