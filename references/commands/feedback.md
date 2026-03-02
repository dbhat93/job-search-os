# feedback — Capture Feedback, Outcomes, and Corrections

A lightweight command for capturing information that arrives between structured workflows. Feedback does **capture**, not analysis. Analysis happens in `analyze`, `progress`, and `prep` when the data becomes relevant.

### When to Use

- Recruiter or interviewer sends feedback (formal or informal)
- Candidate learns an interview outcome (advanced, rejected, offer)
- Candidate wants to correct or adjust a previous coaching assessment
- Candidate remembers something from a past interview they want to log
- Candidate has meta-feedback about the coaching itself

### Input Type Detection

Classify the candidate's input into one of five types. If ambiguous, ask: "Is this recruiter feedback, an outcome update, or something else?"

---

### Type A: Recruiter/Interviewer Feedback

**Trigger**: Candidate shares feedback received from a recruiter, interviewer, or hiring manager.

**Capture process**:
1. Record the feedback as close to verbatim as possible. Ask: "Can you share exactly what they said? Even rough wording helps — paraphrasing loses signal." If the candidate's account is vague or thin, use guided extraction prompts: "Did they mention specific skills or experiences? Did they compare you to other candidates? Did they give any process feedback — like timeline, next steps, or what the team thought? Did they say anything about culture fit or team dynamics?" These prompts help candidates recall details they might otherwise skip.
2. Identify the source: recruiter, interviewer, or hiring manager.
3. Map the feedback to the most relevant scoring dimension(s) — but hold this lightly. Some feedback maps cleanly ("your answers were hard to follow" → Structure), some doesn't ("we went with a candidate with more domain experience" → external factor, not a coaching gap).
4. If the feedback contradicts the coach's assessment, note the discrepancy — don't dismiss it. External feedback is higher-signal than internal scoring. **This is a drift signal** — check whether the contradiction is isolated or part of a pattern. If 2+ pieces of external feedback contradict coach scoring on the same dimension, log it in `coaching_state.md` → Calibration State → Scoring Drift Log and flag for the next `progress` calibration check.

**State updates**:
- Add to Interview Intelligence → Recruiter/Interviewer Feedback table (Date, Company, Source, Feedback, Linked Dimension)
- Update Company Patterns if this reveals something about what the company values
- If feedback references a specific round, cross-reference with Question Bank entries for that round
- If feedback contradicts coach scoring, log the discrepancy in Calibration State → Scoring Drift Log

**Output**: Brief confirmation of what was captured, the dimension mapping, and any discrepancy with previous coaching assessment. If the feedback suggests a coaching pivot, say so: "This feedback suggests [X] matters more than we've been prioritizing. Worth revisiting in your next `progress` review." If the feedback points to a specific interviewer concern pattern, suggest: "`concerns` can help you build counter-evidence for this."

---

### Type B: Outcome Report

**Trigger**: Candidate reports advancing, being rejected, receiving an offer, or any status change in an active interview loop.

**Capture process**:
1. Confirm the company, role, and round.
2. Record the outcome: advanced / rejected / offer / withdrawn.
3. If rejected, ask: "Did they give any reason? Even 'no feedback provided' is worth recording."
4. If advanced, ask: "Do you know what's next? Format, timeline, interviewer?"

**State updates**:
- Update Outcome Log (Date, Company, Role, Round, Result, Notes)
- Update Interview Loops → relevant company entry (Status, Rounds completed)
- Update Interview Intelligence → Question Bank Outcome column for all questions from this company/round
- If advanced with next-round details, update Interview Loops → Next round
- If the loop status change affects pipeline priority, sync `state/pipeline.md` per the Stage Sync Protocol (see COACH.md). Specific mappings: Interview Loops Status "Applied" → pipeline Stage "Applied"; "Interviewing" → "Interviewing"; "Closed" (rejection) → "Closed"; "Offer" → "Offer". Also update: Last Activity date to today, and Round count if advancing. Ground truth: if coaching_state.md and pipeline.md contradict, coaching_state.md is authoritative.

**Output**: Brief confirmation of the update. If outcome data now meets the threshold for outcome-score correlation (3+ real interviews), mention it: "You now have enough real interview data for `progress` to show outcome patterns. Worth running when you're ready."

**Calibration trigger**: When the 3-outcome threshold is crossed, note that calibration is now possible: "With 3+ real interview outcomes, the system can now check whether practice scores are predicting real results. Run `progress` to see the calibration analysis." Update Calibration State → Calibration Status to "calibrating" if it was "uncalibrated" or "practice-calibrating."

#### Rejection Leverage

When the outcome is a rejection, the Challenge Protocol applies based on the candidate's directness level. See `references/challenge-protocol.md` → Rejection Leverage section for the graduated approach (Level 3 = retrospective assumptions only; Level 4 = assumptions + blind spots; Level 5 = full 3-lens retrospective). At Levels 1–2: standard emotional triage from the Psychological Readiness Module in `references/cross-cutting.md`.

---

### Type C: Coaching Correction

**Trigger**: Candidate disagrees with a previous score, assessment, or coaching recommendation.

**Capture process**:
1. Understand what they're correcting and why. Don't get defensive — the candidate has information the coach doesn't.
2. Evaluate the correction against the evidence:
   - **If the correction is warranted** (candidate provides new information, points out something missed): Acknowledge it, adjust the assessment, and update the relevant state. "You're right — I missed that context. That changes the Credibility read from a 3 to a 4."
   - **If the correction reflects a calibration gap** (candidate rates themselves higher than evidence supports): Hold the line on the assessment but acknowledge their perspective. "I hear you, and I understand why you see it differently. Here's what the evidence shows — [specifics]. Let's use this as a data point for your self-assessment calibration."
   - **If it's ambiguous**: Name it. "This could go either way. Here's the case for each read. I'll note your perspective alongside my assessment."
3. Record the exchange regardless of outcome — corrections reveal how the candidate processes feedback.

**State updates**:
- If assessment adjusted: update the relevant Score History entry or Storybank rating
- Record in Coaching Notes (Date, what was corrected, outcome)
- If pattern emerges (candidate consistently corrects in one direction), note in Active Coaching Strategy → Self-assessment tendency

**Output**: Acknowledgment of the correction, the evaluation, and what (if anything) changed. No defensiveness, no rubber-stamping.

---

### Type D: Post-Session Memory

**Trigger**: Candidate remembers a question, story detail, interviewer behavior, or other interview data after the debrief or analysis session has closed.

**The core problem with Type D**: Memory degrades fast. A candidate who remembers a question 3 days after the interview has a partial and reconstructed memory — they may remember the topic but not the exact wording, or the general thrust but not the follow-up. Capturing thin memories is still valuable (the topic is real), but they must be tagged with their reliability so downstream workflows don't treat recalled-days-later data the same as same-day data.

**Capture process**:
1. Identify what type of information it is:
   - A question they forgot during debrief → route to Question Bank
   - A story detail or new story → route to Storybank (suggest `stories` for full development)
   - An interviewer signal they remembered → route to Interview Loops
   - A company culture observation → route to Company Patterns

2. **Before accepting thin input, use guided elicitation.** If the candidate's memory is vague ("I think they asked something about conflict?"), don't just capture "conflict question — vague." Try to sharpen it:
   - "What part of the question do you remember most clearly — the topic, the way they phrased it, or what they seemed to be after?"
   - "Did they give you any context before asking, or was it direct?"
   - "What was your first instinct when you heard it — what did you think they were really testing?"
   - "Did you feel like you answered it well, or was it one that caught you off guard?"
   These prompts don't manufacture memory — they surface what's actually there. If nothing more comes out, capture what exists and tag accordingly.

3. **Tag with memory reliability**:
   - **Same day**: High reliability — candidate captured this within hours. Treat as close to first-hand data.
   - **1–2 days later**: Medium reliability — topic and general intent are likely accurate; exact wording less so. Note: "Recalled 1–2 days post-interview — topic reliable, wording reconstructed."
   - **3+ days later**: Low reliability — capture the topic and any details the candidate is confident about, but flag explicitly: "Recalled 3+ days post-interview — treat as directional. Do not weight exact wording in prep."

4. For questions routed to the Question Bank, add the memory reliability tag to the entry.

**State updates**:
- Route to the appropriate section as identified above
- If it's a question, add to Interview Intelligence → Question Bank with score "recall-only" AND memory reliability tag (Same-day / 1–2 days / 3+ days)
- If it changes a previous assessment meaningfully, flag it

**Output**: Brief confirmation of where the information was captured AND the reliability tag. "Captured that question in the Question Bank — tagged as 'recalled 3+ days later, directional only.' It's useful for prep context, but treat the wording as approximate." If it would benefit from further development, suggest the relevant command.

---

### Type E: Coaching Meta-Feedback

**Trigger**: Candidate provides feedback about the coaching itself — what's working, what isn't, what they want more or less of.

**Capture process**:
1. Listen without defensiveness. This is the most valuable type of feedback for improving the coaching relationship.
2. Classify: Is this about delivery (too direct, not direct enough), content (wrong focus area, missing something), or process (too structured, not structured enough)?
3. Identify any immediate adjustment that can be made.

**State updates**:
- Record in Meta-Check Log (Session, Candidate Feedback, Adjustment Made)
- If delivery feedback, consider adjusting Feedback Directness level in Profile
- If content feedback, evaluate against Active Coaching Strategy — does this warrant a pivot?
- Record in Coaching Notes if it reveals a preference the coach should remember

**Output**: Acknowledgment, any immediate adjustment made, and what will change going forward. "Got it — you want me to focus less on Structure and more on the stories themselves. I'll adjust. For the record, your Structure scores are strong enough that this makes sense."

---

### Design Principles

- **Capture first, analyze later.** Feedback captures data; `analyze`, `progress`, and `prep` are where that data becomes actionable. Don't over-analyze in the moment — confirm what was captured and move on.
- **Flexible output.** There's no fixed output schema for `feedback`. The confirmation adapts to the input type — sometimes it's one line, sometimes it's a paragraph. Match the weight of the output to the weight of the input.
- **Memory reliability is data.** A question recalled 3 days later is still worth capturing — the topic is real. But treating it with the same weight as a same-day recall misleads downstream prep. Tag everything Type D with reliability.
- **Optional next step.** After capturing, suggest the most natural next command if one is relevant. Don't force it.
- **Don't duplicate existing workflows.** If the candidate starts a full debrief during `feedback`, redirect: "This sounds like a full debrief — want to switch to `debrief` so we capture everything systematically?" Same for detailed corrections that become re-analysis — redirect to `analyze`.
