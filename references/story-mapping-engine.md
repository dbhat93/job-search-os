# Story Mapping Engine

Consolidates story mapping logic into a single protocol. Referenced by `prep` (step 8), `stories` (gap analysis), and `progress` (storybank health).

---

## Section 1: Story-Question Fit Scoring

Replace bare `Q1 -> S###` with a 4-level fit classification:

| Fit Level | Definition |
|---|---|
| **Strong Fit** | Primary skill matches the competency being tested. Story strength 4+. Domain aligns with the target company/role. Earned secret is relevant to the question. |
| **Workable** | Secondary skill matches the competency, OR primary skill matches but story strength is 3, OR domain is adjacent but not direct. Can work with framing guidance. |
| **Stretch** | No direct skill match but the story can be reframed to address the competency. Story strength 2+. Requires significant bridging in delivery. |
| **Gap** | No story addresses this competency at any fit level. Trigger gap-handling protocol (see Gap-Handling Module in `references/cross-cutting.md`). |

### Fit Scoring Factor Priority Stack

When evaluating a story-question match, weigh these factors in order:

1. **Competency match** (highest weight) — Primary skill match > Secondary skill match > Reframe match. A story whose primary skill directly addresses the tested competency is always preferred.
2. **Strength score** (high weight) — Stories rated 4–5 > 3 > 2. A strength-5 story with a secondary skill match may outperform a strength-3 story with a primary skill match.
3. **Company/role alignment** (medium weight) — Does the story's domain match the target company? Is the earned secret relevant to what this company values? Stories from the same industry or with transferable context get a boost.
4. **Freshness** (medium weight) — Story freshness score (see Section 5). Stale stories are deprioritized when alternatives exist. Proven performers (stories that contributed to past advancements) get a boost that partially offsets staleness.
5. **Variety** (portfolio constraint) — Applied at the portfolio level, not per-question. See Section 2 for the framing variety constraint — the same story can appear twice in a mapping with demonstrably different angles.

### Mapping Output Format

For each question-story mapping, state:
- **Fit level**: Strong Fit / Workable / Stretch / Gap
- **Why**: One line explaining the match (e.g., "Primary skill (leadership) directly matches competency. Strength 4. Domain aligned (B2B SaaS).")
- **Bridging guidance** (Workable/Stretch only): How to frame the story to better address the competency. (e.g., "Foreground the cross-functional coordination element — it's a secondary skill in this story but it's what the question is testing.")
- **Freshness flag** (if applicable): Note if story is flagged as stale or over-rehearsed.

---

## Section 2: Portfolio Optimization Protocol

7-step process replacing question-by-question mapping:

### Step 1: Generate Candidate Mappings
For each predicted question, identify ALL stories that could work (Strong Fit, Workable, or Stretch). Build a matrix:

```
           Q1    Q2    Q3    Q4    Q5    Q6    Q7
S001       SF    --    W     --    --    St    --
S002       --    SF    --    W     --    --    --
S003       W     --    SF    SF    --    --    --
S004       --    --    --    --    SF    --    W
S005       --    W     --    --    --    SF    --
...
```

SF = Strong Fit, W = Workable, St = Stretch, -- = no viable match.

### Step 2: Detect Conflicts
Identify questions competing for the same best story. A conflict exists when two or more questions have the same story as their highest-fit option.

### Step 3: Resolve Conflicts
For each conflict:
1. Assign the story to the question where it has the highest fit level.
2. If fit levels are equal, assign to the question where the story's strength matters most (i.e., the harder question or the one with fewer alternative stories).
3. Cascade to the next-best story for the losing question.
4. Flag significant downgrades: "Q4 was downgraded from S003 (Strong Fit) to S006 (Workable) due to conflict with Q3. Bridging guidance: [specific framing]."

### Step 4: Apply Framing Variety Constraint

The same story may appear twice in the final mapping if — and only if — the framing angle for each appearance is demonstrably different, and both angles are substantive parts of the story (not a dominant thread vs. a minor subplot).

**Why this replaces the "no story twice" rule**: A strong story with two genuine angles produces better outcomes than forcing a weaker story into one of the slots. One strong story told twice with different leads is more competitive than two mediocre stories. Variety for its own sake is a trap.

**When to allow a story to appear twice**:
- Specify the distinct angle for each: "For Q3, lead with the stakeholder alignment dimension. For Q7, lead with the technical constraint navigation." Both must be explicitly named and genuinely distinct.
- Confirm both angles are substantive using the **Substantiation Test** (all 3 criteria must hold):
  1. **Different competency tested**: Does Q3's angle test a different core competency than Q7's angle? If both angles test "leadership" (even labeled differently), they're relabeling. If one tests "stakeholder management" and the other tests "technical constraint navigation," they're distinct.
  2. **Different STAR section emphasized**: Do the two angles draw from materially different parts of the story? If both lead with the same Action section relabeled, that's cosmetic. If one foregrounds the Situation setup and the other foregrounds the Result or a different Action thread, they're distinct.
  3. **Different interviewer takeaway**: Would an interviewer who heard both versions learn two materially different things about the candidate? If yes — substantive reuse. If no — relabeling.
- Note the reuse in the mapping: "S003 appears twice — distinct angles. Q3: stakeholder angle. Q7: constraint navigation angle."

**When to NOT allow reuse**:
- If the angle difference is cosmetic ("for Q3, I'll say leadership; for Q7, I'll say influence" — these are the same thing relabeled)
- If a Workable or better alternative exists for one of the two questions — use it instead
- If the story appears in a prior round at this company (freshness constraint overrides angle variety)

**If a story must be reused with the same framing angle** (no alternatives exist at any fit level): explain why and flag the limitation: "S003 is the only story addressing both [competency A] and [competency B] at any viable fit level. Reusing with same angle — limited range signal."

### Step 5: Apply Freshness Constraint
Check `coaching_state.md` → Interview Loops for stories used in prior rounds at this company.
- Stories used in a previous round: downgrade by one fit level (Strong Fit → Workable) unless the candidate is asked to go deeper on the same topic.
- Flag: "S003 was used in Round 1. Using it again in Round 2 signals limited range unless they specifically ask you to elaborate."

### Step 6: Apply Overuse Check
Cross-reference story freshness scores (Section 5) and use counts:
- Stories flagged as "Stale" or "Overuse Risk": deprioritize when alternatives exist. Don't eliminate — a Stale Strong Fit still outperforms a Fresh Gap.
- Stories flagged as "Proven Performer": boost priority. Past advancement contribution partially offsets staleness.
- When a stale story is selected because no alternative exists: note it and recommend developing a new story for this competency.

### Step 7: Output Final Mapping
Produce the final mapping with annotations (see Output Schema below).

---

## Section 3: Earned-Secret-Aware Selection

### Default Rule
Between equally ranked stories (same fit level and similar strength), prefer the one with a stronger earned secret. An earned secret makes a story memorable and drives Differentiation scores.

### Conditional Boost
When company culture signals prize differentiation (e.g., companies known for "bar raiser" rounds, companies whose values emphasize innovation or unique thinking, or when Calibration State shows Differentiation predicts advancement), boost stories with strong earned secrets by treating them as +1 fit level.

Example: S005 (Workable, strong earned secret) competes with S008 (Workable, no earned secret). Under the conditional boost, S005 is treated as Strong Fit equivalent.

### When Calibration Confirms
If `coaching_state.md` → Calibration State → Scoring Drift Log shows that Differentiation predicts advancement for this candidate (i.e., advancements correlate with higher Differentiation scores and rejections correlate with lower), upgrade this from conditional to default: always prefer stories with stronger earned secrets.

---

## Section 4: Secondary Skill Utilization

When no story has the target competency as its Primary Skill:
1. Check Secondary Skills across the storybank.
2. A story with the target competency as a Secondary Skill starts at **Workable** fit level.
3. Provide framing guidance: "This story's primary skill is data-driven decision making, but it also demonstrates influence without authority (secondary). Lead with the influence angle: how you got the engineering team to prioritize without having direct authority over them."

Secondary skill matches are always Workable at best — never Strong Fit — because the competency isn't the centerpiece of the story.

---

## Section 5: Story Freshness Score

**The problem**: Use count alone is a blunt instrument. A story used 6 times 8 months ago is functionally fresh. A story used 3 times in the last 2 weeks is overcooked. A story about a project from 6 years ago may feel dated regardless of use count. Freshness needs to account for all three dimensions.

### Three Freshness Factors

Assess each factor independently, then combine into a verdict:

**Factor 1 — Use Frequency Risk**
How often has this story been practiced or used in interviews, and how recently?
- **Low risk**: Used 1–2 times total, OR last use was 3+ months ago regardless of count
- **Medium risk**: Used 3–4 times, with at least one use in the last 2 months
- **High risk**: Used 5+ times in the last 3 months — over-rehearsal territory. Delivery may feel mechanical.

**Factor 2 — Recency of Underlying Experience**
How old is the event the story describes?
- **Low risk**: Experience is < 3 years old — well within "recent and relevant" territory for most roles
- **Medium risk**: Experience is 3–5 years old — still usable, but may need updated framing or a bridge to current context
- **High risk**: Experience is 5+ years old — can feel dated. Exception: career-defining or uniquely powerful stories that have no current equivalent. These should be flagged but not automatically deprioritized.

**Factor 3 — Proven Performer Status**
Has this story contributed to real interview advancement?
- **Yes**: Partially offsets High risk on other factors. A story with a demonstrated track record of working is worth preserving even if it's been used frequently.
- **No**: No offset. Standard freshness rules apply.

### Freshness Verdict

| Factor Combination | Verdict | Action |
|---|---|---|
| 2+ High risk factors, no Proven Performer offset | **Stale** | Deprioritize when alternatives exist. Flag: "This story may feel mechanical or dated. Consider developing a replacement." |
| 1 High risk factor OR 2 Medium risk factors | **Moderate** | Use with awareness. Flag the specific risk: "Use frequency is high — focus on natural delivery." or "Experience is aging — consider bridging to a more recent example if available." |
| All Low risk (with or without Proven Performer) | **Fresh** | No action needed. |
| Any combo with Proven Performer offset | **Fresh (Proven)** | Use with confidence. "This story has a track record. Its use history is an asset, not a liability." |

### Recording in Storybank

Add a `Freshness` field to each storybank entry, updated after each use:

```
Freshness: [Fresh / Fresh (Proven) / Moderate / Stale]
Last assessed: [date]
```

Freshness should be re-assessed at the start of each prep cycle, not just when a story is selected. A story that was Moderate 3 months ago is likely Fresh again now.

### When Staleness is Acceptable

- **No alternative exists**: A Stale Strong Fit outperforms a Fresh Gap every time. Use the stale story, note the risk, and recommend developing a replacement.
- **Proven Performer**: If the story worked in past interviews, its familiarity is partially an asset — the candidate tells it with confidence. Monitor for mechanical delivery, not just use count.
- **Career-defining stories**: Some stories are irreplaceable — a founding moment, a breakthrough that defines the candidate's narrative identity. These should not be rotated out just because they're old. Instead, help the candidate keep them current with updated framing.

---

## Output Schema

Use this schema in `prep` output to replace the current simple story mapping:

```markdown
## Story Mapping

### Mapping Matrix
| Question | Primary Story | Fit | Freshness | Backup Story | Fit | Notes |
|----------|--------------|-----|-----------|--------------|-----|-------|
| Q1: [question summary] | S### — [title] | Strong Fit | Fresh | S### — [title] | Workable | |
| Q2: [question summary] | S### — [title] | Workable | Moderate | S### — [title] | Stretch | Bridging: [guidance] |
| Q3: [question summary] | Gap | — | — | S### — [title] | Stretch | Gap-handling: Pattern 2 |
| Q4: [question summary] | S003 — [title] | Strong Fit | Stale | S### — [title] | Workable | Reusing S003 — no Workable+ alternative. Consider developing replacement. |

### Portfolio Health
- Unique stories used: [N] of [M] mapped questions
- Conflicts resolved: [e.g., "Q3 and Q4 competed for S003 — assigned to Q3 (higher fit), Q4 uses S006"]
- Reuse with different angle: [if any — e.g., "S003 used twice: Q1 stakeholder angle, Q4 constraint navigation angle"]
- Freshness warnings: [stories flagged Stale or Moderate — specific guidance for each]
- Prior round conflicts: [stories used in earlier rounds at this company]

### Gaps
- [Competency]: best available is [story] ([fit level]). Gap-handling: [Pattern 1–4]. Consider developing a new story for this competency.

### Strength Warnings
- [Question] -> [Story]: rated strength [N]. [Specific guidance — e.g., "This story needs quantified impact before deployment. Run `stories improve S###` to strengthen it."]
```

---

## Integration Points

### With Calibration Engine (`references/calibration-engine.md`)
- When scoring drift adjusts a dimension, flag stories whose strength ratings were driven by that dimension for re-evaluation.
- When calibration shows Differentiation predicts advancement, upgrade earned-secret-aware selection from conditional to default.
- When calibration links a specific dimension to rejections, elevate story mapping gaps in that dimension's competencies to "Calibration-Urgent" priority.

### With Prep (`references/commands/prep.md`)
- Prep Step 7 runs a storybank health check before mapping.
- Prep Step 8 invokes this engine for the full mapping protocol.

### With Stories (`references/commands/stories.md`)
- Gap analysis in `stories find gaps` uses the fit scoring system to classify gaps.
- Secondary skills are checked for coverage before declaring a competency a true gap.
- During `stories find gaps`, the Gap classification triggers guided story development — the memory excavation protocol for that specific competency (see `stories` command, sub-option: Find gaps).

### With Progress (`references/commands/progress.md`)
- Storybank health metrics include overuse tracking, freshness risk, and proven performer status.
- Story freshness scores are re-assessed at the start of each progress review cycle.
