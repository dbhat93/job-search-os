# research — Company Research Workflow

A lightweight alternative to `prep` for when the candidate wants to understand a company before committing to a full prep cycle. Use when they're evaluating whether to apply, building a target list, or doing early-stage reconnaissance.

### When to Use Research vs. Prep

| Situation | Use |
|---|---|
| Evaluating whether to apply | `research` |
| Building a target company list | `research` (run multiple) |
| Have an interview scheduled | `prep` |
| Want to understand company culture before networking | `research` |
| Need predicted questions and story mapping | `prep` |

### Sequence

1. Ask for company name and the candidate's target role type (if not already in coaching state).
2. Research publicly available information. Follow the same Company Knowledge Sourcing tiers from `prep` — Tier 1 (verified), Tier 2 (general knowledge), Tier 3 (unknown/say so).
3. Assess fit against the candidate's profile (from `coaching_state.md` if available, or from what they've told you).
4. Output the research brief.

### Research Depth Levels

| Level | When to Use | What to Do | Time Investment |
|---|---|---|---|
| **Quick Scan** | Building a target list, evaluating 5+ companies at once | Company website + careers page + recent news. Enough for a basic fit assessment. | 5-10 min |
| **Standard** | Evaluating whether to apply. Default for `research`. | Full protocol: website, careers, news, Glassdoor, LinkedIn, blog. Produces a complete research brief. | 15-20 min |
| **Deep Dive** | High-priority target, interview scheduled, want maximum intelligence | Standard + employee posts/talks, product reviews, competitor analysis, leadership team profiles. | 30+ min |

Default to **Standard**. Suggest **Deep Dive** when:
- The candidate has an interview scheduled at this company
- The candidate explicitly asks for comprehensive intelligence
- The company is in the candidate's top 3 targets

### Search Tooling

Use **Exa** (`mcp__exa__web_search_exa`) as the default search engine for all research steps. Exa uses neural search — it finds semantically relevant content, not just keyword matches. This matters for job search research: "what does this company's product team actually think about AI" returns real blog posts and talks, not just press releases.

Use `mcp__exa__web_fetch_exa` when you have a specific URL (careers page, blog post, LinkedIn profile) and want cleaner content extraction than a browser read.

Fall back to generic WebSearch only if Exa returns no results or if the query is highly structured (e.g., exact job ID lookups).

**Exa query patterns that work well for this workflow:**
- Company culture/values: `"[Company] engineering culture" OR "[Company] product philosophy"` — finds employee-written posts, not just About pages
- Leadership intel: `"[Name] [Company]" site:linkedin.com OR medium.com OR substack.com` — surfaces thought leadership and public writing
- Interview intel: `"[Company] interview process [role]" Glassdoor OR Blind OR reddit` — finds crowd-sourced signal
- Recent news: `"[Company]" after:2025-01-01` — Exa respects date filters reliably

### Structured Search Protocol

Search for information in this order. Each step builds on the previous ones. Use Exa for all steps unless noted:

1. `[Company] careers` → careers page, open roles, stated values/principles, engineering/product blog links
2. `[Company] about` or `[Company] mission` → stage, funding, size, founding story
3. `[Company] news [current year]` → recent events (funding, layoffs, product launches, leadership changes). **Note**: Recent events change interview culture — a company that just laid off 20% is hiring differently than one that just raised Series C.
4. `[Company] interview process [role type]` → Glassdoor/Blind interview reviews (label as crowd-sourced, not verified)
5. `[Company] engineering blog` or `[Company] product blog` → culture signals, technical maturity, how they think about problems
6. `[Company] culture` → employee reviews, culture deck, values page, recent employee posts
7. (Deep Dive only) `[Company] [leader name]` → leadership profiles, talks, posts, published perspectives

### Claim Verification Protocol

Every company-specific claim in the research output must map to a source tier:

- **Tier 1 — Verified**: Information directly retrieved from the company's own website, careers page, blog, or from the job description/candidate-provided context. Cite the source.
- **Tier 2 — General knowledge**: Widely documented public information about well-known companies (e.g., Amazon's Leadership Principles, Google's Googleyness). Label clearly.
- **Tier 3 — Unknown**: Information that couldn't be verified. State this explicitly — don't guess.

**Rules:**
- When web search returns conflicting information, present both sides and note the conflict: "Source A says [X], but Source B says [Y]. Worth verifying directly."
- When information is dated (>12 months), flag it: "This is from [date] — verify it's still current. Companies change."
- Never synthesize multiple uncertain sources into a confident claim. If 3 Glassdoor reviews each say something slightly different, present the range, not a false consensus.

### What to Research

Pull from publicly available sources only:
- **Company careers page**: Open roles, values, culture signals, engineering/product/design blog
- **Company "About" page**: Mission, stage, funding, size
- **Recent news**: Funding rounds, product launches, leadership changes, layoffs
- **Glassdoor/Blind signals**: Interview process info, culture reviews (label as crowd-sourced, not verified)
- **LinkedIn company page**: Growth trajectory, team composition

### Fit Assessment

Use the Role-Fit Assessment Module from `references/cross-cutting.md`. Without a JD, you can assess 3 of 5 dimensions:

1. **Seniority Alignment** — Does the candidate's experience level match what this company typically hires for this type of role? Use public signals (job postings, team composition on LinkedIn, company stage).
2. **Domain Relevance** — How transferable is the candidate's industry/domain experience? A fintech PM applying to a healthtech startup has a domain gap. Name it, assess how bridgeable it is.
3. **Trajectory Coherence** — Does this role make sense as the next step in their career? A lateral move to a smaller company for more scope is coherent. A step down in title with no clear rationale raises questions.

**Cannot assess without JD**: Requirement Coverage, Competency Overlap. Flag this: "For a full fit assessment, I'd need the job description."

**Verdict**: Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit — with the specific dimension scores driving the verdict.

**If Weak Fit or Long-Shot Stretch**: Follow the Alternative Suggestions Protocol — name the gaps, suggest what a better-fit version looks like, and respect the candidate's decision if they want to proceed.

### Research Rigor Flag

If this role involves market sizing, competitive analysis, or business case interviews (e.g., strategy PM roles, platform PM roles, operations roles at early-stage companies):
- **Flag for later**: When `prep` runs for this company, the **Research Rigor Module** from `references/cross-cutting.md` will apply to all quantitative estimates
- **Start early**: If market estimates surface during research, tag each figure as `[sourced]`, `[estimated]`, or `[inferred]` — this saves time when `prep` builds the full brief
- **Cross-reference**: If two sources disagree on a number, note both — the candidate will need to reconcile before presenting

### Networking Angle Protocol

If the candidate's LinkedIn connections are referenced in `coaching_state.md` (under `## LinkedIn Connections`):

**Step 1: Identify all network sources.** Read every subsection under `## LinkedIn Connections`. Each subsection may contain a separate CSV with its own path, export date, and signal notes. Common patterns:
- `### Candidate's Network` — the candidate's own 1st-degree connections (high signal)
- `### [Name]'s Network (shared with consent)` — a referrer's or ally's connections (second-degree, lower signal — always requires the referrer's approval before requesting intros)
- `### High-Value Intro Targets` — manually curated names (highest signal, already vetted)

**Step 2: Cross-reference ALL sources against the target company.**
For each CSV:
1. Read the CSV file at the specified path. If the file is not found, log a warning ("CSV not found at [path] — skipping") and continue with other sources. Do not crash.
2. Cross-reference the "Company" column against the target company name. Match case-insensitively, trim whitespace, and handle common variants (e.g., "Stripe" matches "Stripe", "Stripe, Inc.", "Stripe Inc", " Stripe ").
3. For each match, extract: First Name, Last Name, Position, Connected On.

Also check the `### High-Value Intro Targets` section for manually listed connections at the target company — these take priority over CSV matches.

**Step 3: Output a structured networking section** in the research brief (see Output Schema). Separate results by network source:
- **Your connections** (1st-degree) — can reach out directly
- **[Referrer]'s connections** (2nd-degree) — requires referrer approval before requesting intro. Always note: "Ask [Referrer] if they know [Name] well enough to intro."
- **Curated intro targets** — already vetted, highest priority

**Categorize matches:**
- **Direct**: Currently employed at the target company (based on CSV "Company" column).
- **Note**: LinkedIn CSVs only contain current employer. Alumni (people who previously worked there) won't appear — flag this limitation and suggest the candidate search LinkedIn manually for former employees.

**Suggested moves per connection — seniority-aware:**
- Tailor the outreach recommendation to BOTH the connection's role AND seniority level:
  - Engineering/technical (IC) → "Ask about team culture, eng-PM dynamics, technical bar — not for a referral directly"
  - Engineering/technical (Director+) → "High-value executive contact — save for when you have a specific role. Ask about org priorities and team direction, not for a referral."
  - Recruiting/talent → "Direct referral path — ask about open roles and process"
  - PM/product (IC) → "Peer intel — ask about PM scope, team structure, interview process"
  - PM/product (Director+) → "Potential hiring manager — approach with a specific role in mind. Lead with what you'd bring, not what you need."
  - Leadership/executive (VP+, C-suite) → "Highest-cost ask in the network. Do NOT cold-approach. Only via warm intro with a specific, well-researched ask."
  - Other functions (IC) → "Cross-functional intel — ask about company culture, growth trajectory, what they'd change"
  - Other functions (Director+) → "Cross-functional leader — can provide org-level context. Save for targeted questions about company direction."
- **Seniority detection heuristic**: Look for title keywords — "Senior", "Staff", "Principal", "Lead" = senior IC; "Director", "Head of", "VP", "SVP", "Chief", "C-suite" = leadership; everything else = mid-level IC.

**If no matches found across ALL sources:** Don't leave the section empty. Suggest: "No connections at [Company] in any of your network exports. Try: (1) search LinkedIn for 2nd-degree connections, (2) check if any of your connections previously worked there, (3) look for shared communities (alumni networks, Slack groups, industry events)."

**If no CSV paths exist in coaching_state.md:** Skip the networking section silently — don't nag about missing data. Fall back to the generic networking angle line in the output schema.

**Staleness check (per source):** If any source's `Last exported` date is >30 days old, add a note per source: "[Source name] export is [N] days old — data may be stale. [If candidate's own: consider re-exporting (Settings → Data Privacy → Get a copy of your data → Connections).] [If referrer's: verify titles/companies before requesting intros.]"

**State handoff to `outreach`:** After outputting the networking section, write discovered connections to the target company's Interview Loop entry in `coaching_state.md` under a `- Networking leads (from research):` field. This ensures `outreach` can read them deterministically in a later session without re-running `research`.

### Output Schema

```markdown
## Company Research: [Company]

## Company Snapshot
- Stage: [startup / growth / public / enterprise]
- Size: [approximate employee count if available]
- Industry: [primary domain]
- Recent signals: [funding, launches, layoffs, leadership changes — anything relevant]
- Sources: [list what you actually looked at]

## Culture Signals
- Public values/principles: [with source]
- What they seem to optimize for: [with source]
- Red flags or concerns: [if any]
- What I couldn't find: [explicitly list gaps]
- Confidence: High / Medium / Low

## Fit Assessment (vs. your profile)
- Verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- Seniority Alignment: [Strong / Moderate / Weak] — [brief evidence]
- Domain Relevance: [Strong / Moderate / Weak] — [brief evidence]
- Trajectory Coherence: [Strong / Moderate / Weak] — [brief evidence]
- Cannot assess without JD: Requirement Coverage, Competency Overlap
- Key gaps (if stretch/weak): [specific gaps, not vague]
- Better-fit alternatives (if weak/long-shot): [what roles would be stronger matches and why]

## If You Decide to Apply
- Recommended next steps:
- Key things to research further before interviewing:

## Networking Angle

### Your connections at [Company] (1st-degree)
| Name | Position | Seniority | Connected | Suggested move |
|------|----------|-----------|-----------|----------------|
| [matches from candidate's CSV] |

### [Referrer]'s connections at [Company] (2nd-degree — requires [Referrer] approval)
| Name | Position | Seniority | Suggested move |
|------|----------|-----------|----------------|
| [matches from referrer's CSV] |
- ⚠️ Ask [Referrer]: "Do you know [Name] well enough to intro me?"

### Curated intro targets (if any in coaching_state.md)
- [Names from High-Value Intro Targets section, with context]

### No connections found? (if no matches across all sources)
- [Manual search suggestions: 2nd-degree connections, alumni, shared communities]

**Recommended next**: `prep [company]` — build a full prep brief now that you have the research foundation. **Alternatives**: `research [another company]`, `stories`
```

### Staleness Detection

When `research` is run for a company that already has a research entry in coaching_state.md, check the date:
- **< 2 weeks old**: "I researched [Company] on [date]. Want me to refresh, or is that still current?"
- **2-8 weeks old**: "My research on [Company] is [N] weeks old. Companies change — want a refresh? I'll focus on what's new since [date]."
- **> 8 weeks old**: Auto-refresh. "My research on [Company] is [N] weeks old — that's stale. Let me update it." Run the full research protocol again, noting what changed vs. the previous entry.

When refreshing, preserve the previous fit verdict and explicitly compare: "Last time I assessed this as an Investable Stretch. Based on [new information], that's now [verdict] because [reason]."

### Coaching State Integration

After research, save a lightweight entry to `coaching_state.md` Interview Loops:
```
### [Company Name]
- Status: Researched (not yet applied)
- Fit verdict: [Strong / Investable Stretch / Long-Shot Stretch / Weak]
- Fit confidence: [Limited — no JD]
- Fit signals: [1-2 lines on what drove the verdict]
- Structural gaps: [gaps that can't be bridged with narrative, if any]
- Date researched: [date]
```

This way, if the candidate later runs `prep` for this company, the coach already has context.
