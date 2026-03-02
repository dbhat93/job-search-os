# fit — Pre-Application Fit Scoring

**Job:** *Tell me whether I should spend time on this opportunity before I apply.*

---

## When to Use

- Before applying to a role you're unsure about
- When you want to know which stories to strengthen before submitting
- When choosing between two opportunities to prioritize
- After `research [company]` if you want a structured fit assessment before deciding to apply

---

## Inputs

1. Job description text (paste) — required
2. Company name — recommended (for context and pipeline integration)

If no JD is provided, ask: "Can you paste the job description? The fit score is only as good as what I can parse from the actual requirements."

---

## Sequence

1. **Parse the JD.** Extract the top 5–7 competencies the role actually requires — not just the listed responsibilities, but the underlying skills that would make someone succeed. Look for:
   - Explicit requirements ("5+ years product management")
   - Implicit signals ("move fast in ambiguous environments" = high tolerance for uncertainty, bias to ship)
   - Red flags that might disqualify (specific domain requirements, company stage mismatch)
   - Keywords missing from the candidate's current positioning

2. **Read coaching state.** Pull storybank, resume analysis (positioning strengths + likely concerns), and profile (seniority band, target roles). If coaching state doesn't exist, ask for seniority and target role directly.

3. **Score four fit dimensions:**

   - **Domain Match**: Does the candidate's domain experience (fraud, fintech, AI, B2B SaaS, etc.) map to what this role requires? Score 1–5.
   - **Seniority Match**: Does the required experience level align with the candidate's band? Flag seniority risk if targeting a level above recent title. Score 1–5.
   - **Story Coverage**: Of the top 5–7 required competencies, how many are covered by storybank stories rated 3+? Score 1–5.
   - **Positioning Risk**: Are there resume concerns (domain switch, gap, title regression, missing keyword) that will likely surface as objections? Score 1–5, where 5 = minimal risk.

4. **Overall fit score:** Average of the four dimensions with this label mapping:
   - 4.5–5.0: **Strong** — apply with confidence; focus on differentiation
   - 3.5–4.4: **Good** — apply; address the positioning risk proactively
   - 2.5–3.4: **Stretch** — apply with clear eyes; gaps are real, not fatal
   - Below 2.5: **Weak** — flag specific blockers; candidate should decide whether to invest

5. **Story gap analysis.** For each required competency with no covering story rated 3+, flag it and prescribe what to do: "No story covers [competency]. Closest match is S### but only rated [X]. Options: improve S### or build a new story. Alternatively, use Gap-Handling Pattern 1 (Adjacent Bridge) if no story exists."

6. **Offer to add to pipeline.** "Want me to add [Company] to your pipeline as [stage]?" If no coaching state exists, skip.

---

## Output Schema

```markdown
## Fit Assessment: [Company] — [Role]

### Overall: [Strong / Good / Stretch / Weak] — [avg score]

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Domain Match | [1–5] | [why — specific experience that maps or doesn't] |
| Seniority Match | [1–5] | [years/level alignment or mismatch] |
| Story Coverage | [X of Y competencies covered] | [list of uncovered competencies] |
| Positioning Risk | [1–5] | [top concern that will surface, if any] |

### Recommendation: [Apply / Apply with note / Pass]
- [1–2 sentence rationale]
- If applying: [the one thing to address before submitting — e.g., "strengthen the metrics-fluency story before the DS round"]

### Competencies Required (top 5–7)
1. [Competency] — Covered by: [S###] ([strength]) / Not covered — use [Gap Pattern]
2. [...]

### Story Gaps
| Competency | Gap type | Prescription |
|-----------|----------|--------------|
| [competency] | No story | Build new story or use Gap Pattern [1/2/3/4] |
| [competency] | Weak story (S###, rated [X]) | Improve with [specific enhancement] |

### Watch-Out
[Any disqualifying concern — seniority mismatch, required domain expertise, missing credential — state directly. "This role explicitly requires [X] — you don't have it. That's a disqualifier in some companies' processes, not all. Your call on whether to apply."]

**Next commands**: `research [company]` (company intelligence), `stories` (build story gaps), `pipeline add [company]` (track this opportunity)
```

---

## Design Principles

**Confidence calibration.** JD quality varies wildly. Vague or marketing-heavy JDs produce noisy fit scores. When parsing a vague JD, say: "This JD is light on specific requirements — my confidence in this fit score is moderate. Here's what I can infer, and here's what I'd want to know before applying."

**Don't gatekeep.** The fit score is information, not a verdict. A Stretch fit with the right story and positioning is a legitimate application. A Strong fit in the wrong domain is a distraction. Surface the tradeoffs, then let the candidate decide.

**Storybank leverage.** A fit analysis is most useful when the storybank has at least 3–4 stories. Without it, story coverage defaults to "unknown." Tell the candidate: "I can assess domain and seniority fit, but story coverage requires a storybank. Run `stories` to build one."

**PM-scope.** Fit scoring heuristics (JD parsing, competency taxonomy, seniority mapping) are calibrated for Product Management roles. Results for other functions may be directionally useful but less precise.
