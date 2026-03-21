# Version Roadmap

Each version has a clear thesis — not a feature grab bag.

---

## v1: Foundation (shipped)

**Thesis**: Build a broad, rigorous interview coaching system that adapts to each candidate.

- 16 commands covering the full interview lifecycle (kickoff through reflect)
- 5-dimension scoring rubric (Substance, Structure, Relevance, Credibility, Differentiation) with seniority calibration
- Root cause taxonomy mapping failures to targeted fixes
- Storybank management with STAR text, earned secrets, strength ratings, and rapid-retrieval drills
- Narrative identity extraction (2-3 core themes across stories)
- 8-stage drill progression with gating thresholds
- Full mock interviews in behavioral, system design, case study, panel, and technical+behavioral formats
- Role-fit assessment across 5 dimensions (requirement coverage, seniority alignment, domain relevance, competency overlap, trajectory coherence)
- Interview intelligence that learns from real experiences (question patterns, effective/ineffective patterns, company patterns)
- Persistent session state via `coaching_state.md` with mid-session saves
- Cross-cutting modules: differentiation, gap-handling, signal-reading, psychological readiness, cultural awareness
- Role-specific drills for PM, Engineering, Design, Data Science, Research, Operations, Marketing
- Technical format coaching boundaries (communication coaching, not domain evaluation)

---

## v2: Coaching Depth (shipped)

**Thesis**: The system is broad but shallow in places. Make it significantly better at its core job before expanding surface area.

### Feature 1: Transcript Format Support
Candidates no longer need to manually reformat transcripts. The system auto-detects and normalizes 8 transcript formats (Otter.ai, Grain, Google Meet, Zoom VTT, Granola, Microsoft Teams, Tactiq, Manual/generic) with disambiguation rules and quality signal reporting.

**Key files**: `references/transcript-formats.md` (new), `references/transcript-processing.md` (Step 0.5), `references/commands/analyze.md` (Step 3.5)

### Feature 2: Multi-Format Transcript Analysis
All transcripts were previously force-parsed as behavioral Q&A pairs. Now the system branches into 5 format-aware parsing paths: behavioral (Q&A pairs), panel (exchanges with cross-interviewer dynamics), system design (phase-based: scoping, approach, deep-dive, tradeoff, adaptation), technical+behavioral mix (segmented mode-switching), and case study (candidate-driven stages). Each format gets its own anti-patterns, additional scoring dimensions, and delta sheet sections.

**Key files**: `references/transcript-processing.md` (Step 2 overhaul, Step 2.5 extensions, Step 3 scoring, Step 4 delta), `references/commands/analyze.md` (format-aware dispatch/scoring/triage), `references/examples.md` (Example 11: system design analysis)

### Feature 3: Smarter Story Mapping
Story-to-question mapping was heuristic and question-by-question. Now uses a portfolio optimization engine with 4-level fit scoring (Strong Fit, Workable, Stretch, Gap), 7-step conflict resolution, freshness/overuse tracking, earned-secret-aware selection, and secondary skill utilization.

**Key files**: `references/story-mapping-engine.md` (new), `references/commands/prep.md` (storybank health gate, expanded output schema), `references/storybank-guide.md` (health metrics), `references/commands/stories.md` (enhanced gap analysis)

### Feature 4: Outcome Calibration Loop
The system detected miscalibration but didn't self-correct. Now includes scoring drift detection (do practice scores predict outcomes?), cross-dimension root cause tracking with unified treatment (one intervention per root cause, not per dimension), temporal decay for intelligence data, role-drill integration with core dimensions, success pattern capture, and structured unmeasured factor investigation.

**Key files**: `references/calibration-engine.md` (new), `references/commands/progress.md` (Steps 5a/5b/5c), `references/commands/analyze.md` (Step 12a), `references/commands/feedback.md` (calibration triggers), `references/commands/practice.md` (role-drill mapping), `references/rubrics-detailed.md` (root cause persistence)

### Feature 5: Enhanced Company Intelligence
Company research was unstructured. Now includes 3 depth levels (Quick Scan, Standard, Deep Dive), a structured 7-step search protocol, and a claim verification protocol with source tiers (verified, general knowledge, unknown).

**Key files**: `references/commands/research.md` (depth levels, search protocol, verification), `references/commands/prep.md` (structured research step)

---

## v3: Full Lifecycle (shipped)

**Thesis**: v2 made the coaching brain deep. v3 makes the system comprehensive — covering every surface where candidates interact with the job market, and tightening cross-command integration across all 23 commands.

v1 and v2 focused on the interview itself: prep, practice, scoring, and post-interview analysis. But candidates spend more time on resumes, LinkedIn profiles, outreach messages, JD analysis, presentations, and salary conversations than they do in actual interviews. v3 extends the coaching engine to every surface that affects job search outcomes.

### Feature 1: Application Materials Commands
Three new commands for the artifacts candidates build before they ever interview.

**`resume`** — Holistic resume optimization across 8 dimensions (ATS parsing, recruiter scan behavior, bullet quality, seniority calibration, keyword coverage, structure, concern management, cross-surface consistency). Three depth levels. When a storybank exists, the storybank-to-bullet pipeline mines earned secrets and quantified outcomes for resume bullets. When a JD is available, produces a targeted version optimized for that specific application.

**`linkedin`** — Platform-native LinkedIn optimization. Treats LinkedIn as its own game — recruiter boolean search mechanics, algorithm distribution, section-specific impact — not a resume copy. Three depth levels from quick audit to deep optimization with content strategy.

**`pitch`** — Core positioning statement: the atomic unit of self-presentation. Uses curiosity-gap hooks, earned-secret anchoring, and a Present-Past-Future formula to produce variants at every duration (10s elevator through 90s interview TMAY). Saved to coaching state and consumed by `resume`, `linkedin`, and `outreach` for cross-surface consistency.

**Key files**: `references/commands/resume.md` (new), `references/commands/linkedin.md` (new), `references/commands/pitch.md` (new)

### Feature 2: Networking and Outreach
**`outreach`** — Coaches the full networking lifecycle: cold LinkedIn messages, warm introductions, informational interview asks, recruiter replies, follow-up sequences, and referral requests. Three depth levels from quick templates to full multi-channel campaign strategy. Messages are built on the candidate's Positioning Statement so every outreach is differentiated. Includes platform mechanics (LinkedIn's 300-char connection request limit, optimal cold email length, InMail response rates).

**Key files**: `references/commands/outreach.md` (new)

### Feature 3: JD Analysis and Targeting
**`decode`** — Analyzes job descriptions using 6 decoding lenses (repetition frequency, order and emphasis, required vs. nice-to-have, verb choices, between-the-lines signals, what's missing) with confidence labels on every interpretation. Maps extracted competencies against the candidate's profile for a fit verdict. Batch triage mode compares 2-5 JDs to find the candidate's sweet spot. Includes a teaching layer so candidates learn to decode JDs themselves.

**Key files**: `references/commands/decode.md` (new)

### Feature 4: Presentation Round Coaching
**`present`** — Fills the prep gap for presentation-format interviews (system design presentations, business cases, portfolio reviews, strategy presentations, technical deep dives). Coaches narrative structure using 4 arc frameworks, calibrates content density against time limits, and prepares for Q&A with predicted questions and answer strategies. Three depth levels. Added corresponding presentation transcript parsing path and format-specific scoring dimensions (Content Density Management, Narrative Arc, Q&A Adaptability, Audience Calibration).

**Key files**: `references/commands/present.md` (new), `references/transcript-processing.md` (Path F), `references/rubrics-detailed.md` (presentation dimensions)

### Feature 5: Early-Process Comp Coaching
**`salary`** — Coaches the highest-leverage compensation moments that happen before an offer exists: the recruiter screen "what are your salary expectations?" question, salary history handling, and application form strategy. Guides candidates through comp research, range construction, and stage-specific scripts. Hands off to `negotiate` when a formal offer arrives.

**Key files**: `references/commands/salary.md` (new)

### Feature 6: Cross-Cutting Quality Pass
28 enhancements across all 23 commands, driven by a systematic audit:

- **Career transition detection** (5 types) in `kickoff` with mid-search profile update protocol
- **Anxiety-profile personalization** (5 profiles) in `hype` with format-specific warmup
- **Signal interpretation guide** (8 signals) in `debrief` with positioning performance check
- **Offer comparison normalization** (7 components) in `negotiate`
- **Diagnostic router** (9 problem-to-command mappings) in `help`
- **Staleness detection** (3 time thresholds) in `research`
- **Redo mechanism** and progression stage calibration in `mock`
- **Guided extraction prompts** for recruiter feedback in `feedback`
- **12 new cross-command integration points** wiring commands together (prep consumes decode output, concerns uses Outcome Log, questions uses intelligence data, stories consumes narrative identity, etc.)
- **3 new schema fields** (Anxiety profile, Career transition, Transition narrative status) with backward-compatible migration rules
- **Gap-Handling Module integration** into `practice`, `mock`, and `stories` — gap response patterns prescribed by storybank score
- **Differentiation in non-interview contexts** — earned secrets applied to resume bullets, LinkedIn sections, pitch hooks, and outreach messages
- **Presentation round scoring and parsing** — 4 format-specific scoring dimensions, transcript parsing path, and anti-pattern detection for presentation interviews
- **Level 5 Challenge Protocol** extended to all new commands + `mock`
- **Format Discovery deduplication** — discovered once in `prep`, saved to Interview Loops, reused by `mock`, `hype`, and `practice`
- **7 new worked examples** in `examples.md` calibrating output quality for decode, resume, pitch, linkedin, outreach, present, and salary

### Feature 7: Schema and Migration Hardening
4 schema migration gap fixes ensuring older `coaching_state.md` files fully upgrade:
- Missing `Known interview formats` Profile field
- Missing `Interview Intelligence` section in migration check
- `Signal` → `Hire Signal` column rename backward compatibility
- Interview Loops per-entry fields (Status, Round formats, Fit verdict, etc.)

**Key files**: `COACH.md` (schema migration rules), `references/commands/kickoff.md` (Interview Intelligence for new users)

---

## v3.1: Navigation, Gap Pipeline, and Security Hardening (shipped)

**Thesis**: v3 made the system comprehensive. v3.1 makes it safer to use at scale (security), easier to navigate (map command), smarter about competency gaps before interviews (gap pipeline), and more accurate in measuring coaching progress (velocity metrics).

### Feature 1: Map Command — Situational GPS
Candidates running multi-week searches with many commands and a growing coaching state frequently lose track of what to do next. `map` answers one question: "Given where I am right now, what should I run?" It reads the full coaching state, runs a 10-condition priority check (urgent through low), and outputs 1–3 time-sensitive actions with a filtered command reference for the candidate's current search phase. Read-only — never writes to state.

**Key files**: `references/commands/map.md` (new), `COACH.md` (registry, file routing, mode detection 9c)

### Feature 2: Storybank Gap Pipeline
Before this, competency gaps were detected in `prep` but there was no structured cross-interview analysis or severity triage. The gap pipeline adds: a Storybank Gap Check module with 3 severity tiers (Critical/Addressable/Covered), timeline-aware routing (3+ weeks / 1-3 weeks / <1 week before interview), and cross-loop analysis that surfaces when the same gap appears across multiple active companies. `prep` and `progress` both consume the module.

**Key files**: `references/cross-cutting.md` (Storybank Gap Check module), `references/commands/prep.md` (Step 7 enrichment), `references/commands/progress.md` (Storybank Health cross-loop analysis)

### Feature 3: Velocity Metric Fixes
Three QA-flagged issues in `progress` velocity metrics:
- **Calculation method**: Simplified from an ⌊N/3⌋ formula to first-2 vs last-2 session windows — easier to verify and less sensitive to session count
- **Stagnant threshold**: Tightened from `< +0.01/session` to `< +0.02/session for 4+ sessions` — the old threshold let slow-but-real progress go unflagged
- **Coaching ROI**: Replaced opaque formula with plain English + worked example ("8 sessions, +1.0 total → 4 sessions per half-point")

**Key files**: `references/commands/progress.md` (velocity metrics section)

### Feature 4: Security Hardening
Prompt injection guards, data privacy documentation, and data retention guidance:
- **Prompt injection**: Content isolation checks added to `analyze` (transcripts) and `prep` (JD parsing) — flags embedded directives before processing
- **Data privacy**: New Data Privacy and Retention section in `COACH.md` covering what `coaching_state.md` contains, compensation data sensitivity, third-party data, and retention guidance
- **Data retention**: Cleanup prompt added to `reflect` — surfaces what to archive vs. delete at end of search
- **Compensation privacy**: Warning added to `salary` — Comp Strategy section is among the most sensitive fields
- **Recruiter feedback provenance**: `feedback` now tracks written vs. paraphrased source — affects calibration confidence; stored as `[written]`/`[paraphrased]` tag in state entries
- **README privacy section**: New `## Data and Privacy` section documents what `coaching_state.md` contains and how to protect it — visible to forkers before first use

**Key files**: `references/commands/analyze.md`, `references/commands/prep.md`, `COACH.md`, `references/commands/reflect.md`, `references/commands/salary.md`, `references/commands/feedback.md`, `README.md`, `.gitignore`

---

## v3.2: Network Intelligence + Async Prep (shipped)

**Thesis**: v3.1 hardened the system. v3.2 makes it smarter about the candidate's actual network and closes the prep gap for async interview formats — the two highest-leverage gaps surfaced by real usage.

### Feature 1: LinkedIn Connections Integration
The `research` command's "networking angle" was generic — "who to talk to, what to ask" with no structured data source. Now, candidates can export their LinkedIn connections as a CSV, and `research` cross-references the target company against their real network. Output includes a connections table, role-appropriate outreach recommendations per contact, and fallback suggestions when no direct connections exist. Staleness detection flags exports older than 30 days.

**Key files**: `references/commands/research.md` (Networking Angle Protocol, updated Output Schema), `references/commands/help.md` (LinkedIn note in research description), `README.md` (Setup section with export instructions)

### Feature 2: Outreach Campaign Cadence Tracking
The `outreach` command coached individual messages well but was blind to multi-step campaigns. Now reads existing outreach logs from Interview Loop entries in `coaching_state.md` before drafting, surfaces contact history, recommends next actions based on follow-up cadence (first at +5 days, second at +10, then close), and flags diminishing returns when cold outreach at a company exceeds 3 unanswered contacts.

**Key files**: `references/commands/outreach.md` (Follow-Up Cadence Tracking section)

### Feature 3: Take-Home / Async Case Prep Protocol
The system handled live interviews well but had no structured guidance for async formats (take-home assignments, business case presentations, written submissions). New protocol in `prep` covers: prompt clarification, time-box strategy (20/30/35/15 split), evaluation criteria inference by role type, outline review, draft review, and live Q&A prep if the candidate presents after submission.

**Key files**: `references/commands/prep.md` (Take-Home / Async Case Prep Protocol)

### Feature 4: Command Registry Completion
`strategy` and `sync` existed as full commands but were not registered in README or `help` — users couldn't discover them. Now listed in both command tables.

**Key files**: `README.md` (command table), `references/commands/help.md` (Search Strategy section)

### v3.2.1: Hardening Pass (from eval audit)

**12 issues identified, all fixed:**

1. **Multi-CSV network support** — Networking Angle Protocol now reads ALL CSV sources under `## LinkedIn Connections` (candidate's network, referrer networks, curated intro targets). Results separated by source with appropriate trust/approval warnings.
2. **Canonical outreach log format** — Defined table schema (Date | Contact | Channel | Attempts | Status) with silent migration for prose/bullet formats. Added to COACH.md Schema Migration Check.
3. **Seniority-aware outreach recommendations** — Position titles now parsed for seniority signals (IC vs Director+ vs VP/C-suite). Different recommendation tiers per seniority level.
4. **Per-contact vs per-company cadence** — Cadence tracking now distinguishes between following up with one person 3x (per-contact limit) and contacting 3 different people (company-level pattern). Different thresholds and recommendations for each.
5. **Calendar days over business days** — Cadence timing simplified from "business days" (unreliable to compute) to "calendar days" as a pragmatic proxy.
6. **Open-ended deadline handling** — Async prep now handles "take as long as you need" cases: recommends self-imposed cap (4-6hr PM, 6-8hr strategy), explains diminishing returns, advises sleeping on multi-day drafts.
7. **Research → Outreach state handoff** — `research` now writes discovered connections to the Interview Loop entry, ensuring `outreach` can read them in a later session without re-running `research`.
8. **Graceful CSV failure** — If a CSV path doesn't resolve, logs a warning and continues with other sources instead of crashing the entire networking section.
9. **Per-source staleness checks** — Each CSV source gets its own staleness warning with source-appropriate advice (re-export for own; verify before intros for referrer's).
10. **Outreach log migration in COACH.md** — Schema Migration Check now includes outreach log format normalization.

**Test suite**: 29 eval test cases in `tests/v3.2-evals.md` (9 LinkedIn + 7 Outreach + 7 Async Prep + 3 Integration + 6 Regression). Mock fixtures in `tests/fixtures/`.

**Key files**: `references/commands/research.md`, `references/commands/outreach.md`, `references/commands/prep.md`, `COACH.md`, `tests/v3.2-evals.md`

### v3.2.2: Full Codebase Audit — Hardening Pass (no new features)

**16 fixes across product, security, usability, and functionality** (S3 excluded by design — names retained for outreach context):

**Product:**
1. **Challenge Protocol activation contradiction** — COACH.md said "Level 5 only" but challenge-protocol.md said "begins at Level 3." Aligned cross-cutting.md to "Levels 3-5 with graduated intensity."
2. **Story over-use detection** — Storybank now flags stories with Use Count > 5 for refresh during `stories improve`.
3. **Positioning drift detection** — Sync Drift Check now flags when 2+ of pitch/resume/linkedin haven't been refreshed in 5+ sessions.
4. **Rejection → Feedback loop** — Sync Drift Check now offers `feedback` after any Outcome Log rejection entry.

**Security:**
5. **External Text Validation Module** — Injection guard centralized in cross-cutting.md. All commands processing external text (debrief, feedback, outreach, stories) now reference the shared module instead of ad-hoc checks.
6. **Transcript retention guidance** — Archive/delete full transcripts 30 days after the relevant loop closes. Keep only extracted questions and scores.
7. **Comp data mitigation** — Data Privacy section now recommends OS-level disk encryption and notes Comp Strategy can be stored in a separate deletable file.

**Usability:**
8. **Session Start Protocol simplified** — Replaced 22-line nested conditional with flat 9-item priority list (first match wins). Deterministic execution across sessions.
9. **Soft Gate Protocol defined** — "Soft gate" now has a canonical definition: collect minimum context (target role, seniority, domain) via 2-3 questions, note that `kickoff` would provide richer context, then proceed.
10. **Coaching Notes categories** — Replaced vague "things a great coach would remember" with 4 explicit categories: format preferences, emotional/psychological patterns, communication quirks, scheduling/logistics.
11. **Fit confidence criteria** — Limited/Medium/High now have defined thresholds based on available data (no JD vs. JD vs. JD + outcomes + feedback).
12. **File Routing table marked as reference** — Clarified it's documentation, not runtime instructions. Each command file contains its own dependencies.

**Functionality:**
13. **Self-assessment calibration thresholds** — Defined: over-rater = self-scores avg 1.0+ above coach scores across 3+ interviews, under-rater = 1.0+ below, well-calibrated = within 0.5.
14. **Drill Progression stage gates** — Defined advancement criteria for all 8 stages (e.g., Stage 2 = one practice with all dimensions ≥3, Stage 3 = one mock with Lean Advance+).
15. **Cross-loop gap prioritization** — Gap Check now preps competencies critical for ANY active loop, prioritizing those critical for 2+ loops.
16. **Test fixture documentation** — Added schema note explaining that fixtures intentionally omit irrelevant sections; Schema Migration auto-adds them at runtime. Dedicated migration fixture (`mock-coaching-state-migration.md`) created for R.1 test with old "Signal" column format.

**Key files**: `COACH.md`, `references/cross-cutting.md`, `tests/v3.2-evals.md`, `tests/fixtures/mock-coaching-state-migration.md`, `tests/fixtures/mock-coaching-state-async.md`

### v3.2.3: Research Rigor for Business Cases

New cross-cutting module ensuring quantitative estimates in business case prep survive interviewer scrutiny.

**Key additions:**
1. **Research Rigor Module** in `references/cross-cutting.md` — confidence tagging (`[sourced]`/`[estimated]`/`[inferred]`), defensibility checks, competitive data freshness tracking, "how to present" coaching notes
2. **`prep` Step 3** — explicit call to Research Rigor Module during Take-Home/Async Case protocol
3. **`research` flag** — detects business case roles and flags Research Rigor for downstream `prep`

**Origin:** Real business case prep where market sizing had inflated percentages that wouldn't survive interviewer challenge (equipment rental at 40% card-addressable when 15-20% was honest).

**Key files**: `references/cross-cutting.md`, `references/commands/prep.md`, `references/commands/research.md`

---

## v4: Interaction Model (planned)

**Thesis**: Now that the coaching brain is strong and comprehensive, change *how* candidates interact with it.

### Voice Mode for Practice/Mock
Scoped tightly to `practice`, `mock`, and `hype` warmups. The candidate speaks, the system listens, scores delivery alongside content (filler words, pacing, confidence, hedging language). Doesn't replace text for `prep` or `progress` — those need structured output. But practice and mocks become dramatically more realistic with voice.

### Session Replay
After a mock or practice round, let the candidate replay the exchange with inline coaching annotations. "Right here you hedged for 8 seconds before getting to the point. Here's what a tighter version sounds like."

### Lightweight Companion UI
Not replacing Claude Code, but a read-only dashboard that visualizes `coaching_state.md`: score trends over time, storybank coverage heatmap, interview loop status, drill progression. Think of it as a `progress` command you can glance at without running anything. Could be a simple local web server that reads the markdown file.

### Calendar Awareness
Connect to Google Calendar / Outlook. When an interview is 24 hours out, auto-trigger `hype`. When it's a week out and no `prep` has been run, nudge. Time-aware coaching exists in v1 but requires the candidate to self-report timelines.

### Collaborative Storybank Building
A friend or mentor can review your storybank and leave comments. Still file-based, but with a lightweight review protocol. Most candidates build stories in isolation — a second pair of eyes catches blind spots the coach can't.

---

## v5: Platform (planned)

**Thesis**: The coaching engine is proven. Now make it accessible to people who'll never touch a CLI.

### Full Web App
Backend, auth, database replacing `coaching_state.md`, real UI for all commands. The skill files become the system prompt for an API-based product. The reference architecture is already modular enough to port — each command file maps to an API endpoint.

### Coaching Marketplace
Let experienced interviewers or career coaches customize the rubrics, add company-specific intelligence, and offer specialized coaching tracks (e.g., "FAANG PM prep" with insider-calibrated scoring). The cross-cutting module architecture already supports this — new modules slot in without rewriting commands.

### Team/Org Mode
Companies use this to prep internal candidates for promotion panels, or recruiting teams use it to train interviewers (flip the perspective — coach the person *giving* the interview). Same 5 dimensions, different lens.

### Anonymized Intelligence Network
With enough users, the system can surface patterns across candidates: "Candidates who get offers at Stripe tend to score 4+ on Differentiation. Candidates rejected at Amazon most often fail on Structure." No individual data shared — just aggregate signals that improve everyone's prep.

---

## Version Tension

v3 was the natural next step after v2 — it extended the coaching engine to every surface that matters in a job search without requiring any architectural changes. The system is now comprehensive: 23 commands covering resume through retrospective, with cross-command integration wiring that makes the whole greater than the parts.

v4 is exciting but expensive (voice, UI, integrations). v5 is a different company. The risk now is premature platforming before v3 has proven that full-lifecycle coaching moves candidate outcomes better than interview-only coaching.
