# draft — Email Drafting

**Job:** *Anything email-shaped — follow-ups, outreach, recruiter replies. Context-driven by what you pass it.*

> **Boundary with `thankyou`**: Use `thankyou` for post-interview thank-you notes — it's optimized for timing guidance, multi-interviewer handling, and advancing vs. rejected variants. Use `draft` for everything else: follow-ups outside the thank-you window, cold/warm outreach, recruiter communication, offer declinations. When in doubt: if it's within 24 hours of an interview and the primary purpose is advancing, use `thankyou`.

---

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `draft [company]` | Follow-up after an interaction — reads pipeline + debrief/coaching state |
| `draft [contact]` | Outreach to a specific person — reads contact record from `state/contacts.md` |
| `draft recruiter` | Recruiter communication — scheduling, status requests, responses |
| `draft review [company]` | Feedback-solicitation email after a loop closes (especially rejections) |
| `draft` (bare) | Ask what kind of draft is needed before proceeding |

**Default (bare `draft`):** Ask one question: "What kind of email do you need? (follow-up after an interview, cold outreach, recruiter reply, feedback request after rejection, other)"

---

## State Files

Read from:
- `coaching_state.md` — storybank, debrief data, interview loop detail, earned secrets
- `state/pipeline.md` — stage, last activity, next action for the relevant company
- `state/contacts.md` — contact record including pronouns, relationship, last touch (**dependency**: this file does not exist until `outreach` or `pipeline add` creates it; if missing, ask for contact details inline)

If a state file doesn't exist, note the gap explicitly and ask for the missing context rather than drafting with assumptions.

---

## `draft [company]` — Post-Interview Follow-Up

### Logic

1. Read the company's entry in `state/pipeline.md` — current stage, last activity.
2. Read the relevant Interview Loop in `coaching_state.md` — which round, what was discussed, debrief data if captured.
3. Identify the specific moment that should anchor the draft: the question they asked, the example that landed, the exchange that mattered. If this isn't in the state, ask before drafting: "What was one specific moment from the conversation I should anchor the draft to?"
4. Check debrief for interviewer name and any signals captured (engagement, skepticism, specific questions). If interviewer name is unknown, ask.
5. Draft. One version first, tight. 4–7 sentences.
6. Offer a variant only if a shorter or more casual version is meaningfully different. Never offer a template alternative.

### Pre-Draft Check

Before writing, confirm:
- [ ] Recipient's first name is known (ask if not in state)
- [ ] At least one specific detail from the interaction is available (ask if not in debrief)
- [ ] Pronouns confirmed or defaulted correctly (see Guardrail 5)

Flag any gap explicitly before drafting. Never fill gaps with placeholders after the draft — surface them before.

### Output Schema

```markdown
## Draft: Follow-Up to [First Name] — [Company]

[Draft body — 4–7 sentences]

---

**Before sending:**
- [Any unknown details the candidate needs to fill in — e.g., "add the specific metric you mentioned"]

**Variant** (if meaningfully different): [optional]
```

---

## `draft [contact]` — Cold or Warm Outreach

### Logic

1. Read the contact record from `state/contacts.md` — name, company, role, pronouns, relationship strength, last touch.
2. Identify the connection angle: mutual contact, shared background, specific reason for reaching out.
3. If no contact record exists for this person, ask for: name, company, role, relationship (direct / 2nd degree / cold), and what the outreach is for.
4. Check pronouns field. If `unknown`, use first name only throughout the draft — no he/she/they. Do not infer pronouns from name. (See Guardrail 5.)
5. Calibrate tone to relationship strength: warm intro = warmer and brief; cold = more explicit on why you're reaching out, shorter.
6. Draft. One version first. 5–8 sentences for outreach.

### Outreach Types

| Type | Tone | Length | Anchor |
|------|------|--------|--------|
| Referral ask (warm) | Warm, direct | 5–6 sentences | Shared connection + specific ask |
| Referral ask (cold) | Professional, brief | 5–6 sentences | Why them, why now, specific ask |
| Coffee chat / intro | Warmer | 4–5 sentences | Genuine curiosity + specific reason |
| Follow-up after no response | Lighter | 3–4 sentences | Brief reference to first outreach |

### Output Schema

```markdown
## Draft: Outreach to [First Name] — [Company]

[Draft body]

---

**Before sending:**
- [Any details to confirm — mutual connection name, specific ask, etc.]

**Pronoun note** (if applicable): [first name only used — pronouns unknown. Confirm and update contact record when known.]
```

---

## `draft review [company]` — Feedback Request After Loop Closes

### When to Use

After a loop closes with a rejection — especially when you advanced multiple rounds and want real signal on where the gap was. Run it when the pipeline loop is closed with outcome: Lost.

This is not a second-chance email. It's a calibration tool. The goal is honest signal for your next search iteration, not reopening a closed door.

### Logic

1. Read the closed loop from `coaching_state.md` (Interview Loops section) and `state/pipeline.md` (Closed/Archived).
2. Identify the strongest moment from the loop — a specific conversation, story, or exchange that landed well (from debrief notes or score history). This becomes the anchor. A good anchor gives the reader something specific to respond to instead of an open-ended request they'll ignore.
3. Identify the likely decision point — which round had the weakest signal, what concern was most visible. This is for internal coaching use, not for the email. Don't self-diagnose in the email; ask for the information.
4. Draft the email using the structure below.

### Structure

**What the email must do:**
- Acknowledge the outcome with zero self-pity (one brief line max)
- Reference one specific moment from the process — something that felt genuine, that you both touched on, that signals you were paying attention
- Make the ask specific and easy to answer — not "any feedback?" but a concrete question they can say yes or no to, or answer in one sentence
- Lower the friction barrier — acknowledge they may not be able to share anything, and invite even a directional nudge

**What it must not do:**
- Sound like a rejection grievance or a second-chance request
- Be longer than 4–6 sentences
- Make the recipient feel obligated to write an essay

### The Core Ask

The most answerable question after a rejection is: **"Was there an area where my experience didn't match what you needed?"** Not "what did I do wrong?" — that's answering in defense. Not "can you share feedback?" — that's too open. The right question points at fit, not performance, which is both easier to answer and more useful information.

If the loop went multiple rounds, it's also legitimate to ask: "Was the gap at a specific point in the process, or more about overall fit?" — this tells you whether to fix execution or positioning.

### Output Schema

```markdown
## Draft: Feedback Request — [First Name] at [Company]

[Draft body — 4–6 sentences]

---

**Before sending:**
- [Any unknown details — first name, specific moment if not in debrief, correct recipient if multiple interviewers]

**Who to send this to:** [recommendation — the HM or most senior interviewer you spoke with, not the recruiter unless the recruiter was the only contact. Recruiters rarely have decision-level feedback.]

**Timing:** [Send 2–4 days after receiving the rejection — not same day, not 2 weeks later.]
```

### Golden Example

**Context:** Ramp loop closes (hypothetical). Candidate advanced 3 rounds. Sam Packard was the HM. The 90-day planning question was a specific exchange. Rejection received from recruiting.

**Output:**

```
## Draft: Feedback Request — Sam

Sam,

Thanks for the time and the thoughtful process — I found the conversation about 90-day planning
genuinely useful to think through. I'm in learning mode on this search, so I wanted to ask: was
there a specific area where my experience wasn't quite the match for what you were looking for?
Even a directional answer is helpful — I'm not looking for a detailed debrief if that's not
something you're able to share.

Appreciate anything you can offer.

Dhiraj

---

**Before sending:**
- Confirm Sam Packard is still the right contact (was he the final HM?)

**Who to send this to:** Sam Packard — HM level, more likely to have substantive feedback than the recruiter.

**Timing:** Send 2–3 days after receiving the rejection from Jocelyn.
```

**Why this works:** Specific anchor (90-day planning exchange), non-defensive ask ("wasn't quite the match"), clear opt-out clause, short enough to actually get read and answered.

---

### Logic

1. Ask what the communication is for: scheduling, status request, offer timing, declination, or other.
2. Read relevant pipeline entry if company is specified.
3. Draft based on type. Recruiter communication should be concise, professional, and specific about asks and timelines.

### Recruiter Communication Types

| Type | Tone | Key elements |
|------|------|--------------|
| Schedule confirmation | Professional | Confirm details, express interest |
| Status request | Direct, polite | Reference timeline, ask for update |
| Timeline extension ask | Professional | State reason briefly, request specific extension |
| Offer decline | Warm but firm | Appreciate the time, close cleanly |
| Response to rejection | Gracious | Thank, ask for feedback, leave door open |

---

## Guardrails

These apply to every draft, regardless of type.

**1. Draft only.** Output is text only. Never triggers a send action. The candidate controls the send.

**2. Never invent details.** If recipient's first name, what was discussed, or the specific moment that mattered isn't in debrief, coaching state, or contact record — ask before drafting, not after, not with placeholders. Gaps that surface before writing are useful; placeholders in a draft are a trap.

**3. Never require a transcript.** Debrief context is sufficient for a follow-up draft. Coaching state + pipeline context covers the baseline. If debrief wasn't run, ask for the one specific detail that should anchor the draft.

**4. Never use a template opener.** No "Thank you so much for taking the time to speak with me." No "I hope this message finds you well." These phrases are invisible to the reader. Start with something real.

**5. Never use gendered pronouns for a contact unless pronouns are confirmed in the contact record.** Use first name only when `Pronouns` field is `unknown`. Do not infer pronouns from a name. A name-only search does not return photos or pronoun fields — confirmation requires an explicit source (LinkedIn profile, the person stating them, or a confirmed field in the contact record). When unknown: "I spoke with [First Name]" not "I spoke with her" or "I spoke with him."

---

## What Makes a Good Draft

1. **Recipient addressed by first name** — not "Hi [Name]," not a formal title unless context requires it.
2. **One specific detail from the interaction** — the question they asked, the example you shared, the moment that landed. Generic follow-ups are invisible.
3. **One earned secret or concrete POV deployed** — not a restatement of the story. The coaching state contains these; use them.
4. **Short enough to send with zero editing** — if the candidate has to substantially rewrite it, the draft failed.
5. **Explicit flag on any unknown detail** — in a "Before sending:" block, not buried in the draft itself.

---

## Tone Calibration

The draft should sound like the candidate, not a template.

| Context | Tone |
|---------|------|
| Follow-up to finance-focused company | Direct, professional, specific |
| Follow-up after a warm conversation | Slightly warmer, still concise |
| Cold outreach to PM peer | Brief, genuine curiosity, specific reason |
| Recruiter reply | Efficient, professional |
| Declining an offer | Warm but firm, no hedging |

When in doubt: shorter and more direct beats longer and polished.

---

## Variants

Allowed, not default. Offer a variant only when a shorter or meaningfully different version serves a real purpose. Never offer a variant that's just a tone-softened version of the same draft — that's a quality problem to fix in the primary draft, not a variant.

When offering a variant: label it clearly ("If you want to be warmer:" or "Shorter version:") and keep it brief.

---

## Design Principles

**Context-first, template-never.** The coaching state, debrief, and contact record contain things no template can access: which story you told, what the interviewer pushed back on, what earned secret you deployed. The draft deploys that context. If the context isn't there, the draft waits until it is.

**Only assert what you can verify.** Pronouns, background details, motivations — never inferred from incomplete data. This includes gender. First name only when pronouns are unknown; confirm before updating the contact record. (See Guardrail 5.)

**Four to seven sentences.** This is a discipline, not a guideline. Long follow-up emails signal that you're compensating for a weak conversation. Short, specific ones signal confidence. If the draft is running long, find the one thing that matters most and cut the rest.

**The coaching layer feeds the draft layer.** Earned secrets, storybank stories, score history, debrief signals — all of this is draft material. A candidate who runs `debrief` and `stories` regularly will get dramatically better drafts than one who doesn't. Surface this connection explicitly when relevant.

---

## Golden Example

**Input context:** Candidate ran `debrief` after a Ramp HM call. Interviewer was Sam Packard. The candidate told the consortium story and Sam asked a follow-up about multi-party governance. Debrief notes: "Sam engaged most on the governance tension — asked a second question about how we handled disputes between contributors." Candidate wants a follow-up draft.

**Output:**

```
## Draft: Follow-Up to Sam — Ramp

Sam,

Really appreciated the conversation today. Your follow-up on multi-party governance was the question I enjoyed most — it gets at the part of the consortium problem that doesn't have a clean answer. The short version of what I've learned: in a shared network, the legal structure you build around the data isn't just compliance — it's the actual trust architecture. Getting that wrong kills adoption before you have enough signal to diagnose why.

I'd be curious to dig into how Ramp thinks about similar problems as the product scales across more customer types. Looking forward to next steps.

Dhiraj

---

**Before sending:**
- Confirm Sam's last name spelling if you want to use it (optional — first name alone is fine)
```

**Why this works:** Specific exchange anchored (governance question + follow-up), earned secret deployed from S001 (legal structure = trust architecture), no generic opener, short enough to send unchanged.
