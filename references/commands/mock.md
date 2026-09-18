# mock: Full Simulated Interview (Firewalled Room)

A complete simulated interview (4 to 6 questions in sequence) with holistic feedback on the full arc, not just individual answers.

## Design principle: the room must not hold the answer key

A mock exists to change what you do in the real room, and it can only do that if the conditions it measures you under match the ones you will actually face. That makes realism the substrate, not a feature. The moment the interviewer softens a question, front-loads structure, telegraphs the rubric, or coaches between answers, every score it produces is measured under assisted conditions that will not exist on the day.

Earlier versions of this command asked ONE agent to hold the rubric, the storybank, and the gap analysis AND play the interviewer AND score. Realism rode on that agent choosing not to peek at material it was staring at. That is discipline, not structure, and it failed the same way every time: the interviewer fished for the rubric answer, interrogated a single thread, and anchored the score on how the room felt live.

This version firewalls the room. Three roles, three information boundaries:

- **Orchestrator** (the main session) holds everything: coaching_state, the rubric, the storybank, the gap analysis. It designs the scenario and briefs the interviewer with an in-world motive, never a rubric. It never speaks to the candidate in character.
- **Interviewer** (a scoped subagent, re-spawned every turn) holds only what a real interviewer holds: the resume, the JD, the role, and its motive. It never receives the rubric, the storybank, the gap list, the concern-as-a-rubric-item, or any score. It cannot leak what it never got.
- **Scorer** (a separate pass) reads the finished transcript with full context and writes the debrief before it sees the candidate's self-read, so the score is a fresh read of the tape, not the warm room it just created.

The firewall is the whole point. Do not collapse it back into one voice for convenience.

---

## Role 1: Orchestrator, scenario design (before any question)

Run silently, in the main session, before the mock starts.

1. **Format.** Ask for the format if unknown (behavioral screen, deep behavioral, panel, bar raiser, system design / case study, technical + behavioral mix; see the format taxonomy in `references/commands/prep.md`). For system design / case study and technical + behavioral mix, check Interview Loops in `coaching_state.md` for saved format data from `prep`; if it exists, use it; if not, run the Format Discovery Protocol (`references/commands/prep.md`) and save the result. **Load ONLY the format-UX branch you need** (see the branches at the end of this file). Do not load all six.
2. **Context.** Pull company, role, and round from `coaching_state.md` Interview Loops, or ask. If a `prep` brief exists for this company and round, use its culture read, interviewer intelligence, and format analysis to shape the persona and tone.
3. **Persona.** Pick a persona from `references/role-drills.md`, or build one from the real interviewer's profile if `prep` captured it. Give it a name, a functional lens, and a temperament.
4. **The one concern to pressure-test.** Choose the single highest-value doubt this room should probe. Pull it from Active Coaching Strategy (current bottleneck), the storybank gap analysis, or the company's likely concern (from `concerns` if it was run). This is the spine of the scenario. You will encode it as a motive, never as a rubric line.
5. **One planted curveball.** Design one moment that tests adaptability: a changed constraint mid-scenario, a skeptical push on a number, a question targeting a known story gap.
6. **The arc.** Real rounds open with a warm-up, not a hypothetical. Script the arc: warm-up and rapport, then the "why this company / why this role" opener, then the situations that carry the concern and the curveball, then hand the floor to the candidate's questions. The interviewer runs this arc; it does not dive straight into a case.
7. **Difficulty and tone.** Calibrate to the Drill Progression stage in `coaching_state.md` (do not run a max-intensity panel for a candidate who has not cleared constraint drills) and to the target company (a FAANG final and a Series A first call feel very different; see the tone notes below).

**Tone calibration:**
- Large tech: structured, high bar on specificity and metrics, interviewers often follow rubrics.
- Startups: conversational, care about adaptability and scrappiness, may go off-script.
- Consulting / finance: case-oriented, precision matters, presentation polish expected.

Now assemble the Interviewer Brief.

---

## The firewall (non-negotiable)

The Interviewer Brief is the ONLY thing the interviewer subagent ever receives, plus the growing transcript. It contains:

- The candidate's resume (the same document a real interviewer reads).
- The JD, the role title, and a one-line company description.
- The persona: name, lens, temperament.
- The **motive**: the concern encoded in-world, as a reason this character would push, never as a scoring dimension.
- The arc the interviewer should run.
- The behavior rules (below).

It NEVER contains: the five scoring dimensions or any rubric, the storybank, the gap analysis, coaching notes, the concern phrased as an evaluation target, prior mock scores, or the candidate's known weaknesses. If the interviewer knows the candidate's weak spot as a weak spot, it will telegraph it. A real interviewer has a hunch and a motive, not a diagnosis.

**Encode the concern as a motive, not a rubric.** Wrong (leaks the answer key): "test whether the candidate narrows to one to three recommendations before expanding." Right (a motive that produces the same pressure honestly): "you are a former BSA officer; you have met a lot of PMs who cannot make a call, so when someone lists options you push, 'if it were only your decision, what ships first?'"

### Interviewer Brief template

```
You are running a job interview. Stay fully in character for the entire conversation. You are a real person with a real motive, not an evaluator. You never break character, never give feedback, never explain what you are looking for, and never coach.

WHO YOU ARE: [persona name], [title / lens]. [Two lines of temperament and background that justify the motive.]

WHAT YOU ARE INTERVIEWING FOR: [role], at [company, one line].

THE CANDIDATE'S RESUME:
[paste resume]

THE JOB DESCRIPTION:
[paste JD or a faithful summary]

YOUR MOTIVE (what you privately care about, phrased in-world):
[the one concern, as a reason this character pushes. Never name a rubric dimension.]

HOW YOU RUN THE ROOM:
- Open with a genuine warm-up and rapport, then ask why this company and this role, then move into situations. Do not open with a hypothetical.
- Chase what is actually interesting in their real work. You have their resume; pull threads from it. Do not run a checklist.
- Ask a thread once, or twice if it is genuinely unresolved, then move on. Do not interrogate the same point three times.
- Stay inside what you, this person, would actually care about. Do not quiz them on a technical fact you would not know or gate on. If they say "I would find that out through discovery," that is a normal, good answer; react like a human and move on. Do not hunt for a specific token answer.
- Pursue a strong answer deeper because you are curious. Redirect a weak answer once, the way a real interviewer does ("say more about your specific role in that").
- One planted moment to include naturally when it fits: [the curveball].
- End by inviting their questions and answering a couple in character.

Keep your turns short and human. Output only what you say out loud (and brief stage directions like *[nods]* if useful). Never output analysis.
```

---

## Role 2: running the mock (per-turn scoped spawn)

The interviewer runs as a subagent that is re-spawned every turn, because a subagent returns once and cannot stay live between the candidate's answers. Each spawn is stateless and firewalled: it sees only the Brief plus the transcript so far, never the orchestrator's knowledge.

**The loop:**

1. Spawn a scoped subagent (via the Agent / Task tool) whose entire prompt is: the Interviewer Brief, then `TRANSCRIPT SO FAR:` and the running transcript, then `Produce only your next thing to say.` For the first turn the transcript is empty and it opens the arc.
2. Relay the interviewer's line to the candidate verbatim, prefixed with the persona name in bold.
3. Wait for the candidate's answer. Do NOT react, score, or coach. Append both the interviewer line and the candidate answer to the transcript.
4. Repeat. Spawn again with the updated transcript for the next question or follow-up.

**Orchestrator discipline during the loop:**
- Never inject your own knowledge into an interviewer turn. If you find yourself wanting the interviewer to ask about a specific weakness, stop: that is the leak. The motive already carries it.
- Never give feedback between questions. Note observations silently for the scorer.
- End the arc after the situations and the candidate's questions are done, or at 4 to 6 substantive beats, whichever is natural. A screen is shorter; a panel or onsite is longer.

**Panel format:** spawn one interviewer subagent per persona, or brief a single subagent to voice 2 to 3 named personas with distinct motives, and prefix each line with the persona name. Create moments where the personas' styles conflict (the Ally wants depth while the Time-Pressured Exec wants the bottom line). Archetypes live in `references/role-drills.md`.

---

## Role 3: self-assessment (before any scoring is revealed)

Keep this verbatim from prior versions. Before the scorer's debrief is shown, ask the candidate for their own read:

- "Before I share the debrief, how do you think that went overall: Strong Hire, Hire, Mixed, or No Hire?"
- "Which answer do you feel best about? Which was weakest?"
- "Anything you would do differently if you could run it again?"

Capture the answers. The delta between their read and the scorer's is coaching gold. Do not let the self-read influence the score (the scorer runs blind, below).

---

## Role 4: blind scorer (separate pass)

Score in a pass that reads the finished transcript with full context, and produce the score before folding in the self-read.

1. Take the complete transcript and evaluate it with everything the orchestrator holds: the Core Rubric and the Context-Sensitive Scoring Module (`references/cross-cutting.md`), the candidate's seniority band, the Active Coaching Strategy, the storybank (for story diversity and gap-handling), and the JD. This is the read that was withheld from the interviewer.
2. Score each unit blind to the candidate's self-assessment. The interviewer never scored anything; the score is a fresh read of the tape, not an anchor from the live room. This is deliberate: a warm room inflates, and fluency is not the same as fit to the scored skill.
3. Then compute the self-read delta (over / under / accurate) against the self-assessment captured in Role 3.
4. Write the debrief using the schema below.

---

## Redo (core step, not optional)

The corrected rep under the same cold conditions is the part that actually rewires behavior, so it is required, not a garnish. After the debrief:

1. Name the weakest answer. "Your answer to [unit] had the most room. We are going to run it again now, same conditions."
2. Re-spawn the interviewer with the Brief and a minimal transcript that reproduces the setup for that one question, and have it ask the question in character.
3. The candidate answers again. Score it blind, the same way, and show the before / after on the relevant dimensions.
4. One redo per mock. This is not a full practice session.

---

## Post-Mock Debrief Schema

```markdown
## Mock Interview Debrief: [Format] - [Company/Role]

## Overall Impression
- Hire Signal: Strong Hire / Hire / Mixed / No Hire
- One-sentence summary of how this interview would land:
- Self-read delta: [candidate said X; the tape reads Y; over / under / accurate]

## Arc Analysis
- Energy trajectory: Started [high/medium/low] to Ended [high/medium/low]
- Story diversity: __ unique stories across __ questions (flag if <80% unique)
- Pacing: [rushed / well-timed / dragged]
- Answer length distribution: [consistent / front-loaded / back-loaded / erratic]

## Per-Unit Scorecard
Use the unit ID for the format: Q# behavioral, E# panel exchange, P# system-design phase, CS# case stage.

### Q1/E1/P1/CS1
- Context: [Question Type] x [Interviewer Type]
- Scores: Substance __ / Structure __ / Relevance __ / Credibility __ / Differentiation __
- Weighted composite: [X.X / 5] (weights per Context-Sensitive Scoring Module in `references/cross-cutting.md`)
- Format-specific scores (if applicable): [e.g., Process Visibility __ / Scoping Quality __]
- Strongest moment:
- Missed opportunity:

[...repeat per unit]

## Holistic Patterns (only visible across the full interview)
- Repeated crutch phrases:
- Topics avoided:
- Questions that caused visible hesitation:
- Answered a different question than the one asked (flag each instance):
- Best moment of the interview:
- Worst moment and recovery quality:

## Signal Reading Notes
- Questions where the interviewer followed up (positive signal):
- Questions where the interviewer moved on quickly (negative signal):
- Questions where the interviewer redirected (answer was not landing):

## Interviewer's Inner Monologue
[Replay key moments from the interviewer's real-time perspective, grounded in the candidate's literal words. See the how-to below.]

## Format-Specific Debrief (include when applicable)
[Pull the matching block from the format branch that was loaded.]

## Challenge (Levels 3 to 5 only; see `references/challenge-protocol.md` Mock Debrief Challenge)
[Level 3: Assumption Audit, one sentence]
[Level 4: Assumption Audit + Blind Spot Scan]
[Level 5: Lenses 1 to 4 + Expanded Inner Monologue + Avoidance Detection if applicable]

## Top 3 Changes for Next Mock
1.
2.
3.

**Recommended next**: `[command]`, [reason from the debrief]. **Alternatives**: `mock [same format]`, `practice [drill]`, `practice technical`, `analyze`
```

### Writing the Interviewer's Inner Monologue

The monologue is the most powerful teaching tool in the debrief, because it shows the candidate the evaluative reactions they cannot normally see. Ground every beat in the candidate's actual words. Quote what they said, then show the reaction:
- "When you said 'we decided to pivot,' my first thought was: who is 'we'? Did you drive this or watch it?"
- "The moment you said 'we reduced churn 40%,' the first real number in four answers, my confidence in everything jumped."

Include both positive and negative reactions. Show the pivot points where the overall impression shifted. Connect to signal-reading (why the interviewer followed up on one thread and moved on from another). Calibrate the lens to the company and role. Because the interviewer ran firewalled, this monologue is reconstructed by the scorer from the tape, which is exactly a real interviewer's post-hoc write-up.

### Level 5 additions

1. **Expanded inner monologue:** include the uncomfortable truths, the moments the interviewer wrote the candidate off or considered ending early. Do not soften.
2. **Holistic Challenge (Lenses 1 to 4; see `references/challenge-protocol.md`):** Assumption Audit (name every assumption the performance disproves) and Blind Spot Scan (the pattern the candidate is not seeing that a hiring committee would).
3. **Avoidance Detection:** if the candidate chose a safe format and avoided a known-weak one, name it. The growth is in the uncomfortable mock.

---

## Coaching State Integration

After the debrief:
1. **Add scores to Score History.** Type = mock. Interview_Type is required (behavioral / live_case / technical_behavioral / system_design / presentation / hybrid). Include the Hire Signal.
2. **Record the self-read delta** (over / under / accurate).
3. **Update Active Coaching Strategy** if the mock confirms, contradicts, or reveals a pattern. Preserve the previous approach before writing the new one.

---

## Format branches (load only the one you need)

### Panel simulation UX
Named personas, distinct motives, prefix each line with the persona name in bold. Switch naturally; engineer a style conflict between personas. Archetypes in `references/role-drills.md`. Spawn one subagent per persona, or one briefed to voice all of them.

### System design / case study simulation UX
Check Interview Loops for saved format data from `prep`; if none, run Format Discovery (`references/commands/prep.md`) and save it; if still unknown, default to a verbal walkthrough and say so.

**State the coaching boundary at setup** (orchestrator says this to the candidate, out of character): "In this mock I am scoring your communication process, how you scope, structure, reason, and articulate tradeoffs. I am not scoring the technical correctness of your solution. For that, practice with a domain peer."

Interviewer-brief adjustments for this format: present an open-ended problem; do not prompt the candidate to ask clarifying questions (note silently whether they scope before solving); behave like an interviewer (occasional clarifying questions, no coaching); probe tradeoffs ("why this over X", "what breaks at 10x", "what are you optimizing for and sacrificing"); test adaptability with a changed constraint. This is the format where the interviewer must most strictly obey "I would discover that is a valid answer" and "do not gate on a correctness token," because the coach's value here is the communication layer, not the solution (see Technical Format Coaching Boundaries in `references/commands/prep.md`).

Scorer tracks: clarification behavior, approach structure, reasoning narration, tradeoff articulation, adaptability, time management, uncertainty handling. Add the format-specific debrief block (process visibility, clarification, tradeoff articulation, approach structure, uncertainty handling) and repeat the boundary reminder.

### Technical + behavioral mix simulation UX
Run Format Discovery with the split questions (technical / behavioral ratio, alternating vs segmented, one interviewer or a handoff). Default to alternating with one interviewer.

**State the coaching boundary at setup:** "I am scoring how you switch between modes, storytelling on the behavioral parts and clarity on the technical parts, and how well they reinforce each other. I am not scoring technical correctness."

Interviewer-brief adjustments: structure the arc to match the described split; include at least one deliberate mode switch inside a single question ("tell me about a hard technical tradeoff, and walk me through both the people side and the technical side"); vary transitions (some clean breaks, some seamless pivots). Scorer tracks: mode-switching fluidity, register appropriateness, integration quality, energy trajectory across a 50 to 70 minute marathon, and which mode is stronger. Add the format-specific debrief block and the boundary reminder.

### Case study (candidate-driven) note
For consulting-style cases where the candidate drives the analysis, use the system-design protocol above; the communication coaching transfers, but say plainly that full case practice (market sizing, framework application, exhibit analysis) needs a domain-specific resource alongside this.
