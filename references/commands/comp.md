# comp — Compensation Strategy

**Job:** *Have a defensible number ready before the recruiter asks.*

> **Distinct from `negotiate`:** `negotiate` runs at offer stage with actual offer numbers and counter-strategies. `comp` runs before the first recruiter screen to establish your market position and anchoring strategy. Run `comp` early; run `negotiate` when you have the offer.

---

## Reference Knowledge

### How Comp Conversations Actually Work

**The Anchoring Effect**: The first number mentioned in a compensation conversation becomes the anchor. If a candidate says "$120K" in a recruiter screen, the final offer will orbit $120K — regardless of market rate. This makes the recruiter screen the highest-leverage comp moment. By the time `negotiate` fires (post-offer), the anchor is already set. `comp` coaches the moment that sets the anchor.

**The Comp Conversation Timeline** (stages `comp` covers):
1. **Application form**: "Expected salary" field. First anchor risk.
2. **Recruiter screen**: "What are your salary expectations?" or "What's your current compensation?" — Highest-stakes comp moment.
3. **Mid-process**: Hiring manager mentions range informally, or recruiter checks comp alignment.
4. **Pre-offer**: Recruiter discusses comp structure, tests whether candidate will accept.
5. **Formal offer** → `negotiate` handles this stage.

`comp` covers stages 1–4. `negotiate` covers stage 5. The handoff is explicit.

**The Deflection vs. Disclosure Tradeoff**:
- Deflecting works best early but becomes less tenable as the process progresses.
- Over-deflecting can signal difficulty, evasiveness, or game-playing.
- Disclosing a researched range (not a point number) is the pragmatic middle ground.
- Key principle: let the company share their range first when possible. The party that names a number first is at a disadvantage.
- In jurisdictions with salary transparency laws, the company must disclose the range — leverage this.

**Salary History Bans**: A growing number of US states and cities prohibit employers from asking salary history (check current state law — this list expands regularly). In banned jurisdictions, they may still ask salary expectations. The coach does NOT provide legal advice — points to lookup resources and coaches the response strategy.

**Comp Range Research Sources** (honest quality assessment):
- **Levels.fyi** — Strongest for tech. Real, verified data with company-specific bands. Limitation: mostly FAANG/big tech, less coverage for mid-size/startups.
- **Glassdoor** — Broader coverage. Self-reported, often outdated. Useful as directional signal, not precise benchmark.
- **Blind** — Anonymous, tech-focused. Variable reliability. Good for sentiment, less reliable for exact numbers.
- **Salary transparency postings** — Many jurisdictions require posted salary ranges (CO, NYC, CA, WA state). Most reliable when available.
- **Recruiter-disclosed ranges** — When a recruiter shares the range, this is the most reliable data for that specific role.
- **Compensation.fyi, Comprehensive.io** — Aggregators of varying quality. Cross-reference, don't rely on a single source.

**Critical principle**: Never fabricate comp data. Never state a salary range as if it's authoritative. Guide the candidate to research sources, help them interpret what they find, help them construct a defensible range.

**Common Comp Mistakes**:
1. Giving a specific number instead of a range (anchors too precisely)
2. Anchoring to current salary rather than market rate (especially in transitions)
3. Not researching before the conversation (shooting blind)
4. Treating base as the only metric (ignoring total comp)
5. Revealing current comp when not legally required to
6. Not asking for the company's range first
7. Getting flustered and saying "I'm flexible" or "whatever's fair" (signals low confidence)
8. Revealing competing offers too early (before leverage is built)
9. Using a range based on current location when the role is in a different market

---

## When to Run

- Before any recruiter screen where comp is likely to come up (almost all of them)
- When you don't know what number to give if asked
- When you need to sanity-check whether your expectations align with the market
- When you have multiple targets at different company types (startup vs. public vs. FAANG) and need differentiated anchors

---

## What This Command Can and Can't Do

**Can do:**
- Frame your negotiation strategy for recruiter comp conversations
- Help you identify the right anchoring approach for each company tier
- Script your response to "what are you looking for?" — a range with a floor, not a single number
- Coach comp conversation timing: when to push for a number, when to defer
- Help you think through total comp (base, equity, bonus, non-monetary) as an integrated picture

**Can't do:**
- Provide real-time market data — no access to current salary databases
- Tell you what the specific company pays — that requires external research
- Give tax or legal advice on equity structures

**Before running:** You need market data. The command is more useful if you bring numbers from Levels.fyi, Glassdoor, LinkedIn Salary, or compensation surveys. If you haven't done this research, say so — I'll tell you what to look up first.

---

## Priority Check

- **No `kickoff` yet**: Soft gate — "I can provide general comp coaching, but without your target role and seniority I can't help calibrate a range. Run `kickoff` first, or tell me your target and I'll work with that."
- **User already has a written offer**: Redirect — "Sounds like you have a written offer. `negotiate` is designed for post-offer strategy. Want to switch?" Note: verbal indications of interest or pre-offer comp alignment conversations are still `comp` territory — only redirect when a formal written offer exists.
- **Urgent** ("recruiter is calling in 30 minutes"): Fast-track to Quick Script — skip research guidance, provide deflection + range scripts immediately.
- **Comp strategy already exists**: Check if context has changed (new target, new company, new stage). Update rather than rebuild.

---

## Required Inputs

- Comp situation: What specifically is happening? (application form / recruiter screen / mid-process call / general strategy / "I don't know what to say about salary")
- Target role context (from coaching_state.md Profile, or ask)

## Optional Inputs

- Depth level: Quick Script / Standard / Deep Strategy (default: Standard)
- Current comp (for calibration — NEVER disclosed to the employer, used only for coaching)
- Research they've already done (ranges, sources)
- Specific company (for targeted research guidance)
- Jurisdiction (for salary history ban awareness)

---

## Depth Levels

| Level | When to Use | What It Covers |
|---|---|---|
| **Quick Script** | "Recruiter is calling in 30 minutes, what do I say?" | Deflection script + range framing script + 3 do-not-say phrases + key principle |
| **Standard** | Default. Full comp strategy for a specific opportunity or general search. | Comp research guidance + range construction + scripts for each comp stage + total comp education + jurisdiction awareness |
| **Deep Strategy** | Career transition, multiple offers likely, executive comp, startup equity evaluation | All of Standard + comp positioning strategy + market analysis guidance + multi-offer leverage planning + comp conversation lifecycle map + Challenge Protocol |

---

## Sequence

**Step 1: Context Assembly**
Pull from coaching_state.md: Profile (target role, seniority, location), Interview Loops (active companies, comp data for each if previously shared), JD Analyses (comp data from JD if `decode` was run and range was included), Comp Strategy (if `comp` was run previously — build on it, don't restart).

**Step 2: Situation Assessment** (ask one at a time)
1. What's the comp conversation? (application form / recruiter screen / mid-process / pre-offer / general strategy)
2. Timeline? (urgent = fast-track to scripts; not urgent = full strategy)
3. What's the candidate's current anchor? (do they have a number in mind? is it calibrated to market, or based on current salary?)
4. What research have they done? (none / some / thorough)
5. Jurisdiction? (salary history ban relevant? salary transparency in postings?)

**Routing decision** (after collecting answers):
- If urgent (recruiter calling <60 mins away): → Quick Script, skip Steps 3–5, go directly to Step 4 scripts
- If no research done + not urgent: → Standard, begin at Step 3 (research guidance first)
- If research done + career transition / multiple offers / equity-heavy: → Deep Strategy
- If research done + single opportunity + standard structure: → Standard, begin at Step 4

**Step 3: Comp Research Guidance** *(skip if urgent — go to Step 4)*
Guide the candidate to research — do NOT fabricate comp data. If urgent, acknowledge the gap explicitly in the Quick Script output: "Note: this script uses a placeholder range — before your next comp conversation, do the research below."
- Point to specific sources matched to their target
- Explain how to interpret what they find (base vs. total comp, percentile meaning, geographic adjustment, band vs. market average)
- Help construct a range:
  - **Bottom** = minimum acceptable (below this, walk away or negotiate hard)
  - **Target** = market rate at their level and location (what a fair offer looks like)
  - **Stretch** = what they'd get with strong positioning, competing offers, or exceptional fit
- If candidate has already researched: validate sources, help interpret, calibrate range
- Explicitly state confidence in the range and what data is missing

**Step 4: Script Construction** (stage-specific)
Provide scripts for the candidate's current stage AND the next likely stage. Every script includes a primary version AND a backup.

**Step 5: Total Comp Education** (Standard + Deep)
Quick primer tailored to the candidate's situation:
- How to weight base vs. equity vs. bonus (varies by career stage, risk tolerance, company stage)
- How to evaluate startup equity (see Startup Equity Decision Framework below)
- How to compare offers with different structures (total comp normalization, risk-adjusted comparison)
- Common traps: comparing base-to-base instead of total-to-total, overvaluing illiquid equity, ignoring vesting cliffs

**Step 6: Challenge Protocol** (Deep Strategy only)
Apply via challenge-protocol.md at the candidate's current activation level (L3–L5). At L3: Assumption Audit only. At L4: add Blind Spot Scan. At L5: add Devil's Advocate and Strengthening Path. See challenge-protocol.md for comp-specific invocation.

---

## Comp Conversation Scripts

### "What are you looking for in terms of compensation?"

**Wrong answers:**
- "I'm open" — signals you'll accept their anchor; leaves money on the table
- "I'm currently making $X" — anchors to the wrong number; recruiter works from that floor
- A single number — you've given away your ceiling with no room to negotiate

**Right approach — the range with context:**
```
"Based on my research for [role title] at [company stage], I'm targeting a total comp range of
[$X to $Y]. I'm weighting that toward base + [equity/bonus] depending on the stage and structure.
I'm flexible within that range — what does the band look like for this role?"
```

The counter-question ("what does the band look like?") is not aggressive — it's calibrating. Any recruiter who won't share the band after you've shared your range is giving you information.

### "What are you currently making?"

**In salary history ban jurisdiction:**
```
"I'm in [state/city] where salary history isn't part of the process, but I'm happy to share
my target range for this role: [range]."
```

**Outside ban jurisdiction — prefer deflection:**
```
"I'd rather focus on the market rate for this role than anchor to my current comp — they're
measuring different things. Can you share the range you have budgeted?"
```

**If they insist:** Share total comp (not just base), rounded, then follow immediately with your target range:
```
"My current total comp is in the [rounded range]. For this move, I'm targeting [higher range]
because [specific reason — scope increase, market rate correction, seniority step]."
```

### "Is that range flexible?"

```
"I'm realistic about ranges — what I care about is the full picture: base, equity structure,
and growth trajectory. If the base is on the lower end, there's often flexibility on signing
or equity. What does the structure typically look like?"
```

### Mid-process: "Are we still aligned on comp?"

```
"Yes — based on what I've learned about the role's scope, [range] still feels right. I'd love
to understand how the total comp package is structured at this level."
```

If range needs to adjust up:
```
"As I've learned more about the scope of this role, I'd want to be in the [adjusted range].
Can you share how the package typically breaks down?"
```

---

## Remote / Location Comp Adjustment

Location significantly affects comp ranges. When helping construct a range:

- **Remote roles at HQ-based companies**: Many companies pay based on the candidate's location (cost-of-living adjustment), not HQ. Ask: "Is this role remote? If so, does the company adjust comp by location?" If yes, the range needs geographic calibration — an SF-based range doesn't apply to a candidate in Austin.
- **Relocation**: Research the target location's market rate, not the candidate's current one. Moving from a low-cost area to SF should anchor to SF rates. Moving from SF to a low-cost area may face downward pressure — prepare for that conversation.
- **Hybrid vs. fully remote**: Some companies offer different comp bands for hybrid vs. fully remote. Ask the recruiter if the comp band differs by work arrangement.
- **Comp range research**: Many data sources show location-adjusted ranges. Point candidates to geographic salary comparison tools alongside Levels.fyi/Glassdoor.

---

## Startup Equity Decision Framework

**Trigger**: Deploy this framework when the candidate is evaluating (or expecting) a startup offer where equity is >20% of the stated total comp, or when they ask about equity. Skip for public company offers where equity is liquid RSUs — those go straight to the vesting comparison in Step 5.

When the candidate is evaluating a startup offer with meaningful equity, walk through this framework:

**1. What stage is the company?**
Pre-seed/seed (highest risk, highest potential upside, hardest to value), Series A-B (validated product, significant risk, more data), Series C+ (lower risk, lower upside multiplier), Pre-IPO (most predictable — check lockup periods and secondary market access).

**2. The expected value reality check**
Ask the candidate to estimate, honestly, the probability they believe this company will have a liquidity event in the next 5–7 years. The base rate for venture-backed startups reaching IPO or meaningful acquisition is ~10–20%. Multiply the equity grant's paper value by that probability. If the expected value is less than the cash comp difference vs. a public company offer, the equity isn't compensating for the risk.

**3. The cash-floor test**
"Can you live on the base salary alone, as if the equity is worth $0? If not, you're depending on equity for financial stability — that's a high-risk position." Base should cover needs. Equity is upside, not income.

**4. Dilution modeling**
Each funding round dilutes existing shareholders. "If the company raises 2 more rounds before an event, your shares could be diluted by 30–50%. Does the potential growth outweigh the dilution?" Don't calculate specific numbers — guide the candidate to ask the company about expected dilution.

**5. The comparison anchor**
"Compare the total package as if the equity is worth $0 (worst case) and as if it hits the target valuation (best case). Both scenarios should be acceptable for this to be a good decision."

---

## Output Schemas

### Quick Script
```markdown
## Comp Quick Script

### Your Situation
[1-2 sentence assessment]

### Key Principle
[The one thing to remember in this conversation]

### Primary Script
[Exact language — ready to say out loud]

### If They Push Back
[Backup script for the most likely pushback]

### Do NOT Say
1. "[specific phrase]" — [why it hurts you]
2. "[specific phrase]" — [why it hurts you]
3. "[specific phrase]" — [why it hurts you]

**Recommended next**: Re-run `comp` at Standard depth after the call to build a full comp strategy (Quick Script is one-time triage, not a permanent plan).
**Alternatives**: `prep [company]`, `negotiate` (when you have an offer)
```

### Standard
```markdown
## Comp Strategy: [Target Role / Company]

### Situation Assessment
- Stage: [application / recruiter screen / mid-process / general]
- Research status: [none / partial / thorough]
- Jurisdiction: [salary history ban status, if applicable]

### Research Guide
- **Sources to check**: [specific to their target]
- **Range construction**:
  - Bottom (minimum acceptable): [guidance]
  - Target (market rate): [guidance]
  - Stretch (strong positioning): [guidance]
- **How to present the range**: "[recommended language]"
- **Confidence in this range**: [honest assessment — what data is missing]

### Scripts
#### [Current Stage]
**Primary**: [exact language]
**If they push back**: [backup language]
**Rationale**: [why this language works]

#### [Next Likely Stage]
**Primary**: [exact language]
**Rationale**: [brief]

### Total Comp Primer
- How comp is typically structured for [role/level]: [base/equity/bonus split]
- What to watch for with [company type]: [specific]
- If multiple offers emerge: [comparison framework]

### Jurisdiction Notes [if applicable]
- Salary history: [banned / not banned]
- Salary transparency: [required / not required]

**Recommended next**: `negotiate` (when offer arrives), `prep [company]`.
```

### Deep Strategy
```markdown
## Comp Deep Strategy: [Target Role]

[All Standard sections, expanded]

### Comp Positioning [for transitions or large comp jumps]
- Current comp context: [candidate-provided, coaching use only]
- Target comp: [market rate at target level and location]
- Gap: [the delta]
- Framing language: ["This reflects the scope increase from [current] to [target]" — value-based, not cost-based]

### Market Analysis Guidance
- How to research this specific company's bands: [specific steps]
- How to read Levels.fyi for [their target]: [interpreting percentiles, recency, geography]
- How to cross-reference sources: [triangulation approach]

### Multi-Offer Leverage Planning [if multiple offers expected]
- Timing strategy: how to align offer windows (slow down fast processes, speed up slow ones)
- Leverage framing: [language for "I have competing offers" that builds leverage without burning bridges]
- When NOT to reveal other offers: [situations where it hurts — e.g., if the other offer is from a lower-tier company]

### Comp Lifecycle View
- Current stage: [where you are]
- Next stages: [comp milestones ahead]
- Handoff to `negotiate`: once you have a written offer with specific numbers

### Challenge (per challenge-protocol.md activation level — L3+ only)
- **Assumptions** (L3+): [what must be true for this comp strategy to work]
- **Blind spots** (L4+): [what you can't see about your own comp positioning]
- **Devil's advocate** (L5): [strongest case that this strategy is miscalibrated]
- **Highest-leverage change** (L5): [the one adjustment that most improves your comp outcome]

### Priority Moves (ordered)
1. [highest-impact — do this first]
2. [second]
3. [third]

**Recommended next**: `negotiate` (when offer arrives), `prep [company]`, `research [company]`
```

---

## Competency Guardrails

This command touches financial territory. Be explicit about what you can and can't do:

- **Can do**: Script the conversation, build anchoring strategy, frame the total comp picture, help evaluate whether to defer or disclose, walk through the equity decision framework.
- **Can't do**: Provide tax advice on equity structures (ISOs, NSOs, AMT triggers), legal advice on salary history disclosure requirements by state, or real-time market data.
- **Specific triggers to flag**:
  - AMT implications for ISOs → "This is getting into tax territory. Consult a tax professional before exercising options early."
  - Relocating across states → comp and tax treatment differ significantly; don't advise.
  - Complex equity structures (SAFEs, liquidation preferences, secondary markets) → flag for `negotiate` and suggest a financial advisor.

---

## Design Principles

**You can't undo a low anchor.** The comp conversation is a one-shot negotiation. Get it right before you're in the room (or on the call).

**Market data is the candidate's job.** The command builds strategy from data the candidate brings. If they haven't done the research, the strategy is directional, not precise. Say so: "I can frame the approach, but you need market data before you name a number. Spend 20 minutes on Levels.fyi for this role/location/level before the call."

**Total comp, not just base.** A $180K base with $400K equity over 4 years and a 20% bonus is a different conversation than $180K base with no equity. Make sure the candidate is working from a total comp number.

**Integrate with `negotiate`.** What gets said in the recruiter screen becomes context for the final negotiation. Log what you shared (or didn't) so `negotiate` can build on it rather than contradict it.

---

## Coaching State Integration

```markdown
## Comp Strategy
- Date: [date]
- Depth: [Quick Script / Standard / Deep Strategy]
- Target range: [bottom / target / stretch — or "not yet researched"]
- Range basis: [sources used / "candidate needs to research"]
- Research completeness: [none / partial / thorough]
- Stage coached: [application / recruiter screen / mid-process / general]
- Jurisdiction notes: [relevant salary history ban, if applicable]
- Scripts provided: [which stages covered]
- Key principle: [the most important thing to remember]
```
