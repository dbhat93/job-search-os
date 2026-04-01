# map — Situational GPS

Answers one question: **"Given where I am right now, what should I do?"**

This is not a trend review (`progress`), not a state consistency check (`sync`), and not a pipeline health analysis (`strategy`). Those go deep on one thing. `map` goes wide and shallow — it reads the full coaching state and tells the candidate what to run next and why, in under 2 minutes.

### When to Use

- Starting a session after a break and not sure where to pick up
- Overwhelmed by the system and want a single clear next move
- Things are moving fast (multiple loops advancing at once) and priorities need to be re-ranked
- Just completed a round and want to know the right sequence of follow-up actions

---

### Logic

Read `coaching_state.md` in full. Then run the priority check below — this determines what goes in "This Week."

**Priority check order (first match wins — but surface up to 3 time-sensitive items):**

| Condition | Action | Urgency |
|-----------|--------|---------|
| Interview completed < 48 hours ago (Next round date passed + no Outcome Log entry for that round) | `round` now — memory decays fast | Urgent |
| Upcoming interview within 72 hours | `hype` + confirm `prep` was done | Urgent |
| New transcript in `~/meetings/` matching active loop, no Score History entry | `round` or `analyze` — transcript auto-detected | Urgent |
| Pending outcome > 7 days with no Outcome Log update | `feedback` to log result | High |
| Stale promise in Contact Network (>7 days, actionable) | Surface as action item: "[Name] — [promise]" | High |
| Losing-touch referral with active loop (3+ interactions, >14 days silent) | "Nudge [Name] — they referred you to [Company]" | High |
| Transcript available but no corresponding Score History entry | `analyze` | High |
| Active loop with no `prep` run (Status: Researched or Decoded, no prep brief) | `prep [company]` | High |
| Interview within 7–14 days, prep done but no mock | `mock` | Medium |
| Storybank < 6 stories | `stories` — critical foundation gap | Medium |
| 3+ scored sessions with no `progress` review in last 3 sessions | `progress` | Medium |
| Storybank has critical competency gaps for active loops (from Storybank Gap Check) | `stories` targeting specific gaps | Medium |
| No active loops, search stalled | `decode` + `strategy` | Medium |
| Search Strategy is >14 days old OR priority stack references closed loops | `strategy` | Low-medium |
| Coaching state appears drifted (loops active with no movement >4 weeks) | `sync` | Low |

Surface only what's actionable this week. Don't list everything — the point of `map` is to reduce cognitive load, not add to it.

---

### Output Schema

```markdown
## Your Map — [Date]

## Where You Are Now
[2–4 sentences. Plain English read of the current search state. Examples:]
- "You have 3 active loops: [Company A] is at final round (interview in 4 days), [Company B] is at debrief stage, [Company C] is researched but no prep done."
- "Your storybank has 9 stories. Last practice session was [N] days ago. No pending outcomes waiting."
- "Search is paused — no active loops, no recent prep. Last session [N] days ago."

## This Week
[1–3 items, in priority order. Each item is one line with a command + brief reason.]

1. **[Most urgent action]** → `[command]` — [one-line reason]
2. **[Second action]** → `[command]` — [one-line reason]
3. **[Third action if applicable]** → `[command]` — [one-line reason]

[If nothing is urgent: "Nothing time-sensitive this week. Use this session for [command] — [why it's the best next investment]."]

## In the Background
[What's in flight but doesn't need action today. 1–3 bullets. Examples:]
- "[Company B] waiting on recruiter response — no action needed until you hear back"
- "Storybank is healthy but S006 hasn't been deployed — low priority"
- "Progress review is coming up (you're 2 sessions away from the 3-session trigger)"

## Command Reference for Your Current Phase
[Filtered list — only commands relevant to current search phase. Don't list the full registry.]

[If candidate is in early search / no active loops:]
Relevant now: `decode`, `research`, `stories`, `pitch`, `resume`, `outreach`, `strategy`

[If candidate is in active interviewing (1+ loops in Interviewing status):]
Relevant now: `prep`, `mock`, `practice`, `analyze`, `debrief`, `concerns`, `questions`, `hype`, `thankyou`, `feedback`

[If candidate has multiple loops at different stages:]
Relevant now: [show commands relevant to the specific stages — interview-track and search-track separately]

[If candidate is at offer stage:]
Relevant now: `negotiate`, `salary`, `reflect`

[In all phases:]
Meta commands (always available): `progress`, `sync`, `strategy`, `map`, `help`
```

---

### Coaching State Integration

`map` is read-only — it does not write to `coaching_state.md`. It reads everything and surfaces priorities, but takes no action itself.

**Exception**: If the priority check reveals a time-sensitive item the candidate wasn't aware of (e.g., a debrief window closing, a loop quietly going stale), name it explicitly rather than burying it in the output: "Before anything else — your [Company] interview was [N] days ago and there's no debrief logged. That window is closing. Run `debrief` first."

**Recommended next**: Whichever command appears at position 1 in "This Week." **Alternatives**: `sync` (if state may be drifted), `strategy` (if pipeline health is the real question), `progress` (if performance trends are the concern).
