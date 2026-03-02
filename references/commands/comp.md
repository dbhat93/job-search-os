# comp — Compensation Strategy

**Job:** *Have a defensible number ready before the recruiter asks.*

> **Distinct from `negotiate`:** `negotiate` runs at offer stage with actual offer numbers and counter-strategies. `comp` runs before the first recruiter screen to establish your market position and anchoring strategy. Run `comp` early; run `negotiate` when you have the offer.

---

## When to Run

- Before any recruiter screen where comp is likely to come up (almost all of them)
- When you don't know what number to give if asked
- When you need to sanity-check whether your expectations align with the market for your target roles
- When you have multiple targets at different company types (startup vs. public vs. FAANG) and need differentiated anchors

---

## What This Command Can and Can't Do

**What it can do:**
- Frame your negotiation strategy for recruiter comp conversations
- Help you identify the right anchoring approach for each company tier
- Script your response to "what are you looking for?" — a range with a floor, not a single number
- Coach comp conversation timing: when to push for a number, when to defer
- Help you think through total comp (base, equity, bonus, non-monetary) as an integrated picture

**What it can't do:**
- Provide real-time market data. I don't have access to current salary databases.
- Tell you what the specific company pays. That requires external research.
- Give tax or legal advice on equity structures.

**Before running:** You need market data. The command is more useful if you bring numbers from Levels.fyi (for PM roles at tech companies), Glassdoor, LinkedIn Salary, or compensation surveys. If you haven't done this research, say so — I'll tell you what to look up before we build a strategy.

---

## Sequence

1. **Collect inputs** (ask one at a time):
   - Target role title and seniority level
   - Target companies (or company tiers — e.g., "Series B startup, public fintech, FAANG")
   - Current comp (base + equity + bonus) — optional but useful for anchoring
   - Location and remote/in-office situation
   - Market data the candidate has gathered (Levels.fyi ranges, Glassdoor, etc.)

2. **Assess market position.** Using the candidate's research:
   - Where does their current comp sit relative to the market? (Below / At / Above)
   - What's the realistic target range for their seniority + company type combination?
   - What's the walk-away floor (the number below which they'd decline)?

3. **Build comp strategy by company tier.** Different companies have different comp structures — base-heavy vs. equity-heavy, narrow bands vs. wide bands, negotiation-friendly vs. rigid. Adjust approach accordingly.

4. **Script the recruiter conversation.** The most dangerous moment is when a recruiter asks "what are you looking for?" and the candidate freezes or names their current salary. Prepare the exact language.

5. **Timing guidance.** When to share numbers, when to ask for theirs first, when to anchor early vs. late.

---

## Comp Conversation Scripts

### "What are you looking for in terms of compensation?"

**Wrong answers:**
- "I'm open" — signals you'll accept their anchor; leaves money on the table
- "I'm currently making $X" — anchors to the wrong number; recruiter will work from that floor
- A single number — you've given away your ceiling with no room to negotiate

**Right approach — the range with context:**
```
"Based on my research for [role title] at [company stage], I'm targeting a total comp range of
[$X to $Y]. I'm weighting that toward base + [equity/bonus] depending on the stage and structure.
I'm flexible within that range — what does the band look like for this role?"
```

The counter-question ("what does the band look like?") is not aggressive — it's calibrating. Any recruiter who won't share the band after you've shared your range is giving you information.

### "What are you currently making?"

**Approach:** You don't have to answer. In most US states, asking for salary history is illegal. Even where it's legal, you can redirect:
```
"I'd rather focus on the market rate for this role than anchor to my current comp — they're
measuring different things. Can you share the range you have budgeted?"
```

If they push: share a total comp figure (not just base), rounded, and follow immediately with your target range.

### "Is that range flexible?"

**Approach:**
```
"I'm realistic about ranges — what I care about is the full picture: base, equity structure, and
growth trajectory. If the base is on the lower end, there's often flexibility on signing or equity.
What does the structure typically look like?"
```

---

## Output Schema

```markdown
## Comp Strategy: [Role] — [Company / Company Tier]

### Your Market Position
- Target range (base): [$X – $Y] — [Source: Levels.fyi / Glassdoor / stated]
- Market position of current comp: [Below / At / Above market]
- Walk-away floor: [$X] — [confirm this with yourself before the call]
- Total comp target: [$X – $Y] (base + equity + bonus, annualized)

### Company Tier Strategy
| Company type | Typical structure | Your approach |
|---|---|---|
| [e.g., Series B startup] | [equity-heavy, lower base] | [Lead with base ask; accept equity if structure is clear] |
| [e.g., Public fintech] | [balanced base + RSU] | [Lead with range; push on band transparency] |

### Anchoring Strategy
- **When asked first:** [Script — range with floor, ask for their band]
- **When you get their number first:** [Script — how to respond if it's below / at / above your range]
- **Timing:** [Early disclosure / Defer until final round — with rationale]

### Recruiter Screen Scripts

**"What are you looking for?"**
> [Exact script customized to this company type and role]

**"What are you currently making?"**
> [Script — redirect or share total comp with target range]

### Red Flags to Watch For
- [Company] has a reputation for narrow bands — if they won't share range, push once then decide whether to proceed
- Equity-heavy structures at early-stage companies require evaluating strike price and dilution — flag this for `negotiate` when you get an offer
- [Any specific concern based on company type or candidate situation]

### What to Log After the Call
- Did they share a range? [Note it for `negotiate` later]
- Did they ask for your current comp? [Note what you shared]
- What's their stated timeline? [Affects negotiation leverage later]

**Next commands**: `prep [company]` (interview prep), `negotiate` (when offer arrives), `pipeline update [company]` (log comp conversation as activity)
```

---

## Competency Guardrails

This command touches financial territory. Be explicit about what you can and can't do:

- **What you can do:** Script the conversation, build anchoring strategy, frame the total comp picture, help evaluate whether to defer or disclose.
- **What you can't do:** Provide tax advice on equity structures (ISOs, NSOs, AMT triggers), legal advice on salary history disclosure requirements by state, or real-time market data.
- **Specific triggers to flag:**
  - If the candidate asks about AMT implications for ISOs: "This is getting into tax territory. Consult a tax professional before exercising options early."
  - If the candidate is relocating across states: comp and tax treatment can differ significantly; don't advise.
  - Complex equity structures (SAFEs, liquidation preferences, secondary markets): flag for `negotiate` and suggest a financial advisor.

---

## Design Principles

**You can't undo a low anchor.** The comp conversation is a one-shot negotiation. Get it right before you're in the room (or on the call). That's the whole point of this command.

**Market data is the candidate's job.** The command builds strategy from data the candidate brings. If they haven't done the research, the strategy is directional, not precise. Say so: "I can frame the approach, but you need market data before you name a number. Spend 20 minutes on Levels.fyi for this role/location/level before the call."

**Total comp, not just base.** A $180K base with $400K equity over 4 years and a 20% bonus is a different conversation than $180K base with no equity. Make sure the candidate is working from a total comp number, not just salary.

**Integrate with `negotiate`.** What gets said in the recruiter screen becomes context for the final negotiation. Log what you shared (or didn't) so `negotiate` can build on it rather than contradict it.
