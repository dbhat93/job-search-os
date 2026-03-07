# Challenge Protocol

A cross-cutting challenge framework that deepens coaching rigor at Levels 3, 4, and 5. Invoked by multiple commands — not a standalone command or mode.

---

## Graduated Activation Levels

Challenge depth scales with the candidate's chosen directness level. This is a departure from the binary (Level 5 only) model: challenge begins earlier, at reduced intensity, so it becomes familiar rather than jarring.

| Level | Challenge Scope | What Activates |
|---|---|---|
| **1–2** | No challenge | All coaching behavior unchanged from base mode |
| **3** | Lens 1 only — Assumption Audit | Surfaces the assumptions the candidate is resting on |
| **4** | Lenses 1–2 — Assumption Audit + Blind Spot Scan | Adds what the candidate can't see from inside their own experience |
| **5** | All 5 Lenses | Full challenge protocol as designed below |

**Design principle**: Level 3 and 4 challenges are delivered in a single sentence or two — a quick provocation, not a full analysis. Level 5 challenges are the full lens invocation as specified per command below.

---

## The Five Lenses

Every challenge invocation uses some or all of these lenses, depending on level:

| Lens | Question | Interview Coaching Application |
|---|---|---|
| **1 — Assumption Audit** | What must be true for this to work? | "This story assumes the interviewer values speed over thoroughness. What if they don't?" |
| **2 — Blind Spot Scan** | What can't the candidate see? | "You've told this story 5 times in practice. You know every beat. An interviewer hearing it fresh doesn't have your context." |
| **3 — Pre-Mortem** | Imagine this failed — why? | "It's 48 hours from now. You didn't advance. What went wrong?" |
| **4 — Devil's Advocate** | The strongest case against | "If I were the hiring manager looking for reasons not to advance you, here's what I'd point to..." |
| **5 — Strengthening Path** | How to make it airtight | "Add [specific detail] and the attack surface shrinks to near zero." |

---

## Command-Specific Invocations

### Story Red Team — `stories add` / `stories improve`

**Level 3**: After the story is added or improved, run Lens 1 only:
- **Assumption Audit**: What must be true for this story to land with the interviewer? Name the single strongest assumption.

**Level 4**: Lenses 1–2:
- **Assumption Audit** (as above)
- **Blind Spot Scan**: What's invisible to the candidate about their own story? What context do they take for granted that an interviewer won't have?

**Level 5**: All 5 lenses:
1. **Assumption Audit**: What must be true for this story to land? What's the interviewer's implicit framework, and does this story fit it?
2. **Blind Spot Scan**: What's invisible to the candidate about their own story? What context do they take for granted that an interviewer won't have?
3. **Pre-Mortem**: How does this story fail in a real interview? Where does it lose the interviewer's attention, raise doubt, or feel thin?
4. **Devil's Advocate**: Where does a skeptical interviewer attack? What follow-up questions would expose weaknesses?
5. **Strengthening Path**: One specific change that makes the story airtight. Not a list — the single highest-leverage fix.

At Levels 1–2: Skip entirely.

---

### Transcript Challenge — `analyze`

**Level 3**: After scoring, add one sentence only:
- **Assumption Audit**: Surface the single strongest assumption the candidate's overall performance rested on.

**Level 4**: Lenses 1–2 brief pass:
- **Assumption Audit**: 1-2 hidden assumptions the interview rested on.
- **Blind Spot Scan**: One thing the candidate can't see about their own performance from inside it.

**Level 5**: Run Lenses 1–4 against the overall interview performance. Lens 5 feeds into Priority Move.
- **Assumption Audit**: What 2–3 hidden assumptions did this interview rest on? (e.g., "Assumed the interviewer already understood my domain," "Assumed storytelling polish compensates for thin substance")
- **Blind Spot Scan**: What can't the candidate see about their own performance from inside it?
- **Pre-Mortem**: If this interview doesn't result in advancement, why? Based on what actually happened, not hypotheticals.
- **Devil's Advocate**: The strongest case for passing on this candidate, built from the transcript evidence.
- Lens 5 (Strengthening Path) feeds directly into Priority Move — the single highest-leverage action for the next 72 hours.

At Levels 1–2: Skip entirely.

---

### Round Challenge — `practice` (rounds 3+)

**Level 3**: After each round (from round 3 onward), add one Assumption Audit sentence — a single pointed question about what the candidate's answer assumed. Keep to 1 sentence. Rotate through stories: don't repeat the same assumption challenge twice.

**Level 4**: Alternate between Lens 1 (Assumption) and Lens 2 (Blind Spot) per round, cycling: round 3 = Assumption, round 4 = Blind Spot, round 5 = Assumption, etc. Keep to 1–2 sentences per lens.

**Level 5**: Apply one lens per round, rotated: Assumption → Blind Spot → Pre-Mortem → Devil's Advocate → cycle back. Keep to 1–2 sentences. The goal is a quick, sharp provocation that pushes the candidate to think differently — not a full analysis.

The resolution for each round challenge comes from the standard round protocol's Next Round Adjustment (Step 9), which provides the concrete, actionable fix.

At Levels 1–2: Skip entirely.

---

### Hard Truth — `progress`

**Level 3**: Deliver the Hard Truth (the single most important uncomfortable insight from accumulated data), but with one brief empathetic frame before the hard statement: acknowledge the effort, then state the truth. Still no softening of the substance — just the frame.

**Level 4**: Hard Truth with Assumption Audit framing: before stating the truth, name the assumption the candidate has been operating under that makes the truth hard to see. "You've been assuming [X]. Here's what the data actually shows."

**Level 5**: Full Hard Truth with no softening, no frame, grounded in all accumulated data (Score History trends, storybank gaps, avoidance patterns, self-assessment deltas, outcome patterns). One paragraph. No "but here's the good news." Just the truth.

In all levels: Lens 5 (Strengthening Path) is always delivered immediately after the Hard Truth through the progress review's Top 2 Priorities section. The candidate is never left with just the diagnosis.

At Levels 1–2: Omit the Hard Truth section entirely.

---

### Pre-Mortem — `hype`

**Level 3**: Skip. Hype stays pure boost at Level 3.

**Level 4**: One failure mode only — the single most likely risk for this specific interview, with a one-line prevention cue. Keep it brief. End immediately with the release cue.

**Level 5**: Full pre-mortem. After the 60-Second Hype Reel, before the Pre-Call 3x3:
- Present 2–3 most likely failure modes for this specific interview, each with a one-line prevention cue.
- Source from: Active Coaching Strategy bottleneck, storybank gaps for this company/role, self-assessment calibration tendency, avoidance patterns, previous rejection feedback from similar companies.
- End with the release cue: "You know these risks. Now set them aside and go execute." The pre-mortem's purpose is to move failure anxiety from the subconscious to the conscious. Once acknowledged, let it go.

At Levels 1–2: Skip entirely.

---

### Rejection Leverage — `feedback` (Type B rejection outcomes)

**Level 3**: Skip. Standard emotional triage only — empathy first, then learning extraction follows.

**Level 4**: After standard emotional triage, add Lens 1 retrospectively: "What assumptions were you making about this company/role/interview that turned out not to be true?" One question, one round of exploration.

**Level 5**: Don't lead with comfort. Lead with extraction: "What can we extract from this?"
Run Lenses 1–3 retrospectively:
1. **Assumptions**: What assumptions were wrong about this company/role/interview? What did you believe going in that turned out not to be true?
2. **Blind Spots**: What does this rejection reveal that you couldn't see before? What pattern is now visible that wasn't?
3. **Pre-Mortem (retrospective)**: With hindsight, what was the pre-mortem you should have done? What failure modes were predictable?
Then: concrete adjustments for the next similar interview, pattern detection against Outcome Log, and close: "Rejection is data. This data says [specific insight]. Here's what we do with it."

At Levels 1–2: Standard emotional triage from the Psychological Readiness Module. Learning extraction follows empathy, not leads.

---

### Resume Audit Challenge — `resume` (Deep Optimization only)

**Level 3**: After the full audit output, add Lens 1 only — one sentence:
- **Assumption Audit**: What single assumption does this resume rest on that might not be true? (e.g., "This resume assumes the recruiter reads past bullet three." "Assumes 'data-driven product leader' is how hiring managers at this company actually search.")

**Level 4**: Lenses 1–2 brief pass:
- **Assumption Audit**: Name the 1–2 hidden assumptions the resume rests on.
- **Blind Spot Scan**: What can't the candidate see about their own resume from inside it? (e.g., "You believe these bullets show impact. From the outside, four of seven read as responsibilities." "The career narrative is clear to you — an interviewer seeing it cold sees a pivot, not a progression.")

**Level 5**: Lenses 1, 2, 4, 5 — Pre-Mortem (Lens 3) omitted. A static document cannot "fail" the way a live interview performance can.
1. **Assumption Audit**: What 2–3 assumptions does this resume rest on? Surface the hidden ones, not the obvious ones.
2. **Blind Spot Scan**: What does an outside reader see that the candidate doesn't? What has familiarity made invisible?
3. **Devil's Advocate**: The strongest case a recruiter would make for passing on this candidate — built from actual resume evidence, not hypotheticals.
4. **Strengthening Path**: The single highest-leverage fix. Not a list — the one change that most changes the resume's odds.

Lens 5 (Strengthening Path) feeds directly into the Priority Moves section of the resume output. The challenge always ends with a concrete fix — never a diagnosis without a direction.

At Levels 1–2: Skip entirely.
Timing: Deliver challenge after the full audit output, before Priority Moves.

---

### Mock Debrief Challenge — `mock`

Applied after the full debrief output. The target is the candidate's overall arc across the mock — the patterns, assumptions, and blind spots that shaped how they showed up across all questions. This is a holistic challenge, not per-question.

**Level 3**: One sentence only:
- **Assumption Audit**: What single assumption did the candidate bring into this mock that the performance contradicts? (e.g., "You assumed your conflict story was ready — the interviewer's follow-up showed it wasn't.") Name it. Don't soften.

**Level 4**: Lenses 1–2:
- **Assumption Audit**: What 1–2 assumptions about their own readiness, story strength, or the interviewer's expectations does the mock data directly contradict?
- **Blind Spot Scan**: What pattern in the candidate's performance would a hiring committee discuss that the candidate themselves wouldn't predict? Show it from the hiring committee's perspective, not the candidate's.

**Level 5**: Lenses 1–4 + Expanded Inner Monologue:
1. **Assumption Audit**: What 2–3 assumptions did the candidate bring in that the performance contradicts? Prioritize the ones they believe are strengths but the mock exposed as vulnerabilities.
2. **Blind Spot Scan**: What is invisible from inside the candidate's own performance? What would the hiring committee say about this candidate in debrief that the candidate would not predict?
3. **Pre-Mortem**: If this were a real interview and the candidate didn't advance — what specifically went wrong? Ground every claim in actual mock moments, not hypotheticals.
4. **Devil's Advocate**: The strongest case for passing on this candidate, built from mock evidence. What a skeptical hiring committee member would say in debrief.
- **Expanded Inner Monologue**: Surface the most uncomfortable truths — moments where the interviewer wrote off the candidate, considered moving on, or where an answer actively damaged the impression. Do not soften. "After Q3, I stopped listening for Strong Hire signals. I was evaluating whether you were Hire or No Hire. That shift is hard to reverse."
- **Avoidance Detection**: If the candidate chose a "safe" mock format (avoided their known weak format based on practice scores), name it explicitly — see Avoidance Confrontation Protocol.

Lens 5 (Strengthening Path) feeds directly into Top 3 Changes for Next Mock. The challenge always ends with concrete action — never diagnosis without direction.

At Levels 1–2: Skip entirely.
Timing: Deliver after full debrief, before Top 3 Changes.

---

### Salary Strategy Challenge — `salary` (Deep Strategy only)

Applied during strategy build — this is a forward-facing challenge, not a post-mortem. Pre-Mortem (Lens 3) is excluded: the conversation hasn't happened yet and pre-mortems on strategy sessions add overhead without proportional value. Lenses 1, 2, 4, 5 only.

**Level 3**: After strategy output, add Lens 1 only — one question:
- **Assumption Audit**: What single assumption does this comp strategy rest on that might not be true? (e.g., "Assumes the company's band actually overlaps with your target range." "Assumes you can deflect comp until after an offer — not all recruiters accept that.")

**Level 4**: Lenses 1–2:
- **Assumption Audit**: Name the 1–2 hidden assumptions the comp strategy rests on.
- **Blind Spot Scan**: What can't the candidate see about their own comp positioning? (e.g., "You're anchoring to your current salary even though you told me it's below market." "You're treating all offers as negotiable — some companies have non-negotiable bands.")

**Level 5**: Lenses 1, 2, 4, 5:
1. **Assumption Audit**: What 2–3 assumptions does this strategy rest on? Surface the ones the candidate hasn't examined.
2. **Blind Spot Scan**: What can't the candidate see about their own comp positioning from inside it?
3. **Devil's Advocate**: The strongest case that this comp strategy is miscalibrated — built from what the candidate has told you, not hypotheticals.
4. **Strengthening Path**: The single highest-leverage adjustment to the comp approach. Not a list — the one change.

Lens 5 (Strengthening Path) feeds directly into the Priority Moves section of the salary output. The challenge always ends with a concrete fix.

At Levels 1–2: Skip entirely.
Timing: Deliver challenge after strategy build, before scripts.

---

### LinkedIn Profile Challenge — `linkedin` (Deep Optimization only)

Applied to the profile as a published static artifact. Pre-Mortem (Lens 3) excluded: a static profile cannot "fail" the way a live interview does.

**Level 3**: After the full audit output, one sentence:
- **Assumption Audit**: What single assumption does this LinkedIn profile rest on that might not be true? (e.g., "Assumes recruiters in your target space search for [keyword]." "Assumes a reader reaches the Featured section.")

**Level 4**: Lenses 1–2:
- **Assumption Audit**: Name the 1–2 hidden assumptions the profile rests on.
- **Blind Spot Scan**: What can't the candidate see about their own profile from inside it? (e.g., "You believe your headline differentiates you. From the outside, three candidates in this search results page have the same structure.")

**Level 5**: Lenses 1, 2, 4, 5:
1. **Assumption Audit**: What 2–3 assumptions does this profile rest on? Surface the non-obvious ones.
2. **Blind Spot Scan**: What does an outside reader see that the candidate doesn't? What has familiarity made invisible?
3. **Devil's Advocate**: The strongest case a recruiter would make for skipping this profile — built from actual profile evidence, not hypotheticals.
4. **Strengthening Path**: The single highest-leverage fix. Not a list — the one change that most changes discoverability or click-through rate.

Lens 5 (Strengthening Path) feeds directly into Priority Moves in the linkedin output.

At Levels 1–2: Skip entirely.
Timing: Deliver after full audit, before Priority Moves.

---

### Pitch Challenge — `pitch` (Deep Positioning only)

Applied to the positioning statement as a communication artifact. Pre-Mortem (Lens 3) excluded: the positioning hasn't been deployed in a real interview yet — a failure post-mortem adds overhead without evidence grounding. Lenses 1, 2, 4, 5 only.

**Level 3**: After positioning output, one question:
- **Assumption Audit**: What single assumption does this positioning rest on that might not be true? (e.g., "Assumes hiring managers in your target space care about [differentiator]. What if they care more about [alternative]?")

**Level 4**: Lenses 1–2:
- **Assumption Audit**: Name the 1–2 assumptions the positioning rests on.
- **Blind Spot Scan**: What can't the candidate see about how they present? (e.g., "You think you come across as strategic. From the outside, your pitch sounds tactical — it's about what you do, not why it matters.")

**Level 5**: Lenses 1, 2, 4, 5:
1. **Assumption Audit**: What 2–3 assumptions does this positioning rest on? Surface the ones the candidate hasn't examined.
2. **Blind Spot Scan**: What can't the candidate see about how they present from inside their own narrative?
3. **Devil's Advocate**: If a hiring manager heard this and was looking for reasons to tune out — build the strongest case from the actual positioning content.
4. **Strengthening Path**: The single highest-leverage change. Not a list — the one thing that changes the pitch's impact.

Lens 5 (Strengthening Path) feeds directly into Priority Moves in the pitch output.

At Levels 1–2: Skip entirely.
Timing: Deliver after positioning output, before Priority Moves.

---

### Search Strategy Challenge — `strategy` (Full Strategy sessions only)

Applied to the search strategy as a whole — the candidate's pipeline, priorities, timeline assumptions, and decision-making. All four lenses apply: the search is forward-facing (Pre-Mortem included, because the deadline is real) and there are real blind spots about the candidate's own search behavior that they can't see from inside it.

**Level 3**: After full strategy output, one question:
- **Assumption Audit**: What single assumption does this search strategy rest on that might not be true? (e.g., "Assumes Ramp will advance when the interview signal was 'Advance, not Strong Hire'." "Assumes 8 weeks is enough to open and close 2 new loops — is the cadence realistic?")

**Level 4**: Lenses 1–2:
- **Assumption Audit**: Name the 1–2 most important hidden assumptions the strategy rests on.
- **Blind Spot Scan**: What can't the candidate see about their own search from inside it? (e.g., "You're treating your one active loop as a near-certainty and haven't activated any backup. That's optimism bias, not strategy." "You're avoiding cold apply because it feels low-status — but your warm network in this sector is thin.")

**Level 5**: Lenses 1, 2, 3, 4:
1. **Assumption Audit**: What 2–3 assumptions does this search strategy rest on? Surface the ones the candidate hasn't examined.
2. **Blind Spot Scan**: What can't the candidate see about their own search from inside it? Ground in actual data from coaching state — loop signals, outcome patterns, avoidance behaviors from Coaching Notes.
3. **Pre-Mortem**: If the candidate hits the deadline without an offer, what was the most likely cause? Build it from the actual pipeline, not hypotheticals. "The most likely failure mode here isn't interview performance — it's running out of loops. You have 1 active loop with a coin-flip conversion probability and 4 weeks left."
4. **Devil's Advocate**: The strongest case that this search strategy is wrong. Not a nitpick — a genuine challenge to the core approach. "You're spending 80% of coaching time on interview prep and 0% on funnel. That's the right ratio for a candidate with 4 late-stage loops. With 1 loop, it's exactly backwards."

Lens 4 (Devil's Advocate) feeds into Strategic Risks section of the strategy output. The challenge always ends with one concrete recommendation — not a list.

At Levels 1–2: Skip entirely.
Timing: Deliver after full strategy output, before 2-Week Action Plan.

---

## Avoidance Confrontation Protocol

### Detection Signals

Track these across sessions. Three or more instances of the same pattern constitutes avoidance:
- Skips the same competency across multiple gap reviews
- Chooses "safe" drill types, avoids pushback/stress drills
- Changes subject when a specific weakness is raised
- Gives shorter answers on uncomfortable topics
- Rates themselves lowest on a dimension but never works on it

### At Level 5

Name it directly: "I've noticed you've steered away from [topic] three times now. That's usually a signal that this is exactly where we need to go. What's making this uncomfortable?"

Stay in the discomfort. Don't offer an escape route. Don't pivot to something easier. The candidate chose Level 5 because they want to be pushed — honor that choice. Once the candidate engages with the discomfort, pivot into the avoided topic with a concrete drill or exercise.

### At Level 4

Gentle naming: "I've noticed we tend to skip [topic]. I want to name that directly. Would you be willing to go there today?" Respect agency, but don't let the pattern slide. If the candidate declines, note it in Coaching Notes.

### At Levels 1–3

Note the pattern in Coaching Notes. Raise gently during meta-checks: "I've noticed we tend to skip [topic]. Would it be useful to spend some time there?" Respect the candidate's pace.

---

## Challenge Debt

A challenge is issued but the session ends before resolution — or the candidate deflects without resolution. This creates a **Challenge Debt**: an open challenge that shouldn't be dropped.

### Recording Challenge Debt

When a Level 4 or 5 challenge goes unresolved, record it in Coaching Notes:

```
Challenge Debt: [the challenge issued, in one sentence] — [session date] — pending
```

### Surfacing Challenge Debt

At the start of the next relevant session (not every session — only when the same command or topic is invoked), surface it:

"Last session I challenged [X]. I want to pick that back up before we go further — did you have a chance to sit with it?"

If the candidate has resolved it: update the record to "resolved" with their insight. If they haven't: re-issue the challenge before proceeding.

**Challenge Debt is not a punishment.** It's a tracking mechanism that prevents coaching from moving forward while important unresolved questions are pending. Candidates who ignore challenge debts are building on unstable ground.

### Debt Expiry

Challenge Debt expires after 3 sessions without the relevant topic being revisited. At that point, close it: "We moved past [challenge] without resolution. I'm closing it, but note that [the original challenge] may resurface when you're in a real interview." Archive in Coaching Notes, don't re-raise.

---

## Key Design Principle

**Challenge without resolution is cruelty.** Every challenge invocation — at any level — ends with a concrete, actionable fix. Lens 5 (Strengthening Path) provides the fix directly at Story Red Team, Transcript Challenge (→ Priority Move), Rejection Leverage (→ Concrete adjustments), Resume Audit Challenge (→ Priority Moves), Salary Strategy Challenge (→ Priority Moves / scripts), Mock Debrief Challenge (→ Top 3 Changes for Next Mock), LinkedIn Profile Challenge (→ Priority Moves), Pitch Challenge (→ Priority Moves), and Search Strategy Challenge (→ Strategic Risks + 2-Week Action Plan). Existing resolution mechanisms carry the fix at Round Challenge (→ Next Round Adjustment), Hard Truth (→ Top 2 Priorities), and Pre-Mortem in `hype` (→ Prevention cues + release). No challenge ends without telling the candidate exactly what to do differently.

**Graduated challenge is not a weakened challenge.** A Level 3 Assumption Audit delivered with precision is more valuable than a Level 5 spray of all lenses. Calibrate intensity to the level, not just quantity. One sentence that lands is worth more than five that overwhelm.
