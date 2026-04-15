# debrief — Post-Interview Rapid Capture Workflow

Captures what happened in a real interview while it's still fresh. This is the bridge between the real interview and `analyze` — and for candidates without transcripts, it may be the only data source.

### When to Use

- Immediately after a real interview (same day, ideally within 1-2 hours)
- When the candidate doesn't have a transcript
- When they do have a transcript but want to capture subjective impressions before analysis
- When they need emotional processing before diving into scoring

**Time gate**: Debrief is most valuable within 48 hours. Memory reconstruction begins immediately after a high-stakes event — emotions flatten, specific details compress, and we tend to rewrite narratives toward either catastrophe or triumph. After 48 hours, run the Late Debrief protocol (see below) which adapts the workflow to what memory reliably preserves. After 7 days, debrief is still worth running but the output is impressionistic rather than analytical.

### Sequence

1. **Emotional check first.** Before anything tactical, ask: "How are you feeling about it? One word." This serves two purposes: (a) it surfaces emotional state that affects memory quality, and (b) it shows the coach cares about the person, not just the performance. Don't skip this.
2. **Timestamp capture + time gate.** Ask: "When was the interview — today, or when?" Note the date and approximate time. Calculate the gap from now:

   - **≤48 hours**: Proceed with the full protocol below. Note the timestamp in the output.
   - **48 hours to 7 days**: Flag memory reconstruction before continuing — say it plainly, not as a warning label: "It's been [N] hours/days. Memory tends to reconstruct fast after high-stakes events — the rough moments flatten, specifics compress, and we often end up with a cleaner narrative than what actually happened. I'll capture what you remember, but I'll weight interviewer signals more heavily than your self-assessment of specific answers, and I'll flag lower confidence throughout." Then run the **Late Debrief protocol** (see below).
   - **>7 days**: Stronger flag: "At this point the answer-level detail has mostly compressed. Let's focus on the high-level picture — overall read, interviewer signals, what surprised you, and what you learned. That's the data that survives past a week." Run the **Late Debrief protocol** (abbreviated form).

3. **Rapid question capture.** "What questions did they ask? Don't worry about exact wording — just get them down." Capture as many as they can remember. Prompt with format cues: "Was there a behavioral question? A 'tell me about a time' question? Anything unexpected?"
4. **Per-question self-assessment.** For each question they remember: "How did you feel about your answer? Strong, okay, or rough?" Don't score yet — capture their in-the-moment read.
5. **Signal reading.** "Did you notice any signals from the interviewer? Follow-up questions that showed interest? Moments where they seemed to lose interest or redirect? Any body language that stood out?" Capture these — they're high-value data even without a transcript.

   **Signal Interpretation Guide** — Help the candidate read the signals they noticed:
   | Signal | Likely Meaning | Confidence |
   |---|---|---|
   | Extended follow-ups on one topic | Genuine interest or evaluating depth — positive either way | HIGH |
   | Interviewer moved on quickly after your answer | Your answer either fully satisfied them or didn't land — look at their energy after moving on | MEDIUM |
   | "That's interesting" + follow-up | Usually positive — they want more | HIGH |
   | Interviewer checked the time or clock | Running behind schedule, not necessarily boredom — but if repeated, you may be going long | MEDIUM |
   | "Let me push back on that" | Testing conviction, not disagreeing — this is often a positive signal | HIGH |
   | Interviewer started selling the role/company to you | Strong buy signal — they want you interested | HIGH |
   | Short, closed-ended follow-ups | They may have already formed their assessment — neutral to negative | MEDIUM |
   | "We'll be in touch" with no specifics | Standard — don't read into it either way | LOW |

   Caveat: "These are common patterns, not certainties. Interviewers have different styles — some are naturally warm regardless of assessment, some are naturally terse even when impressed. Use these as directional signals, not verdicts."

   See also the Signal-Reading Module in `references/cross-cutting.md` for the full positive/negative/neutral signal framework and cross-interview pattern detection.

6. **Surprise capture + Format alignment check.** Ask three questions, one at a time per coaching Rule 1. The second and third questions feed the Round Format Verification Module (`references/cross-cutting.md`) as candidate-memory signals during `analyze` / `round` Step 3.7.

   1. "Was there anything you didn't expect? A question you weren't prepared for, a format difference, something about the interviewer or environment?" Unexpected moments are often the most informative for coaching.
   2. "We prepped for [expected format from the matching Interview Loop → Round formats entry, quoted if available]. Did the interview actually run that way, or did it go in a different direction?"
   3. "What did the interviewer NOT ask about that we were prepared for? Did they decline engagement with any topic you tried to bring up?"

   Capture answers as RFV input signals. If the candidate's memory suggests the round diverged materially from prep (e.g., interviewer declined prepped topics, ran a different format, focused on dimensions the prep did not anticipate), flag for `analyze` Step 3.7 as a pre-seeded Mismatch or Partial candidate. The candidate was in the room and can testify to what the interviewer refused to engage with — weight their memory heavily on scope boundary questions, even if the transcript alone would suggest a different verdict.
7. **Story usage log.** "Which stories did you use? Did any of them land differently than in practice?" Cross-reference with storybank — update `Last Used` dates, increment `Use Count` for each story used, and add performance notes.
8. **Immediate tactical notes.** "Is there anything you want to do differently for the next round, based on this one?" Capture their own coaching instinct.
9. **Positioning performance check.** "How did your introduction / 'tell me about yourself' land? Did the interviewer seem engaged, or did they jump to questions quickly?" Capture this signal — it feeds back to `pitch` for positioning iteration. Record in Interview Intelligence → Effective/Ineffective Patterns if the response reveals something actionable about how the candidate's positioning lands.
10. **Recruiter/interviewer feedback capture.** "Did you get any feedback from the recruiter about this round? Even informal comments — 'they really liked your background' or 'the interviewer had some concerns about X' — are valuable signal." If feedback exists, record it for the Recruiter/Interviewer Feedback table in Interview Intelligence.
11. **Past question similarity check.** Scan the Interview Intelligence Question Bank for questions similar to what the candidate recalled. If matches exist, note them briefly: "You've seen a prioritization question like Q2 before — at [Company] in Round [N]. Your score on that one was [X]." Only surface matches that are useful (same competency tested, score trajectory, or company pattern). Don't force connections.
12. **Transcript availability check.** "Do you have a recording or transcript? If so, we can do a full `analyze` later. If not, I'll work from what you've captured here." If they do have a transcript, mention the tool it came from so they know they can paste raw output: "You can paste the raw transcript directly from Otter, Zoom, Grain, or whatever tool you used — I'll detect the format and clean it up automatically."

### Late Debrief Protocol (>48 hours after interview)

Memory reconstruction is predictable. What survives past 48 hours: overall emotional read, interviewer behavior that was distinctive or unexpected, the one or two moments that stood out most (positive or negative), and general lessons. What compresses quickly: specific question wording, exact answers given, moment-to-moment scoring, subtle signals.

**Adapt the sequence as follows when running late:**

- **Skip step 4 (Per-question self-assessment)**: Don't ask "how did you feel about each answer?" — the per-question read is reconstructed at this point. Replace with: "What's one moment that stands out from the whole interview — positive or negative? Just one." This captures the most salient signal without encouraging false precision.
- **Emphasize signal reading (step 5)**: Interviewer behavior is more durable in memory than answer quality. Spend more time here.
- **Skip story usage log granularity**: Ask broadly "which stories came up?" rather than per-story performance assessment. Use Count can be incremented, but don't capture performance notes — they won't be reliable.
- **Skip positioning performance check (step 9)**: Too granular for late recall.
- **Adjust confidence level**: Throughout the debrief output, flag "Late debrief — [N] days post-interview. Impressions may be reconstructed. Treat signal-reading data as directional; answer-quality data is low-confidence."
- **>7 days — abbreviated form**: Only run steps 1 (emotional), 2 (timestamp), 5 (signals), 6 (surprises), 8 (tactical notes), 11 (past question check), 12 (transcript availability). Everything else is too compressed to be useful.

**What to tell the candidate**: "We're past the window where your moment-to-moment impressions are most reliable, so I'm going to focus on what memory tends to preserve accurately: interviewer signals, what surprised you, and overall lessons. Don't try to reconstruct specific answers — tell me what stood out."

### With vs. Without Transcript

**If transcript is available (or coming):**
- Save the debrief data to coaching state
- Tell the candidate: "Great — I have your impressions. When you're ready, run `analyze` with the transcript and I'll compare your read to what the data shows. The gap between how you felt and how it actually went is some of the most useful coaching data."
- The debrief becomes input to `analyze`, not a replacement for it

**If no transcript exists:**
- This debrief IS the data. Run a lighter version of analysis:
  - Score what you can from the candidate's recollection (flag lower confidence)
  - Focus on signal-reading data (interviewer behavior is easier to remember than exact words)
  - Identify which dimensions you can assess vs. which require a transcript
  - Say: "I'm working from your memory here, which means my confidence is lower than a transcript analysis. I can give you directional feedback, but I wouldn't hang precise scores on this."

### Emotional Triage

Based on the emotional check in step 1, adapt:

- **Candidate feels good**: Proceed normally. Capture data. Offer `analyze` or `thankyou` as next steps.
- **Candidate feels terrible**: Don't jump to tactical feedback. Acknowledge it: "That sounds rough. Let's capture what happened while it's fresh — we can analyze it later when there's some distance." Focus on capture, not coaching. Offer `hype` if another interview is coming soon. Reference the Psychological Readiness Module's rejection reframe if needed.
- **Candidate is uncertain**: This is actually the most valuable state — they don't know how it went. Say: "Uncertainty is normal. Let's capture the data and see what it actually tells us."

### Output Schema

```markdown
## Interview Debrief: [Company] - [Round]
- Interview date/time: [date + approximate time — e.g., "March 10, ~2pm"]
- Debrief captured: [date + time this debrief was run]
- Time since interview: [N hours / N days — determines protocol used]
- Protocol used: [Full / Late Debrief (48h–7d) / Late Debrief (>7d)]
- Interviewer(s):
- Format:
- Emotional read: [candidate's one-word + brief context]

## Questions Recalled
1. [Question as remembered]
   - Self-assessment: [strong / okay / rough]
   - Story used: [S### or none]
   - Notes:
2. [...]

## Interviewer Signals Observed
- Positive signals (interest, follow-ups, engagement):
- Negative signals (redirects, loss of interest, clock-checking):
- Neutral/ambiguous:

## Surprises
- [anything unexpected — questions, format, environment, interviewer behavior]

## Stories Used
| Story | Question | How It Landed (candidate read) |
|-------|----------|-------------------------------|

## Candidate's Own Takeaways
- What to do differently:
- What worked:

## Feedback Received
- Date:
- Company:
- Source: [recruiter / interviewer / hiring manager / none]
- Feedback: [verbatim or close to it]
- Linked dimension: [if mappable]

## Intelligence Notes
- Questions matched from past interviews: [any Question Bank matches, or "no prior data"]
- Company pattern observations: [anything learned about this company's interview approach]

## Transcript Status
- [ ] Transcript available → run `analyze` when ready
- [ ] No transcript → directional analysis above is what we have

**Recommended next**: `analyze` — run full transcript analysis while impressions are fresh (if transcript available). **Alternatives**: `thankyou`, `hype`, `progress`
```

### Coaching State Integration

Update `coaching_state.md` per the State Update Triggers in COACH.md:
- Storybank updates: Last Used dates, increment Use Count for each story used, performance notes
- Interview Loop updates: round completed, stories used, signals noted
- Outcome Log: add entry with Result: pending
- Interview Intelligence updates: recalled questions to Question Bank (marked "recall-only"), recruiter/interviewer feedback to Recruiter/Interviewer Feedback table, Company Patterns if new observations emerged
