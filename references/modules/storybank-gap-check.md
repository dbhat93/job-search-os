## Storybank Gap Check

Pre-interview competency coverage detection. Different from the Gap-Handling Module (which handles real-time in-interview recovery) — this runs *before* the interview to identify coverage holes while there's still time to do something about them.

**When to run:**
- During `prep` (Step 7 — automatically triggered when JD competencies + storybank both exist)
- During `progress` (Storybank Health section — cross-loop view across all active companies)
- On demand during `stories find gaps`

**Story over-use detection (loop-scoped, not global):**

The risk of telling the same story to the same interviewer, or to different interviewers at the same company who compare notes, is categorically different from the risk of telling the same story to different companies. Treat these as two separate checks.

**Loop-scoped overuse (the hard warning, prevents interviewer-facing risk):**
When checking storybank health for a specific upcoming interview, consult `Interview Loops > [Company] > Stories used` (list of stories already deployed in prior rounds at this company).
- If a story appears in any prior round at this company, flag it: "S### was deployed in [Round N] at [Company]. Do not reuse as a round anchor in [next round] unless a different interviewer is present. If the same interviewer may be in the next round, prepare a fresh primary story."
- If the interviewer is confirmed different AND the story wasn't deployed as a round anchor (only as a proof point), it may be safe to reuse. Flag as "reuse allowed, check with candidate."

**Global overuse (the soft signal, tracks candidate delivery staleness, NOT interviewer risk):**
Total Use Count across all companies. Different companies do not share memory. Gabriella at Checkr has no knowledge of what Brian at Plaid heard.
- Use Count 5+: Soft staleness signal only. "S### has been deployed [N] times across the job search. Check your own delivery. Is it still landing with energy, or starting to sound rehearsed? Consider `stories improve S###` to find a fresh angle." Do NOT use this to block deployment at a new company.
- Use Count 8+: Stronger staleness signal. "S### is heavily used in your delivery. Even if interviewers haven't heard it, YOU have told it many times. Watch for energy decay."

**What NEVER triggers an overuse warning:**
- High Use Count alone at a brand-new company with a fresh interviewer loop. Deploy the best story, regardless of global count.
- A story used once at Company A being used once at Company B. That is not overuse. That is normal portfolio rotation.

This check runs during `progress` Storybank Health (global staleness view + per-loop freshness) and `prep` Step 7 (per-loop freshness is the primary check, global staleness is secondary).

**Input required**: JD-derived top competencies (from `decode` or extracted during `prep`) + storybank with Primary/Secondary Skills per story.

**Three severity tiers:**

| Tier | Definition | What to Do |
|------|-----------|------------|
| **Critical Gap** | Top-3 JD competency with zero storybank coverage — no story lists it as primary or secondary | Requires action before the interview |
| **Addressable Gap** | Coverage exists but only weak stories (strength 1–2) — no story can carry this competency on its own | Adapt an adjacent story or prepare a gap-handling pattern |
| **Covered** | At least one story at strength 3+ covers this competency | No action needed; note which story to deploy |

**Critical gap detection — what counts as "top-3 competency":**
A competency qualifies as top-3 if it appears in: (a) the role title or summary, (b) the required qualifications section, or (c) 3+ places in the JD. Decode output makes this explicit — use it if available.

**Timeline-aware routing** (run after triage, before prescribing action):

| Time Until Interview | Critical Gap Action | Addressable Gap Action |
|---------------------|--------------------|-----------------------|
| **3+ weeks** | Build a new story from scratch. Run `stories add` targeting this competency specifically. | Strengthen existing weak story — run `stories improve S###` |
| **1–3 weeks** | Adapt the strongest adjacent story to bridge to this competency. Use Pattern 1 (Adjacent Bridge) as the delivery vehicle. | Drill gap-handling Pattern 1 or 4 under pressure. |
| **< 1 week** | Don't try to build a new story — it won't be polished in time. Prepare Pattern 2 or 3 for delivery. Be ready to be honest about the gap. | Same — drill delivery, not story construction. |

**Cross-loop analysis** (for `progress` Storybank Health):
When multiple active interview loops exist, run the gap check across all of them simultaneously. Surface: (a) competencies that are critical gaps for 2+ companies (highest-leverage fix), (b) competencies covered for all active loops (don't over-prepare these), (c) gaps that are company-specific vs. cross-market (company-specific gaps may be targeting signals).

**Decision rule**: Prep competencies that are critical gaps for ANY active loop — don't wait for a gap to appear in 2+ loops before acting. Prioritize gaps that appear in 2+ loops (highest ROI), then single-loop critical gaps ordered by interview proximity (nearest first).

**Output format** (used by both `prep` and `progress`):

```
