# Inverted claims: the defect class that reads perfectly and says the opposite

Distinct from a hallucinated fact — the source *is* cited, *is* on-topic, and the
composed sentence is fluent. The polarity is just backwards. Fluency is why these
survive composition: nothing looks wrong.

**2026-08-08 run, one entry produced two in three sentences** (macOS Screen
Sharing, from a researcher's informal blog post):

| Composed | What the source actually says |
|---|---|
| "SIP does not block that path" | "It would be perfect if it could bypass SIP. **That one it doesn't do.**" — the "doesn't care" remark was about **TCC**, a different control |
| "arbitrary file read **and write as root**" | "download any file" — read only; the root claim belonged to a *different* team's bug |
| "Apple's **26.6** release patched it" | the string `26.6` appears **0 times**; the post says only "This Monday Apple's Security Bulletin" |

Root cause: two adjacent controls (SIP/TCC), two adjacent researchers' bugs, and
a version number supplied from context rather than the page. Informal prose —
jokes, asides, second-person — is the high-risk shape; the claim you want is
often a clause inside a sentence about something else.

## Countermeasure that works

`grep -o -i "\bSIP\b" / "\bTCC\b"` etc. for **every control name, privilege level
and version string** before writing the sentence — the same literal-substring
discipline v3.30 mandates for `evidence[]` quotes, applied to negations. If a
version number is in your draft, it must be `grep`-able on the page.

Both were caught by verifier iteration 1 and both were real. Related:
`verifier-findings-are-evidence.md` — test findings before applying, but
polarity findings on informal sources have run near 100% true here.
