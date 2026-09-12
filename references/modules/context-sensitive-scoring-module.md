## Context-Sensitive Scoring Module

Scoring dimensions carry different predictive weight depending on what kind of exchange is happening and who is evaluating. Flat weighting across all contexts produces misleading coaching priorities. A structural critique of a moat discussion is noise; the same critique of a behavioral answer is signal.

**Two classification axes** are applied per scored unit before weights are set.

### Axis 1: Question Type

Detect from the question text before scoring each unit.

| Type | Detection Signals |
|---|---|
| **Behavioral** | "tell me about a time," "give me an example," "describe a situation," "walk me through a time" |
| **Strategic-Hypothetical** | "what do you think about," "what's your view on," "how would you approach," "where do you see," theoretical or market questions with no behavioral anchor |
| **Case / System Design** | "design a product," "how would you build," "walk me through how you'd think about," analytical or estimation prompts |
| **Culture-Fit** | "tell me about yourself" (opener context), "why us," "what are you looking for," "what matters to you" |

### Axis 2: Interviewer Type

Detect once per session from: Interview Loops entry (interviewer title/role), then debrief notes, then transcript intro. If none yield a clear signal, ask: "Who's your interviewer, what's their role?" Fallback: Peer.

| Type | Detection Signals |
|---|---|
| **Executive / CEO / Founder** | C-suite title, founder, GM, VP+ at a startup; questions about vision, judgment, ownership |
| **Technical** | Engineering, data science, research title; questions probing methodology, systems, or metrics |
| **HR / Recruiter** | "Recruiter," "talent," "people ops," "coordinator"; structured screening questions |
| **Peer** | Same-level IC or PM; conversational, collaborative tone |

### Weighting Table

Apply base weights by question type. Then apply interviewer modifier (additive). Re-normalize to 100% after applying modifier.

**Base weights by question type:**

| Dimension | Behavioral | Strategic-Hypoth. | Case / Design | Culture-Fit |
|---|---|---|---|---|
| Substance | 25% | 40% | 20% | 20% |
| Structure | 25% | 10% | 30% | 10% |
| Relevance | 20% | 20% | 20% | 20% |
| Credibility | 20% | 15% | 15% | 10% |
| Differentiation | 10% | 15% | 15% | 40% |

**Interviewer-type modifier (additive, before re-normalization):**

| Dimension | Executive | Technical | HR / Recruiter | Peer |
|---|---|---|---|---|
| Substance | +5% | 0% | -5% | 0% |
| Structure | -5% | +5% | +5% | 0% |
| Relevance | 0% | 0% | +5% | 0% |
| Credibility | -5% | +10% | -5% | 0% |
| Differentiation | +5% | -15% | 0% | 0% |

### Feedback Framing Shifts

Context changes not just the weight but the language of coaching.

**Structure: when Question Type = Strategic-Hypothetical.**
Don't say: "Your answer lacked a clear structure."
Say: "State your position upfront, then build the case. In a discussion like this, logical coherence matters more than narrative arc."

**Structure: when Question Type = Culture-Fit.**
Suppress structure feedback unless the answer was actively confusing. Authenticity reads better than format compliance here.

**Credibility: when Interviewer Type = Technical.**
Probe harder on specificity. "What model did you use?" / "What was the actual metric?" / "How did you validate?" If credibility is low, the coaching recommendation is specificity drills, not story structure work.

**Differentiation: when Question Type = Culture-Fit.**
This is the primary coaching axis. The candidate needs to feel memorable, not just competent. If Differentiation < 3 on a culture-fit question, it is the top coaching priority regardless of the standard priority stack.

### Output Format

Display context classification at the top of each scored unit:

```
Context: [Question Type] x [Interviewer Type]
Weighted composite: [X.X / 5]
```

When a dimension's effective weight is 10% or below after modifier (suppressed by context), add "(low weight for this context)" to its feedback line.
When a dimension's effective weight is 30% or above (elevated by context), add "(high weight for this context)" to its feedback line.

**Integration:** `analyze` Step 6.5 and `mock` Per-Unit Scorecard. The raw 1-5 scores per dimension are always recorded. The weighted composite is the coaching-priority signal. Do not replace raw scores with weighted ones.

---
