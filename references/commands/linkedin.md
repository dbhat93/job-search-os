# linkedin — LinkedIn Profile Optimization

> Before returning any LinkedIn content (messages, profile copy, section rewrites), run the **Writing Quality Gate** from `references/cross-cutting.md`. For messages: auto-clean mode, strict context (300 chars for connection requests, 150 words for InMails). For profile copy: auto-clean mode, moderate context (no word limit but no Tier 1 words, no AI-isms, must sound like the candidate). Enforce voice file if it exists.

Optimize the candidate's LinkedIn profile as a search-discoverable, credibility-building, job-landing surface. LinkedIn is its own platform with its own rules — not a resume mirror. The profile needs to be optimized for how LinkedIn actually works: recruiter boolean search, algorithm distribution, section-specific mechanics, and content strategy.

Also read `references/differentiation.md` (for earned secret integration into profile) and `references/storybank-guide.md` (for storybank data to feed into About/Experience rewrites).

---

## How LinkedIn Actually Works

**Recruiter Search**: LinkedIn Recruiter uses boolean search across profile fields. Headline has the highest keyword weight, followed by current title, skills, experience descriptions, and about. Recruiter Lite matches on title + headline + skills. Full Recruiter also searches experience descriptions and about. Skills are filterable (checkbox filters in Recruiter search). Open to Work increases visibility in recruiter results.

**Algorithm (for content/engagement)**: Posts go through 3-phase distribution: quality filter → test audience → broader network. Comments are ~15x more valuable than likes for reach. PDF carousels get 3-6x engagement vs text. External links reduce reach ~60%. Engagement in first 60-90 min determines distribution.

**Section Impact Ranking** (for recruiter discovery + profile visits):
1. Headline (highest search weight, first thing seen)
2. Current title (second-highest search weight)
3. Skills (filterable in recruiter search — the only filterable field)
4. Experience descriptions (searched in full Recruiter)
5. About section (searched, but lower weight)
6. Photo + banner (affects click-through rate from search results)
7. Open to Work signal (increases recruiter visibility)
8. Featured section (credibility when they visit your profile)
9. Recommendations (social proof, low search weight)
10. Custom URL + completeness signals

---

## Priority Check

Before running the full audit, check coaching state:
- If no `kickoff` has been run: "I can audit your LinkedIn profile, but without your target role context I'll be giving generic advice instead of optimizing for how recruiters in your target space actually search. Want to run `kickoff` first so I can target the audit, or proceed with a general review?"
- If the candidate has an interview within 48 hours: "You have an interview in [X] hours. LinkedIn optimization can wait — let's focus on `hype` / `prep` first. Come back to this after."

---

## Required Inputs

- LinkedIn profile URL or full profile text (pasted sections)
- Target role context (from coaching_state.md Profile, or ask)

## Optional Inputs

- Depth level: Quick Audit / Standard / Deep Optimization (default: Standard)
- Specific sections to focus on (e.g., "just headline and about")

---

## Depth Levels

| Level | When to Use | What It Covers |
|---|---|---|
| **Quick Audit** | Fast check, building a target list, or just wants the biggest wins | Headline + title + skills + about. Top 3 fixes only. |
| **Standard** | Default. Full profile review. | All 9 sections. Section-by-section audit + content strategy overview. |
| **Deep Optimization** | High-priority job search, major profile overhaul | All 9 sections + detailed content strategy + positioning consistency check (resume vs. LinkedIn vs. interview narrative) + Challenge Protocol (Levels 3–5). |

---

## Logic / Sequence

### Step 1: Profile Intake

Ask for LinkedIn profile URL or pasted text. If URL provided, ask candidate to paste the relevant sections (the coach can't browse LinkedIn). Accept whatever format they provide — be flexible.

### Step 2: Context Assembly

Pull from coaching_state.md:
- Target role(s) and seniority band
- Resume Analysis (positioning strengths, concerns, story seeds)
- Storybank (for earned secrets that should surface in About/Experience)
- Active Coaching Strategy (bottleneck — if Differentiation is the gap, emphasize that in LinkedIn too)
- Positioning Statement (if exists — use as consistency reference for headline and about rewrite; the LinkedIn Summary Hook variant should align with the Core Statement)
- **JD Analyses** (if `decode` was run for target companies): top competencies become priority keywords for headline, skills, and experience descriptions. Cross-reference the top 3-5 competencies from each active JD Analysis against current LinkedIn keywords — flag missing keywords and recommend placement by section impact ranking.

### Step 3: Section-by-Section Audit (9 sections)

For each section, evaluate against its specific purpose:

**1. Headline** (search + first impression)
- Does it contain keywords recruiters search for in the target role?
- Is it specific enough to differentiate (not "Passionate Leader" — concrete skills/domain)?
- Does it signal seniority appropriately?
- Character limit: 220 chars. Every word must earn its place.
- If Positioning Statement exists: cross-reference. The headline should echo the positioning's key differentiator. Flag misalignment.
- Provide a rewritten headline with rationale.

**2. Current Title + Company** (search weight)
- Does the title match what recruiters search for?
- If current title is non-standard ("Ninja", "Rockstar"), suggest the searchable equivalent.
- Note: Can't change company-assigned title, but can adjust in headline.

**3. Skills Section** (filterable search)
- Are the right skills listed? (Skills are the ONLY filterable field in recruiter search.)
- Are the top 3 pinned skills aligned with target role?
- Are skills ordered by relevance to target, not alphabetically?
- If JD Analyses exist: cross-reference top competencies against current skills list. Flag any high-frequency competency not listed as a skill — these are highest-priority additions.
- Provide a recommended skill list (top 10) with ordering rationale.

**4. About Section** (search + credibility + differentiation)
- First 3 lines visible before "see more" — do they hook?
- Does it contain target keywords naturally (not keyword-stuffed)?
- Does it tell a narrative, or is it a bullet list of skills? (Narrative wins.)
- Does it surface earned secrets or a spiky POV from the storybank?
- Is there a clear "what I do + what makes me different + what I'm looking for" structure?
- If Positioning Statement exists: the About opening (above-fold) should align with the LinkedIn Summary Hook variant. Flag misalignment and provide aligned rewrite.
- Provide a rewritten About with rationale.

**5. Experience Descriptions** (search + depth)
- Are descriptions accomplishment-oriented (not responsibility-oriented)?
- Do they contain searchable keywords?
- Do they quantify impact where possible?
- Are the most recent 2-3 roles fully fleshed out? (Older roles can be brief.)
- For the most recent role: provide a rewritten description.

**6. Photo + Banner** (click-through rate)
- Photo: Professional, approachable, recent? (Can't see it, but provide guidance.)
- Banner: Custom or default? Custom banners with a value prop or domain signal increase profile visit conversions.
- Provide guidance on what a strong banner communicates.

**7. Featured Section** (credibility when they visit)
- Is it being used? Most candidates leave it empty.
- What should go here: published work, key projects, media mentions, portfolio pieces, talks.
- Provide 2-3 specific recommendations based on their resume/storybank.

**8. Recommendations** (social proof)
- How many? (3+ is baseline credibility.)
- Are they from relevant people (managers, cross-functional partners, clients)?
- Provide guidance on who to ask and how to make the ask.

**9. URL + Completeness** (signals)
- Custom URL set?
- Profile completeness: all sections filled, education, certifications, volunteer?
- Open to Work: on or off? When to use each setting.

### Step 4: Positioning Consistency Check (Deep Optimization only)

Cross-reference LinkedIn profile against:
- Resume (from Resume Optimization): Are the same positioning strengths leading? Are titles/descriptions consistent? Inconsistencies create doubt.
- Interview narrative (from storybank + coaching strategy): Does the LinkedIn profile tell the same story the candidate tells in interviews?
- Positioning Statement (from pitch, if run): Does headline echo the Core Statement? Does About echo the LinkedIn Summary Hook variant?
- Flag gaps: "Your resume leads with [X] but your LinkedIn leads with [Y]. A recruiter who reads both will notice."

### Step 5: Content Strategy Overview (Standard + Deep)

Not just the profile — how to use LinkedIn as a platform.

**Timeline-aware content strategy**: If Profile has an interview timeline, calibrate the content recommendation:
- **≤2 weeks to interviews**: Skip content strategy entirely. Focus on profile optimization only. The candidate doesn't have time to build a content presence.
- **2-6 weeks**: Light content — 1 post/week max, focused on credibility-building (sharing an insight from their domain). Don't invest heavily in content creation during active interviewing.
- **6+ weeks or early-stage search**: Full content strategy below. This is where building visibility compounds.

- **Posting cadence**: 2-3 posts/week during active search (if timeline allows). Consistency > volume.
- **Content types that work**: Industry takes with personal angle, "here's what I learned" posts from real experience, PDF carousels with frameworks, commentary on industry news.
- **Content types that don't work**: "Excited to announce" posts (low engagement), reposting without commentary, posting external links (kills reach).
- **Engagement strategy**: Comment thoughtfully on posts by people at target companies and in target roles. This is higher-leverage than posting for getting noticed.
- **What NOT to post**: Anything that signals desperation ("Looking for my next opportunity! Please help!"), anything controversial that could screen you out, anything that contradicts your positioning.

Provide 3 specific post ideas based on their storybank and earned secrets.

### Step 6: Challenge Protocol (Deep Optimization only — see `references/challenge-protocol.md` → LinkedIn Profile Challenge invocation)

Run graduated Challenge Protocol against the LinkedIn profile. Level 3 = Assumption Audit (one sentence). Level 4 = Assumption Audit + Blind Spot Scan. Level 5 = Lenses 1, 2, 4, 5 (Pre-Mortem excluded — static artifact). Timing: after full audit, before Priority Moves.

---

## Output Schema — Quick Audit

```markdown
## LinkedIn Quick Audit

## Top 3 Fixes (in priority order)
1. **[Section]**: [What's wrong] → [Specific fix with rewrite]
2. **[Section]**: [What's wrong] → [Specific fix with rewrite]
3. **[Section]**: [What's wrong] → [Specific fix with rewrite]

## Quick Wins
- [1-2 things that take <5 minutes and improve discoverability]

**Recommended next**: `linkedin` (Standard) — get the full audit. **Alternatives**: `stories`, `prep [company]`
```

## Output Schema — Standard

```markdown
## LinkedIn Profile Audit: [Name]

## Profile Score
- Recruiter discoverability: [Strong / Moderate / Weak] — [1-line evidence]
- Credibility on visit: [Strong / Moderate / Weak] — [1-line evidence]
- Differentiation: [Strong / Moderate / Weak] — [1-line evidence]
- Overall: [Strong / Needs Work / Weak]

## Section-by-Section

### Headline
- Current: [quoted]
- Assessment: [what works, what doesn't, search implications]
- Recommended: [rewritten headline]
- Why: [rationale — keyword targeting, differentiation, seniority signal]

### About
- Assessment: [hook strength, keyword presence, narrative vs. list, differentiation]
- Recommended: [full rewritten About section]
- Why: [rationale]

### Skills
- Assessment: [alignment with target role, top 3 pinned, missing keywords]
- Recommended top 10: [ordered list with rationale]

### Experience (most recent role)
- Assessment: [accomplishment vs. responsibility oriented, keywords, quantification]
- Recommended rewrite: [rewritten description]

### [Other sections — briefer assessments + specific fixes]

## Content Strategy Overview
- Posting approach: [2-3 sentences]
- 3 post ideas based on your background:
  1. [specific idea with hook]
  2. [specific idea with hook]
  3. [specific idea with hook]

## Priority Moves (ordered)
1. [highest-impact fix — do this first]
2. [second-highest]
3. [third]

**Recommended next**: `stories` — make sure your storybank feeds your LinkedIn narrative. **Alternatives**: `prep [company]`, `linkedin` (Deep Optimization)
```

## Output Schema — Deep Optimization

```markdown
## LinkedIn Deep Optimization: [Name]

## Profile Score
[same as Standard]

## Section-by-Section
[same as Standard, but all 9 sections get full treatment — not just headline/about/skills/experience]

## Positioning Consistency
- Resume ↔ LinkedIn: [aligned / gaps — specific gaps listed]
- Positioning Statement ↔ LinkedIn headline/about: [aligned / gaps — specific fix if misaligned]
- Interview narrative ↔ LinkedIn: [aligned / gaps — specific gaps listed]
- Inconsistencies to resolve: [specific items with rewrite for each]

## Content Strategy
[same as Standard, but expanded]
- Engagement targets: [specific people/companies to engage with based on target roles]
- Content calendar: [week 1-4 suggested cadence]

## Challenge (Levels 3–5 — see references/challenge-protocol.md → LinkedIn Profile Challenge)
[Level 3: Assumption Audit — one sentence]
[Level 4: Assumption Audit + Blind Spot Scan]
[Level 5: Lenses 1, 2, 4, 5 — Assumption / Blind Spot / Devil's Advocate / Strengthening Path]

## Priority Moves (ordered)
1. [highest-impact fix]
2. [second]
3. [third]
4. [fourth]
5. [fifth]

**Recommended next**: `stories` — earned secrets from your storybank should surface in your About and Experience. **Alternatives**: `prep [company]`, `practice`
```

---

## Coaching State Integration

After running `linkedin`, save to coaching_state.md:

```markdown
## LinkedIn Analysis
- Date: [date]
- Depth: [Quick Audit / Standard / Deep Optimization]
- Overall: [Strong / Needs Work / Weak]
- Recruiter discoverability: [Strong / Moderate / Weak]
- Credibility on visit: [Strong / Moderate / Weak]
- Differentiation: [Strong / Moderate / Weak]
- Top fixes pending: [1-3 line items]
- Positioning gaps: [resume ↔ LinkedIn inconsistencies, if assessed]
```
