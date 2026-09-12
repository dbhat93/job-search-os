## Writing Quality Gate (v4)

Every piece of externally-facing content the system produces must pass this gate before being shown to the candidate. The goal: sound like the candidate wrote it on a good day. Not AI. Not generic PM. Their actual voice. Borrowed from conorbronsdon/avoid-ai-writing (AI-ism detection) and adapted for job search.

**Applies to**: `outreach`, `thankyou`, `pitch`, `resume`, `linkedin`, `negotiate` (written drafts), cover letter drafting, blog/Medium drafts.

**Two modes:**
- **Auto-clean (default)**: Silently strip AI-isms and enforce voice rules before showing output. The candidate never sees the bad version.
- **Flag mode**: For longer pieces (blog posts, Medium articles, detailed cover letters), surface patterns without rewriting so the candidate can decide what stays. Trigger flag mode when the content is >300 words.

---

### Tier 1: AI-ism Detection (adapted from avoid-ai-writing)

**Tier 1 words (always kill on sight):**
delve, leverage, robust, seamless, watershed, spearhead, synergy, passionate, game-changer, thought leader, self-starter, team player, driven professional, utilize, facilitate, endeavor, cutting-edge, groundbreaking, paradigm shift, holistic, transformative, elevate, empower, harness, navigate (when used metaphorically), deep dive (as noun), double down, move the needle, at the end of the day, it goes without saying, in today's rapidly changing

**Tier 2 words (flag when 2+ appear in same paragraph):**
motivated, eager, enthusiastic, excited to apply, thrilled, honored, humbled, privileged, grateful for the opportunity, dynamic, innovative, impactful, strategic, proactive, cross-functional (when used as filler, not as genuine descriptor), stakeholder alignment, best practices, core competencies

**Tier 3 words (flag at high density only -- 3+ in a single document):**
significant, effective, efficient, unique, comprehensive, extensive, diverse, committed, dedicated

**Replacement approach**: Don't just delete flagged words. Replace with specific, concrete language. "I'm passionate about fraud prevention" becomes "I've spent 5 years building fraud systems." "Leveraging AI" becomes "using AI to automate." The replacement should always be more specific than the original.

---

### Severity Classification

**P0 (credibility killers -- fix before showing anything):**
- Cutoff disclaimers ("As an AI, I don't have access to...")
- Chatbot artifacts ("Sure!", "Great question!", "I'd be happy to help!")
- Vague attributions ("studies show," "research indicates," "experts agree") without naming the source
- Generic objectives ("seeking a challenging role where I can make an impact")
- Cookie-cutter openers ("When I learned about your company...")

**P1 (obvious AI smell -- fix in auto-clean):**
- Tier 1 word violations
- Template phrases ("I bring a unique blend of...")
- Synonym cycling (using 5 different words for "good" in 3 paragraphs)
- Formulaic openings/closings
- Hedging after stating an opinion ("This could potentially perhaps be...")

**P2 (stylistic polish -- fix in auto-clean, flag in flag mode):**
- Generic conclusions
- Uniform paragraph length (all paragraphs same size = AI fingerprint)
- Excessive transition phrases ("Furthermore," "Moreover," "Additionally")
- Passive voice when active is clearer
- Corporate jargon without explanation

---

### Voice Enforcement

If the candidate has a `voice-and-style.md` file (check for it at the project root or in the candidate's coaching directory), read it and enforce as a scoring rubric. If no voice file exists, apply the generic rules below.

**When voice file exists, check:**
- Sentence rhythm matches the candidate's pattern (their file will specify)
- Thesis placement matches their style (early? buried? varies by context?)
- Humor matches their register (parenthetical? dry? absent?)
- Formatting matches their preferences (em dashes, bullet lists, headers)
- Ending style matches (punchy kicker? CTA? casual sign-off?)

**When no voice file exists, apply these defaults:**
- Vary sentence length (short-long-short is more natural than uniform)
- Lead with the point, not the preamble
- Use active voice
- One idea per paragraph
- No filler openers ("I hope this finds you well")
- Under 150 words for outreach and thank-you notes

---

### Context Tolerance Matrix

Different contexts demand different strictness:

| Context | Tier 1 | Tier 2 | P0 | Formality | Max Length |
|---------|--------|--------|-----|-----------|-----------|
| Cold outreach / LinkedIn DM | Strict | Strict | Strict | Low-medium | 300 chars (LI) / 150 words (email) |
| Cover letter | Strict | Strict | Strict | Medium | 400 words |
| Thank-you note | Strict | Moderate | Strict | Medium | 120 words |
| Recruiter email | Strict | Moderate | Strict | Medium | 200 words |
| LinkedIn profile copy | Moderate | Moderate | Strict | Medium | Per-section limits |
| Resume bullets | Strict | Moderate | Strict | High | Per-bullet |
| Blog / Medium post | Moderate | Relaxed | Strict | Low (voice-driven) | No limit |
| Negotiation email | Strict | Strict | Strict | High | 300 words |

**Auto-detect context from signals**: hashtags or @mentions = social; "Dear" or salutation = email; bullet points with metrics = resume; >500 words with headers = blog. If ambiguous, default to cover letter strictness.

---

### Cross-Document Consistency Check

When the system has produced 3+ external documents for the same candidate (cover letters, outreach messages, LinkedIn posts), run a cross-document audit:

- **Fact consistency**: Are the same metrics cited the same way? (Don't say "100+ customers" in one letter and "65 customers" in another unless the context genuinely differs.)
- **Recycled phrases**: Flag verbatim phrases appearing in 2+ documents. Each piece should have unique language even if the story is the same.
- **Narrative alignment**: Does the career thread match across all documents? (Same as Narrative Consistency Checker but for written artifacts, not interview answers.)
- **Comp anchor consistency**: If comp expectations were stated in writing, are they consistent?

Surface cross-doc issues as: "Your cover letter to DoorDash says '100+ customers' but your outreach to Merge says '65 trial customers.' Reconcile to whichever is the more defensible claim."

---

### Second-Pass Audit

After generating any external-facing content, re-read it once more and check:
- Did any Tier 1 words survive the first pass?
- Did the rewrite introduce new AI patterns? (Common: replacing one AI-ism with another)
- Does the final version still sound like the candidate?
- Is it the right length for the context?

If issues found in second pass, fix silently in auto-clean mode. In flag mode, note: "Second-pass caught [issue]. Here's the fix."

---

### Enforcement Protocol

**For auto-clean mode (default):**
1. Generate the draft
2. Run Tier 1/2/3 scan + P0/P1 check + voice enforcement
3. Fix all issues silently
4. Run second-pass audit
5. Return clean copy to candidate

**For flag mode (>300 words or candidate requests):**
1. Generate the draft
2. Run full scan
3. Return draft with inline annotations: "[P1: 'leverage' -- consider 'use' or name the specific tool]"
4. Let candidate decide what to keep

**Integration**: Every command that produces external text must include this line in its output logic: "Before returning any externally-facing draft, run the Writing Quality Gate from `references/cross-cutting.md`."

**Commands that load this module**: `outreach`, `thankyou`, `pitch`, `resume`, `linkedin`, `negotiate` (written drafts), and any ad-hoc cover letter or blog draft request.

---

### Voice-File Character Policy (applies to ALL file writes)

If the candidate's `voice-and-style.md` prohibits specific characters (most commonly U+2014 or U+2013 dashes), that prohibition applies to EVERY file the coach writes on the candidate's behalf, not just externally-facing drafts. This includes:
- `coaching_state.md` writes (from any command)
- Output files in `job-search/`, `~/Desktop/`, or any path specified by the candidate
- PDF-source markdown (prep briefs, case brief drafts, cheat sheets)
- Any file the coach creates or edits via Write or Edit tools

**Why**: Templates and schema files in this skill may contain prohibited characters (U+2014, U+2013) for readability (they are NOT user-generated content). When Claude reads a template and writes content derived from it into a candidate's file, those characters would be copied verbatim. If the candidate's voice file prohibits them (or a hook enforces it), Claude must strip them during the write.

**Substitutions (in order of preference)**:
1. Restructure the sentence into two sentences
2. Replace with colon (`:`) if introducing a list, definition, or explanation
3. Replace with comma (`,`) if setting off a parenthetical clause
4. Replace with period (`.`) if separating two independent thoughts
5. Replace with parentheses `()` if setting off an aside

**Detection rule**: Before any Write or Edit tool call to a candidate file, scan the `content` or `new_string` parameter for U+2014 and U+2013 characters. If either is found and voice-and-style.md prohibits them, substitute before calling the tool.

**Error recovery**: If a hook blocks the write due to these characters, the coach sees the hook error, substitutes them, and retries. Do not announce this to the candidate unless the substitution meaningfully changes the content.

---
