# thankyou — Follow-Up Workflow

> Before returning any draft, run the **Writing Quality Gate** from `references/cross-cutting.md`. Auto-clean mode: strip AI-isms, enforce voice file (if exists), verify context-appropriate tone. No em dashes. No Tier 1 words. Under 120 words. One specific callback.

**Auto-invocation:** `round` produces a v0 of this note at the end of every debrief (see `round.md` Phase 8), so the candidate always leaves a round with a draft in hand rather than a blank page. Invoke `thankyou` directly for a fresh take, a per-interviewer variant, or a note that is not tied to a `round`.

### Coaching State Integration

Before drafting, check `coaching_state.md` for data that strengthens the thank-you:
- **Interview Loops**: Pull interviewer names, round context, stories used, and signals observed from the most recent `debrief` entry.
- **Interviewer Intelligence**: If interviewer profiles were researched during `prep`, reference shared interests or background to personalize the note.
- **Storybank**: If `debrief` logged which stories were used and how they landed, use positive-signal stories as callback material ("I especially enjoyed discussing [topic from the story that landed well]").

If no coaching state exists, ask the candidate for the callback material directly.

### Shared-History Check (run BEFORE choosing a callback)

Before drafting, determine what the interviewer **already knows** about the candidate. Check the Interview Loop entry for a shared-history note, and check whether the interviewer is an ex-colleague, ex-customer, repeat contact, or someone who worked on the same project.

**If shared history exists, do not use a signature story as the callback.** Re-explaining work the interviewer helped build or has heard pitched before reads as if the candidate forgot they were there. It spends credibility instead of building it.

In a warm room the callback must be **forward-looking**: what the candidate would build for *them*, a point of view on a problem *they* named, or a business observation about *their* assets. Say the new thing, not the proven thing.

If the candidate deliberately steered the conversation toward the interviewer's stated vision or named gap instead of their own deepest turf, that was a correct read of the room. The thank-you must reinforce that same direction, not reverse it.

**Source**: 2026-08-28 Ocrolus / David Snitkof. The coach drafted a note re-explaining the consortium hashing methodology to the person who built the consortium alongside the candidate. Caught before sending. See the Ocrolus loop section and the retraction note in Coaching Notes.

---

### Deadline Line (include whenever a visa, offer, or competing-timeline clock is live)

If `coaching_state.md` Profile carries a **STATED EXTERNAL DEADLINE**, use that exact date, verbatim, in the note. Never improvise a different date per company. Multiple dates circulating across live loops is an inconsistency that surfaces at reference-check or offer-timing stage.

Rules for the line:
- **State a date, not a feeling.** "There's a little bit of timeline urgency" gets a warm, undated reply. A named date gets an action.
- **Verify the day of week via Bash before writing it.** A deadline that lands on a Saturday is a visible tell that the number was not computed. Prefer a Friday or a Monday.
- **Put it last, framed as logistics, not as a demand.** Pair it with the next concrete step so it reads as coordination: "When recruiting reaches out I'll flag the timeline piece so they can check it early. I have until [date] to get an offer signed and the visa process kicked off, so I'm working backwards from that."
- **No hedging stack.** Cut "a little bit of," "kind of," "like," and any conditional that hands the reader an exit ("if you think this is worth pursuing").
- If Profile has no stated external deadline yet, ask the candidate for the date once, then write it into Profile so every later draft inherits it.

**Source**: 2026-08-28 Ocrolus. The in-room H1B ask produced no filing date; the thank-you fixed it with an explicit one.

---

### Timing Guidance

Before drafting, advise on timing:
- **Same day** (within 2-4 hours): Standard best practice for most companies. Shows enthusiasm without being desperate.
- **Next morning**: Acceptable if the interview was late in the day. Can feel more thoughtful.
- **Never wait more than 24 hours**: After that, you've missed the window.
- **If you haven't heard back** (after expected timeline): Wait until 1-2 business days past the stated timeline, then send a brief check-in. Don't follow up more than twice.

### Interview-Specific Callbacks

A generic "thanks for your time" is forgettable. A strong thank-you references a specific moment from the conversation:
- Pull from `analyze` or `mock` data if available: "I especially enjoyed our discussion about [specific topic from transcript]."
- If the candidate remembers a particular exchange, weave it in: "Your question about [X] got me thinking further about [Y]."
- If the interviewer shared something personal or professional, acknowledge it: "I appreciated you sharing your perspective on [topic]."
- Keep it brief — one specific callback, not a recap of the entire interview.

### Multi-Interviewer Handling

If the candidate met multiple interviewers in the same round, generate **separate drafts for each person**:
- Each note should reference something specific to that interviewer's questions or conversation.
- Vary the tone slightly — don't send identical notes (interviewers compare).
- The core message can be similar, but the callback and angle should differ.
- Ask the candidate: "Who did you meet with? What stood out from each conversation?"

### Output Schema

```markdown
## Pre-Draft Checks
- Shared history with this interviewer: [none / what they already know -- and therefore what NOT to use as the callback]
- Stated external deadline from Profile: [exact date, day-of-week verified via Bash] or [none on file]

## Timing
- Recommended send time:
- Follow-up if no response by: [date, day-of-week verified via Bash]

## Thank-You Draft: [Interviewer Name] (<120 words)
[draft with specific interview callback]

## Thank-You Draft: [Interviewer 2 Name] (if applicable, <120 words)
[draft with different callback]

## Alternate Tone (optional)
[draft]

## If Rejected: Learning Questions
1.
2.

## If Advancing: Reinforcement Points
1.
2.
3.

**Recommended next**: `round` — capture impressions and score the transcript in one workflow (if not already done). **Alternatives**: `prep [company]` (for next round), `progress`
```
