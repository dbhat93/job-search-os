## Role-Fit Assessment Module

Targeting the right roles is as important as performing well in interviews. This module provides a structured framework for evaluating candidate-role fit, used by `research`, `kickoff`, `prep`, `decode`, `fit`, and `progress`.

### Gate Layer (runs BEFORE the fit verdict)

Borrowed from vaibhavarora14/job-application-agent (MIT) gate-before-score discipline. A strong fit score must never override a hard disqualifier. Before assigning the five-dimension verdict, run these gates and surface the gate result first:

| Gate | Fires when | Result |
|---|---|---|
| **exclude** | Posting is closed/stale, an explicit hard requirement the candidate cannot meet (e.g., "must have active US clearance," "J.D. required," "must be US citizen"), no visa sponsorship where the candidate needs it, or a location/work-mode the candidate has ruled out | Do not proceed to fit scoring. State the disqualifier plainly. Offer to note the company for future roles. |
| **ask** | A gating fact is unknown: posting status, work authorization/sponsorship, location/remote policy, comp floor, or seniority band | Ask the one blocking question before scoring. Do not assume. |
| **skip** | Explicit non-target seniority (e.g., a plain Senior role when the candidate targets Staff+), comp clearly below the candidate's stated floor, or must-have coverage so thin the role is a long-shot | Score if asked, but lead with "this is below your bar because [X]." |
| **review** | No gate fires | Proceed to the five-dimension verdict below. |

Unknown compensation does NOT trigger exclude on its own (many strong roles omit it); it triggers `ask` only if the candidate has a hard floor. A high Domain/Competency score never upgrades a role past an `exclude` gate.

### Per-Requirement Evidence Classification (sharpens Requirement Coverage)

Instead of a single Strong/Moderate/Weak on Requirement Coverage, classify each must-have from the JD and attach evidence:

| Tag | Meaning | Evidence rule |
|---|---|---|
| `met` | Candidate clearly satisfies it | Cite the specific resume/storybank/Proof Bank evidence. |
| `partial` | Adjacent or transferable, not a direct match | Cite the adjacent evidence AND name what is not yet demonstrated. |
| `missing` | No evidence | State it plainly. Do NOT invent evidence to fill it. |
| `unclear` | JD requirement is ambiguous, or candidate data is insufficient to judge | Flag for clarification. |

**Evidence integrity rule:** attach real, sourced evidence for every `met` and `partial`; never fabricate evidence to raise coverage. This is the fit-assessment instance of "No Number Without A Source." Requirement Coverage rolls up from the tags: mostly `met` = Strong, meaningful `partial` mix = Moderate, several `missing` on must-haves = Weak.

### Five Fit Dimensions

| Dimension | What It Measures | Data Source |
|---|---|---|
| **Requirement Coverage** | How many "required" qualifications the candidate meets vs. misses | JD + resume |
| **Seniority Alignment** | Whether the candidate's experience level matches the role's expectations | JD + resume + career trajectory |
| **Domain Relevance** | How transferable the candidate's industry/domain experience is | JD + resume + company context |
| **Competency Overlap** | Overlap between the candidate's demonstrated skills and the role's core competencies | JD + storybank (if available) + resume |
| **Trajectory Coherence** | Whether this role makes sense as the candidate's next career move — narratively and developmentally | Resume + career history + target role |

Score each dimension: Strong / Moderate / Weak. Not every dimension needs data — flag unknowns explicitly.

### Three-Tier Verdict

**Strong Fit** — Candidate meets most requirements, seniority aligns, domain is relevant or closely adjacent, competencies overlap substantially, and the role is a logical next step. Prep focuses on positioning and differentiation.

**Stretch Fit** — Candidate has meaningful gaps but also clear strengths. Two sub-categories:
- **Investable Stretch**: 1-2 addressable gaps (domain switch with transferable skills, one level up with strong trajectory). The candidate can make a credible case. Prep focuses on gap-bridging narratives and concern counters.
- **Long-Shot Stretch**: 3+ gaps or a fundamental mismatch (2+ levels up, zero domain overlap, missing hard requirements). The candidate should understand the odds. Coach helps if they choose to proceed, but names the reality.

**Weak Fit** — Fundamental misalignment across multiple dimensions. The honest coaching move is to say so and suggest better-fit alternatives.

### Confidence by Data Availability

| Data Available | What You Can Assess | What You Can't |
|---|---|---|
| Company name only | Seniority Alignment (from public info), Trajectory Coherence | Requirement Coverage, Competency Overlap (no JD) |
| Company + JD | All 5 dimensions at moderate confidence | Deep domain relevance (may need research) |
| Company + JD + Resume | All 5 dimensions at high confidence | — |
| Company + JD + Resume + Storybank | All 5 dimensions at highest confidence (competency overlap is evidence-based, not inferred) | — |

When data is limited, assess what you can and flag what's missing: "I can assess Seniority Alignment and Trajectory Coherence from what I know. For a full fit assessment, I'd need the JD."

**Confidence thresholds for fit verdicts:**
- **Limited** confidence: No JD, 2-3 of 5 dimensions assessable. Verdicts at this level should include: "My confidence is limited without [specific missing data]."
- **Medium** confidence: JD + resume available, 4-5 dimensions assessable.
- **High** confidence: JD + resume + storybank + interview outcomes available, all dimensions assessable with evidence.

Use these labels explicitly in coaching_state.md fit entries (e.g., "Fit confidence: Limited — no JD, assessed seniority + trajectory only").

### Alternative Suggestions Protocol

When fit is Weak or Long-Shot Stretch, don't just diagnose — help redirect:

1. **Name the specific gaps** driving the weak assessment (not vague "not a great fit")
2. **Suggest what a better-fit version of this role looks like**: "Based on your profile, you'd be a stronger fit for [role type] at [company stage/type] because [specific reason]"
3. **If the candidate wants to proceed anyway**, respect their agency but adjust coaching: "Your odds are lower here, and that's okay if you've decided it's worth the shot. Let me help you build the strongest possible case for the gaps they'll see."

### Anti-Patterns

- Don't gatekeep. The candidate decides whether to apply — the coach provides honest assessment, not permission.
- Don't conflate "stretch" with "impossible." Career growth requires stretch roles. The question is whether the stretch is bridgeable.
- Don't assess fit based on vibes. Use the 5 dimensions with evidence.
- Don't over-index on requirement coverage. Many JDs are wish lists. A candidate who meets 60-70% of requirements is often competitive.
- Don't ignore trajectory coherence. A role someone is qualified for but that doesn't advance their career is a poor fit in a different way.

### Integration

- **`fit` / `decode`**: Run the Gate Layer FIRST (exclude/ask/skip/review), then the five-dimension verdict, using Per-Requirement Evidence Classification for Requirement Coverage. Lead the output with the gate result: an `exclude` gate ends the assessment (state the disqualifier, do not score dimensions as if the role were viable). This is what makes a `fit` call hard to fool: a role that scores well on domain but fails a hard gate (no sponsorship, J.D. required, wrong location) is not a fit, full stop.
- `kickoff`: Target Reality Check — fires only on clear mismatches (2+ level seniority gap, zero domain experience, function switch without bridge narrative)
- `research`: Structured Fit Assessment replaces the current vibes-based section — uses the 3 dimensions assessable without a JD
- `prep`: Full 5-dimension assessment with JD + resume + storybank data. Distinguishes frameable gaps (can counter with narrative) from structural gaps (real limitations)
- `progress`: Outcome-Based Targeting Insights — when 3+ real interview outcomes exist, analyzes rejection patterns to surface targeting issues

---
