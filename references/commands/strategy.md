# strategy — Job Search Strategy Session

The search-level command. `prep` handles company-specific depth, `progress` handles skill trends, `strategy` handles the meta-layer: pipeline health, timeline risk, cross-loop coherence, funnel management, and decision-making at inflection points. Run it when the candidate needs to think about the search as a whole, not just the next interview.

---

## Session Types

| Type | When to Use | Scope |
|------|------------|-------|
| **Quick Pulse** | Fast check — candidate wants to know if the search is on track | Active loops + timeline risk + top 3 actions. 10-minute session. |
| **Full Strategy** | Default. New search, monthly review, major loop closed, or search feeling scattered | Full pipeline audit + timeline + funnel + narrative coherence + 2-week plan |
| **Decision Point** | Offer in hand, exploding deadline, or forced choice between pursuing vs. not | Evaluation framework + pipeline impact + concrete recommendation |

Default to Full Strategy unless the candidate signals urgency or explicitly requests a quick check.

---

## Logic / Sequence

### Step 1: State Assembly

Read `coaching_state.md`:
- **Profile**: deadline, target roles, seniority band, career transition status, comp expectations
- **Interview Loops**: all entries (status, stage, fit verdict, next action, stories deployed, concerns surfaced)
- **Outcome Log**: all results (advanced, rejected, pending, offer, withdrawn)
- **Active Coaching Strategy**: current skill bottleneck and approach
- **Drill Progression**: current stage and gates passed
- **Coaching Notes**: constraints, preferences, emotional patterns relevant to the search
- **Salary / Search Strategy** (if sections exist): prior comp research, prior strategic decisions

Then ask one question before proceeding: "Before I build the full picture — any news since last session? Loops advanced, rejected, or opened?" Wait for response. Incorporate any updates before continuing.

### Step 2: Timeline Analysis

Calculate search health relative to the deadline.

**Weeks remaining**: Count from today to deadline (from Profile). If no deadline is set, ask.

**Loop conversion estimate**: For each active loop, estimate time-to-offer based on:
- Rounds remaining × typical round cadence (1 week between rounds for fast-moving companies, 2 weeks for slower)
- Current stage (deeper in loop = higher probability, shorter timeline)

**Yield projection**: Given N loops at their current stages, what's the probability that at least one converts by the deadline? Be explicit:
- "You have 1 loop at Round 3 of 4 — 3-4 weeks to offer if it moves. Given the Advance (not Strong Hire) signal, I'd put conversion probability at 50-60%."
- "That gives you a search with roughly 50-60% chance of meeting your deadline on the current pipeline alone. That's a coin flip — here's what changes that."

**Status signals:**
- **On Track**: 2+ loops at late stage (Round 3+), or 4+ loops at mid-stage, with ≥6 weeks remaining
- **At Risk**: 1 loop at late stage with <4 weeks remaining, or thin pipeline with deadline approaching
- **Critical**: <3 weeks remaining with no late-stage loops, or 0 active loops

State the status plainly. Don't soften a "Critical" to "Slightly at Risk."

### Step 3: Pipeline Priority Stack

Score each active loop on three dimensions:

1. **Conversion probability** (high/medium/low) — based on stage, interviewer signals, fit verdict, and any intel in coaching state
2. **Strategic value** (Dream / Strong Target / Learning Opp / Backup) — draw from Profile target roles; ask candidate if unclear
3. **Coaching leverage** (how much coaching work changes the outcome this week) — late-stage loops with specific prep needs have high leverage; early-stage loops with no scheduled interviews have low leverage

Output a ranked stack with explicit rationale for each ranking. The stack drives where coaching effort goes this week — this is the core output of the strategy session.

**Coaching investment rule**: If a loop is low-conversion AND low-strategic-value AND requires high coaching effort, name it as dead weight. "Anthropic is currently in round 1 with no timeline. Ramp is in round 3 and decides in 2 weeks. Anthropic needs to be a background task this week, not a coaching priority."

### Step 4: Funnel Health

**Count active loops**: Target 3-5 for most searches; fewer is acceptable if 2+ are late-stage; more risks spreading attention.

**Closed loop check**: Are any loops about to close (pending outcome, or stuck with no movement for 3+ weeks)? If so, will replenishment be needed?

**Top-of-funnel assessment**: Based on Profile (target companies, sector, referral network) and Coaching Notes:
- Are there warm targets not yet activated? (referrals the candidate mentioned, second-degree connections to target companies)
- Is the candidate over-concentrated in one sector or company type (e.g., all fintech, all Series B)?
- Is the apply channel diversified (referrals vs. cold vs. recruiter-sourced)?

If funnel is thin, prescribe specific actions — not generic advice. "You have 1 active loop. You need 2-3 more to have a viable safety net by May 10. Based on your target list, Anthropic and Cohere are the highest-priority warm activations this week. Both require referral outreach, not cold apply. Run `outreach` to build the messages."

### Step 5: Narrative Coherence Audit

With multiple simultaneous loops and potentially multiple resume variants, check for coherence across active applications:

- **Resume variant check**: Is each active loop receiving the right resume variant (TPM vs. PM-T&S vs. general PM)? If the candidate is unclear, flag it — sending the wrong variant to a company that has already formed an impression is a credibility risk.
- **Positioning consistency**: Are the pitches and "why this company" narratives adapted per company but rooted in the same core positioning? Or is the candidate telling inconsistent stories?
- **Live contradictions**: Is the candidate positioning as a fraud PM for one company and a general product PM for another in parallel? Does that create a contradiction if the companies talk? (Usually not — but worth surfacing.)

Flag any misalignments. Don't rewrite here — that's `pitch`, `resume`, or `linkedin`. Just identify the coherence risks.

### Step 6: Decision Logic (Decision Point sessions only)

When an offer is in hand or a forced choice must be made.

**Offer evaluation framework** (run in order):

1. **Comp alignment**: Does the offer meet the target range from `salary`? If salary hasn't been run, ask for the candidate's floor and compare.
2. **Role scope vs. stated goals**: Does the role provide the leverage, growth, and career trajectory the candidate said they wanted at kickoff? Name the specific gaps if any.
3. **Company trajectory**: Stage, growth rate, financial health, leadership. Does this company have the trajectory to make this a good 3-year move?
4. **Optionality cost**: What does accepting this offer close off? Other active loops, career paths, sectors. Is that a real cost?
5. **Timeline fit**: Does this offer solve the deadline, or is it premature to commit (e.g., accepting a backup offer before the Dream company has decided)?

**Pipeline forcing choices** (when loops are pressuring each other):
- If an exploding deadline exists on one offer, help the candidate calculate whether it's worth accelerating other loops or accepting without full information.
- If a Loop is taking too long, name it: "Anthropic has been 'pending' for 6 weeks with no timeline. That loop is functionally closed. Factor that into your plan."
- When to walk away: if a loop has been unresponsive for 4+ weeks, the candidate's time is better spent elsewhere. Don't chase ghosts.

### Step 7: 2-Week Action Plan

Synthesize everything into a concrete, prioritized plan. Two horizons:

**This week (days 1-7) — highest leverage:**
3-5 actions only. Each action must be specific, executable, and linked to a command if applicable. Not "prep for Ramp R3" — "run `prep [Ramp R3 — take-home case]` to build the presentation framework and predicted questions for the business case."

**Next week (days 8-14) — contingent:**
2-3 actions that depend on what happens this week. State the trigger explicitly: "If Ramp advances → immediately run `hype` + `mock [presentation]`. If Ramp rejects → activate Anthropic and Cohere referral outreach via `outreach`."

### Step 8: Challenge (Deep Optimization only — see `references/challenge-protocol.md` → Search Strategy Challenge)

Run graduated Challenge Protocol against the search strategy itself. Level 3 = Assumption Audit (one sentence). Level 4 = Assumption Audit + Blind Spot Scan. Level 5 = Lenses 1, 2, 3, 4 (all applicable — search strategy is forward-facing, so Pre-Mortem is included). Timing: after the full strategy output, before Priority Moves.

Only run for Full Strategy sessions. Skip for Quick Pulse and Decision Point.

---

## Output Schemas

### Quick Pulse

```markdown
## Search Pulse — [Date]

## Active Pipeline
| Company | Stage | Fit | Next Action | Priority |
|---------|-------|-----|------------|----------|

## Timeline: [On Track / At Risk / Critical]
[1-2 sentences — why, and what that means for this week]

## Top 3 Actions This Week
1. [Specific action — command if applicable]
2. [Specific action — command if applicable]
3. [Specific action — command if applicable]
```

### Full Strategy Session

```markdown
## Search Strategy — [Date]

## Pipeline Health
| Company | Status | Stage | Fit Verdict | Coaching Leverage | Priority |
|---------|--------|-------|-------------|------------------|---------|
[ranked by priority — highest first]

## Timeline Analysis
- Deadline: [date]
- Weeks remaining: [N]
- Active loops with conversion timeline:
  - [Company]: Round [N] of [M] — estimated [X] weeks to offer if advancing — conversion probability [%]
  - [Company]: [same]
- Best case: [company + "offer by [date]"]
- Base case: [company + "offer by [date]"]
- Worst case: [what happens if current pipeline doesn't convert — and what the plan is]
- Timeline status: **[On Track / At Risk / Critical]**
- Risk flag: [specific risk + what must happen this week to mitigate]

## Funnel Health
- Active loops: [N] (target for this search: 3-5)
- Funnel status: [Healthy / Thin / Dangerously thin]
- Loops at risk of closing without conversion: [list, or "none"]
- Replenishment needed: [Yes — [N] new loops needed / No]
- Recommended activations (if needed): [specific companies + why + channel]

## Narrative Coherence
| Loop | Resume Variant | Pitch Variant | Coherence Status |
|------|---------------|--------------|-----------------|
[flag any misalignments with specific fix]
- Cross-loop contradictions: [list, or "none detected"]

## Priority Stack
1. **[Company]** — [specific reason this is #1: stage + fit + coaching leverage this week]
2. **[Company]** — [reason]
3. **[Company]** — [reason]
[Dead weight flag if applicable: "[Company] is low-priority this week — here's why and what to do with it"]

## 2-Week Action Plan

### This Week
| Action | Command | Owner | By |
|--------|---------|-------|-----|

### Next Week (contingent)
| Action | Trigger | Command |
|--------|---------|---------|

## Strategic Risks
1. **[Risk name]**: [1-2 sentences on what this risk is and what to watch for]
2. **[Risk name]**: [same]
[Optional 3rd if truly distinct]

## Challenge (Levels 3–5 — see references/challenge-protocol.md → Search Strategy Challenge)
[Level 3: Assumption Audit — one sentence naming the most important hidden assumption the search strategy rests on]
[Level 4: Assumption Audit + Blind Spot Scan]
[Level 5: All four lenses — Assumption / Blind Spot / Pre-Mortem / Devil's Advocate]

**Recommended next**: `[command]` — [reason]. **Alternatives**: `prep [highest-priority company]`, `outreach`, `hype`
```

### Decision Point

```markdown
## Decision Analysis — [Company / Choice]

## The Decision
[Exactly what needs to be decided, and by when]

## Evaluation

### Comp Alignment
[Offer vs. target range — specific numbers if available]

### Role Scope vs. Goals
[Does this role give you what you said you wanted? Name the gaps if any.]

### Company Trajectory
[Stage, growth signals, financial health, leadership quality — be specific]

### Optionality Cost
[What does saying yes close off? Is that a real cost or a theoretical one?]

### Timeline Fit
[Does this solve your deadline? Or are you accepting prematurely?]

## Pipeline Impact
[If yes: how does this affect other active loops? If no: what's the recovery plan?]

## Recommendation
[At Level 5: direct. "Take it" or "Don't take it" with one-sentence rationale.
At Levels 1-4: framed as "Here's what the data says — [assessment]. The call is yours."]

## If Yes — Next 48 Hours
1. [Immediate action]
2. [Immediate action]

## If No — Recovery Plan
[How to maintain momentum — which loops to prioritize, what to activate]
```

---

## Coaching State Integration

After a Full Strategy or Decision Point session, write to `coaching_state.md`:

**Search Strategy section** (create if missing, update if exists):
- Date of strategy session
- Timeline status at time of session
- Priority stack (ranked)
- Funnel status
- Key risks identified
- 2-week action plan (carry forward until next strategy session updates it)

**Active Coaching Strategy** (update if strategy session reveals a skill-level insight):
- If the strategy session surfaces that the primary obstacle is now search-level (pipeline, funnel, narrative) rather than skill-level, note it in Active Coaching Strategy: "Search-level constraint flagged [date]: [issue]. Coaching focus shifted to [outreach / research / strategy] until pipeline is healthy."

**Interview Loops** (update if any loops are reprioritized or flagged as dead weight):
- Add or update Status, Next Action fields per the priority stack output.
