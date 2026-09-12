## Narrative Consistency Checker

Detects when the candidate tells different versions of key narratives across companies. Borrowed from Minutes' consistency report pattern (topic normalization + conflict detection).

**Tracked narratives (check these across Interview Loop notes and Score History deployment notes):**

| Narrative | Why it matters |
|-----------|---------------|
| "Why leaving" | Different framings are fine. Contradictory framings are not. "Looking for growth" at Company A and "my company is failing" at Company B creates risk if the two interviewers ever talk. |
| "Timeline / urgency" | "I'm flexible" at one company and "I have a hard deadline" at another is a problem if both reach offer stage simultaneously. |
| "Comp expectations" | Different anchoring strategies per company are fine. Contradicting your current comp is not. |
| "Why this company" | Should be genuinely different per company. Flag if the same generic answer appears verbatim. |
| "Career narrative" | The thread connecting your past roles should be consistent even if emphasis shifts per audience. |

**Detection logic (adapted from Minutes):**
1. After each `round` or `feedback` that captures interview content, extract the candidate's answers to the tracked narrative questions.
2. Normalize: lowercase, remove filler, extract core claim.
3. Compare against prior entries for the same narrative across other companies.
4. If the core claim contradicts a prior version (not just differs in emphasis), flag it.

**Output (surfaced in `progress` and `sync`):**
```
Narrative consistency check:
- "Why leaving": Consistent across Crux, Interface AI, DoorDash (growth framing)
- "Timeline": INCONSISTENT -- told DoorDash "next several weeks" (Mar 26) but told Interface AI "no specific deadline" (Mar 27). If both reach offer stage, reconcile this.
- "Comp expectations": Not yet captured at enough companies to check.
```

**When NOT to flag:**
- Different emphasis for different audiences is fine ("I'm excited about AI" at one company, "I'm excited about fraud" at another)
- Evolving narratives over time are fine (your "why leaving" may genuinely change as the search progresses)
- Only flag when the same narrative contains contradictory factual claims

**Integration:**
- `round` Phase 7: After all state writes, run a silent consistency check against the tracked narratives. Only surface if a contradiction is found.
- `progress`: Include a "Narrative Consistency" section when 3+ companies have interview data.
- `sync`: Include contradictions in drift check output.

---
