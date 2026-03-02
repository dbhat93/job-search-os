# Job Search OS

*Your job search, as a system.*

A Claude Code skill that runs your entire job search — from first company research to offer negotiation, with an interview coaching layer built in. It tracks every opportunity across a pipeline CRM, manages your network and referrals, scores your interview answers across five dimensions, builds a storybank you can retrieve under pressure, and adapts its coaching to your specific patterns.

Built on [interview-coach-skill](https://github.com/noamseg/interview-coach-skill) by [Noam Segal](https://www.linkedin.com/in/noamsegal/) (MIT License). Extended to run the whole search.

> **Scope:** The coaching layer (scoring, storybank, mocks, practice) works across PM, Engineering, Design, Data Science, and other functions. The search OS layer (pipeline, outreach, fit scoring, draft, comp strategy, weekly review) is scoped to **Product Management hiring**. Focus over breadth — PM first, other functions in a future version.

Say `kickoff`, share your resume, and you're being coached in under 2 minutes. Say `pipeline` to see where every opportunity stands.

---

## What It Does

**Scoring and diagnosis** — Every answer scored on Substance, Structure, Relevance, Credibility, and Differentiation, calibrated to your seniority. Scores map to root causes (status anxiety, narrative hoarding, conflict avoidance) with targeted fixes, not just "do better."

**Adaptive coaching** — After scoring, a decision tree triages your bottleneck and branches to the right drill. If Relevance is your gap, you get question-decoding practice. If Substance, you build raw material. The system doesn't cycle through the same sequence for every candidate.

**Storybank** — Structured story management with full STAR text, earned secrets, field performance notes, strength ratings, and rapid-retrieval drills so you can access the right story under time pressure.

**Practice and mocks** — 8-stage drill progression (constraint ladders, pushback handling, pivot drills, panel simulations, stress tests) plus full 4-6 question mock interviews in behavioral, system design, case study, panel, and technical+behavioral formats.

**Pipeline CRM** — Track every opportunity from first identification to offer decision. Stall detection, prep allocation guidance, and stage-synced coaching state. Nothing falls through the cracks.

**Networking** — Contact tracking with relationship strength, outreach status, pronoun discipline, and referral gap detection. Know who to reach before you apply, not after.

**Pre-application fit scoring** — Score any JD against your profile and storybank before committing prep time. Go/no-go with story gaps identified.

**Compensation strategy** — Have a defensible anchor before the recruiter asks. Scripts for the comp conversation, range construction, and timing guidance.

**Weekly search review** — Separate from coaching progress: pipeline velocity, prep allocation check, outreach momentum, deadline math. The search and the coaching measured independently.

**Session continuity** — A persistent `coaching_state.md` file tracks your storybank, scores, patterns, drill progression, and interview loops across sessions. Pick up where you left off, weeks later. Saves are automatic.

---

## Quick Start

### Option 1: Open in Claude Code on Desktop (recommended)

1. Clone the repo:

```bash
git clone https://github.com/dhirajbhat/job-search-os.git
cd job-search-os
```

2. Rename the skill file to activate:

```bash
cp COACH.md CLAUDE.md
```

3. Open the folder in Claude Code on Desktop and say `kickoff`.

The coach will ask for your resume, target role, and timeline — then build your profile, score your starting point, and give you a prioritized action plan. Everything saves automatically to `coaching_state.md`.

**Also works with**: Claude Code (terminal), Cursor, or any environment with file system access.

---

## Commands

### v1 — Pipeline & Email

The search infrastructure layer. Track opportunities, draft emails, run the pipeline.

| Command | Purpose | Output |
|---|---|---|
| `pipeline` | Full pipeline snapshot — all loops, sorted by urgency | Stage view + stall detection + prep allocation + priority move |
| `pipeline add [company]` | Add a new opportunity | Guided intake → new pipeline row |
| `pipeline update [company]` | Move stage, log activity, set next action | Updated pipeline |
| `pipeline stall` | Surface loops with no activity in 7+ days | Stalled loops + recommended next actions |
| `pipeline close [company]` | Archive with outcome and lessons | Closed entry + outcome log update |
| `draft [company]` | Follow-up after an interview interaction | One tight draft anchored to a specific moment, ready to send |
| `draft [contact]` | Cold or warm outreach to a person | Draft calibrated to relationship strength |
| `draft recruiter` | Recruiter communication — scheduling, status, declinations | Concise, professional draft |
| `draft review [company]` | Feedback-solicitation email after a rejection | Non-defensive ask anchored to a specific moment from the loop |

### v2 — Full Search Layer

Fit scoring before you apply. Network and referral management. Comp strategy before the recruiter asks. Weekly search pulse.

| Command | Purpose | Output |
|---|---|---|
| `fit [JD]` | Pre-application fit scoring — should I apply? | 4-dimension fit score + story gaps + go/no-go recommendation |
| `outreach` | Networking CRM — referral contacts, follow-up tracking | Contacts by active loop + referral gaps + next touch |
| `outreach add [contact]` | Add a contact to the CRM | Contact record with pronoun defaults |
| `outreach prep [company]` | Surface contacts for an active loop + draft outreach | Referral leverage assessment + draft |
| `outreach followup` | Contacts due for follow-up | Stalled contacts + recommended next action |
| `comp` | Comp strategy before recruiter screens | Anchor range + scripted responses + timing guidance |
| `review` | Weekly search review | Pipeline health + prep allocation + coaching summary + outreach + deadline math |

### Coaching Layer (original, extended)

| Command | Purpose | Output |
|---|---|---|
| `kickoff` | Setup profile, track, preferences, pipeline survey | Kickoff summary + pipeline map + time-aware action plan |
| `research [company]` | Company research + fit assessment | Company snapshot + culture signals + fit assessment |
| `prep [company]` | Role-specific prep brief | Format scenarios (probabilistic), culture read, interviewer intel, competencies, predicted Qs, story mapping |
| `analyze` | Transcript analysis with triage-based coaching | Per-answer 5-dimension scoring + decision tree + coaching strategy update |
| `debrief` | Post-interview rapid capture (same day) | Questions recalled, signals, stories used, coaching state updated |
| `practice` | Drill rounds with progression gating | Round debrief + self-assessment delta + targeted adjustment |
| `mock [format]` | Full simulated interview (4-6 Qs) | Holistic arc + signal-reading + energy trajectory + per-Q scoring |
| `stories` | Build/manage storybank + retrieval drill | Story table + earned secrets + field notes + gap analysis |
| `concerns` | Anticipate interviewer concerns | Concern-counter-evidence map |
| `questions` | Generate tailored interviewer questions | 5 non-generic questions calibrated to interviewer + company |
| `hype` | Pre-interview confidence + psychological warmup | 60-second reel + 3x3 cheat sheet + recovery playbook |
| `thankyou` | Post-interview thank-you notes (within 24 hours) | Personalized note + multi-interviewer variants + advancing/rejected framing |
| `progress` | Trends, self-calibration, outcome correlation | Self-assessment delta + outcome correlation + coaching meta-check |
| `negotiate` | Post-offer negotiation coaching | Offer analysis + non-obvious success pathways + scripts + fallback language |
| `reflect` | Post-search retrospective + archive | Journey arc + breakthroughs + transferable lessons |
| `help` | Show command menu | Full command list + recommended next based on state |

### v3 — Strategy (Coming)

| Command | Purpose | Status |
|---|---|---|
| `strategy` | Whole-search strategy — sequencing, leverage, timeline math, energy allocation | Planned |

---

## Fast Workflow Examples

### 1) Initial setup

```text
kickoff
```

The coach will:
- Ask for your resume, target role, and interview timeline
- Analyze your resume for positioning strengths, likely concerns, and story seeds
- Survey your pipeline (desirability × fit per company → priority label)
- Give you a time-aware action plan (triage / focused / full coaching mode)

### 2) Before applying — fit check

```text
fit
```

Paste a JD. Get a 4-dimension fit score, story gap analysis, and a go/no-go recommendation before committing prep time.

### 3) Before an interview

```text
prep Stripe
```

Provide: JD, role/seniority, optional interviewer LinkedIn URLs.

Get: Format scenarios (probabilistic), culture read, interviewer intelligence, predicted questions, story mapping, day-of cheat sheet.

### 4) Right after an interview

```text
debrief
```

Rapid capture while details are fresh — works with or without a transcript. Captures signals, stories used, emotional read. Updates coaching state for the next session.

### 5) Analyzing a transcript

```text
analyze
```

Paste transcript. Get per-answer scoring, triage decision, storybank updates, and a priority move for the next 72 hours.

### 6) After a rejection — get signal

```text
draft review [company]
```

Generates a feedback-solicitation email anchored to a specific moment from your loop. Non-defensive, short, specific enough to actually get answered. Recommends who to send it to and when.

### 7) Weekly search review

```text
review
```

Pipeline health, prep allocation check, coaching progress summary, outreach momentum, deadline math. One priority move to close.

### 8) Comp before the recruiter asks

```text
comp
```

Build your anchoring strategy and scripted responses before any recruiter screen where comp comes up.

### 9) Post-offer negotiation

```text
negotiate
```

Provide offer details and competing offers. Get offer analysis, non-obvious career value pathways (not just comp), scripted negotiation language, and fallback responses.

---

## Repository Structure

```text
job-search-os/
├── COACH.md                            # Core skill — copy to CLAUDE.md to activate
├── README.md                           # This file
├── LICENSE                             # MIT License (Noam Segal + Dhiraj Bhat)
├── coaching_state.md                   # Created on first kickoff — gitignored, never committed
├── state/                              # Search OS state files — gitignored, never committed
│   ├── pipeline.md                     # Job search CRM (all opportunities + stages)
│   └── contacts.md                     # Networking CRM (created on first outreach add)
└── references/
    ├── commands/                       # Per-command workflows (loaded on demand)
    │   ├── pipeline.md                 # v1 — job search CRM
    │   ├── draft.md                    # v1 — email drafting (incl. draft review)
    │   ├── fit.md                      # v2 — pre-application fit scoring
    │   ├── outreach.md                 # v2 — networking CRM
    │   ├── comp.md                     # v2 — compensation strategy
    │   ├── review.md                   # v2 — weekly search review
    │   ├── kickoff.md                  # Extended — pipeline survey added
    │   ├── research.md
    │   ├── prep.md                     # Extended — probabilistic format scenarios
    │   ├── analyze.md                  # Extended — interview_type field
    │   ├── debrief.md
    │   ├── practice.md
    │   ├── mock.md
    │   ├── stories.md
    │   ├── concerns.md
    │   ├── questions.md
    │   ├── hype.md
    │   ├── thankyou.md
    │   ├── progress.md
    │   ├── negotiate.md                # Extended — non-obvious success pathways
    │   ├── reflect.md
    │   └── help.md
    ├── cross-cutting.md                # Shared modules: gap-handling, signal-reading, differentiation, cultural awareness, psychological readiness, cross-command dependencies
    ├── rubrics-detailed.md             # Scoring anchors, root causes, seniority calibration
    ├── role-drills.md                  # Role-specific drills + interviewer archetypes
    ├── differentiation.md              # Earned secrets, spiky POVs, clarity under pressure
    ├── transcript-processing.md        # Step-by-step transcript analysis guide
    ├── storybank-guide.md              # Story management + rapid-retrieval drill
    └── examples.md                     # Worked examples: scored answers, triage, rewrites
```

---

## Best Results

1. Share a real resume (not a high-level summary) at kickoff.
2. Include a full JD for `prep` and `fit` — the more specific, the better.
3. Use real transcripts for `analyze`. The more you give it, the better the triage.
4. Keep a living storybank with `stories`. Extract earned secrets for every story.
5. Run `review` weekly — pipeline health and coaching progress are different things. Track both.
6. After real interviews, log outcomes. The system correlates practice scores with real results.
7. Run `mock` before important interviews. Individual drills build skills; mocks test the full arc.
8. Use `debrief` the same day as a real interview — signals fade fast.
9. Add contacts before you're in Screening, not after. Referrals need lead time.

---

## FAQ

**How is this different from asking ChatGPT for interview help?**
Generic LLM interview help gives you the same advice regardless of your patterns. This system scores you on five dimensions, tracks your scores over time, diagnoses root causes, builds a storybank with retrieval drills, and adapts based on what the data reveals. It remembers your previous sessions, knows which stories you've already used at a company, and changes its approach when something isn't working. It's the difference between a textbook and a coach.

**Does the coaching layer only work for tech roles?**
No. Core coaching workflows are role-agnostic; role drills include PM, Engineering, Design, Data Science, Research, Operations, and Marketing. The search OS layer (pipeline, fit, outreach, comp, review) is PM-scoped in v1.

**Why is the feedback direct?**
The skill is high-candor and evidence-based. It uses strengths-first delivery and self-reflection before critique. You can set your feedback directness level (1-5) during kickoff. At every level, the diagnosis is the same — only the packaging changes.

**How does it work across multiple sessions?**
The skill writes a `coaching_state.md` file that tracks your storybank, scores, patterns, drill progression, interview outcomes, and interview loops. At the start of each session, it reads this file and picks up exactly where you left off. Saves happen automatically after every major workflow — not just at session end.

**What's in v3?**
The `strategy` command — sequencing multiple active loops, using leverage between companies, timeline math, energy allocation across the search. Planned after v1 + v2 are proven.

---

## Contributing

Open an issue or PR with:

- Repro steps
- Current behavior
- Expected behavior
- Suggested fix (optional)

---

## Credits

Original [interview-coach-skill](https://github.com/noamseg/interview-coach-skill) by [Noam Segal](https://www.linkedin.com/in/noamsegal/) — the coaching layer, 5-dimension rubric, storybank system, and session continuity design.

Extended to Job Search OS by [Dhiraj Bhat](https://www.linkedin.com/in/dhirajbhat/):
- **v1**: Pipeline CRM, draft command (incl. `draft review`), probabilistic format modeling, interview_type scoring, pipeline survey in kickoff, priority label redesign, two-factor prep allocation
- **v2**: Fit scoring, outreach/networking CRM, comp strategy, weekly review, non-obvious success pathways in negotiate
- **v3**: Strategy command (planned)

---

## License

MIT
