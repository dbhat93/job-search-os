## Round Format Verification Module (RFV)

Different interviewers run different rounds even inside the same loop. A round that was prepped as a product rigor test can in practice be a culture chat; scoring the transcript against the prepped rubric manufactures false post-mortems (manufactured gaps that don't correspond to anything the interviewer actually evaluated). RFV verifies that the actual round format matches the prepped expected format before scoring runs. This module exists to prevent prior-prep anchoring bias — the pattern where the coach reads coaching_state.md first, then scores the transcript against the primed rubric without ever checking whether the rubric applied.

**When to run:**
- `analyze` Step 3.7 (inserted after Step 3.5 tool-format detection, before cleaning)
- `round` Phase 5A (entry into analyze workflow; also referenced at Phase 6 Step 6.0)
- `debrief` Step 4 (candidate-memory input pass — extended prompts surface expected vs. actual format divergence)

**Inputs:**
1. **Expected format** — LLM-interpreted from `coaching_state.md` → Interview Loops → [matching loop] → Round formats freeform text. Extract: (a) expected dimensions the round was prepped to test, (b) expected interviewer mandate (per HM guidance if captured), (c) expected topics/openings the candidate was briefed on, (d) what would count as scope mismatch if recorded.
2. **Actual interviewer behavior** — from transcript. Detect: (a) topics the interviewer pursued vs. declined, (b) explicit refusals ("we don't need to look at that", "No I'm good", "let's not go there"), (c) question distribution across dimensions, (d) time share per topic, (e) whether prepped openings actually materialized, (f) interviewer's effective evaluation scope based on where they invested follow-ups.
3. **Candidate memory (optional)** — from debrief Step 4 extended prompts. The candidate was in the room and can testify to scope boundaries the transcript alone may understate.

**Verdict levels:**

| Verdict | Criteria | Downstream behavior |
|---|---|---|
| **Match** | ≥75% of expected dimensions were actually tested; no significant declined topics; interviewer ran the format the prep anticipated | Standard scoring. All gap identification rules apply normally. |
| **Partial** | 40–74% overlap; some prepped axes tested, some declined or absent; interviewer partially ran the prepped format but drifted or added new axes | **Soft warn.** Scoring proceeds. Output includes format-mismatch banner. "No Gap Without An Opening" rule applied strictly. Bottleneck findings tagged "Provisional." |
| **Mismatch** | <40% overlap; interviewer explicitly declined prepped topics; round ran a substantially different format (e.g., prepped for product rigor, actual was culture chat) | **Block and confirm.** Halt scoring output generation. Surface the mismatch to the candidate: "Prep expected [X]. Transcript shows [Y]. Interviewer [declined/did not engage with Z]. Should I score against the actual round's rubric instead of the prepped one?" Wait for explicit user confirmation. On confirmation, proceed with actual-format scoring; Primary Bottleneck refuses to update (see Active Coaching Strategy gate in `analyze.md` Step 15). |
| **Unknown** | Thin prep data (no `Round formats` entry, freeform too vague to parse), freestyled round, or insufficient signals to classify | Soft warn. Proceed with scoring at downgraded confidence. Flag "Scope Alignment: Unknown" throughout output. Primary Bottleneck does not update. |

**Detection rules:**
1. Parse expected-format signals from the `Round formats` entry for the matching loop/round. If no entry exists for this round, default to Unknown unless transcript strongly signals otherwise.
2. Parse actual-format signals from transcript: topic distribution, refusal phrases, question types, interviewer scope boundaries. Use the Signal-Reading Module for interviewer behavior cues.
3. Compute overlap: how many prepped dimensions were actually tested? How many prepped topics were engaged vs. declined?
4. **Downgrade rule**: If any explicit refusal of a prepped topic is found in transcript ("we don't have to look at that", "No I'm good", "let's not go there"), downgrade verdict by one level. Two or more explicit refusals force at least Partial.
5. **Candidate memory override**: If the candidate's debrief memory reports the round diverged materially from prep and the transcript doesn't contradict, weight memory heavily — candidate was in the room.
6. Save verdict to be consumed by Steps 3.7 output, Step 6 parsing path selection, Step 11.6 challenge lens, Step 12 gap identification, Step 12a root cause, Step 15 strategy update.

**Confidence self-check + Ambiguity Escalation to AskUserQuestion:**

Before committing a verdict, the coach must self-check confidence. Three possible states:

- **Confident + Match + prepped format aligns with prior emails/calls/HM guidance** → Proceed silently without interrupting the candidate. Record verdict source as "LLM inference." This is the common happy path — a round that matched expectations does not need to pause for confirmation.
- **Confident + Partial or Mismatch** → Surface the verdict per the normal verdict handling (soft warn for Partial, halt-and-confirm for Mismatch). Record verdict source as "LLM inference."
- **Unsure** (ambiguous signals, conflicting evidence between prep expectations and transcript, thin data, freestyled round where signals don't clearly classify into Match/Partial/Mismatch, OR any case where the coach cannot defensibly commit to a single verdict) → **Use AskUserQuestion to solicit candidate input BEFORE committing the verdict.** The candidate was in the room; they can testify to what the interviewer actually tested, what was mandate-aligned vs. divergent, and whether the round felt like the prepped format or something else.

**When to invoke AskUserQuestion for verdict resolution:**
- Thin or vague `Round formats` entry that makes expected format hard to parse
- Transcript has mixed signals (some prepped topics covered, some not, no clear pattern)
- Interviewer freestyled and the format doesn't map to a canonical archetype
- Explicit refusals exist but the candidate may have interpreted them differently than the transcript suggests
- LLM self-confidence on verdict classification is below high confidence
- Any case where proceeding silently would risk false-post-mortem feedback

**AskUserQuestion prompt template for verdict resolution** (ask 2–3 targeted questions, not a long list):
1. *"We prepped [X format testing Y dimensions]. Did the interviewer actually run that format, or did the round go in a different direction?"*
2. *"Was there anything you were prepped on that the interviewer declined to engage with, or never asked about?"* (If applicable based on transcript signals)
3. *"Based on the round, should I score this against the format we prepped for, or against the actual format the interviewer ran?"*

After candidate answers, commit the verdict and record verdict source as "AskUserQuestion confirmation" or "LLM inference + candidate confirmation." Proceed into scoring with the confirmed verdict. The candidate's answer overrides LLM inference in all cases — they have ground truth the transcript may not capture.

**Rationale for this escalation path:** The entire purpose of RFV is to prevent false post-mortems. An uncertain LLM inference that commits to a verdict risks exactly the failure mode RFV exists to prevent — a confidently-scored round against the wrong rubric. When the LLM is unsure, it should NOT default to "proceed with downgraded confidence" (silent ambiguity that still produces labeled gaps); it should explicitly ask the candidate. The friction of one extra question is far cheaper than a false post-mortem.

**Cascade to downstream steps:**

| Downstream | What Changes |
|---|---|
| `analyze` Step 6 parsing path | If Mismatch, parse against the actual detected format, not the prepped one |
| `analyze` Step 11.6 Transcript Challenge | Lens 1 (Assumption Audit) is auto-triggered to check "did the interviewer actually test the dimensions we scored on?" |
| `analyze` Step 12 gap identification | "No Gap Without An Opening" rule applied; every gap requires citation of the opening |
| `analyze` Step 12a root cause | "Interviewer scope mismatch" (Root Cause #10) flagged if 2+ dimensions scored poorly on axes the interviewer did not test |
| `analyze` Step 15 + `round` Phase 7 Write 6 | Scope-alignment gate on Active Coaching Strategy updates — Mismatch/Unknown do not update Primary Bottleneck |
| `round` Phase 6 triage | Suspended for Mismatch; tagged for Partial; downgraded confidence for Unknown |
| `round` Output Schema | New Format Verification section at top of output; every gap inline-tagged |

**Integration:**
- `analyze`: Step 3.7 runs RFV and routes based on verdict. Every downstream step consumes the verdict.
- `round`: Phase 6 Step 6.0 re-checks verdict before triage. Phase 7 Write 6 applies scope-alignment gate on Active Coaching Strategy writes.
- `debrief`: Step 4 extended prompts feed candidate memory into RFV input as pre-seeded Mismatch/Partial candidates.
- `prep`: When writing `Round formats` to Interview Loop for upcoming rounds, capture testable scope assumptions in freeform text so RFV can compare against them post-round.

---
