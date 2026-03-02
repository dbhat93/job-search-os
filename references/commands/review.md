# review — Weekly Search Review

**Job:** *Show me what's working in my search this week and what isn't.*

> **Distinct from `progress`:** `progress` measures coaching quality — are your interview scores improving? `review` measures search health — is the funnel moving, is the network active, is prep allocation right? Run both. They answer different questions.

---

## When to Run

Weekly. Sunday evening or Monday morning is the right rhythm — you can see what happened last week and plan what matters this week before the week absorbs you.

Can also be triggered by: significant pipeline change (new offer, new loop stalling), search milestone (approaching deadline), or a feeling that the search isn't moving.

---

## Sequence

1. Read `state/pipeline.md` — active loops, stages, stalls, last activity.
2. Read `coaching_state.md` — score history, session log, active coaching strategy.
3. Read `state/contacts.md` if it exists — contact activity.
4. Run through each section of the review (see below). Adapt depth to available data.
5. End with one **This Week's Priority Move** — the single highest-leverage action.

---

## Review Sections

### 1. Pipeline Health

What's actually moving vs. what's stalled?

- Count active loops by stage.
- Flag any loop with no activity in 7+ days (⚠️).
- Check whether next actions exist and are dated for every active loop.
- Check overall funnel velocity: are loops progressing or stuck?

**Funnel health signals:**
- Loops advancing stages: healthy
- Loops stalled at Applied (7+ days, no screen): follow-up needed
- Loops stalled at Interviewing (7+ days, no round scheduled): follow-up or close
- No new loops added in 2+ weeks with an active deadline: pipeline may be too thin

### 2. Prep Allocation Check

Is your prep investment matching what each moment actually requires?

For each active loop, assess: Priority (Dream / Strong Target / etc.) × Stage (Onsite / HM / Recruiter / Applied). Flag if a Dream company at Onsite stage hasn't had a recent prep session, or if a Testing Ground company is consuming disproportionate prep time.

This is not about effort — it's about sequencing. Make sure the Dream loops are getting the attention they warrant.

### 3. Coaching Progress (Summary)

Pull the coaching headline from `coaching_state.md` — don't re-run `progress`, just surface the current bottleneck and trend direction.

- Current primary bottleneck: [from Active Coaching Strategy]
- Score trend (last 2 sessions): [improving / flat / declining]
- Storybank health: [total stories, % rated 4+]

If the candidate hasn't had a practice or analyze session in 7+ days, flag it: "No practice this week. If you have interviews scheduled, that gap is worth addressing."

### 4. Outreach & Network

What's happening with referral leverage? (Only if `state/contacts.md` exists.)

- Active loops with no contacts: flag as referral gap
- Contacts awaiting follow-up: surface
- New contacts added this week: note

If `state/contacts.md` doesn't exist: "You don't have a contacts file set up. If networking is part of your strategy, run `outreach add` to start tracking."

### 5. Deadline Math

Check the search deadline from `coaching_state.md` Profile section against today.

- Weeks remaining: [X]
- Active loops currently in Interviewing or Offer stage: [count]
- Are you on track? Flag if deadline is < 4 weeks and no loops are in Interviewing+.

---

## Output Schema

```markdown
## Search Review — [date]

### Pipeline Health
- Active loops: [N] | Interviewing: [N] | Screening: [N] | Applied: [N]
- Stalled loops ⚠️: [list with last activity date]
- Next action coverage: [all loops have dated next actions / [N] loops missing next action]
- Funnel velocity: [Moving / Slow / Stalled]

### Active Loops
| Company | Priority | Stage | Last Activity | Next Action | Due |
|---------|----------|-------|---------------|-------------|-----|
| [company] | [label] | [stage] | [date] | [action] | [date] |

### Prep Allocation Check
| Company | Priority × Stage | Investment needed | Investment this week |
|---------|-----------------|-------------------|---------------------|
| [company] | [Dream × HM] | High | [Y/N — if no, flag] |
| [company] | [Testing Ground × Recruiter] | ~30 min | [Y/N] |

### Coaching Progress
- Primary bottleneck: [from coaching strategy]
- Trend (last 2 sessions): [improving / flat / declining on [dimension]]
- Last practice/analyze session: [date] — [flag if >7 days ago]
- Storybank: [N] stories | [N] rated 4+ | Key gap: [if any]

### Outreach & Network
- Loops with referral contacts: [N of N active loops]
- Referral gaps ⚠️: [companies in active loops with no contacts]
- Contacts awaiting follow-up: [N]
- Network move this week: [action or "none — add contacts for active loops"]

### Deadline Check
- Deadline: [date] — [X] weeks remaining
- Loops in Interviewing+: [N]
- On track: [Yes / Tight — [why] / At risk — [why]]

### This Week's Priority Move
[One action — specific, named, actionable. Not "practice more." Something like: "Schedule prep for the Ramp HM round — it's been 5 days since the recruiter screen and no prep logged."]

**Next commands**: `pipeline update [company]`, `prep [company]`, `practice`, `outreach prep [company]`, `progress`
```

---

## Design Principles

**Search health ≠ coaching health.** Candidates improving their interview skills while their pipeline stalls will miss their deadline. Candidates with active pipelines but poor answers will convert poorly. Both signals matter — `review` and `progress` together give the full picture.

**One priority, not a to-do list.** The output ends with one move. Not five. The candidate knows what to do next, and they're not paralyzed by a list.

**Deadline math is honest.** If the deadline is approaching and the pipeline is thin, say it directly: "You're 4 weeks from your deadline with 1 active loop in Screening. That's tight — you need either more pipeline or faster progression in the current loop. Here's what I'd prioritize."

**Weekly, not daily.** The review is not a dashboard you check constantly — it's a weekly pulse. Daily anxiety-checking of pipeline status is not the goal. Weekly intentionality is.
