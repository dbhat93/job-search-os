# sync — Coaching State Consistency Check

Detects drift between `coaching_state.md` and the candidate's actual search state. Two modes: a lightweight version runs automatically at every session start (see COACH.md → Sync Drift Check); the full audit runs on demand when `sync` is invoked explicitly.

Use `sync` when:
- The search has been moving fast (multiple rounds advancing or closing simultaneously)
- The candidate hasn't run a session in 2+ weeks and state may be stale
- Something "feels off" — a recommendation doesn't make sense given what's happening
- Before running `strategy` — clean state is a prerequisite for accurate search analysis

---

## Session-Start Lightweight Check (automatic — defined here, run from COACH.md)

**Two checks only.** Run silently after Schema Migration and Timeline Staleness checks. Surface only findings that require candidate input.

**Check 1 — Loop-Outcome Drift**
For each Outcome Log entry with a terminal result (rejected / offer / withdrawn): confirm the corresponding Interview Loop's Status field reflects it. If a loop still shows "Interviewing" or "Active" when the outcome is terminal: update the Loop Status silently to match and note the correction in Coaching Notes. No candidate input needed — this is a mechanical fix.

**Check 2 — Passed Next-Round Dates**
For each Interview Loop with a "Next round" date that passed more than 7 days ago: check whether a corresponding new Outcome Log entry or a new completed round exists. If not: surface this as the first thing in the session (before the standard greeting): "I noticed your [Company] [Round] was scheduled for [date] — [N] days ago. Did that happen? Run `debrief` to capture it while impressions are still useful, or `feedback` to log the outcome." Do not guess the result. Wait for the candidate to respond before making any other recommendation.

---

## Full Sync Audit

### Step 1: State Assembly

Read `coaching_state.md` in full:
- Profile (deadline, target roles, coaching mode)
- Interview Loops — all entries (status, rounds completed, next round, stories used, concerns)
- Outcome Log — all entries (result, date)
- Storybank — index (use counts, last used, any retire flags)
- Active Coaching Strategy (primary bottleneck, current approach, last updated)
- Session Log (count recent sessions, last session date)
- Search Strategy (priority stack, 2-week action plan, if exists)

Before running the audit, ask one question: "Before I check everything — any news since we last spoke? New outcomes, interviews scheduled, or loops opened or closed?" Wait. Incorporate any updates before proceeding.

### Step 2: Loop-Outcome Audit

Cross-reference every Interview Loop entry against the Outcome Log:

| Condition | Flag |
|-----------|------|
| Loop shows "Interviewing/Active" + terminal outcome exists in Outcome Log | **Closed-loop drift** — Loop status is stale. Fix: update Status to match outcome. |
| Outcome Log shows "pending" + loop active + no round update in 4+ weeks | **Zombie loop** — Flag for candidate confirmation: "This loop has been pending for [N] weeks with no movement. Is it still alive? If not, log the outcome via `feedback`." |
| Outcome Log shows "advanced" + loop shows no corresponding new round | **Missing round entry** — "You have an 'advanced' outcome for [Company] but the loop doesn't show a new round. What's the current stage?" |
| Loop has rounds completed but no Outcome Log entry, last round >3 weeks ago | **Missing outcome tracking** — "Your last logged round for [Company] was [N] weeks ago. What's the current status?" |

### Step 3: Temporal Drift Check

For each active Interview Loop:

- **Next round date passed >7 days, no Outcome Log update**: "Your [Company] [Round] was scheduled for [date] — [N] days ago. Did this happen? Log it via `debrief` or `feedback`."
- **No activity for 4+ weeks** (no rounds added, no outcome, no prep or debrief sessions referencing this loop): Flag as stale. "This loop hasn't moved in [N] weeks. Is it still active, or quietly closed? If closed, marking it frees up your pipeline read."
- **Search Strategy priority stack references a loop that's now closed**: "Your search strategy has [Company] as #1 priority, but it's been marked closed in your Outcome Log. The priority stack needs to be refreshed."

### Step 4: Story Integrity Check

- **Use Count = 0, story added >2 sessions ago**: Flag as unused. "S### ([Title]) hasn't been deployed yet. Is this an active story you're planning to use, or a candidate for retirement?"
- **Story has a "retire" flag but is still listed in a future Interview Loop's Stories used**: Flag the contradiction. "S### is flagged for retirement but appears in your [Company] loop prep. Decide: retire it or keep it active."
- **Top 3 most-used stories (by Use Count) have no recent field notes** (no field notes added in the last 3 sessions): Flag for maintenance. "S### has been used [N] times with no field notes. Add performance observations so we can track what's landing across different interviewers."

### Step 5: Coaching Strategy Staleness

- **Active Coaching Strategy last updated 4+ sessions ago**: "Your coaching strategy hasn't been updated in roughly [N] sessions. Recent performance data may have outpaced it. Run `progress` to check whether the bottleneck has shifted."
- **Strategy targets a dimension that has scored 4+ consistently in the last 3 sessions**: "Your [dimension] scores have been consistently 4+ lately. The bottleneck may have moved. Worth checking with `progress`."
- **Previous approaches list is empty** but Session Log shows 5+ sessions: Flag as missing coaching history. The history matters for avoiding circular coaching — note this but don't interrupt the session for it.

### Step 6: Search Strategy Drift

Only run if a Search Strategy section exists.

- **Priority stack references a loop that's closed or rejected**: The priority stack is stale. "Your search strategy has [Company] as #[N] priority but it's closed in your Outcome Log. Run `strategy` to rebuild the priority stack."
- **2-Week Action Plan is >14 days old**: "Your action plan from [date] is now [N] days old. Run `strategy` for a fresh plan."
- **Plan calls for activating specific companies (e.g., "Activate Anthropic + Cohere") but no corresponding loop exists**: Flag as unexecuted action. "Your plan flagged activating [Company] — that loop hasn't been opened yet. Is this still the plan, or did the situation change?"

---

## Output Schema

```markdown
## Sync Report — [Date]

## Status: [Clean / Drift Detected]

[If Clean: "No inconsistencies found. coaching_state.md reflects your current search state." — Stop here.]

## Findings

### Loop-Outcome Drift
| Loop | Issue | Fix |
|------|-------|-----|
[rows — or "none"]

### Temporal Drift
| Loop | Issue | Fix |
|------|-------|-----|
[rows — or "none"]

### Story Integrity
| Story | Issue | Fix |
|-------|-------|-----|
[rows — or "none"]

### Coaching Strategy
- [Finding — or "Strategy is current"]

### Search Strategy
- [Finding — or "Strategy is current" / "No Search Strategy section exists — run `strategy` to create one"]

## Fix Plan

Resolve in this order (highest search impact first):
1. [Specific fix — command if applicable]
2. [Specific fix — command if applicable]
3. [...]

**Recommended next**: `[command]` — [reason]. **Alternatives**: `feedback`, `strategy`, `progress`
```

---

## Coaching State Integration

`sync` does not write to `coaching_state.md` directly — it identifies what needs updating and routes to the right command. **Exception**: if the candidate confirms a loop closure or outcome during the sync session (e.g., "yes, Ramp rejected me"), update Outcome Log + Interview Loop Status immediately in the current session without routing elsewhere.
