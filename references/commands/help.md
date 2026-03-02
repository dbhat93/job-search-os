# help — Command Reference Workflow

### Logic

When the user types `help`, generate a context-aware command guide — not just a static list.

1. **Read `coaching_state.md`** and **`state/pipeline.md`** to understand where the candidate is in their search and coaching journey.
2. **Show the full command guide** (see Output Schema below) with sub-commands and key features for each command.
3. **Highlight the 2-3 most relevant commands right now** based on state:
   - If no coaching state exists: highlight `kickoff`
   - If pipeline is empty or missing: highlight `pipeline add`
   - If storybank is empty: highlight `stories`
   - If storybank has 5+ stories but no narrative identity analysis: highlight `stories` (mention option 7)
   - If an interview is scheduled within 48 hours: highlight `hype` and `prep`
   - If transcripts exist but haven't been analyzed: highlight `analyze`
   - If 3+ scored sessions exist: highlight `progress`
   - If an offer was received: highlight `negotiate`
   - If a loop was recently rejected: highlight `draft review [company]`
   - If pipeline has loops with no contacts: highlight `outreach`
   - If drill progression shows the candidate hasn't completed Stage 1: highlight `practice ladder`
   - If it's been 7+ days since last `review`: highlight `review`
4. **Show current coaching state summary** (if it exists): track, seniority band, drill stage, story count, real interviews logged, active pipeline loops.
5. **End with a prompt**: "What would you like to work on?"

### Output Schema

```markdown
## Command Guide

### Getting Started
| Command | What It Does |
|---|---|
| `kickoff` | Set up your profile, choose a track (Quick Prep or Full System), and get a prioritized action plan. Includes a pipeline survey (desirability × fit per company → priority label) so your pipeline is populated from day one. |

### Search CRM — v1
| Command | What It Does |
|---|---|
| `pipeline` | Full pipeline snapshot — all active loops sorted by urgency, stall detection, prep allocation check, and this week's priority move. Reads from `state/pipeline.md`. |
| `pipeline add [company]` | Add a new opportunity. Guided intake: role, stage, priority, next action. Offers to open an Interview Loop in coaching state. |
| `pipeline update [company]` | Move a loop to a new stage, log activity, set next action. Automatically routes to `negotiate` if stage moves to Offer. |
| `pipeline stall` | Surface every loop with no activity in 7+ days, with recommended next actions by stage. |
| `pipeline close [company]` | Archive a loop with outcome (won/lost/withdrew) and lessons. Routes to `draft review` for feedback solicitation on rejections. |

### Search Layer — v2
| Command | What It Does |
|---|---|
| `fit [JD]` | Pre-application fit scoring before committing prep time. Paste a JD → get a 4-dimension fit score (Domain Match, Seniority Match, Story Coverage, Positioning Risk), story gap analysis, and a go/no-go recommendation. |
| `outreach` | Networking CRM. View all contacts by active pipeline loop, referral gap detection (active loops with no contacts flagged), and next touch recommendations. |
| `outreach add [contact]` | Add a contact — name, company, role, relationship strength, outreach status. Pronouns default to `unknown` until confirmed. |
| `outreach prep [company]` | For an active loop, surface relevant contacts and assess referral leverage. Drafts outreach if a contact is ready. |
| `outreach followup` | Contacts with no activity in 7+ days — recommended next actions by status. |
| `comp` | Compensation strategy before any recruiter screen. Build your anchoring range, scripted responses to "what are you looking for?", and timing guidance. Requires market data you bring (Levels.fyi, Glassdoor). |
| `review` | Weekly search review. Pipeline health, prep allocation check, coaching progress summary, outreach momentum, and deadline math. One priority move to close. Distinct from `progress` — measures search health, not coaching quality. |

### Email — v1
| Command | What It Does |
|---|---|
| `draft [company]` | Follow-up email after an interaction — anchored to a specific moment from the conversation. Reads debrief + coaching state. 4–7 sentences. |
| `draft [contact]` | Cold or warm outreach to a person — calibrated to relationship strength. Reads contact record if it exists; asks inline if not. |
| `draft recruiter` | Recruiter communication — scheduling, status requests, timeline extensions, declinations, responses to rejection. |
| `draft review [company]` | Feedback-solicitation email after a rejection. Anchored to the strongest moment from the loop. Non-defensive ask ("was there an area where my experience didn't match?"). Recommends who to send it to and when. |

### Interview Prep
| Command | What It Does |
|---|---|
| `research [company]` | Lightweight company research + fit assessment before committing to full prep |
| `prep [company]` | Full prep brief — probabilistic format scenarios (not one prediction), culture read, interviewer intelligence (from LinkedIn URLs), predicted questions, story mapping, day-of cheat sheet |
| `concerns` | Anticipate likely interviewer concerns about your profile + counter-evidence strategies |
| `questions` | Generate 5 tailored, non-generic questions to ask your interviewer |
| `hype` | Pre-interview boost — 60-second hype reel, 3x3 sheet (concerns + counters + questions), warmup routine, mid-interview recovery playbook |

### Practice and Simulation
| Command | What It Does |
|---|---|
| `practice` | Drill menu with 8 gated stages + standalone retrieval. Sub-commands: `ladder` (constraint drills: 30s → 3min), `pushback` (handle skepticism and interruption), `pivot` (redirect when questions don't match prep), `gap` (no-example moments), `role` (specialist scrutiny), `panel` (multiple interviewer personas), `stress` (high-pressure simulation), `technical` (thinking out loud, clarifying, tradeoff articulation). Standalone: `retrieval` (rapid-fire story matching under time pressure). Includes interviewer's perspective on every round. |
| `mock [format]` | Full 4-6 question simulated interview with holistic arc feedback and interviewer's inner monologue. Formats: `behavioral screen`, `deep behavioral`, `panel`, `bar raiser`, `system design/case study`, `technical+behavioral mix` |

### Analysis and Scoring
| Command | What It Does |
|---|---|
| `analyze` | Paste a transcript. Per-answer 5-dimension scoring (Substance, Structure, Relevance, Credibility, Differentiation), triage-based coaching that branches to your specific bottleneck, answer rewrites showing what a 4-5 looks like, and a priority move for the next 72 hours. Scores tagged by interview type so trends compare like-for-like. |
| `debrief` | Post-interview rapid capture — same day, with or without a transcript. Captures questions recalled, interviewer signals, stories used, emotional read. Updates coaching state. The complement to `analyze`, not a replacement. |

### Storybank
| Command | What It Does |
|---|---|
| `stories` | Full storybank management. `view` (full index with health check), `add` (guided discovery — reflective prompts, not just "tell me a story"), `improve` (structured upgrade with before/after), `find gaps` (prioritized by target roles and competency coverage), `retire` (archive weak stories), `drill` (rapid-fire retrieval: 10 questions, 10 seconds each), `narrative identity` (extract your 2-3 core career themes and see how every story connects). Stories include field notes from real deployment. |

### Progress and Tracking
| Command | What It Does |
|---|---|
| `progress` | Score trends with inflection point narration (not just numbers), self-assessment calibration (are you an over-rater or under-rater?), storybank health, outcome correlation (which dimensions predict your real-interview results), graduation criteria check, and coaching meta-check every 3rd session. |

### Post-Interview and Offers
| Command | What It Does |
|---|---|
| `thankyou` | Post-interview thank-you notes — within 24 hours of an interview. Personalized with a specific callback from the conversation. Separate drafts for multiple interviewers. Advancing and rejected variants. |
| `negotiate` | Post-offer negotiation coaching. Offer analysis (market position, equity evaluation), non-obvious career value pathways (8 dimensions beyond comp, with 15% comp differential threshold), negotiation strategy, priority ordering, exact scripts with fallback language. |
| `reflect` | Post-search retrospective — journey arc, breakthroughs, pattern recognition, transferable lessons, archived coaching state. |

### Meta
| Command | What It Does |
|---|---|
| `help` | This command guide. Context-aware: shows recommended next commands based on where you are in your search and coaching journey. |

---

## Where You Are Now
[Brief coaching state summary — track, seniority, drill stage, story count, real interviews logged, active pipeline loops — or "No coaching state found. Run `kickoff` to get started."]

## Recommended Next
Based on where you are:
1. **[command]** — [why this is the highest-leverage move right now]
2. **[command]** — [secondary recommendation]

---

## Tips
- Share a real resume during `kickoff` — it powers resume analysis, story seeds, and concerns downstream
- Add contacts before you're in Screening — referrals need lead time; `outreach` is the tool
- Run `comp` before any recruiter screen where comp is likely to come up — you can't undo a low anchor
- Use `debrief` the same day as a real interview — signals fade fast
- Run `review` weekly and `progress` monthly — they measure different things (search health vs. coaching quality)
- After real interviews, log outcomes — the system correlates practice scores with real results
- Run `fit` before committing prep time to a role you're unsure about
- Set your feedback directness level (1-5) during `kickoff` — the diagnosis stays the same at every level, only the delivery changes
- Everything saves automatically to `coaching_state.md` and `state/pipeline.md` — pick up where you left off

What would you like to work on?
```
