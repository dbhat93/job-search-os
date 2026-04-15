# coaching_state.md Schema

This is the full template for `coaching_state.md`. Use this when creating a new coaching state (during `kickoff`) or when migrating/validating an existing one.

```markdown
# Coaching State — [Name]
Last updated: [date]

## Profile
- Target role(s):
- Seniority band:
- Track: Quick Prep / Full System
- Feedback directness: [1-5]
- Interview timeline: [date or "ongoing"]
- Time-aware coaching mode: [triage / focused / full]
- Interview history: [first-time / active but not advancing / experienced but rusty]
- Biggest concern:
- Known interview formats: [e.g., "behavioral screen, system design (verbal walkthrough)" — updated by Format Discovery Protocol during prep/mock]
- Anxiety profile: [confident-underprepared / anxious-specific / generalized / post-rejection / impostor — set by hype, reused in subsequent sessions]
- Career transition: [none / function change / domain shift / IC↔management / industry pivot / career restart — set by kickoff]
- Transition narrative status: [not started / in progress / ready — only relevant when Career transition is not "none"]

## Resume Analysis
- Positioning strengths: [the 2-3 signals a hiring manager sees in 30 seconds]
- Likely interviewer concerns: [flagged from resume — gaps, short tenures, domain switches, seniority mismatches]
- Career narrative gaps: [transitions that need a story ready]
- Story seeds: [resume bullets with likely rich stories behind them]

## Storybank
| ID | Title | Primary Skill | Secondary Skill | Impact | Domain | Risk/Stakes | Earned Secret | Strength | Use Count | Last Used | Archetype Fit |
|----|-------|---------------|-----------------|--------|--------|-------------|---------------|----------|-----------|-----------|--------------|
[rows — full index. Archetype Fit = which archetypes this story is strongest for (from Archetype Detection Module). See references/storybank-guide.md for column definitions and health criteria.]

### Story Details
#### S001 — [Title]
- Situation:
- Task:
- Action:
- Result:
- Earned Secret:
- Reflection: [What you learned. What you'd do differently. Signals seniority and self-awareness. Populated during `stories` or `round` when candidate naturally surfaces hindsight. This is NOT the earned secret (which is the non-obvious insight). This is the honest retrospective: "If I could do it again, I would have X because Y."]
- Deploy for: [one-line use case — e.g., "leadership under ambiguity questions"]
- Field notes: [performance notes from actual interviews — date, context, what landed, what didn't]
- Version history: [date — what changed]

[repeat for each story]

## Score History
### Historical Summary (when table exceeds 15 rows, summarize older entries here)
[Narrated trend summary of older sessions — direction per dimension, inflection points, what caused shifts]

### Recent Scores
| Date | Type | Interview_Type | Context | Sub | Str | Rel | Cred | Diff | Hire Signal | Self-Δ |
|------|------|---------------|---------|-----|-----|-----|------|------|-------------|--------|
[rows — Type: interview/practice/mock. Interview_Type: behavioral/live_case/technical_behavioral/system_design/presentation/hybrid — required for interview/mock rows, leave blank for practice. Sub=Substance, Str=Structure, Rel=Relevance, Cred=Credibility, Diff=Differentiation — each 1-5 numeric. Hire Signal: Strong Hire/Hire/Mixed/No Hire (from analyze/mock only — leave blank for practice). Self-Δ: over/under/accurate (>0.5 delta from coach scores = over or under; within 0.5 = accurate). Keep most recent 10-15 rows. Trend analysis in `progress` filters by Interview_Type — compare like-for-like only.]

## Outcome Log
| Date | Company | Role | Round | Result | Notes |
|------|---------|------|-------|--------|-------|
[rows — Result: advanced/rejected/pending/offer/withdrawn]

## Interview Intelligence

### Question Bank
| Date | Company | Role | Round Type | Question | Competency | Score | Outcome |
[Round Type: behavioral/technical/system-design/case-study/bar-raiser/culture-fit.
 Score: average across 5 dims (e.g., 3.4), or "recall-only" for debrief-captured questions.
 Outcome: advanced/rejected/pending/unknown — updated when known.]

### Effective Patterns (what works for this candidate)
- [date]: [pattern + evidence — e.g., "Leading with counterintuitive choice in prioritization stories scores 4+ on Differentiation (CompanyA R1, CompanyB R2)"]

### Ineffective Patterns (what keeps not working)
- [date]: [pattern + evidence — e.g., "Billing migration story has scored below 3 on Differentiation across 3 uses. Retire or rework."]

### Recruiter/Interviewer Feedback
| Date | Company | Source | Feedback | Linked Dimension |
[Source: recruiter/interviewer/hiring-manager. Keep verbatim when possible.]

### Company Patterns (learned from real experience)
#### [Company Name]
- Questions observed: [types and frequency]
- What seems to matter: [observations from real data]
- Stories that landed / didn't: [S### IDs]
- Last updated: [date]

### Historical Intelligence Summary
[Narrated summary when subsections exceed archival thresholds]

## Drill Progression
- Current stage: [1-8]
- Session count: [integer — increment each session; meta-check triggers when divisible by 3]
- Gates passed: [list]
- Revisit queue: [weaknesses to resurface]

Stage gate criteria (advance when gate is passed):
- Stage 1→2: One `practice` session completed (any score)
- Stage 2→3: One `practice` session with all dimensions ≥ 2.5
- Stage 3→4: One `mock` with Hire Signal ≥ "Mixed"
- Stage 4→5: One `mock` with Hire Signal ≥ "Lean Advance" OR one real interview with advance outcome
- Stage 5→6: Two `mock` sessions with Hire Signal ≥ "Advance" (consistency check)
- Stage 6→7: One real interview with "Strong Hire" signal or offer
- Stage 7→8: Sustained performance — 3+ scored sessions at all dimensions ≥ 3.5 avg

## Interview Loops (active)
### [Company Name]
- Status: [Decoded / Researched / Applied / Interviewing / Offer / Closed]
- Rounds completed: [list with dates]
- Round formats:
  - Round 1: [format, duration, interviewer type — e.g., "Behavioral screen, 45min, recruiter"]
  - Round 2: [format, duration, interviewer type]
- Stories used: [S### per round]
- Concerns surfaced: [ranked list from `concerns` — severity + counter strategy, or from analyze/rejection feedback]
- Interviewer intel: [LinkedIn URLs + key insights, linked to rounds]
- Prepared questions: [top 3 from `questions` if run]
- Next round: [date, format if known]
- Fit verdict: [from research or prep — Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- Fit confidence: [Limited — no JD / Medium — JD + resume / High — JD + resume + storybank]
- Fit signals: [1-2 lines on what drove the verdict]
- Structural gaps: [gaps that can't be bridged with narrative, if any]
- Date researched: [date, if `research` was run]

## JD Analyses
[One entry per company+role decoded. Multiple entries can coexist. If a JD was decoded as part of batch triage, note the batch rank here.]

### [Company] — [Role]
- Date: [date]
- Depth: [Quick Scan / Standard / Deep Decode]
- Fit verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- Pathway: [Referral / Warm intro / LinkedIn connection / Cold / Internal]
- Top competencies: [top 3 in priority order]
- Frameable gaps: [list]
- Structural gaps: [list]
- Unverified assumptions: [count of LOW/UNKNOWN confidence items — resolve via recruiter screen]
- Batch triage rank: [if part of batch — e.g., "2 of 4, pathway-weighted"]

### Past JD Analyses (archived — when 10+ analyses exist, non-active decodes compress here)
| Date | Company | Role | Fit Verdict |
[rows — brief archive of decoded JDs the candidate didn't pursue]

## Resume Optimization
- Date:
- Depth: [Quick Audit / Standard / Deep Optimization]
- Overall: [Strong / Needs Work / Weak]
- ATS compatibility: [ATS-Ready / ATS-Risky / ATS-Broken]
- Recruiter scan: [Strong / Moderate / Weak]
- Bullet quality: [Strong / Moderate / Weak]
- Seniority calibration: [Aligned / Mismatched]
- Keyword coverage: [Strong / Moderate / Weak]
- Top fixes pending: [1-3 line items]
- JD-targeted: [yes — which JD / no]
- Cross-surface gaps: [resume ↔ LinkedIn inconsistencies, if assessed]

## Comp Strategy
- Date:
- Depth: [Quick Script / Standard / Deep Strategy]
- Target range: [bottom / target / stretch — or "not yet researched"]
- Range basis: [sources used / "candidate needs to research"]
- Research completeness: [none / partial / thorough]
- Stage coached: [application / recruiter screen / mid-process / general]
- Jurisdiction notes: [relevant salary history ban, if applicable]
- Scripts provided: [which stages covered]
- Key principle: [the most important thing to remember]

## LinkedIn Analysis
- Date:
- Depth: [Quick Audit / Standard / Deep Optimization]
- Overall: [Strong / Needs Work / Weak]
- Recruiter discoverability: [Strong / Moderate / Weak]
- Credibility on visit: [Strong / Moderate / Weak]
- Differentiation: [Strong / Moderate / Weak]
- Top fixes pending: [1-3 line items]
- Positioning gaps: [resume ↔ LinkedIn inconsistencies, if assessed]

## Positioning Statement
- Date:
- Depth: [Quick Draft / Standard / Deep Positioning]
- Core statement: [the full hook + context + bridge — 30-45 second version]
- Hook (10s): [the curiosity-gap opener alone]
- Key differentiator: [one sentence]
- Earned secret anchor: [the earned secret or spiky POV powering the positioning]
- Target audience: [primary audience this was optimized for]
- Variant status: [which variants were produced — TMAY / Networking / Recruiter / Career Fair / LinkedIn Hook]
- Consistency status: [aligned / gaps identified — brief summary]

## Outreach Strategy
- Date:
- Depth: [Quick / Standard / Deep]
- Positioning source: [Positioning Statement / Resume Analysis fallback]
- Message types coached: [list]
- Targets contacted: [people/companies]
- Channel strategy: [primary channels]
- Follow-up status: [pending follow-ups with timing]
- LinkedIn profile flagged: [yes/no]
- Key hooks identified: [1-2 reusable positioning hooks]

## Presentation Prep: [Topic / Company]
- Date:
- Depth: [Quick Structure / Standard / Deep Prep]
- Framework: [selected narrative arc]
- Time target: [X min presentation + Y min Q&A]
- Content status: [outline only / full content / talk track reviewed]
- Top predicted questions: [top 3]
- Key adjustment: [single biggest change recommended]

## Active Coaching Strategy
- Primary bottleneck: [dimension]
- Current approach: [what we're working on and how]
- Rationale: [why this approach — links to decision tree / data]
- Pivot if: [conditions that would trigger a strategy change]
- Root causes detected: [list]
- Self-assessment tendency: [over-rater / under-rater / well-calibrated] — set after 3+ scored interviews. Over-rater = self-scores average 1.0+ points above coach scores. Under-rater = 1.0+ points below. Well-calibrated = within 0.5 points average delta.
- Previous approaches: [list of abandoned strategies with brief reason — e.g., "Structure drills — ceiling at 3.5, diminishing returns"]

## Calibration State

### Calibration Status
- Current calibration: [uncalibrated / calibrating / calibrated / miscalibrated]
- Last calibration check: [date]
- Data points available: [N] real interviews with outcomes

### Scoring Drift Log
| Date | Dimension | Direction | Evidence | Adjustment |

### Calibration Adjustments
| Date | Trigger | What Changed | Rationale |

### Cross-Dimension Root Causes (active)
| Root Cause | Affected Dimensions | First Detected | Status | Treatment |

### Unmeasured Factor Investigations
| Date | Trigger | Hypothesis | Investigation | Finding | Action |

## Proof Bank
| ID | Proof Point | Category | Source | Date |
|----|------------|----------|--------|------|
[rows — atomic evidence: one metric, one achievement, one artifact per entry]

Categories: IP, Scale, Impact, Trust, Credibility, Thought Leadership, Network, Builder, Origin Story, Revenue, Growth, Discovery, Partnerships, Methodology

Populated by: `kickoff` (initial from resume), `feedback` (new outcomes), `round` (new metrics mentioned in debrief), manual additions
Consumed by: `outreach` (top 2-3 by archetype relevance), `prep` (map to predicted concerns), cover letters, `pitch` (evidence layer), `hype` (60-second reel)

## Contact Network
| Name | Company | Role Type | Last Contact | Open Promises | Strength | Losing Touch |
|------|---------|-----------|-------------|---------------|----------|-------------|
[rows — every recruiter, HM, interviewer, referral, and networking contact in the search]

Role types: Recruiter, HM, Interviewer, Referral, Networking, Mentor
Strength: Strong (contact <7d + 2+ interactions), Medium (contact <14d OR 1 interaction <7d), Weak (contact >14d OR 1 interaction only)
Losing Touch: Yes if 3+ prior interactions AND last contact >14 days ago
Open Promises: commitments made by or to the candidate. Stale if >7 days old, or deadline passed, or 2+ sessions since with no update.

Updated by: `round` (Phase 7), `feedback`, `prep` (interviewer entries), `outreach`, `sync` (staleness check), `map` (surface stale promises)

## Meta-Check Log
| Session | Candidate Feedback | Adjustment Made |
|---------|-------------------|-----------------|
[rows — record every meta-check response and any coaching adjustment]

## Session Log
### Historical Summary (when log exceeds 15 rows, summarize older entries here)
[Brief narrative of earlier sessions]

### Recent Sessions
| Date | Commands Run | Key Outcomes |
|------|-------------|--------------|
[rows — brief, 1-line per session]

## Coaching Notes
[Freeform observations that don't fit structured fields — things the coach should remember between sessions]
- [date]: [observation — e.g., "candidate freezes in panel formats," "gets defensive about short tenure at X," "prefers morning interviews," "mentioned they interview better after coffee"]
```
