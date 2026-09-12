# fit - Role-Fit Assessment

Decides whether a role is worth pursuing, before any prep investment. `fit` answers "should I apply / is this a fit?" for a specific role. It is distinct from `prep`, which gets the candidate ready once they have decided to pursue.

The scoring logic is shared, not duplicated here. `fit` runs the **Role-Fit Assessment Module** in `references/cross-cutting.md`. This file defines the command surface (inputs, sequence, output, state writes); the module defines the gates, dimensions, and verdicts.

### Inputs

- Required: one of a JD, a job-posting URL, or a company name (plus role title if known)
- Optional: the candidate's hard constraints if not already in Profile (sponsorship need, comp floor, location/work-mode, seniority target)
- If a URL is given, fetch the JD before assessing. If the fetch fails, fall back to the greenhouse/ashby/workday JSON endpoints or the browser, then say so if the content could not be retrieved.

### Dependencies

Read before executing:
- `references/cross-cutting.md` for the Role-Fit Assessment Module (Gate Layer, Per-Requirement Evidence Classification, Five Fit Dimensions, Three-Tier Verdict, Confidence by Data Availability, Alternative Suggestions Protocol)
- `coaching_state.md` for Profile (target roles, seniority band, deadline, hard constraints), Storybank (`storybank.md`) and Proof Bank (for evidence-based Competency Overlap), and Interview Loops (for any existing context on this company)

### Sequence

1. **Assemble constraints.** Pull the candidate's hard constraints from Profile (sponsorship, comp floor, location, seniority target). If a constraint that a gate depends on is unknown and not in Profile, that is an `ask`, not an assumption.
2. **Run the Gate Layer FIRST** (exclude / ask / skip / review). Lead the output with the gate result. An `exclude` gate ends the assessment: state the disqualifier plainly and do not score the five dimensions as if the role were viable. An `ask` gate surfaces the one blocking question before scoring.
3. **If the gate is `review` (or `skip` and the candidate asked anyway):** run the Five Fit Dimensions, using Per-Requirement Evidence Classification (`met` / `partial` / `missing` / `unclear`) for Requirement Coverage. Attach real sourced evidence for every `met` and `partial`. Never fabricate evidence to raise coverage.
4. **State confidence** by data availability (Limited / Medium / High) and name what is missing.
5. **Give the Three-Tier Verdict** (Strong Fit / Stretch Fit with sub-category / Weak Fit). On Weak or Long-Shot Stretch, run the Alternative Suggestions Protocol.
6. **Respect candidate agency.** The candidate decides whether to apply. `fit` gives an honest assessment, not permission (see Anti-Patterns in the module).

### Output Schema

```markdown
## Fit: [Company], [Role]

## Gate: [exclude / ask / skip / review]
[If exclude: the disqualifier, and an offer to note the company for future roles. Stop here.]
[If ask: the one blocking question. Stop here until answered.]

## Requirement Coverage (per-requirement)
| Requirement | Tag | Evidence |
|-------------|-----|----------|
[met / partial / missing / unclear, with sourced evidence]

## Five Dimensions
- Requirement Coverage: [Strong/Moderate/Weak]
- Seniority Alignment: [Strong/Moderate/Weak]
- Domain Relevance: [Strong/Moderate/Weak]
- Competency Overlap: [Strong/Moderate/Weak]
- Trajectory Coherence: [Strong/Moderate/Weak]

## Confidence: [Limited / Medium / High]. [what is missing, if anything]

## Verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
[One-paragraph rationale. On Weak or Long-Shot: alternative suggestions.]

## Recommended next: [`apply` / `prep` / note-for-later / drop]
```

### Coaching State Integration

When the candidate acts on a `fit` call (applies, or decides to pursue), write a compact entry so the assessment is not lost:
- Interview Loops (or a lightweight pipeline note): company, role, verdict, gate result, and fit confidence, for example "Fit confidence: Limited, no JD, assessed seniority + trajectory only."
- Do not write a full loop entry for a role the candidate has not engaged; a one-line note is enough until there is real activity.

### Distinction From Neighboring Commands

- **`fit` vs `prep`**: `fit` decides whether to pursue. `prep` gets you ready once you have decided. Do not run a full `prep` inside a `fit` call.
- **`fit` vs `decode`**: `decode` reads a JD for what the company is really asking for and how to position; `fit` judges whether the candidate should pursue it at all. `decode` also runs the Gate Layer first (a role that fails a hard gate is not worth decoding).
- **`fit` vs the `kickoff` Target Reality Check**: `kickoff` fires a lightweight fit check only on clear mismatches during setup; `fit` is the on-demand, full-depth version.

### Routing

Wired in COACH.md Mode Detection (4a): an explicit `fit` command, or "is this a fit / should I apply / assess this role" intent with a JD, URL, or company, routes here. Fetch the JD if a URL is given.
