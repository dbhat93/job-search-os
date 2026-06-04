# pipeline

Live pipeline view generated from coaching_state.md. Never reads state/pipeline.md (that file is deprecated). Output is always fresh.

## When to use

Any time the candidate wants a current view of all loops: what's active, what's pending, what's closed. Run this before making offer decisions, at session start as a sanity check, or whenever asked for "where things stand."

## Mandatory pre-step

Run `date "+%A, %B %d, %Y"` before generating output. Use the result to compute days-remaining to search deadline.

## Source of truth

Read `coaching_state.md` in full: Profile (deadline), Interview Loops (all entries), Outcome Log, Comp Strategy (offers in hand), Active Coaching Strategy (72-hour window).

Never read `state/pipeline.md`. That file is stale by design. It is not updated by any command. The coaching_state.md Interview Loops section is authoritative.

## Output schema

Generate the following sections in order. Use markdown tables. No preamble.

---

### Header

One line: `Pipeline: [date]. [N] days to deadline.`

---

### Stats block

Compact bullet list:

- Active loops (total)
- Offers in hand (count + company names + deadlines)
- Late-stage advancing (R2+ or panel): list companies
- Early-stage advancing (recruiter screen done, next round TBD): list companies
- Applied/referred, no screen (count)
- Watching (count)
- Closed this search (count)

---

### Offers in Hand

If any offer is in hand, show it first. Columns: Company | Role | Key terms | Decision deadline.

---

### Late Stage

Loops at R2 or later (HM done, panel confirmed, onsite scheduled). Columns: Company | Role | Stage summary | Next action | Priority.

Sort by urgency (soonest next action first).

---

### Early Stage

Loops where recruiter screen is done but no HM yet, or where CTO/founder call is next. Columns: Company | Role | Stage summary | Next action | Priority.

---

### Applied / Referred, No Screen

Companies where application or referral is submitted but no screen has occurred. Columns: Company | Role | Channel | Status.

---

### Watching

Companies being tracked but not yet applied. One line each.

---

### Closed / Archived

All loops concluded this search. Columns: Company | Outcome | Closed | Notes (1 sentence max).

---

### 72-Hour Priority View

Generate this section only if Active Coaching Strategy contains a current approach or 72-hour window. Pull the top 4-6 actions from coaching_state.md and format as a table: # | Action | When | Risk if skipped.

---

## Rules

- Generate every section from coaching_state.md. Do not invent or estimate loop status.
- If a loop's status is ambiguous (e.g., "awaiting update"), say so in the stage summary rather than guessing an outcome.
- If coaching_state.md has no entry for a company the user asks about, surface it as a gap: "No loop record found for [Company]. Add it via sync or direct state update."
- Do not write to any file. This command is read-only.
- Do not update state/pipeline.md. That file is ignored going forward.
