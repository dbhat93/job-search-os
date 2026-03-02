# pipeline — Job Search CRM

**Job:** *Give me clarity on where I stand and what to do next.*

---

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `pipeline view` | Full pipeline snapshot — all active loops, sorted by urgency; priority check |
| `pipeline add [company]` | Add a new opportunity to the pipeline |
| `pipeline update [company]` | Move to a new stage, log activity, set next action |
| `pipeline stall` | Surface opportunities with no activity in 7+ days |
| `pipeline close [company] [won/lost]` | Archive with outcome and lessons |

**Default (bare `pipeline`):** Run `pipeline view`.

---

## State File

Read from and write to `state/pipeline.md`.

If `state/pipeline.md` doesn't exist, offer to create it: "You don't have a pipeline file yet. Want me to create one and add your first opportunity?"

---

## `pipeline view` — Full Snapshot

### Logic

1. Read `state/pipeline.md`.
2. Read `state/coaching.md` (or `coaching_state.md`) — cross-reference Interview Loops for round detail.
3. Sort active opportunities by urgency: Interviewing > Screening > Applied > Researched > Identified > Offer > Decision.
4. Within same stage, sort by Priority: Dream > Strong Target > Learning Opp > Testing Ground. (Not a fit loops should be closed — flag them if they appear active.)
5. Flag stalled loops (Last Activity > 7 days ago) with ⚠️.
6. Surface the one highest-leverage next action across the whole pipeline.

### Output Schema

```markdown
## Pipeline — [date]

### Active Loops

**[Company] — [Role]** | [Stage] | [Priority]
- Next action: [specific action]
- Due: [date or "ASAP" or "TBD"]
- Last activity: [date] — [what happened]
- Round intel: [from coaching state — e.g., "Round 2 of 3 complete. Decision pending."]

[repeat for each active loop]

---

### Prep Allocation Check
Prep investment = company fit × interview stage (both factors compound):
- [Company] — [Priority / Stage] → [investment level: e.g., "maximum — Dream onsite" or "30min — Testing Ground recruiter screen"]
- [repeat for each active loop, ranked highest to lowest]

Note: Stage is an independent variable. A Testing Ground onsite warrants more prep than a Dream recruiter screen. Match investment to what the moment actually requires.

### Stalled Loops ⚠️
[Any loop with no activity in 7+ days — surface with specific next action]

### This Week's Priority Move
[One highest-leverage action across the whole pipeline — specific and actionable]

**Next commands**: `pipeline add`, `pipeline update`, `pipeline stall`, `prep [company]`, `review`
```

---

## `pipeline add [company]` — Add New Opportunity

### Logic

Ask in sequence — one question at a time:

1. "What role are you targeting at [company]?"
2. "What stage are you at? [Identified / Researched / Applied / Screening / Interviewing]"
3. "What's the priority? [Dream / Strong Target / Learning Opp / Testing Ground / Not a fit]"
4. "What's the next action and when?"
5. "Do you have a referral or contact at this company?" (optional — feeds `state/contacts.md` later)

After collecting inputs, write the new row to `state/pipeline.md` and confirm:

```markdown
Added to pipeline:
- Company: [company]
- Role: [role]
- Stage: [stage]
- Priority: [priority]
- Next action: [action] by [date]
- Loop ID: [COMPANY-00X]

**Next commands**: `research [company]` (if Identified/Researched stage) or `prep [company]` (if Screening/Interviewing)
```

Also offer to initialize the Interview Loop in `coaching_state.md`: "Want me to open an interview loop for [company] in your coaching state? That enables prep briefs, story mapping, and round tracking."

---

## `pipeline update [company]` — Update Stage or Activity

### Logic

1. Pull current record from `state/pipeline.md`.
2. Show current state: "Currently: [Stage] | Last activity: [date] | Next action: [action]"
3. Ask what changed — one question at a time:
   - "What happened? [stage moved / activity logged / next action changed]"
   - "What's the new next action and when?"
4. Write updated row to `state/pipeline.md`.
5. If stage moved to Interviewing, offer to open/update the coaching loop: "Looks like you're now in interviews — want me to update your Interview Loop in the coaching state?"
6. If stage moved to Offer, route to `negotiate` automatically: "You have an offer — let's get you into negotiation prep. Running `negotiate` now."

---

## `pipeline stall` — Find What's Falling Through the Cracks

### Logic

1. Read `state/pipeline.md`.
2. Identify every row where Last Activity is 7+ days ago and Stage is not Closed.
3. For each stalled loop, surface a specific recommended action based on Stage:

| Stage | Default next action if stalled |
|-------|-------------------------------|
| Identified | Research or decide to pass |
| Researched | Apply or discard — why hasn't a decision been made? |
| Applied | Follow up with recruiter |
| Screening | Recruiter hasn't responded — follow up |
| Interviewing | Next round hasn't been scheduled — follow up |
| Offer | Decision is overdue — negotiate or decline |

### Output Schema

```markdown
## Stalled Loops ⚠️

**[Company] — [Role]** | [Stage] | [Priority] | Last activity: [X] days ago
- Recommended action: [specific action]
- Why this matters: [consequence of continued stall]

[repeat for each stalled loop]

**No stalled loops:** If nothing is stalled, say so directly: "No stalled loops — your pipeline is moving."

**Next commands**: `pipeline update [company]`, `draft [company]` (to send a follow-up)
```

---

## `pipeline close [company] [won/lost]` — Archive

### Logic

1. Ask: "What was the outcome?" (if not specified in the command)
2. Ask: "What's the one thing you'd do differently in this loop?"
3. Move the row from Active to Closed in `state/pipeline.md`.
4. Update the Outcome Log in `coaching_state.md`.
5. If won: route to `negotiate` (if not already run) or `reflect` (if search is complete).
6. If lost: ask if they want to run `reflect` on this loop or continue the search.

### Output Schema

```markdown
## Loop Closed: [Company]

- Outcome: [Won / Lost / Withdrew / No response]
- Closed: [date]
- Lessons: [candidate's answer to "what would you do differently"]

[Coaching state updated — Outcome Log entry added.]

**Next commands**: `negotiate` (if won, offer pending) | `reflect` (if search complete) | `pipeline view` (continue search)
```

---

## State Update Triggers

Write to `state/pipeline.md` whenever:
- `pipeline add` creates a new opportunity
- `pipeline update` moves a stage or logs activity
- `pipeline close` archives a loop
- A real interview outcome is reported in any command
- A recruiter screen is scheduled (update Stage from Applied → Screening)
- An offer is received (update Stage from Interviewing → Offer)

---

## Design Principles

**GTD — nothing falls through the cracks.** Every active loop has a Next Action and a Due date. The `stall` sub-command is the enforcer.

**Prep allocation is a function of two compounding factors.** Company fit (Dream → Strong Target → Learning Opp → Testing Ground → Not a fit) tells you how much you want the outcome. Interview stage (Onsite/Super Day → HM/Technical → Recruiter/Phone → Applied/Researched) tells you how much the round demands. Both factors matter independently — weight them together to determine how much prep this moment warrants. A Dream onsite gets maximum investment. A Testing Ground recruiter screen gets ~30 minutes — enough to be sharp, not more. A Testing Ground onsite may warrant more prep than a Dream recruiter screen because stage is an independent variable.

**Cross-reference with coaching state.** `pipeline view` reads both `state/pipeline.md` (search CRM layer) and `coaching_state.md` / `state/coaching.md` (coaching layer) to surface round detail alongside pipeline status. They are complementary — neither replaces the other.
