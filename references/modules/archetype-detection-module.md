## Archetype Detection Module

Different PM roles require fundamentally different framing, story selection, and interview preparation. A Platform PM interview and a Founding PM interview test different things. This module detects the role archetype once, then cascades the framing to every downstream step. Borrowed from career-ops (santifer/career-ops) archetype-driven adaptation pattern.

**When to run:** During `prep` Phase 1 (after JD is parsed, before any prep output is generated). Also during `decode` when evaluating fit.

**Archetypes (detect one per role):**

| Archetype | Signals in JD | What They're Testing | Story Priority | Earned Secret Priority |
|-----------|--------------|---------------------|---------------|----------------------|
| **Platform PM** | "internal teams," "infrastructure," "developer experience," "APIs," "platform," "self-serve" | Systems thinking, cross-team influence, technical depth, scaling patterns | S004 (Consortium Hash), S003 (AI Agents architecture), S009 (Banking Stack) | Technical adoption decisions, architecture tradeoffs |
| **Founding PM** | "first PM," "build from scratch," "0-1," "define the roadmap," "wear many hats," "founder" | Ownership breadth, scrappiness, prioritization under ambiguity, builder instinct | S004 (Consortium zero-to-one), S005 (Fraud Browser), S006 (Rebuild Call) | What you built vs. what you managed; when to build vs. buy |
| **Domain PM** | Specific vertical named (fraud, collections, lending, compliance), "deep domain," "subject matter expert" | Domain depth, customer empathy, regulatory knowledge, workflow understanding | S009 (Banking Stack), S001 (Consortium Activation), S002 (Regulator's Question) | Industry insights competitors don't have; customer patterns only visible from inside |
| **Regulatory Response PM** | "compliance," "regulatory," "global affairs," "policy," "mandates," "assurance" | Regulatory translation, cross-team coordination, ambiguity navigation, stakeholder management | S002 (Regulator's Question), S010 (IDV Kill), S007 (FI Narrowing) | How regulation shapes product decisions; when compliance is a feature vs. a constraint |
| **Agent/AI PM** | "AI agents," "LLM," "automation," "agentic," "model," "ML," "eval" | AI product judgment, eval-driven development, trust/safety tradeoffs, human-AI loop design | S003 (AI Agents), S006 (Rebuild Call), S004 (Consortium Hash for trust patterns) | When AI fails gracefully vs. catastrophically; adoption vs. accuracy tradeoffs |
| **GTM/Growth PM** | "go-to-market," "acquisition," "activation," "expansion," "funnel," "conversion" | Commercial judgment, metrics definition, experiment design, customer segmentation | S007 (FI Narrowing), S001 (Consortium Activation), S008 (Vanity Metrics) | When to kill deals for strategic focus; detection vs. action gap |

**Detection rules:**
1. Read the JD. Match keywords from the "Signals in JD" column.
2. If multiple archetypes match, pick the one with the strongest signal density (most keywords matched).
3. If no clear match, default to **Domain PM** (safest generic framing).
4. Save the detected archetype to the Interview Loop entry: `Archetype: [type]`

**How the archetype cascades:**

| Downstream Step | What Changes |
|----------------|-------------|
| `prep` story mapping | Prioritize stories from the archetype's Story Priority column |
| `prep` predicted questions | Weight questions toward the archetype's testing dimensions |
| `prep` "Why this company" | Frame around what the archetype values (builder instinct for Founding, systems thinking for Platform, domain depth for Domain) |
| `mock` question selection | Bias toward the archetype's testing dimensions |
| `hype` 3x3 concerns | Tailor to archetype-specific interviewer concerns |
| `outreach` and cover letters | Lead with the proof points that map to the archetype |
| `decode` fit assessment | Score fit against archetype requirements, not just generic PM requirements |

**Integration:**
- `prep`: Run archetype detection in Phase 1 after JD parsing. Surface: "Detected archetype: **[type]**. This shapes which stories I'll prioritize and which questions I'll predict." Save to Interview Loop.
- `decode`: Include archetype in fit assessment output.
- `mock`: Use archetype to bias question selection.
- `hype`: Use archetype to frame 3x3 concerns.
- `outreach`: Use archetype to select lead proof point.

---
