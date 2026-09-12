## "No Gap Without An Opening" Rule

A gap can only be logged in coaching output if the interviewer created an opening for the candidate to demonstrate the missed skill. An **opening** is one of:
- (a) A question that invited engagement with the skill dimension
- (b) A topic the interviewer actively pursued (multiple follow-ups, time investment, explicit interest)
- (c) A known evaluation axis of the round's **actual** format (not the prepped format — per RFV verdict from Step 3.7)

**Three tagging categories** — every item in "Top Gaps to Close" in `analyze` or `round` output MUST carry exactly one of these tags:

- `[CANDIDATE GAP]` — the interviewer created an opening and the candidate failed to take it. This is a real gap. Generates a drill. Feeds Active Coaching Strategy if scope-alignment gate passes. Requires citation to the specific opening in the transcript.
- `[SCOPE BOUNDARY]` — the interviewer did not create an opening for this dimension (did not ask, declined engagement, ran a format that does not test it). Not a candidate failure — a scope limit of the round. Does NOT generate a drill. Does NOT update Active Coaching Strategy. Recorded in output for transparency and future prep intelligence only.
- `[PREP MISMATCH]` — the prep expected an opening to exist, but the actual round did not produce it. Updates **loop prep intel** (future rounds with this company or interviewer type should expect the actual format). NOT candidate coaching. Does NOT generate a drill.

**Enforcement:**
- Untagged items in "Top Gaps to Close" are not permitted. The coach must tag every item before writing the output.
- An item tagged `[CANDIDATE GAP]` must include a citation to the specific opening — quote, question, or behavior — that created it. If no opening can be cited, the item is mistagged and must be re-classified as `[SCOPE BOUNDARY]` or `[PREP MISMATCH]`.
- Items tagged `[SCOPE BOUNDARY]` omit the Drill field in output. Items tagged `[PREP MISMATCH]` omit the Drill field and include a "Loop intel update" field instead.
- Only `[CANDIDATE GAP]`-tagged items progress into the Post-Scoring Decision Tree priority stack (`analyze.md` Step 12).

**Principle:** The coach's job is to score what happened, not what was expected to happen. Manufactured gaps from format-reality divergence are actively harmful in rejection scenarios because they calcify wrong stories about why a round didn't convert, misdirecting Active Coaching Strategy and compounding the error across future rounds.

---
