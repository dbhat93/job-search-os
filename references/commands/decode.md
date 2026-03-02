# decode — JD Analysis + Batch Triage

### How JDs Actually Work (Reference Knowledge)

**JD Structure Patterns**: JDs follow predictable structures — company intro, role summary, responsibilities, requirements, nice-to-haves, benefits. But the signal isn't in the structure, it's in the language.

**Signal Density by Section**:
- Requirements = screening criteria (ATS + recruiter first pass). What gets you through the door.
- Responsibilities = what the role actually does. Often more honest than requirements.
- Nice-to-haves = the ideal candidate profile. What "Strong Hire" looks like beyond baseline.
- Company intro = culture signals and positioning. How the company wants to be perceived.
- Benefits = comp philosophy signals. Equity-heavy = startup. Benefits-heavy = mature org.

**The 6 Decoding Lenses** (adapted from prep.md's JD Parsing Guide — decode makes these the main event):
1. **Repetition frequency** — Count how often key themes appear. If "cross-functional collaboration" appears 3 times, it is a primary evaluation criterion. Most repeated = most important, regardless of where it appears.
2. **Order and emphasis** — What's listed first in responsibilities/requirements? First = highest priority. The first 3 bullets typically reflect the top 3 evaluation criteria.
3. **Required vs. nice-to-have** — Required = screening criteria that filter you in/out before a human looks. Nice-to-have = what differentiates "Hire" from "Strong Hire." Many candidates skip nice-to-haves — this is a mistake.
4. **Verb choices** — "Own" vs. "support" vs. "contribute to" signal autonomy and scope. "Own end-to-end" is a fundamentally different job from "contribute to team efforts." "Drive" vs. "execute" signals strategy vs. implementation.
5. **Between-the-lines signals** — Euphemisms decoded. "Fast-paced environment" = likely understaffed or rapid change. "Comfortable with ambiguity" = undefined role or early-stage. "Stakeholder management" = political environment. "Wear many hats" = no clear role boundaries. These are interpretations, not facts — confidence-label accordingly.
6. **What's missing** — Absence is information. A PM JD that doesn't mention data/analytics signals team maturity (or lack of PM influence on data). An engineering JD that doesn't mention testing may indicate culture. A senior role with no mention of mentoring signals an IC-heavy org.

**What JDs Don't Tell You** (honest limitations — surfaced in every decode output, not just reference knowledge):
- Actual day-to-day work (JDs describe the ideal, not the reality)
- Team dynamics, manager quality, internal politics
- Whether the role is backfill (someone left) vs. new headcount (growth)
- Whether the req is actually open vs. evergreen posting
- Real comp range (unless required by jurisdiction or voluntarily disclosed)
- Internal candidate preference
- Hiring timeline urgency

These limitations appear in every Standard and Deep decode output as a "JD Honest Limitations" section. Quick Scans include a single-line reminder. The candidate should never walk away treating a decode as a complete picture.

**Batch Triage Research**:
- Average job search involves 100–200 applications. Hit rate is 2–8%.
- Time per application: 30–90 minutes (resume tailoring, cover letter, research).
- Improving triage accuracy by 20% saves 20–40 hours of application effort.
- Signal: candidates who apply to Strong Fit roles have materially better outcomes than those who spray-and-apply.
- The batch comparison reveals the candidate's "sweet spot" — competencies that recur across JDs they're drawn to — which is itself career intelligence.
- **Pathway matters as much as fit.** A Long-Shot Stretch role with a strong referral often outperforms a Strong Fit cold application. Triage that ignores access is incomplete.

### Confidence Labeling System

Every interpretation gets a confidence label. This is non-negotiable — it's what makes decode honest instead of performative.

| Label | Meaning | Example |
|---|---|---|
| **HIGH** | Directly stated in JD, standard industry meaning | "5+ years of Python required" → HIGH: Python is a hard screening criterion |
| **MEDIUM** | Reasonable inference from language patterns or industry norms | "Cross-functional leadership" repeated 3x → MEDIUM: likely the primary evaluation lens |
| **LOW** | Interpretation of ambiguous language, euphemism decoding | "Fast-paced environment" → LOW: may indicate understaffing or rapid change |
| **UNKNOWN** | Cannot determine from JD alone | Team size, reporting structure, actual day-to-day → UNKNOWN |

**Rule**: Every LOW and UNKNOWN interpretation MUST be paired with a specific recruiter verification question. The candidate should never walk away believing a LOW-confidence interpretation is fact.

### Priority Check

- If no `kickoff`: Soft gate — "I can decode the JD's language and structure, but without your profile I can't assess fit. Run `kickoff` first for a fit assessment, or proceed with a general decode?"
- If interview within 48 hours: Redirect to `hype`/`prep`.
- If JD Analysis already exists for this company+role: Show the existing decode and ask if the JD has changed. Don't re-decode unchanged JDs.

### Required Inputs

- At least one JD (pasted text or key details)
- For batch triage: 2–5 JDs

### Optional Inputs

- Depth level: Quick Scan / Standard / Deep Decode (default: Standard)
- Specific questions about the JD
- Target priority (is this a top target or early-stage exploration?)
- **Pathway** (for each JD in a batch): Do you have a referral, warm intro, or connection at this company? This affects triage ranking.

### Depth Levels

| Level | When to Use | What It Covers |
|---|---|---|
| **Quick Scan** | Fast filter, building a target list, evaluating whether to apply | Top 5 competencies extracted + fit verdict (if Profile exists) + 3 key signals + confidence labels + recruiter verification questions for LOW/UNKNOWN items + one-line JD limitations reminder |
| **Standard** | Default. Full JD analysis. | All 6 lenses + full competency extraction + fit assessment + concern mapping + question-prediction seeds + recruiter verification questions + JD Honest Limitations section + teaching layer |
| **Deep Decode** | High-priority target, unusual JD, career transition, seniority mismatch | All of Standard + seniority calibration + team maturity analysis + JD structural quality assessment + Challenge Protocol (Level 5) |

### Logic / Sequence (7 steps)

**Step 1: JD Intake**
Accept JD in any format — full posting, bullet-point paste, screenshot description, even "here's roughly what the JD says." Parse into sections (responsibilities, requirements, nice-to-haves, etc.). If sections aren't clearly labeled, infer from content. Flag if the JD is unusually short (may be incomplete) or unusually long (may be a kitchen-sink posting).

**Step 2: Context Assembly**
Pull from coaching_state.md: Profile (target role, seniority band), Resume Analysis (skills, experience, positioning strengths), Storybank (skills coverage), Positioning Statement (key differentiator), active Interview Loops (is this company already in progress?), JD Analyses (previous decodes for pattern comparison).

For batch triage, also note pathway information provided: which JDs have referrals, warm intros, connections, or cold access.

**Step 3: 6-Lens Decode**
Apply all 6 decoding lenses. For each finding:
- State the finding
- Assign confidence label (HIGH/MEDIUM/LOW/UNKNOWN)
- Provide evidence (what in the JD supports this)
- For MEDIUM/LOW/UNKNOWN: provide the recruiter verification question

Group findings by lens in Standard/Deep output. In Quick Scan, surface only the top 3 highest-signal findings.

For Lens 5 (between-the-lines signals), use the "decode + verify" pattern:
- State the euphemism or signal
- Provide the most likely interpretation
- Label confidence (almost always LOW or MEDIUM)
- Provide the verification question: what to ask, why it matters, how to ask it naturally

For Lens 6 (what's missing), explicitly state what the absence might mean AND what it might not mean. Absence is ambiguous — don't present a single interpretation as truth.

**Step 4: Competency Extraction**
Extract top 5–7 competencies in priority order. For each:
- The competency (specific, not vague)
- Source section(s) (where in the JD it appears)
- Confidence level
- Repetition count (how many times it appears across sections)
- Type: Screening (required, filters in/out) or Differentiating (nice-to-have, separates Hire from Strong Hire)

**Step 5: Fit Assessment (if Profile exists)**
Map extracted competencies against candidate profile. For each competency:
- **Match**: Direct evidence from resume/storybank (cite specific evidence)
- **Partial**: Adjacent experience, frameable with narrative (explain the bridge)
- **Gap**: No evidence, structural gap (name it honestly)
- **Unknown**: Can't assess without more information from candidate

Produce fit verdict using the Role-Fit Assessment from cross-cutting.md (5 dimensions: Requirement Coverage, Seniority Alignment, Domain Relevance, Competency Overlap, Trajectory Coherence). Classify gaps as Frameable (narrative can bridge) or Structural (real limitation).

Verdict: Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit

For Long-Shot Stretch and Weak Fit: be honest. Don't waste the candidate's time encouraging applications to roles they're not competitive for — unless they have a specific strategy (referral, internal transfer, etc.).

**Step 6: Recruiter Verification Questions**
Compile all MEDIUM, LOW, and UNKNOWN confidence interpretations into a prioritized list of questions to ask the recruiter. For each:
- What you want to verify
- Why it matters for your decision/preparation
- How to ask it naturally

Order by impact on the apply/don't-apply decision.

**Step 7: Batch Triage (if multiple JDs provided)**
For each JD: run Steps 1–6 individually (can be abbreviated for Quick Scan depth).

Then produce comparative analysis with pathway-weighted ranking:

**Pathway Classification** (assess for each JD before ranking):
- **Referral**: Someone at the company has agreed to refer you. Highest-access tier.
- **Warm intro**: A mutual connection can introduce you to someone at the company. Second-highest access.
- **LinkedIn connection**: You have a 1st-degree connection at the company who may respond to outreach. Moderate access.
- **Cold**: No connection. Standard application path only.
- **Internal**: You're already at the company (internal transfer or promotion). Different rules apply.

**Pathway-weighted ranking logic**:
- Base ranking: fit level (Strong Fit > Investable Stretch > Long-Shot Stretch > Weak Fit)
- Pathway boost: A role with a Referral gets a +1 tier boost in ranking. A role with a Warm intro gets a +0.5 tier boost. Cold applications get no boost.
- Example: A Long-Shot Stretch with a Referral ranks above an Investable Stretch with a Cold application if the access is genuine — because the referral changes the odds more than the raw fit gap.
- Flag the logic transparently: "This role is ranked #2 despite being Investable Stretch because you have a referral, which materially increases your odds relative to the Strong Fit cold application at #1."

Then produce:
- **Rank by pathway-weighted fit** (highest first, with evidence for each)
- **Overlapping competencies** across JDs — this reveals the candidate's market-validated sweet spot
- **Divergent requirements** — where JDs pull in different directions
- **Allocation recommendation**: which to pursue first, which to skip, which to research more
- **Target profile synthesis** — what these JDs collectively reveal about what the market wants

### Teaching Layer

Quick Scan includes a "Decode Tip" — one teaching insight per scan, rotating through the 6 lenses. Standard and Deep include the full "Learn to Read This Yourself" section:
- **Pattern spotted**: A specific decoding insight from THIS JD
- **Trap to watch for**: A common misread THIS JD exemplifies
- **Self-decode prompt**: A question the candidate should ask themselves when reading the NEXT JD

### Output Schemas

**Quick Scan**:
```markdown
## JD Quick Scan: [Company] — [Role]

## Top 5 Competencies (priority order)
| # | Competency | Confidence | Type | Source |
|---|---|---|---|---|
| 1 | ... | HIGH/MEDIUM | Screening/Differentiating | [section, repetition count] |

## Key Signals
- [Signal 1] — [Confidence] — [what it means]
- [Signal 2] — [Confidence] — [what it means]
- [Signal 3] — [Confidence] — [what it means]

## Fit Verdict [if Profile exists]
[Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit] — [1-line evidence]
- Strongest match: [competency + evidence]
- Biggest gap: [competency + gap type]

## Verify With Recruiter
1. [Question — for the highest-impact LOW/UNKNOWN item]
2. [Question — second priority]

## JD Reminder
This decode reflects what the JD says — not what the job actually is. Key unknowns: day-to-day reality, team dynamics, whether this is backfill or new headcount, and real comp range.

## Decode Tip
[One teaching insight from this JD]

**Recommended next**: `decode` (Standard) for full analysis. **Alternatives**: `prep [company]`, `research [company]`
```

**Standard**:
```markdown
## JD Decode: [Company] — [Role]

## Decode Summary
- Role type: [what this role actually is — in plain language]
- Seniority signal: [what level this targets — with evidence and confidence]
- Team signal: [what the JD reveals about the team — with confidence]
- JD quality: [well-written / kitchen-sink / sparse / standard — what that implies]

## Competency Map (priority order)
| # | Competency | Confidence | Type | Repetition | Source |
|---|---|---|---|---|---|
| 1 | ... | HIGH | Screening | 3x | Requirements, Responsibilities |

## 6-Lens Analysis

### Lens 1: Repetition Frequency
[Findings with counts. What's repeated most = what they care about most.]

### Lens 2: Order & Emphasis
[Findings. What's listed first = highest priority.]

### Lens 3: Required vs. Nice-to-Have
[Findings. What's actually screening vs. differentiating.]

### Lens 4: Verb Choices
[Findings. Scope and autonomy signals.]

### Lens 5: Between the Lines
| Signal | Likely Meaning | Confidence | Verify |
|---|---|---|---|
| [euphemism] | [interpretation] | LOW/MEDIUM | [question to ask] |

### Lens 6: What's Missing
[Findings. What absence tells you — with alternative explanations.]

## Fit Assessment [if Profile exists]
- **Verdict**: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
| Competency | Match | Evidence |
|---|---|---|
| [competency 1] | Match/Partial/Gap | [specific evidence or gap description] |
- **Frameable gaps** (narrative can bridge): [list with bridge strategy]
- **Structural gaps** (real limitations): [list — honest]

## Question Prediction Seeds
Based on top competencies and identified gaps:
- [Likely question 1 — from competency 1]
- [Likely question 2 — from competency 2]
- [Likely question 3 — from identified gap]

## Verify With Recruiter (priority order)
1. [Question — what you're verifying — how to ask naturally]
2. [Question]
3. [Question]

## JD Honest Limitations
What this decode can't tell you — and what to do about it:
- **Day-to-day reality**: JDs describe the ideal, not the actual work. Ask the hiring manager: "Can you walk me through what a typical week looks like for this role right now?"
- **Team and manager quality**: Not in any JD. Ask to meet the team and ask: "What's the team's working style?"
- **Backfill vs. new headcount**: Signals different urgency and role clarity. Ask: "Is this a new role or one that was previously filled?"
- **Real comp range**: If not posted, ask: "Can you share the budgeted range for this role?" (especially in transparency-law jurisdictions). See the `comp` command for full pre-offer comp coaching and scripts.
- **Internal candidate preference**: Cannot be determined from the JD. Ask: "Are you also considering internal candidates for this role?"

## Learn to Read This Yourself
- **Pattern spotted**: [teaching point from this specific JD]
- **Trap to watch for**: [common misread this JD exemplifies]
- **Next time, try**: [self-decode prompt for future JDs]

**Recommended next**: `prep [company]` for full interview preparation. **Alternatives**: `research [company]`, `decode` (batch triage with more JDs)
```

**Deep Decode**: All of Standard + expanded sections:
```markdown
## JD Deep Decode: [Company] — [Role]

[All Standard sections, expanded]

## Seniority Calibration
- JD states: [what level language the JD uses]
- JD signals: [what level the scope, verbs, and requirements actually target — with evidence and confidence]
- Assessment: [aligned / JD over-titles / JD under-titles] — [Confidence]
- Implication for candidate: [what this means for their application/positioning]

## Team Maturity Signals
[What the JD reveals about the team's stage — with confidence labels and multiple interpretations where ambiguous.]

## JD Structural Analysis
- Quality: [well-written / boilerplate / kitchen-sink / internally contradictory]
- What quality reveals: [what a well-written vs. poorly written JD signals about the hiring process]
- Red flags: [if any — internal contradictions, impossible combinations, unrealistic requirements]

## Challenge (Level 5 only)
- **Assumptions this decode rests on**: [2–3 assumptions with what would change if they're wrong]
- **Blind spots**: [what we fundamentally can't see from a JD alone]
- **Devil's advocate**: [strongest case that this decode is wrong]
- **Highest-leverage verification**: [the single question that would most change the analysis if answered]

## Priority Moves (ordered)
1. [highest-impact action — verify, apply, research more, skip]
2. [second]
3. [third]

**Recommended next**: `prep [company]` for full interview preparation. **Alternatives**: `research [company]`, `practice` (targeted drills on gap competencies)
```

**Batch Triage** (additional output when 2+ JDs provided, appended after individual decodes):
```markdown
## Batch Triage: [N] Roles

## Pathway-Weighted Ranking
| Rank | Company | Role | Fit | Pathway | Pathway Boost | Recommendation |
|---|---|---|---|---|---|---|
| 1 | ... | ... | Strong | Referral | +1 tier | Pursue — prioritize immediately |
| 2 | ... | ... | Investable Stretch | Warm intro | +0.5 tier | Pursue — address gap [X] before applying |
| 3 | ... | ... | Strong | Cold | No boost | Pursue — strong fit, standard odds |
| 4 | ... | ... | Long-Shot Stretch | Referral | +1 tier | Pursue — referral offsets stretch gap |
| 5 | ... | ... | Long-Shot Stretch | Cold | No boost | Skip unless you develop a connection first |

## Your Sweet Spot
[Competencies that appear across multiple JDs — this is what the market values in you. Ordered by frequency across JDs.]

## Divergence
[Requirements that pull in different directions — reveals a scope decision the candidate needs to make.]

## Allocation Recommendation
- **Pursue first**: [which roles, why — highest pathway-weighted rank]
- **Pursue with targeted prep**: [which roles, what specific gap to address]
- **Build pathway before applying**: [roles where cold application is low-odds but access could change the picture — suggest `outreach` to develop a connection]
- **Skip or deprioritize**: [which roles, why — honest about structural gaps with no pathway offset]

## Your Market Profile
[What these JDs collectively reveal about what the market wants from someone like the candidate.]

**Recommended next**: `research [top-ranked company]` or `prep [top-ranked company]`. **Alternatives**: `decode` with more JDs, `outreach [company]` (to build pathway for cold-access roles worth pursuing)
```

### Coaching State Integration

Save to coaching_state.md (one entry per JD — multiple can exist):

```markdown
## JD Analysis: [Company] — [Role]
- Date: [date]
- Depth: [Quick Scan / Standard / Deep Decode]
- Fit verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- Pathway: [Referral / Warm intro / LinkedIn connection / Cold / Internal]
- Top competencies: [top 3 in priority order]
- Frameable gaps: [list]
- Structural gaps: [list]
- Unverified assumptions: [count of LOW/UNKNOWN confidence items]
- Batch triage rank: [if part of batch — rank/total, pathway-weighted]
```
